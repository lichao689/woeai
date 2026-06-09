# WOEAI WeChat Research Magazine

This directory manages public-safe WeChat Official Account article material for WOEAI.

The basic unit is one selected paper, one article. Each article must be source-bounded by Zotero metadata, the WOEAI website, and public publication anchors.

Each One-Paper WeChat Article may also have an RTD Paper Companion Page under `docs/source/paper-notes/<publication_ref>.rst`. The RTD page is generated as Sphinx-compatible reStructuredText converted from the WeChat Markdown article, not through a separate Markdown route in Sphinx. It should preserve the same public title, body text, images, DOI link, WOEAI publication anchor, and contact/link intent, with only markup and rendering differences.

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
2. Use the Zotero source acquisition priority to gather metadata, abstracts,
   attachments, and PDF source material.
3. Create a draft from `wechat/templates/paper-explainer.md`.
4. Convert the same public article content to an RTD Paper Companion Page in `.rst` format when the article should appear on the website.
5. List the RTD page under `学术进展 Academic Progress` on the relevant research-direction page, grouped by second-level research subdirection and sorted by publication date descending until a more specific sorting rule exists.
6. Verify the paper's WOEAI site reference and DOI.
7. Complete the source, copyright, public-safety, and RTD companion-page checklist.
8. Render the Markdown in a WeChat Markdown editor such as doocs/md.
9. Publish manually in the WeChat backend.
10. Record the published URL and state fields in `wechat/backlog/selected-papers.yml` and, when useful, in `wechat/index.yml`.

## Zotero Source Acquisition Priority

Use this order for WOEAI paper articles:

1. Use the Zotero Desktop Local API to read metadata, DOI, and `abstractNote`.
2. Use the Zotero Desktop Local API to list attachment items.
3. If a local PDF attachment exists, use that PDF to extract or verify the
   abstract, figures, captions, and paper body needed for the article.
4. If the local PDF attachment is missing, try the Zotero Web API `/file`
   endpoint for the attachment, using private credentials only outside the
   repository.
5. If neither local attachment nor Web API file access is available, record
   `需要同步 PDF 或提供作者稿` in the review note and do not invent PDF-derived
   facts.
