# WOEAI WeChat Paper Batch 2345 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert selected backlog items 2/3/4/5 into public-safe WOEAI one-paper WeChat article sources, matching RTD Paper Companion Pages, review notes, cover records, and no-submit WeChat draft checks.

**Architecture:** Each `wechat/articles/draft-public-safe/ref-*.md` file is the public content master for its paper. Each paper has an independent worker-owned output set; the controller handles shared navigation, backlog state, cover generation coordination, and final validation. No task creates or updates a live WeChat draft without a later explicit live confirmation from the user.

**Tech Stack:** Sphinx/reStructuredText, Zotero Desktop Local API, WOEAI WeChat Markdown tools, MathJax SVG formula renderer, PDF evidence extraction tools (`pdftotext`, `pdfimages`), public-safe image assets, and `./scripts/check-docs.sh`.

---

## Current Worktree Context

These files already have local modifications before this batch starts. Treat them as user or prior-rule edits and do not revert them:

- `.agents/skills/wechat-paper/SKILL.md`
- `AGENTS.md`
- `claude.md`
- `gemini.md`
- `wechat/README.md`
- `wechat/STYLE.md`
- `wechat/articles/review/ref-zhao2026-BS.review.md`
- `wechat/templates/paper-review.md`
- `wechat/templates/review-checklist.md`

The existing local edits add source-acquisition and evidence-location requirements. Every new review note in this batch must include both:

- `源文件获取记录`
- `关键事实证据定位记录`

## Batch Scope

Process these four selected backlog entries:

| Order | publication_ref | Zotero key | Research placement | Published record |
|---|---|---|---|---|
| 2 | `ref-zhao2025-SCS` | `V6PLJENN` | 建筑结构抗风 / 数值风洞与湍动入流 | Sustainable Cities and Society, 2025, 123: 106237, DOI `10.1016/j.scs.2025.106237` |
| 3 | `ref-li2024-POF` | `2YG78T62` | 建筑结构抗风 / 数值风洞与湍动入流 | Physics of Fluids, 2024, 36(3): 035127, DOI `10.1063/5.0194006` |
| 4 | `ref-tang2025-JBE` | `4BCF65NB` | 建筑结构抗风 / 高层建筑抗风与优化 | Journal of Building Engineering, 2025, 103: 112131, DOI `10.1016/j.jobe.2025.112131` |
| 5 | `ref-he2026-OE-structural` | `EMID6LAJ` | 海上漂浮风电 / 浮式混凝土平台结构设计 | Ocean Engineering, 2026, 346: 123951, DOI `10.1016/j.oceaneng.2025.123951` |

Zotero attachment inventory from the 2026-06-10 pre-plan check:

| publication_ref | PDF attachment key | Attachment mode | Notes |
|---|---|---|---|
| `ref-zhao2025-SCS` | `8DSM76PX` | `imported_file` | PDF and HTML attachment records exist |
| `ref-li2024-POF` | `RIVR33QT` | `imported_url` | PDF and HTML attachment records exist; verify the local PDF file before treating it as evidence |
| `ref-tang2025-JBE` | `G2D6USRE` | `imported_file` | PDF and HTML attachment records exist |
| `ref-he2026-OE-structural` | `UY7S47UC` | `imported_file` | PDF and HTML attachment records exist |

Do not automatically scrape or download PDFs from publisher pages, DOI pages, search results, Google Scholar, ResearchGate, or Sci-Hub. Web pages may verify public metadata only. If a needed local PDF is unavailable, record the gap in the review note and stop short of inventing PDF-derived facts.

## File Structure

Create per-paper public outputs:

- `wechat/articles/draft-public-safe/ref-zhao2025-SCS.md`
- `wechat/articles/draft-public-safe/ref-li2024-POF.md`
- `wechat/articles/draft-public-safe/ref-tang2025-JBE.md`
- `wechat/articles/draft-public-safe/ref-he2026-OE-structural.md`
- `wechat/articles/review/ref-zhao2025-SCS.review.md`
- `wechat/articles/review/ref-li2024-POF.review.md`
- `wechat/articles/review/ref-tang2025-JBE.review.md`
- `wechat/articles/review/ref-he2026-OE-structural.review.md`
- `wechat/articles/review/ref-zhao2025-SCS.cover-brief.md`
- `wechat/articles/review/ref-li2024-POF.cover-brief.md`
- `wechat/articles/review/ref-tang2025-JBE.cover-brief.md`
- `wechat/articles/review/ref-he2026-OE-structural.cover-brief.md`
- `docs/source/paper-notes/ref-zhao2025-SCS.rst`
- `docs/source/paper-notes/ref-li2024-POF.rst`
- `docs/source/paper-notes/ref-tang2025-JBE.rst`
- `docs/source/paper-notes/ref-he2026-OE-structural.rst`
- `wechat/assets/public-safe/ref-zhao2025-SCS/`
- `wechat/assets/public-safe/ref-li2024-POF/`
- `wechat/assets/public-safe/ref-tang2025-JBE/`
- `wechat/assets/public-safe/ref-he2026-OE-structural/`

