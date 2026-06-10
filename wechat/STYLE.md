# WOEAI WeChat Style Guide

## Article Unit

Use one selected paper per article.

Do not turn every article into a multi-paper theme essay. Related papers may appear in the `延伸阅读` section.

Use the reader-facing Markdown file under `wechat/articles/draft-public-safe/`
as the public content master. Public wording, formulas, figure captions, and
body links should be aligned there before generating the RTD RST companion page
and before updating the WeChat draft. If a WeChat backend preview causes a
public正文 edit, apply it back to the Markdown master first, then regenerate the
RST and WeChat outputs.

Generate RTD companion pages with the formal converter:

```bash
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BS
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BS --check
```

The public Markdown owns body wording. The review note owns platform metadata
such as the RTD top cover image and WeChat bottom `content_source_url`.

## Default Structure

1. `论文信息`
2. `摘要`
3. `研究问题`
4. `方法贡献`
5. `关键发现`
6. `工程意义`
7. `适用边界`
8. `图文说明` when a separate figure summary is useful
9. `延伸阅读`

## Title Format

Use this title pattern:

`<title category> | <problem-solving Chinese title>`

The title category is temporarily selected from:

- `数值风洞`
- `结构抗风`
- `漂浮风电`

The second half should say what problem the paper helps solve, not only restate
the paper topic.

Keep the Markdown H1 in the article source. For WeChat draft submission and
manual WeChat editor copy, use it only as the Official Account title field; do
not render the H1 again inside the article body, because WeChat already displays
the title, account, author, and timestamp above the body.

## Abstract Handling

- Add an `摘要` section immediately after `论文信息`.
- For Chinese papers, use the Chinese abstract.
- For English papers, provide a faithful Chinese translation of the original
  abstract, then add `**英文摘要**` followed by the original English abstract
  from Zotero `abstractNote`, the paper PDF, an author manuscript, or another
  approved source.
- Do not replace the English abstract with an English paraphrase.
- Do not invent an abstract from the article body. If the original abstract is
  unavailable, keep the article in drafting/review notes until the paper PDF,
  author manuscript, or another approved source is available.

## Paper Metadata

In `论文信息`, use only:

- `论文题名`
- `作者`
- `期刊`
- `年份`
- `DOI`
- `WOEAI 相关方向`

Do not add `卷期页码` as a separate line in WeChat paper articles.

Write the `作者` line with the same author-marker semantics as
`docs/source/Publications.rst`:

- Student First Authors only use an underline marker. In the Markdown source,
  write this as `<u>Student Name</u>` so RTD can convert it to
  `:student-first-author:`.
- Corresponding authors use `\*` immediately after the displayed name, such as
  `**Li Chao**\*`; rendered WeChat HTML must show a normal `*`, not `\*`.
- Do not write `(corresponding author)` in the reader-facing article.

For journal-paper articles, the Official WeChat draft author field should be
the paper's first author. Keep the full paper author list in `论文信息`.

## Source Acquisition

Use this Zotero-first order before drafting:

1. Read metadata, DOI, and `abstractNote` from the Zotero Desktop Local API.
2. Read attachment records from the Zotero Desktop Local API.
3. If a local PDF attachment exists, extract or verify the abstract, figures,
   captions, and body evidence from that PDF.
4. If the local PDF is missing, try the Zotero Web API `/file` endpoint for the
   attachment. Keep API keys and downloaded private working files outside the
   public repository.
5. If Web API file access also fails, record `需要同步 PDF 或提供作者稿` in the
   review note and do not invent PDF-derived facts.

Do not automatically scrape or download PDFs from publisher pages, DOI landing
pages, Google Scholar, ResearchGate, Sci-Hub, search results, or other general
web pages. Use web pages only for public metadata checks unless the user
explicitly approves a specific public and legal PDF source, such as an OA PDF,
an author manuscript, or a user-provided download link. Store approved web
downloads only under ignored private working paths such as
`wechat/.local/<publication_ref>/`, and record the source, approval, and reuse
status in the review note.

Every article review note must include a public-safe `源文件获取记录` section.
Record the Zotero key, metadata source, attachment-record status, local PDF
status, PDF source type, private-storage class, Zotero Web API `/file` status,
web-download status, abstract source, body-evidence source, and figure source.
Do not record absolute private file paths, credentials, cookies, raw API
payloads, or downloaded PDF contents in committed files.

