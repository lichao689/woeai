---
publication_ref: ref-yang2025-JBE
doi: 10.1016/j.jobe.2025.113635
wechat_status: awaiting_review
wechat_author: Yang Junhui
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
wechat_cover_image: wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5b-pub-line-route.png
rtd_cover_image: wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5b-pub-line-route.png
---

# ref-yang2025-JBE 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-yang2025-JBE.md`
- RTD正文: `docs/source/paper-notes/ref-yang2025-JBE.rst`
- 封面素材: `wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5b-pub-line-route.png`
- 论文图 1 建筑主轴和风向: `wechat/assets/public-safe/ref-yang2025-JBE/fig-01-building-principal-axes-wind-direction.jpg`
- 论文图 3 二维矢量响应极值合成结果和误差: `wechat/assets/public-safe/ref-yang2025-JBE/fig-03-method-error-random-signals.jpg`
- 论文图 5 不同标准差比和相关系数下的二维矢量响应极值误差: `wechat/assets/public-safe/ref-yang2025-JBE/fig-05-error-correlation-map.jpg`
- 论文图 17 建筑框架有限元模型: `wechat/assets/public-safe/ref-yang2025-JBE/fig-17-width-depth-fe-models.jpg`
- 论文图 18 不同宽深比建筑顶层角点的主轴响应和合成响应极值: `wechat/assets/public-safe/ref-yang2025-JBE/fig-18-width-depth-wind-direction-response.jpg`
- 论文图 20 中心点主轴响应与角点合成响应之比: `wechat/assets/public-safe/ref-yang2025-JBE/fig-20-center-corner-response-ratio.jpg`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.jobe.2025.113635
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 24；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `9c68cfe79bddd2b50839d9251df3e18579a0f20edbe6ad8738a1ed252e27f26c`

## 关键事实证据定位记录

本节是本轮核对后的当前证据，页码均为PDF物理文件页序。


- 摘要：PDF file page 1，现有中文摘要保留作者表述；其高阶模态概括较笼统，而PDF file page 15 §3.2.3和PDF file page 22–23 §4(2)区分位移/加速度，已加译注避免读成加速度也可忽略高阶。
- 实际使用公式：PDF file page 7，Eq.(24)，$A(t)=\sqrt{X^2(t)+Y^2(t)}$正确；PDF file page 5 §2.1.3和7–9 §2.2说明主要处理零均值脉动响应，平均风响应另作静力处理。
- 随机算例：PDF file page 10，§3.1、Fig.3，固定ρ=0.2且σX/σY=1的误差为SRSS +25.76%、ERF−7.18%、CDC+0.61%、RPA−2.54%、CPF+4.40%。与参数扫描最大偏差区分。
- 热图纠错：PDF file page 12，Fig.5，横轴σX/σY、纵轴ρXY，色块/数字为相对误差。旧说明颠倒轴向并误称误差曲线不随相关性变化，现均已改正。不显式依赖ρ的是SRSS/ERF/CPF预测公式，不是相对真实值的误差。
- 数值差异保留：PDF file page 10正文报SRSS最大约42%，PDF file page 12 Fig.5显示最高格值0.41；保留作者近似量级并披露差别，不称精确复算上界。其他最大约25%/16%/7%/4%对应ERF/CPF/RPA/CDC。
- 模态：PDF file page 14–16，§3.2.3、Fig.12–13，以0°风向及前20阶为参照；前3阶位移99.8%、前6/11阶加速度96.7%/99.0%。两渠道补参照条件，11阶不是通用阶数。
- 19%范围：PDF file page 19，§3.3.1；PDF file page 21，Fig.20，19%（2:1）/28%（3:1）是中心点主轴加速度相对角点二维加速度的低估，非所有位移指标；开头、数字卡和发现均明确加速度。
- 3%范围：PDF file page 21，Table4，B31全风向最大值的角点二维/角点主轴差别为位移2.20%、加速度1.58%；B31T加速度为5.19%，不能无条件推广。PDF file page 19逐风向最大位移低估另报3.1%，口径不同。
- 扭转边界：PDF file page 21，§3.3.2、Table4，B21T位移下降而加速度上升，不能称所有响应单调增大。
- 源文标签问题：PDF file page 19把第一组加速度比例0.86–0.95和后组0.48–0.72均标3:1；Fig.20用B11/B21/B31区分。现稿不继承此重复标签。
- 六幅图：Fig.1/3/5/17/18/20分别在PDF file page 6/10/12/18/20/21；图18旧裁剪缺底部坐标和第三子图说明，已重新从原PDF忠实提取并查看。

## 当前事实修正与完整度

### 2026-10-05 原文审校与完整度结论

- 原文共24页，已完整读审；本轮重新校验存续PDF并检查相关源图、公式、表格，重新建立既有两渠道改稿，不声称找回此前未保留的输出字节
- 当前事实与修改依据见上方已更新的现行证据段；RTD和公众号分别与原文对照，没有相互转换覆盖
- 原文覆盖清单：§1–4；Fig.1–21；Table1–4；Eq.(1)–(46)；50条参考文献在PDF file page 23–24，无附录
- 现有RTD为选读简介：六幅选图及Eq.(24)的无编号表达；尚未逐段保留全文、全部图表公式、文内引用和参考文献链，顶部也缺全文精解要求的精简版链接行
- 因此全文完整度未完成；原文全页已读、选图已核对不等于RTD全文精解完成
- 原文数值模拟未重新运行；未进行后台上传、更新或发布；新的离线检查结果以本轮执行记录为准

### 本轮离线验证

- 公共安全扫描、产物检查、原生图片/图题/链接目标检查及差异空白检查通过
- 本篇官方工具无提交dry-run通过，使用MathJax SVG；未执行凭据读取、上传或后台更新
- Sphinx标准总构建由整批统一执行；本子批次未重复启动共享构建，微信后台手机预览未执行
