# WOEAI doocs/md Auxiliary Path

Use this path for WOEAI WeChat theme design, formula/style preview, and manual
copy-paste fallback through <https://md.doocs.org/>. The primary automated
submission path is the official WeChat draft API, not doocs/md.

You do not need this file for the normal workflow after the official API path is
configured. Keep it as a troubleshooting and visual-design fallback when the API
path is unavailable, when a theme needs quick manual comparison, or when a
human editor wants to copy-paste through doocs/md.

## Fast Manual Flow

1. Open <https://md.doocs.org/> in Chrome.
2. Put the Markdown H1 into the Official Account title field. Paste only the
   Markdown body below that H1 into doocs/md, so the WeChat body does not repeat
   the title under WeChat's own title block.
3. Paste `wechat/themes/doocs-academic-clean.css` into the custom CSS or style
   extension panel.
4. Upload article images through the doocs/md image tool. For the sample article,
   use `wechat/assets/public-safe/ref-zhao2026-BS/`.
5. Check formulas in the doocs/md preview. doocs/md supports KaTeX, so Markdown
   formulas should remain as `$...$` and `$$...$$`.
6. Use the doocs/md copy action, then paste into the WeChat Official Account
   editor.
7. Run the final WeChat backend mobile preview before publishing.

## Current Sample

- Article: `wechat/articles/draft-public-safe/ref-zhao2026-BS.md`
- Theme CSS: `wechat/themes/doocs-academic-clean.css`
- Images: `wechat/assets/public-safe/ref-zhao2026-BS/`

The API CLI currently supports `academic-clean`, `engineering-note`, and
`recruitment-friendly`. Only `doocs-academic-clean.css` is currently committed
as a reusable doocs/md fallback CSS. Add one CSS file per doocs/md theme only
when the manual fallback path actually needs that theme.

## Image Handling

For the automated path, upload cover and body images through the official
WeChat API layer. For the manual doocs/md fallback, upload images through the
doocs/md image tool. Any image-bed credentials or proxy configuration must stay
outside this public repository.
