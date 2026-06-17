---
name: wechat-paper
description: Use when generating, reviewing, or updating WOEAI WeChat Official Account articles and matching RTD paper companion pages from published journal papers. Applies to one-paper-one-article drafts, historical paper reposts, formula and figure handling, Markdown-to-RST conversion, article/review/RTD outputs, backlog updates, and public-safe publication workflows in this repository.
---

# WeChat Paper Article Skill

Use this skill when a task asks to create, revise, review, or track a WeChat Official Account article based on a published WOEAI journal paper, including the matching Read the Docs paper companion page.

The output is a public-safe reader-facing Markdown article, a matching Sphinx-compatible RST page for RTD, and a separate review note. Do not publish to WeChat automatically. Automation may create or update WeChat drafts, but the public release step must remain a manual WeChat backend action.

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

Do not automatically scrape or download PDFs from publisher pages, DOI landing
pages, Google Scholar, ResearchGate, Sci-Hub, search results, or other general
web pages. Web pages may be used only to verify public metadata such as DOI,
journal page, or open website records. A web PDF may be downloaded only when
the user explicitly approves a specific public and legal source, such as an OA
PDF, an author manuscript, or a user-provided download link. Store any such
download under an ignored private working path, such as
`wechat/.local/<publication_ref>/`, never commit the PDF to the public
repository, and record the source and approval status in the review note.

Every paper article review note must contain a public-safe `源文件获取记录`
section. Record at least: Zotero item key, metadata source, attachment-record
status, local PDF status, PDF source type, private-storage class, whether
Zotero Web API `/file` was attempted, whether any web PDF download was used,
abstract source, body-evidence source, and figure source. Do not record absolute
private file paths, credentials, cookies, raw API payloads, or downloaded PDF
contents in the public repository.

When a Zotero item has multiple PDF-like attachments, choose the source used
for PDF-derived body evidence and figures in this order:

1. author final manuscript / author manuscript,
2. publisher version of record PDF,
3. open-access platform PDF,
4. preprint,
5. other attachments.

If a lower-priority attachment is used because a higher-priority one is
missing, unreadable, legally unsafe, or visually unsuitable, record that reason
in the review note. Formal bibliographic fields such as journal, year, volume,
issue, pages, DOI, and publication status still come from Zotero metadata and
the official published record, not from a preprint or other lower-priority PDF.

Every review note must also contain a public-safe `关键事实证据定位记录`
section. Do not annotate every sentence, but record enough anchors for fast
human review:

- abstract source and location,
- core claims or conclusions and their PDF file page, section, table, or
  paragraph location,
- key figures with PDF file page and original figure number,
- key formulas with PDF file page and equation number when they are original
  paper formulas; if a formula is an editorial explanatory formula added for
  the WeChat article, record it as such and point to the paper evidence it
  explains.

If exact PDF file pages have not been audited yet, mark the page as
`pending PDF page audit` instead of guessing. These evidence-location records
must stay public-safe: do not include absolute private paths or raw copied PDF
content.
Use PDF file page numbers for evidence locations, written as `PDF file page N`.
Do not use journal printed page numbers or article pagination for this purpose,
because local rendering, screenshots, and figure extraction all follow the PDF
file page order.

## Article Unit

Use one selected paper per article.

Do not turn a paper article into a multi-paper survey. Related papers can
appear only as compact platform-specific navigation: published WeChat article
links in the WeChat body, and internal paper-note links on RTD.

## Public Safety

This repository is public. Anything committed here must be safe to expose.

Never include:

- WeChat AppSecret, access token, refresh token, cookies, preview credentials, or API keys.
- raw WeChat API responses, private preview URLs, or remote preview material.
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
3. Verify `publication_ref`, title, year, DOI, and the WOEAI website record.
4. Create or update the reader-facing article under `wechat/articles/draft-public-safe/`.
5. Name the article with the paper's `publication_ref`, for example `wechat/articles/draft-public-safe/ref-zhao2026-BS.md`.
6. Treat that reader-facing Markdown file as the public content master. Align
   all public text, formulas, figure captions, and extended-reading body links
   there first.
