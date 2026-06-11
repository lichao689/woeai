# WOEAI WeChat Research Magazine

This directory manages public-safe WeChat Official Account article material for WOEAI.

The basic unit is one selected paper, one article. Each article must be source-bounded by Zotero metadata, the WOEAI website, and public publication records.

Each One-Paper WeChat Article may also have an RTD Paper Companion Page under `docs/source/paper-notes/<publication_ref>.rst`. The reader-facing Markdown file under `wechat/articles/draft-public-safe/` is the public content master. Align public wording, formulas, figure captions, and body links there first, then convert that same content to Sphinx-compatible reStructuredText and render the WeChat draft from the same Markdown. Platform metadata such as cover image, draft media ID, and WeChat bottom `阅读原文` / `content_source_url` belongs in the review note or backlog, not in the public正文 master.

For WOEAI website links embedded in WeChat draft API payloads, prefer the Read
the Docs project domain `https://woeai.readthedocs.io/zh-cn/latest/`. The
WeChat backend bottom `阅读原文` target defaults to the current paper's RTD
companion page. Reader-facing related-paper navigation in the WeChat body
should use already-published WeChat article links only; RTD companion pages use
internal paper-note links. This does not automatically change the public
website's own canonical SEO URL or homepage contact display.

Use clear visible labels for RTD-side WOEAI links, for example:

- `WOEAI | 建筑结构抗风方向介绍`
- `WOEAI | 主页`

For figure captions in Chinese WeChat articles, use a Chinese figure-title line
translated from the paper's original title, followed by a separate Chinese
explanatory line. The WeChat renderer should make the figure title centered,
one font size smaller than body text, and italic.

Formula source should keep Markdown LaTeX semantics. For the official API path,
MathJax SVG pre-rendering is the default formula route; it converts LaTeX into
inline SVG HTML before submission, without relying on WeChat to run MathJax or
load external scripts. The lightweight HTML renderer remains a fallback for
troubleshooting. Every formula route must be checked in the WeChat backend
mobile preview before publishing.

Formula test summary:

- Published WeChat formula-heavy examples use MathJax-style SVG output with
  `<mjx-container jax="SVG">`, inline `<svg>`, `data-mml-node`, and often
  `data-formula` / `data-formula-type` metadata.
- WOEAI local testing now emits the same core structure, including
  `data-formula-type="inline-equation"` for inline formulas and
  `data-formula-type="block-equation"` for display formulas.
- A 2026-06-10 official `draft/add` stress test accepted one article body of
  about 113k characters containing multiple inline and display SVG formulas;
  the user confirmed the WeChat preview effect was satisfactory.

## Markdown To RTD Conversion

The reader-facing Markdown article is the public content master. Use
`wechat/tools/markdown_to_rtd.py` to generate the matching RTD Paper Companion
Page:

```bash
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BS
python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BS --check
```

Default paths are:

- input article: `wechat/articles/draft-public-safe/<publication_ref>.md`
- review note: `wechat/articles/review/<publication_ref>.review.md`
- output page: `docs/source/paper-notes/<publication_ref>.rst`

The converter handles the WOEAI paper-article subset: headings, paragraphs,
lists, direct external Markdown links, inline/display LaTeX, and local
public-safe body images with two-line Chinese captions. It reads RTD cover
metadata from the review note, preferring `rtd_cover_image`, then
`wechat_cover_image`, then `cover_image`, and finally the `封面素材` line. The
cover is inserted below the RST title, while body figure captions keep the same
two-line meaning as the Markdown source. The converter also appends RTD-only
related-paper navigation with internal `paper-notes` links when related
companion pages already exist.

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

## Publishing Paths

The primary automated path is the official WeChat draft API:

1. Start from the public-safe WeChat Article Source and approved assets.
2. Render Markdown to WeChat-compatible HTML through a deterministic conversion
   layer.
3. Upload the approved cover image and body images through official WeChat API
   endpoints.
4. Create or update the Official Account draft.
5. Record only non-sensitive WeChat Draft Record fields.
6. Stop at the manual publication gate.

The first practical API run is from the current Mac. Long-term cloud or CI
automation should be designed only after this local API path succeeds. If the
Official Account API returns an IP-allowlist error, use the IP reported by the
WeChat response or move the workflow to a fixed-egress remote runner.

The tool must default to a no-submit check. A real draft creation or update
requires a live run. In conversational use, the agent must first explain that
it will read private WeChat API credentials, upload approved images, and create
or update a WeChat backend draft. The user must explicitly confirm creating the
WeChat draft before the agent may run the live command. Vague approval such as
`继续`, `可以`, or `试试` is not enough.

