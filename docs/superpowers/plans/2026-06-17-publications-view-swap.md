# 学术成果默认视图交换与精解融入引用 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 让"按研究方向浏览"成为学术成果页的默认视图，并在该视图中把论文精解标题融入期刊引用上方。

**Architecture:** 交换 `update-publications-from-zotero.py` 里两个生成函数的职责——`build_publications_rst` 改为按方向分组（成为主视图），`build_publications_by_year_rst` 改为按年份倒序（成为子视图）。锚点定义随之移到主视图。主视图里对有精解的论文，在引用行上方插入精解标题行。移除独立的论文精解 section（保留 toctree 注册）。

**Tech Stack:** Python 3.12（标准库），Sphinx RST，unittest。脚本 `scripts/update-publications-from-zotero.py`，工具 `tools/publications/artifacts.py`。

---

## 现状理解（执行者必读）

当前两个视图的生成和锚点归属：

- **`Publications.rst`**（学术成果页，主入口）：`build_publications_rst` 生成，按年份倒序。**拥有锚点**（`.. _ref-xxx:`）。顶部有 banner 指向 PublicationsByYear，有 `.. include:: _paper-notes-fragment.rst`（论文精解 section），然后是期刊论文列表。
- **`PublicationsByYear.rst`**（按研究方向浏览，子页）：`build_publications_by_year_rst` 生成，按方向分组。**不拥有锚点**，用 `:ref:` 链接回 Publications.rst 的锚点。没有 banner。
- 精解标题数据在 `wechat/backlog/selected-papers.yml`（`publication_ref` + `zotero_key` + `title`）。标题格式是 `方向前缀 | 精解标题`，需要去掉前缀。
- `artifacts.py` 生成 `_paper-notes-fragment.rst`，包含 toctree（注册 paper-notes 页面）+ 论文精解 section（`论文精解` 标题 + 按方向分组的精解列表）。

## 目标状态

- **`Publications.rst`**（学术成果页，主入口）：按**研究方向**分组。拥有锚点。banner 指向"按年份倒序浏览"。期刊论文列表里，有精解的论文在引用行上方有精解标题行。不再有独立论文精解 section。
- **`PublicationsByYear.rst`**（按年份倒序浏览，子页）：按**年份倒序**。不拥有锚点，用 `:ref:` 链接回 Publications.rst。有 banner 指回学术成果页。
- **`_paper-notes-fragment.rst`**：只保留 toctree（注册 paper-notes 页面），移除论文精解 section。
- **首页"最新学术进展"**：不受影响（仍由 artifacts.py 的 `render_latest_paper_notes` 生成，数据源不变）。

## 关键约束

- 文件路径不变：`Publications.html` 仍是主入口 URL。
- 锚点不能在两个文件里重复定义（Sphinx 会警告），只在主视图定义。
- CONTEXT.md 的 Chronological/Thematic Publication View 定义需要同步更新语义（哪个是主、哪个是辅交换了）。
- AGENTS/claude/gemini 不需要改（不涉及规则变化，只是生成逻辑变化）。

## 文件结构

- Modify: `scripts/update-publications-from-zotero.py` — 交换两个生成函数的职责，主视图加精解标题行
- Modify: `tools/publications/artifacts.py` — `_paper-notes-fragment.rst` 移除论文精解 section
- Modify: `docs/source/_paper-notes-fragment.rst` — 重新生成（只剩 toctree）
- Modify: `tests/test_publications_research_view.py` — 更新断言
- Modify: `tests/test_update_publications_from_zotero.py` — 更新断言
- Modify: `CONTEXT.md` — 同步视图定义
- Regenerate: `docs/source/Publications.rst`, `docs/source/PublicationsByYear.rst`（跑脚本）

---

### Task 1: 交换两个视图的分组逻辑和锚点归属

**Files:**
- Modify: `scripts/update-publications-from-zotero.py:641-695`
- Test: `tests/test_update_publications_from_zotero.py`

**核心改动**：`build_publications_rst` 改为按方向分组并拥有锚点；`build_publications_by_year_rst` 改为按年份倒序并用 `:ref:` 链接。

- [ ] **Step 1: 写失败测试——主视图按方向分组**

在 `tests/test_update_publications_from_zotero.py` 的测试类里加一个测试，验证 `build_publications_rst` 按方向分组而非按年份：

