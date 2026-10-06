---
publication_ref: ref-tang2025-JBE
doi: 10.1016/j.jobe.2025.112131
wechat_status: awaiting_review
wechat_author: Tang Ao
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
wechat_cover_image: wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v2.png
rtd_cover_image: wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v2.png
---

# ref-tang2025-JBE 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-tang2025-JBE.md`
- RTD正文: `docs/source/paper-notes/ref-tang2025-JBE.rst`
- 封面素材: `wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v2.png`
- 论文图 1 建筑结构模型的结构图表示（不同颜色表示不同标准层）: `wechat/assets/public-safe/ref-tang2025-JBE/fig-01-structural-graph.jpg`
- 论文图 4 数据生成: `wechat/assets/public-safe/ref-tang2025-JBE/fig-04-data-generation.jpg`
- 论文图 6 TBGNN 架构: `wechat/assets/public-safe/ref-tang2025-JBE/fig-06-tbgnn-architecture.jpg`
- 论文图 8 面向超高层建筑的迁移学习: `wechat/assets/public-safe/ref-tang2025-JBE/fig-08-transfer-learning.jpg`
- 论文图 9 验证集回归性能: `wechat/assets/public-safe/ref-tang2025-JBE/fig-09-regression-performance.jpg`
- 论文图 16 不同基本风压下的位移和层间位移: `wechat/assets/public-safe/ref-tang2025-JBE/fig-16-wind-pressure-sensitivity.jpg`
- 论文图 19 CAARC 建筑不同截面工况下预测值与真实值对比: `wechat/assets/public-safe/ref-tang2025-JBE/fig-19-caarc-comparison.jpg`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.jobe.2025.112131
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 19；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `6707673bdeab318e494bd2055506c6053e0196e921baba73e988ff0ed252ec10`

## 关键事实证据定位记录

- PDF file page 1：题名、六名作者、Li Chao 通讯标记、Journal of Building Engineering 103 (2025) 112131、DOI、摘要一致；收稿/修回/接收/在线日期分别为 2024-08-15、2025-01-23、2025-02-13、2025-02-21。
- PDF file pages 3-4, §2.1：刚性楼板、节点/构件边与质量表示；原式 (2) 的风压因子乘积已核对，按面积计风荷载应转换为节点力，节点力单位 N。
- PDF file pages 5-6, §2.2：998 个 21–33 层结构经三风压增强为 2994 组图样本；300 个 45–63 层基础组合经尺寸增强为 1200 组，总计 4194；不能称为同样数量的独立拓扑。
- PDF file page 10, §3：另写 2944 组，与 page 6 的 2994 不一致。80%/20% 训练/验证切分，66084 是位移和层间位移的预测值数量；未写明按拓扑分组切分，不能据此排除同拓扑增强样本的交叉分配。
- PDF file pages 7-9, §2.3：编码、消息传递、楼层融合和解码，以及预训练参数到超高层结构训练的迁移，均与当前图文一致。
- PDF file page 10 Eq. (14)：Accuracy=1−平均绝对相对误差，不是分类准确率；page 11 Table 6 四项位移类指标由 0.8370/0.8228/0.8212/0.8073 变为 0.9196/0.9213/0.9172/0.9157，第五项由 0.9283 到 0.9810。正文约84%→92%的概括与五项算术均值84.332%→93.096%不同，当前稿采用分项值。
- PDF file page 10 Table 5：第五输出正文名为一阶自振周期，但表内单位 rad/s；page 8 Eq. (9) 也称 period。已在正文说明冲突，不替作者改频率或单位。
- PDF file pages 9-12：最大楼层响应/位移趋势损失作用、楼层数外推试验及30/33层范围内超过90%的描述，对应现稿；不能泛化到所有高度或拓扑。
- PDF file pages 13-15 Fig. 16：风压0.30/0.45/0.60/0.75 kN/m²；位移、层间位移分别按73.62/3.48 mm归一化。原文以1.05经验修正应对部分低估，不是普适安全保证。
- PDF file pages 15-17, §4.2/Figs.18-19：60层、182.88×45.72×30.48 m的CAARC结构、五种尺寸情景、层间位移2.61 mm归一化均对应。Fig.18总体较大的S1尺寸、正文S1保守/S5超限与Fig.19响应标签需澄清，当前稿不据此重新排序安全性。
- PDF file pages 16-17, §4.3/Table8：三流程总时间3min13s、1min40s、17.33s。但第三行15s+2.63s=17.63s，原文差额未解释。GTX1050Ti/i5-11500下计时含软件转换，不含前期数据生成/训练；page15另报500轮迁移训练7.9h。
- PDF file page 17, §5：仅钢筋混凝土框架静力分析；墙单元与动态时序模型需扩展。现稿将方案筛选标为应用建议，未声称完成优化闭环、全套规范验算或工程部署。
- 七张选图对应源页：Fig.1 p3、Fig.4 p6、Fig.6 p8、Fig.8 p9、Fig.9 p11、Fig.16 p15、Fig.19 p17。图/图例及已有公开素材与原文一致；原review中式2的p3、Fig16的p14和结论p18定位已废止。

## 当前事实修正与完整度

### 2026-10-05 重建后的源文复核结论

源内冲突除正文所述外，page5 Table4末行标Concrete grade(m)却为135–226.8，page15弹性模量写3.8×10^7/3.6×10^7 MPa，page9 Eq.(13)用Loss_N而前文称Loss_MAE；不擅自修理源数据。

### 事实与完整度分别判断

- 本轮对上述两渠道现有内容分别校正，未用公众号转换覆盖独立RTD。错误和歧义已纠正或明确归属，不宣称独立复现论文计算结果。
- RTD仍为`legacy_intro`，`full_paper_coverage=false`。原文共19页、19图、8表、14编号公式、55项参考文献；当前仅选图1,4,6,8,9,16,19与式(2)，没有逐段完整正文、全部图表/公式及参考文献链；无附录。顶部封面存在，但缺全文页面的精简公众号链接行。
- 微信当前内容已按来源审校；没有新上传、后台手机公式/插图/封面预览或发布。历史工作记录不得继承为新版本验收。
- 本轮重新生成内容及审查记录，未声称已恢复先前丢失提交的完全相同字节。最终检查与新内容指纹由整批集成重新计算。
