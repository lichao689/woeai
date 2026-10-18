# 首页 UI 改进规划与原型（设计评审稿）

日期：2026-10-18。范围：`docs/source/index.rst`、`docs/source/_templates/home.html`、
`en-home.html`、`brand-header.html`、`docs/_static/custom.css`。
原型：`project/prototypes/2026-10-18-home-v2/index.html`（可直接打开，未接入 Sphinx）。

事实边界仍以 `CONTEXT.md` 与 [homepage-content.md](../guides/homepage-content.md) 为准。

## 0 更正

上一版把"390px 下 H1 与正文横向溢出"列为 P0 缺陷，**该判断有误，已撤回**。

原因：先前用 `Google Chrome --headless --window-size=390` 截图，macOS 上该参数的最小窗口宽度
被钳制在 485px，于是 485px 宽的排版被塞进 390px 宽的图片，看起来像被裁切。
改用 Playwright 设定真实视口（390×844）复测：

| 指标 | 当前站点 | 原型 v2 |
| --- | --- | --- |
| 390px `scrollWidth / clientWidth` | 390 / 390 | 390 / 390 |
| 390px 溢出元素 | 0 | 0 |
| 390px H1 | 346×101（两行，40.56px） | 350×46（一行，35.1px） |
| 1440px H1 | 630×62（50px） | 543×55（46px） |

即：当前站点在真实 390px 下**没有横向溢出**，H1 只是折成两行。
之前关于"微信里会直接暴露"的推断同样不成立。

## 1 我实际看到的

- 技术形态：Sphinx + `sphinx-rtd-theme`，首页用独立 `home.html` 模板脱离 RTD 阅读外壳，
  内页保留 RTD 侧栏；导航由 `brand-header.html` 共享；视觉规则集中在 `custom.css`（529 行）。
- 首页 6 个区块：首屏 → 两条研究主线 → 精选研究（6 卡）→ 工程应用（3 项）→
  近期学术进展（3 条）→ 交流与合作。
- 整页高度：1440px 下 4889px；390px 下 9891px。
- 配色仅两组：纸色 `#f6f7f4` + 深青 `#13556c`，唯一色块是 `method-strip` 的 `#eaf0ef`。
- 卡片统一白底 + 1px `#d8e0df` 边 + 直角，无阴影。

优点（改动中应保留）：定位句具体、不堆形容词；成果卡强制写"问题/贡献"；
配色克制、无动效；`skip link`、`aria-*`、`focus-visible`、44px 触控目标都到位；
生成示意图明确标注"非研究数据"。

## 2 诊断

### P0 影响观感与阅读成本

| 编号 | 现象 | 证据 |
| --- | --- | --- |
| P0-1 | 六张成果卡把论文原图当缩略图，视觉重量差 4 倍 | 原图宽高比 1.17 / 1.20 / 2.47 / 2.50 / 2.98 / 4.48，统一 `height:190px; object-fit:contain`；渲染宽度从 223px 到 851px 不等 |
| P0-2 | 六个区块同构，没有节奏峰 | 每块都是 `eyebrow + h2 + 右上链接 → 卡片`，重复 5 次；区块间距统一 `padding:62px 0` |
| P0-3 | 移动端滚动成本高 | 390px 下整页 9891px；其中 6 张成果卡各含 190–200px 高的图片 |

### P1 结构与细节

1. **字号阶梯断档**：小字 10/11/12/13/14/15/16 共 7 档密集分布，之后直接跳到 20/25/29/50。
   缺 18–22 的过渡；`figcaption`、`card-index` 的 10px 中文尤其难读。
2. **三 CTA 同级**：首屏"浏览代表成果 / 研究方向 / 交流与合作"并列，主次只靠实心与描边区分。
3. **中英首页是两套结构**：`index.rst` 6 区块、有图；`en-home.html` 4 区块（缺工程应用与
   近期进展）、全部无图、hero 文案另写。同一份事实维护两处。
4. **色彩缺少"证据色"**：关键结论（1:70 风浪联合试验、Pareto 优化）没有任何视觉标记。

