#!/usr/bin/env python3
"""Conformance and protocol tests for the patch-guard MCP server.

The accept/reject expectations mirror the language-neutral conformance manifests in
`mcpads/create-kr-patch-template` (`conformance/*.json`) and the SKILL.md core
invariants. Fixtures match the Rust reference harness so the two implementations judge
the same counter-examples identically.
"""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

_SERVER_PATH = Path(__file__).resolve().parents[1] / "mcp" / "patch_guard_mcp.py"
_spec = importlib.util.spec_from_file_location("patch_guard_mcp", _SERVER_PATH)
assert _spec is not None and _spec.loader is not None
pg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pg)

# SHA-256 of bytes [0, 1, 2, 3], shared by the source and roundtrip cases.
BASELINE_SHA256 = "054edec1d0211f624fed0cbca9d4f9400b0e491c43742af2c5b0abebf0c990d8"


def accepts(name, args):
    return pg.dispatch(name, args)["accept"]


def report(name, args):
    return pg.dispatch(name, args)["report"]


class VerifySourceTests(unittest.TestCase):
    def test_matching_identity_accepts(self):
        self.assertTrue(
            accepts(
                "verify_source",
                {
                    "id": "rom",
                    "expected_len": 4,
                    "expected_sha256": BASELINE_SHA256,
                    "bytes": [0, 1, 2, 3],
                },
            )
        )

    def test_byte_mismatch_rejects(self):
        self.assertFalse(
            accepts(
                "verify_source",
                {
                    "id": "rom",
                    "expected_len": 4,
                    "expected_sha256": BASELINE_SHA256,
                    "bytes": [0, 1, 2, 9],
                },
            )
        )


class RoundTripTests(unittest.TestCase):
    def test_identical_boundary_accepts(self):
        self.assertTrue(
            accepts(
                "verify_exact_roundtrip",
                {"boundary_id": "header", "original": [1, 2, 3], "rebuilt": [1, 2, 3]},
            )
        )

    def test_tail_diff_rejects(self):
        self.assertFalse(
            accepts(
                "verify_exact_roundtrip",
                {"boundary_id": "header", "original": [1, 2, 3], "rebuilt": [1, 2, 9]},
            )
        )

    def test_partial_boundary_rejects(self):
        self.assertFalse(
            accepts(
                "verify_exact_roundtrip",
                {"boundary_id": "header", "original": [1, 2, 3], "rebuilt": [1, 2]},
            )
        )


def _scope(units, approval, approved_revision):
    return {
        "id": "scope-1",
        "content_revision": "rev-1",
        "release_approval": approval,
        "approved_revision": approved_revision,
        "units": units,
    }


COMPLETE_UNIT = [{"id": "u1", "disposition": "use_localized", "review_state": "complete"}]


class ReadinessTests(unittest.TestCase):
    def test_development_preserves_incomplete(self):
        self.assertTrue(
            accepts(
                "evaluate_readiness",
                {
                    "mode": "development",
                    "scope": _scope(
                        [
                            {"id": "u1", "disposition": "use_localized", "review_state": "complete"},
                            {
                                "id": "u2",
                                "disposition": "preserve_source",
                                "review_state": "untranslated",
                            },
                        ],
                        "pending",
                        None,
                    ),
                },
            )
        )

    def test_release_incomplete_rejects(self):
        self.assertFalse(
            accepts(
                "evaluate_readiness",
                {
                    "mode": "release_candidate",
                    "scope": _scope(
                        [
                            {"id": "u1", "disposition": "use_localized", "review_state": "complete"},
                            {
                                "id": "u2",
                                "disposition": "preserve_source",
                                "review_state": "complete",
                            },
                        ],
                        "approved",
                        "rev-1",
                    ),
                },
            )
        )

    def test_release_unapproved_rejects(self):
        self.assertFalse(
            accepts(
                "evaluate_readiness",
                {"mode": "release_candidate", "scope": _scope(COMPLETE_UNIT, "pending", None)},
            )
        )

    def test_release_changed_after_approval_rejects(self):
        self.assertFalse(
            accepts(
                "evaluate_readiness",
                {
                    "mode": "release_candidate",
                    "scope": _scope(COMPLETE_UNIT, "approved", "rev-0"),
                },
            )
        )

    def test_release_complete_approved_accepts(self):
        result = report(
            "evaluate_readiness",
            {"mode": "release_candidate", "scope": _scope(COMPLETE_UNIT, "approved", "rev-1")},
        )
        self.assertEqual(result["release_candidate"], True)
        self.assertEqual(result["unresolved_units"], [])
        self.assertEqual(result["localized_units"], 1)


