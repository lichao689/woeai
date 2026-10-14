# ref-chen2024-JCP 公众号专用封面整合与非内容等价性复核

## 源文件获取记录

沿用 [ref-chen2024-JCP.review.md](ref-chen2024-JCP.review.md) 中已核验的获授权论文来源。
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
[ref-chen2024-JCP.taxonomy.review.md](ref-chen2024-JCP.taxonomy.review.md)。排除这些已授权编辑差异后，
公众号科学正文、摘要、公式、原图和作者名单与基准逐字节一致。

## 最终路由与冻结输入

- 公众号封面：`wechat/assets/public-safe/ref-chen2024-JCP/cover-wechat-900x383-20261014-badge.png`。
- 新封面 SHA-256：`38454c83607a00b333d375424a14d3f7103f7371c4fbee088e2c28c03144bf1f`；实测画布 900 × 383。
- RTD 封面保持：`wechat/assets/public-safe/ref-chen2024-JCP/cover-wechat-900x383-imagegen-v2.png`。
- RTD 封面 SHA-256：`eddb9ab8a43ecb5439c8968dd28f62d89a1074bd4d81db91019919fabe1793d0`，与基准一致。
- 封面 brief：`wechat/articles/review/ref-chen2024-JCP.cover-brief.md`；SHA-256：`a687e8a553c6a10a83c4bd6d3fbc9437915f3936d9155ba11caa4b2aa91c6246`。
- 该篇目录原有 42 个公开资产全部保持原字节，只新增上述 1 张公众号封面。
- 旧封面和未选历史素材保留，不删除、不改写，也不把新增公众号封面用于 RTD。

## 科学内容等价性证据

- 来源登记 SHA-256：`d179ba92b5e929b2c80db2ede1617a354c05740a11aa999a7fd74d7aa41d1339`，与基准对象相同。
- RTD 源文件 SHA-256：`c4b53e0c540c5246aa79c3f5f29ea81fa82bfb9db41ff8c893dbe2f2c35819bc`，与基准完全一致。
- 主 review 基准 SHA-256：`2d56bf3b71e26f992399d6f1b7a1195b12ad0da9a3087f6592a24e5f8a1b8f85`。
- 仅切换公众号封面路径后的主 review SHA-256：`547137d61133f536cc758e3dcac0cb5e99ee3a1f5da3f28fc640ecef11696943`。
- 移除 wechat_cover_image 单行后，两版主 review 文本完全相同。
- 当前公众号 Markdown SHA-256：`cd88085b83c56be10a00fc701e443e329ec7079e0e691f97d0b405c56082c98b`；5 项正文原图路径不变。
- 定向分类与 AI 声明记录 SHA-256：`0df5b3cab9ea245068307acac3b9af9539b14e011b41699ec56bcc4bf74e8ae8`。

## 审核范围与状态

17 张最终封面及 brief 已冻结，封面独立本地视觉与概念表达边界检查通过。
新工程图只作概念示意，不作为论文测量云图或几何的精确复刻；本记录不以封面
视觉通过替代正文原图证据或微信手机预览。

本轮路由与科学内容等价性的独立复核已通过。原 RTD verified 记录和公众号
历史投递证据完整保留；本轮据此一次性建立新指纹，不宣称新的全文 PDF 审计。
公众号仍停在 awaiting_review；实际后台成功结果由逐篇官方回读回执单独证明，
本记录不把排队或本地预检视作上传完成。浅色、深色手机预览均未由本轮执行。