Modify shared integration files only in controller/final integration tasks:

- `wechat/backlog/selected-papers.yml`
- `docs/source/Research.rst`
- `docs/source/index.rst`

Do not modify `docs/source/Publications.rst` or `docs/source/PublicationsByResearch.rst` unless a verification check reveals a real citation mismatch with Zotero or the existing public record.

## Subagent Execution Model

Use fresh workers sequentially, one paper at a time, with disjoint write ownership:

1. Controller performs Task 1 and prepares exact source inventory.
2. Worker handles one paper task and writes only that paper's files under `wechat/articles/draft-public-safe/`, `wechat/articles/review/`, `docs/source/paper-notes/`, and that paper's directory in `wechat/assets/public-safe/`.
3. Controller or reviewer checks spec compliance for that paper before starting the next worker.
4. Controller performs shared navigation/backlog integration after all four paper tasks are complete.
5. Controller performs final validation across all changed files.

Workers are not alone in the codebase. They must not revert existing local edits or edits from earlier workers.

### Task 1: Baseline And Source Inventory

**Files:**
- Read: `AGENTS.md`
- Read: `CONTEXT.md`
- Read: `wechat/README.md`
- Read: `wechat/STYLE.md`
- Read: `wechat/templates/paper-explainer.md`
- Read: `wechat/templates/paper-review.md`
- Read: `wechat/templates/review-checklist.md`
- Read: `wechat/backlog/selected-papers.yml`
- Read: `docs/source/Publications.rst`
- Read: `docs/source/Research.rst`
- Read: `docs/source/BuildingStructuralWindResistance.rst`
- Read: `docs/source/FloatingOffshoreWindEnergy.rst`
- Private ignored workspace: `wechat/.local/batch-2345/`

- [ ] **Step 1: Confirm dirty worktree baseline**

Run:

```bash
git status --short --branch
git diff --stat
git diff --check
```

Expected:

- Existing rule/template/review-note edits are present.
- No whitespace errors from existing or new edits.
- No files are reverted.

- [ ] **Step 2: Create ignored private inventory directory**

Run:

```bash
mkdir -p wechat/.local/batch-2345
```

Expected:

- Directory exists under ignored `wechat/.local/`.
- No private files are staged or committed from this directory.

- [ ] **Step 3: Query Zotero metadata without credentials**

Run:

```bash
for key in V6PLJENN 2YG78T62 4BCF65NB EMID6LAJ; do
  curl -s -f -H 'Zotero-API-Version: 3' "http://127.0.0.1:23119/api/users/0/items/$key?format=json" \
    | jq '{key, title:.data.title, date:.data.date, DOI:.data.DOI, publicationTitle:.data.publicationTitle, volume:.data.volume, issue:.data.issue, pages:.data.pages, abstract_len:(.data.abstractNote|length), creators:.data.creators}'
done
```

Expected:

- Four JSON summaries print.
- Each item has DOI, title, journal, date, pages, creators, and nonzero `abstract_len`.
- No API key, credential, cookie, or private path is printed.

- [ ] **Step 4: Query Zotero attachment summaries without absolute paths**

Run:

```bash
for key in V6PLJENN 2YG78T62 4BCF65NB EMID6LAJ; do
  printf '%s\n' "KEY $key"
  curl -s -f -H 'Zotero-API-Version: 3' "http://127.0.0.1:23119/api/users/0/items/$key/children?format=json" \
    | jq '[.[] | {key, itemType:.data.itemType, title:.data.title, contentType:.data.contentType, linkMode:.data.linkMode, filename:.data.filename}]'
done
```

Expected:

- The PDF attachment keys match the batch scope table.
- Attachment output omits absolute local paths.
- `ref-li2024-POF` is flagged for an extra local-file availability check because its PDF attachment mode is `imported_url`.

- [ ] **Step 5: Confirm local PDF availability privately**

Run these commands locally for each PDF attachment key. Keep resolved paths in shell variables only; do not paste them into committed files.

