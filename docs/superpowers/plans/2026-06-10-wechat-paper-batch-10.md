# WOEAI WeChat Paper Batch 10 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert ten WOEAI journal papers into public-safe one-paper WeChat article sources, matching RTD Paper Companion Pages, review notes, local assets, and no-submit validation outputs.

**Architecture:** Each paper is owned by one isolated article package: public Markdown, review note, optional cover brief, RTD RST, and `wechat/assets/public-safe/<publication_ref>/`. The shared files `wechat/backlog/selected-papers.yml`, `docs/source/Research.rst`, `docs/source/index.rst`, and direction pages are updated only by the controller after article packages exist. No worker may call the live WeChat draft API; live draft creation/update requires a later explicit user confirmation.

**Tech Stack:** Sphinx/reStructuredText, Zotero Desktop Local API, WOEAI WeChat Markdown tools, MathJax SVG formula renderer, PDF evidence extraction (`pdftotext`, `pdfimages`, page rendering/cropping as needed), public-safe image assets, and `./scripts/check-docs.sh`.

---

## Batch Scope

Process these ten candidate papers unless source inventory proves a paper is blocked:

| Order | publication_ref | Zotero key | DOI | Placement |
|---|---|---|---|---|
| 1 | `ref-zhao2026-BE` | `RLAA46YB` | `10.1016/j.buildenv.2026.114811` | 建筑结构抗风 / 数值风洞与湍动入流 |
| 2 | `ref-chen2024-JCP` | `Y76UWP9R` | `10.1016/j.jcp.2023.112706` | 建筑结构抗风 / 数值风洞与湍动入流 |
| 3 | `ref-yang2025-JBE` | `YZ2D62NB` | `10.1016/j.jobe.2025.113635` | 建筑结构抗风 / 高层建筑抗风与优化 |
| 4 | `ref-he2025-POF` | `ES37XMDV` | `10.1063/5.0293483` | 建筑结构抗风 / 高层建筑抗风与优化 |
| 5 | `ref-zheng2025-OE` | `5W2SZJUT` | `10.1016/j.oceaneng.2025.121336` | 海上漂浮风电 / 数值风浪流水池 |
| 6 | `ref-zhou2023-AE` | `3LWVP7B7` | `10.1016/j.apenergy.2023.121941` | 海上漂浮风电 / 浮式风机系统一体化分析与优化 |
| 7 | `ref-li2022-SOS` | `5AT7UEWV` | `10.1080/17445302.2021.1937801` | 海上漂浮风电 / 浮式混凝土平台结构设计 |
| 8 | `ref-he2026-OE` | `4FX43CFT` | `10.1016/j.oceaneng.2026.124728` | 建筑结构抗风 / 高层建筑抗风与优化 |
| 9 | `ref-tang2026-RE` | `XM44D697` | `10.1016/j.renene.2025.124336` | 建筑结构抗风 / 数值风洞与湍动入流 |
| 10 | `ref-wang2024-ES` | `3HGIR6QR` | `10.1016/j.engstruct.2024.118742` | 建筑结构抗风 / 数值风洞与湍动入流 |

## Shared Requirements

- Reader-facing Markdown lives at `wechat/articles/draft-public-safe/<publication_ref>.md` and is the public content master.
- RTD pages are generated with `python3 wechat/tools/markdown_to_rtd.py --publication-ref <publication_ref>`.
- Review notes live at `wechat/articles/review/<publication_ref>.review.md`.
- Public-safe figures live under `wechat/assets/public-safe/<publication_ref>/`.
- Private Zotero/PDF working files stay under ignored `wechat/.local/<publication_ref>/`.
- Review notes must include `## 源文件获取记录` and `## 关键事实证据定位记录`.
- `论文信息` contains only title, authors, journal, year, DOI, and WOEAI direction; no separate `卷期页码`.
- Author markers match `docs/source/Publications.rst`: student first author uses `<u>...</u>`, corresponding author uses `\*`, and `(corresponding author)` is not used.
- English abstracts must match the original abstract source, normally Zotero `abstractNote` or PDF abstract.
- If no local PDF or approved source exists, the article package may stop at a review note with `需要同步 PDF 或提供作者稿`; do not invent PDF-derived body facts or figures.
- Do not read WeChat credentials or call `create-draft` / `update-draft` in this plan.

## Task Model

Use fresh subagents for implementation tasks. A worker owns a disjoint article package and must not edit other workers' paper files. After each implementation task:

1. Dispatch a spec-compliance reviewer for that paper package.
2. Fix any spec gaps before continuing.
3. Dispatch a code/content-quality reviewer for that paper package.
4. Fix any quality issues before marking the paper complete.

The controller owns shared files and final validation.

## Tasks

### Task 1: Source Inventory And Backlog Normalization

**Files:**
- Modify: `wechat/backlog/selected-papers.yml`
- Private: `wechat/.local/<publication_ref>/`
- Read: `docs/source/Publications.rst`

- [ ] Query Zotero Local API for all known keys and DOI/title-search the three unresolved papers.
- [ ] Record public-safe source availability in each review note once the paper package is created.
- [ ] Add missing backlog entries for `ref-he2026-OE`, `ref-tang2026-RE`, and `ref-wang2024-ES` using the resolved Zotero keys above.
- [ ] Do not print or commit private absolute PDF paths.

### Task 2: Convert `ref-zhao2026-BE`

