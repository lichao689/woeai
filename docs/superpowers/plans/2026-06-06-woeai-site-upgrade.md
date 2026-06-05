# WOEAI Site Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the WOEAI repository from a tutorial-derived Sphinx site into a maintainable, verifiable, bilingual research group website that future agents can safely evolve.

**Architecture:** Keep Sphinx and ReadTheDocs as the publishing backbone for the first upgrade cycle. Treat `docs/source/*.rst` as the canonical content layer, `docs/_static/` as the media layer, and lightweight shell/CI checks as the verification layer. Do not migrate to a custom frontend until the content architecture, build contract, and public navigation are clean.

**Tech Stack:** Python 3.12, Sphinx 9.0.4, sphinx-rtd-theme 3.1.0, sphinx-sitemap 2.9.0, ReadTheDocs, reStructuredText, GitHub Actions.

---

## Current Project Diagnosis

### Repository Shape

This is a docs-only website repository at `/Volumes/WorkSSD/codes/woeai`.

Core files:

- `docs/source/conf.py`: Sphinx project, theme, SEO, sitemap, search, analytics, logo.
- `docs/source/index.rst`: public homepage.
- `docs/source/People.rst`: group leader and students.
- `docs/source/Publications.rst`: publication list, currently the strongest content asset.
- `docs/source/Projects.rst`: government and enterprise project list.
- `docs/source/NumericalWindTunnel.rst`: research direction page, mostly headings.
- `docs/source/WindResistance.rst`: research direction page, mostly headings.
- `docs/source/OffshoreWindEnergy.rst`: research direction page, includes three figures.
- `docs/source/Teaching.rst`: teaching page.
- `docs/source/GroupNews.rst`: hidden by `:orphan:`, currently thin.
- `docs/source/usage.rst` and `docs/source/api.rst`: ReadTheDocs tutorial leftovers.
- `docs/_static/`: logo, QR code, research figures, custom CSS.
- `.readthedocs.yaml`: ReadTheDocs build with Python 3.12 and `fail_on_warning: true`.
- `pyproject.toml`: misleading package metadata; `pip install .` fails because there is no `woeai` Python module.

Verified behavior:

- Strict HTML build succeeds in a temporary venv with:

```bash
/tmp/woeai-docs-venv/bin/sphinx-build -b html -W docs/source /tmp/woeai-sphinx-check-html
```

- Global Python currently lacks Sphinx, so agents need an explicit local setup path.
- `pip install .` fails with `ValueError: No file/folder found for module woeai`.
- `sphinx-build -M latexpdf docs/source ... -W` generates LaTeX but fails at PDF creation because `latexmk` is not installed locally.
- Generated HTML still exposes `Usage`, `API`, `Lumache`, `Documentation coming soon`, and `For example` text.

### Strategic Reading

The site is not primarily a software documentation site. It is a public research group presence for "Wind & Ocean Engineering empowered by AI". The important audiences are:

- Prospective master, PhD, and postdoctoral applicants.
- Academic collaborators looking for research areas and representative work.
- Industry partners looking for engineering capability and project evidence.
- Search engines and AI crawlers looking for stable institutional facts.
- Group members or agents maintaining publications, news, and pages.

The current implementation passes Sphinx, but the public meaning is uneven:

- The homepage mixes group intro, recruiting, research links, template copy, navigation, and contact details.
- Research direction pages do not yet explain capabilities, methods, representative results, or project connections.
- Publications are rich but formatted as a flat list; users cannot quickly see highlights, themes, years, or representative AI-enabled work.
- GroupNews exists but is hidden, which removes the natural "freshness" signal.
- README and `pyproject.toml` can mislead future agents into treating this as a Python package.
- There is no project-level agent contract, local verification script, or CI workflow for docs.

The best upgrade path is therefore content-first and guardrail-first:

1. Clean the public site so it no longer shows template residue.
2. Make the repository unambiguous for future agents.
3. Add one-command verification.
4. Strengthen research pages using facts already present in publications/projects.
5. Improve presentation within Sphinx before considering a custom web framework.

---

## Transformation Principles