```bash
ATTACH_KEY=8DSM76PX
find "$HOME/Zotero/storage/$ATTACH_KEY" -maxdepth 1 -type f -iname '*.pdf' -print

ATTACH_KEY=RIVR33QT
find "$HOME/Zotero/storage/$ATTACH_KEY" -maxdepth 1 -type f -iname '*.pdf' -print

ATTACH_KEY=G2D6USRE
find "$HOME/Zotero/storage/$ATTACH_KEY" -maxdepth 1 -type f -iname '*.pdf' -print

ATTACH_KEY=UY7S47UC
find "$HOME/Zotero/storage/$ATTACH_KEY" -maxdepth 1 -type f -iname '*.pdf' -print
```

Expected:

- Each command prints exactly one local PDF path, or the review note for that paper records `需要同步 PDF 或提供作者稿`.
- No absolute private path is copied into public Markdown, RST, review notes, or this plan.

- [ ] **Step 6: Render or extract private PDF evidence aids**

For each available PDF, use an ignored per-paper directory. Example for `ref-zhao2025-SCS`:

```bash
REF=ref-zhao2025-SCS
mkdir -p "wechat/.local/$REF/pdf-pages" "wechat/.local/$REF/pdf-images"
pdftotext "$PDF_PATH" "wechat/.local/$REF/paper.txt"
pdfimages -list "$PDF_PATH" > "wechat/.local/$REF/pdfimages-list.txt"
```

Expected:

- Text and image inventory exist only under the matching ignored `wechat/.local/ref-*/` directory.
- Review notes later record public-safe evidence locations by PDF page, section, figure number, table, or equation number, not private paths.

### Task 2: `ref-zhao2025-SCS` Article, Review, Assets, And RTD Page

**Files:**
- Create: `wechat/articles/draft-public-safe/ref-zhao2025-SCS.md`
- Create: `wechat/articles/review/ref-zhao2025-SCS.review.md`
- Create: `wechat/articles/review/ref-zhao2025-SCS.cover-brief.md`
- Create: `docs/source/paper-notes/ref-zhao2025-SCS.rst`
- Create/modify: `wechat/assets/public-safe/ref-zhao2025-SCS/`
- Read: `docs/source/Publications.rst`
- Read: `docs/source/BuildingStructuralWindResistance.rst`

- [ ] **Step 1: Draft from the public-safe article template**

Use `wechat/templates/paper-explainer.md` as the shape and remove all template-only instructions from the reader-facing article.

Required public article structure:

```markdown
# 数值风洞 | 用 3D Gaussian Splatting 重建城市建筑几何

## 论文信息

## 摘要

## 研究问题

## 方法贡献

## 关键发现

## 工程意义

## 适用边界

## 延伸阅读
```

Acceptance:

- The title can be refined after PDF reading, but it must keep the `数值风洞 | ...` pattern and describe the problem solved.
- `论文信息` copies authors, journal, year, DOI, and WOEAI direction from Zotero and `docs/source/Publications.rst`.
- `摘要` contains a faithful Chinese translation of Zotero/PDF abstract and then `**英文摘要**` plus the original abstract.
- The article explains 3D Gaussian Splatting as an urban building-geometry reconstruction route for wind simulation without inventing external partners or deployment claims.

- [ ] **Step 2: Extract and insert public-safe figures**

Use the local PDF attachment `8DSM76PX` as the first evidence source. Store final figures under:

```text
wechat/assets/public-safe/ref-zhao2025-SCS/
```

Choose several figures that show the method workflow, 3DGS or building reconstruction result, and wind-simulation validation or use case. Each inserted Markdown image must use this pattern:

```markdown
![图 1 论文原图中文题名](../../assets/public-safe/ref-zhao2025-SCS/fig-01-method.png)

图 1 论文原图中文题名

单独一段中文解释，说明这张图帮助读者理解什么。
```

Acceptance:

- Figure title line is a faithful Chinese translation of the original figure title.
- Explanatory line is separate from the title.
- Final figure files are public-safe and committed only under `wechat/assets/public-safe/ref-zhao2025-SCS/`.
- Temporary extraction files remain under `wechat/.local/ref-zhao2025-SCS/`.

- [ ] **Step 3: Create review note with source and evidence records**

Create `wechat/articles/review/ref-zhao2025-SCS.review.md` from `wechat/templates/paper-review.md`.

Required front matter:

```yaml
publication_ref: ref-zhao2025-SCS
zotero_key: V6PLJENN
doi: 10.1016/j.scs.2025.106237
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: reviewing
wechat_author: WOEAI
source_checked: true
abstract_checked: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
body_images_upload_approved: true
rtd_page_checked: true
```

Acceptance:

- `源文件获取记录` includes Zotero key, metadata source, attachment-record status, local PDF status, PDF source type, private-storage class, Zotero Web API `/file` status, web-download status, abstract source, body-evidence source, and figure source.
- `关键事实证据定位记录` records abstract source, core claims, key figures, and any formulas or explicitly says no important original formula is used.
- No absolute private source PDF path appears.

- [ ] **Step 4: Create cover brief**

Create `wechat/articles/review/ref-zhao2025-SCS.cover-brief.md`.

Include three candidate concepts:

- research scene: urban streets/buildings with wind-field simulation overlay;
- method: Gaussian point-cloud reconstruction becoming clean building geometry;
- engineering impact: faster transition from visual data to simulation-ready urban model.

Acceptance:

- Prompt avoids embedded text, logos, partner names, and unconfirmed place names.
- Review note will later record the selected cover path and crop-preview result.

- [ ] **Step 5: Generate RTD companion page**

Run:

```bash
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2025-SCS
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2025-SCS --check
```

Expected:

- `docs/source/paper-notes/ref-zhao2025-SCS.rst` is generated.
- The `--check` command reports the RTD companion page is in sync.

- [ ] **Step 6: Run per-paper no-submit checks**

Run after cover and body images are present:

```bash
python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-zhao2025-SCS --theme academic-clean
python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-zhao2025-SCS --theme academic-clean
```

Expected:

- Both commands pass.
- Output says `will_read_credentials: false`, `will_contact_wechat: false`, and `will_create_or_update_draft: false`.
- `content_source_url` defaults to `https://woeai.readthedocs.io/zh-cn/latest/paper-notes/<publication_ref>.html` unless the user later explicitly chooses a different bottom `阅读原文` target or an intentionally blank value.

### Task 3: `ref-li2024-POF` Article, Review, Assets, And RTD Page

**Files:**
- Create: `wechat/articles/draft-public-safe/ref-li2024-POF.md`
- Create: `wechat/articles/review/ref-li2024-POF.review.md`
- Create: `wechat/articles/review/ref-li2024-POF.cover-brief.md`
- Create: `docs/source/paper-notes/ref-li2024-POF.rst`
- Create/modify: `wechat/assets/public-safe/ref-li2024-POF/`
- Read: `docs/source/Publications.rst`
- Read: `docs/source/BuildingStructuralWindResistance.rst`

- [ ] **Step 1: Confirm local PDF evidence for imported-url attachment**

Use attachment key `RIVR33QT`.

Run:

```bash
ATTACH_KEY=RIVR33QT
find "$HOME/Zotero/storage/$ATTACH_KEY" -maxdepth 1 -type f -iname '*.pdf' -print
```

Expected:

- If a local PDF exists, use it for body evidence and figures.
- If no local PDF exists, record `需要同步 PDF 或提供作者稿` in `ref-li2024-POF.review.md`, avoid PDF-derived claims, and do not fetch a web PDF without explicit user approval.

- [ ] **Step 2: Draft the formula-aware article**

Use this public article structure:

```markdown
# 数值风洞 | 用矢量势随机流生成无散湍流

## 论文信息

## 摘要

## 研究问题

## 方法贡献

## 关键发现

## 工程意义

## 适用边界

## 延伸阅读
```

Acceptance:

- The article explains why divergence-free homogeneous isotropic turbulence matters for inflow generation and numerical wind tunnel work.
- Important variables, spectra, divergence-free conditions, and unit-bearing values use Markdown LaTeX, not code spans.
- Display formulas stay inside narrative sections and have plain-language explanations.
- Formula notation uses explicit roman text for word-like subscripts, such as `$K_{\mathrm{CFD}}$` when such symbols are introduced editorially.

- [ ] **Step 3: Extract and insert figures**

Store final figures under:

```text
wechat/assets/public-safe/ref-li2024-POF/
```

Choose figures that help readers understand the vector-potential generation logic, validation against target spectra, divergence-free behavior, or turbulence-field examples.

Acceptance:

- Each figure has a two-line Chinese caption.
- The review note maps each used figure to PDF page and original figure number.
- Extraction details stay in the review note, not the reader-facing article.

- [ ] **Step 4: Create review note with formula evidence records**

Create `wechat/articles/review/ref-li2024-POF.review.md` from `wechat/templates/paper-review.md`.

