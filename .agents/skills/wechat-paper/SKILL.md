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

## Source Acquisition Priority

Use this Zotero-first order for WOEAI paper articles:

1. Use the Zotero Desktop Local API to read metadata, DOI, and `abstractNote`.
2. Use the Zotero Desktop Local API to list attachment items.
3. If a local PDF attachment exists, use that PDF to extract or verify the
   abstract, figures, captions, and paper body needed for the article.
4. If the local PDF attachment is missing, try the Zotero Web API `/file`
   endpoint for the attachment. Keep Web API keys and downloaded private working
   files outside this public repository.
5. If neither local attachment nor Web API file access is available, record
   `需要同步 PDF 或提供作者稿` in the review note and do not invent PDF-derived
   facts.

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
2. Follow the Source Acquisition Priority above.
3. Verify `publication_ref`, title, year, DOI, and WOEAI website anchor.
4. Create or update the reader-facing article under `wechat/articles/draft-public-safe/`.
5. Name the article with the paper's `publication_ref`, for example `wechat/articles/draft-public-safe/ref-zhao2026-BS.md`.
6. Convert the same public article content to a Sphinx-compatible RST page for RTD. Do not add a separate Markdown route to Sphinx.
7. Create or update the publishing note under `wechat/articles/review/`, for example `wechat/articles/review/ref-zhao2026-BS.review.md`.
8. Start the reader-facing article from `wechat/templates/paper-explainer.md`, but remove any production-only placeholders before treating it as copy-ready.
9. Keep review details, evidence notes, copyright status, formula preview status, figure insertion status, RST conversion notes, and human checklists in the `.review.md` file, not in the reader-facing article or RTD page.
10. Keep `wechat_status` aligned with the backlog state model:
   - `selected`
   - `drafting`
   - `reviewing`
   - `ready_to_publish`
   - `published`
   - `archived`
11. Update `wechat/backlog/selected-papers.yml` only when the user's task asks for workflow tracking or after a draft/review step changes status.

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
2. `摘要`
3. `研究问题`
4. `方法贡献`
5. `关键发现`
6. `工程意义`
7. `适用边界`
8. `图文说明` when public-safe images are inserted
9. `延伸阅读`
10. `阅读原文`

Use this title pattern:

`<title category> | <problem-solving Chinese title>`

Temporarily choose the title category from `数值风洞`, `结构抗风`, or `漂浮风电`.
The title after the separator should describe what problem the paper helps
solve.

Add `摘要` immediately after `论文信息`. For English papers, translate the
original English abstract faithfully into Chinese and then include
`**英文摘要**` plus the original English abstract. Do not invent an abstract when
the original paper abstract is unavailable; keep that issue in the review note
until a paper PDF, author manuscript, or approved source is available.

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

Do not render formulas as images by default.

Use Markdown LaTeX as the canonical formula source in WeChat article drafts: `$...$` for inline formulas and `$$...$$` for display formulas. Render WeChat formulas through the selected WeChat Markdown workflow, such as doocs/md, and verify the resulting formula display in the final WeChat backend mobile preview.

Convert the same LaTeX formula semantics to Sphinx math markup in RTD companion pages: `:math:` roles for inline formulas and `.. math::` directives for display formulas.

Use formula markup for inline mathematical variables, symbolic parameters, metrics, dimensional quantities, and unit-bearing values inside explanatory prose. Examples:

- WeChat draft: `$X_L$`, `$R$`, `$4H_{\max}$`, `$1\,\mathrm{km} \times 1\,\mathrm{km}$`, `$11\,\mathrm{m/s}$`, `$90^\circ$`.
- RTD companion page: `:math:` roles with the same LaTeX body, for example `X_L`, `4H_{\max}`, and `11\,\mathrm{m/s}`.

Do not use Markdown backticks or RST double backticks for mathematical variables or scientific quantities. Reserve code spans for paths, filenames, commands, literal field names, and code identifiers.

Keep formulas short enough for mobile display when possible.

Do not create a standalone `公式说明` section by default. Put formulas directly
inside the section where they are needed, such as `方法贡献`, `关键发现`,
`工程意义`, or `适用边界`.

For each important formula:

- provide the formula in the draft,
- explain the variables in nearby text,
- add one plain-language sentence explaining what the formula means,
- mark `formula_preview_checked: false` until the formula is checked in the final WeChat backend mobile preview.

If the formula cannot be reliably represented in the current publishing workflow, record the issue near the relevant discussion and simplify the article around the concept rather than using a blurry image.

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
- Zotero Desktop Local API metadata, DOI, `abstractNote`, and attachment
  records are checked.
- Local PDF attachment is used when present. If it is missing, Zotero Web API
  `/file` is tried when credentials are available; if that also fails, the
  review note records `需要同步 PDF 或提供作者稿`.
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
