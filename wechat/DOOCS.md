# WOEAI doocs/md Publishing Path

Use this path when publishing a WOEAI WeChat Markdown article through
<https://md.doocs.org/>.

## Fast Manual Flow

1. Open <https://md.doocs.org/> in Chrome.
2. Paste the article Markdown from `wechat/articles/draft-public-safe/`.
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

## Faster Later

To reduce manual image handling, configure a doocs/md image bed. The doocs/md
project supports multiple image beds, including the WeChat Official Account
image bed when `appID`, `appsecret`, and a proxy domain are configured.
