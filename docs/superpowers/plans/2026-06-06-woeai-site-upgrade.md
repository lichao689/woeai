<!-- /autoplan restore point: /Users/lichao/.gstack/projects/lichao689-woeai/main-autoplan-restore-20260606-121604.md -->
# WOEAI Site Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the WOEAI repository from a tutorial-derived Sphinx site into a maintainable, verifiable, bilingual research group website that future agents can safely evolve.

**Autoplan-approved outcome priority:** 1. 招生 Recruitment. 2. 产业合作 Industry collaboration. 3. 学术可信度 Academic credibility.

**Plan status:** revised after autoplan review. The execution plan below incorporates the required review changes; the `GSTACK REVIEW REPORT` at the end remains as the audit trail.

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

The site is not primarily a software documentation site. It is a public research group presence for "Wind & Ocean Engineering empowered by AI". The important audiences are ordered by the confirmed outcome priority:

- Prospective master, PhD, and postdoctoral applicants.
- Industry partners looking for engineering capability and project evidence.
- Academic collaborators looking for research areas and representative work.
- Search engines and AI crawlers looking for stable institutional facts.
- Group members or agents maintaining publications, news, and pages.

The current implementation passes Sphinx, but the public meaning is uneven:

- The homepage mixes group intro, recruiting, research links, template copy, navigation, and contact details.
- Research direction pages do not yet explain capabilities, methods, representative results, or project connections.
- Publications are rich but formatted as a flat list; users cannot quickly see highlights, themes, years, or representative AI-enabled work.
- GroupNews exists but is hidden, which removes the natural "freshness" signal.
- README and `pyproject.toml` can mislead future agents into treating this as a Python package.
- There is no project-level agent contract, local verification script, or CI workflow for docs.

The best upgrade path is therefore outcome-first, source-grounded, and guardrail-backed:

1. Define recruitment and cooperation success signals.
2. Collect source material before writing persuasive public claims.
3. Clean the public site so it no longer shows template residue.
4. Make the repository unambiguous for future agents.
5. Add one-command verification.
6. Build recruitment, industry cooperation, and academic credibility journeys in that order.
7. Improve presentation within Sphinx only after the journey and content structure are coherent.

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
- `docs/superpowers/research/2026-06-woeai-peer-site-benchmark.md`: benchmark and theme decision record.
- `docs/superpowers/source-packets/2026-06-woeai-site-source-packet.md`: source packet for recruitment, cooperation, people, and public claims.
- `docs/source/Recruitment.rst`: dedicated recruitment page split from homepage.
- `docs/source/IndustryCollaboration.rst`: dedicated industry cooperation page or partner path.
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
- `.vscode/launch.json`: remove it or replace the generic Python launch config with docs-build guidance if the file remains tracked.
- `.gitignore`: add local venv/cache names used by verification script if needed.

### Files to Delete

- `docs/source/usage.rst`: current content is a tutorial artifact.
- `docs/source/api.rst`: current content is a tutorial artifact.
- `pyproject.toml`: current package metadata is false for a docs-only repository.

Deletion note: if the team wants to preserve `usage.html` or `api.html` for old external links, convert them into hidden redirect/landing pages in a separate task. The default recommendation is deletion because the existing public pages are misleading.

---

## Global Execution Rules

- Run every command from the repository root: `/Volumes/WorkSSD/codes/woeai`.
- Use small commits after each completed task. Do not mix unrelated content, tooling, and visual changes in one commit.
- Never invent recruitment terms, student outcomes, grant details, partner claims, publication metadata, or current openings.
- If a public claim cannot be sourced from existing repository content or the source packet, either omit it, mark the section as updating, or ask the site owner.
- Strict Sphinx HTML build is the release gate. Until `scripts/check-docs.sh` exists, run the direct venv commands shown in Phase 0.
- After `scripts/check-docs.sh` exists, run it after every task, followed by `git diff --check`.
- Keep `招生 Recruitment`, `产业合作 Industry Collaboration`, and `学术可信度 Academic Credibility` in that order across homepage hierarchy, navigation, and acceptance criteria.

---

## Phase 0: Baseline, Outcome, and Source Gates

### Task 0.1: Confirm Baseline And Review State

**Files:** none.

- [ ] Run from repo root:

```bash
git status --short --branch
```

Expected before implementation:

```text
## main...origin/main
```

