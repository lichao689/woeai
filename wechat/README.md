# WOEAI WeChat Research Magazine

This directory manages public-safe WeChat Official Account article material for WOEAI.

The basic unit is one selected paper, one article. Each article must be source-bounded by Zotero metadata, the WOEAI website, and public publication records.

Since 2026-06-17, the two channels have independent sources and purposes:

- **WeChat introduction:** `wechat/articles/draft-public-safe/<publication_ref>.md`
  is the source of truth for the reader-facing introduction and its rendered
  WeChat HTML. Apply backend wording corrections to this Markdown first.
- **RTD full-paper deep dive:** `docs/source/paper-notes/<publication_ref>.rst`
  is written directly from the approved original paper, following
  [the full-paper guide](../project/guides/paper-deep-dive-rst.md). Never generate a
  new deep dive from the WeChat introduction or overwrite one with its summary.

The channels may share approved figures, the cover, verified metadata, and
source evidence; their body text and coverage are not required to match.
Platform metadata such as cover image, draft media ID, and WeChat bottom
`阅读原文` / `content_source_url` belongs in the review note or backlog, not in
the reader-facing Markdown body.

For WOEAI website links embedded in WeChat draft API payloads, prefer the Read
the Docs project domain `https://woeai.readthedocs.io/zh-cn/latest/`. The
WeChat backend bottom `阅读原文` target defaults to the current paper's RTD
deep-dive page. Reader-facing related-paper navigation in the WeChat body
should use already-published WeChat article links only; RTD deep-dive pages use
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

Historical formula evidence (not current-run acceptance):

- Published WeChat formula-heavy examples use MathJax-style SVG output with
  `<mjx-container jax="SVG">`, inline `<svg>`, `data-mml-node`, and often
  `data-formula` / `data-formula-type` metadata.
- The repository renderer emits the same core structure, including
  `data-formula-type="inline-equation"` for inline formulas and
  `data-formula-type="block-equation"` for display formulas.
- A 2026-06-10 official `draft/add` stress test accepted one article body of
  about 113k characters containing multiple inline and display SVG formulas;
  the user confirmed the WeChat preview effect was satisfactory.

## Independent RTD Full-Paper Workflow

Read [project/guides/paper-deep-dive-rst.md](../project/guides/paper-deep-dive-rst.md)
before creating or updating an RTD paper deep dive. The approved PDF or author
manuscript and the corresponding `docs/source/Publications.rst` entry are
required. Missing full-paper source is a blocker; an abstract or WeChat article
cannot substitute for it.

Translate the complete paper body sentence by sentence in original order,
including sections, equations, figures, tables, captions, citations, references,
and appendices. Preserve limitations and discrepancies rather than inventing
repairs. Keep appendices before references; omit CRediT, conflict-of-interest,
data-availability, acknowledgements, and supplementary-material tail sections
as specified by the guide. Use `\qquad (N)` for manual equation numbers, not
`\tag{N}`. Place the cover immediately after the short-WeChat-link line and
retain the final `完整引用` link to the paper's Publications anchor.

Complete the guide's source-to-output coverage audit before delivery and run
its required site checks. Keep the audit and private source details out of the
public RST. Register pages under the Academic Outputs research-family and
subdirection hierarchy, preserving the stable paper-note URL.

`wechat/tools/markdown_to_rtd.py` is a historical introduction-page converter.
Use it only for explicitly requested maintenance of a legacy converted
introduction after verifying that its target is not an independent deep dive.
It is not part of new article production, and its `--check` is not a quality
gate for independent RTD pages. Do not run the converter over a full-paper page.

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
- source PDFs, raw paper extraction, private manifests, and local preview HTML.
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

Content production and backend delivery are separate stages. Use the current
authorized cloud workspace or runner; no Mac-first run is required. Follow
[the cloud workflow guide](../project/guides/cloud-wechat-workflow.md) for runtime
setup, private source inventory, and current-run checks. A previous machine's
successful API run does not establish this runner's credentials, connectivity,
or allowlist readiness. If the official API returns an IP-allowlist error,
report the IP returned by WeChat and have the operator resolve the allowlist
or choose an authorized fixed-egress runner; do not bypass the restriction.

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
current paper's RTD deep-dive page:
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

Use the repository renderer and official draft API only. Do not fall back to
third-party Markdown editors, doocs/md, Wechatsync, or browser-plugin submission
routes. If the API stage is blocked, retain the validated offline deliverables
and report the blocker. Human backend preview and publication remain separate.

## Cloud Content Setup

