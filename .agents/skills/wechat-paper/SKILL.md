---
name: wechat-paper
description: Use when generating, reviewing, or updating WOEAI WeChat Official Account articles and matching RTD paper companion pages from published journal papers. Applies to one-paper-one-article drafts, historical paper reposts, formula and figure handling, Markdown-to-RST conversion, article/review/RTD outputs, backlog updates, and public-safe publication workflows in this repository.
---

# WeChat Paper Article Skill

Use this skill when a task asks to create, revise, review, or track a WeChat Official Account article based on a published WOEAI journal paper, including the matching Read the Docs paper companion page.

The output is a public-safe reader-facing Markdown article, a matching Sphinx-compatible RST page for RTD, and a separate review note. Do not publish to WeChat automatically.

## Required Context

Read these files before drafting:

1. `AGENTS.md` for public-site boundaries and required checks.
2. `CONTEXT.md` for WOEAI vocabulary and semantic constraints.
3. `wechat/README.md` for the WeChat content workflow and backlog state model.
4. `wechat/STYLE.md` for article structure, tone, formula rules, and figure rules.
5. `wechat/templates/paper-explainer.md` for the draft shape.
6. `wechat/templates/review-checklist.md` for review gates.
7. `wechat/backlog/selected-papers.yml` to select and update the paper state.
8. `docs/source/Publications.rst` and the relevant research direction page for public website anchors.
9. Existing `docs/source/Research.rst` and direction pages for the RTD Academic Progress placement.

If the task mentions Zotero, DOI, a PDF, or a paper title, inspect those sources when available. Do not invent missing bibliographic facts.

When a local PDF or author manuscript is available, inspect the original paper body, figures, captions, and conclusion instead of relying only on a public abstract.

## Article Unit

Use one selected paper per article.

Do not turn a paper article into a multi-paper survey. Related papers can appear only in `延伸阅读`.

## Public Safety

This repository is public. Anything committed here must be safe to expose.

Never include:

- WeChat AppSecret, access token, refresh token, cookies, preview credentials, or API keys.
- Zotero API keys or private library credentials.
- private partner names or unpublished project details.
- private review notes.
- publisher-owned figures unless reuse rights or author-owned source status are confirmed. For WOEAI WeChat paper articles, the normal scope is the user's own authored papers; once author status is confirmed, figures in that paper PDF may be used directly.
- local WeChat preview HTML.
- source images that are not approved for public release.

Unknown public facts should be written as `to be confirmed` in private planning notes, not in public drafts.

## Research Taxonomy

Use only these public research families and subdirections unless the user explicitly updates the taxonomy:

- `建筑结构抗风`
  - `数值风洞与湍动入流`
  - `高层建筑抗风与优化`
- `海上漂浮风电`
  - `浮式风机系统一体化分析与优化`
  - `浮式混凝土平台结构设计`
  - `数值风浪流水池`

## Draft Workflow

1. Select the target item from `wechat/backlog/selected-papers.yml`.
2. Verify `publication_ref`, title, year, DOI, and WOEAI website anchor.
3. Create or update the reader-facing article under `wechat/articles/draft-public-safe/`.
4. Name the article with the paper's `publication_ref`, for example `wechat/articles/draft-public-safe/ref-zhao2026-BS.md`.
5. Convert the same public article content to a Sphinx-compatible RST page for RTD. Do not add a separate Markdown route to Sphinx.
6. Create or update the publishing note under `wechat/articles/review/`, for example `wechat/articles/review/ref-zhao2026-BS.review.md`.
7. Start the reader-facing article from `wechat/templates/paper-explainer.md`, but remove any production-only placeholders before treating it as copy-ready.
8. Keep review details, evidence notes, copyright status, formula preview status, figure insertion status, RST conversion notes, and human checklists in the `.review.md` file, not in the reader-facing article or RTD page.
9. Keep `wechat_status` aligned with the backlog state model:
   - `selected`
   - `drafting`
   - `reviewing`
   - `ready_to_publish`
   - `published`
   - `archived`
10. Update `wechat/backlog/selected-papers.yml` only when the user's task asks for workflow tracking or after a draft/review step changes status.

