# WOEAI WeChat Style Guide

## Article Unit

Use one selected paper per article.

Do not turn every article into a multi-paper theme essay. Related papers may appear in the `延伸阅读` section.

## Default Structure

1. `论文信息`
2. `研究问题`
3. `方法贡献`
4. `关键发现`
5. `工程意义`
6. `适用边界`
7. `图文说明` when a separate figure summary is useful
8. `延伸阅读`
9. `阅读原文`
10. `联系入口`

## Tone

- Scholarly first.
- Engineering relevance second.
- No hype.
- No unsupported partner names or project claims.
- Use DOI and WOEAI site references for traceability.

## Formula Handling

- Use Markdown LaTeX as the canonical formula source in WeChat article drafts: `$...$` for inline formulas and `$$...$$` for display formulas.
- Render WeChat formulas through the WeChat Markdown workflow, such as doocs/md, and verify the resulting formula display in the final WeChat backend mobile preview.
- RTD companion pages should convert the same LaTeX formula semantics to Sphinx math markup: ``:math:`...` `` for inline formulas and `.. math::` for display formulas.
- Do not render formulas as images by default. Formula images are too easy to blur after upload, compression, or mobile scaling; use them only as a fallback when the final WeChat preview cannot preserve a readable formula.
- Keep formulas short and readable on mobile. If a formula is long, split the explanation into nearby text rather than forcing a dense display block.
- After each important formula, add a plain-language sentence explaining what the formula means and why it matters for the paper.

## Figure Handling

- WOEAI WeChat paper articles are generated for the user's own authored papers unless the user explicitly says otherwise.
- For author-confirmed papers, extract suitable original figures directly from the paper PDF or author manuscript and insert them into the reader-facing Markdown.
- Prefer `pdfimages -all` extraction from the PDF. If a figure is stored as ordered image strips, stitch those strips back into a complete figure before using page-render cropping.
- Store final public-safe article figures under `wechat/assets/public-safe/<publication_ref>/`.
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