Dry-run output should list the approved cover image and every approved body
image that would be uploaded, without reading credentials or contacting WeChat.
Live runs upload the approved cover image, upload every approved body image,
replace local Markdown image paths with WeChat image URLs in the submitted HTML,
and then create or update the WeChat draft.

By default, the API payload sets WeChat's bottom `content_source_url` to the
current paper's RTD companion page:
`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/<publication_ref>.html`.
Reader-facing links should still live in the article body instead of a body
`阅读原文` section. When the editor explicitly wants a different bottom
`阅读原文` target for one article, set `wechat_content_source_url` in that
article's review front matter; the API payload will use that value as
`content_source_url`. An explicitly blank `wechat_content_source_url` means
that article should have no bottom `阅读原文` link.

The API renderer appends WeChat-body related-paper navigation only when related
items already have public WeChat URLs in `latest_published_url`; unpublished
related papers are omitted.

doocs/md is no longer needed for the normal WOEAI draft-submission workflow.
Keep it only as an auxiliary design and fallback path for theme CSS tuning,
formula/style preview, and manual copy-paste when the official API path is not
configured or needs troubleshooting.

Wechatsync or other browser-plugin routes may be useful for one-off
distribution experiments, but they are not the default WOEAI automation path
and should not become the article source of truth.

## Private Credential Storage

Store WeChat Official Account API credentials only on the local machine:

- credential file: `~/.config/woeai/wechat_official_account.env`
- optional IP diagnostic file: `~/.config/woeai/wechat_runner.env`
- token cache: `~/.cache/woeai/wechat_access_token.json`

The credential file should contain only:

```bash
WECHAT_OFFICIAL_ACCOUNT_APP_ID=...
WECHAT_OFFICIAL_ACCOUNT_APP_SECRET=...
```

The optional IP diagnostic file is separate from the credential file so that
manual IP checks can run without reading AppSecret. It may contain:

```bash
WOEAI_WECHAT_EXPECTED_EGRESS_IPS=203.0.113.10
```

Use a comma-separated list if multiple fixed runner IPs are intentionally
allowed. This value is for diagnostics only; live create/update commands no
longer stop on this local check because local public-IP probes can disagree
with the actual WeChat API path.

The token cache is a private implementation detail used by the API layer. A
typical cache record may include `access_token`, `expires_at`, and `fetched_at`,
but the file itself must stay outside this repository and must not be printed,
logged, committed, copied into review notes, or included in API dry-run output.

Agents may read the credential file only when the user explicitly asks to test
the WeChat API path or explicitly confirms live creation/update of an Official
Account draft. Normal article drafting, theme design, RTD conversion, review,
and public-safety checks must not require reading WeChat credentials.

## Local WeChat Draft CLI

Use `wechat/tools/wechat_draft.py` for the official API path.

Safe local checks:

```bash
python wechat/tools/wechat_draft.py config-check
python wechat/tools/wechat_draft.py ip-check
python wechat/tools/wechat_draft.py content-source-plan --all
python wechat/tools/wechat_draft.py preflight --publication-ref ref-zhao2026-BS --theme academic-clean
python wechat/tools/wechat_draft.py token-check
python wechat/tools/wechat_draft.py dry-run --publication-ref ref-zhao2026-BS --theme academic-clean
```

`config-check` verifies credential-file shape without printing secrets.
`ip-check` shows the current public egress IP without reading credentials or
contacting WeChat; it is diagnostic only and is not a live-run gate.
`content-source-plan` lists the expected bottom `阅读原文` targets without
reading credentials or contacting WeChat.
`preflight` runs the same article and asset validation used by `dry-run`
without reading credentials or contacting WeChat. Both commands run
`scripts/check-public-safe-content.py` against the target article and review
note, including the required `源文件获取记录` and `关键事实证据定位记录` section
check.
`token-check` reads the private credential file, requests or reuses an
`access_token`, caches it outside the repository, and never prints the token.
`dry-run` does not read credentials and does not contact WeChat; it lists the
cover image, body images, title, author, digest, and draft action that would be
used.

The Markdown H1 is used as the WeChat draft title field. The rendered WeChat
body is body-only by default, so the title is not repeated inside the article
content under the Official Account's own title block.

Live commands are allowed only after explicit user confirmation at action time:

```bash
python wechat/tools/wechat_draft.py create-draft --publication-ref ref-zhao2026-BS
python wechat/tools/wechat_draft.py update-draft --publication-ref ref-zhao2026-BS
```

