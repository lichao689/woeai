"""Keep active cover guidance and measurement declarations consistent."""
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/wechat-cover"


class CoverContractTests(unittest.TestCase):
    def test_approved_directions_have_exactly_five_palette_rows(self):
        standards = (SKILL / "references/cover-standards.md").read_text()
        rows = re.findall(r"^\| ([^|]+?) \| #[0-9A-F]{6} \|", standards, re.M)
        self.assertEqual(rows, ["数值风洞", "结构抗风", "一体化分析", "混凝土浮体", "数值水池"])

    def test_template_carries_current_contract_and_separate_review_states(self):
        standards = (SKILL / "references/cover-standards.md").read_text()
        version = re.search(r"Series contract: (WOEAI-cover-v\d+)", standards).group(1)
        template = (ROOT / "wechat/templates/cover-brief.md").read_text()
        self.assertIn(f"cover_design_contract: `{version}`", template)
        for field in ("badge_geometry_status", "exact_text_status",
                      "typography_and_radius_status", "scientific_evidence_status",
                      "horizontal_composition_status", "design_contract_checked"):
            self.assertIn(f"{field}: pending", template)
        self.assertIn("backend_preview_checked: false", template)
        for field in ("final_image_sha256", "badge_measurement_method",
                      "badge_outer_bbox_xyxy", "badge_ink_bbox_and_height",
                      "badge_nominal_typography_evidence"):
            self.assertIn(f"{field}:", template)

    def test_active_skill_links_resolve(self):
        for document in (SKILL / "SKILL.md", SKILL / "references/cover-standards.md"):
            for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                if not target.startswith(("https:", "http:", "#")):
                    self.assertTrue((document.parent / target.split("#")[0]).exists(), target)


if __name__ == "__main__":
    unittest.main()
