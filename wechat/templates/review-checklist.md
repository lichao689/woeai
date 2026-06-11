# WeChat Article Review Checklist

## Source

- [ ] Zotero Desktop Local API metadata, DOI, and `abstractNote` have been checked.
- [ ] Zotero Desktop Local API attachment records have been checked.
- [ ] The review note contains a public-safe `源文件获取记录` section.
- [ ] `scripts/check-public-safe-content.py` will fail if this section is
  missing from the review note.
- [ ] The source-acquisition record states the Zotero key, metadata source,
  attachment-record status, local PDF status, PDF source type, and whether
  Zotero Web API `/file` was attempted.
- [ ] If multiple PDF-like attachments exist, the review note records the
  selected attachment class using this priority: author manuscript, publisher
  version of record, OA platform PDF, preprint, then other.
- [ ] If a lower-priority PDF source was used, the review note explains why the
  higher-priority source was not used.
- [ ] Bibliographic fields are taken from Zotero metadata and the official
  published record, not overwritten by a lower-priority PDF such as a preprint.
- [ ] The review note contains a public-safe `关键事实证据定位记录` section.
- [ ] `scripts/check-public-safe-content.py` will fail if this section is
  missing from the review note.
- [ ] The evidence-location record covers the abstract, core claims or
  conclusions, key figures, and key formulas.
- [ ] Evidence page references use PDF file page numbers, written as
  `PDF file page N`, not journal printed page numbers or article pagination.
- [ ] Key figures include PDF file page and original figure number when
  available.
- [ ] Key formulas include PDF file page and equation number when they are
  original paper formulas; editorial explanatory formulas are clearly marked as
  such.
- [ ] Missing page audits are marked `pending PDF page audit` rather than
  guessed.
- [ ] The source-acquisition record states whether any web PDF download was
  used. If yes, it records explicit user approval and the public/legal source.
- [ ] The source-acquisition record does not expose absolute private file
  paths, API keys, cookies, raw downloaded PDF contents, or private credentials.
- [ ] Local PDF attachment exists and was used for PDF-derived abstract, figures, captions, and body evidence; or the review note records why it was unavailable.
- [ ] If local PDF was unavailable, Zotero Web API `/file` access was tried when credentials were available.
- [ ] If no PDF source was available, the review note records `需要同步 PDF 或提供作者稿` and the draft does not invent PDF-derived facts.
- [ ] DOI matches the WOEAI publication record.
- [ ] WOEAI publication record exists in `docs/source/Publications.rst`.
- [ ] Journal, year, authors, and metrics are copied from source-bounded data.
- [ ] The `论文信息` author line uses RTD-compatible markers: only Student First
  Authors are underlined, corresponding authors use a visible `*`, and
  `(corresponding author)` is not used.
- [ ] The Official WeChat draft author field is the paper's first author for a
  journal-paper article.
- [ ] The `论文信息` block omits a separate `卷期页码` line.
- [ ] For English papers, `**英文摘要**` matches the original abstract from
  Zotero `abstractNote`, the PDF abstract, an author manuscript, or another
  approved source, and is not an English paraphrase.
- [ ] Related direction page exists.
- [ ] The `三句话导读` states the paper's object/problem, importance, and reader
  takeaway without repeating the abstract or key-findings wording.
- [ ] The `关键数字 / 关键结论卡` uses high-value numbers with evidence when
  available; if there are no high-value numbers, it uses only key conclusions
  rather than forcing low-value numeric detail.

## Copyright

- [ ] The paper is authored by the user/WOEAI, or reuse rights/source status are otherwise confirmed.
- [ ] Original high-resolution paper figures are extracted from the PDF or author manuscript when they are legally safe and clear on mobile.
- [ ] Redrawn figures are used only when original figures are unavailable, legally unsafe, low-resolution, or unsuitable for WeChat display.
- [ ] Image source and extraction method are recorded in the separate `.review.md` file.

## Formulas And Figures

- [ ] WeChat draft formulas use Markdown LaTeX: `$...$` for inline formulas and `$$...$$` for display formulas.
- [ ] RTD companion formulas use Sphinx math markup: ``:math:`...` `` for inline formulas and `.. math::` for display formulas.
- [ ] Standalone display formulas are visually centered in both WeChat preview and RTD HTML.
- [ ] Inline mathematical variables, symbolic parameters, metrics, dimensional quantities, and unit-bearing values use formula markup rather than code spans.
- [ ] Word-like or abbreviation subscripts use explicit roman text in LaTeX, for example `$H_{\mathrm{max}}$` and `$K_{\mathrm{CFD}}$`.
- [ ] The selected WeChat formula renderer is `mathjax-svg` unless this review
  note explicitly records a fallback reason.
- [ ] The WeChat backend mobile preview preserves the
  `<mjx-container jax="SVG">` / inline SVG formula output clearly.
- [ ] SVG formula containers preserve source metadata such as `data-formula`
  and `data-formula-type` where practical.
- [ ] Formulas are not rendered as raster images unless final WeChat preview proves an image fallback is needed.
- [ ] Important formulas have plain-language explanations.
- [ ] Formula display has been checked in the final WeChat backend mobile preview.
- [ ] Each figure has a Chinese figure-title line translated from the original paper title, followed by a separate Chinese explanatory line.
- [ ] Rendered WeChat figure-title text is centered, one font size smaller than body text, and italic.
- [ ] RTD body figures preserve the same two-line caption meaning: centered
  smaller italic Chinese figure-title line, then separate explanatory line.
- [ ] Figure clarity has been checked in the final WeChat backend mobile preview.

## RTD Companion Page

- [ ] The reader-facing Markdown article is treated as the public content master before generating RTD and WeChat outputs.
- [ ] The RTD companion page is generated with `python3 wechat/tools/markdown_to_rtd.py --publication-ref <publication_ref>`, not by maintaining a separate Markdown route in Sphinx.
- [ ] `python3 wechat/tools/markdown_to_rtd.py --publication-ref <publication_ref> --check` passes.
- [ ] The RTD companion page preserves the same title, body text, images, DOI link, and useful related links as the WeChat article.
- [ ] The RTD related-paper navigation uses internal paper-note links only and
  points only to existing RTD companion pages.
- [ ] The approved cover image appears near the top of the RTD page below the
  title and is recorded in the review note.
- [ ] The RTD companion page is listed under `学术进展 Academic Progress` on the relevant research-direction page.
- [ ] The entry is grouped by second-level research subdirection and sorted by publication date descending until a more specific sorting rule exists.

## Public Safety

- [ ] No WeChat AppSecret, token, cookie, or credential appears.
- [ ] No Zotero API key appears.
- [ ] No private partner name appears.
- [ ] No unconfirmed project status appears.
- [ ] No private review comment appears.
- [ ] The draft is safe to expose in a public GitHub repository.
- [ ] WeChat body related-paper navigation contains only already-published
  WeChat article links; unpublished related articles are omitted.
- [ ] The WeChat API `content_source_url` is the current paper's RTD companion
  page unless the review note explicitly overrides it or explicitly leaves it
  blank.
