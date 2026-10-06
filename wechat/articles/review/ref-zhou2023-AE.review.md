---
publication_ref: ref-zhou2023-AE
doi: 10.1016/j.apenergy.2023.121941
wechat_status: awaiting_review
wechat_author: Zhou Shengtao
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
wechat_cover_image: wechat/assets/public-safe/ref-zhou2023-AE/cover-wechat-900x383-imagegen-v1.png
rtd_cover_image: wechat/assets/public-safe/ref-zhou2023-AE/cover-wechat-900x383-imagegen-v1.png
---

# ref-zhou2023-AE 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhou2023-AE.md`
- RTD正文: `docs/source/paper-notes/ref-zhou2023-AE.rst`
- 封面素材: `wechat/assets/public-safe/ref-zhou2023-AE/cover-wechat-900x383-imagegen-v1.png`
- 论文图 1 自由度和全局坐标系定义: `wechat/assets/public-safe/ref-zhou2023-AE/fig-01-dof-coordinate.jpg`
- 论文图 7 所研究浮式风机的平台构型与系泊布置: `wechat/assets/public-safe/ref-zhou2023-AE/fig-07-platform-mooring-layout.jpg`
- 论文图 19 不同环境输入得到的 Pareto 前沿对比: `wechat/assets/public-safe/ref-zhou2023-AE/fig-19-pareto-environmental-inputs.jpg`
- 论文图 23 方形与 Y 形下部结构的 Pareto 前沿对比: `wechat/assets/public-safe/ref-zhou2023-AE/fig-23-pareto-substructures.jpg`
- 论文图 25 两类下部结构在 135 度波向下的平台运动 RAO 对比: `wechat/assets/public-safe/ref-zhou2023-AE/fig-25-rao-comparison.jpg`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.apenergy.2023.121941
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 20；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `0339a5a26859683341f52de5ecc0c5fd517ab94e38840866dc5885ccf0420b8f`

## 关键事实证据定位记录

本节是本轮核对后的当前证据，页码均为PDF物理文件页序。


- 摘要与身份：PDF file page 1，题名、六位作者及DOI一致，中文摘要与原文方法和两构型比较对应。
- 方法：PDF file page 3 §2.1、Fig.1，八自由度为平台六刚体自由度+塔架两弯曲模态；Kriging与NSGA-II见PDF file page 7 §3.3–3.4及9 §4.4。
- 气动前置：PDF file page 4 §2.2，以OpenFAST预计算固定塔顶转子载荷和气动阻尼表，并进行控制器调谐；迭代可读表，不代表方法无翼型/控制器前置依赖。
- 数据：PDF file page 5 §3.1–3.2，2007–2018缅因湾观测经Nataf扩展25年；PDF file page 6 §3.2.2用MDA选择1000样本，不是连续25年实测。
- 优化：PDF file page 7–9 §4.1–4.3，10 MW、130 m水深、两类均钢结构；吃水/柱半径/柱距/线长/链径为五独立变量，锚点半径从属。制造成本不是全生命周期成本，损伤<1.5为宽松早期约束。
- SMD/LMD：PDF file page 12–13 §5.4.1及15 Fig.19。SMD结果的疲劳按长期模型重算；高成本塔底前沿接近、低成本LMD改善，导缆孔改善主要在高成本区，不能称全部指标和成本点均改善。
- 两构型：PDF file page 14 §5.4.2、PDF file page 17 Fig.23、PDF file page 19结论，同成本方形塔底疲劳大多低30%–50%；部分Y形系泊疲劳更低，涉及二阶慢漂、较粗链径及成本代价。
- OO-Star归属纠错：PDF file page 15 §5.4.2，约900万欧元成本的改进为Y形设计，DFrld/DTwrBs=0.119/0.136，较参考点低4.8%/32%，不是方形设计。参考比较模型改为钢平台、调整系泊并去除集中配重，见PDF file page 9 §5.1。
- 误差：PDF file page 10–11 §5.1.2，运动响应标准差多数工况约10%，部分高于额定风速达10%–25%，涉及气动阻尼和控制动态；强海况线性黏性阻力还会影响张力。PDF file page 17结论更概括，不能当作所有长期指标误差保证。
- 强度边界：PDF file page 7–9 §4.1–4.3及19 §6末段，未校核船体强度，内部加强钢材和成本可能低估。
- 图像：Fig.1/7/19/23/25分别位于PDF file page 3/8/15/17/18。图19旧裁剪残留英文图题、图23残留页脚，已忠实重新提取、检查图例/坐标完整。
- 公式指标：没有展示编号公式；TC见PDF file page 8 Eq.(17)，三目标见PDF file page 9 Eq.(18)，损伤见PDF file page 7 §3.4。

## 当前事实修正与完整度

### 2026-10-05 原文审校与完整度结论

- 原文共20页，已完整读审；本轮重新校验存续PDF并检查相关源图、公式、表格，重新建立既有两渠道改稿，不声称找回此前未保留的输出字节
- 当前事实与修改依据见上方已更新的现行证据段；RTD和公众号分别与原文对照，没有相互转换覆盖
- 原文覆盖清单：§1–6；Fig.1–27；Table1–5；Eq.(1)–(18)；45条参考文献，无附录
- 现有RTD为选读简介：五幅选图，无完整编号公式/表格/参考文献；尚未逐段保留全文、全部图表公式、文内引用和参考文献链，顶部也缺全文精解要求的精简版链接行
- 因此全文完整度未完成；原文全页已读、选图已核对不等于RTD全文精解完成
- 原文数值模拟未重新运行；未进行后台上传、更新或发布；新的离线检查结果以本轮执行记录为准

### 本轮离线验证

- 公共安全扫描、产物检查、原生图片/图题/链接目标检查及差异空白检查通过
- 本篇官方工具无提交dry-run通过，使用MathJax SVG；未执行凭据读取、上传或后台更新
- Sphinx标准总构建由整批统一执行；本子批次未重复启动共享构建，微信后台手机预览未执行
