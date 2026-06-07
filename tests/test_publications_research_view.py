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
    return re.findall(r":ref:`\[\d+\] <(ref-[^>]+)>`", text)


def normalize_publication_entry(line: str) -> str:
    return re.sub(r"^:ref:`\[(\d+)\] <ref-[^>]+>`", r"[\1]", line)


def publication_entries(text: str) -> list[str]:
    entries = re.findall(r"^(?:\[\d+\]|:ref:`\[\d+\] <ref-[^>]+>`).+$", text, flags=re.M)
    return [normalize_publication_entry(entry) for entry in entries]


def publication_numbers(text: str) -> list[int]:
    numbers: list[int] = []
    for line in re.findall(r"^(?:\[\d+\]|:ref:`\[\d+\] <ref-[^>]+>`).+$", text, flags=re.M):
        match = re.match(r"^(?:\[(\d+)\]|:ref:`\[(\d+)\] <ref-[^>]+>`)", line)
        if match:
            numbers.append(int(match.group(1) or match.group(2)))
    return numbers


def publication_number_years(text: str) -> dict[int, int]:
    years: dict[int, int] = {}
    current_year = 0
    for line in text.splitlines():
        if re.fullmatch(r"\d{4}", line):
            current_year = int(line)
            continue
        match = re.match(r"^\[(\d+)\] ", line)
        if match:
            years[int(match.group(1))] = current_year
    return years


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

        chronological_entries = publication_entries(publications_text)
        thematic_entries = publication_entries(research_text)
        self.assertEqual(set(thematic_entries), set(chronological_entries))
        self.assertEqual(len(thematic_entries), len(chronological_entries))
        self.assertEqual(set(research_ref_targets(research_text)), publication_anchors(publications_text))

        family_positions = [research_text.index(f"\n{family}\n") for family in RESEARCH_FAMILIES]
        self.assertEqual(family_positions, sorted(family_positions))
        number_years = publication_number_years(publications_text)

        for family, subdirections in RESEARCH_STRUCTURE.items():
            other_families = tuple(candidate for candidate in RESEARCH_FAMILIES if candidate != family)
            family_section = section_between(research_text, family, other_families)
            subdirection_positions = [family_section.index(f"\n{subdirection}\n") for subdirection in subdirections]
            self.assertEqual(subdirection_positions, sorted(subdirection_positions), family)
            self.assertNotRegex(family_section, r"^\d{4}$", family)

            for index, subdirection in enumerate(subdirections):
                next_subdirections = subdirections[index + 1 :]
                subdirection_section = section_between(family_section, subdirection, next_subdirections)
                numbers = publication_numbers(subdirection_section)
                years = [number_years[number] for number in numbers]
                self.assertEqual(years, sorted(years, reverse=True), subdirection)

    def test_research_view_uses_the_same_publication_expression_as_chronological_view(self) -> None:
        publications_text = PUBLICATIONS.read_text(encoding="utf-8")
        text = PUBLICATIONS_BY_RESEARCH.read_text(encoding="utf-8")

        self.assertEqual(set(publication_entries(text)), set(publication_entries(publications_text)))
        self.assertIn("https://doi.org/", text)
        self.assertIn("影响因子:", text)
        self.assertIn("中科院分区:", text)

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