- Preserve current public URLs for valuable pages where possible: `People.html`, `Publications.html`, `Projects.html`, `NumericalWindTunnel.html`, `WindResistance.html`, `OffshoreWindEnergy.html`, `Teaching.html`.
- Remove public tutorial pages that damage credibility: `usage.html` and `api.html`.
- Do not invent scientific facts, student names, funding details, or publication metadata.
- When content is missing, restructure around existing verified facts instead of adding vague filler.
- Keep Chinese and English paired in headings and key labels.
- Use Sphinx warnings as release blockers.
- Prefer small commits grouped by behavior: cleanup, agent contract, content architecture, research content, visual polish, CI.
- Defer a full frontend migration until the Sphinx version is coherent and validated.

---

## File Responsibility Map

### Files to Create

- `AGENTS.md`: repository-specific operating instructions for future agents.
- `scripts/check-docs.sh`: one-command local verification in an isolated venv.
- `.github/workflows/docs.yml`: CI verification for strict Sphinx HTML build.
- `docs/source/Recruitment.rst`: dedicated recruitment page split from homepage.
- `docs/source/Research.rst`: overview page linking the three research directions.
- `docs/source/Contact.rst`: dedicated contact page with website, email, address, and QR code.

### Files to Modify

- `README.rst`: replace ReadTheDocs tutorial template with project-specific documentation.
- `docs/source/index.rst`: convert to concise public homepage.
- `docs/source/conf.py`: tighten project metadata, SEO, navigation behavior, optional LaTeX settings.
- `docs/source/GroupNews.rst`: make it a visible, useful news page or remove it from the public build.
- `docs/source/NumericalWindTunnel.rst`: expand from headings into evidence-backed research content.
- `docs/source/WindResistance.rst`: expand from headings into evidence-backed research content.
- `docs/source/OffshoreWindEnergy.rst`: add explanatory structure around existing figures.
- `docs/source/People.rst`: remove placeholder text and clarify blank sections.
- `docs/source/Publications.rst`: fix broken emphasis around author/corresponding-author markers.
- `docs/source/Projects.rst`: normalize punctuation and trailing whitespace.
- `docs/source/Teaching.rst`: keep concise, optionally add course grouping text.
- `docs/_static/custom.css`: modest readability and homepage improvements within the RTD theme.
- `.readthedocs.yaml`: keep docs-only install, decide whether PDF remains a required format.
- `.gitignore`: add local venv/cache names used by verification script if needed.

### Files to Delete

- `docs/source/usage.rst`: current content is a tutorial artifact.
- `docs/source/api.rst`: current content is a tutorial artifact.
- `pyproject.toml`: current package metadata is false for a docs-only repository.

Deletion note: if the team wants to preserve `usage.html` or `api.html` for old external links, convert them into hidden redirect/landing pages in a separate task. The default recommendation is deletion because the existing public pages are misleading.

---

## Phase 0: Baseline and Safety

### Task 0.1: Confirm Clean Baseline

**Files:** none.

- [ ] Run:

```bash
git status --short --branch
```

Expected:

```text
## main...origin/main
```

- [ ] Run:

```bash
python3 -m venv /tmp/woeai-docs-venv
/tmp/woeai-docs-venv/bin/python -m pip install --upgrade pip
/tmp/woeai-docs-venv/bin/python -m pip install -r docs/requirements.txt
/tmp/woeai-docs-venv/bin/sphinx-build -b html -W docs/source /tmp/woeai-sphinx-baseline-html
```

Expected:

```text
build succeeded.
```

- [ ] Commit only if this task creates no tracked changes.

### Task 0.2: Record Baseline Public Problems

**Files:** none.

- [ ] Run:

```bash
find /tmp/woeai-sphinx-baseline-html -maxdepth 2 -type f -name '*.html' -print0 \
  | xargs -0 rg -n "Lumache|Documentation coming soon|pip install|Usage|API|For example|This project is under active development"
```

Expected before cleanup: matches in generated `index.html`, `usage.html`, `api.html`, and `People.html`.

- [ ] Keep this output in the PR description when implementing Phase 1.

---

## Phase 1: Agent and Build Readiness

### Task 1.1: Add Repository Agent Contract

**Files:**

- Create: `AGENTS.md`

**Content requirements:**