When a Zotero item has multiple PDF-like attachments, choose the PDF evidence
source in this order: author final manuscript / author manuscript, publisher
version of record PDF, open-access platform PDF, preprint, then other
attachments. Record the selected attachment class in the review note. If a
lower-priority source is used, explain why the higher-priority source was
missing, unreadable, legally unsafe, or visually unsuitable. Bibliographic
fields such as journal, year, volume, issue, pages, DOI, and publication status
still come from Zotero metadata and the official published record.

Every review note must include a public-safe `关键事实证据定位记录` section.
Do not mark every sentence, but record evidence anchors for the abstract, core
claims or conclusions, key figures, and key formulas. Use PDF file page,
section, table, original figure number, or original equation number when
available. If a formula is added as an editorial explanation in the WeChat
article rather than copied from a numbered paper equation, record that
distinction and point to the paper evidence it explains. If exact pages have
not been audited, mark them as `pending PDF page audit` rather than guessing.
Evidence locations use PDF file page numbers, written as `PDF file page N`,
not journal printed page numbers or article pagination.

The public-safety script must fail a review note that omits either
`## 源文件获取记录` or `## 关键事实证据定位记录`.

## Tone

- Scholarly first.
- Engineering relevance second.
- No hype.
- No unsupported partner names or project claims.
- Use DOI in `论文信息` for scholarly traceability.
- Do not include a WOEAI publication anchor in reader-facing WeChat articles
  when the linked RTD publication item or paper companion page duplicates the
  article content.

## Link Domain

- For WOEAI website links embedded in WeChat articles and WeChat draft API
  payloads, prefer the Read the Docs project domain:
  `https://woeai.readthedocs.io/zh-cn/latest/`.
- Use that domain for RTD companion pages, direction pages, and homepage-style
  links when those links are useful to the reader.
- Put reader-facing links under `延伸阅读`. Use direct Markdown hyperlinks such
  as `[WOEAI | 建筑结构抗风方向介绍](...)`, not a label followed by a naked URL.
- Rendered WeChat HTML must show only the Chinese link text. It must not expose
  the raw English URL after the link text.
- The WeChat backend bottom `阅读原文` entry is controlled by the API
  `content_source_url` field, not by body Markdown. Leave it empty by default,
  but set it to a useful WOEAI Read the Docs page when the editor explicitly
  chooses a target for a specific article.
- Keep DOI links visible in `论文信息`; do not duplicate DOI in `延伸阅读`
  unless it is the only useful external reading path.
- This WeChat-link rule does not automatically change the public website's own
  canonical SEO URL or homepage contact display.

## Formula Handling

- Use Markdown LaTeX as the canonical formula source in WeChat article drafts: `$...$` for inline formulas and `$$...$$` for display formulas.
- Render WeChat formulas through the selected WeChat Markdown or API workflow
  and verify the resulting formula display in the final WeChat backend mobile
  preview.
- Use MathJax SVG pre-rendering as the default formula route for the official
  API path. In this route, Markdown LaTeX is converted before submission into
  `<mjx-container jax="SVG">...<svg>...</svg></mjx-container>` HTML, so WeChat
  does not need to run MathJax or load external scripts. A 2026-06-10 single
  article stress test with multiple inline and display SVG formulas was accepted
  by the official draft API and approved by user preview.
- Preserve the source LaTeX in SVG formula containers when possible, using
  `data-formula` plus `data-formula-type="inline-equation"` or
  `data-formula-type="block-equation"`. This makes the submitted HTML easier to
  audit and closer to formula-heavy published WeChat examples.
- The lightweight HTML formula path in `wechat/tools/render-copy-ready.py` is
  only a fallback for troubleshooting or machines without the MathJax SVG
  runtime. It is not a full LaTeX rendering engine.
- RTD companion pages should convert the same LaTeX formula semantics to Sphinx math markup: ``:math:`...` `` for inline formulas and `.. math::` for display formulas.
- RTD display formulas should also be visually centered through the site CSS,
  so standalone formula alignment is consistent between RTD and WeChat.
- Use formula markup for inline mathematical variables, symbolic parameters, metrics, dimensional quantities, and unit-bearing values in prose. Examples: `$X_L$`, `$R$`, `$4H_{\mathrm{max}}$`, `$1\,\mathrm{km} \times 1\,\mathrm{km}$`, `$11\,\mathrm{m/s}$`, and `$90^\circ$`.
- For word-like or abbreviation subscripts in WeChat drafts, prefer explicit
  roman text, such as `$H_{\mathrm{max}}$`, `$K_{\mathrm{CFD}}$`, and
  `$K_{\mathrm{m}}$`. Avoid relying on commands such as `\max` in the WeChat
  HTML renderer.
