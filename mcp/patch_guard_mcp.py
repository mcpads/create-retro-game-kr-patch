#!/usr/bin/env python3
"""patch-guard MCP server — executable enforcement of the create-kr-patch invariants.

Language-neutral patch-guard judgments exposed as MCP tools over newline-delimited
JSON-RPC 2.0 on stdio. Every tool maps a JSON request onto one guard and returns an
accept/reject decision matching the same boundaries as the Rust reference library in
`mcpads/create-kr-patch-template` (`reference/rust/crates/patch-guard`). Malformed
arguments are reported separately as JSON-RPC invalid params so a caller can tell a bad
request from a rejected plan.

Pure Python 3 standard library: no build step, no third-party dependencies, so it ships
inside the plugin and starts with `python3 patch_guard_mcp.py`.
"""

from __future__ import annotations

import hashlib
import json
import sys
from typing import Any, Callable

PROTOCOL_VERSION = "2025-06-18"
SERVER_NAME = "patch-guard"
SERVER_VERSION = "1.0.0"

# JSON-RPC 2.0 error codes.
PARSE_ERROR = -32700
INVALID_REQUEST = -32600
METHOD_NOT_FOUND = -32601
INVALID_PARAMS = -32602
INTERNAL_ERROR = -32603


class InvalidParams(Exception):
    """The request arguments were structurally invalid; the guard never ran."""


class UnknownTool(Exception):
    """No tool matches the requested name."""


class Reject(Exception):
    """The guard ran to a decision and rejected the input."""


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# --------------------------------------------------------------------------- #
# Argument parsing helpers (structural failures -> InvalidParams).
# --------------------------------------------------------------------------- #
def _text(obj: dict[str, Any], key: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str):
        raise InvalidParams(f"`{key}` must be a string")
    return value


def _opt_text(obj: dict[str, Any], key: str) -> str | None:
    value = obj.get(key)
    if value is None:
        return None
    if not isinstance(value, str):
        raise InvalidParams(f"`{key}` must be a string or null")
    return value


def _uint(obj: dict[str, Any], key: str) -> int:
    value = obj.get(key)
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise InvalidParams(f"`{key}` must be a non-negative integer")
    return value


def _object(obj: dict[str, Any], key: str) -> dict[str, Any]:
    value = obj.get(key)
    if not isinstance(value, dict):
        raise InvalidParams(f"`{key}` must be an object")
    return value


def _array(obj: dict[str, Any], key: str) -> list[Any]:
    value = obj.get(key)
    if not isinstance(value, list):
        raise InvalidParams(f"`{key}` must be an array")
    return value


def _byte_vec(obj: dict[str, Any], key: str) -> list[int]:
    result: list[int] = []
    for item in _array(obj, key):
        if not isinstance(item, int) or isinstance(item, bool):
            raise InvalidParams(f"`{key}` contains a non-integer byte")
        if item < 0 or item > 255:
            raise InvalidParams(f"`{key}` byte {item} is out of range 0..=255")
        result.append(item)
    return result


def _string_vec(obj: dict[str, Any], key: str) -> list[str]:
    result: list[str] = []
    for item in _array(obj, key):
        if not isinstance(item, str):
            raise InvalidParams(f"`{key}` must contain only strings")
        result.append(item)
    return result


def _enum(obj: dict[str, Any], key: str, allowed: dict[str, Any]) -> Any:
    raw = _text(obj, key)
    if raw not in allowed:
        options = ", ".join(allowed)
        raise InvalidParams(f"`{key}` must be one of {options}, found `{raw}`")
    return allowed[raw]


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def _nonempty(label: str, value: str) -> None:
    _require(value.strip() != "", f"{label} is empty")


# --------------------------------------------------------------------------- #
# Guards.
# --------------------------------------------------------------------------- #
def verify_source(args: dict[str, Any]) -> dict[str, Any]:
    ident = _text(args, "id")
    expected_len = _uint(args, "expected_len")
    expected_sha256 = _text(args, "expected_sha256")
    data = bytes(_byte_vec(args, "bytes"))

    _nonempty("source id", ident)
    _require(
        len(data) == expected_len,
        f"source {ident} length mismatch: expected {expected_len}, found {len(data)}",
    )
    actual = sha256_hex(data)
    _require(
        actual == expected_sha256,
        f"source {ident} SHA-256 mismatch: expected {expected_sha256}, found {actual}",
    )
    return {"id": ident, "len": len(data), "sha256": actual}


