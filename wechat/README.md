# WOEAI WeChat Research Magazine

This directory manages public-safe WeChat Official Account article material for WOEAI.

The basic unit is one selected paper, one article. Each article must be source-bounded by Zotero metadata, the WOEAI website, and public publication anchors.

## Research Families

- `建筑结构抗风`
- `海上漂浮风电`

## Public Boundary

This repository is public. Anything committed here is treated as public.

Do not commit:

- WeChat AppSecret, access tokens, cookies, preview credentials, or API keys.
- Zotero API keys or private library credentials.
- private review notes.
- unpublished partner names or project details.
- copyrighted publisher figures unless reuse rights are confirmed.
- local WeChat preview HTML.
- source image files that are not approved for public release.

Use `wechat/articles/draft-public-safe/` only for drafts that are safe to expose before publication. Keep private working material under ignored local paths such as `wechat/.local/`.

## Backlog State Model

Use `wechat/backlog/selected-papers.yml` to track selected papers and publication state.

- `repost_priority`: one of `high`, `medium`, or `low`; use higher priorities first when starting the next article.
- `wechat_status`: one of `selected`, `drafting`, `reviewing`, `ready_to_publish`, `published`, or `archived`.
- `publication_mode`: one of `first_publish`, `rewrite`, or `republish`; this records the publication intent, while `wechat_status` records workflow progress.
- `previous_published_url`: the earlier public WeChat URL, if this article is being rewritten or republished.
- `latest_published_url`: the newest public WeChat URL after publication.
- `revision_note`: short public-safe note explaining why a historical paper is being rewritten or republished.
- `publication_history`: optional public-safe list with entries shaped as `published_at`, `mode`, `url`, and `note`.

## Workflow

1. Select a paper in `wechat/backlog/selected-papers.yml`.
2. Create a draft from `wechat/templates/paper-explainer.md`.
3. Verify the paper's WOEAI site reference and DOI.
4. Complete the source, copyright, and public-safety checklist.
5. Render the Markdown in a WeChat Markdown editor such as doocs/md.
6. Publish manually in the WeChat backend.
7. Record the published URL and state fields in `wechat/backlog/selected-papers.yml` and, when useful, in `wechat/index.yml`.