### P2 维护债

- 死样式：`.hero-evidence`、`.hero-urban`、`.hero-platform`、`.profile-title`、
  `.contact-qr`、`.member-status-current/graduated` 已无对应元素。
- `html[lang="zh-CN"] .hero-title-subject{font:inherit}` 让 19px 副标题样式失效，
  `span` 规则成了死代码。
- 图片 `alt` 写成"原文图25"这类内部标记，对屏幕阅读器没有信息量。

## 2.4 精选研究与近期学术进展的关系（补充）

事实核对：

| 位置 | 内容 | 行号 |
| --- | --- | --- |
| `index.rst` | `id="selected-work"` 精选研究：问题与贡献，6 张卡（含图、问题、贡献、书目） | 33–39 |
| `index.rst` | `id="latest-progress"` 近期学术进展，3 条论文精解链接（构建时生成） | 54–67 |
| `docs/_build/html/index.html` | 两段均存在 | — |

结论：**近期学术进展没有替换精选研究**，当前是两段并存。
如果目标是"只留一段"，两种做法：

1. 保留精选研究（信息量更大，能承载"问题/贡献"），把近期进展降为精选研究顶部的一行
   "最新：三篇新精解"链接。
2. 保留近期学术进展，删掉 6 张卡。代价是首页失去唯一带"问题/贡献"结构的证据区，
   招生与工程合作读者少了一层判断依据。

## 3 定位与命名：实验室，直接用 WOEAI

已确认采用「实验室 / Lab」。

**不再另造缩写。** `WOEAI` 本身就是 `Wind and Ocean Engineering with AI` 的缩写，
实验室名直接展开它即可，多造一个 WOSL / WOEL 只会让读者多记一个词。

| 项 | 内容 |
| --- | --- |
| 中文全称 | 风与海洋工程人工智能实验室 |
| 英文全称 | Wind and Ocean Engineering with AI Laboratory |
| 缩写 | WOEAI（沿用现有品牌，不新增） |
| 口语 / 小标 | WOEAI 实验室 / WOEAI LAB |
| 现有品牌 | WOEAI（站点、公众号、域名 `winddee.cn`） |

中文名的其他写法与取舍：

- **风与海洋工程人工智能实验室**（采用）：与 WOEAI 逐词对应，正式场合可用。
- 风与海洋工程 AI 实验室：更短，适合页眉或小标；中英混排做正式名称略随意。
- 风与海洋工程智能实验室：不推荐。"智能实验室"容易被读成智慧实验室（物联网、门禁那类），
  且"智能"不等于 "with AI"。
- AI 赋能风与海洋工程实验室：不推荐。`homepage-content.md` 把"赋能"列为应避免的空话，
  它可以留在 H1 的位置句里，但不适合做机构名。

命名注意事项：

- 中文"实验室"在多数高校语境里指向建制单位（全国重点实验室、省部共建、校级实验室）。
  本实验室没有对应建制，名称要避开"重点""国家""中心"这类词；对外首次出现时说明是研究团队。
- 英文 `Lab` 在 AI 圈是通用品牌词（Stanford AI Lab、BAIR、CSAIL，乃至单个 PI 的 "XX Lab"），
  不承担建制含义，可放心使用。

### 3.1 品牌层级

- `WOEAI` 同时承担品牌与缩写，不再区分。
- 中文全称用于页眉副行、页脚、About、招聘页、论文署名等正式位置。
- `WOEAI 实验室` 用于正文复指，`WOEAI LAB` 用于首屏小标。
- 首屏大标题仍留给研究定位（"AI 赋能风与海洋工程"），不塞机构名。

## 4 原型做了什么

原型：`project/prototypes/2026-10-18-home-v2/index.html`（单文件，内联 CSS，复用现有图片）。

1. **首屏**：`eyebrow` 改为 `风与海洋工程人工智能实验室 / WOEAI LAB`，H1 保持研究主题，
   H1 与三行提要的字号关系从 50/29 改为 46/23（不再像两个标题）；
   CTA 收敛为 1 主 + 1 次 + 1 文字链；负责人 byline 带细分割线。