def verify_exact_roundtrip(args: dict[str, Any]) -> dict[str, Any]:
    boundary_id = _text(args, "boundary_id")
    original = bytes(_byte_vec(args, "original"))
    rebuilt = bytes(_byte_vec(args, "rebuilt"))

    _nonempty("round-trip boundary id", boundary_id)
    _require(
        len(original) == len(rebuilt),
        f"round-trip boundary {boundary_id} length mismatch: "
        f"expected {len(original)}, found {len(rebuilt)}",
    )
    for offset, (expected, found) in enumerate(zip(original, rebuilt)):
        _require(
            expected == found,
            f"round-trip boundary {boundary_id} differs at offset 0x{offset:X}: "
            f"expected 0x{expected:02X}, found 0x{found:02X}",
        )
    return {"boundary_id": boundary_id, "len": len(original), "sha256": sha256_hex(original)}


_BUILD_MODE = {"development": "development", "release_candidate": "release_candidate"}
_DISPOSITION = {"preserve_source": "preserve_source", "use_localized": "use_localized"}
_REVIEW_STATE = {
    "untranslated": "untranslated",
    "draft": "draft",
    "needs_review": "needs_review",
    "needs_human_review": "needs_human_review",
    "complete": "complete",
}
_RELEASE_APPROVAL = {"pending": "pending", "approved": "approved", "rejected": "rejected"}


def evaluate_readiness(args: dict[str, Any]) -> dict[str, Any]:
    mode = _enum(args, "mode", _BUILD_MODE)
    scope = _object(args, "scope")
    scope_id = _text(scope, "id")
    content_revision = _text(scope, "content_revision")
    release_approval = _enum(scope, "release_approval", _RELEASE_APPROVAL)
    approved_revision = _opt_text(scope, "approved_revision")
    units = _array(scope, "units")

    _nonempty("localization scope id", scope_id)
    _require(len(units) > 0, f"localization scope {scope_id} has no units")
    _nonempty(f"localization scope {scope_id} content revision", content_revision)

    seen: set[str] = set()
    localized_units = 0
    source_preserved_units = 0
    unresolved_units: list[str] = []
    for raw in units:
        if not isinstance(raw, dict):
            raise InvalidParams("`units` must contain objects")
        unit_id = _text(raw, "id")
        disposition = _enum(raw, "disposition", _DISPOSITION)
        review_state = _enum(raw, "review_state", _REVIEW_STATE)
        _nonempty("localization unit id", unit_id)
        _require(unit_id not in seen, f"duplicate localization unit id {unit_id}")
        seen.add(unit_id)
        _require(
            not (disposition == "use_localized" and review_state == "untranslated"),
            f"localization unit {unit_id} selects localized text but is untranslated",
        )
        if disposition == "preserve_source":
            source_preserved_units += 1
        else:
            localized_units += 1
        if not (disposition == "use_localized" and review_state == "complete"):
            unresolved_units.append(unit_id)

    if mode == "release_candidate":
        _require(
            release_approval == "approved",
            f"localization scope {scope_id} lacks release approval",
        )
        _require(
            approved_revision == content_revision,
            f"localization scope {scope_id} changed after release approval",
        )
        _require(
            not unresolved_units,
            f"release candidate scope {scope_id} has unresolved units: "
            + ", ".join(unresolved_units),
        )

    return {
        "scope_id": scope_id,
        "mode": mode,
        "release_candidate": mode == "release_candidate",
        "localized_units": localized_units,
        "source_preserved_units": source_preserved_units,
        "unresolved_units": unresolved_units,
    }


_ROOT_KIND = {
    "pure_source": "pure_source",
    "external_derived": "external_derived",
    "research_output": "research_output",
}