Required front matter:

```yaml
publication_ref: ref-li2024-POF
zotero_key: 2YG78T62
doi: 10.1063/5.0194006
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: reviewing
wechat_author: WOEAI
source_checked: true
abstract_checked: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
body_images_upload_approved: true
rtd_page_checked: true
```

Acceptance:

- `源文件获取记录` explicitly states the attachment mode and selected evidence source.
- `关键事实证据定位记录` includes key original equations by PDF page and equation number when the article uses them.
- Editorial explanatory formulas are marked as editorial and linked to the paper evidence they explain.

- [ ] **Step 5: Create cover brief**

Create `wechat/articles/review/ref-li2024-POF.cover-brief.md`.

Include three candidate concepts:

- research scene: clean turbulent vector field with streamlines and vorticity texture;
- method: vector potential field transforming into divergence-free turbulence;
- engineering impact: controllable inflow field for numerical wind tunnel simulation.

Acceptance:

- No raster formula screenshot is used as the cover.
- No generated text is embedded in the cover concept.

- [ ] **Step 6: Generate RTD companion page and no-submit checks**

Run:

```bash
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-li2024-POF
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-li2024-POF --check
python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-li2024-POF --theme academic-clean --math-renderer mathjax-svg
python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-li2024-POF --theme academic-clean --math-renderer mathjax-svg
```

Expected:

- RTD companion page is in sync.
- Formula renderer is `mathjax-svg`.
- No-submit checks do not read credentials or contact WeChat.

### Task 4: `ref-tang2025-JBE` Article, Review, Assets, And RTD Page

**Files:**
- Create: `wechat/articles/draft-public-safe/ref-tang2025-JBE.md`
- Create: `wechat/articles/review/ref-tang2025-JBE.review.md`
- Create: `wechat/articles/review/ref-tang2025-JBE.cover-brief.md`
- Create: `docs/source/paper-notes/ref-tang2025-JBE.rst`
- Create/modify: `wechat/assets/public-safe/ref-tang2025-JBE/`
- Read: `docs/source/Publications.rst`
- Read: `docs/source/BuildingStructuralWindResistance.rst`

- [ ] **Step 1: Draft the GNN/tall-building article**

Use this public article structure:

```markdown
# 结构抗风 | 用图神经网络预测高层建筑结构响应

## 论文信息

## 摘要

## 研究问题

## 方法贡献

## 关键发现

## 工程意义

## 适用边界

## 延伸阅读
```

Acceptance:

- The article explains graph neural networks as a structural-response prediction tool for tall building structures.
- Avoid claims about deployment, commercial software, partner projects, or production use unless directly present in public paper evidence.
- Use formula markup for metrics or response variables if included.

- [ ] **Step 2: Extract and insert figures**

Use attachment key `G2D6USRE`. Store final figures under:

```text
wechat/assets/public-safe/ref-tang2025-JBE/
```

Choose figures that show the GNN workflow, graph representation, training/application process, prediction performance, or response comparison.

Acceptance:

- Figures are clear on mobile scale.
- Captions follow the two-line Chinese rule.
- Review note maps figures to PDF page and original figure number.

- [ ] **Step 3: Create review note**

Create `wechat/articles/review/ref-tang2025-JBE.review.md` from `wechat/templates/paper-review.md`.

Required front matter:

```yaml
publication_ref: ref-tang2025-JBE
zotero_key: 4BCF65NB
doi: 10.1016/j.jobe.2025.112131
research_family: 建筑结构抗风
subdirection: 高层建筑抗风与优化
publication_mode: first_publish
wechat_status: reviewing
wechat_author: WOEAI
source_checked: true
abstract_checked: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
body_images_upload_approved: true
rtd_page_checked: true
```

Acceptance:

- `源文件获取记录` and `关键事实证据定位记录` are complete and public-safe.
- Abstract, method claims, performance claims, and limitations point to Zotero abstract or audited PDF locations.

- [ ] **Step 4: Create cover brief**

Create `wechat/articles/review/ref-tang2025-JBE.cover-brief.md`.

Include three candidate concepts:

- research scene: high-rise structure under wind with response traces;
- method: graph network nodes and edges mapped onto a tall-building structure;
- engineering impact: rapid structural-response screening for wind-resistance design.

Acceptance:

- No embedded text.
- No unconfirmed real building or partner identity.

- [ ] **Step 5: Generate RTD companion page and no-submit checks**

Run:

```bash
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2025-JBE
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2025-JBE --check
python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-tang2025-JBE --theme academic-clean
python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-tang2025-JBE --theme academic-clean
```

