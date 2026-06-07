# Publications Research View Implementation Plan

日期：2026-06-07

## 背景

当前 `docs/source/Publications.rst` 是完整的学术成果页，按照发表年份倒序展示期刊论文。页面由 `scripts/update-publications-from-zotero.py` 从本地 Zotero 数据生成，已经包含稳定 RST 锚点、展示编号、学生第一作者标记、精选证据和指标文本。

用户希望在学术成果页面上同时提供两种浏览方式：

1. 按发表年份浏览：当前已有，年份倒序。
2. 按研究方向浏览：第一层级是研究方向，第二层级是发表年份，年份也倒序。

本计划的核心判断是：两种格式可以共存，但不能形成两份手工维护的完整论文正文。应保留一个权威完整列表，再生成一个按方向组织的浏览视图，所有条目链接回同一组稳定论文锚点。

## 目标

- 保留现有按年份展示方式，继续作为完整、权威的期刊论文清单。
- 增加按研究方向聚合的浏览方式，层级为 `研究方向 -> 年份 -> 论文链接`。
- 避免同一论文长引文、DOI、指标文本在两个页面重复维护。
- 让新增视图由同一脚本和同一数据来源生成，降低后续 Zotero 更新后的维护成本。
- 让研究方向分类遵守 `CONTEXT.md` 中的公开语义约束。

## 不做范围

- 不改变当前完整论文列表的排序规则和展示编号生成逻辑。
- 不把 `Publication Number` 当作跨页面永久标识。
- 不引入 JavaScript tabs 或前端状态切换；Read the Docs / Sphinx 静态页面优先。
- 不借这次改动重新定义研究方向 taxonomy。
- 不把微信文章 backlog 中的精选论文清单当作全量分类来源。

## 关键语义约束

执行时必须遵守 `CONTEXT.md`：

- `Academic Outputs` 是学术成果页的公共标签。
- `Public Journal Paper` 是当前页面中的公开期刊论文记录。
- `Publication Number` 只是当前排序下的展示编号，不能作为稳定引用。
- 跨页面引用必须使用显式 RST anchor。
- `Research Family` 的第一层级只能使用两个公开研究方向：
  - `建筑结构抗风`
  - `海上漂浮风电`
- `数值风洞与湍流入流`、`高层建筑抗风与优化`、`浮式风机系统一体化分析与优化`、`浮式混凝土平台结构设计`、`数值风浪流水池` 等属于 subdirection，不应变成第一层级。
- `Representative Publication` 是精选子集，不能替代完整方向分类。

## 推荐信息架构

保留：

- `docs/source/Publications.rst`

新增：

- `docs/source/PublicationsByResearch.rst`

推荐原因：

- 当前 `Publications.rst` URL 已经存在，应继续作为权威入口。
- 新页面避免在一个 RST 文件中堆叠过长目录，读者可以按需要切换。
- Sphinx / RTD 对普通页面和 `:doc:` / `:ref:` 链接支持稳定，不需要额外前端依赖。

在 `docs/source/Publications.rst` 的 `阅读说明 Notes` 后增加一个小节：

```rst
浏览方式 View Options
---------------------

- 当前页：按发表年份倒序浏览完整期刊论文清单。
- :doc:`PublicationsByResearch`：按研究方向浏览，方向内按发表年份倒序聚合。
```

同时在 `docs/source/index.rst` 的隐藏 toctree 中加入 `PublicationsByResearch`，使页面参与 Sphinx 构建和导航索引。

`docs/source/PublicationsByResearch.rst` 建议结构：

```rst
按研究方向浏览学术成果 Publications by Research Direction
========================================================

阅读说明 Notes
---------------

- 本页用于按研究方向浏览公开期刊论文；完整引文、DOI 和指标请查看对应论文在 :doc:`Publications` 中的条目。
- 研究方向采用本站公开 taxonomy；方向内按发表年份倒序排列。

建筑结构抗风
------------

2026
~~~~

- :ref:`[74] A novel framework for urban geometry rapid reconstruction ... <ref-zhao2026-BE>` （数值风洞与湍流入流）

海上漂浮风电
------------

2026
~~~~

- :ref:`[71] Structural design and optimization ... <ref-he2026-OE-structural>` （浮式混凝土平台结构设计）
```

