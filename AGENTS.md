# WOEAI Site Agent Guide

This repository is the public website for the WOEAI research group. Treat it as
a Sphinx documentation site, not as an application package.

## Outcome Priority

Use this order when deciding navigation weight and copy tradeoffs. On the
homepage, keep recruitment and technical collaboration as visible conversion
paths; represent academic credibility through the opening group introduction
and factual proof pages rather than a standalone homepage section.

1. 招生 Recruitment
2. 技术合作 Technical Collaboration
3. 学术可信度 Academic Credibility

## Required Checks

Run this before claiming a site change is complete:

```bash
./scripts/check-docs.sh
```

The script installs only `docs/requirements.txt` into a temporary virtual
environment and builds HTML with Sphinx warnings treated as failures.

## Content Boundaries

- Do not invent partner names, lab facilities, admission quotas, stipend
  amounts, dated news, media coverage, awards, or publication claims.
- For public facts, start from
  `docs/superpowers/source-packets/2026-06-woeai-site-source-packet.md` and the
  existing source pages under `docs/source/`.
- Unknown facts should be written as "to be confirmed" in planning documents,
  not published as definite public claims.
- Keep recruitment copy direct and useful. It may explain research directions,
  expected backgrounds, contact path, and application materials when those are
  source-supported.
- Keep technical collaboration copy capability-based unless named partners or
  cases are explicitly source-backed.

## Site Structure

- `docs/source/index.rst` owns the homepage and top-level navigation.
- Recruitment content and contact information belong on `docs/source/index.rst`,
  not standalone top-level pages.
- `docs/source/TechnicalCollaboration.rst` should be the second conversion path.
- `docs/source/Research.rst` should connect research themes to direction pages
  and academic outputs.
- `docs/source/People.rst`, `docs/source/Projects.rst`, and
  `docs/source/Publications.rst` are proof pages and should stay factual.

## Editing Notes

- Prefer small, independently verifiable commits.
- Keep Sphinx references valid; broken anchors become release blockers.
- Keep template residue out of the public site.
- Do not add Python package metadata unless the repository intentionally becomes
  an installable package in a future plan.

## Agent skills

### Issue tracker

Issues and PRDs are tracked as local markdown files under
`.scratch/<feature-slug>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

The repo uses the default five triage states: `needs-triage`, `needs-info`,
`ready-for-agent`, `ready-for-human`, and `wontfix`. See
`docs/agents/triage-labels.md`.

### Domain docs

This is a single-context docs-site repo. See `docs/agents/domain.md`.

### WeChat paper articles

Use `.agents/skills/wechat-paper/SKILL.md` when generating, reviewing, or
tracking WeChat Official Account articles from WOEAI journal papers.

## 动态更新规则

| 日期 | 规则 | 适用范围 | 来源 | 备注 |
|---|---|---|---|---|
| 2026-06-07 | 后续 agents 可以读取、维护并修改根目录的 `CONTEXT.md`，把它作为 WOEAI 公共网站的项目词汇表与语义约束来源。 | 全项目 | 对话 | 新增 |
| 2026-06-07 | WOEAI 公众号论文文章只面向作者本人论文；生成公众号正文时，可以直接使用该论文 PDF 中的原始图片，并应优先将 PDF 图片抽取为公众号正文图片，而不是只记录待插图计划。 | WOEAI 公众号论文文章 | 对话 | 新增 |
| 2026-06-07 | 纯公众号正文与 review 文档更新不属于 Sphinx 页面变更；使用 wechat-paper 技能时，不把 `./scripts/check-docs.sh` 作为必跑项，只需运行公开安全、Markdown/路径检查和必要的图片存在性检查。只有同时修改 Sphinx 站点页面、配置或生成脚本时，才运行 docs 检查。 | WOEAI 公众号论文文章 | 对话 | 新增 |
