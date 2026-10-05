# Project maintenance

This directory holds repository maintenance documentation, not public Sphinx
pages. Website sources and URLs remain under `docs/source/`; WeChat article
sources and assets remain under `wechat/`.

## Start here

- [Repository overview](../README.rst): directory map and build checks
- [Contributor guide](../AGENTS.md): task entry points, public safety, and checks
- [Project vocabulary](../CONTEXT.md): public terminology and semantic constraints
- [Domain guide](guides/domain.md): how to explore project documentation
- [Cloud WeChat workflow](guides/cloud-wechat-workflow.md): credential-free setup
- [Publication workflow registry](guides/publication-registry.md) and [generated progress](publication-progress.md): one bibliography, independent RTD/WeChat workflows
- [Paper deep-dive guide](guides/paper-deep-dive-rst.md): independent RTD articles
- [Issue tracker](guides/issue-tracker.md) and [triage labels](guides/triage-labels.md)

## Directory map

- `guides/`: current contributor and workflow guidance
- `plans/`: durable implementation plans, including historical decisions
- `specs/`: design specifications
- `research/`: benchmark and research notes
- `sources/`: public-safe factual source packets, starting with the
  [2026 website source packet](sources/2026-06-woeai-site-source-packet.md)

Historical plans record past work; the current contributor guide and source
code determine today's workflow. Structured website data belongs in
[`docs/data/`](../docs/data/), including the
[Zotero snapshot](../docs/data/2026-06-publications-zotero-snapshot.json).
This first-stage reorganization does not consolidate tool entry points or move
private/ignored material or local `.scratch/` task records.