If the only dirty file is this plan during review, finish and commit the revised plan first. If any implementation file is dirty unexpectedly, stop and inspect before continuing.

- [ ] Run strict baseline build:

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

- [ ] Record current public residue:

```bash
find /tmp/woeai-sphinx-baseline-html -maxdepth 2 -type f -name '*.html' -print0 \
  | xargs -0 rg -n "Lumache|Documentation coming soon|pip install|Usage|API|For example|This project is under active development|Contact Me"
```

Expected before cleanup: matches in generated HTML.

Do not commit this task unless the plan file itself was revised and intentionally staged.

### Task 0.2: Define Outcome Metrics And Benchmark Peer Sites

**Files:**

- Create: `docs/superpowers/research/2026-06-woeai-peer-site-benchmark.md`

**Required content:**

- Confirmed outcome priority: `招生 > 产业合作 > 学术可信度`.
- 5 to 8 peer lab or professor websites, with at least 3 Chinese university or research-group recruiting pages if available.
- For each benchmark: first-viewport message, recruitment path, cooperation path, proof signals, contact path, and visual/theme notes.
- Recommendation: stay with `sphinx-rtd-theme`, build a custom Sphinx homepage, move to `pydata-sphinx-theme`, or defer a custom static site.
- Decision owner and date.

**Acceptance:**

- [ ] The benchmark names a concrete first-cycle theme/page strategy.
- [ ] The decision does not block strict Sphinx HTML build.
- [ ] Commit:

```bash
git add docs/superpowers/research/2026-06-woeai-peer-site-benchmark.md
git commit -m "docs: benchmark peer research group sites"
```

### Task 0.3: Create Public-Claim Source Packet

**Files:**

- Create: `docs/superpowers/source-packets/2026-06-woeai-site-source-packet.md`

**Required sections:**

- Recruitment: current master, PhD, and postdoctoral opening expectations.
- Postdoctoral terms: age, degree timing, publication expectations, salary, subsidies, benefits, and whether each item is current.
- Contact expectations: email, website, address, QR code, response path.
- Industry cooperation: approved project examples, partner-facing capability wording, cooperation contact path.
- People: current students, alumni, titles, and any sections that must remain hidden or marked updating.
- Academic proof: publication highlights, project highlights, facilities/images if available, PI quote if approved.
- Unknowns: every missing fact that must not be invented.

**Acceptance:**

- [ ] Every recruitment and partner-facing claim planned for public pages is backed by a source entry or marked unavailable.
- [ ] Missing source material has a public-safe fallback.
- [ ] Commit:

```bash
git add docs/superpowers/source-packets/2026-06-woeai-site-source-packet.md
git commit -m "docs: add site source packet"
```

---

## Phase 1: Public Embarrassment Cleanup

This phase removes public damage before deeper restructuring. Use the direct strict build commands from Phase 0 until `scripts/check-docs.sh` exists.

### Task 1.1: Remove Tutorial And Placeholder Residue

**Files:**

- Modify: `docs/source/index.rst`
- Modify: `docs/source/People.rst`
- Delete: `docs/source/usage.rst`
- Delete: `docs/source/api.rst`

**Required changes:**

- Remove `usage` and `api` from the homepage toctree.
- Delete `docs/source/usage.rst` and `docs/source/api.rst`.
- Remove homepage `Lumache`, `test`, `This project is under active development`, and broken installation references.
- Remove `For example:` from `People.rst`.
- Change `与我联系 Contact Me` to institutional language such as `联系方式 Contact`.
- Preserve existing people names and verified facts.

**Verification:**

```bash
rm -rf /tmp/woeai-sphinx-cleanup-html
/tmp/woeai-docs-venv/bin/sphinx-build -b html -W docs/source /tmp/woeai-sphinx-cleanup-html
test ! -e /tmp/woeai-sphinx-cleanup-html/usage.html
test ! -e /tmp/woeai-sphinx-cleanup-html/api.html
! find /tmp/woeai-sphinx-cleanup-html -maxdepth 2 -type f -name '*.html' -print0 \
  | xargs -0 rg -n "Lumache|Documentation coming soon|pip install woeai|For example|This project is under active development|Contact Me"
```

Expected: build succeeds, `test` commands pass, and final `rg` has no output.

- [ ] Commit:

```bash
git add docs/source/index.rst docs/source/People.rst
git add -u docs/source/usage.rst docs/source/api.rst
git commit -m "docs: remove public template residue"
```

### Task 1.2: Make Group News Safe Or Hide It

**Files:**

- Modify: `docs/source/GroupNews.rst`

**Required decision:**

Choose one based on source availability:

- If there is a verified news owner/cadence, remove `:orphan:` and publish real dated news.
- If no owner/cadence exists, keep news out of navigation and replace course-copy residue with a verified recent-publications or updates page.

**Minimum safe content if no news owner exists:**

Use verified 2025 publication updates from `Publications.rst`, and avoid claiming a recurring news cadence.

**Verification:**

```bash
/tmp/woeai-docs-venv/bin/sphinx-build -b html -W docs/source /tmp/woeai-sphinx-cleanup-html
! rg -n "Engineering Fluid Mechanics|风工程 Wind Engineering" docs/source/GroupNews.rst
```

Expected: build succeeds and `rg` has no output.

- [ ] Commit:

```bash
git add docs/source/GroupNews.rst
git commit -m "docs: make group news source-safe"
```

---

## Phase 2: Build And Agent Readiness

### Task 2.1: Add One-Command Strict Docs Check

**Files:**

- Create: `scripts/check-docs.sh`
- Modify: `.gitignore` only if a repository-local venv/cache is introduced.

**Required setup:**

```bash
mkdir -p scripts
```

**Script body:**

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${WOEAI_DOCS_VENV:-/tmp/woeai-docs-venv}"
BUILD_DIR="${WOEAI_DOCS_BUILD:-/tmp/woeai-sphinx-html}"

mkdir -p "$(dirname "${VENV_DIR}")" "$(dirname "${BUILD_DIR}")"
"${PYTHON_BIN}" - <<'PY'
import sys
if sys.version_info < (3, 12):
    raise SystemExit("Python 3.12+ is required for WOEAI docs checks")
PY
"${PYTHON_BIN}" -m venv "${VENV_DIR}"
"${VENV_DIR}/bin/python" -m pip install --upgrade pip
"${VENV_DIR}/bin/python" -m pip install -r "${ROOT_DIR}/docs/requirements.txt"
rm -rf "${BUILD_DIR}"
"${VENV_DIR}/bin/sphinx-build" -b html -W --keep-going -E "${ROOT_DIR}/docs/source" "${BUILD_DIR}"
echo "WOEAI docs build succeeded: ${BUILD_DIR}"
```

**Verification:**

```bash
chmod +x scripts/check-docs.sh
./scripts/check-docs.sh
git diff --check
```

- [ ] Commit:

```bash
git add scripts/check-docs.sh .gitignore
git commit -m "build: add strict docs check"
```

### Task 2.2: Replace README And Add Agent Contract

**Files:**

- Modify: `README.rst`
- Create: `AGENTS.md`

**README requirements:**

- Identify the repo as the WOEAI Sphinx website.
- Show `./scripts/check-docs.sh` as the primary local verification command.
- State that this is not an installable Python package and `pip install .` is not a verification step.
- Explain `docs/source/`, `docs/_static/`, `docs/requirements.txt`, `.readthedocs.yaml`, and ReadTheDocs publishing.

**AGENTS requirements:**

- State that commands run from repo root.
- State that content claims require source packet or existing repository evidence.
- State that `招生 > 产业合作 > 学术可信度` is the site priority.
- State that strict Sphinx HTML build is mandatory.
- State that images belong under `docs/_static/`.
- State that `docs/source/conf.py` controls SEO, sitemap, theme, logo, analytics, and base URL.

**Verification:**

```bash
./scripts/check-docs.sh
! rg -n "Read the Docs tutorial|Lumache|pip install \\." README.rst AGENTS.md
git diff --check
```

Expected: build succeeds and `rg` has no output.

- [ ] Commit:

```bash
git add README.rst AGENTS.md
git commit -m "docs: add website maintenance guide"
```

### Task 2.3: Remove False Python-App Signals

**Files:**

- Delete: `pyproject.toml`
- Modify: `docs/source/conf.py`
- Delete or modify: `.vscode/launch.json`

**Required changes:**

- Delete `pyproject.toml` unless a non-package tooling config is intentionally introduced.
- Remove unused API-style Sphinx extensions from `docs/source/conf.py`: `sphinx.ext.doctest`, `sphinx.ext.autodoc`, and `sphinx.ext.autosummary`, unless the README explains why they remain.
- Delete `.vscode/launch.json`, or replace the generic Python current-file debugger with docs-build guidance if the file remains tracked.

**Verification:**

```bash
./scripts/check-docs.sh
test ! -e pyproject.toml
! rg -n "autodoc|autosummary|doctest|Python 调试程序|current file" docs/source/conf.py .vscode/launch.json 2>/dev/null
git diff --check
```

Expected: build succeeds; `pyproject.toml` is absent; `rg` has no output if `.vscode/launch.json` is deleted or cleaned.

- [ ] Commit:

```bash
git add docs/source/conf.py
git add -u pyproject.toml .vscode/launch.json
git commit -m "build: remove false python package signals"
```

### Task 2.4: Add CI That Uses The Local Script

**Files:**

- Create: `.github/workflows/docs.yml`

**Required setup:**

```bash
mkdir -p .github/workflows
```

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
      - name: Strict HTML build
        run: ./scripts/check-docs.sh
```