def validate_product_graph(args: dict[str, Any]) -> dict[str, Any]:
    roots_in = _array(args, "roots")
    steps_in = _array(args, "steps")
    final_artifacts = _string_vec(args, "final_artifacts")

    _require(len(steps_in) > 0, "product graph has no steps")
    _require(len(final_artifacts) > 0, "product graph has no final artifacts")

    roots: dict[str, str] = {}
    for raw in roots_in:
        if not isinstance(raw, dict):
            raise InvalidParams("`roots` must contain objects")
        root_id = _text(raw, "id")
        kind = _enum(raw, "kind", _ROOT_KIND)
        _nonempty("root artifact id", root_id)
        _require(root_id not in roots, f"duplicate root artifact id {root_id}")
        roots[root_id] = kind

    step_ids: set[str] = set()
    producers: dict[str, int] = {}
    steps: list[dict[str, Any]] = []
    for index, raw in enumerate(steps_in):
        if not isinstance(raw, dict):
            raise InvalidParams("`steps` must contain objects")
        step_id = _text(raw, "id")
        inputs = _string_vec(raw, "inputs")
        outputs = _string_vec(raw, "outputs")
        steps.append({"id": step_id, "inputs": inputs, "outputs": outputs})
        _nonempty("product step id", step_id)
        _require(step_id not in step_ids, f"duplicate product step id {step_id}")
        step_ids.add(step_id)
        _require(len(inputs) > 0, f"product step {step_id} has no inputs")
        _require(len(outputs) > 0, f"product step {step_id} has no outputs")
        _unique_values("input", step_id, inputs)
        _unique_values("output", step_id, outputs)
        for output in outputs:
            _nonempty("product artifact id", output)
            _require(output not in roots, f"product output {output} shadows a root artifact")
            _require(
                output not in producers,
                f"product artifact {output} has more than one producer",
            )
            producers[output] = index

    dependencies: list[set[int]] = [set() for _ in steps]
    dependents: list[set[int]] = [set() for _ in steps]
    for index, step in enumerate(steps):
        for source in step["inputs"]:
            _nonempty("product input id", source)
            if source in roots:
                kind = roots[source]
                if kind == "external_derived":
                    raise Reject(
                        f"product step {step['id']} consumes external derived artifact {source}"
                    )
                if kind == "research_output":
                    raise Reject(
                        f"product step {step['id']} consumes research or PoC output {source}"
                    )
            elif source in producers:
                producer = producers[source]
                dependencies[index].add(producer)
                dependents[producer].add(index)
            else:
                raise Reject(
                    f"product step {step['id']} consumes artifact {source} "
                    "with no source or producer"
                )

    final_producers: set[int] = set()
    final_ids: set[str] = set()
    for artifact in final_artifacts:
        _nonempty("final artifact id", artifact)
        _require(artifact not in final_ids, f"duplicate final artifact id {artifact}")
        final_ids.add(artifact)
        _require(
            artifact in producers,
            f"final artifact {artifact} is not produced by the product graph",
        )
        final_producers.add(producers[artifact])

    reachable = _reaching_finals(dependencies, final_producers)
    for index, step in enumerate(steps):
        _require(
            index in reachable,
            f"product step {step['id']} does not contribute to a final artifact",
        )

    indegree = [len(deps) for deps in dependencies]
    ready = sorted(
        ((steps[i]["id"], i) for i, deg in enumerate(indegree) if deg == 0)
    )
    order: list[str] = []
    while ready:
        _, index = ready.pop(0)
        order.append(steps[index]["id"])
        for dependent in dependents[index]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                ready.append((steps[dependent]["id"], dependent))
                ready.sort()
    _require(len(order) == len(steps), "product graph contains a dependency cycle")

    return {"execution_order": order, "final_artifacts": list(final_artifacts)}


def _unique_values(label: str, step: str, values: list[str]) -> None:
    seen: set[str] = set()
    for value in values:
        _require(value not in seen, f"product step {step} repeats {label} {value}")
        seen.add(value)


def _reaching_finals(dependencies: list[set[int]], finals: set[int]) -> set[int]:
    reachable = set(finals)
    pending = list(finals)
    while pending:
        step = pending.pop()
        for dependency in dependencies[step]:
            if dependency not in reachable:
                reachable.add(dependency)
                pending.append(dependency)
    return reachable


_RUNTIME_OUTCOME = {"passed": "passed", "failed": "failed"}


def _artifact(obj: dict[str, Any], key: str) -> dict[str, Any]:
    raw = _object(obj, key)
    return {"id": _text(raw, "id"), "len": _uint(raw, "len"), "sha256": _text(raw, "sha256")}