class ProductGraphTests(unittest.TestCase):
    def test_pure_source_accepts_with_execution_order(self):
        result = report(
            "validate_product_graph",
            {
                "roots": [{"id": "src", "kind": "pure_source"}],
                "steps": [
                    {"id": "b", "inputs": ["a"], "outputs": ["image"]},
                    {"id": "a", "inputs": ["src"], "outputs": ["a"]},
                ],
                "final_artifacts": ["image"],
            },
        )
        self.assertEqual(result["execution_order"], ["a", "b"])

    def test_research_output_rejects(self):
        self.assertFalse(
            accepts(
                "validate_product_graph",
                {
                    "roots": [{"id": "poc", "kind": "research_output"}],
                    "steps": [{"id": "s1", "inputs": ["poc"], "outputs": ["image"]}],
                    "final_artifacts": ["image"],
                },
            )
        )

    def test_duplicate_producer_rejects(self):
        self.assertFalse(
            accepts(
                "validate_product_graph",
                {
                    "roots": [{"id": "src", "kind": "pure_source"}],
                    "steps": [
                        {"id": "s1", "inputs": ["src"], "outputs": ["image"]},
                        {"id": "s2", "inputs": ["src"], "outputs": ["image"]},
                    ],
                    "final_artifacts": ["image"],
                },
            )
        )

    def test_dependency_cycle_rejects(self):
        self.assertFalse(
            accepts(
                "validate_product_graph",
                {
                    "roots": [{"id": "src", "kind": "pure_source"}],
                    "steps": [
                        {"id": "s1", "inputs": ["src", "b"], "outputs": ["a"]},
                        {"id": "s2", "inputs": ["a"], "outputs": ["b"]},
                    ],
                    "final_artifacts": ["a"],
                },
            )
        )

    def test_dead_step_rejects(self):
        self.assertFalse(
            accepts(
                "validate_product_graph",
                {
                    "roots": [{"id": "src", "kind": "pure_source"}],
                    "steps": [
                        {"id": "s1", "inputs": ["src"], "outputs": ["image"]},
                        {"id": "s2", "inputs": ["src"], "outputs": ["orphan"]},
                    ],
                    "final_artifacts": ["image"],
                },
            )
        )


def _artifact(ident, length, sha):
    return {"id": ident, "len": length, "sha256": sha}


class RuntimeEvidenceTests(unittest.TestCase):
    SHA = "a" * 64

    def test_passed_exact_artifact_accepts(self):
        self.assertTrue(
            accepts(
                "require_runtime_pass",
                {
                    "expected_artifact": _artifact("out.bin", 16, self.SHA),
                    "report": {
                        "schema_version": 1,
                        "scenario_id": "boot",
                        "artifact": _artifact("out.bin", 16, self.SHA),
                        "outcome": "passed",
                        "evidence": [_artifact("frame.png", 8, "b" * 64)],
                    },
                },
            )
        )

    def test_evidence_from_different_build_rejects(self):
        self.assertFalse(
            accepts(
                "require_runtime_pass",
                {
                    "expected_artifact": _artifact("out.bin", 16, self.SHA),
                    "report": {
                        "schema_version": 1,
                        "scenario_id": "boot",
                        "artifact": _artifact("out.bin", 16, "c" * 64),
                        "outcome": "passed",
                        "evidence": [_artifact("frame.png", 8, "b" * 64)],
                    },
                },
            )
        )

    def test_passed_without_evidence_rejects(self):
        self.assertFalse(
            accepts(
                "require_runtime_pass",
                {
                    "expected_artifact": _artifact("out.bin", 16, self.SHA),
                    "report": {
                        "schema_version": 1,
                        "scenario_id": "boot",
                        "artifact": _artifact("out.bin", 16, self.SHA),
                        "outcome": "passed",
                        "evidence": [],
                    },
                },
            )
        )

    def test_failed_scenario_rejects(self):
        self.assertFalse(
            accepts(
                "require_runtime_pass",
                {
                    "expected_artifact": _artifact("out.bin", 16, self.SHA),
                    "report": {
                        "schema_version": 1,
                        "scenario_id": "boot",
                        "artifact": _artifact("out.bin", 16, self.SHA),
                        "outcome": "failed",
                        "evidence": [_artifact("frame.png", 8, "b" * 64)],
                    },
                },
            )
        )