```python
def test_publications_rst_groups_by_year_family(self) -> None:
    # After the view swap, Publications.rst (the main page) groups by
    # research family first, not by year.
    items = [
        {"key": "K1", "data": {"date": "2026", "title": "Wind", "creators": [{"lastName": "Zhang", "firstName": "S"}], "publicationTitle": "Ocean Engineering"}, "bib": "Zhang S, Wind[J]. Ocean Engineering, 2026.", "publication_number": 1, "anchor": "ref-zhang2026-OE"},
        {"key": "K2", "data": {"date": "2025", "title": "Wave", "creators": [{"lastName": "Li", "firstName": "C"}], "publicationTitle": "Wind and Structures"}, "bib": "Li C, Wave[J]. Wind and Structures, 2025.", "publication_number": 2, "anchor": "ref-li2025-WAS"},
    ]
    research_map = {
        "K1": {"research_family": "海上漂浮风电", "subdirection": "浮式风机系统一体化分析与优化"},
        "K2": {"research_family": "建筑结构抗风", "subdirection": "数值风洞与湍动入流"},
    }
    page = self.updater.build_publications_rst(items, research_map)
    # Family headings appear; 建筑结构抗风 before 海上漂浮风电 per taxonomy order
    self.assertIn("建筑结构抗风", page)
    self.assertIn("海上漂浮风电", page)
    self.assertLess(page.index("建筑结构抗风"), page.index("海上漂浮风电"))
```

- [ ] **Step 2: 运行测试，确认失败**

Run: `python3 -m unittest tests.test_update_publications_from_zotero -v 2>&1 | tail -10`
Expected: FAIL（`build_publications_rst` 当前只接受 `items`，不接受 `research_map`；且按年份分组）

- [ ] **Step 3: 改 `build_publications_rst` 为按方向分组 + 拥有锚点**

把 `build_publications_rst` 改为接受 `research_map` 参数，按 `RESEARCH_FAMILY_ORDER` / `RESEARCH_SUBDIRECTION_ORDER` 分组，在每个论文条目前输出锚点定义。替换 `scripts/update-publications-from-zotero.py` 里 `build_publications_rst` 函数（当前 641-663 行）为：

```python
def build_publications_rst(
    items: list[dict[str, Any]], research_map: dict[str, dict[str, str]]
) -> str:
    sections = [page_header({})]
    for family in RESEARCH_FAMILY_ORDER:
        sections.extend([family, "-" * 12, ""])
        for subdirection in RESEARCH_SUBDIRECTION_ORDER[family]:
            sections.extend([subdirection, "~" * 40, ""])
            for item in items:
                row = research_map[item["key"]]
                if row["research_family"] != family or row.get("subdirection") != subdirection:
                    continue
                for anchor in publication_anchor_targets(item):
                    sections.extend([f".. _{anchor}:", ""])
                sections.extend([rendered_entry(item, item["publication_number"]), ""])
    return "\n".join(sections).rstrip() + "\n"
```

- [ ] **Step 4: 改 `build_publications_by_year_rst` 为按年份倒序 + `:ref:` 链接**

把当前 `build_publications_by_year_rst`（673-695 行）改为按年份倒序，用 `research_full_entry`（已有 `:ref:` 链接逻辑）。替换为：

```python
def build_publications_by_year_rst(items: list[dict[str, Any]]) -> str:
    sections = [
        ".. role:: student-first-author",
        "",
        "按年份倒序浏览学术成果 Publications by Year",
        "=" * 40,
        "",
        ".. container:: publication-view-banner",
        "",
        "   :doc:`返回按研究方向浏览学术成果 <Publications>`：按研究方向浏览，方向内按发表年份倒序聚合。",
        "",
        ".. toctree::",
        "   :hidden:",
        "   :maxdepth: 1",
        "",
        "   学术成果 Academic Outputs <Publications>",
        "",
        "期刊论文 Journal Papers",
        "------------------------",
        "",
        "- :student-first-author:`学生第一作者` 表示该论文第一作者为团队在校或毕业学生。",
        "- 作者姓名后的 ``*`` 表示通讯作者。",
        "",
    ]
    current_section: int | None = None
    for item in items:
        data = item["data"]
        year = extract_year(data.get("date"))
        section_key = year if year >= EARLY_PUBLICATION_CUTOFF_YEAR else 0
        if section_key != current_section:
            current_section = section_key
            title = str(section_key) if section_key else EARLIER_PUBLICATIONS_TITLE
            sections.extend([title, "~" * 12, ""])
        sections.extend([research_full_entry(item), ""])
    return "\n".join(sections).rstrip() + "\n"
```

