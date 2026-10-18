from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/source"
INDEX = SOURCE / "index.rst"
CONF = SOURCE / "conf.py"
PROJECTS = SOURCE / "Projects.rst"
RESEARCH = SOURCE / "Research.rst"
# The two former direction pages were first merged into a ResearchDirections
# page, then inlined into Research.rst itself; their anchors and project
# records now live directly in Research.rst.
ENGINEERING = SOURCE / "EngineeringApplications.rst"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def public_source_texts() -> dict[str, str]:
    return {path.name: read(path) for path in SOURCE.glob("*.rst") if path.name != "Projects.rst"}


class RTDHomepageProjectsRedesignTests(unittest.TestCase):
    def test_homepage_uses_confirmed_identity_and_research_with_recruitment_path(self) -> None:
        index = read(INDEX)
        conf = read(CONF)

        self.assertNotIn(".. image:: ../_static/logoGroup.png", index)
        self.assertIn('html_logo = "../_static/logoGroup.png"', conf)
        self.assertIn('id="profile-name">AI 赋能<span class="hero-title-subject">风与海洋工程</span>', index)
        self.assertNotIn('融合物理机理与人工智能，探索建筑与能源结构的分析与设计。', index)
        self.assertIn('<h2 class="hero-position">融合物理规律与人工智能<br>揭示风与海洋作用机理<br>探索建筑与能源结构设计</h2>', index)
        self.assertIn('课题组负责人</strong> 李朝 · 教授 · 博士生导师', index)
        self.assertNotIn('id="profile-name">李朝', index)
        self.assertNotIn('paper-record-slot', index)
        self.assertEqual(index.count('class="paper-citation"'), 6)
        self.assertNotIn('<details', index)
        self.assertNotIn('精选研究：问题与贡献', index)
        self.assertIn('Kriging 代理模型', index)
        self.assertIn('图神经网络结合结构连接关系', index)
        self.assertIn('从已完成公众号解读的候选论文中，两个研究方向各按发表日期倒序展示最多三篇', index)
        self.assertIn("教授 · 博士生导师", index)
        self.assertIn("揭示风与海洋作用机理<br>探索建筑与能源结构设计</h2>", index)
        self.assertIn('href="https://homepage.hit.edu.cn/lichao"', index)
        self.assertNotIn("哈尔滨工业大学", index)
        self.assertNotIn("年度招生规划", index)
        self.assertLess(index.index('href="#join-contact"'), index.index('id="research-lines"'))
        sections = ('research-lines', 'selected-work', 'latest-progress', 'applications', 'join-contact')
        positions = [index.index(f'id="{section}"') for section in sections]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(index.count('class="work-card"'), 6)
        progress = index.split('.. BEGIN GENERATED LATEST PAPER NOTES')[1].split('.. END GENERATED LATEST PAPER NOTES')[0]
        self.assertEqual(progress.count('class="work-card"'), 6)
        self.assertEqual(progress.count('class="progress-family"'), 2)
        self.assertNotIn('<section id="latest-progress"', index)
        self.assertEqual(index.count('id="latest-progress"'), 1)
        self.assertIn('href="Recruitment.html"', index)
        self.assertIn('id="contact-heading">交流与合作</h2>', index)
        self.assertIn('href="Recruitment.html">加入团队', index)
        self.assertIn('href="EngineeringApplications.html#discuss-an-engineering-problem">工程合作', index)
        self.assertNotIn('招生与联系', index)
        self.assertTrue((SOURCE / 'Recruitment.rst').is_file())

    def test_direction_concepts_are_explicitly_illustrative_in_both_languages(self) -> None:
        chinese = read(INDEX)
        english = read(SOURCE / '_templates/en-home.html')
        for name in ('research-structural-wind-concept-v1.webp', 'research-marine-structures-concept-v1.webp'):
            self.assertEqual(chinese.count(name), 1)
            self.assertEqual(english.count(name), 1)
            self.assertTrue((ROOT / 'docs/_static/home' / name).is_file())
        self.assertEqual(chinese.count('AI 生成的科研概念示意 · 非研究数据</figcaption>'), 2)
        self.assertEqual(english.count('AI-generated research concept · not research data</figcaption>'), 2)
        self.assertIn('aspect-ratio: 1440 / 811', read(ROOT / 'docs/_static/custom.css'))
        self.assertNotIn('实验室', chinese)

    def test_projects_page_is_removed_from_navigation_and_source_tree(self) -> None:
        index = read(INDEX)

        self.assertFalse(PROJECTS.exists())
        self.assertNotIn("\n   Projects\n", index)
        self.assertIn("\n   Research\n", index)
        self.assertIn("\n   EngineeringApplications\n", index)
        self.assertIn("\n   Publications\n", index)

    def test_project_evidence_migrated_to_receiving_pages(self) -> None:
        research = read(RESEARCH)
        engineering = read(ENGINEERING)

        # Both direction anchors now live directly in Research.rst.
        self.assertIn(".. _building-wind-project-support:", research)
        self.assertIn(".. _floating-wind-project-support:", research)
        self.assertIn(".. _engineering-enterprise-project-evidence:", engineering)

        self.assertIn("数值大气湍流边界层生成方法的改进与验证", research)
        self.assertIn("考虑风致荷载及响应的高层建筑气动外形优化研究", research)
        self.assertIn("面向多设计阶段的浮式风机系统一体化分析与优化方法", research)
        self.assertIn("柱稳型海上浮式风机基础的关键技术开发", research)
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