7. Convert the same public article content to a Sphinx-compatible RST page for
   RTD. Do not add a separate Markdown route to Sphinx.
8. Create or update the publishing note under `wechat/articles/review/`, for example `wechat/articles/review/ref-zhao2026-BS.review.md`.
9. Start the reader-facing article from `wechat/templates/paper-explainer.md`, but remove any production-only placeholders before treating it as copy-ready.
10. Keep review details, evidence notes, copyright status, formula preview status, figure insertion status, RST conversion notes, and human checklists in the `.review.md` file, not in the reader-facing article or RTD page.
11. Keep `wechat_status` aligned with the backlog state model:
   - `selected`
   - `drafting`
   - `reviewing`
   - `ready_to_publish`
   - `published`
   - `archived`
12. When official WeChat API submission is configured, record only non-sensitive
    draft-box metadata in the backlog, such as `wechat_draft_media_id`,
    `wechat_draft_created_at`, `wechat_draft_updated_at`, and
    `latest_published_url`. Do not record credentials, cookies, private preview
    URLs, or raw API responses.
    After a live draft creation/update succeeds, write back
    `wechat_status: ready_to_publish`, `wechat_draft_media_id`,
    `wechat_draft_created_at`, and `wechat_draft_updated_at`. Do not advance
    backlog state after a failed live call or a no-submit check.
    If `wechat_draft_media_id` is absent, create a new WeChat draft. If it is
    present, update that existing draft by default. Create a separate new draft
    only when the user explicitly asks for a new copy.
    Use the paper's first author as the default WeChat draft author field for
    journal-paper articles. Keep the complete paper author list in the public
    `论文信息` section rather than putting it into the WeChat metadata author
    field.
13. Treat the official WeChat draft API as the primary automated submission
    path. Use doocs/md only for theme design, formula/style preview, and manual
    copy-paste fallback when the official API path is unavailable or a human
    editor specifically wants that route. Treat Wechatsync and other
    browser-plugin routes as optional one-off distribution aids, not as the
    default WOEAI pipeline.
14. Read `~/.config/woeai/wechat_official_account.env` only when the user
    explicitly asks to test the WeChat API path or confirms live creation/update
    of a WeChat draft.
    Cache fetched `access_token` data only in
    `~/.cache/woeai/wechat_access_token.json`. Never print, log, commit, or copy
    credential or token values into repository files, review notes, dry-run
    output, or final responses.
    `wechat_draft.py ip-check` is only an optional diagnostic command for
    manually viewing the current public egress IP. Do not use it as a hard
    live-run gate: the local IP-detection route can disagree with the actual
    WeChat API path, so create/update commands should call the official API
    directly and treat the WeChat API response as the source of truth. If
    WeChat returns an IP-allowlist error, ask the user to add the IP reported by
    WeChat or move the workflow to a fixed-egress remote runner.
15. Default to no-submit checks for API tools. Before any live command that
    creates or updates a WeChat draft, explain that the command will read
    private WeChat credentials, upload approved images, and create/update a
    draft in the WeChat backend. Wait for explicit confirmation such as
    `确认创建公众号草稿`; vague approval such as `继续`, `可以`, or `试试` is
    not enough.
    `wechat_draft.py dry-run`, `preflight`, `create-draft`, and `update-draft`
    must run `scripts/check-public-safe-content.py` against the target article
    and review note before any credential read, image upload, or WeChat API
    draft call.
16. Dry-run output must list the approved cover image and each approved body
    image that would be uploaded. Live runs must upload approved body images and
    replace local Markdown image paths with WeChat image URLs in the submitted
    HTML before draft creation/update.
17. Do not call WeChat publish, mass-send, or browser-driven release actions.
    The human editor must preview, proofread, and publish manually in the
    WeChat backend.
18. Use `https://woeai.readthedocs.io/zh-cn/latest/` as the preferred Read the
    Docs project domain for RTD companion pages and WeChat API draft payloads.
    Do not hard-code `winddee.cn` into WeChat article sources when an
    equivalent Read the Docs project-domain URL exists. This does not by itself
    change the public website's own canonical SEO URL or contact-page display.