Expected:

- RTD companion page is in sync.
- Dry-run lists approved cover and body images.
- No-submit checks do not read credentials or contact WeChat.

### Task 5: `ref-he2026-OE-structural` Article, Review, Assets, And RTD Page

**Files:**
- Create: `wechat/articles/draft-public-safe/ref-he2026-OE-structural.md`
- Create: `wechat/articles/review/ref-he2026-OE-structural.review.md`
- Create: `wechat/articles/review/ref-he2026-OE-structural.cover-brief.md`
- Create: `docs/source/paper-notes/ref-he2026-OE-structural.rst`
- Create/modify: `wechat/assets/public-safe/ref-he2026-OE-structural/`
- Read: `docs/source/Publications.rst`
- Read: `docs/source/FloatingOffshoreWindEnergy.rst`

- [ ] **Step 1: Draft the floating-offshore-wind article**

Use this public article structure:

```markdown
# 漂浮风电 | 用钢筋混凝土优化半潜式浮式平台结构

## 论文信息

## 摘要

## 研究问题

## 方法贡献

## 关键发现

## 工程意义

## 适用边界

## 延伸阅读
```

Acceptance:

- The article explains reinforced-concrete semi-submersible platform structural design and optimization.
- It distinguishes structural design, platform motion/loads, and optimization evidence only when supported by the paper.
- It does not invent cost savings, deployment cases, partner names, prototype status, or certification claims.

- [ ] **Step 2: Extract and insert figures**

Use attachment key `UY7S47UC`. Store final figures under:

```text
wechat/assets/public-safe/ref-he2026-OE-structural/
```

Choose figures that show the platform concept, structural layout, optimization workflow, load/response comparison, or final design result.

Acceptance:

- Figures use public-safe source material from the paper PDF.
- Captions follow the two-line Chinese rule.
- Review note maps used figures to PDF page and original figure number.

- [ ] **Step 3: Create review note**

Create `wechat/articles/review/ref-he2026-OE-structural.review.md` from `wechat/templates/paper-review.md`.

Required front matter:

```yaml
publication_ref: ref-he2026-OE-structural
zotero_key: EMID6LAJ
doi: 10.1016/j.oceaneng.2025.123951
research_family: 海上漂浮风电
subdirection: 浮式混凝土平台结构设计
publication_mode: first_publish
wechat_status: reviewing
wechat_author: WOEAI
source_checked: true
abstract_checked: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
body_images_upload_approved: true
rtd_page_checked: true
```

Acceptance:

- `源文件获取记录` and `关键事实证据定位记录` are complete and public-safe.
- Review note records any important formulas or says the article uses only editorial inline variables and no paper equation as a central public formula.

- [ ] **Step 4: Create cover brief**

Create `wechat/articles/review/ref-he2026-OE-structural.cover-brief.md`.

Include three candidate concepts:

- research scene: semi-submersible floating offshore wind platform in ocean environment;
- method: structural members, concrete platform, and optimization grid;
- engineering impact: robust platform structure for floating offshore wind systems.

Acceptance:

- No real project site, company name, or unconfirmed asset identity.
- No embedded generated Chinese or English text.

- [ ] **Step 5: Generate RTD companion page and no-submit checks**

Run:

```bash
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-he2026-OE-structural
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-he2026-OE-structural --check
python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-he2026-OE-structural --theme academic-clean
python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-he2026-OE-structural --theme academic-clean
```

Expected:

- RTD companion page is in sync.
- Dry-run lists approved cover and body images.
- No-submit checks do not read credentials or contact WeChat.

### Task 6: Cover Generation And Crop Preview

**Files:**
- Modify: `wechat/articles/review/ref-zhao2025-SCS.review.md`
- Modify: `wechat/articles/review/ref-li2024-POF.review.md`
- Modify: `wechat/articles/review/ref-tang2025-JBE.review.md`
- Modify: `wechat/articles/review/ref-he2026-OE-structural.review.md`
- Create/modify: `wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-v1.png`
- Create/modify: `wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v1.png`
- Create/modify: `wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v1.png`
- Create/modify: `wechat/assets/public-safe/ref-he2026-OE-structural/cover-wechat-900x383-v1.png`

- [ ] **Step 1: Generate or select final covers from approved public-safe briefs**

Use the `wechat-cover` skill. Store final covers under each paper's public-safe asset directory.

Acceptance:

- Each final cover is approximately `900 x 383 px`.
- The main subject is centered for crop safety.
- No embedded text.
- No private project or partner signal.