**Verification:**

```bash
./scripts/check-docs.sh
git diff --check
```

- [ ] Commit:

```bash
git add .github/workflows/docs.yml
git commit -m "ci: verify docs with strict script"
```

### Task 2.5: Resolve PDF Publishing Policy

**Files:**

- Modify: `.readthedocs.yaml`
- Optionally modify: `README.rst`

**Decision for the first upgrade cycle:**

Use HTML-only unless the site owner explicitly needs PDF. The current public outcome priority does not require PDF, and local PDF verification fails without `latexmk`.

**Default required change:**

Remove:

```yaml
formats:
  - pdf
```

If the owner requires PDF instead, keep the format and add README instructions for a local LaTeX toolchain with `latexmk`.

**Verification:**

```bash
./scripts/check-docs.sh
! rg -n "formats:|pdf|latexmk" .readthedocs.yaml README.rst
git diff --check
```

Expected default: build succeeds and no PDF format remains in `.readthedocs.yaml`.

- [ ] Commit:

```bash
git add .readthedocs.yaml README.rst
git commit -m "build: publish html docs only"
```

---

## Phase 3: Recruitment And Collaboration Journeys

### Task 3.1: Create Source-Grounded Recruitment Page

**Files:**

- Create: `docs/source/Recruitment.rst`
- Modify: `docs/source/index.rst` only if moving content out of the homepage.

**Required content order:**

1. Who should join.
2. Current master, PhD, and postdoctoral opportunities.
3. Why join WOEAI, using only source-packet or existing repository evidence.
4. Postdoctoral requirements and benefits only if source packet confirms they are current.
5. Contact path.
6. Public-safe fallback for unknown or updating items.

**Verification:**

```bash
./scripts/check-docs.sh
! rg -n "source pending|TODO|TBD|待补充" docs/source/Recruitment.rst
git diff --check
```

Expected: build succeeds. Any updating text must be intentionally public-safe, not a TODO.

- [ ] Commit:

```bash
git add docs/source/Recruitment.rst docs/source/index.rst
git commit -m "docs: add recruitment page"
```

### Task 3.2: Create Industry Cooperation Path

**Files:**

- Create: `docs/source/IndustryCollaboration.rst`
- Modify: `docs/source/Projects.rst`

**Required content:**

- Partner-facing capability summary.
- Cooperation areas tied to existing projects and publications.
- Government and enterprise project evidence, preserving years, project levels, titles, and roles.
- What kinds of partner inquiries fit the group.
- Contact path.

**Constraint:**

Do not name confidential partners or imply active cooperation unless source packet confirms it.

**Verification:**

```bash
./scripts/check-docs.sh
! rg -n "TODO|TBD|source pending" docs/source/IndustryCollaboration.rst docs/source/Projects.rst
git diff --check
```

- [ ] Commit:

```bash
git add docs/source/IndustryCollaboration.rst docs/source/Projects.rst
git commit -m "docs: add industry collaboration path"
```

### Task 3.3: Create Contact Page

**Files:**

- Create: `docs/source/Contact.rst`
- Modify: `docs/source/index.rst`

**Required content source:**

Move website, email, address, and WeChat QR code from `index.rst`.

**Required wording:**

Use institutional language such as `联系方式 Contact`, not `Contact Me`.

**Verification:**