19. By default, set the WeChat API `content_source_url`, which controls the
    backend bottom `阅读原文` entry, to the current paper's RTD companion page:
    `https://woeai.readthedocs.io/zh-cn/latest/paper-notes/<publication_ref>.html`.
    Do not add a separate body `阅读原文` section. When the user explicitly
    chooses a different public original-link destination for a specific article,
    record it as `wechat_content_source_url` in that article's review front
    matter and use it as the WeChat API `content_source_url`; do not duplicate
    the raw URL in the body text. An explicitly blank `wechat_content_source_url`
    means the editor wants no bottom `阅读原文` link for that article.
20. Update `wechat/backlog/selected-papers.yml` only when the user's task asks for workflow tracking or after a draft/review/API step changes status.

When a WeChat backend preview leads to public wording changes, apply those
changes back to the Markdown content master first, then regenerate/update the
RST companion page and the WeChat draft from that same Markdown. Do not keep
parallel public正文 edits only in the WeChat draft or only in the RST page.

## Output Model

Generate three public-safe files or records for each paper article:

- `wechat/articles/draft-public-safe/<publication_ref>.md`: reader-facing WeChat Markdown. It should be clean enough to copy into a WeChat Markdown editor or the WeChat backend.
- `docs/source/paper-notes/<publication_ref>.rst`: RTD Paper Companion Page. It should present the same public body text, images, and DOI as the WeChat Markdown article, with markup/rendering differences plus the documented channel adaptations (prefix-stripped title, no WeChat closing block, RTD-only `完整引用` citation section). RTD related-paper navigation is generated separately with internal paper-note links.
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
- Preserve the same section order, body text, images, and DOI link.
- Change only what Sphinx rendering requires plus the channel adaptations
  listed below: heading underline syntax, image directives, internal links,
  external links, code/formula representation, relative asset paths, and
  RTD-only internal related-paper navigation.
- RTD title: strip the WeChat title-category prefix (`数值风洞 |`, `结构抗风 |`,
  `漂浮风电 |`) from the page title and related-navigation link labels. The
  category packaging is a WeChat surface concern; RTD pages get their
  categorization from direction pages and the site navigation.
- Closing block: skip the paragraph containing the fixed WeChat closing
  sentence (anchored on `点击阅读原文`); RTD pages carry no closing block.
- Citation section: after the body and before `相关论文解读`, the converter
  appends a `完整引用` section with the full bibliographic citation, extracted
  from the `docs/source/Publications.rst` paragraph under the
  `.. _<publication_ref>:` anchor and truncated at the DOI URL (impact factor
  and CAS partition stay on the Publications page), plus a `:ref:` link to
  that Publications entry. If the anchor is missing, the converter warns and
  omits the section; for a real paper article that warning must be resolved
  before the draft is called ready.
- Keep private review metadata out of the RST page.
- Use `wechat/tools/markdown_to_rtd.py` as the formal Markdown-to-RST
  converter for this pipeline. Example:

  ```bash
  python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BS
  python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BS --check
  ```

- Put article-wide RTD metadata in the review note, not in the public Markdown
  body. The RTD top cover is read from `rtd_cover_image`, `wechat_cover_image`,
  `cover_image`, or the review note's `封面素材` line, then inserted below the
  RST title.
- Register RTD pages through the relevant research-direction Academic Progress section, grouped by second-level research subdirection.
- On `docs/source/Research.rst`, use the public label `学术进展 Academic Progress` instead of `近期证据 Selected Proof Points` when listing these companion pages.
- Within each second-level subdirection, list RTD Paper Companion Pages by publication date descending until a more specific sorting rule is chosen.
- If the RST page or research-direction navigation changes, this is a Sphinx site-build input and `./scripts/check-docs.sh` becomes required.

## Article Structure

Use this default order unless the paper strongly requires a small adjustment:

1. `论文信息`
2. `三句话导读`
3. `关键数字 / 关键结论卡`
4. `摘要`
5. `研究问题`
6. `方法贡献`
7. `关键发现`
8. `工程意义`
9. `适用边界`
10. `图文说明` when public-safe images are inserted
11. `延伸阅读` or platform-generated related-paper navigation when useful

