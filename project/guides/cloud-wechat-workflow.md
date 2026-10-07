# Credential-free cloud WeChat workflow

This configuration was rebuilt on 2026-10-02 from the current public checkout
and fresh dependency resolution. It is not a byte-for-byte restoration of the
lost uncommitted configuration. The checkout is a working copy, not a durable
backup or a promise of fixed egress. Keep authorized source PDFs in private
Library and use Git for approved public source changes.

## Setup and repeatable local checks

Prerequisites: Git, Python 3.12+, Node 20+, npm. Chinese preview fonts should
include Noto Sans CJK SC / Noto Serif CJK SC; PDF inspection uses Poppler
(`pdfinfo`, `pdftotext`, `pdftoppm`, `pdfimages`). Install missing prerequisites
from official OS/vendor sources. They are not bundled in this repository.

From the repository root:

```bash
./scripts/setup-cloud-workflow.sh
source scripts/cloud-workflow-env.sh
./scripts/check-cloud-workflow.sh
```

Setup contacts the Python/npm registries. After setup, the smoke check renders
existing public assets locally, without credentials, WeChat calls or uploads.
Check outputs are ignored under `wechat/.local/cloud-check/`; the cover HTML
board is under `wechat/.local/cover-previews/`. The sample is
`ref-zhao2026-BS`: formulas pre-rendered to MathJax SVG, embedded body images,
and a separately validated cover (the official draft API uses a cover field).

Runtime isolation:

- Python packages in `.venv`; all resolved versions in
  `wechat/runtime/requirements.lock.txt`
- npm package closure and integrity hashes in
  `wechat/runtime/package-lock.json`; installed modules ignored
- MathJax 3.2.2 matches the renderer's current `mathjax-full/js/...` imports.
  It is deprecated upstream in favor of MathJax 4; a major upgrade is a separate
  tested renderer change. `@xmldom/xmldom` is explicitly overridden to 0.9.12
  rather than the warned-about 0.9.10 transitive resolution.
- Python lock is version-pinned, not hash-pinned; OS, Python and Node are
  prerequisites rather than a fully hermetic environment.

When changing dependencies, resolve in a clean environment, update the locks,
replay setup, and run the smoke check. Keep `docs/requirements.txt` compatible
with the Python lock. Do not replace locks with guesses from an old report.

## Content sources and channel rules

- WeChat short guide: `wechat/articles/draft-public-safe/<ref>.md`
- Independent full-paper RTD deep dive: `docs/source/paper-notes/<ref>.rst`
- Evidence/review: `wechat/articles/review/<ref>.review.md`
- Approved public assets: `wechat/assets/public-safe/<ref>/`

Follow `AGENTS.md` and `project/guides/paper-deep-dive-rst.md`. New RTD deep dives
must not be regenerated from the shorter WeChat Markdown. The old
`markdown_to_rtd.py` is only for historical guide-page maintenance. Official
WeChat draft APIs are the submission path; no third-party editor fallback is
maintained. Successful rendering is not scientific fact verification, renewed
image-reuse approval, or WeChat backend mobile preview.

## Private PDFs and recovery

Keep materialized PDFs under ignored `wechat/.local/`. A local
`journal-papers/cloud-ingestion-manifest.json` can map Zotero keys, DOI and title
to actual local paths. Treat its `source_pdf_sha256` (original Mac copy) and
`library_download_sha256` (downloaded Library copy) as distinct: provenance
metadata may change a PDF's bytes. Check actual hashes, PDF parsing/page counts
and the appropriate visual evidence; do not claim all files are byte-identical.
Never commit this private inventory, extracted full text, PDFs or page images.

On an environment replacement, check surviving authorized working files first,
then materialize missing files using the supported Library route. Preserve
incoming source variants and compare them with their base and current main
before applying edits. A historical status report does not recreate scripts,
locks or installed packages. Rebuild and recheck anything that was not saved.

## Acceptance limits and stage-two gate

For Sphinx source/config changes, `./scripts/check-docs.sh` remains the required
full gate. A cloud restriction may deny the local multiprocessing socket used
by `sphinx_sitemap`. Report that blocker without bypassing the restriction or
weakening the gate. A diagnostic content-only build, if separately permitted,
does not satisfy the full gate. Browser screenshots and phone preview remain
separate checks; no render success implies that they happened.

`config-check` reads private credential configuration; `token-check` uses
credentials and contacts WeChat; `ip-check` contacts an external service. None
belongs in the offline smoke check. Secure credential setup, actual API/egress
verification and a named create/update-draft action require the applicable
explicit authorization. Never auto-publish, mass-send or configure credentials
as part of stage-one setup. No live operation is performed by these scripts.

## Private account configuration and delivery limits

