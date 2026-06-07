# Research Directions And WeChat Magazine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize WOEAI around two public research families, `建筑结构抗风` and `海上漂浮风电`, then add a public-safe one-paper-one-post WeChat article system in the same public repository.

**Architecture:** Keep Sphinx and Read the Docs as the public website backbone. Convert the research information architecture from three first-level direction pages to two first-level families with explicit subdirections, while preserving old URLs as hidden legacy pointer pages. Add `wechat/` as a public-safe content-production layer whose basic unit is one selected paper per WeChat article.

**Tech Stack:** Sphinx, reStructuredText, YAML, Python 3.12, shell checks, GitHub/Read the Docs static publishing.

---

## Scope Check

This plan covers two connected subsystems:

1. Public website research-direction information architecture.
2. WeChat Official Account content workflow.

They belong in one plan because the WeChat system's `research_family` and `subdirection` fields depend on the website taxonomy. Execute the website taxonomy tasks first, then the WeChat tasks.

## File Structure

### Website Taxonomy Files

- Modify: `CONTEXT.md`
  - Responsibility: canonical vocabulary and semantic constraints for future agents.
- Modify: `docs/source/Research.rst`
  - Responsibility: public research overview and first-level direction navigation.
- Create: `docs/source/BuildingStructuralWindResistance.rst`
  - Responsibility: public first-level family page for `建筑结构抗风`.
- Create: `docs/source/FloatingOffshoreWindEnergy.rst`
  - Responsibility: public first-level family page for `海上漂浮风电`.
- Modify: `docs/source/NumericalWindTunnel.rst`
  - Responsibility: legacy URL pointer to `BuildingStructuralWindResistance`.
- Modify: `docs/source/WindResistance.rst`
  - Responsibility: legacy URL pointer to `BuildingStructuralWindResistance`.
- Modify: `docs/source/OffshoreWindEnergy.rst`
  - Responsibility: legacy URL pointer to `FloatingOffshoreWindEnergy`.
- Modify: `docs/source/index.rst`
  - Responsibility: homepage research-direction bullets.
- Modify: `docs/source/TechnicalCollaboration.rst`
  - Responsibility: capability areas aligned with new families.
- Modify: `docs/source/Projects.rst`
  - Responsibility: project proof grouped by new families.
- Modify: `docs/source/Publications.rst`
  - Responsibility: selected highlights grouped by new families.
- Modify: `docs/source/conf.py`
  - Responsibility: SEO metadata reflecting new public direction labels.

### WeChat Content Files

- Modify: `.gitignore`
  - Responsibility: block local WeChat drafts, source images, preview HTML, and secret-bearing files from accidental commits.
- Create: `wechat/README.md`
  - Responsibility: public-safe workflow overview.
- Create: `wechat/STYLE.md`
  - Responsibility: one-paper-one-post editorial style and terminology.
- Create: `wechat/templates/paper-explainer.md`
  - Responsibility: reusable article template.
- Create: `wechat/templates/review-checklist.md`
  - Responsibility: article-level source, copyright, and public-safety review checklist.
- Create: `wechat/topics/building-structural-wind-resistance.yml`
  - Responsibility: topic metadata for `建筑结构抗风`.
- Create: `wechat/topics/floating-offshore-wind-energy.yml`
  - Responsibility: topic metadata for `海上漂浮风电`.
- Create: `wechat/backlog/selected-papers.yml`
  - Responsibility: selected historical paper backlog for one-paper WeChat articles.
- Create: `wechat/checks/public-safety-checklist.md`
  - Responsibility: repository policy for what can and cannot be committed.
- Create: `scripts/check-public-safe-content.py`
  - Responsibility: local check for common secret patterns in committed WeChat content.
- Modify: `scripts/check-docs.sh`
  - Responsibility: run the public-safety check before the strict Sphinx build.

## Canonical Taxonomy

Use these labels exactly in public navigation, WeChat tags, and metadata.

### 一级方向 1: 建筑结构抗风

Subdirections:

1. `数值风洞与湍流入流`
   - Includes urban wind environment.
   - Includes complex terrain wind fields.
   - Includes atmospheric boundary layer turbulence, LES inflow, divergence-free random flow generation, and data-driven wind-field reconstruction.
2. `高层建筑抗风与优化`
   - Includes tall-building wind loads, response prediction, aerodynamic optimization, and wind-induced response extremes.
   - Includes wind-induced vibration control and flow control.
   - Includes historical transmission tower-line and engineering-structure wind-resistance proof, but that material is not a future-facing primary direction.

### 一级方向 2: 海上漂浮风电

Subdirections:

1. `浮式风机系统一体化分析与优化`
2. `浮式混凝土平台结构设计`
3. `数值风浪流水池`

## Task 1: Record The Taxonomy In Project Vocabulary

**Files:**
- Modify: `CONTEXT.md`

- [ ] **Step 1: Inspect current vocabulary**

Run:

```bash
rg -n "Research Family|建筑结构抗风|海上漂浮风电|数值风洞|漂浮风电|建筑抗风" CONTEXT.md
```

Expected before this task: either no match for `建筑结构抗风` and `海上漂浮风电`, or only older planning language outside the canonical vocabulary section.

- [ ] **Step 2: Add canonical research-family terms**

Add this block to `CONTEXT.md` after the existing public-language definitions:

```markdown
**Research Family**:
The canonical public first-level research taxonomy for WOEAI. Use exactly two public research families: `建筑结构抗风` and `海上漂浮风电`. Method names such as `数值风洞` are subdirections, not first-level public families.
_Avoid_: treating `数值风洞`, `结构抗风`, or `海上风电` as peer first-level directions after this taxonomy change

**建筑结构抗风**:
The first canonical public research family. It covers building and structural wind-resistance research, including `数值风洞与湍流入流` and `高层建筑抗风与优化` as subdirections. Urban wind environment and complex terrain wind fields belong under `数值风洞与湍流入流`. Wind-induced vibration control, flow control, and historical tower-line wind-resistance proof belong under `高层建筑抗风与优化` when they are needed as supporting evidence.
_Avoid_: expanding this into a broad all-structures direction in current public navigation

**海上漂浮风电**:
The second canonical public research family. It covers floating offshore wind research, including `浮式风机系统一体化分析与优化`, `浮式混凝土平台结构设计`, and `数值风浪流水池` as subdirections.
_Avoid_: generic `海上风电` when the public page is specifically about floating offshore wind

**One-Paper WeChat Article**:
A WeChat Official Account article whose core unit is one selected paper. It should explain the paper's problem, method, findings, boundaries, engineering significance, DOI, WOEAI publication anchor, and related direction pages.
_Avoid_: forcing every article into a multi-paper theme essay
```

- [ ] **Step 3: Verify vocabulary terms are present**

Run:

```bash
rg -n "Research Family|建筑结构抗风|海上漂浮风电|One-Paper WeChat Article" CONTEXT.md
```

Expected: all four terms appear in `CONTEXT.md`.

- [ ] **Step 4: Commit the vocabulary change**

Run:

```bash
git add CONTEXT.md
git commit -m "docs: define research taxonomy vocabulary"
```

Expected: commit succeeds with only `CONTEXT.md` staged.

## Task 2: Create The Two New Direction Pages

**Files:**
- Create: `docs/source/BuildingStructuralWindResistance.rst`
- Create: `docs/source/FloatingOffshoreWindEnergy.rst`

- [ ] **Step 1: Create `BuildingStructuralWindResistance.rst`**

Create `docs/source/BuildingStructuralWindResistance.rst` with this content:

```rst
建筑结构抗风 Building Structural Wind Resistance
==============================================

建筑结构抗风方向关注建筑与相关工程结构在强风、复杂风场和风致作用下的荷载、响应、优化与控制问题。该方向以数值风洞、湍流入流、物理试验、工程项目和 AI 赋能建模为支撑，服务高层建筑抗风、城市风环境评估和工程结构防灾减灾。

数值风洞与湍流入流
------------------

该子方向关注大气边界层湍流生成、LES 入流条件、城市风环境和复杂地形风场。城市风环境与复杂地形风场归入本子方向，因为它们都依赖可追溯的风场建模、边界条件处理和局部风环境重建。

代表性证据包括：

- :ref:`Precomputed CFD database framework for urban microscale wind prediction <ref-zhao2026-BS>`；
- :ref:`Satellite-imagery urban geometry reconstruction framework <ref-zhao2026-BE>`；
- :ref:`Temporal super-resolution of wind in urban energy applications <ref-tang2026-RE>`；
- :ref:`3D Gaussian Splatting building geometry framework <ref-zhao2025-SCS>`；
- :ref:`A novel vector potential random flow generation method <ref-li2024-POF>`；
- :ref:`A coherence-improved and mass-balanced inflow turbulence generation method <ref-chen2024-JCP>`。

高层建筑抗风与优化
------------------

该子方向关注高层建筑风荷载、结构响应预测、气动外形优化、风致振动控制和流动控制。风致振动控制、流动控制以及既有输电塔线和工程结构抗风研究在公开页面中归入本子方向，作为建筑结构抗风能力的支撑证据。

代表性证据包括：

- :ref:`Graph neural networks for predicting tall-building structural responses <ref-tang2025-JBE>`；
- :ref:`Statistical extremes of 2D vectorial response for wind-excited tall buildings <ref-yang2025-JBE>`；
- :ref:`Implanted-pole tuned liquid damper nonlinear sloshing and vibration mitigation <ref-he2025-POF>`；
- :ref:`Deep reinforcement learning-based active flow control for a tall building <ref-yan2025-POF>`；
- :ref:`Large eddy simulation methods for high-rise building wind load assessment <ref-chen2024-POF>`；
- :ref:`Engineering method for tower-line coupling effects under strong winds <ref-liu2024-JWEIA>`。

项目连接
--------

公开项目记录中包含高层建筑气动外形优化、数值大气湍流边界层生成方法、复杂地形下微尺度台风风场、风洞试验及风振分析等方向。相关项目见 :doc:`Projects`。
```

- [ ] **Step 2: Create `FloatingOffshoreWindEnergy.rst`**

Create `docs/source/FloatingOffshoreWindEnergy.rst` with this content:

```rst
海上漂浮风电 Floating Offshore Wind Energy
=========================================

海上漂浮风电方向关注浮式风机系统、浮式混凝土平台、风浪流环境作用、数值风浪流水池、结构优化和运动/振动控制。该方向连接海洋环境作用、结构动力学、数值优化、物理模型试验和工程系统设计。

浮式风机系统一体化分析与优化
----------------------------

该子方向关注浮式风机系统在不同设计阶段的一体化分析、长期动力响应、系统优化和敏感性评估。

代表性证据包括：

- :ref:`Long-term dynamic optimization of floating wind turbine substructure designs <ref-zhou2023-AE>`；
- :ref:`Global sensitivity study on the semisubmersible substructure of a floating wind turbine <ref-zhou2021-OE>`；
- :ref:`Importance of platform mounting orientation of Y-shaped semi-submersible floating wind turbines <ref-zhou2020-RE>`。

浮式混凝土平台结构设计
----------------------

该子方向关注半潜式浮式平台、浮式混凝土基础、混凝土与钢支撑结构对比、局部浮力基础方案和结构设计优化。

代表性证据包括：

- :ref:`Reinforced-concrete semi-submersible platform structural design and optimization <ref-he2026-OE-structural>`；
- :ref:`Concrete and steel support structure comparison for a Y-shaped semi-submersible floating wind turbine <ref-li2022-SOS>`；
- :ref:`Efficient optimization design method of jacket structures for offshore wind turbines <ref-zheng2023-MS>`。

数值风浪流水池
--------------

该子方向关注风、浪、流联合作用下的模型试验、数值水池、等效静力波浪荷载、动力响应和多物理场多体动力学分析。

代表性证据包括：

- :ref:`Equivalent static wave loads for a delta-shaped semi-submersible 10-MW wind turbine <ref-zheng2025-OE>`；
- :ref:`Wind tunnel and wave flume testing for a 10 MW Y-shaped semi-submersible wind turbine <ref-zheng2023-JRSE>`；
- :ref:`Dynamics of a Y-shaped semi-submersible floating wind turbine <ref-li2022-SOS>`。

图示资料
--------

.. figure:: ../_static/sea_floating_wind_turbine_optimization.png
   :alt: 浮式风机基础的主尺寸优化
   :align: center

   浮式风机基础的主尺寸优化

.. figure:: ../_static/concrete_structure_floating_wind_turbine_optimization.png
   :alt: 混凝土结构浮式风机基础结构的设计与优化
   :align: center

   混凝土结构浮式风机基础结构的设计与优化

.. figure:: ../_static/multiphysics_multibody_model_floating_wind_turbine_optimization.png
   :alt: 多物理场多体动力学分析模型
   :align: center

   浮式风机系统多物理场多体动力学分析模型

项目连接
--------

公开项目记录中包含浮式风机系统一体化分析与优化、半潜式基础结构设计、风浪联合模型试验、运动和振动控制等方向。相关项目见 :doc:`Projects`。
```

- [ ] **Step 3: Check referenced publication anchors exist**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
pub = Path("docs/source/Publications.rst").read_text()
refs = [
    "ref-zhao2026-BS",
    "ref-zhao2026-BE",
    "ref-tang2026-RE",
    "ref-zhao2025-SCS",
    "ref-li2024-POF",
    "ref-chen2024-JCP",
    "ref-tang2025-JBE",
    "ref-yang2025-JBE",
    "ref-he2025-POF",
    "ref-yan2025-POF",
    "ref-chen2024-POF",
    "ref-liu2024-JWEIA",
    "ref-zhou2023-AE",
    "ref-zhou2021-OE",
    "ref-zhou2020-RE",
    "ref-he2026-OE-structural",
    "ref-li2022-SOS",
    "ref-zheng2023-MS",
    "ref-zheng2025-OE",
    "ref-zheng2023-JRSE",
]
missing = [ref for ref in refs if f".. _{ref}:" not in pub]
if missing:
    raise SystemExit("Missing refs: " + ", ".join(missing))
print("All planned publication refs exist")
PY
```

Expected: `All planned publication refs exist`.

- [ ] **Step 4: Run a focused Sphinx build check**

Run:

```bash
./scripts/check-docs.sh
```

Expected: `WOEAI docs build succeeded: /tmp/woeai-sphinx-html`.

- [ ] **Step 5: Commit the new direction pages**

Run:

```bash
git add docs/source/BuildingStructuralWindResistance.rst docs/source/FloatingOffshoreWindEnergy.rst
git commit -m "docs: add two research family pages"
```

Expected: commit succeeds with only the two new pages staged.

## Task 3: Replace First-Level Research Navigation

**Files:**
- Modify: `docs/source/Research.rst`
- Modify: `docs/source/index.rst`
- Modify: `docs/source/NumericalWindTunnel.rst`
- Modify: `docs/source/WindResistance.rst`
- Modify: `docs/source/OffshoreWindEnergy.rst`

- [ ] **Step 1: Replace the research overview**

Replace the body of `docs/source/Research.rst` with this content:

```rst
科研方向 Research
=================

WOEAI 围绕建筑结构抗风和海上漂浮风电开展研究，关注强风、风浪流环境作用与工程结构相互作用。研究工作结合数值模拟、物理试验、工程项目、理论分析和 AI 赋能方法，服务工程结构防灾减灾与海上风电工程创新。

研究主线 Research Logic
-----------------------

- **建筑结构抗风**: 面向建筑和相关工程结构的强风作用、风环境建模、风荷载、结构响应、优化与控制问题。
- **海上漂浮风电**: 面向浮式风机系统、浮式混凝土平台、风浪流环境作用和数值风浪流水池的分析、试验与优化问题。
- **AI 赋能工程方法**: 将图神经网络、深度学习、超分辨率重建、智能几何建模和代理模型用于工程仿真与预测。
- **工程验证闭环**: 通过公开项目和论文记录连接数值方法、物理试验和工程应用。

研究方向 Research Directions
----------------------------

.. toctree::
   :maxdepth: 1

   BuildingStructuralWindResistance
   FloatingOffshoreWindEnergy

近期证据 Selected Proof Points
------------------------------

- 建筑结构抗风中的数值风洞与湍流入流: :ref:`2024 Physics of Fluids <ref-li2024-POF>`、:ref:`2024 Journal of Computational Physics <ref-chen2024-JCP>`、:ref:`2024 Engineering Structures <ref-wang2024-ES>`。
- 建筑结构抗风中的城市风环境和复杂风场: :ref:`2026 Building Simulation <ref-zhao2026-BS>`、:ref:`2026 Building and Environment <ref-zhao2026-BE>`、:ref:`2025 Sustainable Cities and Society <ref-zhao2025-SCS>`。
- 建筑结构抗风中的高层建筑响应与优化: :ref:`2025 Journal of Building Engineering <ref-tang2025-JBE>`、:ref:`2025 Journal of Building Engineering <ref-yang2025-JBE>`、:ref:`2025 Physics of Fluids <ref-he2025-POF>`。
- 海上漂浮风电中的系统分析、平台结构和风浪流作用: :ref:`2026 Ocean Engineering <ref-he2026-OE-structural>`、:ref:`2025 Ocean Engineering <ref-zheng2025-OE>`、:ref:`2023 Applied Energy <ref-zhou2023-AE>`。