## Output Model

Generate three public-safe files or records for each paper article:

- `wechat/articles/draft-public-safe/<publication_ref>.md`: reader-facing WeChat Markdown. It should be clean enough to copy into a WeChat Markdown editor or the WeChat backend.
- `docs/source/paper-notes/<publication_ref>.rst`: RTD Paper Companion Page. It should present the same public title, body text, images, DOI link, WOEAI publication anchor, and contact/link intent as the WeChat Markdown article, with only markup and rendering differences needed for Sphinx/reStructuredText.
- `wechat/articles/review/<publication_ref>.review.md`: publishing note for authors and editors. It records metadata, evidence, figure source status, formula preview status, copyright checks, unresolved tasks, and checks run.

The reader-facing Markdown must not contain:

- YAML front matter,
- `pending` status,
- `计划配图`,
- `发布前人工复核项`,
- private file paths,
- copyright notes intended only for the editor,
- source evidence notes,
- credential or preview workflow notes.

For author-confirmed WOEAI papers, extract suitable figures directly from the paper PDF or author manuscript, store them under `wechat/assets/public-safe/<publication_ref>/`, and insert normal Markdown image links in the reader-facing article. If images are genuinely not ready, omit image placeholders from the reader-facing article and record the reason in the review note.

## RTD Paper Companion Page

The RTD page is not a shorter summary and not a separate editorial rewrite. It is the Sphinx/RST rendering of the same public article content.

Rules:

- Convert the WeChat Markdown article to reStructuredText rather than enabling a new Markdown/MyST route in Sphinx.
- Use `docs/source/paper-notes/<publication_ref>.rst` as the canonical RTD page path, for example `docs/source/paper-notes/ref-zhao2026-BS.rst`.
- Preserve the same title, section order, body text, images, DOI link, WOEAI publication anchor, related direction links, and contact/link intent.
- Change only what Sphinx rendering requires: heading underline syntax, image directives, internal links, external links, code/formula representation, and relative asset paths.
- Keep private review metadata out of the RST page.
- Register RTD pages through the relevant research-direction Academic Progress section, grouped by second-level research subdirection.
- On `docs/source/Research.rst`, use the public label `学术进展 Academic Progress` instead of `近期证据 Selected Proof Points` when listing these companion pages.
- Within each second-level subdirection, list RTD Paper Companion Pages by publication date descending until a more specific sorting rule is chosen.
- If the RST page or research-direction navigation changes, this is a Sphinx site-build input and `./scripts/check-docs.sh` becomes required.

## Article Structure

Use this default order unless the paper strongly requires a small adjustment:

1. `论文信息`
2. `研究问题`
3. `方法贡献`
4. `关键发现`
5. `公式说明`
6. `工程意义`
7. `适用边界`
8. `图文说明` when public-safe images are inserted
9. `延伸阅读`
10. `阅读原文`
11. `联系入口`

Write for technically literate readers who may include prospective students, collaborators, engineering software users, and academic peers.

Tone:

- Use the author's perspective and voice. The article should read like WOEAI or the authors are explaining their own paper to readers.
- Prefer `我们在这项研究中...`, `这项工作...`, and `这篇论文...` over third-party phrases such as `从公开摘要可确认...`.
- Scholarly first.
- Engineering relevance second.
- No hype.
- No unsupported partner names or project claims.
- Keep limitations visible.
- Avoid standing outside the paper as a detached reviewer unless explicitly writing a review note.

## Formula Handling

Do not render formulas as images.

Use the most direct formula format supported by the WeChat publishing workflow selected for the article. Keep formulas short enough for mobile display when possible.

For each important formula:

- provide the formula in the draft,
- explain the variables in nearby text,
- add one plain-language sentence explaining what the formula means,
- mark `formula_preview_checked: false` until the formula is checked in the final WeChat backend mobile preview.

If the formula cannot be reliably represented in the current publishing workflow, record the issue in `公式说明` and simplify the article around the concept rather than using a blurry image.

## Figure Handling

Prefer the paper's original high-resolution figures and use them directly when the paper is authored by the user/WOEAI and author status has been confirmed.

