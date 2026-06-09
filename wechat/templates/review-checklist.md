# WeChat Article Review Checklist

## Source

- [ ] Zotero Desktop Local API metadata, DOI, and `abstractNote` have been checked.
- [ ] Zotero Desktop Local API attachment records have been checked.
- [ ] Local PDF attachment exists and was used for PDF-derived abstract, figures, captions, and body evidence; or the review note records why it was unavailable.
- [ ] If local PDF was unavailable, Zotero Web API `/file` access was tried when credentials were available.
- [ ] If no PDF source was available, the review note records `需要同步 PDF 或提供作者稿` and the draft does not invent PDF-derived facts.
- [ ] DOI matches the WOEAI publication record.
- [ ] WOEAI publication anchor exists in `docs/source/Publications.rst`.
- [ ] Journal, year, authors, and metrics are copied from source-bounded data.
- [ ] Related direction page exists.

## Copyright

- [ ] The paper is authored by the user/WOEAI, or reuse rights/source status are otherwise confirmed.
- [ ] Original high-resolution paper figures are extracted from the PDF or author manuscript when they are legally safe and clear on mobile.
- [ ] Redrawn figures are used only when original figures are unavailable, legally unsafe, low-resolution, or unsuitable for WeChat display.
- [ ] Image source and extraction method are recorded in the separate `.review.md` file.

## Formulas And Figures

- [ ] WeChat draft formulas use Markdown LaTeX: `$...$` for inline formulas and `$$...$$` for display formulas.
- [ ] RTD companion formulas use Sphinx math markup: ``:math:`...` `` for inline formulas and `.. math::` for display formulas.
- [ ] Inline mathematical variables, symbolic parameters, metrics, dimensional quantities, and unit-bearing values use formula markup rather than code spans.
- [ ] Formulas are not rendered as images unless final WeChat preview proves an image fallback is needed.
- [ ] Important formulas have plain-language explanations.
- [ ] Formula display has been checked in the final WeChat backend mobile preview.
- [ ] Figure clarity has been checked in the final WeChat backend mobile preview.

## RTD Companion Page

- [ ] The RTD companion page is reStructuredText converted from the WeChat Markdown article, not a separate Markdown route in Sphinx.
- [ ] The RTD companion page preserves the same title, body text, images, DOI link, WOEAI publication anchor, and contact/link intent as the WeChat article.
- [ ] The RTD companion page is listed under `学术进展 Academic Progress` on the relevant research-direction page.
- [ ] The entry is grouped by second-level research subdirection and sorted by publication date descending until a more specific sorting rule exists.

## Public Safety

- [ ] No WeChat AppSecret, token, cookie, or credential appears.
- [ ] No Zotero API key appears.
- [ ] No private partner name appears.
- [ ] No unconfirmed project status appears.
- [ ] No private review comment appears.
- [ ] The draft is safe to expose in a public GitHub repository.