每条方向页记录应是短链接，不重复完整引文正文。推荐包含：

- 当前展示编号：用于读者快速对应完整列表，但不作为稳定 ID。
- 标题短文本：从 Zotero title 或渲染后条目提取。
- RST anchor：链接回 `Publications.rst` 的稳定论文锚点。
- 可选 subdirection：帮助读者理解方向内细分，但不作为第一层级。

## 数据来源设计

新增一个专用映射文件：

- `docs/data/publication-research-map.json`

说明：当前工作区已经出现 `docs/superpowers/` 被 `.gitignore` 忽略和若干既有 source-packet 文件被删除的状态。本功能的生产输入不应放在一个可能不被 Git 跟踪的位置。`docs/superpowers/` 后续仍可作为审阅快照或历史证据目录，但方向页生成所依赖的映射文件应放在可跟踪的 `docs/data/` 下。

推荐字段：

```json
{
  "items": {
    "CGKPKZ8I": {
      "research_family": "建筑结构抗风",
      "subdirection": "数值风洞与湍流入流",
      "note": "urban microscale wind, precomputed CFD database"
    },
    "EMID6LAJ": {
      "research_family": "海上漂浮风电",
      "subdirection": "浮式混凝土平台结构设计",
      "note": "reinforced-concrete semi-submersible platform"
    }
  }
}
```

以 Zotero key 作为主键，原因：

- `zotero_key` 已在 snapshot 中保存。
- 展示编号会随排序变化，不能作为映射键。
- anchor 当前有稳定性保护，但仍由生成脚本派生；Zotero key 更适合做脚本输入映射。
- JSON 可以用 Python 标准库解析，避免为了维护文件新增 `PyYAML` 依赖。

`wechat/backlog/selected-papers.yml` 可以作为初始参考，但不能作为方向页全量来源：

- 它是微信选题和精选论文清单，不是完整期刊论文分类表。
- 当前工作区中微信稿件相关文件有未提交改动，本计划不应触碰或依赖这些脏改动。
- 方向页需要覆盖所有 Public Journal Papers，而不是只覆盖 Representative Publications。

## 未分类论文处理规则

公开页面不建议出现长期的 `待归类` 分类，因为这会弱化“第一层级是研究方向”的产品承诺。

推荐规则：

- 生成方向页时，所有 `Public Journal Paper` 必须有 `research_family`。
- `research_family` 必须是 `建筑结构抗风` 或 `海上漂浮风电`。
- `subdirection` 可以为空，但如果填写，必须是当前公开方向文案中已经存在或在 `CONTEXT.md` 中补充定义的子方向。
- 如果有论文无法确定方向，脚本应失败并输出缺失 Zotero key、标题和年份，要求人工补齐映射后再生成页面。

## 脚本实施计划

修改 `scripts/update-publications-from-zotero.py`：

1. 新增常量：

```python
PUBLICATIONS_BY_RESEARCH_PATH = ROOT / "docs/source/PublicationsByResearch.rst"
RESEARCH_MAP_PATH = ROOT / "docs/data/publication-research-map.json"
RESEARCH_FAMILY_ORDER = ("建筑结构抗风", "海上漂浮风电")
```

2. 新增映射读取函数：

```python
def load_research_map() -> dict[str, dict[str, str]]:
    ...
```

3. 新增映射校验函数：

```python
def validate_research_map(items, research_map) -> None:
    ...
```

校验内容：

- 每个 `item["key"]` 都存在映射。
- 不允许映射文件中出现当前 Zotero Public Journal Papers 不存在的 key，除非显式标注为历史保留并被脚本忽略。
- `research_family` 必须在 `RESEARCH_FAMILY_ORDER` 中。
- 同一 key 只能属于一个 first-level family。

4. 新增方向页生成函数：

```python
def build_publications_by_research_rst(items, research_map) -> str:
    ...
```

排序规则：

- family 按 `RESEARCH_FAMILY_ORDER`。
- family 内年份按倒序。
- 年份内沿用当前 `items` 的排序，即发表日期倒序、规范化标题升序。

5. 更新 `write_outputs`：

```python
research_map = load_research_map()
validate_research_map(items, research_map)
by_research_page = build_publications_by_research_rst(items, research_map)
...
PUBLICATIONS_BY_RESEARCH_PATH.write_text(by_research_page, encoding="utf-8")
```