- [ ] **Step 5: 改 `page_header`——banner 文字指向按年份视图**

把 `page_header`（599-629 行）的 banner 文字从"按研究方向浏览"改为"按年份倒序浏览"。toctree 注册改为 `按年份倒序浏览 Publications by Year <PublicationsByYear>`。移除 `.. include:: _paper-notes-fragment.rst`（精解 section 将在 Task 3 移除，但 include 先保留——Task 3 会改 fragment 内容）。

实际上 `page_header` 不再需要 `items_by_key` 参数（精解标题不在 page_header 里加），但签名保留以兼容。banner 行改为：

```python
"   :doc:`按年份倒序浏览学术成果 Publications by Year <PublicationsByYear>`：按发表年份倒序浏览完整期刊论文清单。",
```

toctree 注册改为：

```python
"   按年份倒序浏览 Publications by Year <PublicationsByYear>",
```

- [ ] **Step 6: 改 `write_outputs` 的调用签名**

`write_outputs` 里（当前 `page = build_publications_rst(items)`），改为 `page = build_publications_rst(items, research_map)`。`by_year_page = build_publications_by_year_rst(items, research_map)` 改为 `by_year_page = build_publications_by_year_rst(items)`。

- [ ] **Step 7: 运行测试，确认主视图分组测试通过**

Run: `python3 -m unittest tests.test_update_publications_from_zotero -v 2>&1 | tail -10`
Expected: 新测试 PASS，但其他测试可能有断言失败（预期，后续步骤修）

- [ ] **Step 8: Commit**

```bash
git add scripts/update-publications-from-zotero.py tests/test_update_publications_from_zotero.py
git commit -m "refactor: swap publications views — thematic becomes main, chronological becomes sub"
```

---

### Task 2: 更新现有测试断言适配视图交换

**Files:**
- Modify: `tests/test_publications_research_view.py`
- Modify: `tests/test_update_publications_from_zotero.py`

**核心改动**：现有测试断言了旧的"Publications.rst 按年份、PublicationsByYear 按方向"结构，现在反过来了，要更新断言。

- [ ] **Step 1: 读现有断言，列出需要改的**

Run: `python3 -m unittest discover -s tests 2>&1 | grep "FAIL:\|ERROR:"`
记录所有失败的测试名。

- [ ] **Step 2: 更新 `test_publications_research_view.py` 的断言**

以下断言需要反转语义（文件 `tests/test_publications_research_view.py`）：
- `test_publications_page_links_to_research_view`：断言 Publications.rst（主视图）现在按方向分组，banner 指向"按年份"。`PublicationsByYear` 的 toctree 注册文字改为"按年份倒序浏览"。
- `test_research_view_groups_every_publication_by_family_then_subdirection`：现在测的是 Publications.rst（主视图），不是 PublicationsByYear.rst。断言的文件引用要对调。
- `test_research_view_uses_the_same_publication_expression_as_chronological_view`：引用一致性断言不变（两个视图引用文字仍应一致），但读取的文件角色对调。
- `test_publications_page_groups_early_papers_without_degree_theses`：这个断言现在要针对 PublicationsByYear.rst（按年份视图）。
- `_paper-notes-fragment` 相关断言（Task 3 会移除 section，这里先不碰）。

逐个修改断言里的文件常量（`PUBLICATIONS` vs `PUBLICATIONS_BY_YEAR`）和预期文字。

- [ ] **Step 3: 更新 `test_update_publications_from_zotero.py` 的断言**

- `test_page_header_matches_committed_publications_structure`：banner 文字从"按研究方向浏览"改为"按年份倒序浏览"。
- `test_student_training_section_is_sorted_by_graduation_date` 等不受影响（Teaching 页不变）。

- [ ] **Step 4: 运行全量测试**

Run: `python3 -m unittest discover -s tests 2>&1 | tail -5`
Expected: 全部 PASS（除了 `_paper-notes-fragment` 相关的，Task 3 处理）

- [ ] **Step 5: Commit**

