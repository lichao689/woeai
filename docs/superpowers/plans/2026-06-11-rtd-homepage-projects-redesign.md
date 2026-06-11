# RTD Homepage Projects Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the WOEAI RTD homepage around engineering applications first, recruitment second, academic credibility third, while deleting the standalone `Projects.rst` page and migrating its evidence into research and engineering-application pages.

**Architecture:** This is a Sphinx documentation-site change. Add one focused regression test file that codifies the navigation, homepage, and project-evidence migration expectations, then update only the relevant `.rst` pages and delete the old project archive. Keep existing public facts source-bounded and preserve any unrelated uncommitted work.

**Tech Stack:** Sphinx, `sphinx_rtd_theme`, reStructuredText, Python `unittest`, repo gate `./scripts/check-docs.sh`.

---

## File Structure

- Create: `tests/test_rtd_homepage_projects_redesign.py`
  - Owns regression checks for the redesigned homepage, removal of `Projects.rst`, new project-support anchors, and absence of legacy project references.
- Modify: `docs/source/index.rst`
  - Removes the duplicate content-area logo.
  - Reorders the homepage story to `工程应用` -> `加入 WOEAI` -> `最新学术进展`.
  - Removes `Projects` from the hidden toctree.
- Modify: `docs/source/Research.rst`
  - Adds a concise government/vertical project-support section that points readers to the two research-family pages.
  - Does not reintroduce `学术进展 Academic Progress` if the current branch has already moved paper-note archive behavior elsewhere.
- Modify: `docs/source/BuildingStructuralWindResistance.rst`
  - Replaces the old `:doc:\`Projects\`` project connection with building-wind government project support and a stable anchor.
- Modify: `docs/source/FloatingOffshoreWindEnergy.rst`
  - Replaces the old `:doc:\`Projects\`` project connection with floating-offshore-wind government project support and a stable anchor.
- Modify: `docs/source/EngineeringApplications.rst`
  - Replaces legacy `projects-*` references and `:doc:\`Projects\`` links with scenario-local project evidence and a stable enterprise evidence anchor.
- Delete: `docs/source/Projects.rst`
  - Removes the standalone project archive after its public-safe content has been migrated.

Before editing, run `git status --short`. If unrelated files are already modified, keep them and avoid reverting them.

---

### Task 1: Add Redesign Regression Tests

**Files:**
- Create: `tests/test_rtd_homepage_projects_redesign.py`

- [ ] **Step 1: Create the failing test file**

Use `apply_patch` to add:

```python
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
```

- [ ] **Step 2: Run the new test and confirm it fails for the current site**

Run:

```bash
python3 -m unittest tests.test_rtd_homepage_projects_redesign -v
```

Expected: FAIL. At minimum, failures should mention the duplicate homepage `logoGroup.png`, existing `Projects.rst`, `Projects` in the homepage toctree, and missing new anchors.

- [ ] **Step 3: Commit the failing test**

```bash
git add tests/test_rtd_homepage_projects_redesign.py
git commit -m "test: cover RTD homepage project redesign"
```

---

### Task 2: Rewrite Homepage Around Engineering Applications

**Files:**
- Modify: `docs/source/index.rst`
- Test: `tests/test_rtd_homepage_projects_redesign.py`

- [ ] **Step 1: Replace the homepage opening and remove the duplicate logo**

In `docs/source/index.rst`, remove this block:

```rst
.. image:: ../_static/logoGroup.png
   :alt: WOEAI group logo
   :width: 260px
   :align: right
```

Replace the current opening prose through the first section break with:

```rst
把风与海洋工程研究转化为可验证的工程能力
======================================

WOEAI（Wind and Ocean Engineering with AI）面向建筑结构抗风、城市风环境、海上漂浮风电和海洋工程结构场景，研究 AI 赋能的风与海洋工程问题，服务工程结构防灾减灾与海上风电工程创新。

团队结合数值模拟、物理试验、公开项目记录和理论分析，把风与海洋环境作用、结构响应、工程优化和智能建模连接起来。网站优先呈现可公开说明的工程应用场景，也为有志于相关方向的学生、博士后和学术同行提供研究脉络与成果入口。
```

- [ ] **Step 2: Move engineering applications before recruitment**

In `docs/source/index.rst`, place this section immediately after the opening:

