# 论文清单与两个独立工作流

## 唯一手工状态源

`docs/data/publications.json` 是 CSL-JSON 数组，每篇论文一条。`id` 是稳定的
Zotero item key，`custom.publication_ref` 保持现有 RTD anchor 与 URL。
Zotero 继续是题名、作者、DOI 等书目信息的上游；更新器只合并书目字段，
不覆盖 `custom` 工作流、核验历史或 issue 链接，也不因一次刷新缺项而删除旧记录。
新增论文先在清单登记稳定标识和科研分类，然后运行 Zotero 更新器。

旧快照只有作者显示字符串，迁移不把它猜拆为 CSL 作者，也不从排版引文猜卷、期、页。
可靠的旧值完整保存在 `custom.legacy_bibliography`；后续 Zotero 结构化作者可写入 `author`。
旧 snapshot 仅保留历史证据，不再作为制作进度源。

以下文件全部自动生成，不手工编辑：

- `wechat/backlog/selected-papers.yml`：17 篇已选文章的兼容读取视图
- `docs/data/publication-research-map.json`：全部论文的科研分类视图
- [论文制作进度](../publication-progress.md)：全量可点击清单，含两个渠道的 issue 链接

```sh
python3 tools/publications/registry.py --write
python3 tools/publications/registry.py --check
```

检查命令使用 vendored 官方 CSL schema（安装 `docs/requirements.txt`），另检查工作流、
证据、issue URL 和生成视图一致性。`scripts/check-docs.sh` 已包含此门禁。

## 状态与证据

`custom.rtd` 与 `custom.wechat` 独立。RTD 不要求已选公众号文章；公众号草稿也不证明
RTD 完整。`unregistered` 只表示未登记，绝不等于没有开始。

- RTD：`unregistered` / `planned` / `drafting` / `awaiting_audit` / `verified` / `blocked`
- 微信：`unregistered` / `planned` / `drafting` / `awaiting_review` / `draft_created` /
  `ready_to_publish` / `published` / `blocked`

RTD `kind` 单独区分 `legacy_intro`、`full_paper`、`unregistered`。
文件存在只说明可访问，`full_paper` 只表示全文型页面；都不是全文核验通过。
2026-10-05 迁移覆盖 75 篇：14 篇旧导读、3 篇全文型页面均待原 PDF 覆盖核验；
58 篇未登记。17 篇旧 `ready_to_publish` 只按历史 API 草稿记录登记为 `draft_created`，
没有确认手机预览或发布 URL；9 组 backlog/review 时间冲突原样记录在 `conflicts`，待核对。

以上为迁移日历史基线，并非永久状态。本轮17篇、371页来源审校见
[审校记录](../research/2026-10-05-existing-paper-source-audit.md)。只有Chen2024-POF达到RTD完整覆盖；
其余缺口保留。公众号当前改稿回到`awaiting_review`，不继承旧版本上传/预览状态。

2026-10-06 第一批全文重建后，Chen2022-JWEIA、Li2024-POF 和 Zhao2026-BE 新通过独立全文与原图覆盖审校；
见[第一批记录](../research/2026-10-06-full-paper-completion-batch-01.md)。其他篇目的状态继续按当前清单和各自证据判断。

Review 文件提供事实证据，不能以其中的旧 front matter 状态覆盖清单。
历史记录保存在 `legacy_backlog` / `historical_draft_evidence`，不视为当前版本核验。
确认冲突时保留原始双方值并补充解决依据，不静默删除或覆盖。

核验完成时记录：

1. `custom.source.status = verified` 和实际核验的获授权论文副本 `sha256`（不存 PDF 私有路径）
2. 渠道 `evidence.verified` 的 `recorded_at`、公开安全的 `review_path`、逐项 `checks`
3. `workflow_fingerprint(record, channel, root)` 输出的 `fingerprint`

`sha256_scope=current_audited_copy`标明当前审查字节，另存`historical_original_sha256`及匹配情况；
不同副本不宣称原始字节等价。附录来源记录在 `source.supplements`：每份具有唯一 `id`、
题名、页数、`verified` 状态、当前核验副本 SHA-256 和 `sha256_scope=current_audited_copy`。
整个来源对象进入渠道指纹；替换附录哈希、身份或页数都会使既有核验失效，
已登记附录的身份字段缺失或无效时不能通过核验。`source_audit`记录阅读页数与视觉范围。未完成渠道可以在
`awaiting_audit`/`awaiting_review`记录当前阶段指纹，但不会升级为完整验收；未做手机预览不填通过。

RTD 必须有 `source_identity`、`full_paper_coverage`、`public_safety` 全为 true。
微信必须有 `source_identity`、`facts`、`public_safety`、`formula_preview`、`figure_preview`、
`cover_preview` 全为 true；预览项必须来自实际后台预览。Review 应记录核验人、来源定位、
覆盖范围、差异和结论。写好 review 后再计算指纹。没有实际核验不得机械填 true。

指纹包含 CSL 书目、源文件身份/哈希、渠道正文、review、渠道规范、正文实际引用的图片/include 文件和该论文公开资产的字节，
不包含状态、issue、时间和指纹本身，避免 commit 自引用。正文、来源、资产或 review 改动后，
旧证据保留但不再生效，检查失败且进度页标出失效；重核验，或把当前状态退回待核验/待审核。
Zotero 更新可保留旧核验记录，不能把旧证据自动刷新为当前。
`published` 还须有 `https://mp.weixin.qq.com/s...` 公开链接；草稿上传成功不是发布。

