---
publication_ref: ref-tang2026-RE
doi: 10.1016/j.renene.2025.124336
wechat_status: awaiting_review
wechat_author: Tang Lingxiao
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
wechat_cover_image: wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot.png
rtd_cover_image: wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot.png
---

# ref-tang2026-RE 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-tang2026-RE.md`
- RTD正文: `docs/source/paper-notes/ref-tang2026-RE.rst`
- 封面素材: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot.png`
- 论文图 6 风场快照的时间超分辨率流程: `wechat/assets/public-safe/ref-tang2026-RE/fig-06-temporal-super-resolution.jpg`
- 论文图 1 基于步长的稀疏操作示意图: `wechat/assets/public-safe/ref-tang2026-RE/fig-01-stride-sparse-operation.jpg`
- 论文图 4 所提出 WTT-SRST 的详细结构与各模块架构: `wechat/assets/public-safe/ref-tang2026-RE/fig-04-wtt-srst-framework.jpg`
- 论文图 14 脉动速度的功率谱密度结果: `wechat/assets/public-safe/ref-tang2026-RE/fig-14-power-spectra.jpg`
- 论文图 24 凌晨 3:45 生成风场的可视化表示: `wechat/assets/public-safe/ref-tang2026-RE/fig-24-generated-wind-field.jpg`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 本轮逐段全文与图表公式已补齐，等待独立复核；不据此标记 verified
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.renene.2025.124336
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 24；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `74fafba653edad10e497c9cc029394655ea3dd5c2b3bb9157ee016739e8f4780`

## 关键事实证据定位记录

- PDF file page 1：题名、五名作者、Li Chao和Zhao Zihan通讯标记、Renewable Energy256(2026)124336及DOI一致；在线2025-09-04与卷年2026不混同。摘要按原文翻译，物理保证措辞另由方法与边界作限制。
- PDF file pages 3-7, Figs.1/4/6, Eq.(12)：两个已知快照间插值，不是未知未来时刻预报；数据是二维平面上的三分量速度，非完整三维城市重建。
- PDF file page 5 Eq.(5)：SPW-MSA复杂度4hwc²+4(L²/s²)hwc已对原页；仅第二项按1/s²缩减，不能推成整个模型平方加速。
- PDF file pages 5-7 Eqs.(6)-(10)：未解析垂向项并入残差，比较预测与参考残差差值，不是强制完整三维残差为零。式8/9/10、符号定义与Tables2-5的Lc/Ls/Lm互有冲突，现稿不代定唯一实现。
- PDF file pages 8-9：缩尺空场LES，0.2m高度的0.64×0.64m平面；训练低分辨率输入来自下采样，测试先时间平均滤高频；最后1s独立测试。Table2训练区间0.5–6s与正文首6s的说法不完全一致，未补造索引。
- PDF file pages 8-9/Fig8/Table5：全尺度取JHTDB-Wind风场上游、轮毂高度64×64平面；02:00–04:00两小时数据，参考0.5s，输入1.5/3/4.5s，训练/验证/测试90%/5%/5%。不等于复杂城区实测、尾流全场、功率或调度验证。
- PDF file pages 10-14：训练对照含线性插值，测试Fig16主要比较WTSR-ST和WTT-SRST。相对误差较低不等于绝对误差始终小；page13较大插值间隔MAPE超过100%。Eq.(15)分母为重建量，不能与另一定义的MAPE直接比较。
- PDF file pages 13-19：谱/相干支持低频与部分高频重建，但更大stride、快照间隔、噪声使结果退化。训练Fig14位于p14，测试谱Fig19位于p18，不混同。
- PDF file pages 15/20, Tables8-9：单模块359.92/250.35 MB相对1225.26 MB约29.37%/20.43%。整体s=2参数2.993M相对3.718M约降19.50%，显存1034.24相对3472.55 MB约降70%；是显存不是总GPU资源。s=2 FLOPs23.78G高于原架构21.58G，现稿保留不利项。
- PDF file page 17, §4.5；page20 Fig22：双残差约束三组MSE为基线0.86/0.88/0.74，原导读泛称所有统计指标下降至74%–88%已纠正。
- PDF file page 22 Table10：三组平均误差较WTSR-ST低，但J1-CM MAPE标准差8.13→10.28，J3-CM平均MAPE111.87%；不能说每项稳定性都改善。
- PDF file pages 17-18/22 Table11：1282→860min训练时间及17700→11880Wh估计支持原报告约32.9%相对量级；只按额定功率/使用率估计运行期，未计待机、数据生成、完整风能系统，不是电表实测绝对节能。
- 五张选图：Fig1 p3、Fig4 p4、Fig6 p6、Fig14 p14、Fig24 p21；原式12物理页为p7而不是p6，已校正定位。Fig24色标m/s、三分量行和时间间隔列完整。

## 当前事实修正与完整度

### 2026-10-05 重建后的源文复核结论

原文另有未决项：page15 s=4模块参数0.095M/时间0.32ms与page20 Table8的0.085M/0.42ms不同；page7 Table1最小频率50Hz与page8正文0.5Hz不同；page18碳强度702gCO2e/kWh与page22的17.7kWh/9510gCO2e不满足相乘关系，测试秒数/Wh/功率口径也需澄清；Table9/11基线引用[47]/[38]不同；式16百分数TI与式17使用I的换算不明。保留这些复现限制，不擅自补造正确值。

### 事实与完整度分别判断

- 本轮对上述两渠道现有内容分别校正，未用公众号转换覆盖独立RTD。错误和歧义已纠正或明确归属，不宣称独立复现论文计算结果。
- 2026-10-05 历史快照：当时 RTD 为 legacy_intro，只有选图 1、4、6、14、24 与式（5），缺全文及公众号链接行。该状态已由下述 2026-10-06 全文补齐记录取代；无附录。
- 微信当前内容已按来源审校；没有新上传、后台手机公式/插图/封面预览或发布。历史工作记录不得继承为新版本验收。
- 本轮重新生成内容及审查记录，未声称已恢复先前丢失提交的完全相同字节。最终检查与新内容指纹由整批集成重新计算。


## 2026-10-06 独立 RTD 全文补齐与图框校准

### 本轮范围与状态

- 从授权出版版 PDF 独立重写 RTD，不由公众号短稿转换；公众号正文、封面、注册表与生成视图均未改动。
- 本轮工作稿包含完整论文信息、五名作者与 a–d 单位映射、两条通讯脚注与原文公开邮箱、收稿/修回/录用/上线信息、完整摘要与关键词、逐段引言及方法/训练/结果/结论、科学符号表与完整参考文献。
- 24 幅原图、11 张可编辑中文编号表、18 个原编号公式全部保留；另包含表 1 的三个 Von Kármán 谱、训练 argmin、数据维度与参数关系等重要未编号数学表达式。
- Nomenclature 依照原文位于结论之后、参考文献之前；保留全部缩写和科学符号定义，不含声明/致谢。原文没有附录。CRediT、利益冲突、致谢和数据可用性均未进入 RTD 正文。
- 页面顶部的精简公众号链接行后紧接既有 v5-b 封面，底部完整引用链接保持原有出版物锚点。
- 这是作者工作级自检结果；仍须独立审稿，不设置 RTD verified，不声称完成微信后台预览或发布。

### 源文件与素材处理

- 沿用已核对的授权期刊出版版 PDF；当前可用清单未提供更高优先级作者稿。本轮没有访问 Zotero 写权限、重新联网下载 PDF 或读取凭据。
- 当前副本与历史源 SHA-256 均为 `74fafba653edad10e497c9cc029394655ea3dd5c2b3bb9157ee016739e8f4780`，24 页；源 PDF、逐页文本、整页截图与裁图校验证据保留在仓库外的授权私有工作区。
- Fig. 1–24 均为单独嵌入 PDF 的原生 JPEG 位图，完整像素经无损 PNG 编码保存为 `fig01.png` 至 `fig24.png`，不重绘、不超分辨率补画、不猜测裁框。
- 逐幅查看最终图片，再与对应整张 PDF 页视觉核对；图轴、刻度、图例、子面板字母、全部色标、边界条件与重要图中文字均按原图范围保留，图片不夹入相邻正文或图题。PDF 文本层检查未发现与这些原图重叠的独立文字标注，整页检查亦未发现需额外合成的矢量标注。
- 原先五张选图别名重新核对后与原生 JPEG 字节相同，因此无需人为改变已准确的范围；它们与新增全图保持一致。所有封面文件字节未修改。
- 原生图片本身存在少量紧贴边缘的刻度（如 Fig.13 最右侧刻度），本轮不引入二次裁切，也不补画源文件没有的内容。

### 图号与文件页定位

- PDF file page 3：Fig.1–2
- PDF file page 4：Fig.3–4
- PDF file page 6：Fig.5–6
- PDF file page 7：Fig.7
- PDF file page 8：Fig.8
- PDF file page 10：Fig.9
- PDF file page 11：Fig.10–11
- PDF file page 12：Fig.12
- PDF file page 13：Fig.13
- PDF file page 14：Fig.14
- PDF file page 15：Fig.15
- PDF file page 16：Fig.16–17
- PDF file page 17：Fig.18
- PDF file page 18：Fig.19
- PDF file page 19：Fig.20
- PDF file page 20：Fig.21–22
- PDF file page 21：Fig.23–24

### 完整表格、公式与引用定位

- PDF file page 7：Table 1；page 8：Table 2；page 9：Tables 3–5；page 11：Table 6；page 17：Table 7；page 20：Tables 8–9；page 22：Tables 10–11。合并单元格含义已在中文表中展开，各组所有数值、符号、单位和表注保留。
- PDF file page 4：Eq.(1)；page 5：Eqs.(2)–(6)；page 6：Eqs.(7)–(9)；page 7：Eqs.(10)、(12)；page 8：Eq.(11)；page 10：Eqs.(13)–(18)。式（12）先于式（11）的原始顺序保留。
- PDF file pages 22–23：完整 Nomenclature；pages 23–24：References [1]–[50] 全部保留。文内引注通过可点击的原编号链接到完整文献，断行 DOI 已拼回可读 URL。

### 新增源文差异与解释边界

- PDF file page 3：章节组织段与 2.1 引导段的节号/顺序不符；原文编号说明保留，不冒充其原始节号。
- PDF file page 5：Swin-Transformer 的 [12] 引用与参考文献内容不一致；K1 维数重复 Dk，Eq.(4) 第二项写 c²，均保留并说明；Eq.(5) 仅第二项按 1/s² 缩减。
- PDF file pages 5–7：动力黏度名称与式子量纲、Eq.(7) 第三残差的垂向二阶项缺黏度系数、Eqs.(8)–(10) 与文字/表格的损失下标冲突、e′ 定义与符号表顺序冲突，均就近说明。
- PDF file pages 7–9：Table 1 的最小频率 50 Hz 与正文 0.5 Hz；Fig.8 的直径 125 m 与正文 126 m；Table 2 的训练时段 0.5–6.0 s 与“前 6 s”，均不代改。
- PDF file pages 10–12：Eq.(15) 以重建量为分母；TI 百分数与 TKE 公式比例值口径未交代；训练正文部分百分比不能由列示数值直接算得；Fig.12 的 MSE 图题与 m/s 轴单位不一致，正文孤立“(c) W 分量”与原图 U 标签不同。
- PDF file pages 14–15、20：噪声 S2-CM 的 0.379 RMSE / 0.476 MAE 与同样本同权重的通常关系不符；s=4 模块参数/平均时间正文与表格不同；整体 s=4 参数减少量正文与表格不同；s=2 显存并非严格低于普通窗口架构的三分之一，且 FLOPs 高于原始架构。
- PDF file page 19：Fig.20 的九个面板在原图均写 F1-CM，不能按排列擅改为 F2-CM、F3-CM。
- PDF file pages 20–21：Fig.22 纵轴写 Relative to Ls，横轴以 Lc 为基准，并与正文残差命名不一致；相对 MSE 为无量纲但原图题写 m²/s²。Fig.23 保留各面板 W/V/U 行序和不同色标。正文称 Fig.24 示出正方向，但图内没有独立坐标方向标识。
- PDF file pages 17–22：74%–88% 为 MSE 的基线剩余比例；全尺度 MAPE 可超过 100%，并非所有标准差都改善；70% 指整体显存降幅。碳强度与能量/排放、测试时间口径，以及 s=2 节能对应乘用车公里数仍不一致，均明确标注为源文问题。

### 本轮检查结果

- `scripts/check-public-safe-content.py`：通过；科学符号表已按原文审核。
- `git diff --check`：本任务范围通过。
- `tools/publications/artifacts.py --check`：通过，无结构问题；该工具结果不替代全文独立审核。
- 新鲜全站 Sphinx `-W --keep-going -E` 诊断构建：通过；仅临时移除 sitemap 扩展，不宣称标准门禁通过。
- 实际生成 HTML 检查：25 张图片（含封面）路径均存在；正文无裸露 math/ref/sup 角色或未解析数字引注；50 项文献目标与所有 73 处引注链接有效。
- 实际 HTML 的 20 个块公式与 179 个行内公式已交给仓库 MathJax SVG 渲染器，全部成功，无 merror；这是离线数学语法检查，不是微信后台手机预览。
- 标准 `./scripts/check-docs.sh` 已执行；本次停止于整批注册表的未更新核验指纹和生成视图暂不同步，未达到后续标准 Sphinx 阶段。由集成流程在独立审核后重跑。


## 2026-10-06 独立全文复核通过

- 24 页全文、24 幅源图、11 张编号表及完整符号/缩写表、18 个原编号公式、50 条参考文献已完成独立逐页复核；作者单位、通讯脚注、全部引用和适用边界均保留。
- 每幅最终科学图分别与完整 PDF 原页核对，并独立重现源像素；已有选图别名经过复核，封面未改。
- 原文内部差异就近明确标注，不通过改数据、换图例或泛化结论掩盖差异。
- 最终诊断 Sphinx、实际 HTML 图像/引用/角色检查及 MathJax 渲染通过；标准门禁和部署由发布批次验证。
- 本结论取代上文的待独立审校状态，公众号后台预览及发布状态不变。

- 符号表位于原文结论后、参考文献前，逐项确认仅含科学定义；按原位置保留。项目指南与布局检查新增精确符号表标题例外，声明/致谢仍禁止，变更另经独立审查。
- 独立复核修正规范化后的式（4）（5）运算量标签中的多余感叹号，并去除图 9 替代文本中的引用标记残留；公式其余项和正文引用未变。