6. 更新 dry-run 输出：

- 输出将写入 `PublicationsByResearch.rst`。
- 输出分类覆盖数。
- 输出每个 research family 的论文数量。

7. 更新 snapshot：

在 `snapshot(...)` 的每个 item 中增加：

```json
"research_family": "...",
"subdirection": "..."
```

这样后续 review 可以直接从 snapshot 检查分类覆盖。

## 页面实施计划

1. 修改 `docs/source/Publications.rst` 生成模板：
   - 在 `page_header(...)` 中加入 `浏览方式 View Options`。
   - 说明当前页按发表年份浏览完整清单。
   - 链接 `:doc:`PublicationsByResearch``。

2. 新增 `docs/source/PublicationsByResearch.rst`：
   - 首次可以由脚本生成。
   - 标题使用 `按研究方向浏览学术成果 Publications by Research Direction`。
   - 引导读者回到 `Publications.rst` 查看完整引文、DOI 和指标。

3. 修改 `docs/source/index.rst`：
   - 在 hidden toctree 中加入 `PublicationsByResearch`。
   - 不一定把它放入首页显式正文；先让 `Publications.rst` 承担切换入口。

4. 修改 `CONTEXT.md`：
   - 新增 `Chronological Publication View`。
   - 新增 `Thematic Publication View`。
   - 新增 `Publication Research Mapping`。
   - 明确两个视图共享同一组 Public Journal Papers，方向视图链接回完整列表，不复制完整引文。

## 测试与验收计划

必须通过：

```bash
./scripts/check-docs.sh
git diff --check
```

建议新增轻量检查脚本：

- `scripts/check-publications-research-view.py`

检查内容：

- `docs/source/PublicationsByResearch.rst` 存在。
- 两个 first-level family 都存在，且顺序为 `建筑结构抗风`、`海上漂浮风电`。
- 每个 family 内年份倒序。
- 方向页中每个 `:ref:` target 都能在 `docs/source/Publications.rst` 找到对应 anchor。
- 方向页不重复 DOI、影响因子、中科院分区、引用次数等长引文指标文本。
- `Publications.rst` 的每个 Public Journal Paper anchor 至少在方向页出现一次。

将该脚本接入 `./scripts/check-docs.sh`，推荐放在 Sphinx build 前，先捕获生成语义错误。

本地构建后人工检查：

- `Publications.html` 中有清晰的两种浏览方式入口。
- `PublicationsByResearch.html` 的层级是 `研究方向 -> 年份 -> 论文`。
- 点击方向页条目能跳转到 `Publications.html` 的对应论文锚点。
- 页面没有把 subdirection 提升为第一层级。
- 页面没有新增单位、合作方、项目细节、个人隐私或未确认指标。

## 推荐提交拆分

建议拆成 3 个小提交，便于 review：

1. `docs: add publication research mapping plan terms`
   - `CONTEXT.md`
   - mapping 文件骨架

2. `docs: generate publications research view`
   - `scripts/update-publications-from-zotero.py`
   - `docs/source/Publications.rst`
   - `docs/source/PublicationsByResearch.rst`
   - snapshot 更新

3. `test: check publications research view links`
   - 新增检查脚本
   - 接入 `scripts/check-docs.sh`

如果一次性实现，也必须保持 diff 清晰，避免同时修改当前微信文章相关文件。

## 风险与缓解

| 风险 | 影响 | 缓解 |
|---|---|---|
| 双视图复制完整引文 | 后续 Zotero 更新后两处漂移 | 方向页只放短链接，完整引文只在 `Publications.rst` |
| 分类映射不全 | 方向页承诺被破坏 | 脚本 fail-fast，列出缺失 key |
| 使用展示编号做稳定引用 | 新论文加入后链接含义变化 | 方向页用 RST anchor，编号只作读者可见提示 |
| taxonomy 漂移 | 网站研究方向表达混乱 | 第一层级强制读取固定 family order |
| 引入 YAML 依赖 | docs 构建依赖变复杂 | 优先用 JSON 映射文件 |
| 触碰当前微信工作区改动 | 干扰并行工作 | 本任务只改 docs/source、docs/data、scripts、CONTEXT/check 脚本 |

## 执行顺序

