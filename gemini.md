# WOEAI Agent Guide

WOEAI is a public Sphinx documentation site with publication tools and a
WeChat article workflow, not an installable application package.

## Start here

1. Check `git status --short` and the target files before editing. Preserve
   unrelated work; stage only reviewed files belonging to the requested task.
2. Read [CONTEXT.md](CONTEXT.md) for project vocabulary and semantic constraints.
   Maintain it when the task changes that vocabulary. Consult relevant ADRs in
   `docs/adr/` if present, and report conflicts rather than silently replacing them.
3. Choose the task branch below. This guide is the project rule source;
   `claude.md` and `gemini.md` are full mirrors and must stay byte-identical.
   Repository guidance does not grant permission to access credentials, upload,
   create remote drafts, commit, push, or publish beyond the user's authorization.

## Repository navigation

- `docs/`: public website sources, data, and Sphinx dependencies.
- `wechat/`: article content, evidence reviews, assets, and existing workflows.
- [project/README.md](project/README.md): maintenance guides, plans, specs,
  research, and public fact sources; these are not Sphinx pages.
- `tools/`: publication command entry points; `woeai/`: shared Python logic.
- `scripts/`: setup/build/check utilities and the existing Zotero updater.
- `tests/`: regression checks. Existing tool paths are unchanged.

## Task entry points

- **Website content or navigation:** read [README.rst](README.rst),
  [the public fact source packet](project/sources/2026-06-woeai-site-source-packet.md),
  and the affected `docs/source/` pages. Use the site boundaries below.
- **WeChat article, evidence review, or backlog:** read
  [.agents/skills/wechat-paper/SKILL.md](.agents/skills/wechat-paper/SKILL.md),
  [wechat/STYLE.md](wechat/STYLE.md), [wechat/README.md](wechat/README.md),
  the article/review templates, and `wechat/backlog/selected-papers.yml`.
- **Cover generation, prompts, or crop review:** read
  [.agents/skills/wechat-cover/SKILL.md](.agents/skills/wechat-cover/SKILL.md)
  and its linked standards; follow its cover-text confirmation and preview gates.
- **RTD paper deep dive:** read
  [project/guides/paper-deep-dive-rst.md](project/guides/paper-deep-dive-rst.md),
  the original paper, and its `docs/source/Publications.rst` entry. Use the
  independent full-paper workflow below, including its coverage audit.
- **Publication generation or Python tools:** inspect `woeai/publications/`,
  `tools/publications/`, `scripts/update-publications-from-zotero.py`, and the
  relevant `tests/`. Research taxonomy belongs only in
  `woeai/publications/taxonomy.py`; author/text/citation logic belongs in
  `woeai/publications/`. Import it rather than copying it into scripts or tests.
- **Planning, tickets, or triage:** read [domain.md](project/guides/domain.md),
  [issue-tracker.md](project/guides/issue-tracker.md), and
  [triage-labels.md](project/guides/triage-labels.md). The tracker is local Markdown
  under `.scratch/<feature-slug>/`, not an assumed external service.

## Site boundaries

- Prioritize recruitment, engineering applications, then academic credibility.
  `docs/source/index.rst` owns homepage navigation, recruitment, and contacts;
  `EngineeringApplications.rst` is the second conversion path. Research,
  publications, teaching, and direction pages supply factual supporting evidence.
- Publish source-backed facts only. Unconfirmed partners, facilities, quotas,
  stipends, news, awards, metrics, and publication claims stay out of public copy.
  Track uncertainty in planning/review material rather than public placeholders.
- Teaching-reform and ideological/political-course papers belong in
  `docs/source/Teaching.rst` under “教改探索”, not the research publication list.
- Preserve stable publication anchors and `paper-notes/<publication_ref>.html`
  URLs. `Publications.rst` owns the research-family/subdirection hierarchy;
  `PublicationsByYear.rst` owns chronological browsing. Follow `CONTEXT.md` for
  citation-link scope, author markers, and sidebar structure. Do not restore a
  flat paper-note toctree or a `Journal Papers` sidebar node.