2. **研究方向去图**：改用大号序号（01/02）+ 英文小标 + 标签 + 方法段承担结构，
   彻底绕开 `object-fit:contain` 的留白与比例问题。
3. **精选研究改"1 大 5 小"**：首篇做横向卡（图 16:10 + 问题/贡献），
   其余 5 篇改为列表行（年份 / 标签 / 标题 / 一句话 / 期刊 / 两个链接）。
4. **底色分层代替阴影**：纸白与纯白交替，保持直角与 1px 线，不加圆角与投影。
5. **间距三级化**：88 / 64px 两档 + 首屏 84px，替代统一 62px。
6. **深色收口**：交流与合作改为深青整幅，白字 + 白底主按钮，页面有明确结尾。
7. **一个强调色**：暖赭 `#a4632c`，只用于区块序号与标签，不超过 20 处。
8. **字号阶梯收敛**：最小 11px，删掉 10px 与 12px 档。

实测对比：

| 指标 | 当前 | 原型 v2 |
| --- | --- | --- |
| 1440px 整页高度 | 4889px | 4668px |
| 390px 整页高度 | 9891px | 7115px（−28%） |
| 横向溢出 | 无 | 无 |
| 390px H1 行数 | 2 行 | 1 行 |

## 5 约束（不得越界）

- 事实边界：不放个人照片、不复述机构/学院/地址/行政职务、不新增联系方式。
- 样式改动只进 `docs/_static/custom.css`，页面不写内联样式。
- 不改论文锚点、`paper-notes/<ref>.html` URL、侧栏层级。
- 改完跑 `./scripts/check-docs.sh`；只改样式时不改 Site Build ID。

## 6 落地顺序（原型确认后）

1. 把原型 CSS 映射进 `custom.css`，用 `.woeai-home-page` 作用域包住，不污染内页。
2. 改 `index.rst` 的区块结构与 `home.html` 模板；保留现有锚点
   `research-lines` / `selected-work` / `applications` / `latest-progress` / `join-contact`。
3. 精选研究从 6 卡改 1 大 5 小后，`paper-record-slot` 的展开书目需要重新验证
   （列表行不再有卡片容器）。
4. 同步 `en-home.html` 到同一结构，或抽出共享区块模板。
5. 跑 `./scripts/check-docs.sh`，并在 390 / 768 / 1440 三档人工复核。

## 7 待确认（已全部关闭）

- **精选研究与近期学术进展并存**（见 §2.4）。当前 `index.rst` 第 33 行是"精选研究：问题与贡献"
  （6 张卡），第 54 行是"近期学术进展"（3 条），两者都在，构建产物里也是两段。
  两段内容有重叠：`ref-zhao2026-BS` 同时出现在精选研究第 1 张卡与近期进展第 1 条。
  需要确认是"保留两段"还是"只留一段"。
- 精选研究是否接受"1 大 5 小"（会牺牲两张配图）。
- 深色收口区块已确认保留。

**关闭情况**：上游已用"近期学术进展"整体替换"精选研究"（`55f27d6`、`490d14e`），
所以 §4.3 的"1 大 5 小"和 §6.3 的 `paper-record-slot` 复验都不再适用——
现行结构是两条主线各三张等权卡片，由 `woeai/publications/homepage.py::render_home_progress`
在 `.. BEGIN/END GENERATED LATEST PAPER NOTES` 之间生成，不手工改这六张卡。
深色收口保留，已落地。

## 8 落地结果（2026-10-18，已通过门禁）

落地到上游新版首页，改动四个文件：

