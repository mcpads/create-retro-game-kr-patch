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
            tips.mkdir(parents=True)
            (tips / "README.md").write_text(
                "| 색인 라벨 | 라우팅 판단 영역 | 문서 |\n"
                "| PoC | PoC | `references/strategy/poc.md` |\n\n"
                "| ID | 판단 영역 | 관측 플랫폼 | 발동 조건 | 사례 파일 |\n"
                f"| GG-999 | {judgment_area} | Game Gear | test | "
                "`references/tips/gg.md#gg-999` |\n",
                encoding="utf-8",
            )
            (tips / "gg.md").write_text(
                f"# Game Gear\n\n## GG-999\n\n{body}\n", encoding="utf-8"
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
            "`references/tips/nds.md#nds-001`",
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
            "`references/tips/nds.md#nds-001?broken`",
            "`references/tips/nds.md#nds-001/extra`",
            "`references/tips/nds.md#nds-001.`",
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

    def test_reports_nonstandard_tip_heading(self) -> None:
        with TemporaryDirectory() as directory:
            tips = Path(directory)
            (tips / "README.md").write_text("# index\n", encoding="utf-8")
            (tips / "gg.md").write_text(
                "# Game Gear\n\n## GG-999 설명\n", encoding="utf-8"
            )
            errors: list[str] = []
            with (
                patch.object(validate_docs, "TIPS_DIR", tips),
                patch.object(validate_docs, "repo_name", return_value="tips/gg.md"),
            ):
                validate_docs.validate_tips(errors)
        self.assertTrue(any("invalid tip heading" in error for error in errors))

    def test_reports_missing_required_tip_field(self) -> None:
        errors = self.validate_tip_fixture(
            "\n".join(
                (
                    "- **관측 범위:** test",
                    "- **사고 맥락:** test",
                    "- **결정 실험:** test",
                    "- **확정 결론:** test",
                    "- **관련 판단 기준:** `references/strategy/poc.md`.",
                )
            )
        )
        self.assertTrue(
            any("missing required field: 전이 한계" in error for error in errors)
        )

    def test_reports_tip_route_mismatch(self) -> None:
        errors = self.validate_tip_fixture(
            "\n".join(
                (
                    "- **관측 범위:** test",
                    "- **선택 맥락:** test",
                    "- **검증 근거:** test",
                    "- **확정 결과:** test",
                    "- **전이 한계:** test",
                    "- **관련 판단 기준:** `references/strategy/poc.md`.",
                )
            ),
            judgment_area="초기 조사",
        )
        self.assertTrue(any("tip route mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
