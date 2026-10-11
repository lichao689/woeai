# RTD 上线与 JCP 样板交付核验

核验日期：2026-10-11；仓库基线：`44af3cfda7cda845daa81fb68737b3d5ef2931ce`。

## 结论与范围

- 现有 17 篇登记为已核验的独立论文精解，线上全部返回 HTTP 200，论文 DOI 均存在，HTML 内没有重复 id。
- 检查的是已部署页面、公式源片段和图像字节，不等同于重新逐句完成 17 篇原文审校，也不代表浏览器端所有公式已经视觉验收。
- JCP 的附录 A/B 已在线，A13、B18 等末尾公式可定位；页面含 892 个数学片段。
- JCP 的 35 幅正文图及封面共 36 个线上图像，与当前仓库对应文件逐字节一致。
- 当前 JCP 公众号稿通过 preflight、dry-run 和真实 MathJax SVG 离线渲染：29 个数学片段、5 幅嵌入正文图、0 数学渲染错误。
- 上述检查不读取微信凭据、不联系微信、不上传图片、不更新草稿。

## 已部署页面抽查清单

| 论文 | HTTP | DOI | 数学片段 | 页面内容图像（含封面） | 重复 id |
| --- | --- | --- | ---: | ---: | ---: |
| [ref-zhao2026-BE](https://winddee.cn/zh-cn/latest/paper-notes/ref-zhao2026-BE.html) | 200 | 存在 | 83 | 21 | 0 |
| [ref-he2026-OE](https://winddee.cn/zh-cn/latest/paper-notes/ref-he2026-OE.html) | 200 | 存在 | 201 | 22 | 0 |
| [ref-zhao2026-BS](https://winddee.cn/zh-cn/latest/paper-notes/ref-zhao2026-BS.html) | 200 | 存在 | 347 | 27 | 0 |
| [ref-he2026-OE-structural](https://winddee.cn/zh-cn/latest/paper-notes/ref-he2026-OE-structural.html) | 200 | 存在 | 199 | 36 | 0 |
| [ref-tang2026-RE](https://winddee.cn/zh-cn/latest/paper-notes/ref-tang2026-RE.html) | 200 | 存在 | 199 | 25 | 0 |
| [ref-he2025-POF](https://winddee.cn/zh-cn/latest/paper-notes/ref-he2025-POF.html) | 200 | 存在 | 296 | 32 | 0 |
| [ref-yang2025-JBE](https://winddee.cn/zh-cn/latest/paper-notes/ref-yang2025-JBE.html) | 200 | 存在 | 381 | 22 | 0 |
| [ref-zheng2025-OE](https://winddee.cn/zh-cn/latest/paper-notes/ref-zheng2025-OE.html) | 200 | 存在 | 185 | 21 | 0 |
| [ref-tang2025-JBE](https://winddee.cn/zh-cn/latest/paper-notes/ref-tang2025-JBE.html) | 200 | 存在 | 121 | 20 | 0 |
| [ref-zhao2025-SCS](https://winddee.cn/zh-cn/latest/paper-notes/ref-zhao2025-SCS.html) | 200 | 存在 | 131 | 35 | 0 |
| [ref-chen2024-POF](https://winddee.cn/zh-cn/latest/paper-notes/ref-chen2024-POF.html) | 200 | 存在 | 269 | 25 | 0 |
| [ref-wang2024-ES](https://winddee.cn/zh-cn/latest/paper-notes/ref-wang2024-ES.html) | 200 | 存在 | 310 | 22 | 0 |
| [ref-li2024-POF](https://winddee.cn/zh-cn/latest/paper-notes/ref-li2024-POF.html) | 200 | 存在 | 324 | 12 | 0 |
| [ref-chen2024-JCP](https://winddee.cn/zh-cn/latest/paper-notes/ref-chen2024-JCP.html) | 200 | 存在 | 892 | 36 | 0 |
| [ref-zhou2023-AE](https://winddee.cn/zh-cn/latest/paper-notes/ref-zhou2023-AE.html) | 200 | 存在 | 324 | 28 | 0 |
| [ref-chen2022-JWEIA](https://winddee.cn/zh-cn/latest/paper-notes/ref-chen2022-JWEIA.html) | 200 | 存在 | 633 | 25 | 0 |
| [ref-li2022-SOS](https://winddee.cn/zh-cn/latest/paper-notes/ref-li2022-SOS.html) | 200 | 存在 | 103 | 27 | 0 |

## JCP 当前稿复核

- 主文 PDF SHA-256 与既有审校副本一致，本次重新核对所用关键量化事实及图 4、7、17、28、30 的可读像素。
- 保留单波入口压力污染、SW4 动能代价、50/20 次随机筛选、仅 u 分量/Y 向相干直接输入、HA1/HA2 不同位置比较以及边界残余等限制。
- 已有原图和公众号文字本次尚未更改；附录完整性沿用既有独立审校证据，本次线上核验没有伪装为重新审校附录。

## 离线核验时的交付门槛（历史记录，后续结果见下节）

- 新封面：用户已确认文案并选定候选 B，授权等比缩放及微量裁切；正式输出 900×383，已查看全图、宽缩略图与中心方图。网页部署与微信后台实际裁切仍需分别核验。
- 当前公众号稿仍为 awaiting_review；离线成功不改变该状态。
- 更新现有草稿前须验证实际账号绑定与文章索引，并取得明确的凭据使用、图片上传与目标草稿更新确认。不能推断文章索引为 0。
- 官方微信后台/手机实际预览、最终人工发布未执行；历史草稿时间冲突不得用本轮离线时间覆盖。

## 既有 17 篇公众号离线渲染回归

- 17/17 篇使用 academic-clean / MathJax SVG 实际渲染成功，共 678 个数学片段、88 幅正文图片，0 个数学渲染错误。
- 这是渲染回归，不是本轮逐篇重新全文校对，也不代表后台上传或手机预览已完成。

## 2026-10-11 正式草稿交付结果

- 交付候选：`ccd56d9a7278f832b4ad203001196cca588d3ae9`；对应 CI 成功，RTD 新封面已于 13:54 UTC 完成在线字节核对。
- 获得本次账号凭据使用、封面及 5 幅正文图上传、原有草稿更新的明确授权后，执行环境在线核实账号绑定和目标文章索引。
- 同一原有 JCP 草稿于 13:58:11 UTC 更新成功；14:02:24 UTC 官方 API 只读回查通过。
- 回查覆盖标题、v2 封面、5 幅正文图映射、原文链接、正文文字、29 处公式元数据与 SVG 几何。微信会转换 HTML 和 CDN 图像格式，不宣称远端字节与源文件一致。
- 状态为 `draft_created`，操作为 `update`；没有创建重复草稿。手机实际预览未执行，未发布或群发。不得标记为 `ready_to_publish` 或 `published`。
- 私有账号绑定、文章索引、凭据及 API 原始回执不进入公共仓库；历史时间冲突原样保留。