Put reader-facing links under `延伸阅读`. Use direct Markdown hyperlinks, not a
label followed by a naked URL. Keep DOI visible in `论文信息`, and do not repeat
it in `延伸阅读` unless it is the only useful external reading path. Do not
include a WOEAI publication-page anchor in the reader-facing article when that
public page merely duplicates the article or paper record.

For new articles, add `三句话导读` near the top. The three sentences should say
what the paper studies, why it matters, and what the reader can take away. They
are entry guidance, not a compressed duplicate of `摘要` or `关键发现`.

For new articles, add `关键数字 / 关键结论卡`. Use high-value numbers only when
they carry real explanatory value and can be traced to paper evidence in the
review note. If the paper has no high-value numbers, use `关键结论卡` with 2-3
non-overlapping conclusions instead of forcing low-value numeric detail.

Use this title pattern:

`<title category> | <problem-solving Chinese title>`

Temporarily choose the title category from `数值风洞`, `结构抗风`, or `漂浮风电`.
The title after the separator should describe what problem the paper helps
solve.

Keep this title as the Markdown H1 in the WeChat Article Source. In the
Official WeChat Draft API Path and manual WeChat-editor copy path, use that H1
only as the WeChat title field and do not render it again inside the submitted
article body. The WeChat backend already displays the title, account, author,
and timestamp above the body, so rendering another H1 creates a duplicate
title.

The current official API renderer themes are:

- `academic-clean`: default scholarly paper-explainer style.
- `engineering-note`: applied technical style for engineering readers.
- `recruitment-friendly`: warmer direction-introduction style for recruitment
  readers.

Themes change presentation only. They must not change facts, section order,
citations, formula semantics, image approval status, or public-safety
boundaries.

Add `摘要` immediately after `论文信息`. For English papers, translate the
original English abstract faithfully into Chinese. Do not include the original
English abstract in the reader-facing article, the WeChat draft, or the RTD
page; readers are Chinese-first. The Chinese translation may be split into 2-3
paragraphs by meaning for mobile readability; splitting changes layout only,
not the faithful-translation requirement. Do not invent an abstract when the
original paper abstract is unavailable; keep that issue in the review note
until a paper PDF, author manuscript, or approved source is available.
`scripts/check-public-safe-content.py` must fail any reader-facing draft that
still contains `**英文摘要**`.

In `论文信息`, keep the article metadata compact:

- `论文题名`
- `作者`
- `期刊`
- `年份`
- `DOI`
- `WOEAI 相关方向`

Do not add a separate `卷期页码` line to WeChat paper articles. Volume, issue,
page, and article-number details belong to the full RTD publication citation,
not to the WeChat article metadata block.

Write the `作者` line with the same author-marker semantics as
`docs/source/Publications.rst`:

- wrap only a Student First Author name in `<u>...</u>` in the Markdown source;
  the RTD converter maps this to `:student-first-author:` and the WeChat HTML
  renderer displays it as underlined text.
- mark corresponding authors with `\*` immediately after the displayed name,
  for example `**Li Chao**\*`.
- do not write `(corresponding author)` in the reader-facing article.

Write for technically literate readers who may include prospective students, collaborators, engineering software users, and academic peers.

Tone:

- Write from the author's perspective and voice. The article should read like WOEAI or the authors are explaining their own paper to readers.
- Use `我们` as the default subject for research actions, method choices,
  comparisons, interpretation, and recommendations. Prefer wording such as
  `我们提出...`, `我们构建...`, `我们比较了...`, `我们发现...`, and `我们建议...`.
- Do not let detached third-person subjects replace the authorial voice when
  the sentence describes research work or judgment. Avoid patterns such as
  `它说明...`, `该研究发现...`, `本文认为...`, and `从公开摘要可确认...`; recast
  them as first-person explanations unless doing so would distort the source.
- Use `论文`, `模型`, `方法`, or `结果` as the subject only for static facts,
  definitions, reported values, or citation precision. When citing specific
  numeric results, `论文中给出的结果` is acceptable.