```bash
./scripts/check-docs.sh
! rg -n "Contact Me|与我联系" docs/source/index.rst docs/source/Contact.rst
git diff --check
```

Expected: build succeeds and `rg` has no output.

- [ ] Commit:

```bash
git add docs/source/Contact.rst docs/source/index.rst
git commit -m "docs: add contact page"
```

### Task 3.4: Add Research Overview Before Homepage References It

**Files:**

- Create: `docs/source/Research.rst`

**Required sections:**

- `研究方向 Research Areas`
- `数值风洞 Numerical Wind Tunnel`
- `结构抗风 Structural Wind Resistance`
- `海上风电 Offshore Wind Energy`
- `人工智能赋能 AI Empowerment`

**Constraint:**

This file must exist before `index.rst` references `Research` in a toctree.

**Verification:**

```bash
./scripts/check-docs.sh
git diff --check
```

- [ ] Commit:

```bash
git add docs/source/Research.rst
git commit -m "docs: add research overview page"
```

### Task 3.5: Rewrite Homepage Around Priority Journeys

**Files:**

- Modify: `docs/source/index.rst`

**Homepage target structure:**

1. Site title: `Wind & Ocean Engineering empowered by AI (WOEAI)`.
2. One short mission paragraph using existing group wording.
3. Recruitment first: positions, fit, and contact link.
4. Industry cooperation second: capability summary and project/contact links.
5. Academic credibility third: research areas, representative publications/projects, people.
6. Public toctree with every referenced page already present.

**Required toctree order:**

```rst
.. toctree::
   :maxdepth: 2
   :caption: Site Navigation

   Recruitment
   IndustryCollaboration
   Contact
   Research
   People
   Projects
   Publications
   Teaching
   GroupNews
```

Only include `GroupNews` if Task 1.2 made it source-safe.

**Verification:**

```bash
./scripts/check-docs.sh
! find /tmp/woeai-sphinx-html -maxdepth 2 -type f -name '*.html' -print0 \
  | xargs -0 rg -n "Lumache|Documentation coming soon|pip install woeai|For example|This project is under active development|Contact Me"
git diff --check
```

Expected: build succeeds and `rg` has no output.

- [ ] Commit:

```bash
git add docs/source/index.rst
git commit -m "docs: make homepage recruitment first"
```

---

## Phase 4: Research And Academic Credibility

### Task 4.1: Expand Research Overview

**Files:**

- Modify: `docs/source/Research.rst`

**Required changes:**

- Connect the three research directions to recruitment and cooperation outcomes.
- Use existing page headings, project titles, and publication titles only.
- Add links to `NumericalWindTunnel`, `WindResistance`, and `OffshoreWindEnergy`.

**Verification:**

```bash
./scripts/check-docs.sh
git diff --check
```

- [ ] Commit:

```bash
git add docs/source/Research.rst
git commit -m "docs: expand research overview"
```

### Task 4.2: Expand Numerical Wind Tunnel Page

**Files:**

- Modify: `docs/source/NumericalWindTunnel.rst`

**Evidence to use:**

- Publication [61] on 3D Gaussian Splatting for urban wind simulations.
- Publication [54] on vector potential random flow generation.
- Publication [50] on coherence-improved and mass-balanced inflow turbulence generation.
- Publication [45] on multiscale urban wind simulation under typhoon weather.
- Projects on numerical atmospheric turbulent boundary layer generation and complex terrain wind field simulation.

**Required sections:**

- `方向概述 Overview`
- `大气边界层湍流风场生成方法`
- `工程实践`
- `城镇风环境`
- `复杂地形风场`
- `代表性成果 Representative Publications`
- `相关项目 Related Projects`

**Verification:**

```bash
./scripts/check-docs.sh
git diff --check
```

- [ ] Commit:

```bash
git add docs/source/NumericalWindTunnel.rst
git commit -m "docs: expand numerical wind tunnel research"
```

### Task 4.3: Expand Structural Wind Resistance Page

**Files:**

- Modify: `docs/source/WindResistance.rst`

**Evidence to use:**

- Publication [60] on graph neural networks for tall-building structural response prediction.
- Publication [56] on transmission tower-line coupling under strong winds.
- Publication [55] on transmission tower-line dynamic failure mode.
- Publication [44] on reconstructing dynamic wind forces on transmission towers.
- Projects on high-rise aerodynamic shape optimization and transmission-line typhoon wind field.

