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

Follow `AGENTS.md` and `docs/agents/paper-deep-dive-rst.md`. New RTD deep dives
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