更多论文、项目和团队信息见 :doc:`Publications`、:doc:`Projects` 和 :doc:`People`。
```

- [ ] **Step 2: Update homepage research bullets**

In `docs/source/index.rst`, replace the three bullets under `研究方向 Research Directions` with:

```rst
- :doc:`BuildingStructuralWindResistance`: 建筑结构抗风，包括数值风洞与湍流入流、高层建筑抗风与优化；
- :doc:`FloatingOffshoreWindEnergy`: 海上漂浮风电，包括浮式风机系统一体化分析与优化、浮式混凝土平台结构设计、数值风浪流水池。
```

- [ ] **Step 3: Convert `NumericalWindTunnel.rst` to a hidden legacy pointer**

Replace `docs/source/NumericalWindTunnel.rst` with:

```rst
:orphan:

数值风洞 Numerical Wind Tunnel
==============================

数值风洞与湍流入流现在作为 :doc:`BuildingStructuralWindResistance` 下的子方向维护。城市风环境与复杂地形风场也归入该子方向。

请阅读 :doc:`BuildingStructuralWindResistance`。
```

- [ ] **Step 4: Convert `WindResistance.rst` to a hidden legacy pointer**

Replace `docs/source/WindResistance.rst` with:

```rst
:orphan:

结构抗风 Structural Wind Resistance
===================================

结构抗风内容现在并入 :doc:`BuildingStructuralWindResistance`。公开一级方向使用 `建筑结构抗风`。

请阅读 :doc:`BuildingStructuralWindResistance`。
```

- [ ] **Step 5: Convert `OffshoreWindEnergy.rst` to a hidden legacy pointer**

Replace `docs/source/OffshoreWindEnergy.rst` with:

```rst
:orphan:

海上风电 Offshore Wind Energy
=============================

海上风电相关内容现在聚焦为 :doc:`FloatingOffshoreWindEnergy`。公开一级方向使用 `海上漂浮风电`。

请阅读 :doc:`FloatingOffshoreWindEnergy`。
```

- [ ] **Step 6: Verify old first-level pages are no longer in the research toctree**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
research = Path("docs/source/Research.rst").read_text()
for old in ["NumericalWindTunnel", "WindResistance", "OffshoreWindEnergy"]:
    if old in research:
        raise SystemExit(f"Old first-level direction still in Research.rst: {old}")
for new in ["BuildingStructuralWindResistance", "FloatingOffshoreWindEnergy"]:
    if new not in research:
        raise SystemExit(f"New first-level direction missing: {new}")
print("Research navigation uses the two new families")
PY
```

Expected: `Research navigation uses the two new families`.

- [ ] **Step 7: Run strict docs check**

Run:

```bash
./scripts/check-docs.sh
```

Expected: `WOEAI docs build succeeded: /tmp/woeai-sphinx-html`.

- [ ] **Step 8: Commit navigation changes**

Run:

```bash
git add docs/source/Research.rst docs/source/index.rst docs/source/NumericalWindTunnel.rst docs/source/WindResistance.rst docs/source/OffshoreWindEnergy.rst
git commit -m "docs: update research direction navigation"
```

Expected: commit succeeds with only the navigation and legacy pointer pages staged.

## Task 4: Align Proof And Collaboration Pages

**Files:**
- Modify: `docs/source/TechnicalCollaboration.rst`
- Modify: `docs/source/Projects.rst`
- Modify: `docs/source/Publications.rst`
- Modify: `docs/source/conf.py`

- [ ] **Step 1: Update `TechnicalCollaboration.rst` capability areas**

Replace the `技术合作方向 Capability Areas` section in `docs/source/TechnicalCollaboration.rst` with:

```rst
技术合作方向 Capability Areas
--------------------------------

建筑结构抗风
~~~~~~~~~~~~

- 数值风洞与湍流入流，包括大气边界层湍流生成、LES 入流和城市/复杂地形风场；
- 高层建筑抗风与优化，包括风致荷载、结构响应、气动外形优化和减振控制；
- 面向建筑风场、建筑几何和数值模拟流程的 AI 赋能建模方法。

海上漂浮风电
~~~~~~~~~~~~

- 浮式风机系统一体化分析与优化；
- 浮式混凝土平台结构设计；
- 数值风浪流水池、风浪流联合作用和动力响应分析；
- 浮式风机运动和振动控制。
```

- [ ] **Step 2: Update `Projects.rst` capability map**

Replace the three bullets under `能力地图 Capability Map` with:

```rst
- **建筑结构抗风**: 数值风洞与湍流入流、城市风环境、复杂地形风场、高层建筑气动外形优化、风洞试验与风振分析。
- **海上漂浮风电**: 浮式风机系统优化、浮式混凝土平台结构设计、风浪联合模型试验、数值风浪流水池、运动和振动控制。
```

Replace the `相关页面 Related Pages` list with:

```rst
- :doc:`TechnicalCollaboration`
- :doc:`BuildingStructuralWindResistance`
- :doc:`FloatingOffshoreWindEnergy`
```

- [ ] **Step 3: Update `Publications.rst` selected highlights**

Replace the bullets under `精选证据 Selected Highlights` with:

```rst
- 建筑结构抗风 / 数值风洞与湍流入流: :ref:`[51] vector-potential random flow generation <ref-li2024-POF>`、:ref:`[50] coherence-improved and mass-balanced inflow turbulence <ref-chen2024-JCP>`、:ref:`[55] weak recycling inflow turbulence generator <ref-wang2024-ES>`。
- 建筑结构抗风 / 城市风环境与复杂地形风场: :ref:`[72] precomputed CFD database for urban microscale wind <ref-zhao2026-BS>`、:ref:`[74] satellite-imagery urban geometry reconstruction <ref-zhao2026-BE>`、:ref:`[61] 3D Gaussian Splatting building geometry <ref-zhao2025-SCS>`。
- 建筑结构抗风 / 高层建筑抗风与优化: :ref:`[64] graph neural networks for tall-building response <ref-tang2025-JBE>`、:ref:`[68] 2D vectorial response extremes <ref-yang2025-JBE>`、:ref:`[69] implanted-pole tuned liquid damper <ref-he2025-POF>`。
- 海上漂浮风电 / 系统分析与结构设计: :ref:`[71] reinforced-concrete semi-submersible platform optimization <ref-he2026-OE-structural>`、:ref:`[48] floating wind turbine substructure optimization <ref-zhou2023-AE>`、:ref:`[33] concrete and steel support structure comparison <ref-li2022-SOS>`。
- 海上漂浮风电 / 数值风浪流水池: :ref:`[66] equivalent static wave loads for semi-submersible turbines <ref-zheng2025-OE>`、:ref:`[42] wind tunnel and wave flume testing <ref-zheng2023-JRSE>`。
```

- [ ] **Step 4: Update SEO metadata**

In `docs/source/conf.py`, replace `html_meta['description']` and `html_meta['keywords']` with:

```python
    'description': 'WOEAI - 哈尔滨工业大学（深圳）Wind and Ocean Engineering with AI 研究团队。面向招生、技术合作、建筑结构抗风、海上漂浮风电、数值风洞与 AI 赋能工程研究。',
    'keywords': 'WOEAI, 招生, 技术合作, 建筑结构抗风, 海上漂浮风电, 数值风洞, 湍流入流, 高层建筑抗风, 浮式风机, 浮式混凝土平台, 风浪流水池, 哈尔滨工业大学, HIT, 李朝',
```

- [ ] **Step 5: Verify no public page still presents the old three-direction taxonomy**

Run:

```bash
rg -n "研究方向页|三个研究方向|NumericalWindTunnel|WindResistance|OffshoreWindEnergy|数值风洞、结构抗风与海上风电|数值风洞, 结构抗风" docs/source README.rst CONTEXT.md
```

Expected: matches only in orphan legacy pointer pages or historical planning documents. If a match appears in `Research.rst`, `index.rst`, `TechnicalCollaboration.rst`, `Projects.rst`, `Publications.rst`, or `conf.py`, update that file before continuing.

- [ ] **Step 6: Run strict docs check**

Run:

```bash
./scripts/check-docs.sh
git diff --check
```

Expected:

```text
WOEAI docs build succeeded: /tmp/woeai-sphinx-html
```

`git diff --check` prints no output.

- [ ] **Step 7: Commit proof-page alignment**

Run:

```bash
git add docs/source/TechnicalCollaboration.rst docs/source/Projects.rst docs/source/Publications.rst docs/source/conf.py
git commit -m "docs: align proof pages with research taxonomy"
```

Expected: commit succeeds with only the four aligned files staged.

## Task 5: Add Public-Safe WeChat Repository Structure

**Files:**
- Modify: `.gitignore`
- Create: `wechat/README.md`
- Create: `wechat/STYLE.md`
- Create: `wechat/templates/paper-explainer.md`
- Create: `wechat/templates/review-checklist.md`
- Create: `wechat/topics/building-structural-wind-resistance.yml`
- Create: `wechat/topics/floating-offshore-wind-energy.yml`
- Create: `wechat/checks/public-safety-checklist.md`

- [ ] **Step 1: Add WeChat local-only ignores**

Append this block to `.gitignore`:

```gitignore

### WOEAI WeChat local-only material ###
wechat/.local/
wechat/private/
wechat/review-notes/
wechat/wechat-preview-html/
wechat/source-images/
wechat/secrets/
*.wechat-token
*.appsecret
```

- [ ] **Step 2: Create public directory structure**

Run:

```bash
mkdir -p wechat/templates wechat/topics wechat/backlog wechat/articles/draft-public-safe wechat/articles/published wechat/assets/public wechat/checks
```

Expected: command succeeds and creates only public-safe directories.

- [ ] **Step 3: Create `wechat/README.md`**

Create `wechat/README.md` with:

```markdown
# WOEAI WeChat Research Magazine

This directory manages public-safe WeChat Official Account article material for WOEAI.

The basic unit is one selected paper, one article. Each article must be source-bounded by Zotero metadata, the WOEAI website, and public publication anchors.

## Research Families

- `建筑结构抗风`
- `海上漂浮风电`

## Public Boundary

This repository is public. Anything committed here is treated as public.

Do not commit:

- WeChat AppSecret, access tokens, cookies, preview credentials, or API keys.
- Zotero API keys or private library credentials.
- private review notes.
- unpublished partner names or project details.
- copyrighted publisher figures unless reuse rights are confirmed.
- local WeChat preview HTML.
- source image files that are not approved for public release.

Use `wechat/articles/draft-public-safe/` only for drafts that are safe to expose before publication. Keep private working material under ignored local paths such as `wechat/.local/`.

## Workflow

1. Select a paper in `wechat/backlog/selected-papers.yml`.
2. Create a draft from `wechat/templates/paper-explainer.md`.
3. Verify the paper's WOEAI site reference and DOI.
4. Complete the source, copyright, and public-safety checklist.
5. Render the Markdown in a WeChat Markdown editor such as doocs/md.
6. Publish manually in the WeChat backend.
7. Record the published URL in `wechat/backlog/selected-papers.yml` and, when useful, in `wechat/index.yml`.
```