- Keep Sphinx references valid and public pages free of template residue.
  For a site release, follow README's Site Build ID procedure; a guidance-only
  edit does not require changing site release metadata.

## Paper sources and public safety

- Use the authorized source files actually available in the current workspace.
  Check ignored `wechat/.local/` sources and their manifests before requesting
  another copy; journal files may be under `journal-papers/<ZoteroKey>/source.pdf`
  or `<publication_ref>/source.pdf`. File counts and machine paths are inventory,
  not permanent project rules. A clone alone does not restore private sources.
- Verify the paper identity, source version, reuse status, and manifest before
  relying on a PDF. Keep original/source SHA-256 and downloaded-copy SHA-256
  separately labelled; a library transfer hash is not proof of byte identity to
  an original source unless both bytes have been checked.
- Use Zotero metadata/attachment records when accessible; the Desktop Local API
  requires the user's actual desktop and is not a cloud prerequisite. Missing
  source evidence is a blocker for full-paper work, never a license to invent it.
  Follow the paper skill's attachment priority and source-acquisition record.
  Zotero write credentials are only for explicitly requested Zotero item changes;
  ordinary paper reading and page generation use read-only sources and must not
  read those credentials. Handle any credential access through authorized secure
  mechanisms; never print secrets or copy them into this repository.
- Web pages can verify public metadata. Download a web PDF only from a specific,
  public, legal source explicitly approved by the user; keep it private and
  record source/approval/reuse status. Do not automatically scrape paper PDFs.
- Keep credentials and token caches outside the repository. Keep source PDFs,
  raw extraction, private manifests/IDs, preview HTML, API payloads, and private
  review material in ignored private storage.
  Commit only approved public-safe text and assets. `wechat/articles/review/`
  is public too: use storage classes and evidence locators, not private absolute
  paths, private download links, or raw paper text.
- Every article review needs `## 源文件获取记录` and
  `## 关键事实证据定位记录`. Use `PDF file page N`, original figure/equation
  numbers, and claim locations. Write `pending PDF page audit` when unaudited.
  Record contradictory numbers, citations, or equations with both locations;
  preserve the evidence and flag the discrepancy rather than silently repairing
  the original paper.

## Publication registry

`docs/data/publications.json` is the single manually maintained publication and
workflow registry (standard CSL-JSON, extension fields under `custom`). Zotero
owns upstream bibliographic facts. RTD and WeChat states/evidence are independent;
file existence, issue closure, and draft upload do not prove content verification
or publication. See [the registry guide](project/guides/publication-registry.md).
The backlog, research map, and `project/publication-progress.md` are generated
compatibility views, not additional authorities. After registry edits run
`python3 tools/publications/registry.py --write` and `--check`. Keep private draft
IDs in ignored operational storage, never the public registry.

An explicit user approval on 2026-10-07 permits the 17 existing draft mappings
in `wechat/data/draft-map.json` to be public. This is the sole exception to the
private draft-ID rule: each array item contains only `publication_ref` and
`wechat_draft_media_id`. The approved snapshot is pinned by the public-safety
checker. No account IDs, article indices, timestamps, image paths, API responses,
credentials, tokens, or other private metadata are approved for this table.
Changes to the approved records require renewed authorization. Do not copy this
table into the public registry, backlog, article/review files, or other paths.

Runtime lookup prefers ignored private records and falls back to this public
table. Missing or invalid mappings must not silently create a replacement
draft. Public records have no confirmed article index; never infer zero.
Live use requires a privately confirmed account binding and article index;
offline `update` planning alone does not verify either or authorize a live call.

## Independent channel outputs

**WeChat is a reader-facing introduction.** Its source is
`wechat/articles/draft-public-safe/<publication_ref>.md`; review and approved
assets live in the matching `wechat/articles/review/` and
`wechat/assets/public-safe/` paths. Use the author's confirmed papers, original
figures with approved reuse, faithful Chinese abstract, numbered research
questions, restrained quantitative hooks, and visible limitations. Follow the
paper skill/STYLE for author markers, captions, conclusion emphasis, and links.
Apply backend wording corrections back to this Markdown before regenerating.