def _validate_artifact(label: str, artifact: dict[str, Any]) -> None:
    ident = artifact["id"]
    _require(ident.strip() != "", f"{label}: artifact id is empty")
    _require(artifact["len"] > 0, f"{label}: artifact {ident} is empty")
    sha = artifact["sha256"]
    _require(
        len(sha) == 64 and all(c in "0123456789abcdefABCDEF" for c in sha),
        f"{label}: artifact {ident} has an invalid SHA-256",
    )


def require_runtime_pass(args: dict[str, Any]) -> dict[str, Any]:
    expected = _artifact(args, "expected_artifact")
    report = _object(args, "report")
    schema_version = _uint(report, "schema_version")
    scenario_id = _text(report, "scenario_id")
    artifact = _artifact(report, "artifact")
    outcome = _enum(report, "outcome", _RUNTIME_OUTCOME)
    evidence_in = _array(report, "evidence")

    _require(
        schema_version == 1,
        f"unsupported runtime evidence schema version {schema_version}",
    )
    _require(scenario_id.strip() != "", "runtime scenario id is empty")
    _validate_artifact("expected runtime artifact", expected)
    _validate_artifact("runtime artifact", artifact)
    _require(artifact == expected, "runtime evidence targets a different build artifact")
    _require(outcome == "passed", f"runtime scenario {scenario_id} did not pass")
    _require(
        len(evidence_in) > 0,
        f"passed runtime scenario {scenario_id} has no evidence artifacts",
    )

    ids: set[str] = set()
    for raw in evidence_in:
        if not isinstance(raw, dict):
            raise InvalidParams("`evidence` must contain objects")
        item = {"id": _text(raw, "id"), "len": _uint(raw, "len"), "sha256": _text(raw, "sha256")}
        _validate_artifact("runtime evidence artifact", item)
        _require(
            item["id"] not in ids,
            f"duplicate runtime evidence artifact id {item['id']}",
        )
        ids.add(item["id"])

    return {"scenario_id": scenario_id, "outcome": "passed"}


_REGION_KIND = {
    "data": "data",
    "metadata": "metadata",
    "machine_code": "machine_code",
    "protected": "protected",
}
_WRITE_INTENT = {"data": "data", "metadata": "metadata", "machine_code": "machine_code"}


def apply_write_plan(args: dict[str, Any]) -> dict[str, Any]:
    baseline = bytes(_byte_vec(args, "baseline"))

    resize = None
    raw_resize = args.get("resize")
    if raw_resize is not None:
        if not isinstance(raw_resize, dict):
            raise InvalidParams("`resize` must be an object or null")
        resize = {
            "actor": _text(raw_resize, "actor"),
            "purpose": _text(raw_resize, "purpose"),
            "expected_input_len": _uint(raw_resize, "expected_input_len"),
            "output_len": _uint(raw_resize, "output_len"),
        }

    regions: list[dict[str, Any]] = []
    for raw in _array(args, "regions"):
        if not isinstance(raw, dict):
            raise InvalidParams("`regions` must contain objects")
        regions.append(
            {
                "id": _text(raw, "id"),
                "start": _uint(raw, "start"),
                "end": _uint(raw, "end"),
                "kind": _enum(raw, "kind", _REGION_KIND),
                "reason": _text(raw, "reason"),
            }
        )

    writes: list[dict[str, Any]] = []
    for raw in _array(args, "writes"):
        if not isinstance(raw, dict):
            raise InvalidParams("`writes` must contain objects")
        intent = _enum(raw, "intent", _WRITE_INTENT)
        machine_code = None
        if intent == "machine_code":
            provenance = _object(raw, "machine_code")
            machine_code = {
                "assembly_source_id": _text(provenance, "assembly_source_id"),
                "isa_profile_id": _text(provenance, "isa_profile_id"),
            }
        writes.append(
            {
                "id": _text(raw, "id"),
                "actor": _text(raw, "actor"),
                "purpose": _text(raw, "purpose"),
                "offset": _uint(raw, "offset"),
                "expected_original": _byte_vec(raw, "expected_original"),
                "replacement": _byte_vec(raw, "replacement"),
                "intent": intent,
                "machine_code": machine_code,
            }
        )

    validated = _validate_write_plan(baseline, resize, regions, writes)
    output_len = validated["output_len"]
    write_ranges = validated["write_ranges"]

    output = bytearray(baseline[: min(len(baseline), output_len)])
    output.extend(b"\x00" * (output_len - len(output)))
    for write, (start, end) in zip(writes, write_ranges):
        output[start:end] = bytes(write["replacement"])

    _audit_write_plan(baseline, bytes(output), resize, regions, writes, write_ranges)

    write_reports = []
    for write, region_index in zip(writes, validated["region_indices"]):
        write_reports.append(
            {
                "id": write["id"],
                "actor": write["actor"],
                "purpose": write["purpose"],
                "region_id": regions[region_index]["id"],
                "intent": write["intent"],
                "offset": write["offset"],
                "len": len(write["replacement"]),
                "changed_bytes": _changed_byte_count(baseline, write),
            }
        )

    resize_report = None
    if resize is not None:
        resize_report = {
            "actor": resize["actor"],
            "purpose": resize["purpose"],
            "input_len": resize["expected_input_len"],
            "output_len": resize["output_len"],
        }

    return {
        "output": list(output),
        "output_sha256": sha256_hex(bytes(output)),
        "output_len": len(output),
        "resize": resize_report,
        "writes": write_reports,
    }