```bash
git add tests/test_publications_research_view.py tests/test_update_publications_from_zotero.py
git commit -m "test: update assertions for thematic-as-main view swap"
```

---

### Task 3: 移除独立的论文精解 section，保留 toctree

**Files:**
- Modify: `tools/publications/artifacts.py`
- Modify: `docs/source/_paper-notes-fragment.rst`

**核心改动**：`_paper-notes-fragment.rst` 只保留 toctree（注册 paper-notes 页面），移除 `论文精解` section 和按方向分组的精解列表。

- [ ] **Step 1: 改 `render_paper_notes_fragment` 只输出 toctree**

在 `tools/publications/artifacts.py` 里，`render_paper_notes_fragment` 当前输出 toctree + 论文精解标题 + area。改为只输出 toctree：

```python
def render_paper_notes_fragment(root: Path) -> str:
    """Render the paper-notes fragment file owned by this tool.

    After the view swap, this fragment only holds the hidden toctree that
    registers paper-notes pages. The 论文精解 section was removed; deep-dive
    titles now appear inline in the Publications page (see
    update-publications-from-zotero.py).
    """
    return render_paper_notes_toctree(root).rstrip("\n") + "\n"
```

- [ ] **Step 2: 重新生成 fragment 并验证**

Run: `python3 tools/publications/artifacts.py --write`
Run: `cat docs/source/_paper-notes-fragment.rst`
Expected: 只有 toctree，没有 `论文精解` section。

- [ ] **Step 3: 更新 `page_header` 移除 fragment include（如果 fragment 为空则不 include）**

检查 `render_paper_notes_toctree` 是否返回空（如果没有 public artifacts）。如果 toctree 内容存在，`page_header` 的 `.. include:: _paper-notes-fragment.rst` 保留。如果 fragment 只有 toctree，include 保留即可（toctree 是 hidden 的，不影响正文显示）。

实际上 include 保留是对的——它注册 paper-notes 页面到 Sphinx 导航。不需要改 `page_header`。

- [ ] **Step 4: 更新 `test_publication_artifacts.py` 的 fragment 断言**

`test_write_regenerates_fragment_and_check_then_passes` 断言 fragment 含 `论文精解`——改为断言 fragment 只含 toctree（不含 `论文精解`）。

- [ ] **Step 5: 更新 `test_publications_research_view.py` 的 fragment 断言**

`test_publications_page_links_to_research_view` 里有断言 fragment 含 `论文精解`——移除或改为断言不含。

- [ ] **Step 6: 运行全量测试**

Run: `python3 -m unittest discover -s tests 2>&1 | tail -5`
Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add tools/publications/artifacts.py docs/source/_paper-notes-fragment.rst tests/
git commit -m "refactor: remove standalone 论文精解 section, keep toctree only"
```

---

### Task 4: 主视图里给有精解的论文加精解标题行

**Files:**
- Modify: `scripts/update-publications-from-zotero.py`

**核心改动**：在 `build_publications_rst`（现在按方向分组的主视图）里，对有精解的论文，在锚点块之后、引用行之前，插入一行精解标题（`* {year}: {精解标题}`，去掉方向前缀，作为 `:doc:` 链接）。

精解标题数据来源：从 `wechat/backlog/selected-papers.yml` 读 `zotero_key → publication_ref → 标题` 映射。标题去掉 `方向 | ` 前缀。

- [ ] **Step 1: 写失败测试——主视图有精解标题行**

在 `tests/test_update_publications_from_zotero.py` 加测试：

```python
def test_publications_rst_inlines_deep_dive_title_above_citation(self) -> None:
    items = [
        {"key": "CGKPKZ8I", "data": {"date": "2026", "title": "Fast prediction", "creators": [{"lastName": "Zhao", "firstName": "Peisheng"}], "publicationTitle": "Building Simulation"}, "bib": "Zhao P, Fast prediction[J]. Building Simulation, 2026.", "publication_number": 1, "anchor": "ref-zhao2026-BS"},
    ]
    research_map = {"CGKPKZ8I": {"research_family": "建筑结构抗风", "subdirection": "数值风洞与湍动入流"}}
    # Mock: the real backlog maps CGKPKZ8I -> ref-zhao2026-BS with a title
    # containing "数值风洞 | 我们如何用预计算 CFD 数据库加速城市微尺度风环境预测"
    page = self.updater.build_publications_rst(items, research_map)
    # Deep-dive title line appears above the citation, without direction prefix
    self.assertIn("我们如何用预计算 CFD 数据库加速城市微尺度风环境预测", page)
    # The title should be a :doc: link to the paper-notes page
    self.assertIn(":doc:`我们如何用预计算 CFD 数据库加速城市微尺度风环境预测 <paper-notes/ref-zhao2026-BS>`", page)
