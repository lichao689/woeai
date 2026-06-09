# WOEAI Site Agent Guide

This repository is the public website for the WOEAI research group. Treat it as
a Sphinx documentation site, not as an application package.

## Outcome Priority

Use this order when deciding navigation weight and copy tradeoffs. On the
homepage, keep recruitment and engineering applications as visible conversion
paths; represent academic credibility through the opening group introduction
and factual proof pages rather than a standalone homepage section.

1. 招生 Recruitment
2. 工程应用 Engineering Applications
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
- Keep engineering-application copy scenario- and evidence-based unless named
  partners or cases are explicitly source-backed. Technical collaboration may
  remain a contact action, but should not be the primary navigation label.

## Site Structure

- `docs/source/index.rst` owns the homepage and top-level navigation.
- Recruitment content and contact information belong on `docs/source/index.rst`,
  not standalone top-level pages.
- `docs/source/EngineeringApplications.rst` should be the second conversion path.
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
| 2026-06-07 | AGENTS.md 是项目主规则源；claude.md / CLAUDE.md 供 Claude Code 使用，gemini.md / GEMINI.md 供 Gemini 使用；这些镜像文件应保留并随 AGENTS.md 全量同步，不应因为它们是新生成文件就删除。 | 全项目规则文件 | 对话 | 新增 |
| 2026-06-08 | 教学改革、思政建设类论文统一放在教育教学页面的“教改探索”小节，不进入学术成果或按研究方向浏览页面。 | WOEAI 公共网站内容分类 | 对话确认 | 新增 |
| 2026-06-08 | Zotero Web API 写权限 key 是本机私密凭据，固定存放在 `~/.config/woeai/zotero_write_api_key`；仅当用户明确要求修改 Zotero 条目时读取，用于 Web API 写入。不得打印、提交、复制到仓库，普通论文读取与页面生成仍优先使用 Zotero Desktop 本地只读 API。 | Zotero 学术成果维护 | 对话确认 | 新增 |
| 2026-06-08 | WOEAI 公众号论文文章应优先通过 Zotero Desktop Local API 获取元数据、DOI、abstractNote 和附件记录；本地 PDF 存在时直接用于摘要、图片、图注和正文证据抽取，本地 PDF 缺失时再尝试 Zotero Web API /file；仍不可获得时在 review 文档记录“需要同步 PDF 或提供作者稿”，不得编造 PDF 原文信息。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
