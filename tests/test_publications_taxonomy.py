"""Tests for the WOEAI research taxonomy (single source of truth).

The Research Family taxonomy is a public fact locked by CONTEXT.md: exactly two
families, a fixed set of subdirections, a fixed order. These tests pin that
contract at the shared module's interface so the three former copies
(scripts/, tools/, tests/) can all import one source without re-asserting it.
"""

from __future__ import annotations

import unittest

from woeai.publications import (
    RESEARCH_FAMILY_ORDER,
    RESEARCH_SUBDIRECTION_ORDER,
)


class ResearchTaxonomyTests(unittest.TestCase):
    def test_has_exactly_two_families_in_fixed_order(self) -> None:
        self.assertEqual(
            RESEARCH_FAMILY_ORDER, ("结构风工程", "海洋能源结构")
        )

    def test_wind_resistance_family_subdirections(self) -> None:
        self.assertEqual(
            RESEARCH_SUBDIRECTION_ORDER["结构风工程"],
            ("数值风洞", "结构抗风"),
        )

    def test_current_family_name_and_english_translation_reach_generated_views(self):
        from pathlib import Path
        from woeai.publications.taxonomy import RESEARCH_FAMILY_EN
        from woeai.publications.registry import load_registry, generated_views
        from woeai.publications.homepage import render_home_progress
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(RESEARCH_FAMILY_EN['结构风工程'], 'Structural Wind Engineering')
        self.assertNotIn('工程结构抗风', RESEARCH_FAMILY_EN)
        for path, text in generated_views(root, load_registry(root)).items():
            with self.subTest(path=path):
                self.assertNotIn('工程结构抗风', text)
        self.assertIn('结构风工程', render_home_progress(root))
        self.assertIn('Structural Wind Engineering', render_home_progress(root, english=True))
        self.assertNotIn('工程结构抗风', render_home_progress(root, english=True))

    def test_floating_wind_family_subdirections(self) -> None:
        self.assertEqual(
            RESEARCH_SUBDIRECTION_ORDER["海洋能源结构"],
            (
                "一体化分析",
                "混凝土浮体",
                "数值水池",
            ),
        )

    def test_every_family_has_a_subdirection_order_entry(self) -> None:
        self.assertEqual(set(RESEARCH_FAMILY_ORDER), set(RESEARCH_SUBDIRECTION_ORDER))

class TaxonomySurfaceTests(unittest.TestCase):
    """Published navigation and reader metadata must follow the registry."""

    def test_publication_sections_match_every_registry_record(self):
        import json
        import re
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        rows = json.loads((root / 'docs/data/publications.json').read_text())
        expected = {r['custom']['publication_ref']: (
            r['custom']['research_family'], r['custom']['subdirection']) for r in rows}
        family = subdirection = None
        observed = {}
        for line in (root / 'docs/source/Publications.rst').read_text().splitlines():
            if line in RESEARCH_FAMILY_ORDER:
                family = line
                subdirection = None
            elif line in RESEARCH_SUBDIRECTION_ORDER.get(family, ()):
                subdirection = line
            match = re.fullmatch(r'\.\. _(ref-[^:]+):', line)
            if match and match[1] in expected:
                self.assertNotIn(match[1], observed)
                observed[match[1]] = (family, subdirection)
        self.assertEqual(observed, expected)

    def test_existing_article_direction_matches_registry(self):
        import json
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        for row in json.loads((root / 'docs/data/publications.json').read_text()):
            c = row['custom']
            path = root / c['wechat']['path']
            if not path.exists():
                continue
            with self.subTest(ref=c['publication_ref']):
                expected = f"- WOEAI 相关方向: {c['research_family']} / {c['subdirection']}"
                lines = [line for line in path.read_text().splitlines() if 'WOEAI 相关方向' in line]
                self.assertEqual(lines, [expected])


if __name__ == "__main__":
    unittest.main()