- State that this is a pure Sphinx/ReadTheDocs website.
- State that agents must not run or recommend `pip install .`.
- State that all content changes must pass strict HTML build.
- State that factual claims about publications, people, titles, grants, and recruitment must come from supplied source material or existing repository content.
- State that public-facing content should keep Chinese/English paired headings where the existing page does.
- State that images belong under `docs/_static/`.
- State that `docs/source/conf.py` controls SEO, sitemap, theme, logo, analytics, and base URL.

**Suggested file body:**

````markdown
# AGENTS.md

## Project Identity

This repository is the source for the WOEAI research group website, built with Sphinx and published through ReadTheDocs. It is a docs-only project, not an installable Python package.

## Build and Verification

Use a virtual environment and install only `docs/requirements.txt`.

```bash
python3 -m venv /tmp/woeai-docs-venv
/tmp/woeai-docs-venv/bin/python -m pip install --upgrade pip
/tmp/woeai-docs-venv/bin/python -m pip install -r docs/requirements.txt
/tmp/woeai-docs-venv/bin/sphinx-build -b html -W docs/source /tmp/woeai-sphinx-html
```

Do not run `pip install .`; this repository does not contain a Python package named `woeai`.

## Content Rules

- Keep public headings bilingual when the surrounding page uses Chinese and English.
- Do not invent publication metadata, student names, grant information, recruitment terms, or institutional titles.
- Use existing repository content as the source of truth unless the user provides newer material.
- Keep images in `docs/_static/` and reference them from `.rst` files with paths relative to `docs/source/`.
- Treat Sphinx warnings as release blockers.

## Key Files

- `docs/source/index.rst`: homepage.
- `docs/source/conf.py`: Sphinx, SEO, theme, sitemap, logo, analytics, canonical URL.
- `docs/source/Publications.rst`: publication records.
- `docs/source/People.rst`: group members.
- `docs/source/Projects.rst`: project records.
- `docs/source/*Wind*.rst`: research direction pages.
````

- [ ] Run:

```bash
git diff --check
```

Expected:

```text
```

- [ ] Commit:

```bash
git add AGENTS.md
git commit -m "docs: add agent operating guide"
```

### Task 1.2: Replace README Tutorial Text

**Files:**

- Modify: `README.rst`

**Replacement structure:**

```rst
WOEAI Website
=============

This repository contains the Sphinx source for the Wind & Ocean Engineering empowered by AI (WOEAI) research group website.

Project Structure
-----------------

- ``docs/source/``: reStructuredText source pages.
- ``docs/_static/``: logos, figures, CSS, and other static assets.
- ``docs/requirements.txt``: Python dependencies for local and ReadTheDocs builds.
- ``.readthedocs.yaml``: ReadTheDocs build configuration.

Local Build
-----------

Create a temporary virtual environment, install the documentation dependencies, and run a strict HTML build:

.. code-block:: console

   $ python3 -m venv /tmp/woeai-docs-venv
   $ /tmp/woeai-docs-venv/bin/python -m pip install --upgrade pip
   $ /tmp/woeai-docs-venv/bin/python -m pip install -r docs/requirements.txt
   $ /tmp/woeai-docs-venv/bin/sphinx-build -b html -W docs/source /tmp/woeai-sphinx-html

Publishing
----------

ReadTheDocs builds the site from ``docs/source/conf.py`` using the dependencies in ``docs/requirements.txt``.
``.readthedocs.yaml`` sets warnings as build failures.

Maintenance Notes
-----------------

This is a documentation website, not an installable Python package. Do not use ``pip install .`` for verification.
```

- [ ] Run:

```bash
/tmp/woeai-docs-venv/bin/sphinx-build -b html -W docs/source /tmp/woeai-readme-check-html
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add README.rst
git commit -m "docs: replace template README"
```

### Task 1.3: Add One-Command Docs Check

**Files:**

- Create: `scripts/check-docs.sh`
- Modify: `.gitignore` if the script uses a local repository venv.

**Script body:**

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${WOEAI_DOCS_VENV:-/tmp/woeai-docs-venv}"
BUILD_DIR="${WOEAI_DOCS_BUILD:-/tmp/woeai-sphinx-html}"