| 文件 | 改动 |
| --- | --- |
| `docs/source/index.rst` | 首屏 `eyebrow` 改为 `风与海洋工程人工智能实验室 / WOEAI LAB`；`本课题组`→`本实验室`；`课题组负责人 李朝`→`实验室负责人 李朝`；删除两条研究主线下方的两张概念示意图 |
| `docs/_static/custom.css` | 新增 v2 样式段（交替底色带、88/64px 间距、深色收口、等权卡片）；删除 `.direction-figure` / `.direction-image` 四条失效规则 |
| `docs/source/_templates/en-home.html` | 同步删除两张概念示意图，保持中英两版结构一致 |
| `tests/test_rtd_homepage_projects_redesign.py` | 身份断言改为 `<strong>实验室负责人 李朝</strong>`；`test_direction_concepts_…` 换成 `test_direction_cards_are_text_led_in_both_languages` |

### 8.1 关于两张示意图（结论：移除）

判断依据不是"好不好看"，是**信息权重错配**：

1. 两张图是 1440×811 的柔和渲染图，`object-fit: contain` 后在 608px 宽的卡里只占
   约 342px 高，却因为是**唯一的彩色大块**，抢在 `01 / STRUCTURAL WIND ENGINEERING`
   之前被读到——访客先看到"一张图"，再看到"这里在讲什么研究"。
2. 研究主线区块的功能是**说清两条线各研究什么、AI 方法在哪一步起作用**。文字已经承担了
   这件事（标题 + 一句话定位 + 标签 + 方法段 + 证据链接），图片只是重复了同一件事的
   低分辨率版本。
3. 首屏已经有一张信息量更高的概念图（`english-research-hero-v2.webp`，含城市风场、
   半潜平台、波浪系泊）。同一页第二、第三张同风格概念图会稀释首屏那张的权重。
4. 图注写的是"AI 生成的科研概念示意 · 非研究数据"——它承认自己不是证据，而它所在的
   位置是"研究方向"这个最需要可信度的区块。

移除后该区块 1440px 下高 820px（含标题与方法条），两张卡 608×457，卡片内以
`01 / STRUCTURAL WIND ENGINEERING`（暖赭 11px）起头，正文承接。

如果以后仍想保留视觉线索，替代方案按推荐度排序：

1. **不给图**（当前）：文字主导，最快读到研究内容。
2. **缩成卡内小图**（120×68 缩略图放 `card-index` 右侧）：保留视觉锚点，不抢标题。
3. **换成真实成果图**（论文里的风场云图、平台网格、试验照片）：图注可以写实，
   不再是"概念示意"，但要过 `check-public-safe-content.py`。

### 8.2 落地过程中修掉的两个问题

- **两张方向卡不等高**。`align-items: start` + 固定 `margin-top: 22px` 会让卡片各自
  按内容收缩，右卡三个标签、左卡两个标签，底部边缘差 23px，两个 CTA 也不在同一基线。
  改为网格 `align-items: stretch` + CTA `margin-top: auto`：两卡同为 608×457，
  CTA 顶部都在 1364px。
- **`.site-skip` 造成的截图假象**。主题的"跳到主要内容"是 `position: fixed; top: -100px`，
  用 Playwright 的**元素截图**截一个高于视口的区块时，固定元素会被画到错位处，
  在移动端裁图上压住了 `01 /`。改用 `page.screenshot({clip, fullPage:true})` 并先滚动
  预加载 `loading="lazy"` 图片后消失。**这是截图方法的问题，不是页面缺陷**——
  与 §0 那次"假溢出"同类，记录在此避免重复踩。

### 8.3 实测（构建产物，非原型）

| 指标 | 上游新版 | 落地后 |
| --- | --- | --- |
| 1440px 整页高度 | 4887px | 4519px |
| 390px 整页高度 | 10129px | 9112px |
| 横向溢出（1440 / 390） | 无 | 无 |
| 方向卡（1440） | 不等高 | 608×457 ×2，CTA 同基线 |

门禁：`./scripts/check-docs.sh` → 293 tests OK（1 skipped），`sphinx-build -W` 通过。

### 8.4 复核截图

`project/prototypes/2026-10-18-home-v2/landed-{desktop,mobile}-{hero,research,work,join,full}.png`
由 `shoot-landed.js` 对 `/tmp/woeai-sphinx-html` 的构建产物生成，可随时重跑。
这些 PNG 已加入 `.gitignore`（`project/prototypes/**/*.png`），不进公开仓库；
原型 HTML 与截图脚本保留在仓库里，方便复现。

