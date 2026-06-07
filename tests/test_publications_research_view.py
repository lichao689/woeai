from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS = ROOT / "docs/source/Publications.rst"
PUBLICATIONS_BY_RESEARCH = ROOT / "docs/source/PublicationsByResearch.rst"
RESEARCH_MAP = ROOT / "docs/data/publication-research-map.json"

RESEARCH_FAMILIES = ("建筑结构抗风", "海上漂浮风电")


def publication_anchors(text: str) -> set[str]:
    return set(re.findall(r"^\.\. _(ref-[^:]+):$", text, flags=re.M))


def research_ref_targets(text: str) -> list[str]:
    return re.findall(r":ref:`[^`<]+ <(ref-[^>]+)>`", text)


class PublicationsResearchViewTests(unittest.TestCase):
    def test_publications_page_links_to_research_view(self) -> None:
        text = PUBLICATIONS.read_text(encoding="utf-8")

        self.assertIn("浏览方式 View Options", text)
        self.assertIn(":doc:`PublicationsByResearch`", text)

    def test_research_view_groups_every_publication_by_family_then_descending_year(self) -> None:
        publications_text = PUBLICATIONS.read_text(encoding="utf-8")
        research_text = PUBLICATIONS_BY_RESEARCH.read_text(encoding="utf-8")

        source_anchors = publication_anchors(publications_text)
        linked_anchors = research_ref_targets(research_text)
        self.assertEqual(set(linked_anchors), source_anchors)
        self.assertEqual(len(linked_anchors), len(source_anchors))

        family_positions = [research_text.index(f"\n{family}\n") for family in RESEARCH_FAMILIES]
        self.assertEqual(family_positions, sorted(family_positions))

        for family, start in zip(RESEARCH_FAMILIES, family_positions, strict=True):
            next_positions = [pos for pos in family_positions if pos > start]
            end = min(next_positions) if next_positions else len(research_text)
            section = research_text[start:end]
            years = [int(year) for year in re.findall(r"^(\d{4})$", section, flags=re.M)]
            self.assertEqual(years, sorted(years, reverse=True), family)

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