def _intersects(left: tuple[int, int], right: tuple[int, int]) -> bool:
    return left[0] < right[1] and right[0] < left[1]


def _contains(outer: tuple[int, int], inner: tuple[int, int]) -> bool:
    return outer[0] <= inner[0] and inner[1] <= outer[1]


def _validate_write_plan(
    baseline: bytes,
    resize: dict[str, Any] | None,
    regions: list[dict[str, Any]],
    writes: list[dict[str, Any]],
) -> dict[str, Any]:
    if resize is not None:
        _nonempty("resize actor", resize["actor"])
        _nonempty("resize purpose", resize["purpose"])
        _require(
            resize["expected_input_len"] == len(baseline),
            "resize input length precondition failed",
        )
        _require(
            resize["output_len"] != len(baseline),
            "resize plan does not change the image length",
        )
        output_len = resize["output_len"]
    else:
        output_len = len(baseline)

    region_ids: set[str] = set()
    region_ranges: list[tuple[int, int]] = []
    for index, region in enumerate(regions):
        _nonempty("region id", region["id"])
        _nonempty("region reason", region["reason"])
        _require(region["id"] not in region_ids, f"duplicate region id {region['id']}")
        region_ids.add(region["id"])
        start, end = region["start"], region["end"]
        _require(
            start < end <= output_len,
            f"region {region['id']} is outside the planned output",
        )
        if region["kind"] == "protected":
            _require(
                end <= len(baseline),
                f"protected region {region['id']} is outside the original image",
            )
        for other_index in range(index):
            _require(
                not _intersects((start, end), region_ranges[other_index]),
                f"region {region['id']} overlaps {regions[other_index]['id']}",
            )
        region_ranges.append((start, end))

    write_ranges = _write_ranges(writes)
    write_ids: set[str] = set()
    region_indices: list[int] = []
    for index, (write, (start, end)) in enumerate(zip(writes, write_ranges)):
        _nonempty("write id", write["id"])
        _nonempty("write actor", write["actor"])
        _nonempty("write purpose", write["purpose"])
        _require(
            write["id"] not in write_ids,
            f"duplicate Expected Write id {write['id']}",
        )
        write_ids.add(write["id"])
        _require(
            end <= output_len,
            f"Expected Write {write['id']} is outside the planned output",
        )

        overlap_len = max(0, min(end, len(baseline)) - write["offset"])
        _require(
            len(write["expected_original"]) == overlap_len,
            f"Expected Write {write['id']} has {len(write['expected_original'])} "
            f"precondition bytes; {overlap_len} required",
        )
        offset = write["offset"]
        _require(
            list(baseline[offset : offset + overlap_len]) == write["expected_original"],
            f"Expected Write {write['id']} original-byte precondition failed",
        )

        for other_index in range(index):
            _require(
                not _intersects((start, end), write_ranges[other_index]),
                f"Expected Write {write['id']} by actor {write['actor']} overlaps "
                f"{writes[other_index]['id']} by actor {writes[other_index]['actor']}",
            )

        containing = [
            region_index
            for region_index, region_range in enumerate(region_ranges)
            if _contains(region_range, (start, end))
        ]
        _require(
            len(containing) == 1,
            f"Expected Write {write['id']} is not contained in exactly one declared region",
        )
        region_index = containing[0]
        region = regions[region_index]
        _require(
            region["kind"] != "protected",
            f"Expected Write {write['id']} intersects protected region {region['id']}",
        )
        _require(
            write["intent"] == region["kind"],
            f"Expected Write {write['id']} intent {write['intent']} does not match "
            f"region {region['id']} kind {region['kind']}",
        )

        if write["intent"] == "machine_code":
            provenance = write["machine_code"]
            _nonempty("assembly source id", provenance["assembly_source_id"])
            _nonempty("ISA profile id", provenance["isa_profile_id"])
            # No machine-code ISA verifier can cross the JSON boundary, so machine-code
            # writes always reject here, matching the `machine_code_without_verifier`
            # conformance case. A target project installs its verifier in-process.
            raise Reject(
                f"Expected Write {write['id']} targets machine code without a project verifier"
            )
        region_indices.append(region_index)

    if output_len > len(baseline):
        for offset in range(len(baseline), output_len):
            _require(
                any(start <= offset < end for (start, end) in write_ranges),
                f"grown output byte 0x{offset:X} has no Expected Write actor",
            )

    return {
        "output_len": output_len,
        "write_ranges": write_ranges,
        "region_indices": region_indices,
    }