- [ ] **Step 2: Run local cover previews**

Run:

```bash
python .agents/skills/wechat-cover/scripts/cover_preview.py \
  wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-v1.png \
  wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v1.png \
  wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v1.png \
  wechat/assets/public-safe/ref-he2026-OE-structural/cover-wechat-900x383-v1.png
```

Expected:

- Command prints JSON with `"ok": true`.
- Preview HTML is written under `wechat/.local/cover-previews/`.

- [ ] **Step 3: Update review notes with cover metadata**

Each review note must record:

- cover source or prompt;
- generation tool;
- source candidate path if committed as public-safe;
- final cover path;
- dimensions;
- local crop-preview path;
- approval state;
- WeChat backend preview state.

Required front-matter fields, one in each review note:

- `ref-zhao2025-SCS`: `rtd_cover_image: wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-v1.png`
- `ref-li2024-POF`: `rtd_cover_image: wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v1.png`
- `ref-tang2025-JBE`: `rtd_cover_image: wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v1.png`
- `ref-he2026-OE-structural`: `rtd_cover_image: wechat/assets/public-safe/ref-he2026-OE-structural/cover-wechat-900x383-v1.png`

Acceptance:

- `wechat/tools/markdown_to_rtd.py` can read each cover path from review front matter.
- `wechat/tools/wechat_draft.py preflight` can read each cover path from review front matter.

### Task 7: Shared Navigation, Backlog, And Homepage Integration

**Files:**
- Modify: `docs/source/Research.rst`
- Modify: `docs/source/index.rst`
- Modify: `wechat/backlog/selected-papers.yml`

- [ ] **Step 1: Register hidden RTD toctree pages**

Modify the hidden toctree in `docs/source/Research.rst` so it includes:

```rst
   paper-notes/ref-zhao2026-BS
   paper-notes/ref-he2026-OE-structural
   paper-notes/ref-tang2025-JBE
   paper-notes/ref-zhao2025-SCS
   paper-notes/ref-li2024-POF
```

Acceptance:

- Existing `ref-zhao2026-BS` remains.
- New pages are reachable in Sphinx.

- [ ] **Step 2: Add Academic Progress entries grouped by subdirection**

Update `docs/source/Research.rst` under `学术进展 Academic Progress`.

Required grouping:

```rst
建筑结构抗风
~~~~~~~~~~~~

数值风洞与湍动入流
^^^^^^^^^^^^^^^^^^

- 2026: :doc:`论文解读 | 我们如何用预计算 CFD 数据库加速城市微尺度风环境预测 <paper-notes/ref-zhao2026-BS>`
- 2025: :doc:`数值风洞 | 用 3D Gaussian Splatting 重建城市建筑几何 <paper-notes/ref-zhao2025-SCS>`
- 2024: :doc:`数值风洞 | 用矢量势随机流生成无散湍流 <paper-notes/ref-li2024-POF>`

高层建筑抗风与优化
^^^^^^^^^^^^^^^^^^

- 2025: :doc:`结构抗风 | 用图神经网络预测高层建筑结构响应 <paper-notes/ref-tang2025-JBE>`

海上漂浮风电
~~~~~~~~~~~~

浮式混凝土平台结构设计
^^^^^^^^^^^^^^^^^^^^^^

- 2026: :doc:`漂浮风电 | 用钢筋混凝土优化半潜式浮式平台结构 <paper-notes/ref-he2026-OE-structural>`
```

Acceptance:

- Replace angle-bracket title markers with the final H1 titles from the Markdown articles.
- Do not create dead links.
- Within each subdirection, sort by publication year descending.

- [ ] **Step 3: Update homepage latest academic progress**

Modify `docs/source/index.rst` under `最新学术进展 Latest Academic Progress`.

Acceptance:

- Keep the homepage list concise.
- Include the new RTD companion pages because the homepage is the latest visible update surface.
- Use the final article titles from the Markdown sources.
- Keep no more than ten latest progress entries.

- [ ] **Step 4: Update backlog workflow state**

Modify the four selected entries in `wechat/backlog/selected-papers.yml`:

```yaml
wechat_status: reviewing
revision_note: "Public-safe Markdown, RTD companion page, review note, and no-submit checks prepared; pending human WeChat backend preview and live draft confirmation."
```

Acceptance:

- Do not add `wechat_draft_media_id`, `wechat_draft_created_at`, or `wechat_draft_updated_at` because no live draft is created in this batch.
- Preserve `previous_published_url`, `latest_published_url`, `publication_history`, and other existing fields.