- Keep abstract translation faithful. Do not force `我们` into the translated
  abstract if the original abstract would be distorted; strengthen first-person
  narration mainly in `三句话导读`, `研究问题`, `方法贡献`, `关键发现`, `工程意义`,
  and `适用边界`.
- Scholarly first.
- Engineering relevance second.
- No hype.
- No unsupported partner names or project claims.
- Keep limitations visible.
- Avoid standing outside the paper as a detached reviewer unless explicitly writing a review note.

Opening and skim path:

- Vary the opening strategy across articles. Choose from: real-world
  contradiction, counter-intuition (challenge a common assumption), concrete
  number lead, or scenario lead. Adjacent articles in the same batch should not
  reuse the same strategy.
- When the paper provides citable numbers, put a quantified hook in the first
  one or two paragraphs (for example a maximum error reduction, a speedup, or
  a deviation percentage). Never invent numbers; if no suitable number exists,
  record a `待确认可公开的量化数字` item in the review note instead.
- In each `关键发现` subsection, bold exactly one conclusion sentence so a
  skimming reader can follow the bolded sentences alone. Keep other bold usage
  restrained.
- Write `研究问题` as a numbered list of questions. Open each `关键发现`
  subsection with a sentence that answers back to a numbered question, for
  example `针对问题 1，...`.

## Formula Handling

Do not render formulas as raster images by default.

Use Markdown LaTeX as the canonical formula source in WeChat article drafts:
`$...$` for inline formulas and `$$...$$` for display formulas. For the official
WeChat API path, use MathJax SVG pre-rendering as the default formula route:
convert the LaTeX before submission into
`<mjx-container jax="SVG">...<svg>...</svg></mjx-container>` HTML, then verify
the resulting formula display in the final WeChat backend mobile preview. In
this route WeChat does not need to run MathJax or load external scripts.
Preserve the source LaTeX in the SVG formula container when possible, using
`data-formula` plus `data-formula-type="inline-equation"` or
`data-formula-type="block-equation"`.

This default is based on the 2026-06-10 WeChat draft API stress tests: SVG
formulas with both inline and display cases were accepted in a single article
draft and the user confirmed the preview effect was satisfactory.

The lightweight HTML formula path in `wechat/tools/render-copy-ready.py` is
only a fallback for troubleshooting or machines without the MathJax SVG
runtime. It is not a full LaTeX engine and should not be described as
LaTeX-quality rendering. PNG formula images are also fallback-only unless final
preview proves SVG is not preserved.

Convert the same LaTeX formula semantics to Sphinx math markup in RTD companion pages: `:math:` roles for inline formulas and `.. math::` directives for display formulas.
RTD display formulas should also be visually centered through the site CSS, so
the same standalone-formula alignment expectation applies to both WeChat and
RTD HTML.

Use formula markup for inline mathematical variables, symbolic parameters, metrics, dimensional quantities, and unit-bearing values inside explanatory prose. Examples:

- WeChat draft: `$X_L$`, `$R$`, `$4H_{\mathrm{max}}$`, `$1\,\mathrm{km} \times 1\,\mathrm{km}$`, `$11\,\mathrm{m/s}$`, `$90^\circ$`.
- RTD companion page: `:math:` roles with the same LaTeX body, for example `X_L`, `4H_{\mathrm{max}}`, and `11\,\mathrm{m/s}`.

For word-like or abbreviation subscripts in WeChat drafts, prefer explicit
roman text, such as `$H_{\mathrm{max}}$`, `$K_{\mathrm{CFD}}$`, and
`$K_{\mathrm{m}}$`. Do not rely on shorthand commands such as `\max` in the
WeChat HTML renderer.

Do not use Markdown backticks or RST double backticks for mathematical variables or scientific quantities. Reserve code spans for paths, filenames, commands, literal field names, and code identifiers.

Keep formulas short enough for mobile display when possible.

For formula-heavy articles, do not split formulas into artificial
formula-only sections just to reduce rendering risk. Keep formulas in the
normal narrative flow: inline SVG for variables and short symbolic quantities
inside Chinese prose, display SVG for longer derivations or definitions, and
nearby plain-language explanations for important formulas.

