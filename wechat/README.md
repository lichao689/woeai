# WOEAI WeChat Research Magazine

This directory manages public-safe WeChat Official Account article material for WOEAI.

This README owns WeChat **delivery**: rendering, formula SVG and dark-mode
acceptance, the official draft API, credentials, and backlog state. Other rules
live in one place each:

- writing rules and article structure: [writing-standards.md](../.agents/skills/wechat-paper/references/writing-standards.md)
- de-AI editing workflow: [natural-scientific-writing.md](../.agents/skills/wechat-paper/references/natural-scientific-writing.md)
- source acquisition, evidence records, figure extraction:
  [paper-sources-and-evidence.md](../project/guides/paper-sources-and-evidence.md)
- execution order for agents: [wechat-paper skill](../.agents/skills/wechat-paper/SKILL.md)
- templates: [templates/](templates/)

Workflow state now lives only in `docs/data/publications.json`; the backlog is a
generated compatibility view. Read [the registry guide](../project/guides/publication-registry.md)
and [progress view](../project/publication-progress.md). Historical statuses in
review notes are evidence history, not current readiness. New draft media IDs
are private operational data in ignored `wechat/.local/registry-drafts.json`.

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

### One current cover source

Each paper has one approved current cover: `wechat/assets/public-safe/<publication_ref>/cover.png`.
Its current review note selects it with the single `cover_image` field. WeChat,
RTD and the bilingual homepage share that source; `wechat_cover_image`,
`rtd_cover_image` and historical `封面素材` prose are never fallback selectors.
A missing, redirected or noncanonical current path fails rather than reviving an old image.
Historical audit text is evidence about its Git baseline, not a second active source.

Sphinx generates homepage copies directly under its output `_static/home/`;
those bytes are reproducible output, never hand-maintained source assets under
`docs/_static/home/progress-*.png`. Keep only the approved current source in the
working tree. Delete recoverable tracked superseded covers normally, preserving
Git history; unique uncommitted candidates need recovery protection first.
Do not delete scientific figures, PDFs, audit notes, private journals or backups.

Cover or review changes invalidate old fingerprints. Retain the prior scientific
audit and perform an explicitly documented non-content equivalence check before
renewing verification: compare bibliography, source identities, scientific prose,
figures and applicable rules, and record the approved cover's identity and scope.
Add separate migration review/evidence; preserve old fingerprints. An already
stale record cannot become approved through migration. This is not a new PDF
full-paper audit, backend phone preview or publication. Channel statuses and
backend history do not change merely because local paths were unified.

For WOEAI website links embedded in WeChat draft API payloads, prefer the Read
the Docs project domain `https://woeai.readthedocs.io/zh-cn/latest/`. The
WeChat backend bottom `阅读原文` target defaults to the current paper's RTD
deep-dive page. Reader-facing related-paper navigation in the WeChat body
should use already-published WeChat article links only; RTD deep-dive pages use
internal paper-note links. This does not automatically change the public
website's own canonical SEO URL or homepage contact display.

Figure-caption wording follows the bundled writing standards section 7. The WeChat renderer makes
the figure-title line centered, one font size smaller than body text, and italic.

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

## Formula SVG And Dark-Mode Acceptance

Formula writing rules are in the bundled writing standards section 8; this section covers rendering.

- Use transparent SVG formulas that inherit the adjacent text color through
  `currentColor`. Use standard `span` (inline) / `section` (display)
  containers and set the first SVG group's fill/stroke both as presentation
  attributes and inline styles. Preserve vector geometry, fraction bars,
  baseline, explicit internal colors and LaTeX metadata (`data-formula`,
  `data-formula-type`). Formula blocks must not impose a fixed foreground or
  background; do not restore opaque white formula tiles.