The optional `wechat/.local/account.json` is ignored by Git. It requires
`app_id` (the account's `wx` plus 16 hexadecimal characters) and
`credential_source` (`legacy-file` or `network-secret`), and optionally accepts
`public_draft_mapping_app_id` for a confirmed binding of the approved public
draft table to its account. Keep actual account IDs
and all unapproved draft metadata private; never put AppSecret, tokens or extra fields in this
file. No real account example belongs in the public repository.

`python wechat/tools/wechat_draft.py account-check` validates only this nonsecret
configuration. It prints presence/source status, without displaying the AppID,
reading credentials or contacting WeChat. Missing configuration preserves the
legacy-file behavior; an existing malformed file fails rather than falling back.

`legacy-file` retains the external credential file at
`~/.config/woeai/wechat_official_account.env`. AppID may come from `account.json`;
if also present in the credential file it must match. `config-check` still reads
that private credential file and requires the corresponding authorization.
It reports unknown-key counts, never their arbitrary names. Account selection
also prevents reuse of a token cache belonging to another account; a legacy
cache without account identity is refreshed when an explicit account is set.

The supported file route is a manual setup on an explicitly authorized runner:
the account owner provisions that external file through an approved secure
channel, with owner-only access (0600). This workflow does not provision it,
copy Mac credentials, or turn a direct environment variable into a protected
secret. Without an approved credential route, keep producing offline content;
the account owner can separately manage drafts and publication manually.
Backend browser access by an agent is not an alternative credential route.

`network-secret` is a reserved, **unverified and disabled** source. Selecting it
blocks credential checks and token acquisition before any credential/environment
secret or token cache is read, including when a cached token exists. There is no
raw-environment fallback or invented placeholder syntax. The interface does not
claim that Personal vault is connected.

The [official cloud environment documentation](https://learn.chatgpt.com/docs/environments/cloud-environments)
distinguishes direct environment values from proxy-substituted Network secrets
for allowed HTTPS services on port 443. It does not establish this client's
compatibility with WeChat's query parameters, URL encoding, or returned access
tokens. Enabling that route requires separate verification of all three, the
actual allowed destination and egress, and explicit authorization for live tests.
Never supply an AppSecret in chat or assume an ordinary environment value has
proxy protection.

Private draft overrides belong in `wechat/.local/registry-drafts.json`, mapping each
`ref-...` to an object with `media_id` and optional `created_at` / `updated_at`
strings, an optional confirmed nonnegative integer `article_index`, and an
optional private `app_id` binding. The legacy key `wechat_draft_media_id` is accepted; if both ID keys are
present they must agree. Unknown fields are rejected before use or writeback.
Restore only authorized nonsecret mapping data, retain existing records, and
keep the file private (0600). Do not fabricate IDs or create replacement drafts
to compensate for a missing mapping. Successful writes keep the mapping out of
the public registry and generated backlog. Legacy private records retain the
existing index-zero convention only for references outside the approved public
table. Private overrides of any approved public reference must confirm an index;
copying an ID into private storage does not confirm zero.

The user's 2026-10-07 exception authorizes only the 17-record public array in
`wechat/data/draft-map.json`, with exactly `publication_ref` and
`wechat_draft_media_id` per item. The safety checker pins the approved file's
SHA-256; even changes at that path need renewed approval and a reviewed digest
update. All other backend data remains private. The runtime validates registered
references, unique refs/IDs and the exact schema. Private records override the
public table; corrupt private overrides fail instead of silently selecting a
different draft.

The public source has no confirmed article indices. Its dry-run reports
`action: update`, `article_index: null`, and `article_index_verified: false`;
it never guesses zero. Before live use, the account owner must confirm the
target article index and place it in an ignored private override with the same
draft ID and the account's private `app_id`. Public-source use (including an
unbound private override for a public ref) also requires
`public_draft_mapping_app_id` to match the selected `app_id`. Mismatches and
unknown indices stop before credentials or networking. A successful writeback
preserves the selected index and private account binding. Migration and local
lookup do not verify remote existence, current contents, account membership,
or permission to update; Network secret remains disabled as described above.

CLI failures use allowlisted diagnostic fields instead of raw exceptions or API
responses. `wechat_rejected_ip` is emitted only for an integer 40164 with a complete
recognized allowlist message and valid, consistent IP addresses; an unrecognized
message still fails without exposing it. A token-check cache hit reports
`network_verified: false`; a successful token request reports `true` for that
invocation only. Neither certifies future connectivity or draft permissions.

`dry-run` and `preflight` validate content/assets and list planned actions; they
do not render final HTML. Run the renderer or offline smoke script separately
for actual MathJax/image rendering. No offline result certifies mobile preview,
WeChat authorization, IP allowlisting, or successful draft delivery.
