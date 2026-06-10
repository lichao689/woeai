# Public Safety Checklist

This repository is public. Every committed file must be safe to expose.

## Never Commit

- WeChat AppSecret.
- WeChat access token or refresh token.
- Zotero API key.
- cookies or preview credentials.
- private partner names.
- unconfirmed project status.
- internal review notes.
- local preview HTML.
- publisher-owned figures without confirmed reuse rights.

## Allowed

- public-safe article drafts.
- published article Markdown.
- original diagrams approved for public release.
- WOEAI website links.
- DOI links.
- Zotero item keys when used as public workflow identifiers.

## Automated Checks

- `scripts/check-public-safe-content.py` must pass before a WeChat paper article
  review note is treated as ready.
- Every `wechat/articles/review/*.review.md` file must include
  `## 源文件获取记录` and `## 关键事实证据定位记录`.
- `wechat/tools/wechat_draft.py dry-run`, `preflight`, `create-draft`, and
  `update-draft` must run the public-safety check against the target article
  and review note before any credential read or WeChat API draft call.
