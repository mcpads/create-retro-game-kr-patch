import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts import validate_docs


class DocumentationValidatorTest(unittest.TestCase):
    def collect_line(
        self, line: str, current_skill_path: str | None = None
    ) -> tuple[set[tuple[str, str]], int, list[str]]:
        with TemporaryDirectory() as directory:
            source = Path(directory) / "sample.md"
            source.write_text(f"{line}\n", encoding="utf-8")
            errors: list[str] = []
            with (
                patch.object(validate_docs, "markdown_files", return_value=[source]),
                patch.object(validate_docs, "repo_name", return_value="sample.md"),
                patch.object(
                    validate_docs,
                    "skill_name",
                    return_value=current_skill_path,
                ),
            ):
                section_uses, reference_count, _ = validate_docs.collect_references(
                    errors
                )
        return section_uses, reference_count, errors

    def validate_tip_fixture(self, body: str, judgment_area: str = "PoC") -> list[str]:
        with TemporaryDirectory() as directory:
            skill_root = Path(directory)
            tips = skill_root / "references" / "tips"
            general = tips / "general"
            general.mkdir(parents=True)
            (tips / "README.md").write_text(
                "| Index label | Strategy document |\n"
                "| PoC | `references/strategy/poc.md` |\n\n"
                "| Case | Judgment areas | Read when | First observed on | Reference |\n"
                f"| Proven rendering path | {judgment_area} | test | Game Gear | "
                "`references/tips/general/cases.md#proven-rendering-path` |\n",
                encoding="utf-8",
            )
            (general / "cases.md").write_text(
                f"# General cases\n\n## Proven rendering path\n\n{body}\n",
                encoding="utf-8",
            )
            errors: list[str] = []
            with (
                patch.object(validate_docs, "SKILL_ROOT", skill_root),
                patch.object(validate_docs, "TIPS_DIR", tips),
                patch.object(
                    validate_docs,
                    "repo_name",
                    side_effect=lambda path: path.name,
                ),
            ):
                validate_docs.validate_tips(errors)
        return errors

    def test_accepts_complete_reference_code_spans(self) -> None:
        samples = (
            "`references/strategy/poc.md` §1",
            "`references/strategy/poc.md`,",
            "`references/tips/platforms/nds.md#nftr-tags-and-cmap-order-follow-on-disk-consumer-semantics`",
            "`references/strategy/poc.md`. 다음 문장",
        )
        for sample in samples:
            with self.subTest(sample=sample):
                _, count, errors = self.collect_line(sample)
                self.assertEqual(count, 1)
                self.assertEqual(errors, [])

    def test_reports_malformed_reference_code_spans(self) -> None:
        samples = (
            "`references/strategy/poc.md-old`",
            "`references/strategy/poc.mdx`",
            "`references/strategy/poc.md.extra`",
            "`references/tips/platforms/nds.md#nftr-tags?broken`",
            "`references/tips/platforms/nds.md#nftr-tags/extra`",
            "`references/tips/platforms/nds.md#nftr-tags.`",
        )
        for sample in samples:
            with self.subTest(sample=sample):
                _, count, errors = self.collect_line(sample)
                self.assertEqual(count, 0)
                self.assertTrue(any("malformed reference" in error for error in errors))

    def test_reports_reference_outside_code_span(self) -> None:
        _, count, errors = self.collect_line("[PoC](references/strategy/poc.md)")
        self.assertEqual(count, 0)
        self.assertTrue(any("reference is not a code span" in error for error in errors))

    def test_reports_malformed_section_tokens(self) -> None:
        for token in ("§3oops", "§3..9"):
            with self.subTest(token=token):
                uses, _, errors = self.collect_line(
                    f"`references/strategy/poc.md` {token}"
                )
                self.assertEqual(uses, set())
                self.assertTrue(any("malformed section" in error for error in errors))

    def test_does_not_attach_section_across_sentence_boundary(self) -> None:
        uses, _, errors = self.collect_line(
            "`references/strategy/poc.md`. 다음 문장의 독립 포인터 §3"
        )
        self.assertEqual(uses, set())
        self.assertTrue(any("bare section reference" in error for error in errors))

    def test_attaches_sections_joined_by_english_conjunction(self) -> None:
        uses, _, errors = self.collect_line("`references/strategy/poc.md` §1 and §3")
        self.assertEqual(
            uses,
            {
                ("references/strategy/poc.md", "1"),
                ("references/strategy/poc.md", "3"),
            },
        )
        self.assertEqual(errors, [])

    def test_reports_ambiguous_section_after_explicit_reference(self) -> None:
        uses, _, errors = self.collect_line(
            "Use `references/strategy/runtime-assets.md` §1, then its §2.",
            current_skill_path="references/strategy/initial-survey.md",
        )
        self.assertEqual(
            uses,
            {("references/strategy/runtime-assets.md", "1")},
        )
        self.assertTrue(any("bare section reference" in error for error in errors))

    def test_allows_current_section_before_an_explicit_reference(self) -> None:
        uses, _, errors = self.collect_line(
            "Apply §3.1, then `references/strategy/runtime-assets.md` §2.",
            current_skill_path="references/strategy/translation-workflow.md",
        )
        self.assertEqual(
            uses,
            {
                ("references/strategy/translation-workflow.md", "3.1"),
                ("references/strategy/runtime-assets.md", "2"),
            },
        )
        self.assertEqual(errors, [])

    def test_section_target_requires_the_number_not_fixed_heading_wording(self) -> None:
        with TemporaryDirectory() as directory:
            skill_root = Path(directory)
            target = skill_root / "references" / "strategy" / "sample.md"
            target.parent.mkdir(parents=True)
            target.write_text("## 1. Current descriptive heading\n", encoding="utf-8")
            with (
                patch.object(validate_docs, "SKILL_ROOT", skill_root),
                patch.object(validate_docs, "repo_name", return_value="sample.md"),
            ):
                valid_errors: list[str] = []
                validate_docs.validate_section_targets(
                    {("references/strategy/sample.md", "1")}, valid_errors
                )
                missing_errors: list[str] = []
                validate_docs.validate_section_targets(
                    {("references/strategy/sample.md", "2")}, missing_errors
                )
        self.assertEqual(valid_errors, [])
        self.assertTrue(missing_errors)

    def test_reports_nonstandard_tip_heading(self) -> None:
        with TemporaryDirectory() as directory:
            tips = Path(directory)
            (tips / "README.md").write_text("# index\n", encoding="utf-8")
            (tips / "gg.md").write_text(
                "# Game Gear\n\n## GG-999\n", encoding="utf-8"
            )
            errors: list[str] = []
            with (
                patch.object(validate_docs, "TIPS_DIR", tips),
                patch.object(validate_docs, "repo_name", return_value="tips/gg.md"),
            ):
                validate_docs.validate_tips(errors)
        self.assertTrue(
            any("tip heading must describe the case" in error for error in errors)
        )

    def test_reports_tip_file_outside_case_roots(self) -> None:
        with TemporaryDirectory() as directory:
            tips = Path(directory)
            (tips / "README.md").write_text("# index\n", encoding="utf-8")
            (tips / "legacy.md").write_text(
                "# Legacy\n\n## Descriptive case heading\n", encoding="utf-8"
            )
            errors: list[str] = []
            with (
                patch.object(validate_docs, "SKILL_ROOT", tips.parent),
                patch.object(validate_docs, "TIPS_DIR", tips),
                patch.object(validate_docs, "repo_name", return_value="tips/legacy.md"),
            ):
                validate_docs.validate_tips(errors)
        self.assertTrue(any("tip case files must be under" in error for error in errors))

    def test_reports_missing_required_tip_field(self) -> None:
        errors = self.validate_tip_fixture(
            "\n".join(
                (
                    "- **Search terms:** test",
                    "- **Observed scope:** test",
                    "- **Failure context:** test",
                    "- **Decisive test:** test",
                    "- **Established result:** test",
                    "- **Related criteria:** `references/strategy/poc.md`.",
                )
            )
        )
        self.assertTrue(
            any("missing required field: Transfer limit" in error for error in errors)
        )

    def test_reports_missing_search_terms(self) -> None:
        errors = self.validate_tip_fixture(
            "\n".join(
                (
                    "- **Observed scope:** test",
                    "- **Decision context:** test",
                    "- **Evidence:** test",
                    "- **Established result:** test",
                    "- **Transfer limit:** test",
                    "- **Related criteria:** `references/strategy/poc.md`.",
                )
            )
        )
        self.assertTrue(
            any("missing required field: Search terms" in error for error in errors)
        )

    def test_reports_tip_route_mismatch(self) -> None:
        errors = self.validate_tip_fixture(
            "\n".join(
                (
                    "- **Search terms:** test",
                    "- **Observed scope:** test",
                    "- **Decision context:** test",
                    "- **Evidence:** test",
                    "- **Established result:** test",
                    "- **Transfer limit:** test",
                    "- **Related criteria:** `references/strategy/poc.md`.",
                )
            ),
            judgment_area="Initial survey",
        )
        self.assertTrue(any("tip route mismatch" in error for error in errors))

    def test_reports_hangul_in_agent_facing_guidance(self) -> None:
        with TemporaryDirectory() as directory:
            skill_root = Path(directory)
            skill_file = skill_root / "SKILL.md"
            skill_file.write_text("# Skill\n\n판정 규칙\n", encoding="utf-8")
            errors: list[str] = []
            with (
                patch.object(validate_docs, "SKILL_ROOT", skill_root),
                patch.object(
                    validate_docs,
                    "AGENT_ENGLISH_PATHS",
                    (skill_file,),
                ),
                patch.object(validate_docs, "AGENT_ENGLISH_LITERAL_PATHS", ()),
                patch.object(
                    validate_docs,
                    "repo_name",
                    return_value="skills/create-kr-patch/SKILL.md",
                ),
            ):
                validate_docs.validate_agent_facing_language(errors)
        self.assertTrue(any("must use English" in error for error in errors))

    def test_allows_source_script_in_core_document_code_span(self) -> None:
        with TemporaryDirectory() as directory:
            skill_root = Path(directory)
            skill_file = skill_root / "SKILL.md"
            skill_file.write_text("Source evidence: `한글`\n", encoding="utf-8")
            errors: list[str] = []
            with (
                patch.object(validate_docs, "SKILL_ROOT", skill_root),
                patch.object(
                    validate_docs,
                    "AGENT_ENGLISH_PATHS",
                    (skill_file,),
                ),
                patch.object(validate_docs, "AGENT_ENGLISH_LITERAL_PATHS", ()),
                patch.object(
                    validate_docs,
                    "repo_name",
                    return_value="skills/create-kr-patch/SKILL.md",
                ),
            ):
                validate_docs.validate_agent_facing_language(errors)
        self.assertEqual(errors, [])

    def test_allows_source_script_only_in_tip_code_spans(self) -> None:
        with TemporaryDirectory() as directory:
            tips = Path(directory)
            case = tips / "general" / "cases.md"
            case.parent.mkdir(parents=True)
            case.write_text("Literal `예` is evidence.\n", encoding="utf-8")
            errors: list[str] = []
            with (
                patch.object(validate_docs, "AGENT_ENGLISH_PATHS", ()),
                patch.object(
                    validate_docs,
                    "AGENT_ENGLISH_LITERAL_PATHS",
                    (tips,),
                ),
                patch.object(validate_docs, "repo_name", return_value="cases.md"),
            ):
                validate_docs.validate_agent_facing_language(errors)
        self.assertEqual(errors, [])

    def test_reports_hangul_tip_prose_outside_code_spans(self) -> None:
        with TemporaryDirectory() as directory:
            tips = Path(directory)
            case = tips / "general" / "cases.md"
            case.parent.mkdir(parents=True)
            case.write_text("한국어 지시 `예`\n", encoding="utf-8")
            errors: list[str] = []
            with (
                patch.object(validate_docs, "AGENT_ENGLISH_PATHS", ()),
                patch.object(
                    validate_docs,
                    "AGENT_ENGLISH_LITERAL_PATHS",
                    (tips,),
                ),
                patch.object(validate_docs, "repo_name", return_value="cases.md"),
            ):
                validate_docs.validate_agent_facing_language(errors)
        self.assertTrue(any("source-script evidence" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
