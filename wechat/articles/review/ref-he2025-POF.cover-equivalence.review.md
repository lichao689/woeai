# ref-he2025-POF 公众号专用封面整合与非内容等价性复核

## 源文件获取记录

沿用 [ref-he2025-POF.review.md](ref-he2025-POF.review.md) 中已核验的获授权论文来源。
来源登记及源副本 SHA-256 保持不变；本轮不下载、替换或重新审计 PDF。
科学核验基准为 `86bc3ed2354c9e5d296f9b9326bd601f65eede24`。

## 关键事实证据定位记录

原科学审校记录中的 PDF 物理页码、图号、式号、表格及全文覆盖证据保留。
旧指纹因新增素材和共享 review 元数据改变而失效，须经本轮等价性复核后续验。
本轮逐字节核对 RTD 源文件、全部基准公开资产、原科学审校内容及来源登记，
并检查原 RTD 指纹的每个文件输入：仅新增最终公众号封面、变更主 review 的封面路径，
其他输入和全文规范均保持原字节。原指纹在纯基准输入上重新计算仍与历史记录一致。
只有主 review 的 wechat_cover_image 字段切换；rtd_cover_image 和科学审校文字不变。
公众号的分类前缀、独立方向说明与 AI 辅助声明另见
[ref-he2025-POF.taxonomy.review.md](ref-he2025-POF.taxonomy.review.md)。排除这些已授权编辑差异后，
公众号科学正文、摘要、公式、原图和作者名单与基准逐字节一致。

## 最终路由与冻结输入

- 公众号封面：`wechat/assets/public-safe/ref-he2025-POF/cover-wechat-900x383-20261014-v5.png`。
- 新封面 SHA-256：`597a68db4ed6449b356883c0d5194ed3917e7db96451058040cd6f2526e18eb7`；实测画布 900 × 383。
- RTD 封面保持：`wechat/assets/public-safe/ref-he2025-POF/cover-wechat-900x383-imagegen-v1.png`。
- RTD 封面 SHA-256：`5aebd52c6acf1e3a713615d2b4f340bfd9485d6b28ffffb4d3029224fff63328`，与基准一致。
- 封面 brief：`wechat/articles/review/ref-he2025-POF.cover-brief.md`；SHA-256：`df138bf32e2b3e7f380d249e7377783eea9e2c979f5ca326642166ade6f3bce4`。
- 该篇目录原有 40 个公开资产全部保持原字节，只新增上述 1 张公众号封面。
- 旧封面和未选历史素材保留，不删除、不改写，也不把新增公众号封面用于 RTD。

## 科学内容等价性证据

- 来源登记 SHA-256：`4e379ed89ebfd6070d5cb7d9b03a4b6a2e368073aac3ed30dac91ece232dd7e3`，与基准对象相同。
- RTD 源文件 SHA-256：`e60f76b9b22cc1bcea94fe2eeec8b34a4055e6aab2cc3a4f75de3ed25c431c58`，与基准完全一致。
- 主 review 基准 SHA-256：`ff6a30753a1b6163c63432f27335014980706c059379b4887b2fba750397e88c`。
- 仅切换公众号封面路径后的主 review SHA-256：`c3dc315de5a4efde23b72b5a12530da4a163953de713cdcc44690843b9c3f283`。
- 移除 wechat_cover_image 单行后，两版主 review 文本完全相同。
- 当前公众号 Markdown SHA-256：`3b236cd47b4048e2d24cd4345312a855498b06ae3979e03e9d36ef1436790e30`；5 项正文原图路径不变。
- 定向分类与 AI 声明记录 SHA-256：`d96382b05469afdfe98f6472824c06a2c5af3dff786d45ef3ecf99dfe054631b`。

## 审核范围与状态

17 张最终封面及 brief 已冻结，封面独立本地视觉与概念表达边界检查通过。
新工程图只作概念示意，不作为论文测量云图或几何的精确复刻；本记录不以封面
视觉通过替代正文原图证据或微信手机预览。

本轮路由与科学内容等价性的独立复核已通过。原 RTD verified 记录和公众号
历史投递证据完整保留；本轮据此一次性建立新指纹，不宣称新的全文 PDF 审计。
公众号仍停在 awaiting_review；实际后台成功结果由逐篇官方回读回执单独证明，
本记录不把排队或本地预检视作上传完成。浅色、深色手机预览均未由本轮执行。
