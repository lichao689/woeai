from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


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
