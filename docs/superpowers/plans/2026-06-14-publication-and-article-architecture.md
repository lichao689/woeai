# WOEAI 出版物与文章架构深化计划

- **日期**：2026-06-14
- **来源**：`improve-codebase-architecture` skill 评审（候选 A/B/C/D）
- **状态**：待批准
- **评审报告**：`/var/folders/hf/6ps1qfj9575dlgk7wy0h3r5r0000gn/T/architecture-review-20260613-1900.html`
- **范围**：`scripts/` · `tools/` · `wechat/tools/` · `docs/source/`
- **不在范围**：网站视觉/内容策略（另见 `2026-06-06-woeai-site-upgrade.md`）、公众号内容生产流程

## 背景与术语

本计划使用 `CONTEXT.md` 的领域术语（Publication Artifact / WeChat Article Source /
Research Family / Student First Author / Public Formula）与 skill 的架构术语
（module / interface / depth / seam / adapter / leverage / locality）。

评审发现的根因：**本仓库没有 Python 包**——无 `__init__.py`，所有脚本靠
`importlib.util.spec_from_file_location` 按文件路径互相加载，连测试也是。共享代码
无处安放，于是事实（引用文字、分类、学生一作标记、公式渲染器白名单、图注规则）
被复制到多处，各自漂移。四个候选（A/B/C/D）共享这个根前提。

## 约束（全部候选共同）

1. **RTD 不运行生成脚本**。提交进仓库的 RST 才是构建源
   （`update-publications-from-zotero.py` docstring 已声明）。所以深化后的模块产出
   必须离线、可重复地从已提交数据生成，不依赖网络。
2. **`./scripts/check-docs.sh` 是必跑门禁**（同时跑 public-safe 检查、artifacts 检查、
   `unittest discover`、Sphinx `-W` 构建）。每个阶段结束都必须通过。
3. **不引入外部依赖**。`docs/requirements.txt` 仅含 Sphinx；新模块只用标准库，
   确保门禁在临时 venv 里能跑。
4. **CONTEXT.md 是事实源**，AGENTS.md 动态更新规则必须随实现同步。

## 依赖分类（来自 DEEPENING.md）

| 候选 | 类别 | 含义 |
|---|---|---|
| A | In-process | 纯计算（JSON/YAML 读取 + 渲染），可直接合并、过新接口测试 |
| B | In-process | 纯文本解析，直接合并 |
| C | In-process | 纯文件操作，结构重组 |
| D | Local-substitutable | 两个 renderer 已有本地 stand-in，是真实 seam |

没有需要 Mock 的真正外部依赖（Zotero HTTP 仅在 `update-publications-from-zotero.py`
内部，不进入共享模块接口）。

---

## 总控策略

四个候选不能并行——它们有强依赖：

```
第 0 阶段（建包）          ← 所有共享代码的安身之处；A/B/D 的前提
   └─> 第 1 阶段（候选 A）   ← Publication Data 模块；B/D 读论文事实的前置
          ├─> 第 2 阶段（候选 C）  ← 依赖 A 的"单一写入者"，最便宜的 latent bug 修复
          └─> 第 3 阶段（候选 B）  ← Article 模块；可复用 A 的论文事实回填
                 └─> 第 4 阶段（候选 D）  ← 公式渲染 seam；最独立，风险最低
```

每个阶段独立可验证、可单独提交、可单独回滚。任一阶段失败不影响已完成阶段。
建议**每个阶段一个 PR / 一组小提交**，按 AGENTS.md "小而可独立验证的提交"原则。

---

# 第 0 阶段：建立共享 Python 包

**目的**：给 A/B/D 的共享代码一个安身之处，消除"无处安放 → 复制"的根因。

**改动**

1. 新建包 `woeai/`（仓库根），含 `woeai/__init__.py`。
2. 新建子包：
   - `woeai/publications/`（A 阶段填充）— `__init__.py` 空占位
   - `woeai/wechat/`（B 阶段填充）— `__init__.py` 空占位