From the repository root, set up the content runtime, then load its environment
in each new shell:

```bash
./scripts/setup-cloud-workflow.sh
source scripts/cloud-workflow-env.sh
```

See [the cloud workflow guide](../project/guides/cloud-wechat-workflow.md) for
requirements and supported configuration. Setup prepares dependencies; it is
not an API credential setup, source-PDF restoration, live API check, or draft
submission. A fresh clone does not restore ignored `wechat/.local/` sources.
Verify the actual source files and runtimes before claiming readiness.

After setup, `./scripts/check-cloud-workflow.sh` runs the aggregate offline
smoke check with existing public-safe sample assets. Its private outputs go to
`wechat/.local/cloud-check/`. It does not contact WeChat or read credentials;
passing it establishes sample content/runtime readiness, not live API or
mobile-preview acceptance.

## Private Credential Storage

Keep WeChat Official Account API credentials in the authorized runner's private
storage outside the repository, using the supported secure setup. Default paths:

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
Account draft. Normal article drafting, theme design, independent RTD work, review,
and public-safety checks must not require reading WeChat credentials.

## WeChat Draft CLI: Offline Checks

Use `wechat/tools/wechat_draft.py` for the official API path. After runtime
setup and environment loading, run these no-submit content checks:

```bash
python3 wechat/tools/wechat_draft.py content-source-plan --all
python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-zhao2026-BS --theme academic-clean
python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-zhao2026-BS --theme academic-clean
```

These commands do not read credentials, contact WeChat, upload images, or
create/update a backend draft. `content-source-plan` lists expected bottom
`阅读原文` targets. `preflight` and `dry-run` validate the article, review note,
and assets, including the required `源文件获取记录` and `关键事实证据定位记录`
sections through `scripts/check-public-safe-content.py`. `dry-run` lists the
cover, body images, title, author, digest, and intended draft action.

### Credential And Network Diagnostics: Separate Opt-In Stage

Do not put these commands into the offline content-check sequence:

- `python3 wechat/tools/wechat_draft.py config-check` reads the private
  credential file to validate its shape without printing secrets. Run only
  when the user has explicitly authorized WeChat API configuration testing.
- `python3 wechat/tools/wechat_draft.py token-check` reads private credentials,
  requests or reuses an access token, and caches it outside the repository.
  It may contact WeChat and requires explicit authorization to test the API.
  It must never print the token.
- `python3 wechat/tools/wechat_draft.py ip-check` is optional network
  diagnostics. It contacts public-IP services but neither reads AppSecret nor
  contacts WeChat. It is not an offline check or a mandatory live-run gate;
  its detected route can differ from the actual API route.

A successful offline check does not establish API readiness. Report credential,
network, and allowlist checks independently from content and rendering checks.

### Authorized Live Draft Submission

The Markdown H1 is used as the WeChat draft title field. The rendered WeChat
body is body-only by default, so the title is not repeated inside the article
content under the Official Account's own title block.

After explicit user confirmation, choose the one appropriate live command;
do not run both as a setup sequence:

```bash
python3 wechat/tools/wechat_draft.py create-draft --publication-ref ref-zhao2026-BS
python3 wechat/tools/wechat_draft.py update-draft --publication-ref ref-zhao2026-BS
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

## Remote Draft Runner

An authorized cloud workspace can prepare content without API credentials or
a fixed public IP. A separate fixed-egress runner may be useful when the
Official Account's allowlist prevents the current runner from reaching the API.
It is not a prerequisite for writing, source review, offline rendering, or
no-submit validation.

Prepare a chosen runner using
[the cloud workflow guide](../project/guides/cloud-wechat-workflow.md), then verify
its own runtime, credentials, and official API connectivity within the user's
authorization. Keep credentials and token caches outside the repository. If a
fixed IP is required, have the operator configure the WeChat backend allowlist;
`WOEAI_WECHAT_EXPECTED_EGRESS_IPS` is only a local diagnostic expectation.

Run offline `preflight` before seeking or using approval for live submission.
Only after explicit approval run `update-draft` for a paper with an existing
`wechat_draft_media_id`, or `create-draft` for a paper without one. Do not bundle
live commands into setup or offline validation instructions. The runner must
stop at draft creation/update; publication, mass-send, and backend release
clicks remain prohibited for automation.

## Theme Selection

The official API path submits rendered HTML through the internal renderer.
Select a supported API renderer theme with `--theme` on `dry-run`,
`create-draft`, or `update-draft`.

Select the formula renderer with `--math-renderer`. Current options:

- `mathjax-svg`: default renderer for professional formula output.
  Standalone display formulas are wrapped as centered SVG formula blocks.
- `lightweight`: fallback renderer for troubleshooting or machines without the
  MathJax SVG runtime.

RTD display formulas should also render centered. The Sphinx site CSS applies
this to `.. math::` blocks, while inline formulas remain inline with the prose.

Example local preview:

```bash
python3 wechat/tools/render-copy-ready.py wechat/articles/draft-public-safe/ref-zhao2026-BS.md \
  -o wechat/.local/exports/ref-zhao2026-BS.academic-clean.mathjax-svg.html \
  --theme academic-clean \
  --no-embed-images