```

- [ ] **Step 2: 运行测试，确认失败**

Run: `python3 -m unittest tests.test_update_publications_from_zotero -v 2>&1 | tail -10`
Expected: FAIL（当前 `build_publications_rst` 不插入精解标题）

- [ ] **Step 3: 加精解标题映射加载函数**

在 `scripts/update-publications-from-zotero.py` 里加一个函数，从 backlog 读 `zotero_key → (publication_ref, title)` 映射，并去掉标题的方向前缀。这个函数用 `woeai.wechat.backlog.parse_backlog_papers`（已存在于共享包）：

```python
def load_deep_dive_titles() -> dict[str, tuple[str, str]]:
    """Return zotero_key -> (publication_ref, reader_title) for papers with deep-dives.

    The reader_title strips the direction prefix (e.g. '数值风洞 | ...' -> '...').
    """
    backlog_path = ROOT / "wechat/backlog/selected-papers.yml"
    if not backlog_path.exists():
        return {}
    from woeai.wechat.backlog import parse_backlog_papers
    result: dict[str, tuple[str, str]] = {}
    for paper in parse_backlog_papers(backlog_path):
        # Title format: "方向前缀 | 精解标题" or just "精解标题"
        title = paper.title
        if " | " in title:
            title = title.split(" | ", 1)[1]
        result[paper.publication_ref] = (paper.publication_ref, title)
    # We also need zotero_key mapping; read it from the raw backlog
    raw = _read_backlog_zotero_keys(backlog_path)
    # Map zotero_key -> (publication_ref, title)
    by_ref = result
    key_map: dict[str, tuple[str, str]] = {}
    for ref, zotero_key in raw.items():
        if ref in by_ref:
            key_map[zotero_key] = by_ref[ref]
    return key_map
```

注意：`parse_backlog_papers` 返回的 `BacklogPaper` 没有 `zotero_key` 字段。需要额外读 backlog 的原始 `zotero_key`。加一个 helper：

```python
def _read_backlog_zotero_keys(backlog_path: Path) -> dict[str, str]:
    """Return publication_ref -> zotero_key from the backlog."""
    mapping: dict[str, str] = {}
    current_ref = ""
    for raw in backlog_path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*-\s+publication_ref:\s+(\S+)", raw)
        if m:
            current_ref = m.group(1)
            continue
        m = re.match(r"\s*zotero_key:\s+(\S+)", raw)
        if m and current_ref:
            mapping[current_ref] = m.group(1)
    return mapping
```

- [ ] **Step 4: 在 `build_publications_rst` 里用映射插入精解标题行**

修改 `build_publications_rst`，在锚点块之后、引用行之前，检查 item 的 key 是否在 deep-dive 映射里。如果在，插入：

```python
def build_publications_rst(
    items: list[dict[str, Any]], research_map: dict[str, dict[str, str]]
) -> str:
    deep_dive_titles = load_deep_dive_titles()
    sections = [page_header({})]
    for family in RESEARCH_FAMILY_ORDER:
        sections.extend([family, "-" * 12, ""])
        for subdirection in RESEARCH_SUBDIRECTION_ORDER[family]:
            sections.extend([subdirection, "~" * 40, ""])
            for item in items:
                row = research_map[item["key"]]
                if row["research_family"] != family or row.get("subdirection") != subdirection:
                    continue
                for anchor in publication_anchor_targets(item):
                    sections.extend([f".. _{anchor}:", ""])
                dd = deep_dive_titles.get(item["key"])
                if dd:
                    pub_ref, dd_title = dd
                    year = extract_year(item["data"].get("date"))
                    sections.append(f"* {year}: :doc:`{dd_title} <paper-notes/{pub_ref}>`")
                    sections.append("")
                sections.extend([rendered_entry(item, item["publication_number"]), ""])
    return "\n".join(sections).rstrip() + "\n"