Live commands read private credentials, upload the approved cover image and
approved body images, replace local Markdown image paths with WeChat image
URLs in the submitted HTML, create or update the WeChat backend draft, and then
write only non-sensitive draft metadata back to `wechat/backlog/selected-papers.yml`.
Before reading credentials or uploading images, live commands run the same
target article/review public-safety validation as `preflight`.
They do not run a local fixed-IP guard by default. If WeChat rejects the token
or draft request with an IP-allowlist error, use the IP reported by WeChat as
the next action item.

## Remote Publishing Runner

Use a remote runner when the local network's public IP can change. The runner
is just a small machine with a fixed public egress IP that can pull this repo
and run `wechat/tools/wechat_draft.py`.

Minimum runner requirements:

- a stable public IPv4 address that can be added to the Official Account API IP
  allowlist;
- SSH access for the human/operator or agent;
- Python 3.10+ and Git;
- a clone of this repository;
- private files on the runner only:
  `~/.config/woeai/wechat_official_account.env` and
  `~/.config/woeai/wechat_runner.env`;
- the runner's fixed IP configured in both the WeChat backend allowlist and
  `WOEAI_WECHAT_EXPECTED_EGRESS_IPS`.

Recommended runner flow:

```bash
cd /path/to/woeai
git pull --ff-only
python wechat/tools/wechat_draft.py preflight --publication-ref ref-zhao2026-BS --theme academic-clean
python wechat/tools/wechat_draft.py update-draft --publication-ref ref-zhao2026-BS --theme academic-clean
```

The final live command still requires explicit human confirmation in the
conversation or operating procedure. The runner may create or update drafts; it
must not publish, mass-send, or click WeChat backend release buttons.

## Theme Selection

The official API path submits rendered HTML, not doocs/md CSS. Select a
supported API renderer theme with `--theme` on `dry-run`, `create-draft`, or
`update-draft`.

Select the formula renderer with `--math-renderer`. Current options:

- `mathjax-svg`: default renderer for professional formula output.
  Standalone display formulas are wrapped as centered SVG formula blocks.
- `lightweight`: fallback renderer for troubleshooting or machines without the
  MathJax SVG runtime.

RTD display formulas should also render centered. The Sphinx site CSS applies
this to `.. math::` blocks, while inline formulas remain inline with the prose.

Example local preview:

```bash
python wechat/tools/render-copy-ready.py wechat/articles/draft-public-safe/ref-zhao2026-BS.md \
  -o wechat/.local/exports/ref-zhao2026-BS.academic-clean.mathjax-svg.html \
  --theme academic-clean \
  --no-embed-images
```

Example API dry-run:

```bash
python wechat/tools/wechat_draft.py dry-run \
  --publication-ref ref-zhao2026-BS \
  --theme academic-clean
```

`mathjax-svg` requires Node.js and the `mathjax-full` package on the publishing
machine. Keep these runtime dependencies outside the public repository, for
example:

```bash
npm --prefix /tmp/woeai-formula-render-node install mathjax-full
```

If the package is installed somewhere else, set
`WOEAI_MATHJAX_NODE_MODULE_DIR` to that `node_modules` directory before running
the renderer.

Current supported API theme:

- `academic-clean`: the default scholarly WOEAI article style used by
  `wechat/tools/render-copy-ready.py`.
- `engineering-note`: a more applied technical style for engineering readers
  and collaboration-facing articles.
- `recruitment-friendly`: a warmer direction-introduction style for
  recruitment-facing articles while keeping the same paper facts.

These themes change presentation only. They must not change the article's
facts, section order, citations, formulas, or public-safety boundaries. Check
the WeChat backend mobile preview before publishing a theme for the first time.

Recommended default for paper explainers: `academic-clean`.

For manual doocs/md fallback, use the CSS files under `wechat/themes/`. The
current committed doocs/md CSS is `wechat/themes/doocs-academic-clean.css`.

## Backlog State Model

Use `wechat/backlog/selected-papers.yml` to track selected papers and publication state.

- `repost_priority`: one of `high`, `medium`, or `low`; use higher priorities first when starting the next article.
- `wechat_status`: one of `selected`, `drafting`, `reviewing`, `ready_to_publish`, `published`, or `archived`.
- `publication_mode`: one of `first_publish`, `rewrite`, or `republish`; this records the publication intent, while `wechat_status` records workflow progress.
- `previous_published_url`: the earlier public WeChat URL, if this article is being rewritten or republished.
- `latest_published_url`: the newest public WeChat URL after publication.
- `wechat_draft_media_id`: optional non-sensitive draft `media_id` returned by the WeChat draft API after the article is created in the Official Account draft box.
- `wechat_draft_created_at`: optional Beijing-time timestamp for the first successful draft-box creation.
- `wechat_draft_updated_at`: optional Beijing-time timestamp for the latest successful draft-box update.
- `wechat_author`: optional WeChat draft author field; default to `WOEAI` for
  WOEAI paper articles.
