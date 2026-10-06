from __future__ import annotations

import importlib.util
import argparse
import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/update-publications-from-zotero.py"


def load_publication_script():
    spec = importlib.util.spec_from_file_location("update_publications_from_zotero", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load publication updater")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_item(extra: str | None, creators: list[dict[str, str]], bib: str) -> dict[str, object]:
    return {
        "key": "TEST1234",
        "data": {
            "extra": extra,
            "creators": creators,
            "publicationTitle": "Journal of Tests",
        },
        "bib": bib,
    }


class UpdatePublicationsFromZoteroTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.updater = load_publication_script()

    def make_registry_repo(self) -> tuple[Path, list[dict]]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "docs/data").mkdir(parents=True)
        (root / "docs/source/paper-notes").mkdir(parents=True)
        records = [{
            "id": "TEST1234",
            "type": "article-journal",
            "title": "Original metadata",
            "issued": {"date-parts": [[2026]]},
            "custom": {
                "publication_ref": "ref-example2026-JOT",
                "research_family": "建筑结构抗风",
                "subdirection": "数值风洞与湍动入流",
                "order": 0,
                "rtd": {
                    "status": "planned",
                    "kind": "full_paper",
                    "path": "docs/source/paper-notes/ref-example2026-JOT.rst",
                    "public_title": "数值风洞 | Registry RTD title",
                    "issues": [],
                    "evidence": {},
                },
                "wechat": {
                    "selected": False, "status": "planned",
                    "path": "wechat/articles/draft-public-safe/ref-example2026-JOT.md",
                    "issues": [], "evidence": {},
                },
            },
        }]
        records.append(copy.deepcopy(records[0]))
        records[1]["id"] = "RETAIN12"
        records[1]["custom"]["publication_ref"] = "ref-retained2026-JOT"
        records[1]["custom"]["rtd"]["path"] = "docs/source/paper-notes/ref-retained2026-JOT.rst"
        records[1]["custom"]["wechat"]["path"] = "wechat/articles/draft-public-safe/ref-retained2026-JOT.md"
        (root / "docs/data/publications.json").write_text(json.dumps(records), encoding="utf-8")
        (root / "docs/source/paper-notes/ref-example2026-JOT.rst").write_text(
            "RTD page title\n==============\n", encoding="utf-8"
        )
        return root, records

    def test_registry_research_map_precedes_compatibility_view(self) -> None:
        root, records = self.make_registry_repo()
        view = root / "docs/data/publication-research-map.json"
        view.write_text('{"items": {"STALE123": {}}}', encoding="utf-8")
        with patch.multiple(self.updater, ROOT=root, RESEARCH_MAP_PATH=view):
            mapping = self.updater.load_research_map()
        self.assertEqual(set(mapping), {record["id"] for record in records})
        self.assertEqual(mapping["TEST1234"]["research_family"], "建筑结构抗风")

    def test_registry_deep_dive_titles_need_only_available_rtd(self) -> None:
        root, _records = self.make_registry_repo()
        with patch.object(self.updater, "ROOT", root):
            titles = self.updater.load_deep_dive_titles()
        self.assertEqual(titles, {"TEST1234": ("ref-example2026-JOT", "Registry RTD title")})

    def test_registry_research_map_failure_does_not_fall_back(self) -> None:
        root, _records = self.make_registry_repo()
        (root / "docs/data/publications.json").write_text("invalid JSON", encoding="utf-8")
        with patch.object(self.updater, "ROOT", root):
            with self.assertRaises((RuntimeError, ValueError)):
                self.updater.load_research_map()

    def test_refresh_validation_rejects_unfetched_registry_records(self) -> None:
        root, _records = self.make_registry_repo()
        with patch.object(self.updater, "ROOT", root):
            mapping = self.updater.load_research_map()
        items = [{"key": "TEST1234", "data": {"title": "Refreshed", "date": "2026"}}]
        with self.assertRaisesRegex(self.updater.ZoteroError, "Incomplete Zotero refresh"):
            self.updater.validate_research_map(items, mapping)
        with self.assertRaises(self.updater.ZoteroError):
            self.updater.validate_research_map(items, {})

    def run_registry_refresh(self, root: Path, *, dry_run: bool, partial: bool = False,
                             corresponding_extra: str | None = None):
        items = [{
            "key": "TEST1234",
            "data": {
                "itemType": "journalArticle",
                "title": "Fresh Zotero metadata",
                "extra": corresponding_extra,
                "date": "2026-05-01",
                "publicationTitle": "Journal of Tests",
                "creators": [{"creatorType": "author", "firstName": "Chao", "lastName": "Li"}],
            },
            "anchor": "ref-example2026-JOT",
            "publication_number": 1,
        }]
        if not partial:
            items.append({
                "key": "RETAIN12",
                "data": {"title": "Original metadata"},
                "anchor": "ref-retained2026-JOT",
                "publication_number": 2,
            })
        with patch.multiple(
            self.updater,
            ROOT=root,
            PUBLICATIONS_PATH=root / "docs/source/Publications.rst",
            PUBLICATIONS_BY_YEAR_PATH=root / "docs/source/PublicationsByYear.rst",
            TEACHING_PATH=root / "docs/source/Teaching.rst",
            SNAPSHOT_PATH=root / "docs/data/snapshot.json",
            verify_style=lambda: None,
            fetch_publication_items=lambda: items,
            merge_old_anchors=lambda _items: {},
            build_publications_rst=lambda *_args: "Publications\n",
            build_publications_by_year_rst=lambda *_args: "By year\n",
            snapshot=lambda *_args: {"items": []},
            fetch_teaching_reform_items=lambda: [],
            build_teaching_rst=lambda *_args: "Teaching\n",
        ), patch.object(
            self.updater, "write_views", wraps=self.updater.write_views
        ) as write_views, contextlib.redirect_stdout(io.StringIO()):
            self.updater.write_outputs(argparse.Namespace(dry_run=dry_run))
        return write_views

    def test_complete_refresh_preserves_workflow_and_all_records(self) -> None:
        root, records = self.make_registry_repo()
        write_views = self.run_registry_refresh(root, dry_run=False)
        updated = self.updater.load_registry(root)
        by_key = {record["id"]: record for record in updated}
        self.assertEqual(set(by_key), {"TEST1234", "RETAIN12"})
        self.assertEqual(by_key["TEST1234"]["title"], "Fresh Zotero metadata")
        self.assertEqual(by_key["TEST1234"]["custom"], records[0]["custom"])
        self.assertEqual(by_key["RETAIN12"], records[1])
        write_views.assert_called_once_with(root, updated)

    def test_partial_refresh_leaves_registry_pages_snapshot_and_views_unchanged(self) -> None:
        root, _records = self.make_registry_repo()
        for name in (
            "docs/source/Publications.rst", "docs/source/PublicationsByYear.rst",
            "docs/source/Teaching.rst", "docs/data/snapshot.json",
            "docs/data/publication-research-map.json", "wechat/backlog/selected-papers.yml",
            "project/publication-progress.md",
        ):
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"Existing content: {name}\n", encoding="utf-8")
        before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
        with patch.object(self.updater, "save_registry") as save_registry:
            with self.assertRaisesRegex(self.updater.ZoteroError, "Incomplete Zotero refresh.*"):
                self.run_registry_refresh(root, dry_run=False, partial=True)
            save_registry.assert_not_called()
        after = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
        self.assertEqual(after, before)

    def test_pure_metadata_merge_still_preserves_unfetched_records(self) -> None:
        _root, records = self.make_registry_repo()
        merged = self.updater.merge_zotero_items(records, [{
            "key": "TEST1234", "data": {"title": "Updated metadata"},
        }])
        self.assertEqual(merged[0]["title"], "Updated metadata")
        self.assertEqual(merged[0]["custom"], records[0]["custom"])
        self.assertEqual(merged[1], records[1])
        self.assertEqual(records[0]["title"], "Original metadata")

    def test_refresh_dry_run_does_not_write_registry_or_views(self) -> None:
        root, _records = self.make_registry_repo()
        path = root / "docs/data/publications.json"
        before = path.read_bytes()
        write_views = self.run_registry_refresh(root, dry_run=True)
        self.assertEqual(path.read_bytes(), before)
        self.assertFalse((root / "docs/source/Publications.rst").exists())
        write_views.assert_not_called()

    def test_rejected_registry_does_not_partially_write_public_pages(self) -> None:
        root, _records = self.make_registry_repo()
        with patch.object(self.updater, "save_registry", side_effect=ValueError("Invalid registry")):
            with self.assertRaises(ValueError):
                self.run_registry_refresh(root, dry_run=False)
        self.assertFalse((root / "docs/source/Publications.rst").exists())
        self.assertFalse((root / "docs/source/PublicationsByYear.rst").exists())
        self.assertFalse((root / "docs/source/Teaching.rst").exists())

    def test_main_reports_registry_validation_failure_cleanly(self) -> None:
        errors = io.StringIO()
        with patch.object(self.updater.sys, "argv", [str(SCRIPT)]), patch.object(
            self.updater, "write_outputs", side_effect=ValueError("Invalid registry")
        ), contextlib.redirect_stderr(errors):
            self.assertEqual(self.updater.main(), 1)
        self.assertEqual(errors.getvalue(), "error: Invalid registry\n")

    def test_source_audit_conflict_stops_before_public_writes(self) -> None:
        for expected in (["Wang Xiaolu"], ["Li Chao", "Zhou Shengtao"]):
            for marker in ("_通讯作者", None):
                with self.subTest(expected=expected, marker=marker):
                    root, records = self.make_registry_repo()
                    records[0]["custom"]["bibliography_audit"] = {
                        "field": "corresponding_authors", "source_supported_value": expected,
                        "review_path": "wechat/articles/review/example.review.md",
                        "evidence_locator": "PDF file page 1, corresponding-author footnote",
                    }
                    (root / "docs/data/publications.json").write_text(json.dumps(records), encoding="utf-8")
                    for name in ("docs/source/Publications.rst", "docs/source/PublicationsByYear.rst",
                                 "docs/source/Teaching.rst", "docs/data/snapshot.json",
                                 "docs/data/publication-research-map.json", "wechat/backlog/selected-papers.yml",
                                 "project/publication-progress.md", "docs/_static/publication-board-data.json"):
                        path = root / name; path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(f"Existing content: {name}\n", encoding="utf-8")
                    before = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
                    with patch.object(self.updater, "save_registry") as save, patch.object(self.updater, "write_views") as views:
                        with self.assertRaisesRegex(ValueError, "TEST1234.*corresponding_authors.*PDF file page 1"):
                            self.run_registry_refresh(root, dry_run=False, corresponding_extra=marker)
                        save.assert_not_called(); views.assert_not_called()
                    self.assertEqual({p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}, before)

    def test_corresponding_author_tag_marks_group_leader(self) -> None:
        item = make_item(
            "🏷️ _通讯作者、Wind engineering",
            [
                {"firstName": "Lingwei", "lastName": "Chen", "creatorType": "author"},
                {"firstName": "Chao", "lastName": "Li", "creatorType": "author"},
            ],
            "Chen Lingwei; Li Chao, Example[J]. Journal of Tests, 2024.",
        )

        rendered = self.updater.rendered_entry(item, 1)

        self.assertIn(":student-first-author:`Chen Lingwei`; **Li Chao**\\*, Example[J]. **Journal of Tests**", rendered)
        self.assertEqual(self.updater.corresponding_author_display_names(item), ["Li Chao"])

    def test_explicit_corresponding_author_marks_named_author(self) -> None:
        item = make_item(
            "通讯作者: Gang Hu",
            [
                {"firstName": "Lingwei", "lastName": "Chen", "creatorType": "author"},
                {"firstName": "Chao", "lastName": "Li", "creatorType": "author"},
                {"firstName": "Gang", "lastName": "Hu", "creatorType": "author"},
            ],
            "Chen Lingwei; Li Chao; Hu Gang, Example[J]. Journal of Tests, 2024.",
        )

        rendered = self.updater.rendered_entry(item, 1)

        self.assertIn(":student-first-author:`Chen Lingwei`; **Li Chao**; Hu Gang\\*, Example[J]", rendered)
        self.assertEqual(self.updater.corresponding_author_display_names(item), ["Hu Gang"])

    def test_existing_star_is_not_duplicated(self) -> None:
        item = make_item(
            "🏷️ _通讯作者",
            [{"firstName": "Chao", "lastName": "Li", "creatorType": "author"}],
            "Li Chao*, Example[J]. Journal of Tests, 2024.",
        )

        rendered = self.updater.rendered_entry(item, 1)

        self.assertIn("**Li Chao**\\*, Example[J]", rendered)
        self.assertNotIn("\\*\\*", rendered)

    def test_degree_thesis_data_provides_student_author_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            thesis_data = Path(tmpdir) / "degree-theses.json"
            thesis_data.write_text(
                json.dumps(
                    {
                        "student_authors": [
                            {"name_cn": "何欣", "name_en": "He Xin", "aliases": ["Xin He"]},
                        ],
                        "theses": {
                            "phd": [
                                {
                                    "name_cn": "郑舜云",
                                    "name_en": "Zheng Shunyun",
                                    "aliases": ["Shunyun Zheng"],
                                    "date": "2024-11",
                                    "thesis_type": "博士学位论文",
                                    "title": "半潜式风机支撑结构的尺度优化及强度评估",
                                }
                            ],
                            "master": [
                                {
                                    "name_cn": "李超",
                                    "name_en": "Li Chao",
                                    "aliases": [],
                                    "date": "2023",
                                    "thesis_type": "硕士学位论文",
                                    "title": "基于气象资料统计的滨海城市微尺度风气候分析",
                                }
                            ],
                        },
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            original_path = self.updater.DEGREE_THESES_PATH
            self.updater.DEGREE_THESES_PATH = thesis_data
            self.updater.load_degree_thesis_data.cache_clear()
            self.updater.load_student_author_names.cache_clear()
            try:
                names = self.updater.load_student_author_names()
            finally:
                self.updater.DEGREE_THESES_PATH = original_path
                self.updater.load_degree_thesis_data.cache_clear()
                self.updater.load_student_author_names.cache_clear()

        self.assertIn(self.updater.normalize_author_name("Zheng Shunyun"), names)
        self.assertIn(self.updater.normalize_author_name("Shunyun Zheng"), names)
        self.assertIn(self.updater.normalize_author_name("He Xin"), names)
        self.assertIn(self.updater.normalize_author_name("李超"), names)
        self.assertNotIn(self.updater.normalize_author_name("Li Chao"), names)

    def test_student_training_section_is_sorted_by_graduation_date(self) -> None:
        section = self.updater.student_training_section()

        self.assertIn("2.1 博士生 PhD Students", section)
        self.assertIn("2.2 硕士生 Master Students", section)
        self.assertIn("周盛涛(Zhou Shengtao)，2021，博士学位论文：基于快速动力响应分析的半潜式风机下部结构主尺寸优化；去向：风电企业。", section)
        self.assertLess(section.index("周盛涛(Zhou Shengtao)，2021"), section.index("郑舜云(Zheng Shunyun)，2024-11"))
        self.assertLess(section.index("陈铃伟(Chen Lingwei)，2025-09"), section.index("何欣(He Xin)，在读"))
        self.assertIn("刘尚佩(Liu Shangpei)，在读", section)
        self.assertLess(section.index("王一鸣(Wang Yiming)，2023"), section.index("赵培升(Zhao Peisheng)，2025"))

    def test_page_header_matches_committed_publications_structure(self) -> None:
        """page_header must emit the current committed structure, not the stale
        'View Options'/'Selected Highlights' sections, so that regenerating
        Publications.rst does not clobber hand-curated content. The
        paper-notes top-level toctree is no longer emitted by the include
        fragment. The include remains as a no-op guard, while per-subdirection
        paper-note toctrees are emitted by build_publications_rst."""
        header = self.updater.page_header({})

        # The stale sections must not come back on regeneration.
        self.assertNotIn("浏览方式 View Options", header)
        self.assertNotIn("精选证据 Selected Highlights", header)
        # The current committed structure must be reproduced.
        self.assertIn(".. container:: publication-view-banner", header)
        self.assertIn("PublicationsByYear", header)
        self.assertNotIn("PublicationsBy" + "Research", header)
        self.assertIn(".. rubric:: 期刊论文 Journal Papers", header)
        self.assertNotIn("期刊论文 Journal Papers\n------------------------", header)
        # Paper-notes content lives in an artifacts-owned fragment.
        self.assertIn(".. include:: _paper-notes-fragment.rst", header)

    def test_deep_dive_link_text_includes_publication_year(self) -> None:
        item = make_item(
            None,
            [
                {"firstName": "Peisheng", "lastName": "Zhao", "creatorType": "author"},
                {"firstName": "Chao", "lastName": "Li", "creatorType": "author"},
            ],
            "Zhao Peisheng; Li Chao, Example[J]. Journal of Tests, 2026.",
        )
        item["data"]["date"] = "2026"
        item["key"] = "TEST1234"
        item["anchor"] = "ref-zhao2026-JOT"
        item["publication_number"] = 75

        original_loader = self.updater.load_deep_dive_titles
        self.updater.load_deep_dive_titles = lambda: {
            "TEST1234": ("ref-zhao2026-JOT", "如何把卫星影像转成 CFD 可用城市几何")
        }
        try:
            page = self.updater.build_publications_rst(
                [item],
                {
                    "TEST1234": {
                        "research_family": "建筑结构抗风",
                        "subdirection": "数值风洞与湍动入流",
                    }
                },
            )
        finally:
            self.updater.load_deep_dive_titles = original_loader

        self.assertIn(
            "[75] :doc:`2026 JOT | 如何把卫星影像转成 CFD 可用城市几何 <paper-notes/ref-zhao2026-JOT>`",
            page,
        )
        subdirection_index = page.index("\n数值风洞与湍动入流\n")
        toctree_index = page.index(".. toctree::", subdirection_index)
        entry_index = page.index("2026 JOT | 如何把卫星影像转成 CFD 可用城市几何 <paper-notes/ref-zhao2026-JOT>", toctree_index)
        citation_index = page.index("[75] :doc:`2026 JOT | 如何把卫星影像转成 CFD 可用城市几何", entry_index)
        self.assertLess(toctree_index, entry_index)
        self.assertLess(entry_index, citation_index)
        self.assertNotIn("[75] 2026 | :doc:", page)


if __name__ == "__main__":
    unittest.main()