**Files:** `wechat/articles/draft-public-safe/ref-zhao2026-BE.md`, `wechat/articles/review/ref-zhao2026-BE.review.md`, `docs/source/paper-notes/ref-zhao2026-BE.rst`, `wechat/assets/public-safe/ref-zhao2026-BE/`

- [ ] Build the article package from Zotero/PDF evidence.
- [ ] Include suitable public-safe figures if PDF evidence is available.
- [ ] Generate and check the RTD page.

### Task 3: Convert `ref-chen2024-JCP`

**Files:** `wechat/articles/draft-public-safe/ref-chen2024-JCP.md`, `wechat/articles/review/ref-chen2024-JCP.review.md`, `docs/source/paper-notes/ref-chen2024-JCP.rst`, `wechat/assets/public-safe/ref-chen2024-JCP/`

- [ ] Build the article package from Zotero/PDF evidence.
- [ ] Include suitable public-safe figures if PDF evidence is available.
- [ ] Generate and check the RTD page.

### Task 4: Convert `ref-yang2025-JBE`

**Files:** `wechat/articles/draft-public-safe/ref-yang2025-JBE.md`, `wechat/articles/review/ref-yang2025-JBE.review.md`, `docs/source/paper-notes/ref-yang2025-JBE.rst`, `wechat/assets/public-safe/ref-yang2025-JBE/`

- [ ] Build the article package from Zotero/PDF evidence.
- [ ] Include suitable public-safe figures if PDF evidence is available.
- [ ] Generate and check the RTD page.

### Task 5: Convert `ref-he2025-POF`

**Files:** `wechat/articles/draft-public-safe/ref-he2025-POF.md`, `wechat/articles/review/ref-he2025-POF.review.md`, `docs/source/paper-notes/ref-he2025-POF.rst`, `wechat/assets/public-safe/ref-he2025-POF/`

- [ ] Build the article package from Zotero/PDF evidence.
- [ ] Include suitable public-safe figures if PDF evidence is available.
- [ ] Generate and check the RTD page.

### Task 6: Convert `ref-zheng2025-OE`

**Files:** `wechat/articles/draft-public-safe/ref-zheng2025-OE.md`, `wechat/articles/review/ref-zheng2025-OE.review.md`, `docs/source/paper-notes/ref-zheng2025-OE.rst`, `wechat/assets/public-safe/ref-zheng2025-OE/`

- [ ] Build the article package from Zotero/PDF evidence.
- [ ] Include suitable public-safe figures if PDF evidence is available.
- [ ] Generate and check the RTD page.

### Task 7: Convert `ref-zhou2023-AE`

**Files:** `wechat/articles/draft-public-safe/ref-zhou2023-AE.md`, `wechat/articles/review/ref-zhou2023-AE.review.md`, `docs/source/paper-notes/ref-zhou2023-AE.rst`, `wechat/assets/public-safe/ref-zhou2023-AE/`

- [ ] Build the article package from Zotero/PDF evidence.
- [ ] Include suitable public-safe figures if PDF evidence is available.
- [ ] Generate and check the RTD page.

### Task 8: Convert `ref-li2022-SOS`

**Files:** `wechat/articles/draft-public-safe/ref-li2022-SOS.md`, `wechat/articles/review/ref-li2022-SOS.review.md`, `docs/source/paper-notes/ref-li2022-SOS.rst`, `wechat/assets/public-safe/ref-li2022-SOS/`

- [ ] Build the article package from Zotero/PDF evidence.
- [ ] Include suitable public-safe figures if PDF evidence is available.
- [ ] Generate and check the RTD page.

### Task 9: Resolve And Convert Three Extra Candidates

**Files:** `wechat/backlog/selected-papers.yml`, per-paper article package paths for `ref-he2026-OE`, `ref-tang2026-RE`, and `ref-wang2024-ES`

- [ ] Resolve Zotero keys for each extra candidate by local title/DOI search.
- [ ] If a key and abstract/PDF evidence are available, create the same article package as Tasks 2-8.
- [ ] If any candidate lacks a reliable Zotero/PDF source, create or update backlog/review state only to document the blocker, then stop that paper before drafting body claims.

### Task 10: Shared RTD Navigation, Backlog State, And Final Validation

**Files:**
- Modify: `docs/source/Research.rst`
- Modify as needed: `docs/source/index.rst`
- Modify as needed: `docs/source/BuildingStructuralWindResistance.rst`
- Modify as needed: `docs/source/FloatingOffshoreWindEnergy.rst`
- Modify: `wechat/backlog/selected-papers.yml`

- [ ] Add generated RTD pages to the hidden toctree in `docs/source/Research.rst`.
- [ ] Add Academic Progress links under the correct subdirection, sorted by publication year descending.
- [ ] Keep homepage latest-progress limits readable if `docs/source/index.rst` is updated.
- [ ] Set converted items to `reviewing`; do not set `ready_to_publish` unless a WeChat draft API action succeeds later.
- [ ] Run `python3 wechat/tools/markdown_to_rtd.py --publication-ref <publication_ref> --check` for each generated page.
- [ ] Run `python3 scripts/check-public-safe-content.py`.
- [ ] Run `python3 -m unittest tests/test_wechat_tools.py`.
- [ ] Run `git diff --check`.
- [ ] Run `./scripts/check-docs.sh` because Sphinx pages are changed.