```rst
工程应用 Engineering Applications
================================

WOEAI 围绕建筑结构抗风、海上漂浮风电，以及支撑两类问题的 AI 赋能工程建模方法开展工程应用研究。公开可说明的应用场景包括城市风环境与复杂地形风场评估、高层建筑风荷载与风致响应、浮式风机系统分析与优化、浮式混凝土平台结构设计，以及风浪联合模型试验。

重点入口：

- **建筑结构抗风**：城市风环境、复杂地形风场、数值风洞与湍动入流、高层建筑风荷载、风致响应和气动外形优化。
- **海上漂浮风电**：浮式风机系统一体化分析、浮式混凝土平台结构设计、风浪流联合作用和数值风浪流水池。
- **AI 赋能工程方法**：图神经网络、深度学习、超分辨率重建、智能几何建模和代理模型，用于工程仿真、预测和快速评估。

详见 :doc:`EngineeringApplications`。
```

- [ ] **Step 3: Keep recruitment concise after engineering applications**

Move the existing recruitment section so it follows the engineering applications section. Keep the current annual recruitment planning numbers, but use this tightened body:

```rst
加入 WOEAI Recruitment
=====================

WOEAI 欢迎对风工程、海洋工程、海上风电、结构防灾减灾和 AI 赋能工程方法有持续兴趣的学生与青年研究人员加入。

希望你：

- 踏实上进，有强烈求知欲和持续学习意愿；
- 愿意结合基础理论、数值模拟和物理试验形成创新技术解决实际工程问题；
- 尤其欢迎有读博意愿的学生。

年度招生规划：

- 硕士研究生：2-3 名/年；
- 博士研究生：1-2 名/年；
- 博士后：1-2 名/年。

博士后岗位面向土木工程、海洋工程及相关方向博士，关注科研论文基础和工程研究能力。年龄、获学位年限、待遇、补贴、住房、落户及出站政策等均应以相关公开政策和团队当年公开信息为准。

招生咨询可通过页面底部邮箱联系。建议简要说明申请类型、研究兴趣、教育背景和希望进一步讨论的问题。
```

- [ ] **Step 4: Keep research directions compact**

Keep the existing `研究方向 Research Directions` section, but place it after recruitment. Keep the two research-family bullets and horizontal support bullets. Do not add a new first-level family beyond `建筑结构抗风` and `海上漂浮风电`.

- [ ] **Step 5: Keep latest academic progress as homepage preview**

Keep the current 10 paper-note bullets under `最新学术进展 Latest Academic Progress`. Change the lead sentence to:

```rst
首页展示最近 10 条论文解读与 RTD 配套文章，完整研究脉络见 :doc:`Research`，完整论文记录见 :doc:`Publications`。
```

- [ ] **Step 6: Remove Projects from hidden toctree**

Ensure the hidden toctree ends like this:

```rst
.. toctree::
   :hidden:
   :maxdepth: 2

   首页 Home <self>
   Research
   EngineeringApplications
   Publications
   Teaching
   Privacy
```

- [ ] **Step 7: Run the homepage-focused test**

Run:

```bash
python3 -m unittest tests.test_rtd_homepage_projects_redesign.RTDHomepageProjectsRedesignTests.test_homepage_uses_engineering_first_story_without_duplicate_logo -v
```

Expected: PASS.

- [ ] **Step 8: Commit the homepage rewrite**

```bash
git add docs/source/index.rst
git commit -m "docs: make homepage engineering-first"
```

---

### Task 3: Move Government Project Support Into Research Pages

**Files:**
- Modify: `docs/source/Research.rst`
- Modify: `docs/source/BuildingStructuralWindResistance.rst`
- Modify: `docs/source/FloatingOffshoreWindEnergy.rst`
- Test: `tests/test_rtd_homepage_projects_redesign.py`

- [ ] **Step 1: Add public project support to Research.rst**

In `docs/source/Research.rst`, after the visible research-direction toctree, add:

```rst
.. _research-public-project-support:

公开科研项目支撑 Public Research Project Support
----------------------------------------------

WOEAI 的公开科研项目记录按两条研究主方向归集，用于说明研究问题、方法发展和工程验证闭环。政府和纵向项目不再单独放在项目实践页面，而是作为科研方向的支撑材料呈现。

- **建筑结构抗风**：数值大气湍流边界层生成、LES 数值风洞、高层建筑气动外形优化、城市风环境和复杂地形风场相关研究。详见 :ref:`building-wind-project-support`。
- **海上漂浮风电**：浮式风机系统一体化分析、浮式混凝土平台结构设计、浮式风机平衡与振动控制、半潜式基础关键技术和垂直轴风机控制策略相关研究。详见 :ref:`floating-wind-project-support`。

工程应用和企业委托项目证据见 :doc:`EngineeringApplications`。
```

If `Research.rst` currently has no paper-note archive, do not re-add `学术进展 Academic Progress`. Preserve any current hidden toctree decisions from the active branch.

- [ ] **Step 2: Replace building-wind project connection section**

