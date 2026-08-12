#!/usr/bin/env python3
"""Validate documentation pointers and the tips index."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "create-kr-patch"
TIPS_DIR = SKILL_ROOT / "references" / "tips"
REFERENCE_CANDIDATE_RE = re.compile(
    r"references/[^\s`),;:}\]|§<>]*\.md[^\s`),;:}\]|§<>]*"
)
CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
REFERENCE_RE = re.compile(
    r"references/[A-Za-z0-9_./-]+\.md(?:#[A-Za-z0-9_-]+)?"
)
SECTION_RE = re.compile(
    r"§(\d+(?:\.\d+)*)(?![A-Za-z0-9_]|[.](?!\s|$))"
)
NUMBERED_HEADING_RE = re.compile(
    r"^#{2,6}\s+(\d+(?:\.\d+)*)\.?\s+(.+?)\s*$"
)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
TIP_HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
LEGACY_TIP_ID_RE = re.compile(r"^[A-Z][A-Z0-9]*-\d{3}$")
TIP_INDEX_RE = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|.*?"
    r"`(references/tips/[A-Za-z0-9_./-]+\.md)#([A-Za-z0-9_-]+)`\s*\|"
)
TIP_ROUTE_MAPPING_RE = re.compile(
    r"^\|\s*([^|`]+?)\s*\|\s*"
    r"`(references/strategy/[A-Za-z0-9_.-]+\.md)`\s*\|"
)
TIP_FIELD_RE = re.compile(r"^- \*\*([^*:]+):\*\*")
TIP_STRATEGY_REFERENCE_RE = re.compile(
    r"`(references/strategy/[A-Za-z0-9_.-]+\.md)`"
)
TIP_CASE_ROOTS = {"general", "platforms"}
AGENT_ENGLISH_PATHS = (
    SKILL_ROOT / "SKILL.md",
    SKILL_ROOT / "references" / "strategy",
    SKILL_ROOT / "references" / "conventions",
    SKILL_ROOT / "references" / "platforms",
)
AGENT_ENGLISH_LITERAL_PATHS = (TIPS_DIR,)
HANGUL_RE = re.compile(r"[\uac00-\ud7a3]")

TIP_REQUIRED_FIELDS = {
    "Search terms": {"Search terms"},
    "Observed scope": {"Observed scope"},
    "Problem or decision context": {"Failure context", "Decision context"},
    "Evidence": {"Decisive test", "Evidence"},
    "Established result": {"Established result"},
    "Transfer limit": {"Transfer limit"},
    "Related criteria": {"Related criteria"},
}


def markdown_files() -> list[Path]:
    return sorted(REPO_ROOT.glob("*.md")) + sorted(SKILL_ROOT.rglob("*.md"))


def repo_name(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def skill_name(path: Path) -> str | None:
    try:
        return path.relative_to(SKILL_ROOT).as_posix()
    except ValueError:
        return None


def slugify_heading(title: str) -> str:
    title = re.sub(r"\s+#+\s*$", "", title.strip().lower())
    title = re.sub(r"[^\w\s-]", "", title, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", title).strip("-")


def find_sections(
    line: str, source: Path, line_no: int, errors: list[str]
) -> list[re.Match[str]]:
    sections: list[re.Match[str]] = []
    for marker in re.finditer("§", line):
        if line.startswith("§N", marker.start()):
            continue
        match = SECTION_RE.match(line, marker.start())
        if match:
            sections.append(match)
            continue
        token_match = re.match(r"§[^\s`),;:}\]|·]*", line[marker.start() :])
        token = token_match.group(0) if token_match else "§"
        errors.append(f"{repo_name(source)}:{line_no}: malformed section: {token}")
    return sections


def attached_sections(
    line: str, span_end: int, sections_by_start: dict[int, re.Match[str]]
) -> list[re.Match[str]]:
    attached: list[re.Match[str]] = []
    cursor = span_end
    while True:
        while cursor < len(line) and line[cursor].isspace():
            cursor += 1
        section = sections_by_start.get(cursor)
        if section is None:
            break
        attached.append(section)
        cursor = section.end()
        separator = re.match(r"\s*(?:·|,|와|과|및|and|or)\s*", line[cursor:])
        if separator is None:
            break
        next_cursor = cursor + separator.end()
        if next_cursor not in sections_by_start:
            break
        cursor = next_cursor
    return attached


def numbered_headings(path: Path, errors: list[str]) -> dict[str, str]:
    headings: dict[str, str] = {}
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = NUMBERED_HEADING_RE.match(line)
        if not match:
            continue
        section, title = match.groups()
        if section in headings:
            errors.append(f"{repo_name(path)}:{line_no}: duplicate section {section}")
        else:
            headings[section] = title
    return headings


def heading_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = slugify_heading(match.group(1))
        if not base:
            continue
        count = counts.get(base, 0)
        anchors.add(base if count == 0 else f"{base}-{count}")
        counts[base] = count + 1
    return anchors


def collect_references(
    errors: list[str],
) -> tuple[set[tuple[str, str]], int, int]:
    section_uses: set[tuple[str, str]] = set()
    explicit_reference_count = 0
    section_reference_count = 0
    anchor_cache: dict[Path, set[str]] = {}

    for source in markdown_files():
        current_skill_path = skill_name(source)
        for line_no, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            code_spans = list(CODE_SPAN_RE.finditer(line))
            reference_spans: list[tuple[re.Match[str], str]] = []
            for span in code_spans:
                candidate = span.group(1)
                if not candidate.startswith("references/") or ".md" not in candidate:
                    continue
                if "<" in candidate or ">" in candidate:
                    continue
                if REFERENCE_RE.fullmatch(candidate) is None:
                    errors.append(
                        f"{repo_name(source)}:{line_no}: malformed reference: {candidate}"
                    )
                    continue
                reference_spans.append((span, candidate))

            for candidate in REFERENCE_CANDIDATE_RE.finditer(line):
                if not any(
                    span.start(1) <= candidate.start() and candidate.end() <= span.end(1)
                    for span in code_spans
                ):
                    errors.append(
                        f"{repo_name(source)}:{line_no}: reference is not a code span: "
                        f"{candidate.group(0)}"
                    )

            sections = find_sections(line, source, line_no, errors)
            sections_by_start = {section.start(): section for section in sections}
            claimed_sections: set[int] = set()

            for span, raw_reference in reference_spans:
                attached = attached_sections(line, span.end(), sections_by_start)
                claimed_sections.update(section.start() for section in attached)

                explicit_reference_count += 1
                target_name, separator, anchor = raw_reference.partition("#")
                target = (SKILL_ROOT / target_name).resolve()
                for section_match in attached:
                    section_uses.add((target_name, section_match.group(1)))
                    section_reference_count += 1

                try:
                    target.relative_to(SKILL_ROOT.resolve())
                except ValueError:
                    errors.append(
                        f"{repo_name(source)}:{line_no}: reference escapes skill root: "
                        f"{target_name}"
                    )
                    continue

                if not target.is_file():
                    errors.append(
                        f"{repo_name(source)}:{line_no}: missing reference: {target_name}"
                    )
                    continue

                if separator:
                    anchors = anchor_cache.setdefault(target, heading_anchors(target))
                    if anchor not in anchors:
                        errors.append(
                            f"{repo_name(source)}:{line_no}: missing anchor "
                            f"{target_name}#{anchor}"
                        )

            for section_match in sections:
                if section_match.start() in claimed_sections:
                    continue
                if any(
                    span.end() < section_match.start() for span, _ in reference_spans
                ):
                    errors.append(
                        f"{repo_name(source)}:{line_no}: ambiguous bare section reference "
                        f"after explicit document reference: §{section_match.group(1)}"
                    )
                    continue
                if current_skill_path is None:
                    errors.append(
                        f"{repo_name(source)}:{line_no}: bare section reference outside skill: "
                        f"§{section_match.group(1)}"
                    )
                    continue
                section_uses.add((current_skill_path, section_match.group(1)))
                section_reference_count += 1

    return section_uses, explicit_reference_count, section_reference_count


def validate_section_targets(
    section_uses: set[tuple[str, str]], errors: list[str]
) -> None:
    heading_cache: dict[str, dict[str, str]] = {}
    for path, section in sorted(section_uses):
        target = SKILL_ROOT / path
        if not target.is_file():
            errors.append(f"missing section target file: {path}")
            continue
        headings = heading_cache.setdefault(path, numbered_headings(target, errors))
        if section not in headings:
            errors.append(f"{path}: missing referenced section §{section}")


def markdown_targets(targets: tuple[Path, ...]) -> list[Path]:
    paths: list[Path] = []
    for target in targets:
        if target.is_file():
            paths.append(target)
        elif target.is_dir():
            paths.extend(sorted(target.rglob("*.md")))
    return paths


def validate_agent_facing_language(errors: list[str]) -> None:
    for path in markdown_targets(AGENT_ENGLISH_PATHS):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            prose = CODE_SPAN_RE.sub("", line)
            if HANGUL_RE.search(prose):
                errors.append(
                    f"{repo_name(path)}:{line_no}: agent-facing guidance must use English"
                )
    for path in markdown_targets(AGENT_ENGLISH_LITERAL_PATHS):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            prose = CODE_SPAN_RE.sub("", line)
            if HANGUL_RE.search(prose):
                errors.append(
                    f"{repo_name(path)}:{line_no}: agent-facing guidance must use English; "
                    "preserve source-script evidence only in code spans"
                )



def validate_tips(errors: list[str]) -> int:
    actual: dict[str, str] = {}
    titles: dict[str, str] = {}
    bodies: dict[str, list[str]] = {}
    locations: dict[str, tuple[Path, int]] = {}
    for path in sorted(TIPS_DIR.rglob("*.md")):
        if path.name == "README.md":
            continue
        relative = path.relative_to(TIPS_DIR)
        if len(relative.parts) < 2 or relative.parts[0] not in TIP_CASE_ROOTS:
            errors.append(
                f"{repo_name(path)}: tip case files must be under "
                "references/tips/general/ or references/tips/platforms/"
            )
        current_tip: str | None = None
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.startswith("## "):
                if current_tip is not None:
                    bodies[current_tip].append(line)
                continue
            match = TIP_HEADING_RE.fullmatch(line)
            if not match:
                errors.append(
                    f"{repo_name(path)}:{line_no}: invalid tip heading: {line}"
                )
                current_tip = None
                continue
            title = match.group(1).strip()
            tip_key = slugify_heading(title)
            if not tip_key or LEGACY_TIP_ID_RE.fullmatch(title):
                errors.append(
                    f"{repo_name(path)}:{line_no}: tip heading must describe the case: "
                    f"{line}"
                )
                current_tip = None
                continue
            if tip_key in actual:
                errors.append(
                    f"{repo_name(path)}:{line_no}: duplicate tip anchor {tip_key}; "
                    f"first in {actual[tip_key]}"
                )
                current_tip = None
            else:
                actual[tip_key] = path.relative_to(SKILL_ROOT).as_posix()
                titles[tip_key] = title
                bodies[tip_key] = []
                locations[tip_key] = (path, line_no)
                current_tip = tip_key

    indexed: dict[str, tuple[str, str, str]] = {}
    strategy_labels: dict[str, str] = {}
    index_path = TIPS_DIR / "README.md"
    for line_no, line in enumerate(index_path.read_text(encoding="utf-8").splitlines(), 1):
        route_match = TIP_ROUTE_MAPPING_RE.match(line)
        if route_match is not None:
            label, strategy_reference = route_match.groups()
            if strategy_reference in strategy_labels:
                errors.append(
                    f"{repo_name(index_path)}:{line_no}: duplicate strategy route: "
                    f"{strategy_reference}"
                )
            else:
                strategy_labels[strategy_reference] = label.strip()

        match = TIP_INDEX_RE.match(line)
        if not match:
            continue
        title, judgment_area, target, anchor = match.groups()
        if anchor in indexed:
            errors.append(
                f"{repo_name(index_path)}:{line_no}: duplicate tip anchor {anchor}"
            )
        else:
            indexed[anchor] = (title.strip(), judgment_area.strip(), target)

    derived_areas: dict[str, str] = {}
    for tip_key, body in bodies.items():
        labels = {
            match.group(1)
            for line in body
            if (match := TIP_FIELD_RE.match(line)) is not None
        }
        path, line_no = locations[tip_key]
        for field, alternatives in TIP_REQUIRED_FIELDS.items():
            if labels.isdisjoint(alternatives):
                errors.append(
                    f"{repo_name(path)}:{line_no}: tip {titles[tip_key]} missing required field: "
                    f"{field}"
                )

        strategy_references: list[str] = []
        for line in body:
            if not line.startswith("- **Related criteria:**"):
                continue
            strategy_references.extend(TIP_STRATEGY_REFERENCE_RE.findall(line))

        route_labels: list[str] = []
        for reference in strategy_references:
            label = strategy_labels.get(reference)
            if label is None:
                errors.append(
                    f"{repo_name(path)}:{line_no}: tip {titles[tip_key]} uses an unregistered "
                    f"strategy route: {reference}"
                )
            elif label not in route_labels:
                route_labels.append(label)
        derived_areas[tip_key] = " / ".join(route_labels)

    for tip_key in sorted(actual.keys() - indexed.keys()):
        errors.append(f"tip missing from index: {titles[tip_key]} ({actual[tip_key]})")
    for tip_key in sorted(indexed.keys() - actual.keys()):
        errors.append(f"index points to missing tip: {tip_key}")
    for tip_key in sorted(actual.keys() & indexed.keys()):
        index_title, judgment_area, target = indexed[tip_key]
        if target != actual[tip_key] or index_title != titles[tip_key]:
            errors.append(
                f"tip index mismatch for {titles[tip_key]}: expected "
                f"{actual[tip_key]}#{tip_key}, found {target}#{tip_key} "
                f"with title {index_title}"
            )
        expected_area = derived_areas[tip_key]
        if judgment_area != expected_area:
            errors.append(
                f"tip route mismatch for {titles[tip_key]}: expected {expected_area}, "
                f"found {judgment_area}"
            )
    return len(actual)


def main() -> int:
    errors: list[str] = []
    section_uses, explicit_count, section_count = collect_references(errors)
    validate_section_targets(section_uses, errors)
    validate_agent_facing_language(errors)
    tip_count = validate_tips(errors)

    if errors:
        print("documentation validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "documentation validation passed: "
        f"references={explicit_count}, section_refs={section_count}, "
        f"section_targets={len(section_uses)}, tips={tip_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
