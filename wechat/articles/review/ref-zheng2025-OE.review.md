---
publication_ref: ref-zheng2025-OE
doi: 10.1016/j.oceaneng.2025.121336
wechat_status: awaiting_review
wechat_author: Zheng Shunyun
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
wechat_cover_image: wechat/assets/public-safe/ref-zheng2025-OE/cover-wechat-900x383-imagegen-v1.png
rtd_cover_image: wechat/assets/public-safe/ref-zheng2025-OE/cover-wechat-900x383-imagegen-v1.png
---

# ref-zheng2025-OE 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-zheng2025-OE.md`
- RTD正文: `docs/source/paper-notes/ref-zheng2025-OE.rst`
- 封面素材: `wechat/assets/public-safe/ref-zheng2025-OE/cover-wechat-900x383-imagegen-v1.png`
- 论文图 1(a) 三角形半潜式 10 MW 风机系统三维模型: `wechat/assets/public-safe/ref-zheng2025-OE/fig-01-delta-shaped-system.jpg`
- 论文图 7 三角形半潜式风机系统 RAO: `wechat/assets/public-safe/ref-zheng2025-OE/fig-07-raos-validation.jpg`
- 论文图 12 基于 LTSCR 和 LTCLR 的 ESWL 方法流程: `wechat/assets/public-safe/ref-zheng2025-OE/fig-12-eswl-workflow.jpg`
- 论文图 13a 半潜式 10 MW 风机平台的波浪诱导 LTSCR: `wechat/assets/public-safe/ref-zheng2025-OE/fig-13a-ltscr-distribution.jpg`
- 论文图 19 基于标准、LTSCR 和 LTCLR 工况的最大 Von Mises 应力对比: `wechat/assets/public-safe/ref-zheng2025-OE/fig-19-von-mises-comparison.jpg`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.oceaneng.2025.121336
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 20；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `597a79ff7b94eec72871358e5562a1aed9187085af80793c88338eb2bb7644dd`

## 关键事实证据定位记录

本节是本轮核对后的当前证据，页码均为PDF物理文件页序。


- 摘要与身份：PDF file page 1；中文摘要对应三类路线及精度/成本取舍，50年按§3.1明确为重现期。
- 对象：PDF file page 3 §2.2、Fig.1、Table2，三立柱三角形、DTU10 MW、四系泊线、S355钢材。当前首图只含Fig.1(a)，已明确子图；分类为混凝土方向不等于混凝土材料验证。
- 方法及验证：PDF file page 4–5 §2.3，AQWA/OpenF2A/APDL；1:70试验核对动力响应，Fig.7在PDF file page 7，不代表全部局部应力均经试验测量。
- 数据期：PDF file page 5 §2.4，1992–2016海况样本；PDF file page 8 Eq.(4)–(6)外推50年重现期，不是50年应力实测。
- 概率纠错：PDF file page 8 Eq.(5)为$F_R^{\mathrm{LT}}(R_Q)=Q$且Q=1−1/N，所以Q是不超越概率、1−Q才是超越概率；原文文字误称exceedance，当前按公式定义区分。
- 波幅公式：PDF file page 10 Fig.12直接写$A=R_Q/RAO_{\mathrm{max}}$；PDF file page 11 §3.2对应说明。不是编辑凭空新造或原文编号公式，且A表示波幅。
- 标准法：PDF file page 12 §4.2，图14在PDF file page 14；高应力区−99.93%至28.58%、最大分量−71.05%至6.75%的误差与正文一致。
- LTCLR：PDF file page 9–11 §3.2及13–15 §4.3，18截面×6内力+3整体加速度=111目标，筛至12工况；最大等效误差27.80%–36.91%、平均17.88%–22.71%。
- LTSCR：PDF file page 15–16 §4.4、Table11–13，筛至6工况；保守率低于23.86%、平均5.06%–8.06%；少数单元可低估，准则为相对误差≥−2%或绝对误差<5.5 MPa，已补边界。
- 平衡常量：PDF file page 13 §4.3，表中波浪诱导系泊力和塔底载荷不含初始平衡常量，最终线性结构设计需叠加，已补两渠道。
- 强度：PDF file page 17 §4.6 Eq.(7)–(8)、PDF file page 18 Fig.18–19，355/(1.3×1.0)=273.08 MPa；标准/LTCLR/LTSCR最大值187.20/252.14/228.97 MPa。仅为该文波浪工况屈服评估。
- 源文倒置：PDF file page 11初始工况段将87705×6与111的LTCLR/LTSCR标签写反，同页后续及§4.3–4.4明确111属于特征荷载，现稿不继承倒置。87705与PDF file page 4的87729节点/109284单元不同，不猜原因。
- 图像：Fig.1(a)/7/12/13a/19分别位于PDF file page 3/7/10/12/18；Fig.13a是三正应力，剪应力另在13b，图说已限定。
- 最终边界：PDF file page 19 §5，极端风浪相关性及等效静力风荷载尚未充分纳入，不能视为完整联合荷载验收。

## 当前事实修正与完整度

### 2026-10-05 原文审校与完整度结论

- 原文共20页，已完整读审；本轮重新校验存续PDF并检查相关源图、公式、表格，重新建立既有两渠道改稿，不声称找回此前未保留的输出字节
- 当前事实与修改依据见上方已更新的现行证据段；RTD和公众号分别与原文对照，没有相互转换覆盖
- 原文覆盖清单：§1–5；Fig.1–19（13分13a/13b）；Table1–13；Eq.(1)–(8)；参考文献PDF file page 19–20，无附录
- 现有RTD为选读简介：五个选图位置（含Fig.1(a)）与流程图中的一条波幅公式；尚未逐段保留全文、全部图表公式、文内引用和参考文献链，顶部也缺全文精解要求的精简版链接行
- 因此全文完整度未完成；原文全页已读、选图已核对不等于RTD全文精解完成
- 原文数值模拟未重新运行；未进行后台上传、更新或发布；新的离线检查结果以本轮执行记录为准

### 本轮离线验证

- 公共安全扫描、产物检查、原生图片/图题/链接目标检查及差异空白检查通过
- 本篇官方工具无提交dry-run通过，使用MathJax SVG；未执行凭据读取、上传或后台更新
- Sphinx标准总构建由整批统一执行；本子批次未重复启动共享构建，微信后台手机预览未执行