1. 确认当前工作区未提交改动范围，避开微信稿件相关文件。
2. 新增 publication research mapping JSON，并完成所有现有 Public Journal Papers 的分类。
3. 扩展生成脚本，生成两个页面并更新 snapshot。
4. 增加方向页检查脚本，并接入 `./scripts/check-docs.sh`。
5. 更新 `CONTEXT.md` 中的出版物视图术语。
6. 运行 `./scripts/check-docs.sh` 和 `git diff --check`。
7. 人工打开本地 HTML 检查两个页面的阅读体验和锚点跳转。

## GSTACK REVIEW REPORT

### Autoplan Adaptation

本复核按 `autoplan` 的 CEO、Design、Eng、DX 四视角执行。当前 Codex 环境没有可用的 Claude `AskUserQuestion` 工具，本次不触发交互式决策门，而是按用户已确认的方向自动作出低风险默认决策，并把复核结论写入计划文件。

### CEO Review

结论：通过，但要求保持“双入口、单事实源”的策略。

这个方案解决的是读者的两种真实动机：一种是看最近成果，另一种是判断某个研究方向的积累。按年份视图适合评估持续产出，按方向视图适合招生、技术合作和研究可信度判断。两者共存有价值。

必须避免把方向页做成第二个完整 bibliography。那会让维护成本翻倍，也会在指标、DOI、作者标记和引用次数更新时制造不一致。方向页应是浏览索引，不是第二份权威论文正文。

CEO 修改建议：计划中的 fail-fast 分类覆盖规则是正确选择。公开页不要长期出现 `待归类`，因为那会削弱方向聚合视图的可信度。

### Design Review

结论：通过，推荐普通页面链接，不推荐 tabs。

Read the Docs 的主题和 Sphinx 文档站更适合使用两个页面互链，而不是在一个页面上用前端 tabs 切换。两个页面的认知负担更低，URL 可分享，也更利于搜索引擎和 AI 抓取。

方向页的条目应短、密、可扫读。建议每条只保留编号、标题短文本和 subdirection 标签。完整 DOI、指标、长作者列表回到 `Publications.rst` 查看。这样读者在方向页不会被重复引文淹没。

Design 修改建议：在 `Publications.rst` 顶部加 `浏览方式 View Options`，但不要在首页额外制造复杂入口。首页导航仍以学术成果页为主。

### Engineering Review

结论：通过，但执行时必须先做映射数据结构，再改生成脚本。

当前 `scripts/update-publications-from-zotero.py` 已经拥有 `item["key"]`、`anchor`、`publication_number`、年份排序和 snapshot 输出。这是理想的生成入口。新增方向页不需要额外爬取或手工解析 `Publications.rst`。

最大工程风险是映射漂移。解决方法是让脚本校验每个 Public Journal Paper 都有研究方向映射，并在 dry-run 中报告 family 计数。方向页所有链接必须从 item 的 anchor 生成，不能从展示编号生成。

Engineering 修改建议：映射文件优先用 JSON 而不是 YAML，避免为了一个维护文件增加 PyYAML 依赖。

### DX Review

结论：通过，但要把未来维护路径写清楚。

后续维护者最容易困惑的问题是：新增 Zotero 论文后为什么生成脚本失败。计划需要在映射文件顶部或相邻文档中说明，新增 Public Journal Paper 时必须补充 `research_family`，否则方向页无法生成。

`snapshot` 中加入 `research_family` 和 `subdirection` 很有价值，可以让 review 不必重新打开映射文件和 Zotero 数据做人工对照。

DX 修改建议：检查脚本的报错要输出 Zotero key、标题和年份，方便维护者直接补映射。

### Final Decision

批准执行。

执行时采用以下最终决策：

- 保留 `Publications.rst` 为按年份倒序的完整权威列表。
- 新增 `PublicationsByResearch.rst` 为按方向浏览索引。
- 方向页第一层级只使用 `建筑结构抗风` 和 `海上漂浮风电`。
- 方向页第二层级按年份倒序。
- 方向页条目链接回 `Publications.rst` 的稳定 RST anchor，不复制完整长引文。
- 新增 JSON 映射文件，以 Zotero key 作为分类主键。
- 生成脚本对分类覆盖 fail-fast。
- 验收以 `./scripts/check-docs.sh`、`git diff --check` 和本地 HTML 人工检查为准。
