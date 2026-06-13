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
- `docs/source/Publications.rst`, `docs/source/Teaching.rst`, and the research
  direction pages are proof surfaces and should stay factual.

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

### WeChat cover images

Use `.agents/skills/wechat-cover/SKILL.md` when generating, improving,
reviewing, or recording WOEAI WeChat Official Account cover images.

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
| 2026-06-10 | WOEAI 公众号论文文章默认不从出版社页面、DOI 落地页、Google Scholar、ResearchGate、Sci-Hub、搜索结果或其他普通网页自动抓取/下载 PDF；网页只可用于核对公开元数据。只有用户明确批准某个具体、公开且合法的 PDF 来源（如 OA PDF、作者公开稿或用户提供下载链接）时才可下载，且下载文件必须放在 `wechat/.local/<publication_ref>/` 等忽略的本地私有目录，不得提交到公开仓库，并在 review note 记录来源、批准和复用状态。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-10 | 每篇 WOEAI 公众号论文文章的 review note 必须包含 public-safe 的“源文件获取记录”，至少记录 Zotero key、元数据来源、附件记录状态、本地 PDF 状态、PDF 来源类型、私有存放类型、Zotero Web API `/file` 是否尝试、是否使用网页 PDF 下载、摘要依据、正文证据依据和图片依据；不得记录本机绝对私有路径、凭据、cookie、原始 API payload 或下载 PDF 正文内容。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-10 | 当 Zotero 条目存在多个 PDF 类附件时，WOEAI 公众号论文文章用于正文证据和图片抽取的 PDF 优先级为：作者最终稿/作者稿、出版商正式版 PDF、OA 平台 PDF、预印本、其他附件。若使用低优先级附件，review note 必须说明高优先级来源缺失、不可读、版权不安全或视觉不适合等原因；期刊、年份、卷期页、DOI 和发表状态仍以 Zotero 元数据和正式发表记录为准，不由预印本等低优先级 PDF 覆盖。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-10 | 每篇 WOEAI 公众号论文文章的 review note 必须包含 public-safe 的“关键事实证据定位记录”。不要求逐句标页码，但必须覆盖摘要、核心结论、关键图和关键公式；关键图优先记录 PDF 文件页码与原始图号，关键公式若来自论文则记录 PDF 文件页码与公式编号，若为公众号解释性公式则标明为 editorial explanatory formula 并指向其解释的论文证据。未完成页码审计时写 `pending PDF page audit`，不得猜测页码，也不得记录本机绝对私有路径或大段复制 PDF 原文。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-10 | WOEAI 公众号论文文章的证据定位页码统一使用 PDF 文件页码，写作 `PDF file page N`；不得使用论文印刷页码、期刊页码或文章正文分页作为 review note 的证据定位页码。该口径与本地 PDF 渲染、截图、抽图和复核流程一致。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-10 | `scripts/check-public-safe-content.py` 必须自动检查 `wechat/articles/review/*.review.md`；任何 review note 缺少 `## 源文件获取记录` 或 `## 关键事实证据定位记录` 时都应失败，不能只依赖人工复核发现。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-10 | `wechat/tools/wechat_draft.py dry-run`、`preflight`、`create-draft` 和 `update-draft` 必须在读取微信凭据、上传图片或调用微信草稿 API 前，对目标公众号正文和 review note 运行公开安全检查；若缺少必填 review note 小节或发现公开安全问题，必须停止。 | WOEAI 公众号自动化发布流程 | 对话确认 | 新增 |
| 2026-06-09 | WOEAI 公众号自动化流程只能创建或更新微信公众号草稿；不得自动发布、群发或通过浏览器自动点击发布。最终发布必须由人工在微信公众号后台预览、校对并确认。 | WOEAI 公众号自动化发布流程 | 对话确认 | 新增 |
| 2026-06-11 | WOEAI 公众号自动化主线采用官方微信公众号草稿 API；不再维护第三方 Markdown 编辑器手工复制兜底路径，Wechatsync 或浏览器插件不作为默认主线或内容事实源。 | WOEAI 公众号自动化发布流程 | 对话确认 | 更新 |
| 2026-06-09 | 微信公众号 API 凭据仅放在本机私密配置：AppID/AppSecret 存于 `~/.config/woeai/wechat_official_account.env`，`access_token` 缓存于 `~/.cache/woeai/wechat_access_token.json`；仓库不得提交、打印、记录或复制这些内容，只有用户明确要求测试 API 或创建/更新草稿时才读取。 | WOEAI 公众号自动化发布流程 | 对话确认 | 新增 |
| 2026-06-09 | 微信公众号 API 工具默认只做不提交检查；真实创建或更新公众号草稿前，agent 必须说明将读取私密凭据、上传已批准图片并在微信后台生成/更新草稿，且必须等用户明确确认“创建公众号草稿”后才可执行 live 命令。`继续`、`可以`、`试试` 等模糊回复不足以授权 live。 | WOEAI 公众号自动化发布流程 | 对话确认 | 新增 |
| 2026-06-09 | 微信公众号 live 创建/更新草稿成功后，工具应自动把非敏感状态写回 `wechat/backlog/selected-papers.yml`：`wechat_status: ready_to_publish`、`wechat_draft_media_id`、`wechat_draft_created_at`、`wechat_draft_updated_at`。失败或仅 dry-run 时不得推进状态。 | WOEAI 公众号自动化发布流程 | 对话确认 | 新增 |
| 2026-06-09 | 微信公众号 live 提交时，如果 backlog 没有 `wechat_draft_media_id`，默认新建草稿；如果已有 `wechat_draft_media_id`，默认更新该草稿。只有用户明确要求“新建一份草稿”时才另建新草稿。 | WOEAI 公众号自动化发布流程 | 对话确认 | 新增 |
| 2026-06-10 | WOEAI 公众号论文文章的“论文信息”作者行必须与 RTD 学术成果作者标记语义一致：仅学生第一作者使用下划线标记，通讯作者姓名后使用 `*` 星标，不写 `(corresponding author)`；Markdown 公共正文中可用 `<u>学生第一作者</u>` 表示该标记，RTD 转换为 `:student-first-author:`，微信公众号 HTML 必须显示为下划线且 `\*` 必须显示为普通星号。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-11 | WOEAI 公众号论文文章不再保留“英文摘要”段：Markdown 母版、微信正文和 RTD 页都只保留由原文摘要忠实翻译的中文摘要；中文摘要可按语义拆分为 2–3 段（忠实翻译要求不变，仅排版分段）。`scripts/check-public-safe-content.py` 应禁止公开正文出现 `**英文摘要**`。 | WOEAI 公众号论文文章 | 对话确认 | 更新 |
| 2026-06-10 | WOEAI 公众号论文文章“论文信息”只保留论文题名、作者、期刊、年份、DOI 和 WOEAI 相关方向；卷、期、页码或文章号属于完整文献引用信息，不再单列 `卷期页码`。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-10 | WOEAI 公众号论文文章的微信公众号草稿作者字段默认使用该期刊论文第一作者；论文作者列表仍保留在正文“论文信息”中。已有 review note 若仍写 `wechat_author: WOEAI`，工具应优先从正文作者行解析第一作者作为草稿作者。 | WOEAI 公众号自动化发布流程 | 对话确认 | 更新 |
| 2026-06-09 | WOEAI 公众号文章和微信草稿 API payload 中的 WOEAI 官网外链优先使用 `https://woeai.readthedocs.io/zh-cn/latest/`；读者侧链接统一放入“延伸阅读”，使用直接超链接，不再单列“阅读原文”，也不重复放置与正文内容一致的 WOEAI 论文条目锚点。`winddee.cn` 可作为网站自身 canonical/联系方式，但不作为公众号内容默认硬编码域名。 | WOEAI 公众号自动化发布流程 | 对话确认 | 新增 |
| 2026-06-11 | 微信草稿 API 的 `content_source_url` 默认使用当前论文对应的 RTD 解读页：`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/<publication_ref>.html`；只有用户针对某篇文章明确选择其他阅读原文目标或明确要求留空时，才在发布说明 front matter 写入 `wechat_content_source_url` 覆盖默认值。 | WOEAI 公众号自动化发布流程 | 对话确认 | 更新 |
| 2026-06-11 | WOEAI 公众号论文文章的正文图片说明采用两行结构：第一行用中文图名，由论文原英文图名忠实翻译而来，并以“论文图 N”标注论文原始图号（例如“论文图 21 气象自动站的位置与观测环境”），alt 文本与图名行一致；第二行另起中文解释说明，只写读者看图时需要的信息（读图顺序、颜色或线型含义、应关注的区域等），不复述正文主旨。图名在微信正文中居中显示，使用比正文小一号的斜体样式；图名和说明文字都应与正文显著区分。 | WOEAI 公众号论文文章 | 对话确认 | 更新 |
| 2026-06-09 | WOEAI 公众号论文文章中的数学变量、文字性下标和单位应保持 LaTeX 语义；文字性下标优先使用 `\mathrm{...}`，例如 `$H_{\mathrm{max}}$`、`$K_{\mathrm{CFD}}$`。当前 `render-copy-ready.py` 的公式输出是轻量 HTML 近似渲染，不是完整 LaTeX 排版；正式发布前必须在微信后台手机预览中确认公式观感，后续应优先改进为真正的数学排版渲染链路。 | WOEAI 公众号论文文章 | 对话确认 | 更新 |
| 2026-06-10 | WOEAI 公众号论文文章的公式渲染优先采用 Markdown LaTeX 源码到 MathJax SVG 的预渲染路线，即提交前生成 `<mjx-container jax="SVG">...<svg>...</svg></mjx-container>`；微信端不运行 MathJax/KaTeX 脚本。轻量 HTML 只作简单公式兜底，PNG 公式只在 SVG 预览不可用时作为兜底。正式发布前仍必须以微信公众号后台手机预览为准。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-10 | WOEAI 公众号公式单篇压力测试已确认：官方 `draft/add` 可接受约 113k 字符、包含多组行内与展示 MathJax SVG 公式的单篇正文，用户确认预览效果满意。后续 `render-copy-ready.py` 和 `wechat_draft.py` 默认公式渲染器改为 `mathjax-svg`；`lightweight` 仅作排障或缺少 MathJax SVG 运行时的兜底。SVG 容器应尽量保留 `data-formula` 与 `data-formula-type` 元信息。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-10 | WOEAI 公众号正文中的展示公式应在独立公式块中视觉居中，保留 `data-formula` 元信息并允许宽公式横向滚动。微信底部“阅读原文”由 API `content_source_url` 控制，不是正文“延伸阅读”小节；默认使用当前论文对应的 RTD 解读页，只有用户明确指定其他目标或留空时才在发布说明 front matter 中写入 `wechat_content_source_url` 覆盖默认值并提交。 | WOEAI 公众号论文文章 | 对话确认 | 更新 |
| 2026-06-10 | WOEAI 公众号论文文章固定采用“Markdown 公共正文母版 -> RTD RST -> 微信草稿”的同步顺序。正文措辞、公式、图注和正文链接先在 `wechat/articles/draft-public-safe/*.md` 对齐，再转换到 `docs/source/paper-notes/*.rst` 并由同一 Markdown 渲染微信草稿；微信后台预览若产生正文修改，必须先反向录回 Markdown，再重新生成 RST 和草稿。RTD 展示公式也应通过站点 CSS 保持居中。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-11 | WOEAI 公众号论文文章的正式 Markdown 到 RTD 转换脚本为 `wechat/tools/markdown_to_rtd.py`；生成命令为 `python3 wechat/tools/markdown_to_rtd.py --publication-ref <publication_ref>`，同步检查命令为同命令追加 `--check`。RTD 顶部封面图由 review note 的 `rtd_cover_image` / `wechat_cover_image` / `cover_image` 或“封面素材”记录提供，插在标题下方；RTD 正文图使用两行图注并由站点 CSS 将中文图名显示为居中、小一号、斜体，说明文字另起一行。转换时的 RTD 渠道适配：页标题与“相关论文解读”链接文字去掉“数值风洞/结构抗风/漂浮风电 \|”分类前缀（仅 RTD 端）；识别 “点击阅读原文” 锚点并跳过微信固定结尾块；正文后追加“完整引用”小节（取自 `docs/source/Publications.rst` 对应锚点条目并截到 DOI 为止，不含影响因子与分区，附学术成果页锚点链接），再接内部“相关论文解读”导航。 | WOEAI 公众号论文文章 | 对话确认 | 更新 |
| 2026-06-09 | WOEAI 微信公众号 API 第一次实操从当前 Mac 本机运行；长期云端/CI 自动化待首轮本机 API 链路跑通后再设计。本机实操需要将当前公网出口 IP 配置到公众号后台 IP 白名单。 | WOEAI 公众号自动化发布流程 | 对话确认 | 新增 |
| 2026-06-10 | WOEAI 微信公众号 API 的本地公网 IP 探测不再作为 live 创建/更新草稿前的硬性守门，因为该探测结果可能与微信 API 实际链路不一致。`wechat_draft.py ip-check` 仅保留为人工诊断命令；live 创建/更新应直接调用微信官方 API，并以微信 API 返回的白名单错误作为后续处理依据。 | WOEAI 公众号自动化发布流程 | 对话确认 | 更新 |
| 2026-06-11 | WOEAI 公众号论文文章的表达规范：开头策略多样化（现实矛盾式、反常识式、具体数字式、场景式，相邻文章错开）；论文有可引用数字时在开头一两段放量化钩子，无证据不编造，缺数字时在 review note 记待确认项；每个“关键发现”小节恰好加粗一句结论句作为扫读路径，其余加粗保持克制；叙述人称统一为“我们”（研究动作与决策），引用具体数值结果时可写“论文中给出的结果”；“研究问题”使用编号列表，“关键发现”各小节首句回扣对应问题（例如“针对问题 1，……”）。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-11 | WOEAI 公众号论文文章在“延伸阅读”前固定加入一句结尾块：“如果你对建筑结构抗风 / 海上漂浮风电方向的研究生学习或工程合作感兴趣，点击阅读原文查看本文网页版，并从 WOEAI 主页了解更多。”该句与微信底部“阅读原文”默认指向本文 RTD 解读页的规则配套；该句为微信渠道专属，`markdown_to_rtd.py` 以“点击阅读原文”为锚点识别并跳过该段，RTD 页不放结尾块。 | WOEAI 公众号论文文章 | 对话确认 | 新增 |
| 2026-06-14 | WOEAI 研究方向分类（Research Family / Subdirection）的唯一源是 `woeai/publications/taxonomy.py` 的 `RESEARCH_FAMILY_ORDER` 与 `RESEARCH_SUBDIRECTION_ORDER`；出版物纯计算逻辑（作者名归一、学生一作与通讯作者检测、引用渲染）的唯一源是 `woeai/publications/`（`textutils.py` / `authors.py` / `rendering.py`）。禁止在 `scripts/`、`tools/`、`tests/` 或其他 Python 文件中重新定义这些常量或复制这些逻辑；需要时从 `woeai.publications` 导入。`scripts/update-publications-from-zotero.py` 与 `tools/publications/artifacts.py` 通过重新导出（re-export）保持各自公开面，不等于允许在别处重新定义。 | 全项目 Python 代码 | 架构深化计划 | 新增 |
| 2026-06-14 | 推送 WOEAI 仓库到 GitHub 时，HTTPS（443 端口）在本机网络下经常超时阻断；SSH（22 端口）畅通且已配置认证。当 `git push origin main`（HTTPS）超时失败时，改用 SSH 推送：`git push git@github.com:lichao689/woeai.git main`。该规则仅适用于本机当前网络环境，若日后 HTTPS 恢复正常可移除。 | Git 运维 | 实测确认 | 新增 |