In `docs/source/BuildingStructuralWindResistance.rst`, replace the old `项目连接` section with:

```rst
.. _building-wind-project-support:

公开科研项目支撑 Public Research Project Support
----------------------------------------------

建筑结构抗风方向的政府和纵向项目记录支撑数值风洞、湍动入流、城市/复杂地形风场和高层建筑抗风优化等研究问题。

- 2018-2021 国家，数值大气湍流边界层生成方法的改进与验证，主持。
- 2014-2016 国家，基于粗糙壁面修正的平衡大气边界层紊流风场大涡模拟研究，主持。
- 2014-2016 校级，三维自平衡紊流边界层风场的大涡模拟研究，主持。
- 2013-2015 校级，大气边界层数值风洞中三维紊流风场的大涡模拟研究，主持。
- 2020-2023 市级，考虑风致荷载及响应的高层建筑气动外形优化研究，主持。

企业委托项目证据见 :ref:`engineering-enterprise-project-evidence`。
```

- [ ] **Step 3: Replace floating-wind project connection section**

In `docs/source/FloatingOffshoreWindEnergy.rst`, replace the old `项目连接` section with:

```rst
.. _floating-wind-project-support:

公开科研项目支撑 Public Research Project Support
----------------------------------------------

海上漂浮风电方向的政府和纵向项目记录支撑浮式风机系统分析、浮式混凝土平台、风浪联合模型试验、运动和振动控制等研究问题。

- 2022-2025 省级，面向多设计阶段的浮式风机系统一体化分析与优化方法，主持。
- 2022-2025 省级，FRP-钢复合筋-海水海砂混凝土的半潜式风机基础结构设计方法，参与。
- 2018-2020 市级，浮式海上风机的平衡及振动控制系统研究，骨干成员。
- 2016-2018 市级，柱稳型海上浮式风机基础的关键技术开发，主持。
- 2013-2015 市级，垂直轴风机的主/被动桨距控制策略优化研究，主持。

企业委托项目证据见 :ref:`engineering-enterprise-project-evidence`。
```

- [ ] **Step 4: Run project-support checks that can pass before deleting Projects.rst**

Run:

```bash
python3 -m unittest tests.test_rtd_homepage_projects_redesign.RTDHomepageProjectsRedesignTests.test_project_evidence_migrated_to_receiving_pages -v
```

Expected: FAIL only for missing `engineering-enterprise-project-evidence` and enterprise evidence in `EngineeringApplications.rst`. The research, building, and floating anchors and government project strings should now pass.

- [ ] **Step 5: Commit government project migration**

```bash
git add docs/source/Research.rst docs/source/BuildingStructuralWindResistance.rst docs/source/FloatingOffshoreWindEnergy.rst
git commit -m "docs: move government project support into research pages"
```

---

### Task 4: Move Enterprise Evidence Into Engineering Applications And Delete Projects.rst

**Files:**
- Modify: `docs/source/EngineeringApplications.rst`
- Delete: `docs/source/Projects.rst`
- Test: `tests/test_rtd_homepage_projects_redesign.py`

- [ ] **Step 1: Replace legacy project references under application scenarios**

In `docs/source/EngineeringApplications.rst`, replace each `公开证据` line that references `projects-*` or `:doc:\`Projects\``:

```rst
公开证据：:ref:`building-wind-project-support`、:doc:`BuildingStructuralWindResistance`、:doc:`PublicationsByResearch`。
```

Use that line for `数值风洞与湍动入流`.

```rst
公开证据：:ref:`building-wind-project-support`、:ref:`engineering-enterprise-project-evidence`、:doc:`BuildingStructuralWindResistance`、:doc:`Publications`。
```

Use that line for `高层建筑抗风与优化`.

```rst
公开证据：:ref:`floating-wind-project-support`、:ref:`engineering-enterprise-project-evidence`、:doc:`FloatingOffshoreWindEnergy`、:doc:`PublicationsByResearch`。
```

Use that line for `浮式风机系统一体化分析与优化`.

```rst
公开证据：:ref:`floating-wind-project-support`、:ref:`engineering-enterprise-project-evidence`、:doc:`FloatingOffshoreWindEnergy`。
```

Use that line for `浮式混凝土平台结构设计` and `数值风浪流水池`.

- [ ] **Step 2: Replace the Project Evidence section with enterprise evidence**

Replace the current `项目证据 Project Evidence` section with:

