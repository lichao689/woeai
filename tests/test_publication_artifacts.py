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
            "    title: Backlog Title\n"
            "    research_family: 建筑结构抗风\n"
            "    subdirection: 数值风洞与湍动入流\n"
            "    original_year: 2026\n"
            "    wechat_status: ready_to_publish\n"
            "  - publication_ref: ref-missing-rtd\n"
            "    title: Missing RTD\n"
            "    research_family: 建筑结构抗风\n"
            "    subdirection: 数值风洞与湍动入流\n"
            "    original_year: 2025\n"
            "    wechat_status: drafting\n",
            encoding="utf-8",
        )
        (root / "wechat/articles/draft-public-safe/ref-complete.md").write_text("# Markdown Title\n", encoding="utf-8")
        (root / "wechat/articles/review/ref-complete.review.md").write_text("review\n", encoding="utf-8")
        (root / "docs/source/paper-notes/ref-complete.rst").write_text("RTD\n", encoding="utf-8")
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
        # The fragment owns the toctree + 论文解读 area; Publications.rst no
        # longer carries them inline.
        self.assertIn(".. toctree::", fragment_text)
        self.assertIn("   paper-notes/ref-complete", fragment_text)
        self.assertIn("论文解读 Paper Notes", fragment_text)
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


if __name__ == "__main__":
    unittest.main()