```

- [ ] **Step 5: 运行测试，确认通过**

Run: `python3 -m unittest tests.test_update_publications_from_zotero -v 2>&1 | tail -10`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add scripts/update-publications-from-zotero.py tests/test_update_publications_from_zotero.py
git commit -m "feat: inline deep-dive titles above citations in thematic view"
```

---

### Task 5: 重新生成页面、更新 CONTEXT.md、全量验证

**Files:**
- Regenerate: `docs/source/Publications.rst`, `docs/source/PublicationsByYear.rst`
- Modify: `CONTEXT.md`
- Run: `./scripts/check-docs.sh`

- [ ] **Step 1: 重新生成两个页面**

Run: `python3 scripts/update-publications-from-zotero.py`
Expected: 写入 Publications.rst（按方向 + 精解标题）、PublicationsByYear.rst（按年份）。

- [ ] **Step 2: 人工检查生成结果**

Run: `head -60 docs/source/Publications.rst`
确认：banner 指向"按年份倒序浏览"；按方向分组；有精解的论文引用上方有标题行。

Run: `head -30 docs/source/PublicationsByYear.rst`
确认：标题"按年份倒序浏览"；有 banner 指回学术成果页；按年份分组。

- [ ] **Step 3: 跑完整门禁**

Run: `./scripts/check-docs.sh`
Expected: `build succeeded` + 所有测试 PASS。

- [ ] **Step 4: 更新 CONTEXT.md**

更新以下词条的语义描述（哪个是主视图、哪个是子视图交换了）：
- `Chronological Publication View`：现在描述"按年份倒序浏览"是**子视图**（`PublicationsByYear.rst`，但语义是按年份），文件名保留但标题改为"按年份倒序浏览"。
- `Thematic Publication View`：现在描述"按研究方向浏览"是**主视图**（`Publications.rst`），在 toctree 里是默认入口。
- `Academic Outputs`：更新描述——默认按研究方向展示，论文精解标题融入引用。
- `Paper Deep-Dive Area`：更新——不再有独立 section，精解标题融入期刊论文列表。

- [ ] **Step 5: 更新测试里的文件角色断言（如果有遗漏）**

Run: `python3 -m unittest discover -s tests 2>&1 | grep "FAIL:\|ERROR:"`
修复任何遗漏的断言。

- [ ] **Step 6: Commit**

```bash
git add docs/ CONTEXT.md scripts/update-publications-from-zotero.py tests/
git commit -m "feat: swap default publications view to thematic, inline deep-dive titles"
```

- [ ] **Step 7: 推送**

```bash
git push origin main
```
（如 HTTPS 超时，用 `git push git@github.com:lichao689/woeai.git main`）

---

## Self-Review

**Spec coverage:**
- 需求 1（交换默认视图）：Task 1 交换分组逻辑 + Task 2 更新测试 ✓
- 需求 2（精解标题融入引用上方，只在主视图）：Task 4 插入精解标题行 + Task 3 移除独立 section ✓
- 精解标题去方向前缀：Task 4 Step 3 的 `split(" | ", 1)[1]` ✓
- 按年份视图不加精解标题：Task 4 只改 `build_publications_rst`（主视图），不改 `build_publications_by_year_rst`（年份视图）✓

**Placeholder scan:** 无 TBD/TODO，每个步骤都有具体代码或命令。

**Type consistency:** `build_publications_rst` 签名从 `(items)` 改为 `(items, research_map)`，`build_publications_by_year_rst` 从 `(items, research_map)` 改为 `(items)`——write_outputs 调用在 Task 1 Step 6 同步改 ✓。`load_deep_dive_titles` 返回 `dict[str, tuple[str, str]]`，在 Task 4 Step 4 用 `.get(item["key"])` 解包 ✓。

**风险点：**
1. `publication_number` 编号——交换后主视图（按方向）拥有 `[N]` 编号，年份视图用 `:ref:` 链接。编号仍由 `assign_publication_numbers` 统一分配（在 write_outputs 里，按 items 顺序），不受分组方式影响。✓
2. 首页"最新学术进展"——由 artifacts.py 的 `render_latest_paper_notes` 生成，数据源是 backlog + rst 标题，不受视图交换影响。✓
3. `_paper-notes-fragment.rst` 的 `LATEST_MARKER`（首页）——不受 fragment section 移除影响（LATEST_MARKER 在 index.rst，不在 fragment）。✓