3. `tools/publications/artifacts.py` 暂留原位（第 2 阶段处理）。
4. 不新增项目打包元数据；本仓库仍保持 docs-first 形态。`scripts/check-docs.sh`
   通过 `PYTHONPATH` 注入仓库根，让本地 `import woeai` 在脚本、测试和门禁中可用。
5. 让测试从 `importlib.util` 路径加载切换为 `import woeai...`——**只切导入方式**，
   不动逻辑。先让 `tests/` 能 `import woeai`。
6. `scripts/check-docs.sh` 不变（仍跑 `python3 -m unittest discover`）。

**验证**
- `python3 -c "import woeai.publications, woeai.wechat"` 成功。
- `./scripts/check-docs.sh` 全绿（此时无逻辑变化，纯结构）。

**风险**：低。纯结构，无行为变化。唯一注意点是 `sys.path`——测试与脚本目前都用
`Path(__file__).parents[N]` 推根目录，建包后改为标准 import，需确认 CI/本地都能
找到包根（`PYTHONPATH` + 仓库根运行即可）。

**回归保护**：此阶段不改任何行为，所有现有测试必须原样通过。

---

# 第 1 阶段（候选 A）：Publication Data 模块

**要解决的问题**：一篇 Public Journal Paper 散落在 6 种数据形态；引用文字、
Research Family、Student First Author 标记在 RST / YAML / 手写 markdown 各自维护，
悄悄漂移；分类常量在 3 个文件逐字节复制。

**seam 后面放什么**

`woeai/publications/model.py` 提供一个深模块：

```
Publication（dataclass）
  zotero_key, anchor, publication_number, year, title,
  doi, creators, citation_text（渲染好的 [N] ... 行）,
  student_first_author_name | None,
  corresponding_authors: list[str],
  research_family, subdirection

load_publications(root) -> list[Publication]
  从 Zotero 快照 JSON + research-map.json + degree-theses.json 合并
  （不调 Zotero HTTP；HTTP 留在 update-publications-from-zotero.py）

RESEARCH_FAMILY_ORDER / RESEARCH_SUBDIRECTION_ORDER  ← 唯一源，模块常量
```

**改动步骤**

1. 把 `update-publications-from-zotero.py` 里的纯计算逻辑搬进 `woeai/publications/`：
   - `model.py`：`Publication` + taxonomy 常量（**唯一源**）。
   - `rendering.py`：`rendered_entry`、`mark_student_first_author`、
     `mark_corresponding_authors`、`bold_*`、citation 后处理。
   - `authors.py`：作者名归一、student-first-author 检测、通讯作者检测。
   - `data.py`：`load_degree_thesis_data`、`load_research_map`、`load_student_author_names`。
2. `scripts/update-publications-from-zotero.py` 变薄：保留 Zotero HTTP 抓取
   （`fetch_publication_items`、`paginated`、CSL 样式校验）+ CLI 编排，逻辑全部
   `from woeai.publications import ...`。
3. `tools/publications/artifacts.py` 删除本地 `RESEARCH_FAMILY_ORDER` /
   `RESEARCH_SUBDIRECTION_ORDER`，改 `from woeai.publications.model import ...`。
4. `tests/test_publications_research_view.py` 删除本地 `RESEARCH_FAMILIES` /
   `RESEARCH_STRUCTURE`，改 import。
5. **WeChat md 的"论文信息"暂不自动回填**——本阶段只统一"事实源"，不动 md 措辞
   （措辞归 WeChat Article Source）。回填留到第 3 阶段与 B 一起做。

**验证**
- taxonomy 常量全仓库只剩 `woeai/publications/model.py` 一处（`grep -rn
  "建筑结构抗风" --include=*.py` 只命中 model.py）。
- `test_publications_research_view.py` 7 个行为测试原样通过（两视图引用一致、
  分组、锚点稳定、teaching-reform 隔离、early 分组、anchor alias）。
- `test_update_publications_from_zotero.py`（对应作者、学生一作）通过。
- `./scripts/check-docs.sh` 全绿。