**Required sections:**

- `方向概述 Overview`
- `超高层结构 Super High-Rise Structures`
- `输电塔 Transmission Towers`
- `AI 辅助结构响应预测 AI-Assisted Structural Response Prediction`
- `代表性成果 Representative Publications`
- `相关项目 Related Projects`

**Verification:**

```bash
./scripts/check-docs.sh
git diff --check
```

- [ ] Commit:

```bash
git add docs/source/WindResistance.rst
git commit -m "docs: expand structural wind resistance research"
```

### Task 4.4: Expand Offshore Wind Energy Page

**Files:**

- Modify: `docs/source/OffshoreWindEnergy.rst`

**Evidence to use:**

- Existing three figures in `docs/_static/`.
- Publication [48] on long-term dynamic optimization of floating wind turbine substructure designs.
- Publication [47] on jacket structures for offshore wind turbines.
- Publication [46] on wind tunnel and wave flume testing.
- Publication [32] on comparison of concrete and steel support structures.
- Projects on floating wind turbine system analysis and optimization.

**Required sections:**

- `方向概述 Overview`
- `浮式风机基础主尺寸优化`
- `混凝土浮式基础结构设计与优化`
- `多物理场多体动力学分析模型`
- `运动和振动控制`
- `代表性成果 Representative Publications`
- `相关项目 Related Projects`

**Verification:**

```bash
./scripts/check-docs.sh
git diff --check
```

- [ ] Commit:

```bash
git add docs/source/OffshoreWindEnergy.rst
git commit -m "docs: expand offshore wind energy research"
```

---

## Phase 5: Publications, Projects, And Proof Reuse

### Task 5.1: Normalize Publication Author Markup

**Files:**

- Modify: `docs/source/Publications.rst`

**Problem:**

Current entries use mixed literal-star conventions such as `*Li Chao**`, `Wang Xiaolu*`, `Liu Zhenqing*`, and `Xiao Yiqing*`. The cleanup must cover all corresponding-author markers, not only Li Chao.

**Required convention:**

- Use bold for the group leader name: `**Li Chao**` and `**李朝**`.
- Escape literal corresponding-author stars with `\*`.
- Preserve existing publication order, numbering, anchors, titles, journals, years, DOIs, impact factors, divisions, and citations.

**Verification:**

```bash
./scripts/check-docs.sh
! rg -n "\*Li Chao\*\*|\*李朝\*\*|[A-Za-z][A-Za-z -]*\*\*" docs/source/Publications.rst
git diff --check
```

Expected: build succeeds and grep finds no broken emphasis patterns. Also spot-check generated `Publications.html` for rendered author markers.

- [ ] Commit:

```bash
git add docs/source/Publications.rst
git commit -m "docs: normalize publication author markup"
```

### Task 5.2: Add Minimal Publication Highlights

**Files:**

- Modify: `docs/source/Publications.rst`

**Required additions near top:**

- Total visible publication count.
- Recent highlights for 2025 and 2024.
- Manual topic links for:
  - AI for wind and structural engineering.
  - Numerical wind tunnel and turbulence generation.
  - Offshore wind energy.
  - Structural wind resistance.

**Constraint:**

Do not renumber publications. Preserve existing anchors.

**Verification:**

```bash
./scripts/check-docs.sh
git diff --check
```

- [ ] Commit:

```bash
git add docs/source/Publications.rst
git commit -m "docs: add publication highlights"
```

### Task 5.3: Normalize Project Page Formatting And Partner Proof

**Files:**

- Modify: `docs/source/Projects.rst`
- Modify: `docs/source/IndustryCollaboration.rst` if project wording changes.

**Required changes:**

- Normalize Chinese and English punctuation.
- Remove trailing whitespace.
- Preserve years, levels, titles, and roles.
- Keep project grouping by government and enterprise project types.
- Link project evidence back to industry cooperation capabilities.

**Verification:**

```bash
! rg -n "  $" docs/source/Projects.rst
./scripts/check-docs.sh
git diff --check
```

Expected: no trailing whitespace and build succeeds.

- [ ] Commit:

```bash
git add docs/source/Projects.rst docs/source/IndustryCollaboration.rst
git commit -m "docs: strengthen project evidence"
```

---

## Phase 6: Presentation, SEO, And Final Verification

### Task 6.1: Improve Custom CSS Conservatively