源文通讯作者纠正保存在`custom.bibliography_audit`，包含旧值、支持值和页码证据。
Zotero更新器在清单/页面/快照写入前核对；缺失或冲突的作者/标记会停止刷新。
它不修改远端Zotero，也不静默替换入站元数据，须先核对上游再继续。

## 微信后台操作边界

预检、dry-run 和失败操作不写清单。只有获授权且真实成功的官方草稿 create/update，
才写 `draft_created`、成功时间和提交前内容指纹；真实移动端预览与人工发布仍独立。
不要复制 token、API 原响应、私有 PDF 路径进清单。

草稿 media ID 是操作定位符，不是公开核验依据。新操作将它写到忽略的
`wechat/.local/registry-drafts.json`，权限为 0600；公开清单和新生成 backlog 不含它。
用户于 2026-10-07 单独批准 `wechat/data/draft-map.json` 中现有 17 条
`publication_ref` / `wechat_draft_media_id` 两字段对应表公开；这是唯一的
草稿 ID 公开例外，由公开安全检查器固定已审批快照。该表只作私有记录缺失时
的运行时兜底，不回填本清单或 backlog，不包含 AppID、索引、时间戳或其他
私有元数据。源记录没有确认文章索引，不能推断为 0；实时操作前须在忽略的
私有配置中确认账号绑定及目标索引。详见 `cloud-wechat-workflow.md`。
一次性迁移保留了当前 backlog 中的 ID 于该私有映射，没有修改既有 review 历史。
更换执行环境时需经批准安全迁移私有覆盖；普通 clone 不携带私有文件，
但会携带上述获批公共对应表。
迁移前提交 `86ca48340d227c27310848dece61cfa28c3253c7` 的 backlog
及既有 review 可供人工恢复定位，但旧 ID 或旧时间不证明后台当前状态；
不要为恢复映射自动创建重复草稿。现有公开历史未在本次改写或抹除。

## 与 GitHub Issues 配合

每个渠道的 `issues` 是可选 GitHub issue URL 数组，支持一个任务关联多个 issue。
例如 RTD 补全文核验和微信手机预览分别建任务，标题可用：

- `[全文精解][ref-...] 补齐正文与覆盖核验`
- `[公众号][ref-...] 完成手机预览`

Issue 放 DOI / Zotero key / publication_ref、正文和 review 路径、当前缺口及验收清单。
讨论、负责人、优先级在 issue；论文事实和验收状态在仓库清单。一次提交同时更新正文、
清单与证据，再按实际验收关闭 issue。关闭不自动等于 verified；取消不等于完成；
草稿创建不等于 published。无后台同步、无自动建 issue、无凭据或网络依赖。

本次只实现可选链接与生成视图，不改变 [现行项目 issue tracker](issue-tracker.md)
对一般软件任务使用本地 Markdown 的约定，也没有创建任何在线 issue。

## 只读进度看板

[打开看板](https://woeai.readthedocs.io/zh-cn/latest/PublicationProgress.html)。
看板是公开的独立 Sphinx 页面，不加入学术网站左侧栏、目录树或前后页导航；
隐藏入口不是访问控制。入口保留在仓库 README 和生成的进度清单中。

先选择 RTD / 微信公众号，再按题名或 DOI、年份、研究方向、原始状态筛选。
“仅看未完成”按当前渠道判断：RTD 须有效核验；公众号须已发布且核验有效。
切换渠道保留关键词、年份、方向和未完成选项，清空原渠道状态；“重置筛选”
清除所有筛选并保留当前渠道。展开论文可查看两个渠道、检查项、缺口及公开链接。每列先显示 4 篇，
可点击“显示全部”展开；列计数和筛选始终覆盖全部论文。
未记录检查项不等于未通过；历史阶段检查不等于当前版本验收。

看板没有编辑、拖动改状态、后台登录或微信接口。助手维护唯一清单，运行
`registry.py --write` 生成 `docs/_static/publication-board-data.json`，随网站构建更新。
`registry.py --check` 检查数据是否过期；不是在线实时后台状态。生成器仅投影白名单
字段，不发布私有 ID、原论文路径或任意历史证据内容。无 JavaScript / 加载失败时，
页面仍提供仓库进度清单入口。未来增加新状态需同步显示语义与测试，不把未知归为已完成。

Sphinx 构建只在看板页加载专用 CSS / JavaScript，并自动附加内容哈希；
数据 URL 也带生成 JSON 的内容哈希。清单、样式或脚本更新后，新的页面引用新的
缓存版本，避免部署成功但浏览器继续使用旧资产。不要改回未版本化的原始 script/link 标签。

## Public review records and synchronization identities

Public article reviews retain DOI, source-page evidence, source hashes, current accuracy and coverage results, and public body/asset links. Internal bibliography identifiers, historical backend timestamps and private preview locators belong in ignored private production records. Current review status must not inherit historical draft readiness.

The existing registry and compatibility data still use bibliographic synchronization identities. Review minimization does not change the registry schema, upstream matching, or historical snapshots. A future private identity-map adapter keyed by stable publication_ref requires a separate explicit migration with matching/uniqueness tests; do not delete identifiers ad hoc or claim repository-wide identity removal.
