# ref-li2022-SOS 公众号专用封面整合与非内容等价性复核

## 源文件获取记录

沿用 [ref-li2022-SOS.review.md](ref-li2022-SOS.review.md) 中已核验的获授权论文来源。
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
[ref-li2022-SOS.taxonomy.review.md](ref-li2022-SOS.taxonomy.review.md)。排除这些已授权编辑差异后，
公众号科学正文、摘要、公式、原图和作者名单与基准逐字节一致。

## 最终路由与冻结输入

- 公众号封面：`wechat/assets/public-safe/ref-li2022-SOS/cover-wechat-900x383-20261014-approved.png`。
- 新封面 SHA-256：`e3aec006fd0c654a90914848408eec6b14e5fa8f00752bf919933e4d8dd030ff`；实测画布 900 × 383。
- RTD 封面保持：`wechat/assets/public-safe/ref-li2022-SOS/cover-wechat-900x383-imagegen-v1.png`。
- RTD 封面 SHA-256：`050ad867136fdc19ab7605c837dcfa073c431777486353dad4cb28ebb9fc6a6c`，与基准一致。
- 封面 brief：`wechat/articles/review/ref-li2022-SOS.cover-brief.md`；SHA-256：`bb04bdfbe1b15d6320dce5825da73ffb4c8945b749dd0db8c5152432af6cdc4e`。
- 该篇目录原有 31 个公开资产全部保持原字节，只新增上述 1 张公众号封面。
- 旧封面和未选历史素材保留，不删除、不改写，也不把新增公众号封面用于 RTD。

## 科学内容等价性证据

- 来源登记 SHA-256：`8296a688d5f2860f6fedfc934527f318d52a050c841f19c00d1c79d20dfa861d`，与基准对象相同。
- RTD 源文件 SHA-256：`e6d22e71b287ed7288350f882deb7bced475e35ea7b6a78d64aea0264724fd2a`，与基准完全一致。
- 主 review 基准 SHA-256：`e3def75f8fbe982c7c92b827907516042c1919bef70ec67eab87b9c4eb941743`。
- 仅切换公众号封面路径后的主 review SHA-256：`9a0d3ae924a7f392b4de2d1a503f0e3670ed7939ee4237c575977478e65cc487`。
- 移除 wechat_cover_image 单行后，两版主 review 文本完全相同。
- 当前公众号 Markdown SHA-256：`4f762beb82860cfd5ce5947c2f6a484892219fa34c4d0f947414c4045178a1ba`；4 项正文原图路径不变。
- 定向分类与 AI 声明记录 SHA-256：`1a03afb31d36934f7ad59a33935fa1dfebc2831240a8d4d8915b94831bdb4428`。

## 审核范围与状态

17 张最终封面及 brief 已冻结，封面独立本地视觉与概念表达边界检查通过。
新工程图只作概念示意，不作为论文测量云图或几何的精确复刻；本记录不以封面
视觉通过替代正文原图证据或微信手机预览。

本轮路由与科学内容等价性的独立复核已通过。原 RTD verified 记录和公众号
历史投递证据完整保留；本轮据此一次性建立新指纹，不宣称新的全文 PDF 审计。
公众号仍停在 awaiting_review；实际后台成功结果由逐篇官方回读回执单独证明，
本记录不把排队或本地预检视作上传完成。浅色、深色手机预览均未由本轮执行。
