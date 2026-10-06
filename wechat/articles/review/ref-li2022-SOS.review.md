---
publication_ref: ref-li2022-SOS
doi: 10.1080/17445302.2021.1937801
wechat_status: awaiting_review
wechat_author: Li Chao
source_checked: true
facts_checked: true
abstract_checked: true
body_images_upload_approved: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
wechat_backend_preview_checked: false
rtd_page_checked: false
wechat_cover_image: wechat/assets/public-safe/ref-li2022-SOS/cover-wechat-900x383-imagegen-v1.png
rtd_cover_image: wechat/assets/public-safe/ref-li2022-SOS/cover-wechat-900x383-imagegen-v1.png
---

# ref-li2022-SOS 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-li2022-SOS.md`
- RTD正文: `docs/source/paper-notes/ref-li2022-SOS.rst`
- 封面素材: `wechat/assets/public-safe/ref-li2022-SOS/cover-wechat-900x383-imagegen-v1.png`
- 论文图 1 半潜式浮式风机的构型: `wechat/assets/public-safe/ref-li2022-SOS/fig-01-configuration.png`
- 论文图 10 FAST 仿真器框架: `wechat/assets/public-safe/ref-li2022-SOS/fig-10-fast-framework.png`
- 论文图 12 LCP3 与 HSP3 模型的响应幅值算子对比: `wechat/assets/public-safe/ref-li2022-SOS/fig-12-rao-comparisons.png`
- 论文图 26 组合随机风浪条件下风机结构动力学统计数据: `wechat/assets/public-safe/ref-li2022-SOS/fig-26-structural-dynamics-statistics.png`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1080/17445302.2021.1937801
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 22；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `a93b07709c4acebdd38215a10076c71a45fb323cad7c6c13dcc017d7ce617700`
- 当前核验副本与历史原始副本的字节等价性未建立；不混同两者哈希

## 关键事实证据定位记录

本节是本轮核对后的当前证据，页码均为PDF物理文件页序。


- 身份与摘要：PDF file page 1出版封面、PDF file page 2摘要；题名、八位作者与DOI对应。摘要保留作者概括，正文按具体工况细化其塔底/机舱响应判断。
- 原型：PDF file page 3–4 §2、Fig.1/Table1，5 MW、LCP3混凝土/HSP3高强钢Y形平台，同几何/吃水/系泊。HSP3本体更轻但需更多压载，总质量相同、重心更低、横摇纵摇惯量更小。
- 实验边界：PDF file page 4 §3.2、PDF file page 5系泊和测量；1:60 Froude比尺，两状态均由不锈钢模型和铁块匹配原型质量分布，不是直接缩尺混凝土材料试验；阻力盘匹配平均推力，水平弹簧替代悬链线，只测平台运动。
- 数值：PDF file page 6–9 §4，与实验对应的FAST使用等效非旋转气动及弹簧回复；塔底/机舱响应由数值计算；完整运行转子、Kaimal湍流风和随机波为PDF file page 20–21 §5.6另设工况。
- 周期：PDF file page 10 Table6，横摇26.7−25.2=1.5 s，纵摇26.5−24.7=1.8 s；PDF file page 9 §5.1及21 §6的约1.6 s为合并概述，现稿分方向报告。
- 均值：PDF file page 11 Fig.13、PDF file page 12 §5.3及21 §6，额定稳态风单独作用时HSP3平均纵摇约低0.5°，不代表全部风浪工况。
- RAO：PDF file page 11 Fig.12及9–12 §5.2，上排平台运动有实测对照，下排塔底载荷/机舱加速度只有数值。HSP3低频纵摇较小，不保证波频载荷同步减小。
- 完整运行：PDF file page 20 Fig.26及20–21 §5.6，额定工况机舱加速度接近，最大运行工况HSP3最大加速度更高；不能泛化成全部差异不显著。摘要与结论强调存在差别，现稿按统计量区分。
- 周期简式：PDF file page 9 §5.1未编号$T=2\pi(I/(D h_T))^{0.5}$，不是Eq.(1)。D仅称displacement，式旁单位未明，保留原式并说明量纲和完整耦合边界，不擅改重力/附加惯性项。
- 四图：Fig.1/10/12/26分别在PDF file page 4/10/11/20；Fig.10原图归属Jonkman(2007)。图1原资产缺矢量标注、图12缺图例、图26缺子图字母，均从原PDF重新提取并检查。
- 正文结论在PDF file page 21，不能定位到印刷页号或PDF file page 20；研究不构成所有材料/海况的选型通则。

## 当前事实修正与完整度

### 2026-10-05 原文审校与完整度结论

- 原文共22页，已完整读审；本轮重新校验存续PDF并检查相关源图、公式、表格，重新建立既有两渠道改稿，不声称找回此前未保留的输出字节
- 当前事实与修改依据见上方已更新的现行证据段；RTD和公众号分别与原文对照，没有相互转换覆盖
- 原文覆盖清单：正文至PDF file page 21；Fig.1–26；Table1–8；4条编号公式；42条参考文献在PDF file page 21–22，无附录
- 现有RTD为选读简介：四幅选图与一条未编号周期解释式；尚未逐段保留全文、全部图表公式、文内引用和参考文献链，顶部也缺全文精解要求的精简版链接行
- 因此全文完整度未完成；原文全页已读、选图已核对不等于RTD全文精解完成
- 原文数值模拟未重新运行；未进行后台上传、更新或发布；新的离线检查结果以本轮执行记录为准

### 本轮离线验证

- 公共安全扫描、产物检查、原生图片/图题/链接目标检查及差异空白检查通过
- 本篇官方工具无提交dry-run通过，使用MathJax SVG；未执行凭据读取、上传或后台更新
- Sphinx标准总构建由整批统一执行；本子批次未重复启动共享构建，微信后台手机预览未执行