def _data_region():
    return {"id": "data", "start": 1, "end": 3, "kind": "data", "reason": "text pool"}


def _data_write():
    return {
        "id": "first",
        "actor": "layout",
        "purpose": "place",
        "offset": 1,
        "expected_original": [1, 2],
        "replacement": [8, 9],
        "intent": "data",
    }


class WritePlanTests(unittest.TestCase):
    def test_owned_data_write_accepts(self):
        result = report(
            "apply_write_plan",
            {"baseline": [0, 1, 2, 3], "regions": [_data_region()], "writes": [_data_write()]},
        )
        self.assertEqual(result["output"], [0, 8, 9, 3])
        self.assertEqual(len(result["output_sha256"]), 64)
        self.assertEqual(result["writes"][0]["region_id"], "data")
        self.assertEqual(result["writes"][0]["changed_bytes"], 2)

    def test_overlapping_writes_reject(self):
        second = _data_write()
        second.update({"id": "second", "offset": 2, "expected_original": [2], "replacement": [7]})
        self.assertFalse(
            accepts(
                "apply_write_plan",
                {
                    "baseline": [0, 1, 2, 3],
                    "regions": [
                        {"id": "data", "start": 0, "end": 4, "kind": "data", "reason": "pool"}
                    ],
                    "writes": [_data_write(), second],
                },
            )
        )

    def test_protected_region_write_rejects(self):
        self.assertFalse(
            accepts(
                "apply_write_plan",
                {
                    "baseline": [0, 1, 2, 3],
                    "regions": [
                        {"id": "data", "start": 1, "end": 3, "kind": "protected", "reason": "crc"}
                    ],
                    "writes": [_data_write()],
                },
            )
        )

    def test_wrong_original_bytes_rejects(self):
        wrong = _data_write()
        wrong["expected_original"] = [9, 9]
        self.assertFalse(
            accepts(
                "apply_write_plan",
                {"baseline": [0, 1, 2, 3], "regions": [_data_region()], "writes": [wrong]},
            )
        )

    def test_untracked_final_diff_via_audit(self):
        # Manually corrupt the produced output and re-audit through the internal path.
        baseline = bytes([0, 1, 2, 3])
        regions = [{"id": "data", "start": 1, "end": 3, "kind": "data", "reason": "pool"}]
        writes = [
            {
                "id": "first",
                "actor": "layout",
                "purpose": "place",
                "offset": 1,
                "expected_original": [1, 2],
                "replacement": [8, 9],
                "intent": "data",
                "machine_code": None,
            }
        ]
        ranges = pg._write_ranges(writes)
        corrupted = bytes([0, 8, 9, 9])
        with self.assertRaises(pg.Reject):
            pg._audit_write_plan(baseline, corrupted, None, regions, writes, ranges)

    def test_raw_data_in_machine_code_rejects(self):
        self.assertFalse(
            accepts(
                "apply_write_plan",
                {
                    "baseline": [0, 1, 2, 3],
                    "regions": [
                        {"id": "code", "start": 1, "end": 3, "kind": "machine_code", "reason": "hook"}
                    ],
                    "writes": [
                        {
                            "id": "x",
                            "actor": "layout",
                            "purpose": "place",
                            "offset": 1,
                            "expected_original": [1, 2],
                            "replacement": [8, 9],
                            "intent": "data",
                        }
                    ],
                },
            )
        )

    def test_machine_code_without_verifier_rejects(self):
        self.assertFalse(
            accepts(
                "apply_write_plan",
                {
                    "baseline": [0, 1, 2, 3],
                    "regions": [
                        {"id": "code", "start": 1, "end": 3, "kind": "machine_code", "reason": "hook"}
                    ],
                    "writes": [
                        {
                            "id": "hook",
                            "actor": "layout",
                            "purpose": "code-patch",
                            "offset": 1,
                            "expected_original": [1, 2],
                            "replacement": [170, 187],
                            "intent": "machine_code",
                            "machine_code": {
                                "assembly_source_id": "asm/hook.s",
                                "isa_profile_id": "isa-v1",
                            },
                        }
                    ],
                },
            )
        )

    def test_resize_growth_requires_ownership(self):
        result = report(
            "apply_write_plan",
            {
                "baseline": [0, 1, 2, 3],
                "resize": {
                    "actor": "grow",
                    "purpose": "append",
                    "expected_input_len": 4,
                    "output_len": 6,
                },
                "regions": [{"id": "tail", "start": 4, "end": 6, "kind": "data", "reason": "new"}],
                "writes": [
                    {
                        "id": "append",
                        "actor": "grow",
                        "purpose": "append",
                        "offset": 4,
                        "expected_original": [],
                        "replacement": [5, 6],
                        "intent": "data",
                    }
                ],
            },
        )
        self.assertEqual(result["output_len"], 6)
        self.assertEqual(result["resize"]["input_len"], 4)