```rst
.. _engineering-enterprise-project-evidence:

企业项目证据 Enterprise Project Evidence
---------------------------------------

以下企业委托项目记录仅展示公开可说明的问题类型、年份和承担角色，不披露未公开确认的合作方名称、当前合作状态、具体设施名称或项目细节。

建筑结构抗风方向
~~~~~~~~~~~~~~~~

- 2016 企业委托，微地形下输电线路微尺度台风风场特性及模型研究，骨干。
- 2016 企业委托，某再生能源发电厂风洞试验及风振分析，骨干。

海上漂浮风电方向
~~~~~~~~~~~~~~~~

- 2016 企业委托，钢筋混凝土半潜式浮力风机系统的风浪联合模型试验研究，骨干。
- 2014 企业委托，基于钢筋混凝土结构的海上风电机组局部浮力基础的初步方案设计，主持。
```

Keep the existing `工程问题交流 Discuss an Engineering Problem` section after the new enterprise evidence section.

- [ ] **Step 3: Delete Projects.rst**

Run:

```bash
git rm docs/source/Projects.rst
```

Expected: `rm 'docs/source/Projects.rst'`.

- [ ] **Step 4: Run the redesign test suite**

Run:

```bash
python3 -m unittest tests.test_rtd_homepage_projects_redesign -v
```

Expected: PASS for all four tests.

- [ ] **Step 5: Run legacy reference scan**

Run:

```bash
rg -n "Projects|项目实践|projects-" docs/source || true
```

Expected: matches only where intentional and not in public `.rst` source. A clean result is acceptable. `docs/source/conf.py` may still contain `logoGroup.png` through `html_logo` and Open Graph metadata; that is allowed.

- [ ] **Step 6: Commit enterprise migration and deletion**

```bash
git add docs/source/EngineeringApplications.rst tests/test_rtd_homepage_projects_redesign.py
git commit -m "docs: merge enterprise project evidence into applications"
```

If `git status --short` shows `D  docs/source/Projects.rst`, it is already staged by `git rm` and included in this commit.

---

### Task 5: Final Docs Verification

**Files:**
- Verify all changed files from Tasks 1-4.

- [ ] **Step 1: Run whitespace check**

```bash
git diff --check
```

Expected: no output and exit code 0.

- [ ] **Step 2: Run the required docs gate**

Use Python 3.12, matching the repo check requirement:

```bash
PYTHON_BIN=/opt/homebrew/bin/python3.12 ./scripts/check-docs.sh
```

Expected final line:

```text
WOEAI docs build succeeded: /tmp/woeai-sphinx-html
```

If `/opt/homebrew/bin/python3.12` does not exist on the executor, run:

```bash
python3 --version
```

Expected: Python 3.12 or newer. Then run:

```bash
./scripts/check-docs.sh
```

- [ ] **Step 3: Inspect the rendered homepage and navigation output**

Run:

```bash
rg -n "把风与海洋工程研究转化为可验证的工程能力|工程应用 Engineering Applications|加入 WOEAI Recruitment|最新学术进展 Latest Academic Progress|Projects|项目实践" /tmp/woeai-sphinx-html/index.html /tmp/woeai-sphinx-html/searchindex.js || true
```

Expected:

- `index.html` contains the new headline.
- `index.html` contains `工程应用 Engineering Applications`, `加入 WOEAI Recruitment`, and `最新学术进展 Latest Academic Progress` in that order.
- No `Projects` or `项目实践` match appears in `index.html`.

- [ ] **Step 4: Optional browser QA**

If a local HTML preview is useful, open:

```text
/tmp/woeai-sphinx-html/index.html
```

Check visually:

- The sidebar still shows the WOEAI logo from `html_logo`.
- The page body does not repeat the logo in the first screen.
- The first visible content emphasizes engineering applications before recruitment.
- The left navigation has no `Projects` entry.

- [ ] **Step 5: Commit any final verification-only fixes**

If Task 5 required small fixes, commit them:

```bash
git add docs/source tests/test_rtd_homepage_projects_redesign.py
git commit -m "docs: finalize RTD homepage project redesign"
```

If no files changed during Task 5, do not create an empty commit.

---

## Completion Criteria

- `docs/source/Projects.rst` is deleted.
- `docs/source/index.rst` no longer contains the page-body `logoGroup.png` image.
- Homepage order is engineering applications, recruitment, latest academic progress.
- `Research.rst`, `BuildingStructuralWindResistance.rst`, and `FloatingOffshoreWindEnergy.rst` contain government/vertical project support.
- `EngineeringApplications.rst` contains enterprise project evidence and no legacy `Projects` links.
- `python3 -m unittest tests.test_rtd_homepage_projects_redesign -v` passes.
- `PYTHON_BIN=/opt/homebrew/bin/python3.12 ./scripts/check-docs.sh` passes, or `./scripts/check-docs.sh` passes under another Python 3.12+ interpreter.

