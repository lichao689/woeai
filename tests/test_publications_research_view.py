from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS = ROOT / "docs/source/Publications.rst"
PUBLICATIONS_BY_RESEARCH = ROOT / "docs/source/PublicationsByResearch.rst"
INDEX = ROOT / "docs/source/index.rst"
RESEARCH_MAP = ROOT / "docs/data/publication-research-map.json"

RESEARCH_FAMILIES = ("建筑结构抗风", "海上漂浮风电")
RESEARCH_STRUCTURE = {
    "建筑结构抗风": ("数值风洞与湍动入流", "高层建筑抗风与优化"),
    "海上漂浮风电": ("浮式风机系统一体化分析与优化", "浮式混凝土平台结构设计", "数值风浪流水池"),
}


def publication_anchors(text: str) -> set[str]:
    return set(re.findall(r"^\.\. _(ref-[^:]+):$", text, flags=re.M))


def research_ref_targets(text: str) -> list[str]:
    return re.findall(r":ref:`[^`<]+ <(ref-[^>]+)>`", text)


def section_between(text: str, title: str, next_titles: tuple[str, ...]) -> str:
    start = text.index(f"\n{title}\n")
    following = [text.index(f"\n{next_title}\n", start + 1) for next_title in next_titles if f"\n{next_title}\n" in text[start + 1 :]]
    end = min(following) if following else len(text)
    return text[start:end]


class PublicationsResearchViewTests(unittest.TestCase):
    def test_publications_page_links_to_research_view(self) -> None:
        text = PUBLICATIONS.read_text(encoding="utf-8")
        index_text = INDEX.read_text(encoding="utf-8")

        self.assertIn("浏览方式 View Options", text)
        self.assertIn(":doc:`PublicationsByResearch`", text)
        self.assertIn("按研究方向浏览 Publications by Research Direction <PublicationsByResearch>", text)
        self.assertNotIn("\n   PublicationsByResearch\n", index_text)

    def test_research_view_groups_every_publication_by_family_then_subdirection(self) -> None:
        publications_text = PUBLICATIONS.read_text(encoding="utf-8")
        research_text = PUBLICATIONS_BY_RESEARCH.read_text(encoding="utf-8")

        source_anchors = publication_anchors(publications_text)
        linked_anchors = research_ref_targets(research_text)
        self.assertEqual(set(linked_anchors), source_anchors)
        self.assertEqual(len(linked_anchors), len(source_anchors))

        family_positions = [research_text.index(f"\n{family}\n") for family in RESEARCH_FAMILIES]
        self.assertEqual(family_positions, sorted(family_positions))

        for family, subdirections in RESEARCH_STRUCTURE.items():
            other_families = tuple(candidate for candidate in RESEARCH_FAMILIES if candidate != family)
            family_section = section_between(research_text, family, other_families)
            subdirection_positions = [family_section.index(f"\n{subdirection}\n") for subdirection in subdirections]
            self.assertEqual(subdirection_positions, sorted(subdirection_positions), family)
            self.assertNotRegex(family_section, r"^\d{4}$", family)

            for index, subdirection in enumerate(subdirections):
                next_subdirections = subdirections[index + 1 :]
                subdirection_section = section_between(family_section, subdirection, next_subdirections)
                years = [int(year) for year in re.findall(r"^- \((\d{4})\) ", subdirection_section, flags=re.M)]
                self.assertEqual(years, sorted(years, reverse=True), subdirection)

    def test_research_view_is_a_short_index_not_a_duplicate_bibliography(self) -> None:
        text = PUBLICATIONS_BY_RESEARCH.read_text(encoding="utf-8")

        self.assertNotIn("https://doi.org/", text)
        self.assertNotIn("影响因子:", text)
        self.assertNotIn("中科院分区:", text)
        self.assertNotIn("引用次数:", text)

    def test_research_mapping_uses_canonical_public_families(self) -> None:
        mapping = json.loads(RESEARCH_MAP.read_text(encoding="utf-8"))
        items = mapping["items"]
        source_anchors = publication_anchors(PUBLICATIONS.read_text(encoding="utf-8"))
        self.assertEqual(len(items), len(source_anchors))

        families = {row["research_family"] for row in items.values()}
        self.assertEqual(families, set(RESEARCH_FAMILIES))

        for key, row in items.items():
            self.assertRegex(key, r"^[A-Z0-9]{8}$")
            self.assertIn(row["research_family"], RESEARCH_FAMILIES)


if __name__ == "__main__":
    unittest.main()