def _write_ranges(writes: list[dict[str, Any]]) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for write in writes:
        _require(len(write["replacement"]) > 0, f"Expected Write {write['id']} is empty")
        ranges.append((write["offset"], write["offset"] + len(write["replacement"])))
    return ranges


def _audit_write_plan(
    baseline: bytes,
    output: bytes,
    resize: dict[str, Any] | None,
    regions: list[dict[str, Any]],
    writes: list[dict[str, Any]],
    write_ranges: list[tuple[int, int]],
) -> None:
    validated = _validate_write_plan(baseline, resize, regions, writes)
    _require(
        len(output) == validated["output_len"],
        "output length differs from the validated write plan",
    )
    for write, (start, end) in zip(writes, write_ranges):
        _require(
            list(output[start:end]) == write["replacement"],
            f"output does not contain the planned bytes for write {write['id']}",
        )
    for region in regions:
        if region["kind"] == "protected":
            start, end = region["start"], region["end"]
            _require(
                output[start:end] == baseline[start:end],
                f"protected region {region['id']} changed",
            )
    for offset in range(min(len(baseline), len(output))):
        if baseline[offset] != output[offset]:
            _require(
                any(start <= offset < end for (start, end) in write_ranges),
                f"untracked final diff at offset 0x{offset:X}",
            )


def _changed_byte_count(baseline: bytes, write: dict[str, Any]) -> int:
    count = 0
    for index, value in enumerate(write["replacement"]):
        position = write["offset"] + index
        original = baseline[position] if position < len(baseline) else None
        if original != value:
            count += 1
    return count


# --------------------------------------------------------------------------- #
# Tool registry and schemas.
# --------------------------------------------------------------------------- #
HANDLERS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "verify_source": verify_source,
    "verify_exact_roundtrip": verify_exact_roundtrip,
    "evaluate_readiness": evaluate_readiness,
    "validate_product_graph": validate_product_graph,
    "require_runtime_pass": require_runtime_pass,
    "apply_write_plan": apply_write_plan,
}


def dispatch(name: str, args: dict[str, Any]) -> dict[str, Any]:
    """Run a tool, returning {"accept": bool, "report": dict}.

    Raises InvalidParams for malformed arguments and UnknownTool for a bad name.
    """
    handler = HANDLERS.get(name)
    if handler is None:
        raise UnknownTool(name)
    try:
        report = handler(args)
    except Reject as error:
        return {"accept": False, "report": {"reason": str(error)}}
    return {"accept": True, "report": report}


def _byte_array_schema() -> dict[str, Any]:
    return {"type": "array", "items": {"type": "integer", "minimum": 0, "maximum": 255}}


def _artifact_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "required": ["id", "len", "sha256"],
        "properties": {
            "id": {"type": "string"},
            "len": {"type": "integer", "minimum": 0},
            "sha256": {"type": "string"},
        },
    }