**测试存活判定**（DEEPENING: interface is the test surface）
- **存活**：所有断言"生成结果"的行为测试（引用一致、分组、锚点）。
- **删除**：如有测内部 helper 的脆弱测试（grep 确认无）。
- **新增**：`test_model.py` 直接测 `load_publications` 返回的 `Publication` 结构，
  而非通过 RST 间接测。

**风险与缓解**
- Zotero 脚本是 1068 行单文件——搬家是机械工作但量大。**缓解**：分小提交，
  每搬一个子模块就跑一次 `check-docs.sh`。
- 学生一作/通讯作者逻辑搬家时，行为必须逐字不变——靠现有测试锁定。

---

# 第 2 阶段（候选 C）：一个文件一个写入者

**要解决的问题**：`Publications.rst` 被 Zotero 脚本和 `artifacts.py` 两个写入者
瓜分；Zotero 重新生成时不保留 `artifacts.py` 的标记块 → 潜在的静默覆盖。

**改动**

1. `artifacts.py` 不再往 `Publications.rst` 写 `TOCTREE_MARKER` /
   `AREA_MARKER` 两个标记块。
2. 新建独立文件，由 `artifacts.py` 独占写入：
   - `docs/source/paper-notes/_index.rst`（toctree + 区域内容合一）。
3. `Publications.rst` 用 `.. include:: paper-notes/_index.rst` 或在自身 toctree
   里引用，由 Zotero 脚本独占写入全文。
4. 删除 `artifacts.py` 里的 `replace_marker_block` / `current_marker_body` /
   `marker_lines` / `TOCTREE_MARKER` / `AREA_MARKER`（拼接引擎整个删掉）。
   `index.rst` 的 `LATEST_MARKER` 块**暂保留**（首页最近进展，语义不同，且只有一个写入者）。
5. `markdown_to_rtd.py` 里若依赖 Publications.rst 的标记块定位"完整引用"，改为
   按 anchor 从 Publications.rst 抓取（现有 `parse_publications_citation` 逻辑不变）。

**验证**
- `Publications.rst` 不再含 `BEGIN GENERATED` 标记块（`grep` 确认）。
- 重新跑 `update-publications-from-zotero.py`（若可离线）→ `Publications.rst`
  不丢失任何 paper-notes 内容（因为内容在 include 文件里）。
- `test_publication_artifacts.py`：
  - `test_write_replaces_marker_blocks_and_check_then_passes` → **改写**为
    "write 生成 paper-notes/_index.rst，check 通过"。
  - `test_check_fails_when_marker_block_is_stale` → **删除**（标记块机制已移除，
    这是 DEEPENING 说的"旧测试变废"）。
  - 新增："Publications.rst 通过 include 引入 paper-notes 区域，且 Zotero
    重生成后内容不丢失"。
- `./scripts/check-docs.sh` 全绿（含 Sphinx `-W` 构建，确认 include 正确）。

**为何紧跟 A**：A 让 Publication Data 模块就位后，"谁该写 Publications.rst 的什么"
有了清晰归属——Zotero 脚本（经模块）写论文条目，artifacts.py 写 paper-notes 索引。
两者不再争同一个文件的同一区域。

---

# 第 3 阶段（候选 B）：Article 模块

**要解决的问题**：同一篇 WeChat Article Source `.md` 被
`markdown_to_rtd.py` / `render-copy-ready.py` / `wechat_draft.py` 三个脚本各用
一套正则重解析，规则漂移（图注 RTD 用位置、HTML 用正则）；`BacklogPaper`、
`parse_front_matter`、封面正则、`parse_title`、图注、related-papers 排序重复 6+ 处。

**seam 后面放什么**

`woeai/wechat/article.py`：

```
Article（dataclass）
  title, digest, author_line, body_images, cover_path,
  blocks: list[Block]   ← 统一解析后的结构化块（标题/段落/列表/图注/公式/延伸阅读）

parse(article_md_path, review_md_path) -> Article
  统一解析 front-matter、封面、标题、作者行、图片、图注（位置规则，对齐 CONTEXT.md
  2026-06-11 两行结构规范）、延伸阅读。

BacklogPaper（dataclass）+ load_backlog(yml_path) -> list[BacklogPaper]
  唯一实现，三个脚本共用。
```