- [ ] **Step 4: Create `wechat/STYLE.md`**

Create `wechat/STYLE.md` with:

```markdown
# WOEAI WeChat Style Guide

## Article Unit

Use one selected paper per article.

Do not turn every article into a multi-paper theme essay. Related papers may appear in the `延伸阅读` section.

## Default Structure

1. `论文信息`
2. `研究问题`
3. `方法贡献`
4. `关键发现`
5. `工程意义`
6. `适用边界`
7. `延伸阅读`
8. `联系入口`

## Tone

- Scholarly first.
- Engineering relevance second.
- No hype.
- No unsupported partner names or project claims.
- Use DOI and WOEAI site references for traceability.

## Research Family Labels

- `建筑结构抗风`
- `海上漂浮风电`

## Subdirection Labels

建筑结构抗风:

- `数值风洞与湍流入流`
- `高层建筑抗风与优化`

海上漂浮风电:

- `浮式风机系统一体化分析与优化`
- `浮式混凝土平台结构设计`
- `数值风浪流水池`
```

- [ ] **Step 5: Create `wechat/templates/paper-explainer.md`**

Create `wechat/templates/paper-explainer.md` with:

```markdown
---
title:
status: draft-public-safe
research_family:
subdirection:
publication_ref:
zotero_key:
doi:
original_year:
wechat_status: not_started
source_checked: false
copyright_checked: false
public_safety_checked: false
published_url:
---

# 论文解读 | <填写中文标题>

## 论文信息

- 论文题名:
- 作者:
- 期刊:
- 年份:
- DOI:
- WOEAI 官网条目:

## 研究问题

这篇论文解决的工程或科学问题是:

## 方法贡献

论文提出或改进的方法是:

## 关键发现

最值得读者注意的结果是:

## 工程意义

对工程技术负责人有启发的是:

## 适用边界

这篇论文没有证明或不应被夸大的地方是:

## 延伸阅读

- WOEAI 相关方向页:
- WOEAI 相关论文:

## 联系入口

- Website: https://winddee.cn
- Email: lichaosz@hit.edu.cn
```

- [ ] **Step 6: Create `wechat/templates/review-checklist.md`**

Create `wechat/templates/review-checklist.md` with:

```markdown
# WeChat Article Review Checklist

## Source

- [ ] DOI matches the WOEAI publication record.
- [ ] WOEAI publication anchor exists in `docs/source/Publications.rst`.
- [ ] Journal, year, authors, and metrics are copied from source-bounded data.
- [ ] Related direction page exists.

## Copyright

- [ ] No publisher PDF figure is copied without confirmed reuse rights.
- [ ] All diagrams are original, redrawn, generated for this article, or public-safe.
- [ ] Image source is recorded in the article notes or asset metadata.

## Public Safety

- [ ] No WeChat AppSecret, token, cookie, or credential appears.
- [ ] No Zotero API key appears.
- [ ] No private partner name appears.
- [ ] No unconfirmed project status appears.
- [ ] No private review comment appears.
- [ ] The draft is safe to expose in a public GitHub repository.
```

- [ ] **Step 7: Create topic metadata files**

Create `wechat/topics/building-structural-wind-resistance.yml`:

```yaml
id: building-structural-wind-resistance
label_cn: 建筑结构抗风
label_en: Building Structural Wind Resistance
subdirections:
  - id: numerical-wind-tunnel-and-turbulent-inflow
    label_cn: 数值风洞与湍流入流
    includes:
      - 城市风环境
      - 复杂地形风场
      - 大气边界层湍流
      - LES 入流
  - id: tall-building-wind-resistance-and-optimization
    label_cn: 高层建筑抗风与优化
    includes:
      - 风致振动控制与流动控制
      - 历史输电塔线及工程结构抗风证据
```

Create `wechat/topics/floating-offshore-wind-energy.yml`:

```yaml
id: floating-offshore-wind-energy
label_cn: 海上漂浮风电
label_en: Floating Offshore Wind Energy
subdirections:
  - id: integrated-floating-wind-turbine-analysis-and-optimization
    label_cn: 浮式风机系统一体化分析与优化
  - id: floating-concrete-platform-structural-design
    label_cn: 浮式混凝土平台结构设计
  - id: numerical-wind-wave-current-basin
    label_cn: 数值风浪流水池
```

- [ ] **Step 8: Create public-safety checklist**

Create `wechat/checks/public-safety-checklist.md` with:

```markdown
# Public Safety Checklist

This repository is public. Every committed file must be safe to expose.

## Never Commit

- WeChat AppSecret.
- WeChat access token or refresh token.
- Zotero API key.
- cookies or preview credentials.
- private partner names.
- unconfirmed project status.
- internal review notes.
- local preview HTML.
- publisher-owned figures without confirmed reuse rights.

## Allowed

- public-safe article drafts.
- published article Markdown.
- original diagrams approved for public release.
- WOEAI website links.
- DOI links.
- Zotero item keys when used as public workflow identifiers.
```

- [ ] **Step 9: Commit WeChat scaffold**

Run:

```bash
git add .gitignore wechat/README.md wechat/STYLE.md wechat/templates/paper-explainer.md wechat/templates/review-checklist.md wechat/topics/building-structural-wind-resistance.yml wechat/topics/floating-offshore-wind-energy.yml wechat/checks/public-safety-checklist.md
git commit -m "docs: scaffold public-safe wechat workflow"
```

Expected: commit succeeds with only the scaffold files staged.

## Task 6: Add Selected Paper Backlog

**Files:**
- Create: `wechat/backlog/selected-papers.yml`

- [ ] **Step 1: Create starter selected-paper backlog**

Create `wechat/backlog/selected-papers.yml` with:

```yaml
schema_version: 1
description: Public-safe backlog of selected WOEAI papers for one-paper WeChat articles.
selection_policy:
  - Use one selected paper per article.
  - Include historical papers when they still support current WOEAI research identity, recruitment, technical collaboration, or academic credibility.
  - Confirm final inclusion before writing each article.
items:
  - publication_ref: ref-zhao2026-BS
    zotero_key: CGKPKZ8I
    title: A fast prediction framework for urban microscale wind environment based on precomputed CFD database
    research_family: 建筑结构抗风
    subdirection: 数值风洞与湍流入流
    original_year: 2026
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-zhao2026-BE
    zotero_key: RLAA46YB
    title: A novel framework for urban geometry rapid reconstruction utilizing high-resolution stereo satellite imagery for wind environment assessment
    research_family: 建筑结构抗风
    subdirection: 数值风洞与湍流入流
    original_year: 2026
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-zhao2025-SCS
    zotero_key: V6PLJENN
    title: A novel framework utilizing 3D Gaussian Splatting to construct building geometry for urban wind simulations
    research_family: 建筑结构抗风
    subdirection: 数值风洞与湍流入流
    original_year: 2025
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-li2024-POF
    zotero_key: 2YG78T62
    title: A novel vector potential random flow generation method for synthesizing divergence-free homogeneous isotropic turbulence with arbitrary spectra
    research_family: 建筑结构抗风
    subdirection: 数值风洞与湍流入流
    original_year: 2024
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-chen2024-JCP
    zotero_key: Y76UWP9R
    title: A coherence-improved and mass-balanced inflow turbulence generation method for large eddy simulation
    research_family: 建筑结构抗风
    subdirection: 数值风洞与湍流入流
    original_year: 2024
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-tang2025-JBE
    zotero_key: 4BCF65NB
    title: Training and application of graph neural networks for predicting structural responses targeted at tall building structures
    research_family: 建筑结构抗风
    subdirection: 高层建筑抗风与优化
    original_year: 2025
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-yang2025-JBE
    zotero_key: YZ2D62NB
    title: Statistical extremes of 2D vectorial response for wind-excited tall buildings
    research_family: 建筑结构抗风
    subdirection: 高层建筑抗风与优化
    original_year: 2025
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-he2025-POF
    zotero_key: ES37XMDV
    title: Numerical investigation of nonlinear sloshing features and vibration mitigation efficiency of the implanted pole tuned liquid damper
    research_family: 建筑结构抗风
    subdirection: 高层建筑抗风与优化
    original_year: 2025
    repost_priority: medium
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-he2026-OE-structural
    zotero_key: EMID6LAJ
    title: Structural design and optimization of a novel semi-submersible floating offshore wind turbine platform using reinforced concrete
    research_family: 海上漂浮风电
    subdirection: 浮式混凝土平台结构设计
    original_year: 2026
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-zheng2025-OE
    zotero_key: 5W2SZJUT
    title: Evaluating equivalent static wave loads for a delta-shaped semi-submersible 10-MW wind turbine
    research_family: 海上漂浮风电
    subdirection: 数值风浪流水池
    original_year: 2025
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-zhou2023-AE
    zotero_key: 3LWVP7B7
    title: Evaluation of floating wind turbine substructure designs by using long-term dynamic optimization
    research_family: 海上漂浮风电
    subdirection: 浮式风机系统一体化分析与优化
    original_year: 2023
    repost_priority: high
    wechat_status: selected
    published_url: ""
  - publication_ref: ref-li2022-SOS
    zotero_key: 5AT7UEWV
    title: Dynamics of a Y-shaped semi-submersible floating wind turbine: a comparison of concrete and steel support structures
    research_family: 海上漂浮风电
    subdirection: 浮式混凝土平台结构设计
    original_year: 2022
    repost_priority: medium
    wechat_status: selected
    published_url: ""
```

- [ ] **Step 2: Verify backlog refs exist**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re
pub = Path("docs/source/Publications.rst").read_text()
backlog = Path("wechat/backlog/selected-papers.yml").read_text()
refs = re.findall(r"publication_ref: (ref-[A-Za-z0-9-]+)", backlog)
missing = [ref for ref in refs if f".. _{ref}:" not in pub]
if missing:
    raise SystemExit("Missing refs: " + ", ".join(missing))
print(f"Backlog refs verified: {len(refs)}")
PY
```

Expected: `Backlog refs verified: 12`.

- [ ] **Step 3: Verify backlog uses only canonical families and subdirections**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path("wechat/backlog/selected-papers.yml").read_text()
allowed_families = {"建筑结构抗风", "海上漂浮风电"}
allowed_subdirections = {
    "数值风洞与湍流入流",
    "高层建筑抗风与优化",
    "浮式风机系统一体化分析与优化",
    "浮式混凝土平台结构设计",
    "数值风浪流水池",
}
families = [line.split(": ", 1)[1] for line in text.splitlines() if line.strip().startswith("research_family: ")]
subdirections = [line.split(": ", 1)[1] for line in text.splitlines() if line.strip().startswith("subdirection: ")]
bad_families = sorted(set(families) - allowed_families)
bad_subdirections = sorted(set(subdirections) - allowed_subdirections)
if bad_families or bad_subdirections:
    raise SystemExit(f"Bad families={bad_families}; bad subdirections={bad_subdirections}")
print("Backlog taxonomy labels verified")
PY
```

Expected: `Backlog taxonomy labels verified`.

- [ ] **Step 4: Commit selected-paper backlog**

Run:

```bash
git add wechat/backlog/selected-papers.yml
git commit -m "docs: add selected wechat paper backlog"
```

Expected: commit succeeds with only the backlog file staged.

## Task 7: Add Public-Safety Check To The Verification Script

**Files:**
- Create: `scripts/check-public-safe-content.py`
- Modify: `scripts/check-docs.sh`