```

Example API dry-run:

```bash
python3 wechat/tools/wechat_draft.py dry-run \
  --publication-ref ref-zhao2026-BS \
  --theme academic-clean
```

`mathjax-svg` requires Node.js and `mathjax-full` in the current runtime.
Use `./scripts/setup-cloud-workflow.sh`, then
`source scripts/cloud-workflow-env.sh` to load the configured runtime and
`WOEAI_MATHJAX_NODE_MODULE_DIR`. Keep dependencies and generated HTML out of
public commits. If setup or rendering fails, report the actual blocker;
`lightweight` is an explicitly labelled diagnostic fallback, not evidence that
the default MathJax SVG route passed. Offline HTML/SVG counts and historical
stress tests do not replace a current WeChat backend mobile preview.

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
- `wechat_author`: optional WeChat draft author field; default to the paper's
  first author for journal-paper articles. Keep the full author list in `论文信息`.
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

1. Select a paper in `wechat/backlog/selected-papers.yml` and verify its
   `publication_ref`, WOEAI publication record, and DOI.
2. Inventory authorized sources in the current workspace and follow the source
   acquisition priority below. A repository clone is not a source-PDF backup.
3. Draft the WeChat introduction from `wechat/templates/paper-explainer.md`
   and create the separate public-safe evidence/review note.
4. When an RTD deep dive is in scope, produce it independently from the approved
   full paper under [the full-paper guide](../project/guides/paper-deep-dive-rst.md).
   Never derive it from the WeChat introduction. Complete its coverage audit
   and required Sphinx/site checks separately.
5. Check source evidence, figure reuse, public safety, and article/asset paths.
   Render offline HTML with the repository renderer and run `preflight` or
   `dry-run`. Pure WeChat article/review work does not require a Sphinx build.
6. If backend delivery is requested, assess credentials and actual-runner API
   connectivity in the separately authorized diagnostic stage. Explain the
   credential access, approved-image uploads, and target draft create/update,
   then obtain explicit confirmation before live submission.
7. After a successful live operation, record only non-sensitive draft metadata
   and supported backlog state. Failed calls and no-submit checks do not
   advance the state.
8. A human previews, proofreads, and publishes in the WeChat backend. Keep
   formula/figure/cover preview flags false until their actual backend previews
   are checked. Apply wording corrections back to the WeChat Markdown and
   regenerate that draft; do not synchronize its abbreviated body into RTD.
9. Record the confirmed published URL and appropriate state in the backlog
   and, when relevant, `wechat/index.yml`.

## Zotero Source Acquisition Priority

Use this order for WOEAI paper articles:

1. Inspect authorized source files and manifests already available in the
   current workspace, including ignored `wechat/.local/` storage. Journal
   PDFs may be under `journal-papers/<ZoteroKey>/source.pdf` or
   `<publication_ref>/source.pdf`; inspect actual files rather than assuming
   a historical inventory was restored. Verify paper identity, source version,
   reuse status, and manifest before use.
2. Check Zotero metadata, DOI, `abstractNote`, and attachment records when
   accessible. Zotero Desktop Local API is available only on the user's actual
   desktop; it is not a prerequisite for cloud content production. Record the
   metadata source and unavailable checks rather than claiming a Desktop check.
3. Use the approved local PDF or author manuscript to verify abstract, figures,
   captions, and body evidence. If sources were transferred, keep the original
   source SHA-256 and downloaded-copy SHA-256 separately labelled in private
   records. A transfer hash alone does not prove original byte identity.
4. If the source is missing, try the Zotero Web API `/file` endpoint only when
   authorized access is available, with credentials and downloaded files kept
   private. Otherwise request source synchronization or an approved author
   manuscript and record `需要同步 PDF 或提供作者稿`.
5. Do not invent PDF-derived facts. Missing full-paper source blocks an RTD
   full-paper deep dive even if the WeChat introduction or abstract is present.

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