Use the clearest legally safe source:

- PDF-embedded original figures extracted from the paper file,
- author-owned original figure export,
- author manuscript figure,
- supplementary material,
- publisher figure with confirmed reuse rights.

Redraw only when the original figure is unavailable, legally unsafe, low-resolution, or unsuitable for WeChat display.

For the user's own papers, do not leave the public article imageless while waiting for separate figure approval. Extract figures from the PDF first, then let the review note track the source, extraction method, and mobile preview status.

Recommended extraction order:

1. Use `pdfimages -all` to inspect and extract embedded PDF images.
2. If the PDF stores a figure as ordered strips, stitch those extracted strips back into a complete figure before using page-render cropping.
3. Use page-render cropping only when the figure is vector-only, not recoverable from embedded images, or needs surrounding vector labels.
4. Store final public-safe assets in `wechat/assets/public-safe/<publication_ref>/`.
5. Keep temporary extraction files under ignored local paths such as `wechat/.local/<publication_ref>/`.

Every figure needs:

- figure identifier from the paper, when applicable,
- source or generation method,
- copyright/reuse note,
- mobile clarity preview result,
- `figure_preview_checked: false` until final WeChat backend preview.

For a normal paper article, include several figure positions when the original paper has suitable figures. Choose figures that help readers understand:

- the method or workflow,
- the study object or geometry,
- the validation evidence,
- the final engineering or platform application.

Do not leave the article imageless unless the paper truly has no suitable figure or the user requests text-only output.

Do not commit unapproved source images for papers outside the user's authored-paper scope. Keep private or unapproved image work under ignored local paths such as `wechat/.local/`.

If image rights or final high-resolution assets are not ready for a non-authored or unclear paper, put figure recommendations in the review note. Do not put visible `待上传原文图` placeholders into the reader-facing article.

## Original Article Link

Add a `阅读原文` section near the end of the article.

For the first workflow version, use the DOI URL as the reading link. Do not imply that the repository hosts the full paper PDF unless a public author manuscript or approved download link is actually available.

## Draft Quality Gates

Before calling a draft ready:

- DOI and WOEAI publication anchor are checked.
- Research family and subdirection match `wechat/topics/`.
- No invented collaboration, partner, project, facility, award, or metric claims appear.
- The reader-facing article has no YAML front matter, pending fields, figure plans, private notes, or human checklist.
- Important formulas are not images and have explanations.
- For author-confirmed papers, suitable PDF figures are extracted into `wechat/assets/public-safe/<publication_ref>/` and inserted into the article. For non-authored or unclear papers, suitable figure recommendations are recorded in the review note until rights are confirmed.
- The article includes a DOI-based `阅读原文` link.
- The separate review note records source evidence, image/copyright status, formula preview status, and remaining human-review items.
- The RTD Paper Companion Page matches the WeChat Markdown article in title, body text, images, DOI link, WOEAI publication anchor, and contact/link intent.
- The relevant research-direction page exposes the RTD page under `学术进展 Academic Progress`, grouped by second-level research subdirection and sorted by publication date descending.
- `wechat/templates/review-checklist.md` is satisfied or remaining items are explicitly marked in the review note.
- `scripts/check-public-safe-content.py` passes.
- Markdown/path checks pass for the article and review files, including checking that reader-facing image links resolve to public-safe assets when images are inserted.
- `./scripts/check-docs.sh` is not required for pure WeChat article/review updates because those files are not Sphinx pages. Run docs checks only when the task also changes Sphinx pages, Sphinx config, website data generation, publication pages, or other site-build inputs.

Use `PYTHON_BIN=/opt/homebrew/bin/python3.12 ./scripts/check-docs.sh` on this Mac if the default `python3` is older than 3.12.

## Output

When generating a draft, return:

- reader-facing article path,
- RTD Paper Companion Page path, when generated or updated,
- review note path,
- source evidence used,
- unresolved facts or human-review items,
- formula preview requirements,
- figure reuse and preview requirements,
- commands/checks run.

Do not claim the article is publish-ready until the WeChat backend mobile preview has checked formulas and figures.