### Task 8: Per-Paper And Whole-Batch Validation

**Files:**
- Validate all files changed in Tasks 2-7.

- [ ] **Step 1: Check reader-facing drafts for editor-only residue**

Run:

```bash
rg -n "pending|待上传|待确认|计划配图|发布前任务|发布前人工复核项|wechat_draft_media_id|AppSecret|access_token|Zotero API key" \
  wechat/articles/draft-public-safe/ref-zhao2025-SCS.md \
  wechat/articles/draft-public-safe/ref-li2024-POF.md \
  wechat/articles/draft-public-safe/ref-tang2025-JBE.md \
  wechat/articles/draft-public-safe/ref-he2026-OE-structural.md
```

Expected:

- No matches.
- If `access_token` or similar appears only as part of a false positive introduced by prose, rewrite the prose.

- [ ] **Step 2: Run Markdown-to-RTD sync checks**

Run:

```bash
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2025-SCS --check
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-li2024-POF --check
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2025-JBE --check
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-he2026-OE-structural --check
```

Expected:

- All four report `RTD companion page is in sync`.

- [ ] **Step 3: Run no-submit WeChat draft validations**

Run:

```bash
python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-zhao2025-SCS --theme academic-clean
python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-li2024-POF --theme academic-clean --math-renderer mathjax-svg
python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-tang2025-JBE --theme academic-clean
python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-he2026-OE-structural --theme academic-clean
python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-zhao2025-SCS --theme academic-clean
python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-li2024-POF --theme academic-clean --math-renderer mathjax-svg
python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-tang2025-JBE --theme academic-clean
python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-he2026-OE-structural --theme academic-clean
```

Expected:

- Every summary has `"ok": true`.
- Every summary says `will_read_credentials`, `will_contact_wechat`, and `will_create_or_update_draft` are false.
- Every summary has empty `content_source_url`.

- [ ] **Step 4: Run unit and public-safety checks**

Run:

```bash
python3 -m unittest tests/test_wechat_tools.py
python3 -m unittest discover -s tests
python3 scripts/check-public-safe-content.py
git diff --check
```

Expected:

- Unit tests pass.
- Public-safety check passes.
- Diff check passes.

- [ ] **Step 5: Run Sphinx docs check**

Run:

```bash
./scripts/check-docs.sh
```

Expected:

- Sphinx builds with warnings treated as failures.
- No broken `:doc:` or `:ref:` links.

- [ ] **Step 6: Final human-review summary**

Prepare a concise handoff that lists:

- created article paths;
- created RTD page paths;
- created review note paths;
- cover preview status;
- formula-heavy article status for `ref-li2024-POF`;
- unavailable or weak evidence items;
- all commands run and outcomes;
- explicit reminder that no live WeChat draft was created.

## Review Checklist For Each Paper Worker

Before a paper task is considered complete:

- The Markdown article has no YAML front matter and no editor-only checklist.
- The article has DOI in `论文信息`.
- The article has `摘要` immediately after `论文信息`.
- English abstracts are faithfully translated and preserved as `**英文摘要**`.
- Public claims are supported by Zotero metadata, existing WOEAI publication records, or audited PDF evidence.
- Review note includes `源文件获取记录`.
- Review note includes `关键事实证据定位记录`.
- Public figures live under the matching `wechat/assets/public-safe/ref-*/` paper directory.
- Temporary PDF text, page renders, image strips, and extraction aids live under the matching ignored `wechat/.local/ref-*/` paper directory.
- Formula semantics remain Markdown LaTeX in the public Markdown source.
- RTD companion page is generated from Markdown, not hand-diverged.
- `content_source_url` defaults to `https://woeai.readthedocs.io/zh-cn/latest/paper-notes/<publication_ref>.html` unless the user later explicitly selects a different bottom `阅读原文` target or an intentionally blank value.
- No live WeChat credential file is read.
- No WeChat draft is created or updated.

## Blocking Conditions

Stop and ask the user only if:

- a local PDF is missing and Zotero Web API `/file` cannot be used without reading private Web API credentials or user confirmation;
- a needed source figure is illegible and a redrawn/generative replacement would change the evidence meaning;
- the paper's public record conflicts with Zotero metadata in DOI, title, authors, journal, year, or pages;
- WeChat no-submit validation requires a cover or body image that cannot be made public-safe;
- a shared navigation update conflicts with uncommitted user edits in the same lines.

Do not stop merely because the article is long or formula-heavy; use the plan and run the checks.