Display SVG formulas should be visually centered in their standalone formula
block, with horizontal overflow allowed for unusually wide equations and the
original LaTeX source preserved in `data-formula` metadata.

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

For WeChat cover images, do not use a paper figure by default. The cover should
be a purpose-designed or generated public-safe image sized for the WeChat cover
surface, normally `900 x 383 px` for the first article cover. Keep the core
visual in the center for crop safety, avoid generated text unless explicitly
approved, and record the cover source, prompt, dimensions, and preview status in
the review note.

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

- figure identifier from the paper, written as `论文图 N` at the start of the
  caption-title line (for example `论文图 21 气象自动站的位置与观测环境`), so
  readers understand the numbering comes from the paper and is not a missing
  in-article sequence; keep the Markdown image alt text identical to the
  caption-title line,
- Chinese figure title on its own caption-title line, faithfully translated
  from the original paper figure title,
- separate Chinese explanatory text on the following caption-body line; write
  only what the reader needs while looking at the figure (reading order, what
  colors or line styles mean, which region to focus on) and do not restate the
  article's main argument,
- source or generation method,
- copyright/reuse note,
- mobile clarity preview result,
- `figure_preview_checked: false` until final WeChat backend preview.

In rendered WeChat HTML, the Chinese figure-title line should be centered, one
font size smaller than body text, and italic. The explanatory line should remain
separate and visually distinct from normal body text.

In RTD HTML, the Markdown-to-RST converter should emit body figures with the
`paper-note-figure` class. The first indented caption paragraph is the centered,
smaller, italic Chinese figure-title line; the following legend paragraph is
the separate Chinese explanatory line. Keep the two lines in the Markdown
content master so both WeChat and RTD receive the same wording.

For a normal paper article, include several figure positions when the original paper has suitable figures. Choose figures that help readers understand:

- the method or workflow,
- the study object or geometry,
- the validation evidence,
- the final engineering or platform application.

Do not leave the article imageless unless the paper truly has no suitable figure or the user requests text-only output.

Do not commit unapproved source images for papers outside the user's authored-paper scope. Keep private or unapproved image work under ignored local paths such as `wechat/.local/`.

If image rights or final high-resolution assets are not ready for a non-authored or unclear paper, put figure recommendations in the review note. Do not put visible `待上传原文图` placeholders into the reader-facing article.

## Closing Block And Extended Reading Links

Immediately before `延伸阅读`, every paper article ends its body with this
fixed closing sentence as its own paragraph:

`如果你对建筑结构抗风 / 海上漂浮风电方向的研究生学习或工程合作感兴趣，点击阅读原文查看本文网页版，并从 WOEAI 主页了解更多。`

This sentence is WeChat-channel-specific: the bottom `阅读原文` entry it refers
to is provided by the WeChat API `content_source_url`, which defaults to the
current paper's RTD companion page. `markdown_to_rtd.py` recognizes the
`点击阅读原文` anchor and skips the paragraph, so the RTD page carries no
closing block.

Add only a `延伸阅读` section near the end of the article when there are useful
reader-facing links. For related paper navigation in the WeChat body, include
only already-published WeChat article links from `latest_published_url`. Omit
related papers that do not yet have public WeChat URLs.

RTD related-paper navigation is generated separately as internal paper-note
links and should point only to existing `docs/source/paper-notes/*.rst` pages.

Do not add a separate `阅读原文` section. Keep the DOI visible in `论文信息`.
Do not include a WOEAI publication-page anchor in the reader-facing article
when that public page merely duplicates the article or paper record. Do not
imply that the repository hosts the full paper PDF unless a public author
manuscript or approved download link is actually available.

## Draft Quality Gates

Before calling a draft ready:

- DOI and the WOEAI website record are checked.
- The `论文信息` author line uses RTD-compatible markers: Student First Authors
  only are underlined, corresponding authors use a visible `*`, and
  `(corresponding author)` is not used.
- The WeChat draft author field is the paper's first author for journal-paper
  articles.
- The `论文信息` block does not contain a separate `卷期页码` line.
- Zotero Desktop Local API metadata, DOI, `abstractNote`, and attachment
  records are checked.