- `revision_note`: short public-safe note explaining why a historical paper is being rewritten or republished.
- `publication_history`: optional public-safe list with entries shaped as `published_at`, `mode`, `url`, and `note`.

After a live draft creation/update succeeds, the tool should write back only
these non-sensitive fields to `wechat/backlog/selected-papers.yml`:
`wechat_status: ready_to_publish`, `wechat_draft_media_id`,
`wechat_draft_created_at`, and `wechat_draft_updated_at`. If the live call fails
or only a no-submit check was run, do not advance `wechat_status` and do not
write speculative draft metadata.

When `wechat_draft_media_id` is absent, a live submission creates a new WeChat
draft. When `wechat_draft_media_id` is already present, a live submission should
update that existing draft by default. Create a separate new draft only when the
user explicitly asks for a new copy.

Do not store WeChat AppSecret, access tokens, refresh tokens, cookies, preview
credentials, raw API responses, or private preview URLs in the backlog. When an
article has been successfully submitted to the WeChat draft box and has no
known review blockers, `wechat_status` should normally be `ready_to_publish`
until the human publication step is complete.

Automation must stop at draft creation or draft update. It must not call WeChat
publish, mass-send, or browser-driven release actions. The final publication
gate is manual preview, proofreading, and confirmation in the WeChat backend.

## Workflow

1. Select a paper in `wechat/backlog/selected-papers.yml`.
2. Use the Zotero source acquisition priority to gather metadata, abstracts,
   attachments, and PDF source material.
3. Create a draft from `wechat/templates/paper-explainer.md`.
4. Convert the same public article content to an RTD Paper Companion Page in `.rst` format when the article should appear on the website.
5. List the RTD page under `学术进展 Academic Progress` on the relevant research-direction page, grouped by second-level research subdirection and sorted by publication date descending until a more specific sorting rule exists.
6. Verify the paper's WOEAI site record and DOI.
7. Complete the source, copyright, public-safety, and RTD companion-page checklist.
8. Render the Markdown through the deterministic Markdown-to-WeChat-HTML
   conversion layer for API submission. Use doocs/md for theme design, formula
   preview, and manual fallback.
9. Create or update a WeChat draft through the official draft API as the
   primary automated submission path when credentials are configured.
10. Preview, proofread, and publish manually in the WeChat backend. Do not
   automate this release step.
11. Record only non-sensitive draft metadata, the published URL, and state
   fields in `wechat/backlog/selected-papers.yml` and, when useful, in
   `wechat/index.yml`.

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

This is not a general web-scraping workflow. Do not automatically scrape or
download PDFs from publisher pages, DOI landing pages, Google Scholar,
ResearchGate, Sci-Hub, search results, or other general web pages. Web pages
may be used to verify public metadata only. A web PDF may be downloaded only
after the user explicitly approves a specific public and legal source, such as
an OA PDF, an author manuscript, or a user-provided download link. Keep such
downloads under ignored private working paths such as
`wechat/.local/<publication_ref>/`, never commit the PDF to the public
repository, and record the source and approval status in the review note.

Every article review note must include a public-safe `源文件获取记录` section.
Use it to record the Zotero key, metadata source, attachment-record status,
local PDF status, PDF source type, private-storage class, Zotero Web API
`/file` status, web-download status, abstract source, body-evidence source, and
figure source. Do not record absolute private file paths, credentials, cookies,
raw API payloads, or downloaded PDF contents in committed files.

When a Zotero item has multiple PDF-like attachments, choose the PDF evidence
source in this order: author final manuscript / author manuscript, publisher
version of record PDF, open-access platform PDF, preprint, then other
attachments. Record the selected class in the review note. If a lower-priority
source is used, explain why the higher-priority source was missing, unreadable,
legally unsafe, or visually unsuitable. Journal, year, volume, issue, pages,
DOI, and publication status still come from Zotero metadata and the official
published record.

Every article review note must also include a public-safe
`关键事实证据定位记录` section. It should not annotate every sentence, but it
must record evidence anchors for the abstract, core claims or conclusions, key
figures, and key formulas. Use PDF file page, section, table, original figure
number, or original equation number when available. If a WeChat article formula
is an editorial explanation rather than a numbered paper equation, record that
distinction and point to the paper evidence it explains. Mark unaudited pages
as `pending PDF page audit` instead of guessing. Evidence locations use PDF
file page numbers, written as `PDF file page N`, not journal printed page
numbers or article pagination.

`scripts/check-public-safe-content.py` enforces that every
`wechat/articles/review/*.review.md` file includes both `## 源文件获取记录` and
`## 关键事实证据定位记录`.