**RTD is an independent full-paper deep dive.** Write
`docs/source/paper-notes/<publication_ref>.rst` directly from the approved
original paper, preserving its full body order, equations, figures, tables,
appendices, citations, and references under the deep-dive guide's rules.
Do not derive it from the WeChat introduction. `wechat/tools/markdown_to_rtd.py`
is only for explicitly requested legacy introduction-page maintenance; it must
not overwrite an independent deep dive. Existing skill/README/STYLE references
to a shared Markdown master or automatic RTD conversion are historical and are
superseded by this distinction. The same applies to old Mac-first setup advice.

RTD keeps the cover immediately below the short-WeChat-link line and retains
appendices before references while omitting the publication/declaration tail
sections listed in the deep-dive guide. Use `\qquad (N)` for manual equation
numbers, not `\tag{N}`. Complete the guide's source-to-output coverage audit.

## WeChat delivery stages

1. **Content production:** draft, evidence review, approved assets, offline
   HTML, and `dry-run`/`preflight`. These checks do not read credentials, contact
   WeChat, upload images, or create a backend draft. Verify current runtime
   availability; neither a fresh clone nor an old migration report proves it.
2. **Backend draft:** the official draft API is the automated route. Old skill
   instructions for a third-party Markdown editor/manual-copy fallback are retired;
   do not revive that workflow or make Wechatsync/browser plugins the default.
   Before a
   live create/update, explain the credential access, approved-image upload,
   and target draft operation, and obtain explicit confirmation for that action.
   API configuration and connectivity must be verified in the actual runner;
   prior-machine success is not current cloud readiness. Keep secrets outside
   the repository using the supported secure setup. A successful live operation
   may update non-sensitive backlog state; dry runs and failed calls may not.
   Update an existing draft by default; create a duplicate only when requested.
3. **Publication:** a human previews, proofreads, and publishes in the WeChat
   backend. Do not automate publish, mass-send, or browser release clicks.

Use MathJax SVG as the default WeChat formula renderer; troubleshooting fallbacks
must be labelled. Offline HTML/SVG counts, crop boards, and previous stress tests
are not acceptance of current WeChat mobile rendering. Set formula/cover preview
flags only after the actual backend preview. `ip-check` is optional diagnostics,
not a live gate; handle official API allowlist errors without bypassing controls.

## Verification and completion

Run from the repository root; inspect script help/source before adding flags.

- **All edits:** `python3 scripts/check-public-safe-content.py` and
  `git diff --check`; inspect the full diff for private material and scope.
- **Guidance:** verify linked files and commands exist; run
  `cmp AGENTS.md claude.md` and `cmp AGENTS.md gemini.md` after syncing mirrors.
- **WeChat-only text/review/assets:** check Markdown image/link paths and evidence
  records. When preparing rendered content, run
  `python3 wechat/tools/wechat_draft.py dry-run --publication-ref <publication_ref>`
  or the no-submit `preflight` equivalent. Sphinx is not required for this branch.
- **RTD/site/config/generator changes:** run `./scripts/check-docs.sh`.
  It requires Python 3.12+, checks public safety and publication artifacts,
  runs `unittest`, installs `docs/requirements.txt` in its configured temporary
  environment, and builds Sphinx HTML with warnings as errors. For affected
  Python tools, run relevant tests during development as well.
- **Commit/push when authorized:** prefer small verifiable commits; inspect
  staged scope, verify the remote commit, and report the corresponding CI result.
  Use transport supported by the current environment, not a historical machine's
  network workaround. See `.github/workflows/docs.yml` for the CI gate.

Report each check as passed, failed, blocked, or not run with the reason and
remaining impact. Dependency/network/socket/browser restrictions are observations
about the current run, not permanent product limitations. Do not bypass them or
label a reduced/diagnostic build as a successful standard gate.