三个脚本成为 adapter：
- `markdown_to_rtd.py` = RST emitter（`Article → .rst`）
- `render-copy-ready.py` = HTML emitter（`Article → .html`）
- `wechat_draft.py` = WeChat payload builder（`Article → 草稿 API payload`）

**改动步骤**

1. `woeai/wechat/article.py`：搬入 `parse_front_matter`、`parse_cover_path`、
   `parse_markdown_images`、`parse_title`、`BacklogPaper` + `parse_backlog_papers`、
   related-papers 排序。**统一图注为位置规则**（对齐 CONTEXT.md）。
2. 删除三脚本里的重复 helper（6+ 处）。
3. 删除 `wechat_draft.py` 的 `importlib load_renderer` 路径 hack——改为
   `from woeai.wechat import render` 正常 import（render-copy-ready 逻辑搬进
   `woeai/wechat/render.py`）。
4. 删除 `wechat_draft.py` 的 `importlib load_public_safety_checker`——
   `check-public-safe-content.py` 暴露的 `collect_findings` 也搬进包或保留脚本但用
   正常 import（见下方"开放问题"）。
5. **与 A 的衔接**：`wechat_draft.py` 读论文事实（DOI/作者标记/年份/方向）改为
   `from woeai.publications import load_publications`，不再从手写 md 的"论文信息"
   块解析。md 的"论文信息"块**保留**（CONTEXT.md 规定它是读者可见信息），但工具
   校验它与模型一致（不一致则 fail）。

**验证**
- 仓库内 `def parse_front_matter` / `def parse_title` / `BacklogPaper` 各只剩一处。
- 图注规则统一：对同一 md，三个 adapter 产出的图注块结构一致（标题行 + 说明行）。
- `test_wechat_tools.py` 全部行为测试通过（RST 转换、作者标记、related links、
  citation 截断、HTML 渲染、content_source_url、author 默认值）。
- 新增 `test_article.py`：直接测 `parse()` 返回的 `Article` 结构。
- `./scripts/check-docs.sh` 全绿。

**测试存活判定**
- **存活**：所有断言"生成的 RST/HTML/payload 含什么"的行为测试。
- **删除**：验证重复 helper 一致性的测试（如有）。
- **新增**：`test_article.py` 测结构，不测字符串。

**风险与缓解**
- 图注规则统一（位置 vs 正则）可能改变某些现有 md 的输出。**缓解**：先跑现有
  15 篇文章的 dry-run，diff 输出，确认无意外变化再合并。若有差异，按 CONTEXT.md
  两行规范修正 md（规范是位置的）。
- `check-public-safe-content.py` 是被 `check-docs.sh` 直接调用的脚本——它要不要
  也进包？见下方"开放问题"。

---

# 第 4 阶段（候选 D）：公式渲染 seam

**要解决的问题**：Public Formula 渲染有 2 个真实 adapter（lightweight / mathjax-svg），
但选择靠字符串比较、`AVAILABLE_MATH_RENDERERS` 在两个文件重复、异常类型不一致；
CONTEXT.md 提到的 PNG tier 在代码里不存在。

**seam 后面放什么**

`woeai/wechat/options.py`：

```
DEFAULT_THEME / AVAILABLE_THEMES / validate_theme
DEFAULT_MATH_RENDERER / AVAILABLE_MATH_RENDERERS / validate_math_renderer
```

完整 Public Formula renderer registry 仍是未来可选深化；本阶段只统一已经
重复漂移的主题与公式渲染器白名单、默认值和校验函数。

**改动步骤**

1. 新增 `woeai/wechat/options.py`，集中主题、公式渲染器默认值、白名单和校验函数。
2. 删除 `wechat_draft.py` 和 `render-copy-ready.py` 里重复的
   `AVAILABLE_MATH_RENDERERS` / `AVAILABLE_THEMES` / `validate_*`。
