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
- RTD全文覆盖: 未完成，缺项详见下文
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
- RTD仍为`legacy_intro`，`full_paper_coverage=false`。原文共24页、24图、11表、18编号公式、50项参考文献；当前仅选图1,4,6,14,24与式(5)，没有逐段完整正文、全部图表/公式及参考文献链；无附录。顶部封面存在，但缺全文页面的精简公众号链接行。
- 微信当前内容已按来源审校；没有新上传、后台手机公式/插图/封面预览或发布。历史工作记录不得继承为新版本验收。
- 本轮重新生成内容及审查记录，未声称已恢复先前丢失提交的完全相同字节。最终检查与新内容指纹由整批集成重新计算。
