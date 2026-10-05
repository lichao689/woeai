from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


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
            "   PublicationsByYear\n"
            "\n"
            ".. include:: paper-notes/_fragments.rst\n",
            encoding="utf-8",
        )
        (root / "docs/source/_paper-notes-fragment.rst").write_text(
            "stale fragment\n", encoding="utf-8"
        )
        self.addCleanup(temp.cleanup)
        return temp

    def test_generated_fragments_only_link_available_artifacts(self) -> None:
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
        missing = next(row for row in diagnostics if row["publication_ref"] == "ref-missing-rtd")
        self.assertIn("docs/source/paper-notes/ref-missing-rtd.rst", missing["missing"])

    def write_registry(self, root: Path, records: list[dict] | None = None) -> list[dict]:
        if records is None:
            records = [{
                "id": "TEST1234",
                "type": "article-journal",
                "title": "Original paper title",
                "issued": {"date-parts": [[2026]]},
                "custom": {
                    "publication_ref": "ref-complete",
                    "research_family": "建筑结构抗风",
                    "subdirection": "数值风洞与湍动入流",
                    "order": 4,
                    "rtd": {
                        "status": "planned",
                        "kind": "full_paper",
                        "path": "docs/source/paper-notes/ref-complete.rst",
                        "public_title": "数值风洞 | Independent RTD label",
                        "order": 2,
                        "issues": [],
                        "evidence": {},
                    },
                    "wechat": {"selected": False, "status": "planned"},
                },
            }]
        target = root / "docs/data/publications.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")
        return records

    def test_registry_rtd_is_independent_of_wechat_selection_and_title(self) -> None:
        root = Path(self.make_repo().name)
        self.write_registry(root)
        with patch.object(self.artifacts, "parse_backlog_papers", side_effect=AssertionError("No backlog read")):
            artifacts = self.artifacts.load_artifacts(root)
            latest = self.artifacts.render_latest_paper_notes(root)

        self.assertEqual(len(artifacts), 1)
        self.assertEqual(artifacts[0].order, 2)
        self.assertIn("数值风洞 | Independent RTD label", latest)
        self.assertNotIn("Markdown Title", latest)
        self.assertTrue(artifacts[0].is_public_available)
        self.assertFalse(artifacts[0].is_public_complete)

    def test_registry_does_not_need_backlog_or_wechat_article(self) -> None:
        root = Path(self.make_repo().name)
        self.write_registry(root)
        (root / "wechat/backlog/selected-papers.yml").unlink()
        (root / "wechat/articles/draft-public-safe/ref-complete.md").unlink()

        self.assertEqual(len(self.artifacts.public_artifacts(root)), 1)
        self.assertIn("Independent RTD label", self.artifacts.render_paper_notes_area(root))

    def test_page_existence_never_means_verified_completion(self) -> None:
        root = Path(self.make_repo().name)
        legacy = self.artifacts.load_artifacts(root)[0]
        self.assertTrue(legacy.is_public_available)
        self.assertFalse(legacy.is_public_complete)
        self.write_registry(root)
        registered = self.artifacts.load_artifacts(root)[0]
        self.assertTrue(registered.is_public_available)
        self.assertFalse(registered.is_public_complete)
        summary = self.artifacts.summary(root)
        self.assertEqual(summary["public_available_count"], 1)
        self.assertEqual(summary["public_complete_count"], 0)
        self.assertFalse(summary["diagnostics"][0]["public_complete"])

    def test_completion_uses_current_workflow_evidence(self) -> None:
        root = Path(self.make_repo().name)
        records = self.write_registry(root)
        artifact = self.artifacts.load_artifacts(root)[0]
        with patch.object(self.artifacts, "workflow_verified", side_effect=[True, False]) as verify:
            self.assertTrue(artifact.is_public_complete)
            self.assertFalse(artifact.is_public_complete)
        self.assertEqual(verify.call_count, 2)
        verify.assert_called_with(records[0], "rtd", root)

    def test_completed_status_without_proof_is_not_complete(self) -> None:
        root = Path(self.make_repo().name)
        records = self.write_registry(root)
        records[0]["custom"]["rtd"]["status"] = "verified"
        self.write_registry(root, records)
        self.assertFalse(self.artifacts.load_artifacts(root)[0].is_public_complete)

    def test_output_changes_invalidate_completion_without_removing_links(self) -> None:
        from woeai.publications.registry import workflow_fingerprint

        root = Path(self.make_repo().name)
        records = self.write_registry(root)
        record = records[0]
        record["custom"]["source"] = {"status": "verified", "sha256": "a" * 64}
        rtd = record["custom"]["rtd"]
        rtd["status"] = "verified"
        rtd["evidence"] = {"verified": {
            "recorded_at": "2026-10-05T03:00:00Z",
            "review_path": "wechat/articles/review/ref-complete.review.md",
            "checks": {"source_identity": True, "full_paper_coverage": True, "public_safety": True},
        }}
        rtd["evidence"]["verified"]["fingerprint"] = workflow_fingerprint(record, "rtd", root)
        self.write_registry(root, records)
        artifact = self.artifacts.load_artifacts(root)[0]
        self.assertTrue(artifact.is_public_complete)

        artifact.rtd_path.write_text("Edited after audit\n==================\n", encoding="utf-8")
        self.assertFalse(artifact.is_public_complete)
        self.assertTrue(artifact.is_public_available)
        self.assertIn("paper-notes/ref-complete", self.artifacts.render_latest_paper_notes(root))

    def test_registry_title_falls_back_to_rtd_without_wechat(self) -> None:
        root = Path(self.make_repo().name)
        records = self.write_registry(root)
        del records[0]["custom"]["rtd"]["public_title"]
        self.write_registry(root, records)
        self.assertEqual(self.artifacts.load_artifacts(root)[0].title, "数值风洞 | RTD Title")

    def test_invalid_registry_does_not_silently_use_backlog(self) -> None:
        root = Path(self.make_repo().name)
        self.write_registry(root)
        (root / "docs/data/publications.json").write_text("invalid JSON", encoding="utf-8")
        with self.assertRaises((ValueError, RuntimeError)):
            self.artifacts.load_artifacts(root)

    def test_compact_wechat_title_wins_over_rtd_title_and_keeps_prefix(self) -> None:
        # The compact WeChat article H1 (a direction-prefix hook sentence) is
        # the canonical compact public label, preferred over the RTD page
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
        # The fragment no longer owns a top-level hidden toctree; the
        # Publications generator emits paper-note toctrees under each research
        # subdirection instead.
        self.assertNotIn(".. toctree::", fragment_text)
        self.assertNotIn("paper-notes/ref-complete", fragment_text)
        self.assertIn("Paper-note toctrees are emitted inside each Academic Outputs research", fragment_text)
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