3. CLI 的 `--math-renderer` / `--theme` choices 改为读 `woeai.wechat.options`。
4. **PNG tier 暂不实现**（CONTEXT.md 提及但无现成需求）——只在 registry 留扩展点，
   不为不存在的需求写代码。

**验证**
- `AVAILABLE_MATH_RENDERERS` 全仓库只剩 `woeai/wechat/options.py` 一处。
- `test_lightweight_formula_renderer_does_not_call_mathjax` 通过。
- `render-copy-ready.py` 与 `wechat_draft.py` 的 CLI choices 均来自同一 options 模块。
- `./scripts/check-docs.sh` 全绿。

---

## 开放问题（需在对应阶段决策，不阻塞批准）

1. **`check-public-safe-content.py` 是否进包？**
   它被 `check-docs.sh` 直接当脚本调用，又被 `wechat_draft.py` 经 importlib 复用。
   选项：(a) 进 `woeai/safety.py`，脚本变薄 wrapper；(b) 保留脚本，仅复用方式
   改正常 import。**倾向 (a)**——它有明确的纯函数 `collect_findings`，适合进包。
   决策点在第 3 阶段。

2. **WeChat md 的"论文信息"块是校验还是回填？**
   CONTEXT.md 把 WeChat Article Source 当措辞事实源，所以工具不能覆盖作者手写措辞。
   倾向：第 3 阶段工具**校验** md 里的 DOI/作者标记/年份/方向与 Publication Data
   模型一致，不一致则 fail，而非自动回填。措辞（如"作者:"行格式）仍归 md。

3. **是否为 Publication Data 模块引入缓存？**
   `load_publications` 每次调用都读 3 个 JSON。当前调用频率低（离线生成），暂不需要
   缓存。若第 3 阶段 wechat_draft 频繁调用再加。

4. **`LATEST_MARKER`（首页最近进展）保留还是也拆？**
   它只有一个写入者（artifacts.py），无 C 的竞争问题，本计划保留不动。

## CONTEXT.md / AGENTS.md 同步

边界：`CONTEXT.md` 是**公共网站措辞**词汇表（领域语言），不混入 Python 模块路径
这类实现细节。实现层的约束写进 **AGENTS.md 动态更新规则**。

- 第 1 阶段：AGENTS.md 动态更新规则追加——Research Family/Subdirection 分类常量
  唯一源为 `woeai/publications/model.py`，禁止在其他 Python 文件复制；Publication
  与 Degree Thesis Data 的加载由该模块承担。
- 第 3 阶段：AGENTS.md 动态更新规则追加——WeChat Article Source 的事实字段（DOI、
  作者标记、年份、Research Family）必须与 Publication Data 模型一致，工具不一致则
  fail，而非覆盖作者措辞。
- 第 4 阶段：AGENTS.md 动态更新规则追加——Public Formula renderer 白名单唯一源为
  `woeai/wechat/options.py`。
- 各阶段不动 CONTEXT.md 的公共措辞词条（它描述读者可见语言，不描述代码结构）。

## 不做什么（防止范围蔓延）

- 不改网站视觉/主题/CSS（不在本计划范围）。
- 不引入第三方库（坚持标准库，保门禁可移植）。
- 不把仓库变成可发布包；本地 import 由门禁脚本注入 `PYTHONPATH`。
- 不自动发布公众号、不碰凭据存储（CONTEXT.md 已有 Manual Publication Gate 规则）。
- 不实现 PNG 公式 tier（无现成需求）。
- 不动 Zotero HTTP 抓取逻辑（保留在脚本里，不进包接口）。

## 阶段验收清单（每阶段结束）

- [ ] `./scripts/check-docs.sh` 全绿
- [ ] 该阶段声称"删除的复制"经 grep 确认只剩唯一源
- [ ] 该阶段声称"存活"的测试确实原样通过
- [ ] 该阶段声称"删除/改写"的测试已处理，无悬挂的失败测试
- [ ] CONTEXT.md / AGENTS.md 对应词条已同步
- [ ] 小提交，每个独立可回滚
