from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from woeai.publications import (
    RESEARCH_FAMILY_ORDER,
    RESEARCH_SUBDIRECTION_ORDER,
)


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS = ROOT / "docs/source/Publications.rst"
PUBLICATIONS_BY_RESEARCH = ROOT / "docs/source/PublicationsByResearch.rst"
RESEARCH = ROOT / "docs/source/Research.rst"
TEACHING = ROOT / "docs/source/Teaching.rst"
INDEX = ROOT / "docs/source/index.rst"
PEOPLE = ROOT / "docs/source/People.rst"
CONF = ROOT / "docs/source/conf.py"
DOI_NEW_TAB_JS = ROOT / "docs/_static/doi-new-tab.js"
RESEARCH_MAP = ROOT / "docs/data/publication-research-map.json"

# Aliases kept for the existing assertions below; the values now come from the
# single source of truth in woeai.publications rather than a third local copy.
RESEARCH_FAMILIES = RESEARCH_FAMILY_ORDER
RESEARCH_STRUCTURE = RESEARCH_SUBDIRECTION_ORDER
TEACHING_REFORM_PUBLICATION_KEY = "KT6UR5JW"
TEACHING_REFORM_PUBLICATION_TITLE = "中国共产党精神谱系视域下土木工程课程思政建设的探索与实践"


def publication_anchors(text: str) -> set[str]:
    return set(re.findall(r"^\.\. _(ref-[^:]+):$", text, flags=re.M))


def canonical_publication_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    pattern = re.compile(r"(?P<label_block>(?:^\.\. _ref-[^:]+:\n\n)+)\[\d+\] ", flags=re.M)
    for match in pattern.finditer(text):
        labels = re.findall(r"^\.\. _(ref-[^:]+):$", match.group("label_block"), flags=re.M)
        if labels:
            anchors.add(labels[-1])
    return anchors


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
        if line == "更早 Earlier":
            current_year = 0
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
        research_text = RESEARCH.read_text(encoding="utf-8")
        index_text = INDEX.read_text(encoding="utf-8")

        self.assertNotIn("浏览方式 View Options", text)
        self.assertNotIn("精选证据 Selected Highlights", text)
        self.assertIn(".. container:: publication-view-banner", text)
        self.assertIn("论文解读 Paper Notes", text)
        self.assertIn("按研究方向浏览学术成果 Publications by Research Direction <PublicationsByResearch>", text)
        self.assertNotIn("学术进展 Academic Progress", research_text)
        self.assertNotIn("paper-notes/", research_text)
        self.assertNotIn("\n   PublicationsByResearch\n", index_text)
        self.assertNotIn("\n   People\n", index_text)
        self.assertFalse(PEOPLE.exists())

    def test_research_view_groups_every_publication_by_family_then_subdirection(self) -> None:
        publications_text = PUBLICATIONS.read_text(encoding="utf-8")
        research_text = PUBLICATIONS_BY_RESEARCH.read_text(encoding="utf-8")

        chronological_entries = publication_entries(publications_text)
        thematic_entries = publication_entries(research_text)
        self.assertEqual(set(thematic_entries), set(chronological_entries))
        self.assertEqual(len(thematic_entries), len(chronological_entries))
        self.assertEqual(set(research_ref_targets(research_text)), canonical_publication_anchors(publications_text))

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
        source_anchors = canonical_publication_anchors(PUBLICATIONS.read_text(encoding="utf-8"))
        self.assertEqual(len(items), len(source_anchors))

        families = {row["research_family"] for row in items.values()}
        self.assertEqual(families, set(RESEARCH_FAMILIES))

        for key, row in items.items():
            self.assertRegex(key, r"^[A-Z0-9]{8}$")
            self.assertIn(row["research_family"], RESEARCH_FAMILIES)

    def test_teaching_reform_publications_live_on_teaching_page(self) -> None:
        publications_text = PUBLICATIONS.read_text(encoding="utf-8")
        research_text = PUBLICATIONS_BY_RESEARCH.read_text(encoding="utf-8")
        teaching_text = TEACHING.read_text(encoding="utf-8")
        mapping = json.loads(RESEARCH_MAP.read_text(encoding="utf-8"))

        self.assertNotIn(TEACHING_REFORM_PUBLICATION_TITLE, publications_text)
        self.assertNotIn(TEACHING_REFORM_PUBLICATION_TITLE, research_text)
        self.assertNotIn(TEACHING_REFORM_PUBLICATION_KEY, mapping["items"])
        self.assertIn("教改探索", teaching_text)
        self.assertIn(TEACHING_REFORM_PUBLICATION_TITLE, teaching_text)

    def test_publications_page_groups_early_papers_and_degree_theses(self) -> None:
        text = PUBLICATIONS.read_text(encoding="utf-8")

        self.assertIn("\n更早 Earlier\n", text)
        self.assertNotRegex(text, r"\n2018\n~+\n")
        self.assertNotRegex(text, r"\n2017\n~+\n")
        self.assertLess(text.index("期刊论文 Journal Papers"), text.index("学位论文 Degree Theses"))
        self.assertIn("博士学位论文 PhD Theses", text)
        self.assertIn("硕士学位论文 Master Theses", text)
        self.assertLess(text.index("周盛涛(Zhou Shengtao)，2021"), text.index("郑舜云(Zheng Shunyun)，2024-11"))
        self.assertLess(text.index("陈铃伟(Chen Lingwei)，2025-09"), text.index("何欣(He Xin)，博士生在读"))
        self.assertIn("刘尚佩(Liu Shangpei)，博士生在读", text)
        self.assertLess(text.index("王一鸣(Wang Yiming)，2023"), text.index("赵培升(Zhao Peisheng)，2025"))

    def test_updated_wake_model_publication_year_keeps_old_anchor_alias(self) -> None:
        text = PUBLICATIONS.read_text(encoding="utf-8")
        old_anchor = ".. _ref-zhang2015-E:"
        new_anchor = ".. _ref-zhang2022-E:"
        title = "Applicability of wake models to predictions of turbine-induced velocity deficit and wind farm power generation"

        self.assertIn(old_anchor, text)
        self.assertIn(new_anchor, text)
        self.assertLess(text.index("\n2022\n"), text.index(title))
        self.assertLess(text.index(title), text.index("\n2021\n"))

    def test_doi_links_open_in_new_tab(self) -> None:
        conf_text = CONF.read_text(encoding="utf-8")
        js_text = DOI_NEW_TAB_JS.read_text(encoding="utf-8")

        self.assertIn("doi-new-tab.js", conf_text)
        self.assertIn('target = "_blank"', js_text)
        self.assertIn('rel = "noopener noreferrer"', js_text)
        self.assertIn('href^="https://doi.org/"', js_text)


if __name__ == "__main__":
    unittest.main()