python3 -m venv "${VENV_DIR}"
"${VENV_DIR}/bin/python" -m pip install --upgrade pip
"${VENV_DIR}/bin/python" -m pip install -r "${ROOT_DIR}/docs/requirements.txt"
"${VENV_DIR}/bin/sphinx-build" -b html -W "${ROOT_DIR}/docs/source" "${BUILD_DIR}"
```

- [ ] Run:

```bash
chmod +x scripts/check-docs.sh
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add scripts/check-docs.sh .gitignore
git commit -m "build: add docs verification script"
```

### Task 1.4: Remove False Python Package Metadata

**Files:**

- Delete: `pyproject.toml`

**Rationale:**

`pyproject.toml` currently declares a Flit package named `woeai`, but the repository contains no `woeai` Python module. This makes `pip install .` fail and misleads agents.

- [ ] Delete the file.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add -u pyproject.toml
git commit -m "build: remove false package metadata"
```

### Task 1.5: Add GitHub Actions Docs Build

**Files:**

- Create: `.github/workflows/docs.yml`

**Workflow body:**

```yaml
name: Docs

on:
  pull_request:
  push:
    branches:
      - main

jobs:
  sphinx:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install -r docs/requirements.txt
      - name: Strict HTML build
        run: |
          sphinx-build -b html -W docs/source /tmp/woeai-sphinx-html
```

- [ ] Run local script:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add .github/workflows/docs.yml
git commit -m "ci: verify sphinx docs"
```

---

## Phase 2: Public Content Cleanup

### Task 2.1: Remove Tutorial Pages from Navigation

**Files:**

- Modify: `docs/source/index.rst`
- Delete: `docs/source/usage.rst`
- Delete: `docs/source/api.rst`

**Required changes:**

- Remove `usage` and `api` from the homepage toctree.
- Delete `docs/source/usage.rst`.
- Delete `docs/source/api.rst`.
- Ensure generated HTML no longer contains public `Usage`, `API`, `pip install woeai`, or `Documentation coming soon`.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Run:

```bash
find /tmp/woeai-sphinx-html -maxdepth 2 -type f -name '*.html' -print0 \
  | xargs -0 rg -n "Documentation coming soon|pip install woeai|Lumache|For example|This project is under active development"
```

Expected: no output.

- [ ] Commit:

```bash
git add docs/source/index.rst
git add -u docs/source/usage.rst docs/source/api.rst
git commit -m "docs: remove tutorial pages"
```

### Task 2.2: Rewrite Homepage Around Public Audiences

**Files:**

- Modify: `docs/source/index.rst`
- Create: `docs/source/Recruitment.rst`
- Create: `docs/source/Contact.rst`

**Homepage target structure:**

1. Site title: `Wind & Ocean Engineering empowered by AI (WOEAI)`
2. Short Chinese group mission paragraph using existing wording.
3. Three research direction links.
4. Short "研究亮点 Research Highlights" list derived from current publication/project themes:
   - AI-enabled urban wind simulation.
   - Numerical wind tunnel and atmospheric boundary layer turbulence generation.
   - Structural wind resistance and tall-building/transmission-tower response.
   - Floating offshore wind turbine dynamics, design, and optimization.
5. Recruitment callout linking to `Recruitment`.
6. Toctree with public pages only.

**Toctree after this task:**

```rst
.. toctree::
   :maxdepth: 2
   :caption: Site Navigation

   Research
   People
   Projects
   Publications
   Teaching
   GroupNews
   Recruitment
   Contact
```

**Recruitment page content source:**

Move the current recruitment section from `index.rst` into `Recruitment.rst`.

**Contact page content source:**

Move website, email, address, and WeChat QR code from `index.rst` into `Contact.rst`.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add docs/source/index.rst docs/source/Recruitment.rst docs/source/Contact.rst
git commit -m "docs: restructure homepage"
```

### Task 2.3: Make Group News Public and Real

**Files:**

- Modify: `docs/source/GroupNews.rst`

**Required changes:**

- Remove `:orphan:`.
- Replace course-copy residue with real news entries derived from existing publications.
- Use reverse chronological sections.

**Minimum content based on existing repository facts:**