- Do not use Markdown backticks or RST double backticks for mathematical variables or scientific quantities. Reserve code spans for paths, filenames, commands, literal field names, and code identifiers.
- Do not render formulas as raster images by default. PNG formula images are
  stable but can blur after upload, compression, or mobile scaling; use them
  only as a fallback when the final WeChat preview cannot preserve a readable
  SVG formula.
- For formula-heavy articles, keep formulas in the normal article flow rather
  than splitting them into artificial formula-only sections. Use inline SVG for
  variables inside Chinese prose, and display SVG for longer formulas. If a
  display formula is very wide, rely on horizontal overflow rather than shrinking
  the whole article text.
- Display SVG formulas should be visually centered in their standalone formula
  block, with the original LaTeX source kept in `data-formula` metadata.
- Do not create a fixed `公式说明` section by default. Put formulas in the section where they are needed, usually `方法贡献`, `关键发现`, `工程意义`, or `适用边界`.
- Keep formulas short and readable on mobile. If a formula is long, split the explanation into nearby text rather than forcing a dense display block.
- After each important formula, add a plain-language sentence explaining what the formula means and why it matters for the paper.

## Cover Image

- Do not use a paper figure as the WeChat cover image by default. Paper figures
  are often too tall, too detailed, or visually weak after WeChat cover cropping.
- Prefer a purpose-designed or generated cover image based on the article's
  core idea, target readers, and title category.
- Generate cover candidates through image generation with the user-confirmed
  cover text embedded directly in the image. Do not use no-text covers or add
  Chinese text after generation with any overlay method.
- Generate at least three image-gen-text candidates per round. If all
  candidates have wrong, missing, rewritten, distorted, low-contrast, or
  unreadable Chinese text, retry once with the same confirmed text. If two
  rounds fail, stop and ask the editor to confirm shorter or clearer cover text.
- Use a first-article cover target of `900 x 383 px`, about `2.35:1`. Larger
  source images may use the same ratio and be resized down for upload.
- Keep the main visual concept in the center so the image still works if a
  WeChat surface crops it toward a square thumbnail.
- Check small-thumbnail readability, not only full-size dimensions and crop
  ratio.
- Keep cover text to the confirmed `分类标签 | 主钩子 / 可选副标题`
  structure. Let the WeChat article title carry the full title; do not repeat
  the full article title on the cover.
- Store final public-safe cover images under
  `wechat/assets/public-safe/<publication_ref>/` and record the source or prompt
  in the article review note. Also record candidate count, selected text mode,
  selected candidate, rejected candidate reasons, and local candidate-preview
  path when a cover is generated through the upgraded workflow.
- Mark cover approval as pending until the cover is checked in the WeChat
  backend preview.

## Figure Handling

- WOEAI WeChat paper articles are generated for the user's own authored papers unless the user explicitly says otherwise.
- For author-confirmed papers, extract suitable original figures directly from the paper PDF or author manuscript and insert them into the reader-facing Markdown.
- Prefer `pdfimages -all` extraction from the PDF. If a figure is stored as ordered image strips, stitch those strips back into a complete figure before using page-render cropping.
- Store final public-safe article figures under `wechat/assets/public-safe/<publication_ref>/`.
- After each inserted figure, write a Chinese figure-title line translated
  faithfully from the paper's original figure title. Put the explanatory
  Chinese sentence in a separate following line.
- Rendered Chinese figure-title text should be centered, one font size smaller
  than body text, and italic. The explanatory line should remain separate and
  visually distinct from normal body text.
- RTD companion pages should preserve the same two-line figure-caption meaning.
  The converter emits `paper-note-figure` on body figures so site CSS can render
  the Chinese figure-title line centered, smaller, and italic, with the
  explanatory line separate below it.
- Redraw a figure only when the original figure is unavailable, legally unsafe to reuse, too low-resolution, or visually unsuitable for a WeChat article.
- Record figure source, extraction method, and copyright status in the separate `.review.md` file, not as internal notes inside the reader-facing article.
- Check every figure in the WeChat backend mobile preview, not only in a Markdown editor preview.

## Research Family Labels

- `建筑结构抗风`
- `海上漂浮风电`

## Subdirection Labels

建筑结构抗风:

- `数值风洞与湍动入流`
- `高层建筑抗风与优化`

海上漂浮风电:

- `浮式风机系统一体化分析与优化`
- `浮式混凝土平台结构设计`
- `数值风浪流水池`