- For English papers, the public `摘要` text is a faithful Chinese translation
  of the original abstract from Zotero `abstractNote`, the PDF abstract, an
  author manuscript, or another approved source; the article contains no
  `**英文摘要**` block.
- The article uses a first-person authorial voice in explanatory sections:
  `我们` is the normal subject for research actions and judgments, and detached
  wording such as `它说明`, `该研究发现`, `本文认为`, or `从公开摘要可确认` has been
  recast unless needed for citation precision or faithful abstract translation.
- `研究问题` is a numbered question list, and each `关键发现` subsection opens
  by answering back to a numbered question.
- Each `关键发现` subsection bolds exactly one conclusion sentence.
- Figure caption-title lines use the `论文图 N` original-number format and the
  explanatory line does not restate the article's main argument.
- The fixed closing sentence appears as its own paragraph immediately before
  `延伸阅读`.
- Local PDF attachment is used when present. If it is missing, Zotero Web API
  `/file` is tried when credentials are available; if that also fails, the
  review note records `需要同步 PDF 或提供作者稿`.
- No general web-page PDF scraping is used. If a web PDF is used, the review
  note records the explicit user approval, public/legal source,
  private-storage class or ignored relative path, and public-safe reuse status.
- The review note includes a public-safe `源文件获取记录` section covering
  Zotero key, metadata source, attachment status, local PDF status, PDF source
  type, Zotero Web API `/file` status, web-download status, abstract source,
  body source, and figure source.
- If multiple PDF-like attachments exist, the review note records which
  attachment class was selected, follows the standard priority order, and
  explains any lower-priority selection.
- The review note includes a public-safe `关键事实证据定位记录` section for
  abstract source, core claims, key figures, and key formulas. Missing page
  audits are marked pending rather than guessed.
- `scripts/check-public-safe-content.py` fails any
  `wechat/articles/review/*.review.md` file that omits `## 源文件获取记录` or
  `## 关键事实证据定位记录`.
- Research family and subdirection match `wechat/topics/`.
- No invented collaboration, partner, project, facility, award, or metric claims appear.
- The reader-facing article has no YAML front matter, pending fields, figure plans, private notes, or human checklist.
- Important formulas are not images and have explanations.
- For author-confirmed papers, suitable PDF figures are extracted into `wechat/assets/public-safe/<publication_ref>/` and inserted into the article. For non-authored or unclear papers, suitable figure recommendations are recorded in the review note until rights are confirmed.
- The article uses `延伸阅读` for useful reader-facing links, direct Markdown
  hyperlinks instead of naked URLs, and no separate `阅读原文` section.
- New articles include `三句话导读` and `关键数字 / 关键结论卡`; these entry
  modules do not repeat the abstract or key-findings wording, and key numbers
  have review-note evidence when used.
- WeChat related-paper navigation contains only already-published WeChat
  article links; unpublished related papers are omitted.
- RTD related-paper navigation uses internal paper-note links only.
- The WeChat API `content_source_url` defaults to the current paper's RTD
  companion page unless the review note explicitly overrides it or explicitly
  leaves it blank.
- Rendered WeChat HTML shows Chinese link text only and does not expose raw
  English URLs after the link text.
- DOI remains visible in `论文信息` for scholarly traceability.
- The separate review note records source evidence, image/copyright status, formula preview status, and remaining human-review items.
- The RTD Paper Companion Page matches the WeChat Markdown article in body
  text, images, and DOI link, with the documented channel adaptations:
  prefix-stripped title, no closing block, the `完整引用` section (citation
  truncated at the DOI plus a Publications anchor link), and platform-specific
  related-paper navigation generated for RTD.
- `python3 wechat/tools/markdown_to_rtd.py --publication-ref <publication_ref> --check`
  passes after generating the RTD companion page.
- The relevant research-direction page exposes the RTD page under `学术进展 Academic Progress`, grouped by second-level research subdirection and sorted by publication date descending.
- `wechat/templates/review-checklist.md` is satisfied or remaining items are explicitly marked in the review note.
- `scripts/check-public-safe-content.py` passes, including the required review
  note section check.
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