```rst
团队动态 Group News
==================

2025
----

论文发表 Publications
~~~~~~~~~~~~~~~~~~~~

- Zhao Peisheng, Li Chao, Jiang Jianxun, Chen Lingwei, and Wang Xiaolu published work on using 3D Gaussian Splatting to construct building geometry for urban wind simulations in **Sustainable Cities and Society**.
- Tang Ao, Li Chao, Yang Junhui, Zhang Heqiang, Zheng Qingxing, and Zhang Jianjun published work on graph neural networks for predicting structural responses of tall buildings in **Journal of Building Engineering**.

研究进展 Research Updates
~~~~~~~~~~~~~~~~~~~~~~~~

- The group continues to develop AI-enabled methods for wind and ocean engineering, including urban wind simulation, structural response prediction, and offshore wind energy system analysis.
```

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add docs/source/GroupNews.rst
git commit -m "docs: publish group news page"
```

### Task 2.4: Clean People Page Placeholders

**Files:**

- Modify: `docs/source/People.rst`

**Required changes:**

- Remove `For example:`.
- Keep known names.
- For empty alumni/master sections, either remove empty subsections or add a factual maintenance sentence:

```rst
名单将根据团队公开信息持续更新。
```

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Run:

```bash
rg -n "For example" docs/source/People.rst
```

Expected: no output.

- [ ] Commit:

```bash
git add docs/source/People.rst
git commit -m "docs: clean people page placeholders"
```

---

## Phase 3: Research Information Architecture

### Task 3.1: Add Research Overview Page

**Files:**

- Create: `docs/source/Research.rst`
- Modify: `docs/source/index.rst`

**Page purpose:**

Create a bridge between the homepage and the three direction pages. Users should understand the group's research map before diving into detail.

**Required sections:**

- `研究方向 Research Areas`
- `数值风洞 Numerical Wind Tunnel`
- `结构抗风 Structural Wind Resistance`
- `海上风电 Offshore Wind Energy`
- `人工智能赋能 AI Empowerment`

**Content source:**

Use existing page headings, project titles, and publication titles only.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add docs/source/Research.rst docs/source/index.rst
git commit -m "docs: add research overview"
```

### Task 3.2: Expand Numerical Wind Tunnel Page

**Files:**

- Modify: `docs/source/NumericalWindTunnel.rst`

**Required sections:**

- `方向概述 Overview`
- `大气边界层湍流风场生成方法`
- `工程实践`
- `城镇风环境`
- `复杂地形风场`
- `代表性成果 Representative Publications`
- `相关项目 Related Projects`

**Evidence to cite from existing repository:**

- Publication [61] on 3D Gaussian Splatting for urban wind simulations.
- Publication [54] on vector potential random flow generation.
- Publication [50] on coherence-improved and mass-balanced inflow turbulence generation.
- Publication [45] on multiscale simulation of urban wind environment under typhoon weather.
- Projects involving numerical atmospheric turbulent boundary layer generation and complex terrain wind field simulation.

- [ ] Use `:ref:` links for publication anchors already present in `Publications.rst`, such as `ref-zhao20250`, `ref-li20240`, `ref-chen20241`, and `ref-zhao20230`.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add docs/source/NumericalWindTunnel.rst
git commit -m "docs: expand numerical wind tunnel research"
```

### Task 3.3: Expand Structural Wind Resistance Page

**Files:**

- Modify: `docs/source/WindResistance.rst`

**Required sections:**

- `方向概述 Overview`
- `超高层结构 Super High-Rise Structures`
- `输电塔 Transmission Towers`
- `AI 辅助结构响应预测 AI-Assisted Structural Response Prediction`
- `代表性成果 Representative Publications`
- `相关项目 Related Projects`

**Evidence to cite from existing repository:**

- Publication [60] on graph neural networks for tall-building structural response prediction.
- Publication [56] on transmission tower-line coupling under strong winds.
- Publication [55] on transmission tower-line dynamic failure mode.
- Publication [44] on reconstructing dynamic wind forces on transmission towers.
- Project on aerodynamic shape optimization for high-rise buildings.
- Enterprise project on transmission line micro-scale typhoon wind field.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add docs/source/WindResistance.rst
git commit -m "docs: expand structural wind resistance research"
```

### Task 3.4: Expand Offshore Wind Energy Page

**Files:**

- Modify: `docs/source/OffshoreWindEnergy.rst`

**Required sections:**

- `方向概述 Overview`
- `浮式风机基础主尺寸优化`
- `混凝土浮式基础结构设计与优化`
- `多物理场多体动力学分析模型`
- `运动和振动控制`
- `代表性成果 Representative Publications`
- `相关项目 Related Projects`

**Evidence to cite from existing repository:**

