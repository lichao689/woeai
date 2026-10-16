# 论文源文件与证据记录

本指南是论文源文件获取、PDF 选择、证据定位与原图抽取的唯一规则来源。
公众号导读（`.agents/skills/wechat-paper/references/writing-standards.md`）、RTD 论文精解
（[paper-deep-dive-rst.md](paper-deep-dive-rst.md)）和两个技能文件只引用这里，
不再各自复述。凭据、API 与草稿操作见 [wechat/README.md](../../wechat/README.md)。

## 1 获取顺序

1. **先查当前工作区。** 检查被忽略的 `wechat/.local/` 私有存储及其 manifest。
   期刊 PDF 可能位于 `journal-papers/<ZoteroKey>/source.pdf` 或
   `<publication_ref>/source.pdf`。以实际文件为准；新克隆不会恢复私有源文件，
   历史清单也不代表当前可用。
2. **核对 Zotero 元数据。** 在可访问时读取 DOI、`abstractNote` 与附件记录。
   Zotero Desktop Local API 只存在于用户本人的桌面，不是云端前提；不可用时
   如实记录，不声称做过桌面检查。
3. **用获授权 PDF 或作者稿核实正文。** 摘要、图、图题、公式和结论均回到原文。
4. **源文件缺失时**，仅在已授权的情况下尝试 Zotero Web API `/file`，下载结果
   放在私有存储。仍不可得时记录 `需要同步 PDF 或提供作者稿` 并停止依赖
   PDF 的工作。摘要或公众号稿不能替代 RTD 全文精解所需的原文。

网页只用于核对公开元数据（DOI、期刊页面）。不得自动从出版社页面、DOI 落地页、
Google Scholar、ResearchGate、Sci-Hub 或搜索结果抓取 PDF。只有用户明确批准某个
具体、公开、合法的来源（OA PDF、作者稿、用户给出的链接）时才可下载，下载件
放在 `wechat/.local/<publication_ref>/` 等私有路径，不提交，并在 review 记录来源
与批准情况。

只读的论文阅读和页面生成不得读取 Zotero 写入凭据。

## 2 多个 PDF 附件的选择

正文证据和原图按以下优先级选源：

1. 作者终稿 / 作者稿
2. 出版社正式版（version of record）
3. 开放获取平台 PDF
4. 预印本
5. 其他附件

使用低优先级来源时，在 review 写明高优先级来源缺失、不可读、法律上不安全或
图像不适用的原因。期刊、年份、卷期、页码、DOI 和出版状态始终以 Zotero 元数据
和正式出版记录为准，不由预印本覆盖。

## 3 身份与哈希

使用前核对论文身份、来源版本、复用状态和 manifest。原始来源 SHA-256 与下载副本
SHA-256 分开标注；未逐字节比对时，图书馆传输哈希不能证明与原始文件一致。
哈希、私有路径与 manifest 只放私有记录或注册表允许的字段。

## 4 review 中必须有的两节

每个 `wechat/articles/review/*.review.md` 必须包含以下两个二级标题，
`scripts/check-public-safe-content.py` 会检查。

### `## 源文件获取记录`

至少记录：元数据来源、附件记录状态、本地 PDF 状态、已选 PDF 类型及低优先级原因、
私有存储类别（只写类别，不写绝对路径）、Zotero Web API `/file` 是否尝试、
是否使用网页下载及批准记录、摘要依据、正文证据依据、图片依据。

### `## 关键事实证据定位记录`

不必逐句标注，但要让人工复核能快速定位：

- 摘要来源与位置；
- 核心结论、文中引用的数字及其条件：`PDF file page N`、章节、表号；
- 所用图：`PDF file page N` 与原图号；
- 所用公式：原文公式写 `PDF file page N` 与原式号；文章为解释而新增的公式
  标为“编辑解释式”，并指向它所解释的原文证据。

页码一律用 PDF 文件物理页码，写作 `PDF file page N`，不用期刊印刷页码。
尚未核页时写 `pending PDF page audit`，不要猜。

原文内部矛盾（数字、引用、公式、图题与正文不一致）时，两处位置都记下，正文保留
原文并标明差异，不暗中“修正”原论文。

## 5 原图抽取

团队作者已确认的论文，可直接使用论文 PDF 或作者稿中的原图；其他论文需确认复用
权利后才可提交图片。

1. 先用 `pdfimages -all` 抽取嵌入图像。
2. 原图被拆成有序条带时，按页面顺序拼回完整图，不重采样原生像素。
3. 只有矢量图、无法从嵌入图像恢复或需要周边矢量标注时，才用页面渲染裁切。
4. 最终公开素材放 `wechat/assets/public-safe/<publication_ref>/`；临时文件放
   `wechat/.local/<publication_ref>/`。
5. 与原 PDF 页逐幅对照：分图、坐标轴、色标、图例完整，不混入邻近正文或其他图。

只有原图缺失、法律上不安全、分辨率不足或不适合手机显示时才重绘。
图片来源、抽取方式与复用状态记在 review，不写进读者正文。

## 6 公开安全

公开仓库中不得出现：源 PDF、原始抽取全文、整页渲染、私有 manifest、绝对私有路径、
附件标识、凭据、cookie、API 原始返回、本地预览 HTML。review 文件同样公开，
使用存储类别和证据定位，不使用私有路径或长段原文。