### 8.5 英文站同步（同批完成）

中文站改叫"实验室"后，英文站若仍写 `research group` / `group leader`，两版会互相矛盾。
同批做了术语替换（只换称谓，不改任何事实），并删掉两张概念图后不再引用的图片文件：

| 文件 | 改动 |
| --- | --- |
| `docs/source/_templates/en-home.html` | 小标补全为 `WIND AND OCEAN ENGINEERING WITH AI LABORATORY`；H1 `Research group` → `WOEAI Lab`；`Our research group` → `Our laboratory`；`Group leader` → `Laboratory lead`；联系段 `joining the group` → `joining the laboratory` |
| `docs/source/en/index.rst` | 标题 `WOEAI \| Research group` → `WOEAI \| WOEAI Lab` |
| `docs/source/en/Research.rst` | `Our research group studies` → `Our laboratory studies` |
| `docs/source/en/Publications.rst` | `group leader’s` → `laboratory lead’s` |
| `docs/source/en/JoinUs.rst` | 4 处 `group` → `laboratory`（含页脚 `Laboratory lead’s official profile`） |
| `docs/source/_templates/home.html` | 页脚副行补全为 `Wind and Ocean Engineering with AI Laboratory`；英文免责声明 `Research group website` → `WOEAI Lab website` |
| `docs/source/english_site.py` | meta description 改为 `WOEAI Lab studies … Laboratory lead: Chao Li.` |
| `tests/test_english_site.py` | 断言改为 `WOEAI Lab` / `Laboratory lead`，并加 `assertNotIn('the group', join)` 防止回退 |
| `docs/_static/home/research-*-concept-v1.webp` | **删除**（全站无引用） |

`GroupNews.rst`（`:orphan:` 的中文页）里那句英文 "The group published work on …" 未改：
它属于中文站的内容，不在本次英文站范围内。CSS 类名 `.group-lead` 也保留——
它只是样式钩子，改名要同时动模板和样式，收益为零。

英文首页实测：1440px 首屏 704→676px（H1 变短），整页 4288→4286px；390px 无横向滚动。


## 9 本轮审核整合与图片纠正（2026-10-18）

本轮按用户明确要求整合上述已落地UI，保留实验室称谓、文字主导的研究方向卡、
两图删除、交替底色和深色收口；不恢复已关闭的“1大5小”或重复进展栏目。
首屏补明其为研究团队，权威首页指南同步。旧独立原型仅为历史设计探索，不作为发布内容。

图片核查区分三种用途：研究方向概念图、首页解读封面、公众号正文科研图。
原首页五张封面精确匹配旧 `rtd_cover_image`，与当前公众号封面不同；QHDXXB原无图。
经官方API只读核对六篇原草稿的账号绑定和实际文章索引，并读取封面永久素材，
六张900×383封面均与当前公开审稿的 `wechat_cover_image` 字节一致。
因此最小修复为五张换成现稿已批准版本并补齐QHDXXB封面，不改公众号、不重做图片；
中英文共用静态副本，新增字节一致回归。卡片保留完整900×383比例，避免固定高度裁字。
正文图核对另存本机脱敏回执，不把缩略图、平台转码差异直接判成旧科学图。


## 10 用户追加：全库单源封面

目录盘点为44篇71个封面源，均受Git跟踪；17篇旧分渠道选择导致分叉。
44篇官方后台永久素材与当前公众号批准源逐字节相同。统一为每篇 `cover.png`，
删除工作树中27个多余版本；同字节源迁移不新生成或编辑图像。
当前review仅保留 `cover_image`，旧字段/历史正文不得回退；RTD仅改顶部路径，
不重生独立全文。首页副本直接由Sphinx写入构建输出，不再手工跟踪。
按独立非内容等价复核续接有效证据，保留旧审校、4篇原失效状态、全部科学图及私有资料。
