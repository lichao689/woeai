from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools/publications/artifacts.py"


def load_artifacts_module():
    spec = importlib.util.spec_from_file_location("woeai_publication_artifacts_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load publication artifacts tool")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class PublicationArtifactsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.artifacts = load_artifacts_module()

    def make_repo(self) -> tempfile.TemporaryDirectory[str]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "wechat/backlog").mkdir(parents=True)
        (root / "wechat/articles/draft-public-safe").mkdir(parents=True)
        (root / "wechat/articles/review").mkdir(parents=True)
        (root / "docs/source/paper-notes").mkdir(parents=True)
        (root / "docs/source").mkdir(parents=True, exist_ok=True)

        (root / "wechat/backlog/selected-papers.yml").write_text(
            "items:\n"
            "  - publication_ref: ref-complete\n"
            "    title: 数值风洞 | Backlog Title\n"
            "    research_family: 建筑结构抗风\n"
            "    subdirection: 数值风洞与湍动入流\n"
            "    original_year: 2026\n"
            "    wechat_status: ready_to_publish\n"
            "  - publication_ref: ref-missing-rtd\n"
            "    title: 数值风洞 | Missing RTD\n"
            "    research_family: 建筑结构抗风\n"
            "    subdirection: 数值风洞与湍动入流\n"
            "    original_year: 2025\n"
            "    wechat_status: drafting\n",
            encoding="utf-8",
        )
        (root / "wechat/articles/draft-public-safe/ref-complete.md").write_text("# 数值风洞 | Markdown Title\n", encoding="utf-8")
        (root / "wechat/articles/review/ref-complete.review.md").write_text("review\n", encoding="utf-8")
        (root / "docs/source/paper-notes/ref-complete.rst").write_text("数值风洞 | RTD Title\n===================\n", encoding="utf-8")
        (root / "wechat/articles/draft-public-safe/ref-missing-rtd.md").write_text("# Missing RTD Title\n", encoding="utf-8")
        (root / "wechat/articles/review/ref-missing-rtd.review.md").write_text("review\n", encoding="utf-8")
        (root / "docs/source/index.rst").write_text(
            "最新学术进展 Latest Academic Progress\n"
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"
            ".. BEGIN GENERATED LATEST PAPER NOTES\n\n"
            "- stale\n\n"
            ".. END GENERATED LATEST PAPER NOTES\n",
            encoding="utf-8",
        )
        (root / "docs/source/Publications.rst").write_text(
            ".. toctree::\n"
            "   :hidden:\n\n"
            "   PublicationsByResearch\n"
            "\n"
            ".. include:: paper-notes/_fragments.rst\n",
            encoding="utf-8",
        )
        (root / "docs/source/_paper-notes-fragment.rst").write_text(
            "stale fragment\n", encoding="utf-8"
        )
        self.addCleanup(temp.cleanup)
        return temp

    def test_generated_fragments_only_publish_complete_artifacts(self) -> None:
        temp = self.make_repo()
        root = Path(temp.name)

        latest = self.artifacts.render_latest_paper_notes(root)
        area = self.artifacts.render_paper_notes_area(root)
        diagnostics = self.artifacts.artifact_diagnostics(root)

        self.assertIn("Markdown Title", latest)
        self.assertIn("paper-notes/ref-complete", latest)
        self.assertNotIn("ref-missing-rtd", latest)
        self.assertIn("建筑结构抗风", area)
        self.assertIn("数值风洞与湍动入流", area)
        self.assertEqual(diagnostics[0]["publication_ref"], "ref-missing-rtd")
        self.assertIn("docs/source/paper-notes/ref-missing-rtd.rst", diagnostics[0]["missing"])

    def test_compact_wechat_title_wins_over_rtd_title_and_keeps_prefix(self) -> None:
        # The compact WeChat article H1 (a direction-prefix hook sentence) is
        # the canonical fragment navigation label, preferred over the RTD page
        # title. Both are kept prefix-conformant so no redundant "论文精解"
        # suffix drifts back into the navigation list.
        temp = self.make_repo()
        root = Path(temp.name)
        (root / "docs/source/paper-notes/ref-complete.rst").write_text(
            "数值风洞 | RTD Deep-Dive Title\n"
            "=================================\n",
            encoding="utf-8",
        )

        latest = self.artifacts.render_latest_paper_notes(root)
        area = self.artifacts.render_paper_notes_area(root)

        # The compact article title wins over the RTD title.
        self.assertIn("数值风洞 | Markdown Title", latest)
        self.assertIn("数值风洞 | Markdown Title", area)
        self.assertNotIn("RTD Deep-Dive Title", latest)

    def test_load_artifacts_consumes_shared_backlog_records(self) -> None:
        temp = self.make_repo()
        root = Path(temp.name)
        (root / "wechat/backlog/selected-papers.yml").unlink()

        original_parser = self.artifacts.parse_backlog_papers
        self.artifacts.parse_backlog_papers = lambda _path: [
            self.artifacts.BacklogPaper(
                "ref-complete",
                "Shared Backlog Title",
                "建筑结构抗风",
                "数值风洞与湍动入流",
                2026,
                "",
                7,
            )
        ]
        try:
            artifacts = self.artifacts.load_artifacts(root)
        finally:
            self.artifacts.parse_backlog_papers = original_parser

        self.assertEqual(len(artifacts), 1)
        self.assertEqual(artifacts[0].publication_ref, "ref-complete")
        self.assertEqual(artifacts[0].order, 7)

    def test_write_regenerates_fragment_and_check_then_passes(self) -> None:
        temp = self.make_repo()
        root = Path(temp.name)

        with contextlib.redirect_stdout(io.StringIO()):
            write_result = self.artifacts.main(["--root", str(root), "--write"])
            check_result = self.artifacts.main(["--root", str(root), "--check"])

        index_text = (root / "docs/source/index.rst").read_text(encoding="utf-8")
        fragment_text = (root / "docs/source/_paper-notes-fragment.rst").read_text(encoding="utf-8")
        self.assertEqual(write_result, 0)
        self.assertEqual(check_result, 0)
        self.assertIn("- 2026 | 建筑结构抗风 / 数值风洞与湍动入流", index_text)
        # The fragment only holds the hidden toctree (论文精解 section removed;
        # deep-dive titles now appear inline in the Publications page).
        self.assertIn(".. toctree::", fragment_text)
        self.assertIn("   paper-notes/ref-complete", fragment_text)
        self.assertNotIn("论文精解", fragment_text)
        self.assertNotIn("stale", fragment_text)

    def test_check_fails_when_fragment_is_stale(self) -> None:
        temp = self.make_repo()
        root = Path(temp.name)

        with contextlib.redirect_stdout(io.StringIO()):
            result = self.artifacts.main(["--root", str(root), "--check"])

        self.assertEqual(result, 1)

    def test_public_complete_artifacts_must_use_known_research_mapping(self) -> None:
        temp = self.make_repo()
        root = Path(temp.name)
        backlog = root / "wechat/backlog/selected-papers.yml"
        backlog.write_text(
            backlog.read_text(encoding="utf-8").replace(
                "    subdirection: 数值风洞与湍动入流\n"
                "    original_year: 2025\n",
                "    subdirection: 未知方向\n"
                "    original_year: 2025\n",
            ),
            encoding="utf-8",
        )
        (root / "docs/source/paper-notes/ref-missing-rtd.rst").write_text("RTD\n", encoding="utf-8")

        problems = self.artifacts.artifact_integrity_problems(root)

        self.assertEqual(problems[0]["kind"], "unknown_subdirection")
        self.assertEqual(problems[0]["publication_ref"], "ref-missing-rtd")

    def test_paper_note_title_without_direction_prefix_is_flagged(self) -> None:
        # Regression guard: a 论文精解 navigation label that reads like a
        # table-of-contents entry (no "方向 |" prefix) must be caught, so it can
        # no longer drift into the fragment list unnoticed. The label comes from
        # the canonical compact article H1, so that is what must be malformed.
        temp = self.make_repo()
        root = Path(temp.name)
        (root / "wechat/articles/draft-public-safe/ref-complete.md").write_text(
            "# CIRFG 大气边界层 LES 入流湍流生成方法\n", encoding="utf-8"
        )

        problems = self.artifacts.artifact_integrity_problems(root)
        kinds = {p["kind"] for p in problems}

        self.assertIn("paper_note_title_missing_prefix", kinds)
        flagged = next(p for p in problems if p["kind"] == "paper_note_title_missing_prefix")
        self.assertEqual(flagged["publication_ref"], "ref-complete")
        self.assertEqual(flagged["research_family"], "建筑结构抗风")

    def test_paper_note_title_with_redundant_suffix_is_flagged(self) -> None:
        # The "论文精解" suffix is redundant (it already heads the section) and
        # must not appear at the end of any navigation label.
        temp = self.make_repo()
        root = Path(temp.name)
        (root / "wechat/articles/draft-public-safe/ref-complete.md").write_text(
            "# 数值风洞 | 把相关性写进入流湍流论文精解\n", encoding="utf-8"
        )

        problems = self.artifacts.artifact_integrity_problems(root)
        kinds = {p["kind"] for p in problems}

        self.assertIn("paper_note_title_redundant_suffix", kinds)

    def test_compliant_paper_note_titles_pass_integrity_check(self) -> None:
        # A prefix-conformant, suffix-free title must produce no title problems.
        temp = self.make_repo()
        root = Path(temp.name)

        problems = self.artifacts.artifact_integrity_problems(root)
        title_kinds = {
            "paper_note_title_missing_prefix",
            "paper_note_title_redundant_suffix",
        }
        self.assertFalse(title_kinds & {p["kind"] for p in problems})


if __name__ == "__main__":
    unittest.main()