class InvalidArgumentTests(unittest.TestCase):
    def test_missing_field_raises_invalid_params(self):
        with self.assertRaises(pg.InvalidParams):
            pg.dispatch("verify_source", {"id": "rom"})

    def test_unknown_tool_raises(self):
        with self.assertRaises(pg.UnknownTool):
            pg.dispatch("does_not_exist", {})


class ProtocolTests(unittest.TestCase):
    def _call(self, request):
        return pg.handle_line(json.dumps(request))

    def test_initialize_advertises_tools(self):
        response = self._call(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {"protocolVersion": "2025-06-18"},
            }
        )
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["result"]["serverInfo"]["name"], "patch-guard")
        self.assertIn("tools", response["result"]["capabilities"])

    def test_initialized_notification_has_no_response(self):
        self.assertIsNone(
            pg.handle_line(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}))
        )

    def test_tools_list_returns_all_tools(self):
        response = self._call({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        names = {tool["name"] for tool in response["result"]["tools"]}
        self.assertEqual(names, set(pg.HANDLERS))
        for tool in response["result"]["tools"]:
            self.assertEqual(tool["inputSchema"]["type"], "object")

    def test_tools_call_structured_decision(self):
        response = self._call(
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "verify_exact_roundtrip",
                    "arguments": {"boundary_id": "h", "original": [1, 2, 3], "rebuilt": [1, 2, 9]},
                },
            }
        )
        self.assertFalse(response["result"]["isError"])
        self.assertEqual(response["result"]["structuredContent"]["decision"], "reject")

    def test_unknown_tool_reports_invalid_params(self):
        response = self._call(
            {
                "jsonrpc": "2.0",
                "id": 4,
                "method": "tools/call",
                "params": {"name": "no_such_tool", "arguments": {}},
            }
        )
        self.assertEqual(response["error"]["code"], -32602)

    def test_unknown_method_reports_method_not_found(self):
        response = self._call({"jsonrpc": "2.0", "id": 5, "method": "frobnicate"})
        self.assertEqual(response["error"]["code"], -32601)

    def test_malformed_json_reports_parse_error(self):
        response = pg.handle_line("{not json")
        self.assertEqual(response["error"]["code"], -32700)


if __name__ == "__main__":
    unittest.main()