- Existing three figures in `docs/_static/`.
- Publication [48] on long-term dynamic optimization of floating wind turbine substructure designs.
- Publication [47] on jacket structures for offshore wind turbines.
- Publication [46] on wind tunnel and wave flume testing.
- Publication [32] on comparison of concrete and steel support structures.
- Projects on floating wind turbine system analysis and optimization.

- [ ] Ensure each figure has `:alt:`, `:align: center`, and a caption.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add docs/source/OffshoreWindEnergy.rst
git commit -m "docs: expand offshore wind energy research"
```

---

## Phase 4: Publication and Project Quality

### Task 4.1: Fix Publication Emphasis Markup

**Files:**

- Modify: `docs/source/Publications.rst`

**Problem:**

Entries such as `*Li Chao**` render incorrectly as `Li Chao*` in emphasis. The second star appears to mean corresponding author, but reStructuredText treats it as markup.

**Recommended convention:**

- Use bold for the group leader name: `**Li Chao**`.
- Escape literal corresponding-author stars: `\\*`.
- For Chinese name: `**李朝**`.

**Example replacement:**

```rst
[60] Tang Ao; **Li Chao**\*; Yang Junhui; Zhang Heqiang; Zheng Qingxing; Zhang Jianjun, ...
```

- [ ] Run:

```bash
rg -n "\*Li Chao\*\*|\*李朝\*\*" docs/source/Publications.rst
```

Expected before fix: matches.

- [ ] Fix each match.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Run:

```bash
rg -n "\*Li Chao\*\*|\*李朝\*\*" docs/source/Publications.rst
```

Expected after fix: no output.

- [ ] Commit:

```bash
git add docs/source/Publications.rst
git commit -m "docs: fix publication author markup"
```

### Task 4.2: Add Publication Summary Blocks

**Files:**

- Modify: `docs/source/Publications.rst`

**Required additions near top of page:**

- Total count statement based on visible list count.
- Recent highlights for 2025 and 2024.
- Topic filters as manually curated links:
  - AI for wind and structural engineering.
  - Numerical wind tunnel and turbulence generation.
  - Offshore wind energy.
  - Structural wind resistance.

**Implementation constraint:**

Do not renumber publications in this task. Preserve existing anchors.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add docs/source/Publications.rst
git commit -m "docs: add publication highlights"
```

### Task 4.3: Normalize Project Page Formatting

**Files:**

- Modify: `docs/source/Projects.rst`

**Required changes:**

- Normalize Chinese and English punctuation.
- Remove trailing whitespace.
- Preserve project years, levels, titles, and roles.
- Group projects by `政府项目 Government Projects`, `企业项目 Enterprise Projects`, `结构抗风方向`, and `海上风电方向`.

- [ ] Run:

```bash
rg -n "  $" docs/source/Projects.rst
```

Expected after cleanup: no output.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add docs/source/Projects.rst
git commit -m "docs: normalize project formatting"
```

---

## Phase 5: Site Presentation Within Sphinx

### Task 5.1: Improve Custom CSS Conservatively

**Files:**

- Modify: `docs/_static/custom.css`

**Goals:**

- Keep ReadTheDocs navigation and search.
- Improve content readability for bilingual research pages.
- Make figures responsive.
- Avoid decorative gradients and heavy custom layouts.

**Suggested additions:**

```css
.wy-nav-content {
    max-width: 1200px !important;
}

.wy-nav-content p,
.wy-nav-content li {
    line-height: 1.72;
}

.wy-nav-content h1,
.wy-nav-content h2,
.wy-nav-content h3 {
    letter-spacing: 0;
}

.wy-nav-content img {
    max-width: 100%;
    height: auto;
}

.figure,
figure {
    margin: 1.5rem auto;
}

.admonition,
.note,
.attention {
    border-radius: 4px;
}
```

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit:

```bash
git add docs/_static/custom.css
git commit -m "style: improve docs readability"
```

### Task 5.2: Review SEO and Canonical Metadata

**Files:**

- Modify: `docs/source/conf.py`

**Required checks:**

- `html_baseurl` remains `https://winddee.cn/`.
- `html_meta` description describes the group and domains.
- `og:title`, `og:description`, `og:url`, and `og:image` remain aligned with the public site.
- `html_search_language = 'zh'` remains.
- `sphinx_sitemap` remains installed and enabled.

