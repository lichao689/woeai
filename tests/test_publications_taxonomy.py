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
            RESEARCH_FAMILY_ORDER, ("建筑结构抗风", "海上漂浮风电")
        )

    def test_wind_resistance_family_subdirections(self) -> None:
        self.assertEqual(
            RESEARCH_SUBDIRECTION_ORDER["建筑结构抗风"],
            ("数值风洞与湍动入流", "高层建筑抗风与优化"),
        )

    def test_floating_wind_family_subdirections(self) -> None:
        self.assertEqual(
            RESEARCH_SUBDIRECTION_ORDER["海上漂浮风电"],
            (
                "浮式风机系统一体化分析与优化",
                "浮式混凝土平台结构设计",
                "数值风浪流水池",
            ),
        )

    def test_every_family_has_a_subdirection_order_entry(self) -> None:
        self.assertEqual(set(RESEARCH_FAMILY_ORDER), set(RESEARCH_SUBDIRECTION_ORDER))


if __name__ == "__main__":
    unittest.main()
