from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/source"
INDEX = SOURCE / "index.rst"
CONF = SOURCE / "conf.py"
PROJECTS = SOURCE / "Projects.rst"
RESEARCH = SOURCE / "Research.rst"
BUILDING = SOURCE / "BuildingStructuralWindResistance.rst"
FLOATING = SOURCE / "FloatingOffshoreWindEnergy.rst"
ENGINEERING = SOURCE / "EngineeringApplications.rst"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def public_source_texts() -> dict[str, str]:
    return {path.name: read(path) for path in SOURCE.glob("*.rst") if path.name != "Projects.rst"}


class RTDHomepageProjectsRedesignTests(unittest.TestCase):
    def test_homepage_uses_engineering_first_story_without_duplicate_logo(self) -> None:
        index = read(INDEX)
        conf = read(CONF)

        self.assertNotIn(".. image:: ../_static/logoGroup.png", index)
        self.assertIn('html_logo = "../_static/logoGroup.png"', conf)
        self.assertIn("把风与海洋工程研究转化为可验证的工程能力", index)
        self.assertLess(index.index("工程应用 Engineering Applications"), index.index("加入 WOEAI Recruitment"))
        self.assertLess(index.index("加入 WOEAI Recruitment"), index.index("最新学术进展 Latest Academic Progress"))
        self.assertIn("完整研究脉络见 :doc:`Research`，完整论文记录见 :doc:`Publications`。", index)

    def test_projects_page_is_removed_from_navigation_and_source_tree(self) -> None:
        index = read(INDEX)

        self.assertFalse(PROJECTS.exists())
        self.assertNotIn("\n   Projects\n", index)
        self.assertIn("\n   Research\n", index)
        self.assertIn("\n   EngineeringApplications\n", index)
        self.assertIn("\n   Publications\n", index)

    def test_project_evidence_migrated_to_receiving_pages(self) -> None:
        research = read(RESEARCH)
        building = read(BUILDING)
        floating = read(FLOATING)
        engineering = read(ENGINEERING)

        self.assertIn(".. _research-public-project-support:", research)
        self.assertIn(".. _building-wind-project-support:", building)
        self.assertIn(".. _floating-wind-project-support:", floating)
        self.assertIn(".. _engineering-enterprise-project-evidence:", engineering)

        self.assertIn("数值大气湍流边界层生成方法的改进与验证", building)
        self.assertIn("考虑风致荷载及响应的高层建筑气动外形优化研究", building)
        self.assertIn("面向多设计阶段的浮式风机系统一体化分析与优化方法", floating)
        self.assertIn("柱稳型海上浮式风机基础的关键技术开发", floating)
        self.assertIn("微地形下输电线路微尺度台风风场特性及模型研究", engineering)
        self.assertIn("钢筋混凝土半潜式浮力风机系统的风浪联合模型试验研究", engineering)

    def test_legacy_projects_references_are_removed_from_public_sources(self) -> None:
        for filename, text in public_source_texts().items():
            with self.subTest(filename=filename):
                self.assertNotIn(":doc:`Projects`", text)
                self.assertNotIn("projects-numerical-wind-tunnel", text)
                self.assertNotIn("projects-structural-wind", text)
                self.assertNotIn("projects-offshore-wind", text)
                self.assertNotIn("项目实践 Project Evidence", text)


if __name__ == "__main__":
    unittest.main()