- [ ] **Step 1: Create public-safety checker**

Create `scripts/check-public-safe-content.py` with:

```python
#!/usr/bin/env python3
"""Check public WeChat content for obvious secret patterns."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = [ROOT / "wechat"]

SECRET_PATTERNS = [
    re.compile(r"(?i)appsecret\s*[:=]\s*['\"]?[A-Za-z0-9_-]{8,}"),
    re.compile(r"(?i)access_token\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{12,}"),
    re.compile(r"(?i)refresh_token\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{12,}"),
    re.compile(r"(?i)zotero[-_ ]?api[-_ ]?key\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{8,}"),
    re.compile(r"(?i)wechat[-_ ]?(token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{8,}"),
]

IGNORED_DIR_NAMES = {
    ".local",
    "private",
    "review-notes",
    "wechat-preview-html",
    "source-images",
    "secrets",
}


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_DIR_NAMES for part in path.parts)


def main() -> int:
    findings: list[str] = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if should_skip(path) or not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".rst", ".yml", ".yaml", ".txt"}:
                continue
            text = path.read_text(encoding="utf-8")
            for pattern in SECRET_PATTERNS:
                for match in pattern.finditer(text):
                    line_no = text.count("\n", 0, match.start()) + 1
                    rel = path.relative_to(ROOT)
                    findings.append(f"{rel}:{line_no}: possible secret pattern")
    if findings:
        print("Public-safety check failed:", file=sys.stderr)
        for finding in findings:
            print(finding, file=sys.stderr)
        return 1
    print("Public-safety check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Make checker executable**

Run:

```bash
chmod +x scripts/check-public-safe-content.py
```

Expected: command succeeds.

- [ ] **Step 3: Wire checker into `scripts/check-docs.sh`**

Insert this line after the Python version check block and before creating the virtual environment:

```bash
"${PYTHON_BIN}" "${ROOT_DIR}/scripts/check-public-safe-content.py"
```

The top portion of `scripts/check-docs.sh` should then contain:

```bash
"${PYTHON_BIN}" - <<'PY'
import sys

if sys.version_info < (3, 12):
    raise SystemExit("Python 3.12+ is required for WOEAI docs checks")
PY
"${PYTHON_BIN}" "${ROOT_DIR}/scripts/check-public-safe-content.py"
"${PYTHON_BIN}" -m venv "${VENV_DIR}"
```

- [ ] **Step 4: Run the public-safety check directly**

Run:

```bash
python3 scripts/check-public-safe-content.py
```

Expected: `Public-safety check passed`.

- [ ] **Step 5: Run full docs check**

Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
Public-safety check passed
WOEAI docs build succeeded: /tmp/woeai-sphinx-html
```

- [ ] **Step 6: Commit verification change**

Run:

```bash
git add scripts/check-public-safe-content.py scripts/check-docs.sh
git commit -m "build: check public-safe wechat content"
```

Expected: commit succeeds with only the checker and docs-check script staged.

## Task 8: Final Verification And Handoff

**Files:**
- No new files.

- [ ] **Step 1: Run all required checks**

Run:

```bash
./scripts/check-docs.sh
git diff --check
python3 - <<'PY'
from pathlib import Path
required = [
    "docs/source/BuildingStructuralWindResistance.rst",
    "docs/source/FloatingOffshoreWindEnergy.rst",
    "wechat/README.md",
    "wechat/STYLE.md",
    "wechat/backlog/selected-papers.yml",
    "scripts/check-public-safe-content.py",
]
missing = [path for path in required if not Path(path).exists()]
if missing:
    raise SystemExit("Missing files: " + ", ".join(missing))
print("Required files exist")
PY
```

Expected:

```text
Public-safety check passed
WOEAI docs build succeeded: /tmp/woeai-sphinx-html
Required files exist
```

`git diff --check` prints no output.

- [ ] **Step 2: Inspect generated HTML pages**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
build = Path("/tmp/woeai-sphinx-html")
for name in ["Research.html", "BuildingStructuralWindResistance.html", "FloatingOffshoreWindEnergy.html", "TechnicalCollaboration.html", "Projects.html", "Publications.html"]:
    path = build / name
    if not path.exists():
        raise SystemExit(f"Missing generated page: {path}")
print("Generated HTML pages exist")
PY
```

Expected: `Generated HTML pages exist`.

- [ ] **Step 3: Confirm current git status**

Run:

```bash
git status --short
```

Expected: no output.

- [ ] **Step 4: Report implementation result**

Report:

```text
Implemented the WOEAI research taxonomy and WeChat public-safe workflow.
Top-level families are 建筑结构抗风 and 海上漂浮风电.
WeChat workflow uses one selected paper per article.
Checks passed: ./scripts/check-docs.sh and git diff --check.
```

## Self-Review

Spec coverage:

- Two top-level directions are covered by Tasks 1-4.
- Requested subdirection grouping is covered in the canonical taxonomy, direction pages, topic YAML files, and backlog metadata.
- One-paper-one-post WeChat workflow is covered in Tasks 5-7.
- Secret and key safety is covered in `.gitignore`, public-safety checklist, and `scripts/check-public-safe-content.py`.
- Read the Docs/Sphinx verification is covered in Tasks 2-4, 7, and 8.

Placeholder scan:

- No deferred-detail markers.
- No deferred code steps.
- No unspecified tests.
- No unbounded edge-case instructions.

Type and label consistency:

- Research families use `建筑结构抗风` and `海上漂浮风电`.
- Subdirections use `数值风洞与湍流入流`, `高层建筑抗风与优化`, `浮式风机系统一体化分析与优化`, `浮式混凝土平台结构设计`, and `数值风浪流水池`.
- File names use existing Sphinx CamelCase page style.