**Files:**

- Modify: `docs/_static/custom.css`

**Goals:**

- Keep ReadTheDocs navigation and search.
- Improve bilingual page readability.
- Make figures responsive.
- Avoid heavy decorative layouts until benchmark/theme decision justifies them.

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

**Verification:**

```bash
./scripts/check-docs.sh
git diff --check
```

- [ ] Commit:

```bash
git add docs/_static/custom.css
git commit -m "style: improve docs readability"
```

### Task 6.2: Tighten Metadata And SEO

**Files:**

- Modify: `docs/source/conf.py`

**Required checks:**

- `html_baseurl` remains `https://winddee.cn/`.
- `html_meta` description reflects recruitment, wind/ocean engineering, AI, and HIT Shenzhen without keyword stuffing.
- `og:title`, `og:description`, `og:url`, and `og:image` align with the public site.
- `html_search_language = 'zh'` remains.
- `sphinx_sitemap` remains installed and enabled.
- Analytics ID remains only if confirmed by site owner.

**Verification:**

```bash
./scripts/check-docs.sh
rg -n 'rel="canonical"|sitemap.xml' /tmp/woeai-sphinx-html
git diff --check
```

Expected: canonical links point to `https://winddee.cn/`.

- [ ] Commit:

```bash
git add docs/source/conf.py
git commit -m "docs: tighten site metadata"
```

### Task 6.3: Final HTML Acceptance Pass

**Files:** none unless fixes are needed.

**Run:**

```bash
./scripts/check-docs.sh
! find /tmp/woeai-sphinx-html -maxdepth 2 -type f -name '*.html' -print0 \
  | xargs -0 rg -n "Lumache|Documentation coming soon|pip install woeai|For example|This project is under active development|Contact Me|TODO|TBD"
test ! -e /tmp/woeai-sphinx-html/usage.html
test ! -e /tmp/woeai-sphinx-html/api.html
rg -n "Recruitment|IndustryCollaboration|Contact|Research" /tmp/woeai-sphinx-html/index.html
git diff --check
```

Expected:

- Strict build succeeds.
- Template residue grep has no output.
- Deleted tutorial pages are absent.
- Homepage contains the priority journey links.
- Working tree is clean after final commit.

If fixes are needed, commit them by the smallest affected behavior.

---

## Phase 7: Longer-Term Options After First Upgrade

### Option 7.1: Minimal Structured Publication Highlights

Do after the first upgrade is stable.

**Goal:** Create a small structured source for homepage/research/news highlights before attempting a full publication generator.

**Candidate files:**

- Create: `data/publication-highlights.yml`
- Create: `scripts/generate-publication-highlights.py`
- Modify: `docs/source/Publications.rst`

**Guardrail:** do not start this before author markup and public content cleanup are complete.

### Option 7.2: Full Publication Generator

Do after the minimal highlight data source proves useful.

**Candidate files:**

- Create: `data/publications.yml` or BibTeX source.
- Create: `scripts/generate-publications.py`.
- Modify: `docs/source/Publications.rst`.

### Option 7.3: Sphinx Theme Or Static-Site Migration

Use the Phase 0 benchmark decision:

- Stay with `sphinx-rtd-theme` if content and journey clarity are the main problems.
- Move to `pydata-sphinx-theme` if a modern academic look is needed while retaining Sphinx.
- Move to a custom static site only if recruitment UX, multilingual routing, people profiles, publication filters, or visual storytelling cannot be maintained cleanly in Sphinx.

---

## Acceptance Criteria for the First Upgrade Cycle

- Outcome priority is visible in homepage hierarchy and navigation: recruitment first, industry cooperation second, academic credibility third.
- `docs/superpowers/research/2026-06-woeai-peer-site-benchmark.md` records benchmark and theme decision.
- `docs/superpowers/source-packets/2026-06-woeai-site-source-packet.md` records sources or public-safe fallbacks for every persuasive claim.
- `README.rst` describes WOEAI and local docs build, not the ReadTheDocs tutorial.
- `AGENTS.md` exists and prevents future agents from treating the repo as a Python package.
- `./scripts/check-docs.sh` cleans the build directory and builds the site with warnings as errors.
- GitHub Actions calls `./scripts/check-docs.sh`.
- `pyproject.toml` no longer misrepresents the project as an installable package.
- PDF policy is resolved early; default first-cycle policy is HTML-only.
- Generated HTML contains no `Lumache`, `Documentation coming soon`, `pip install woeai`, `For example`, `Contact Me`, or tutorial `Usage/API` pages.
- Homepage has source-grounded paths to `Recruitment`, `IndustryCollaboration`, `Contact`, and `Research`.
- Research direction pages contain evidence-backed content, not only headings.
- GroupNews is source-safe or absent from public navigation.
- Publication author markup renders cleanly for all corresponding-author markers, not only Li Chao.
- Sphinx strict HTML build passes after every phase.