def tool_defs() -> list[dict[str, Any]]:
    byte_array = _byte_array_schema()
    artifact = _artifact_schema()
    return [
        {
            "name": "verify_source",
            "description": "Verify supplied bytes match a declared source identity (length and SHA-256).",
            "inputSchema": {
                "type": "object",
                "required": ["id", "expected_len", "expected_sha256", "bytes"],
                "properties": {
                    "id": {"type": "string"},
                    "expected_len": {"type": "integer", "minimum": 0},
                    "expected_sha256": {"type": "string"},
                    "bytes": byte_array,
                },
            },
        },
        {
            "name": "verify_exact_roundtrip",
            "description": "Require a decode/rebuild boundary to reproduce every byte it declared.",
            "inputSchema": {
                "type": "object",
                "required": ["boundary_id", "original", "rebuilt"],
                "properties": {
                    "boundary_id": {"type": "string"},
                    "original": byte_array,
                    "rebuilt": byte_array,
                },
            },
        },
        {
            "name": "evaluate_readiness",
            "description": "Judge a build mode against a localization scope; release candidates require completion and human approval.",
            "inputSchema": {
                "type": "object",
                "required": ["mode", "scope"],
                "properties": {
                    "mode": {"enum": ["development", "release_candidate"]},
                    "scope": {
                        "type": "object",
                        "required": ["id", "content_revision", "release_approval", "units"],
                        "properties": {
                            "id": {"type": "string"},
                            "content_revision": {"type": "string"},
                            "release_approval": {"enum": ["pending", "approved", "rejected"]},
                            "approved_revision": {"type": ["string", "null"]},
                            "units": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["id", "disposition", "review_state"],
                                    "properties": {
                                        "id": {"type": "string"},
                                        "disposition": {
                                            "enum": ["preserve_source", "use_localized"]
                                        },
                                        "review_state": {
                                            "enum": [
                                                "untranslated",
                                                "draft",
                                                "needs_review",
                                                "needs_human_review",
                                                "complete",
                                            ]
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "validate_product_graph",
            "description": "Validate that every final artifact is reproducible from pure sources through the registered product graph.",
            "inputSchema": {
                "type": "object",
                "required": ["roots", "steps", "final_artifacts"],
                "properties": {
                    "roots": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["id", "kind"],
                            "properties": {
                                "id": {"type": "string"},
                                "kind": {
                                    "enum": [
                                        "pure_source",
                                        "external_derived",
                                        "research_output",
                                    ]
                                },
                            },
                        },
                    },
                    "steps": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["id", "inputs", "outputs"],
                            "properties": {
                                "id": {"type": "string"},
                                "inputs": {"type": "array", "items": {"type": "string"}},
                                "outputs": {"type": "array", "items": {"type": "string"}},
                            },
                        },
                    },
                    "final_artifacts": {"type": "array", "items": {"type": "string"}},
                },
            },
        },
        {
            "name": "require_runtime_pass",
            "description": "Require passing runtime evidence bound to the exact build artifact hash being gated.",
            "inputSchema": {
                "type": "object",
                "required": ["expected_artifact", "report"],
                "properties": {
                    "expected_artifact": artifact,
                    "report": {
                        "type": "object",
                        "required": [
                            "schema_version",
                            "scenario_id",
                            "artifact",
                            "outcome",
                            "evidence",
                        ],
                        "properties": {
                            "schema_version": {"type": "integer", "minimum": 0},
                            "scenario_id": {"type": "string"},
                            "artifact": artifact,
                            "outcome": {"enum": ["passed", "failed"]},
                            "evidence": {"type": "array", "items": artifact},
                        },
                    },
                },
            },
        },
        {
            "name": "apply_write_plan",
            "description": "Apply and audit an Expected Write plan against a baseline image. Machine-code writes reject without an in-process ISA verifier.",
            "inputSchema": {
                "type": "object",
                "required": ["baseline", "regions", "writes"],
                "properties": {
                    "baseline": byte_array,
                    "resize": {
                        "type": ["object", "null"],
                        "required": ["actor", "purpose", "expected_input_len", "output_len"],
                        "properties": {
                            "actor": {"type": "string"},
                            "purpose": {"type": "string"},
                            "expected_input_len": {"type": "integer", "minimum": 0},
                            "output_len": {"type": "integer", "minimum": 0},
                        },
                    },
                    "regions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["id", "start", "end", "kind", "reason"],
                            "properties": {
                                "id": {"type": "string"},
                                "start": {"type": "integer", "minimum": 0},
                                "end": {"type": "integer", "minimum": 0},
                                "kind": {
                                    "enum": ["data", "metadata", "machine_code", "protected"]
                                },
                                "reason": {"type": "string"},
                            },
                        },
                    },
                    "writes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": [
                                "id",
                                "actor",
                                "purpose",
                                "offset",
                                "expected_original",
                                "replacement",
                                "intent",
                            ],
                            "properties": {
                                "id": {"type": "string"},
                                "actor": {"type": "string"},
                                "purpose": {"type": "string"},
                                "offset": {"type": "integer", "minimum": 0},
                                "expected_original": byte_array,
                                "replacement": byte_array,
                                "intent": {"enum": ["data", "metadata", "machine_code"]},
                                "machine_code": {
                                    "type": "object",
                                    "required": ["assembly_source_id", "isa_profile_id"],
                                    "properties": {
                                        "assembly_source_id": {"type": "string"},
                                        "isa_profile_id": {"type": "string"},
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    ]


# --------------------------------------------------------------------------- #
# MCP transport (newline-delimited JSON-RPC 2.0 on stdio).
# --------------------------------------------------------------------------- #
def _error_response(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


def _initialize_result(params: dict[str, Any]) -> dict[str, Any]:
    protocol_version = params.get("protocolVersion")
    if not isinstance(protocol_version, str):
        protocol_version = PROTOCOL_VERSION
    return {
        "protocolVersion": protocol_version,
        "capabilities": {"tools": {"listChanged": False}},
        "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "instructions": (
            'Language-neutral patch-guard judgments. Each tool returns '
            '{"decision":"accept"|"reject"}; a reject is a valid guard outcome, '
            "not a transport error."
        ),
    }


def _tools_call_result(params: dict[str, Any]) -> dict[str, Any]:
    name = params.get("name")
    if not isinstance(name, str):
        raise InvalidParams("`name` must be a string")
    arguments = params.get("arguments", {})
    if not isinstance(arguments, dict):
        raise InvalidParams("`arguments` must be an object")

    outcome = dispatch(name, arguments)
    decision = "accept" if outcome["accept"] else "reject"
    structured = {"decision": decision, "report": outcome["report"]}
    return {
        "content": [{"type": "text", "text": json.dumps(structured, indent=2, ensure_ascii=False)}],
        "structuredContent": structured,
        "isError": False,
    }


def handle_line(line: str) -> dict[str, Any] | None:
    """Handle one framed JSON-RPC message. Returns None for notifications."""
    try:
        request = json.loads(line)
    except json.JSONDecodeError as error:
        return _error_response(None, PARSE_ERROR, f"invalid JSON: {error}")
    if not isinstance(request, dict):
        return _error_response(None, INVALID_REQUEST, "request must be an object")

    method = request.get("method")
    request_id = request.get("id")
    is_notification = "id" not in request
    if not isinstance(method, str):
        return _error_response(request_id, INVALID_REQUEST, "missing method")

    params = request.get("params", {})
    if not isinstance(params, dict):
        params = {}

    if method in ("notifications/initialized", "notifications/cancelled"):
        return None

    try:
        if method == "initialize":
            result: dict[str, Any] = _initialize_result(params)
        elif method == "ping":
            result = {}
        elif method == "tools/list":
            result = {"tools": tool_defs()}
        elif method == "tools/call":
            result = _tools_call_result(params)
        elif is_notification:
            return None
        else:
            return _error_response(request_id, METHOD_NOT_FOUND, f"unknown method `{method}`")
    except InvalidParams as error:
        return _error_response(request_id, INVALID_PARAMS, str(error))
    except UnknownTool as error:
        return _error_response(request_id, INVALID_PARAMS, f"unknown tool `{error}`")

    if is_notification:
        return None
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def serve_stdio() -> int:
    for raw in sys.stdin:
        if raw.strip() == "":
            continue
        response = handle_line(raw)
        if response is not None:
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(serve_stdio())
