# ref-tang2025-JBE 公众号专用封面整合与非内容等价性复核

## 源文件获取记录

沿用 [ref-tang2025-JBE.review.md](ref-tang2025-JBE.review.md) 中已核验的获授权论文来源。
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
[ref-tang2025-JBE.taxonomy.review.md](ref-tang2025-JBE.taxonomy.review.md)。排除这些已授权编辑差异后，
公众号科学正文、摘要、公式、原图和作者名单与基准逐字节一致。

## 最终路由与冻结输入

- 公众号封面：`wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-20261014-v5.png`。
- 新封面 SHA-256：`84ca93b386b5a9800cea6ab0acd50074cd5eb45b5406c07ade425a78a1636c95`；实测画布 900 × 383。
- RTD 封面保持：`wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v2.png`。
- RTD 封面 SHA-256：`adb5305058faa5264420fd1a0d8bb784352eb919cb43c7d8f7de3169b272cea4`，与基准一致。
- 封面 brief：`wechat/articles/review/ref-tang2025-JBE.cover-brief.md`；SHA-256：`ab1d2646366aa39d8bf5d3982f421180e71e68bf567f7e1ce7e1350430bf2ee7`。
- 该篇目录原有 27 个公开资产全部保持原字节，只新增上述 1 张公众号封面。
- 旧封面和未选历史素材保留，不删除、不改写，也不把新增公众号封面用于 RTD。

## 科学内容等价性证据

- 来源登记 SHA-256：`0116c593fe133ca421595e31aa09e3cd70f2532f4921e9a1e0313ba197cc6643`，与基准对象相同。
- RTD 源文件 SHA-256：`0f17b93ef31f2febf7d08a16eda6a495c982333c4294192c1a501440e0c1f957`，与基准完全一致。
- 主 review 基准 SHA-256：`d4e16d428ac2fb32a16d4846f97f9d72d54b05bfa8e9e72ce79433373d92ec6b`。
- 仅切换公众号封面路径后的主 review SHA-256：`b480044bc1d36fce7f0e611c3c9d2d3adad0eec422af45c6f026fdabebb4e561`。
- 移除 wechat_cover_image 单行后，两版主 review 文本完全相同。
- 当前公众号 Markdown SHA-256：`1d1e2c5bd18308d6f0dfbcffb7b642c8a733a295d38e6c4c382a3434875a31bb`；5 项正文原图路径不变。
- 定向分类与 AI 声明记录 SHA-256：`ef7942ddd0291a3845d05fc5de28603d0660d5dfd774f41b28397b36ec432dda`。

## 审核范围与状态

17 张最终封面及 brief 已冻结，封面独立本地视觉与概念表达边界检查通过。
新工程图只作概念示意，不作为论文测量云图或几何的精确复刻；本记录不以封面
视觉通过替代正文原图证据或微信手机预览。

本轮路由与科学内容等价性的独立复核已通过。原 RTD verified 记录和公众号
历史投递证据完整保留；本轮据此一次性建立新指纹，不宣称新的全文 PDF 审计。
公众号仍停在 awaiting_review；实际后台成功结果由逐篇官方回读回执单独证明，
本记录不把排队或本地预检视作上传完成。浅色、深色手机预览均未由本轮执行。