---

## Autoplan Decision Audit Trail

**Review date:** 2026-06-06

**Restore point:** `/Users/lichao/.gstack/projects/lichao689-woeai/main-autoplan-restore-20260606-121604.md`

**User-confirmed premise:** the website upgrade should optimize for `招生 Recruitment` first, `产业合作 Industry collaboration` second, and `学术可信度 Academic credibility` third.

**Premise change accepted during review:**

- The site is not primarily a documentation site. It is a public research group website whose first job is to convert qualified applicants.
- Sphinx and ReadTheDocs remain acceptable for the first upgrade only if benchmark/prototype work proves they can carry the recruitment and cooperation journeys.
- Public credibility cleanup must happen before internal agent convenience work, except where a verification script is needed to keep the cleanup safe.
- Recruitment claims, postdoctoral compensation, open positions, student outcomes, project claims, and partner-facing language require a source packet or explicit owner verification before publication.

**Model availability:**

- CEO review: Codex and Claude both produced usable outside-voice findings.
- Design review: Codex produced findings; Claude was attempted but hung and was marked unavailable.
- Engineering review: Codex produced findings; main-thread repo inspection was used to validate build-order issues.
- DX review: Codex produced findings; main-thread repo inspection was used to validate first-run risks.

## Incorporated Autoplan Revisions

The execution plan above now incorporates the review findings instead of leaving them as an appendix.

- Outcome priority is built into global rules, homepage tasks, navigation order, and acceptance criteria.
- Benchmark and source-packet tasks now run before public persuasive copy.
- Public embarrassment cleanup now precedes internal agent convenience work.
- `Research.rst` is created before the homepage references it in a toctree.
- GroupNews cleanup happens before it is eligible for public navigation.
- `scripts/check-docs.sh` now cleans the build directory, checks Python version, and becomes the single CI command.
- PDF policy is resolved in Phase 2, not deferred to the end.
- Publication author markup cleanup covers all corresponding-author markers, not only Li Chao.
- README, AGENTS, `pyproject.toml`, `conf.py`, and `.vscode/launch.json` are grouped as first-run repository signal cleanup.

## NOT In Scope For The First Upgrade

- Full custom web app migration. First prove content, source packet, and journeys.
- Automated publication database generator for the entire bibliography. A minimal highlight data source is enough for the first cycle.
- News manufacturing. If there is no owner/cadence/source, hide news or use verified recent publications instead.
- Full multilingual split with `/zh/` and `/en/` unless the team commits to real translation ownership.

## GSTACK REVIEW REPORT

| Review | Scope | Runs | Status | Findings |
| --- | --- | ---: | --- | --- |
| CEO Review | Strategy, audience, positioning | 2 | Incorporated | No outcome metric; Sphinx assumed before benchmark; AI positioning generic; recruitment/source risks. |
| Design Review | Audience journeys and visual hierarchy | 1 | Incorporated | Plan was a cleanup plan, not yet a recruitment-first site plan; homepage and navigation did not match confirmed priority. |
| Eng Review | Build order, tests, implementation safety | 1 | Incorporated | `Research` toctree order could break `-W`; build dir could leave stale HTML; publication cleanup was too narrow; PDF policy was deferred too late. |
| DX Review | First-run setup and future-agent maintainability | 1 | Incorporated | Needed Python version check, clean build script, explicit directory creation, README/pyproject/conf.py signal cleanup, and repo-root command convention. |

**Consensus:** Keep Sphinx/ReadTheDocs only as a first-cycle publishing backbone, but revise the plan so recruitment and industry cooperation drive the information architecture.

**Blocking before implementation:** no separate appendix action remains. The blockers are integrated into the phase tasks above and should be executed in order.

**Final gate status:** user chose `Revise plan`; this document is the revised executable plan.