- This follows the [WeChat SVG guidance](https://github.com/wechatjs/verify-article-structure-spec/blob/main/verify_article_structure.md#44-svg)
  and the export structure used by [doocs/md](https://github.com/doocs/md/blob/main/packages/core/src/extensions/katex.ts).
  These sources support the approach, not a guarantee for every phone reader.
- Display formulas are centered, with horizontal overflow for wide equations.
  RTD display formulas are centered by the site CSS.

Validated workflow:

1. Render canonical LaTeX with MathJax SVG; export standard containers with
   source metadata and original SVG geometry.
2. On the first SVG `g`, keep `fill="currentColor" stroke="currentColor"` and
   inline `style="fill:currentColor;stroke:currentColor;"`.
3. Check inline, display, fraction and multiline formulas in light/dark browser
   fixtures at mobile width.
4. After updating the draft, read back SVG paint, containers, LaTeX and
   geometry. WeChat may strip redundant outer `color:inherit` and
   `background:transparent`; that alone is not a failure. Check for forced
   ancestor styles, then verify the actual phone reader.
5. Record phone light and dark outcomes separately. One article's acceptance
   does not transfer to other articles or devices, and does not imply
   whole-article publication readiness.

Precedent: for `ref-chen2024-JCP`, the user confirmed normal dark-mode formula
colors on 2026-10-11 at 17:15 UTC after the same-draft update at 15:23 UTC
(candidate `960ce68f3dc9777cfc9305162f55e5bcdb71fe2c`). Light mode, phone OS and
WeChat version were not separately confirmed.

## Independent RTD Full-Paper Workflow

RTD deep dives are a separate task. Follow
[paper-deep-dive-rst.md](../project/guides/paper-deep-dive-rst.md) (structure,
coverage and audit) and [rtd-translation-style.md](../project/guides/rtd-translation-style.md)
(translation quality). Missing full-paper source is a blocker; an abstract or
WeChat article cannot substitute for it.

`wechat/tools/markdown_to_rtd.py` is a historical introduction-page converter.
Use it only for explicitly requested maintenance of a legacy converted
introduction after verifying that its target is not an independent deep dive.
It is not part of new article production, and its `--check` is not a quality
gate for independent RTD pages. Do not run the converter over a full-paper page.

## Standalone account introduction

The opening article is maintained separately from journal-paper records at
[woeai-opening.md](articles/introductions/woeai-opening.md). Its existing title,
recruitment invitation, signature, links and approved illustration stay independent
of paper-title generation. Update this source before rendering its offline preview;
backend changes require the explicitly authorized existing-draft procedure and a
verified private mapping. Do not register it as a paper or create a replacement.

This is a five-section account introduction, not a paper explainer. Preserve its
approved concept-image caption and existing layout when synchronizing the local
HTML; paper-only figure/reading-guide and publication-registry checks do not apply.


## Research Families

- `结构风工程`
- `海洋能源结构`

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

### Existing draft title-prefix changes

For an explicitly authorized direction-prefix-only migration, keep the approved
cover's secondary label and all scientific body bytes. The WeChat title H1 uses
`custom.research_family`; the website's independent `custom.rtd.public_title`
does not change. Use the dedicated command, which defaults to an offline plan:

```sh
python3 wechat/tools/wechat_draft.py update-title --publication-ref <publication_ref>
# Only after explicit authorization for the existing draft title change:
python3 wechat/tools/wechat_draft.py update-title --publication-ref <publication_ref> --live
```

This command requires the existing private account binding and verified article
index, never assumes index zero, never creates a draft and never uploads images.
It accepts the exact old secondary-prefix title or the already-migrated primary
prefix with the same question. It reads the current remote article twice,
ignoring only the platform-regenerated read-only preview `url` in both comparisons;
thumbnail URLs and original links remain checked. It refuses unexpected titles
or concurrent changes, and sends the same remote body,
cover/crop and metadata with only the title changed. Read-only preview/thumbnail
URLs are omitted from the update payload. It reads back and compares every
non-title article field except the platform-generated preview URL, including
body HTML, cover IDs/URLs, crop information, author, digest and original link.

The official API provides no atomic compare-and-swap; avoid simultaneous backend
editing during the operation. A changed readback, permission error or uncertain
network outcome stops the action. Authorized live title operations now save
credential-excluded snapshots under ignored `wechat/.local/title-updates/<receipt_id>/`:
the two GET responses immediately before a write, the actual UTF-8 JSON request
body, the update response, the raw GET response after the write, and typed field
differences (including same-draft other articles). Artifacts are immutable, mode
0600, inside a mode-0700 directory, with timestamped SHA-256 entries in a private
manifest. No endpoint URL containing the API token is recorded. Credential keys,
known token values and credential-bearing URLs are redacted; the manifest marks
redactions and whether exact transport text was retained. Unparseable response
text is conservatively omitted and marked incomplete rather than risking unknown
credential leakage. Public output contains
only the receipt identifier and safe status, never raw snapshots or private URLs.

A request snapshot must succeed before sending. A known ACK is retained even if
saving its response fails; incomplete evidence, unknown changes, body HTML changes
(including whitespace), cover material/URL/crop/display changes, metadata changes
or other-article changes stop the operation. Only the existing top-level read-only
preview `url` exception remains. Evidence completeness is independent of success;
a failed verification can have a complete diagnostic record. Inspect uncertain
outcomes before any retry. Saving later snapshots does not reconstruct missing
historical inputs or retroactively certify an earlier failed update. Never substitute a normal
`update-draft`, which uploads assets and replaces the rendered body, for this
operation. A verified title update does not renew scientific review, preview or
publication status. Title/standard migrations preserve old evidence and require
separate actual non-content comparisons before adding any current evidence.

For an explicitly authorized platform-formatting run, add
`--allow-platform-formatting` to the live `update-title` command. Without that
flag the strict comparison above remains unchanged. The opt-in permits only:

- HTML `img` closing syntax (trailing whitespace/slash). The complete remaining
  raw body and parsed image attributes must be identical; no text, image URL,
  attribute, formula, SVG or other HTML cleanup is accepted.
- A changed `thumb_url` when cover material ID, crop and display configuration
  remain strictly identical, and both exact official CDN URLs return identical
  file bytes and decoded full RGBA pixels. No redirects, credentials in URLs,
  fallback protocol/host, unreadable images or unknown equivalence are accepted.

Each opt-in readback stores a separate private `platform-equivalence` proof while
retaining all original field differences. Other metadata and same-draft articles
remain strict. The title target may accept the retired primary prefix solely as
exact historical input with the same hook, account and index; generators emit
only the current registered family. New evidence never fills missing historical
snapshots or proves an earlier operation. Requests still change only the title:
remote body, including existing direction metadata, is preserved as read.

By default, the API payload sets WeChat's bottom `content_source_url` to the
current paper's RTD deep-dive page:
`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/<publication_ref>.html`.
Reader-facing links should still live in the article body instead of a body
`阅读原文` section. When the editor explicitly wants a different bottom
`阅读原文` target for one article, set `wechat_content_source_url` in that
article's review front matter; the API payload will use that value as
`content_source_url`. An explicitly blank `wechat_content_source_url` means
that article should have no bottom `阅读原文` link.

The API renderer builds optional WeChat-body related reading from verified
same-account publication records. Selection and placement follow the bundled
[writing standards](../.agents/skills/wechat-paper/references/writing-standards.md).
It emits title-text hyperlinks, not native WeChat article cards. The existing
Python `limit` parameter defaults to three and remains caller-adjustable; there
is no new hard cap, CLI flag or per-article count setting. This count applies
only to automatic end-of-article recommendations, not necessary in-text
citations/hyperlinks, and is not a WeChat platform limit. Standalone
source rendering does not inject navigation; inspect the assembled output too.

### Publication records and explicit relevance

The registry `custom.wechat.latest_published_url` stores the canonical public
permalink. A nonempty URL, a successful draft receipt, or a draft-box `url` is
not publication evidence. Register `custom.wechat.publication_record` only after
an actual publication has been checked. Its fields are:

| Field | Meaning |
| --- | --- |
| `status` | Exactly `published`, describing the actual public release |
| `url`, `title` | Verified permanent URL and the title at publication time |
| `published_at` | Actual publication date/time if known; omit when unknown, never substitute the paper year |
| `verified_at` | ISO date/time of the publication check |
| `source` | `official_published_list`, `official_publication_receipt`, or `public_article` |
| `same_account` | `true` only after ownership by this Official Account was checked |
| `evidence_path`, `evidence_sha256` | Public repository Markdown note and its SHA-256 |

The redacted evidence note contains exactly one unquoted `key: value` line for
each of `publication_ref`, `status`, `title`, `url`, `source`, `same_account`,
and `verified_at`, matching the record exactly. Include `published_at` too if
recorded. Use `status: published` and `same_account: true`; a draft receipt is
not a publication note. Other explanatory Markdown is allowed. Keep raw API responses,
account bindings and private IDs in local private operational storage. The
reader verifies the note's hash and article locators. URL syntax alone cannot
prove ownership, liveness or publication. Invalid/missing evidence is excluded
before the configured recommendation count; registry validation rejects invalid declared
publication records. An older verified release can remain linkable while its
new draft is `awaiting_review`; do not relabel draft readiness or old reviews.

For explicit relevance, `custom.wechat.related_articles` is a manually reviewed
list of objects with `publication_ref` and a nonempty `reason`. The referenced
record must exist, differ from the current article, and appear only once.
Only this list enables cross-direction recommendations, including another
subdirection in the same family. Within the same subdirection, the list's
order takes precedence over paper year; generic same-direction candidates come
next. Self-references and canonical URL duplicates are excluded before sorting
and limiting. Use one canonical permalink per actual article, including when
short and long share URLs refer to the same release.

A missing publication mapping leaves related reading empty. If the official
publication-list API rejects access, stop that check; do not broaden credentials
or substitute material/draft/preview URLs. Collect an existing publication
receipt or a confirmed public article record instead. Updating a draft does
not edit an already published page; old-article backlink changes require a
separately verified platform capability and authorization. New articles may
link to older verified releases without promising automatic reciprocal edits.
No link-data maintenance authorizes uploading, drafting, publishing or mass-send.

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
- `python3 wechat/tools/wechat_draft.py token-check` reuses an unexpired local
  cache without reading AppSecret or contacting WeChat (`access_token_cached`,
  `network_verified: false`). Without a usable cache it reads private credentials,
  requests and caches a token (`access_token_fetched`). This verifies only the
  token request, not draft API permissions. `--force-refresh` remains an explicit
  option; do not delete a cache or refresh automatically for diagnostics.
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

### Figure groups

New articles associate each paper image with its original figure number, title
and reading guide explicitly. The number after `figure` is the positive integer
from the original paper. Keep exactly three blank-line-separated paragraphs:

```markdown
::: figure 17

![论文图 17 三个波向的响应幅值算子比较](../../assets/public-safe/<publication_ref>/fig17.png)

论文图 17 三个波向的响应幅值算子比较

上排为平台运动，下排为塔底荷载和机舱加速度；横轴均为波周期。

:::
```

The image alt must exactly match the title. Preserve original subfigure labels
in both, for example `（原图子图d–f）`; do not renumber selected figures. A guide
may wrap across source lines within its one paragraph. Put scientific findings,
conditions and adjoining prose outside the block. Writing rules remain owned by
the bundled writing standards; this section owns the syntax and diagnostics.

Both explicit groups and historical image/title/guide sequences render through
one template using the existing theme's `img`, `caption_title`, and `caption_body`
styles. Historical `图N`, `Fig. N`, `Figure N`, and `论文图 N` forms are recognized
only after a standalone image with the same alt/title and a following guide
paragraph. Generic/formula images and ordinary figure references in prose are
not groups. Ambiguous historical sequences report a diagnostic instead of
silently consuming a different title or a heading as the guide.

Selected-article checks, rendering, and draft `preflight`/`dry-run` validation
report missing fields, mismatched numbers/alt, or unclosed blocks with source
line numbers. No credentials or live calls are needed for these checks. They
verify structure, not figure reuse rights, scientific meaning, old approval, or
actual WeChat phone rendering. Existing articles are not migrated automatically.

## Backlog State Model

Use `wechat/backlog/selected-papers.yml` to track selected papers and publication state.

- `repost_priority`: one of `high`, `medium`, or `low`; use higher priorities first when starting the next article.
- `wechat_status`: one of `selected`, `drafting`, `reviewing`, `ready_to_publish`, `published`, or `archived`.
- `publication_mode`: one of `first_publish`, `rewrite`, or `republish`; this records the publication intent, while `wechat_status` records workflow progress.
- `previous_published_url`: the earlier public WeChat URL, if this article is being rewritten or republished.
- `latest_published_url`: the newest public WeChat URL after publication.
- `wechat_draft_media_id` is a private backend identifier returned by the WeChat draft API. Keep its value only in ignored private operational records, never in public reviews, backlog, or registry data.
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

The step-by-step execution order lives in the
[wechat-paper skill](../.agents/skills/wechat-paper/SKILL.md). In outline:

1. Select an included paper and verify `publication_ref`, DOI and the WOEAI
   publication record.
2. Obtain and verify sources under
   [paper-sources-and-evidence.md](../project/guides/paper-sources-and-evidence.md).
3. Draft from `../.agents/skills/wechat-paper/templates/paper-explainer.md` under [writing-standards.md](../.agents/skills/wechat-paper/references/writing-standards.md), edit
   with the natural-writing guide, and record evidence in the review note.
4. Run `python3 scripts/check-wechat-content.py <article.md>` for the selected
   revised article; semantic review follows the bundled checklist. Render offline and run `preflight` / `dry-run`. Pure WeChat article/review
   work does not require a Sphinx build.
5. Backend delivery only after the explicit authorization described above;
   only a successful live operation advances state.
6. A human previews, proofreads and publishes. Apply wording corrections back
   to the WeChat Markdown; do not synchronize the abbreviated body into RTD.
7. Record the confirmed published URL and state.
