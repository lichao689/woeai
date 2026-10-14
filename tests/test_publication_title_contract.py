"""Canonical RTD navigation prefixes are direction-exact, with bounded legacy snapshots."""
from pathlib import Path
import unittest
from unittest.mock import patch

from tools.publications import artifacts
from woeai.publications.taxonomy import RESEARCH_SUBDIRECTION_ORDER


class PublicationTitleContractTests(unittest.TestCase):
    def problems(self, ref, family, direction, title):
        root = Path(__file__).resolve().parents[1]
        artifact = artifacts.PublicationArtifact(
            publication_ref=ref, title=title, research_family=family,
            subdirection=direction, original_year=2026, wechat_status="awaiting_review",
            order=1, article_path=root / "example.md", review_path=root / "review.md",
            rtd_path=root / "example.rst", root=root,
        )
        with patch.object(artifacts, "public_artifacts", return_value=[artifact]):
            return artifacts.artifact_integrity_problems(root)

    def test_prefix_vocabulary_comes_from_single_taxonomy(self):
        self.assertEqual(artifacts.PAPER_NOTE_TITLE_PREFIXES, {
            family: tuple(f"{direction} |" for direction in directions)
            for family, directions in RESEARCH_SUBDIRECTION_ORDER.items()
        })
        self.assertEqual(sum(map(len, artifacts.PAPER_NOTE_TITLE_PREFIXES.values())), 5)
        self.assertFalse(any("漂浮风电 |" in values
                             for values in artifacts.PAPER_NOTE_TITLE_PREFIXES.values()))

    def test_all_five_directions_accept_only_their_own_prefix(self):
        directions = [direction for values in RESEARCH_SUBDIRECTION_ORDER.values()
                      for direction in values]
        for family, values in RESEARCH_SUBDIRECTION_ORDER.items():
            for direction in values:
                for prefix in directions:
                    with self.subTest(family=family, direction=direction, prefix=prefix):
                        problems = self.problems("ref-new", family, direction, f"{prefix} | Source-backed hook")
                        self.assertEqual(bool(problems), prefix != direction)
                        if prefix != direction:
                            self.assertEqual(problems[0]["kind"], "paper_note_title_missing_prefix")
                            self.assertEqual(problems[0]["expected_prefixes"], [f"{direction} |"])

    def test_only_four_exact_legacy_snapshots_are_accepted(self):
        self.assertEqual(set(artifacts.LEGACY_RTD_PUBLIC_TITLES), {
            "ref-he2026-OE-structural", "ref-li2022-SOS", "ref-zheng2025-OE", "ref-zhou2023-AE"})
        for ref, (family, direction, title) in artifacts.LEGACY_RTD_PUBLIC_TITLES.items():
            with self.subTest(ref=ref):
                self.assertEqual(self.problems(ref, family, direction, title), [])
                self.assertTrue(self.problems("ref-new", family, direction, title))
                self.assertTrue(self.problems(ref, family, direction, title + " changed"))
                self.assertTrue(self.problems(ref, family, "数值水池", title))
                self.assertTrue(self.problems(ref, "工程结构抗风", "数值风洞", title))

    def test_legacy_refs_can_adopt_their_correct_canonical_prefix(self):
        for ref, (family, direction, _) in artifacts.LEGACY_RTD_PUBLIC_TITLES.items():
            with self.subTest(ref=ref):
                self.assertEqual(self.problems(ref, family, direction, f"{direction} | Reviewed new hook"), [])
                self.assertTrue(self.problems(ref, family, direction, "数值水池 | Wrong direction"))

    def test_new_marine_refs_cannot_use_generic_legacy_prefix(self):
        for direction in RESEARCH_SUBDIRECTION_ORDER["海上漂浮风电"]:
            with self.subTest(direction=direction):
                self.assertTrue(self.problems("ref-new", "海上漂浮风电", direction, "漂浮风电 | New hook"))

    def test_redundant_suffix_and_unknown_mapping_still_fail(self):
        problems = self.problems("ref-new", "海上漂浮风电", "一体化分析", "一体化分析 | Hook论文精解")
        self.assertIn("paper_note_title_redundant_suffix", {p["kind"] for p in problems})
        self.assertTrue(self.problems("ref-new", "海上漂浮风电", "未知方向", "未知方向 | Hook"))
        self.assertTrue(self.problems("ref-new", "未知一级", "一体化分析", "一体化分析 | Hook"))


if __name__ == "__main__":
    unittest.main()