**Recommended cleanup:**

- Keep analytics ID only if the ID is confirmed by the site owner.
- Remove comments that say "replace with your GA ID" if the current ID is real.

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Verify generated canonical links:

```bash
rg -n 'rel="canonical"|sitemap.xml' /tmp/woeai-sphinx-html
```

Expected: canonical links point to `https://winddee.cn/`.

- [ ] Commit:

```bash
git add docs/source/conf.py
git commit -m "docs: tighten site metadata"
```

---

## Phase 6: PDF and Publishing Policy

### Task 6.1: Decide PDF Requirement

**Files:**

- Modify: `.readthedocs.yaml`
- Optionally modify: `README.rst`

**Current state:**

ReadTheDocs is configured to build PDF:

```yaml
formats:
  - pdf
```

Local PDF build fails because `latexmk` is not installed. HTML build is the core website path.

**Recommended decision:**

If PDF is not needed for the public website, remove the PDF format from `.readthedocs.yaml`. If PDF is needed, add a README section explaining that local PDF verification requires a LaTeX distribution with `latexmk`.

**Option A: HTML-only**

Remove:

```yaml
formats:
  - pdf
```

**Option B: Keep PDF**

Add README section:

```rst
PDF Builds
----------

ReadTheDocs can build PDF output. Local PDF verification requires a LaTeX toolchain with ``latexmk`` available on ``PATH``.
```

- [ ] Run:

```bash
./scripts/check-docs.sh
```

Expected:

```text
build succeeded.
```

- [ ] Commit with one of:

```bash
git add .readthedocs.yaml
git commit -m "build: publish html docs only"
```

or:

```bash
git add README.rst
git commit -m "docs: document pdf build requirements"
```

---

## Phase 7: Longer-Term Upgrade Options

### Option 7.1: Data-Driven Publications

Do after Phase 1-6 are stable.

**Goal:** Move publication metadata into a structured source such as YAML or BibTeX, then generate `Publications.rst`.

**Candidate files:**

- Create: `data/publications.yml`
- Create: `scripts/generate-publications.py`
- Modify: `docs/source/Publications.rst`

**Reason:**

The current flat RST page is easy to edit once, but hard to sort, filter, validate, or reuse across homepage highlights, news, and topic pages.

**Guardrail:**

Do not start this before the author markup and public content cleanup are complete.

### Option 7.2: Sphinx Theme Upgrade

Do after content architecture is stable.

**Candidates:**

- Stay with `sphinx-rtd-theme` and improve CSS.
- Move to `pydata-sphinx-theme` for a more modern research-site feel.
- Move to a custom static site framework only if the team needs homepage-specific visual design, cards, people profiles, publication filters, or multilingual routing that Sphinx becomes awkward to maintain.

**Recommendation:**

Stay on Sphinx for the first upgrade. The current problems are not caused by Sphinx; they are caused by content residue, weak information architecture, and missing build guardrails.

---

## Acceptance Criteria for the First Upgrade Cycle

- `README.rst` describes WOEAI and local docs build, not the ReadTheDocs tutorial.
- `AGENTS.md` exists and prevents future agents from treating the repo as a Python package.
- `./scripts/check-docs.sh` builds the site successfully with warnings as errors.
- GitHub Actions runs strict Sphinx HTML build.
- `pyproject.toml` no longer misrepresents the project as an installable package.
- Generated HTML contains no `Lumache`, `Documentation coming soon`, `pip install woeai`, `For example`, or tutorial `Usage/API` pages.
- Homepage presents mission, research directions, recruitment entry, and navigation clearly.
- Research direction pages contain meaningful evidence-backed content, not only headings.
- GroupNews is either a visible useful page or absent from the public site; it is not a hidden warning workaround.
- Publication author markup renders cleanly.
- Sphinx strict HTML build passes after every phase.

---

## Recommended Execution Order

1. Phase 1: Agent and build readiness.
2. Phase 2: Public content cleanup.
3. Phase 3: Research information architecture.
4. Phase 4: Publication and project quality.
5. Phase 5: Site presentation.
6. Phase 6: PDF policy.
7. Phase 7: Optional data/theme modernization.

This order makes later creative or visual work safer. It first removes false project signals, then removes public embarrassment, then adds real research substance, and only then polishes presentation.
