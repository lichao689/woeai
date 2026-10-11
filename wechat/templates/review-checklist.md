# WeChat Article Review Checklist

## Source

- [ ] Available authorized metadata, DOI and `abstractNote` have been checked; unavailable sources are recorded, and desktop access is not a cloud prerequisite.
- [ ] Available attachment records and current-workspace sources/manifests have been checked.
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
- [ ] For English papers, the `摘要` text is a faithful Chinese translation of
  the original abstract from Zotero `abstractNote`, the PDF abstract, an author
  manuscript, or another approved source; the article contains no `**英文摘要**`
  block.
- [ ] Related direction page exists.
- [ ] 已执行自然写作审校；可选导读或数字卡有独立用途，不与正文重复。

## Engineering Story And Series Consistency

- [ ] Opening identifies an engineering decision and constraint before jargon.
- [ ] Innovation explains the actual baseline, limitation and changed component.
- [ ] Mechanism, observed association and verification scope are distinguished.
- [ ] Numeric hooks retain metric, baseline and condition, not universal best cases.
- [ ] Demonstrated results and potential applications are explicitly separated.
- [ ] Application names inputs, useful decisions/outputs and missing transfer validation.
- [ ] Title, guide, cover and requested digest do not outrun source evidence.
- [ ] Important limitations also sit beside affected claims.
- [ ] Cover brief uses `WOEAI-cover-v2`, confirmed wording and evidenced scientific elements.
- [ ] Final dimensions are measured, not inferred from filenames or ratio.
- [ ] Fixed layout, type, palette and wide/square/mobile checks meet the contract.
- [ ] Guidance-only migration has not falsely accepted an old image or backend preview.

## Expression

- [ ] The opening strategy differs from adjacent articles (现实矛盾式 /
  反常识式 / 具体数字式 / 场景式).
- [ ] 数字放在有解释价值的位置；开头不强制数字钩子。
- [ ] 作者语气自然；不编造经历、情绪、动机，不强制每段“我们”。
- [ ] 无强制问题编号回扣或加粗数量；关键限定、归因、否定和确定程度保留。
- [ ] 结尾简短相关，无已发布公众号链接时完全省略延伸阅读。

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
  standard `span` / `section` containers and inline SVG formula output clearly.
- [ ] SVG formula containers preserve source metadata such as `data-formula`
  and `data-formula-type` where practical.
- [ ] Formulas are not rendered as raster images unless final WeChat preview proves an image fallback is needed.
- [ ] Important formulas have plain-language explanations.
- [ ] SVG 根组 currentColor 属性及内联 fill/stroke 保留，无强制黑白字或人为白底；分式横线与显式内部颜色保留。
- [ ] API 清洗外层 inherit/transparent 时记录清洗结果，并以实际手机预览验证效果，不单凭样式缺失判失败。
- [ ] 实际微信手机浅色模式公式预览通过（记录设备/版本/时间）。
- [ ] 实际微信手机深色模式公式预览通过（记录设备/版本/时间）。
- [ ] 离线模拟、API 回查没有被当作上述两项通过的证据。
- [ ] 延伸阅读真实链接在实际预览中可点击；无可用链接时整节省略。
- [ ] Each figure has a Chinese figure-title line in the `论文图 N` format
  translated from the original paper title, with identical alt text, followed
  by a separate Chinese explanatory line.
- [ ] Figure explanatory lines carry look-at-the-figure information only and do
  not restate the article's main argument.
- [ ] Rendered WeChat figure-title text is centered, one font size smaller than body text, and italic.
- [ ] RTD body figures preserve the same two-line caption meaning: centered
  smaller italic Chinese figure-title line, then separate explanatory line.
- [ ] Figure clarity has been checked in the final WeChat backend mobile preview.

## Independent RTD Page

- [ ] RTD 按全文精解指南从获授权原文独立维护，不由公众号改稿覆盖。
- [ ] 公众号语气修订未改 RTD 正文、附录、原图或其核验状态。
- [ ] 底部阅读原文指向正确的独立精解页，RTD 相关导航仍为站内链接。

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
