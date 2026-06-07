---
title: 论文解读 | 预计算 CFD 数据库如何加速城市微尺度风环境预测
status: draft-public-safe
research_family: 建筑结构抗风
subdirection: 数值风洞与湍流入流
publication_ref: ref-zhao2026-BS
zotero_key: CGKPKZ8I
doi: 10.1007/s12273-025-1379-7
original_year: 2026
publication_mode: first_publish
wechat_status: drafting
previous_published_url:
latest_published_url:
revision_note:
source_checked: false
copyright_checked: false
public_safety_checked: false
formula_preview_checked: false
figure_preview_checked: false
---

# 论文解读 | 预计算 CFD 数据库如何加速城市微尺度风环境预测

城市风环境评估常常面临一个两难问题：如果要看清街区尺度的风场细节，就需要较高分辨率的计算；但如果每次规划调整、场地评估或工程咨询都重新做完整 CFD，时间成本又很高。

这篇发表在 **Building Simulation** 的论文尝试回答一个很直接的问题：能不能把城市微尺度风场的高精度计算结果提前组织成数据库，让后续预测和应用更快发生？

## 论文信息

- 论文题名: A fast prediction framework for urban microscale wind environment based on precomputed CFD database
- 作者: Zhao Peisheng; **Li Chao**; Yang Chao; Han Zhichen; Chen Lingwei; Hu Gang; Li Lixiao; Wang Xiaolu
- 期刊: Building Simulation
- 年份: 2026
- 卷期页码: 19(2): 333-357
- DOI: https://doi.org/10.1007/s12273-025-1379-7
- WOEAI 官网条目: https://winddee.cn/Publications.html#ref-zhao2026-BS
- WOEAI 相关方向: 建筑结构抗风 / 数值风洞与湍流入流

## 研究问题

城市微尺度风环境关系到行人舒适度、建筑群通风、污染物扩散、城市规划和局地风风险评估。传统数值天气预报可以提供区域尺度风场背景，但在空间和时间分辨率上往往难以直接支撑街区尺度判断。

另一方面，CFD 可以解析更细的建筑绕流和局地风场，但如果每一个新场景都从头计算，工程应用会受到计算成本限制。

因此，这篇论文关注的核心问题是：

> 如何在保留 CFD 局地风场解析能力的同时，提高城市微尺度风环境预测的效率？

## 方法贡献

论文提出的思路是建立一个**预计算 CFD 数据库**。

根据公开摘要，整体框架包括几个关键步骤：

1. 基于 GIS 建筑与地形模型建立城市计算对象；
2. 将城市模型划分为 `1 km × 1 km` 的区块；
3. 对每个区块分别开展 CFD 计算；
4. 将各区块的计算结果组织成预计算数据库；
5. 在应用阶段调用数据库中的风速比、风压系数等信息，实现更快的风场预测和展示。

这个思路的重点不是简单“少算一点”，而是把大量重复出现的城市风场计算前置，让后续预测从“重新求解”变成“调用和组合已有高分辨率结果”。

## 关键发现

从公开摘要可确认，论文做了两类重要验证。

第一，论文分析了区块之间需要多长的过渡区域，才能考虑周边建筑对局地风场的气动影响。这个问题很关键，因为如果区块切分过于生硬，相邻区块边界处的风场可能不连续。

第二，论文比较了相邻区块交界处的风剖面差异。公开摘要指出，相邻区块界面处的风剖面差异较小，这支持了独立区块计算方法的可行性。

此外，论文还将统计得到的平均风速与多个气象站一年的实测数据进行了对比，用于展示该框架的预测能力。

## 公式说明

- 使用公式: no formulas used in this draft
- 公众号公式呈现方式: 本篇样板稿暂不放公式；如果后续从论文正文补入风速比、风压系数或误差评价公式，应使用公众号发布流程支持的直接公式格式，不转成图片。
- 公式移动端预览结论: pending WeChat backend mobile preview

## 工程意义

这篇论文对工程应用的价值在于，它把城市风环境评估从“一次任务一次完整计算”的模式，推进到“预计算数据库 + 快速调用”的模式。

对城市风环境、复杂地形风场和数值风洞相关工作来说，这类框架有几个潜在应用场景：

- 城市片区规划阶段的快速风环境筛查；
- 建筑群布局调整时的多方案对比；
- 局地风风险或行人风舒适度的初步判断；
- 风环境数据与 WebGIS 平台结合后的可视化展示；
- 后续与 AI surrogate model、快速重构模型或工程咨询平台结合。

需要强调的是，预计算数据库并不等于完全替代高精度专项 CFD。更稳妥的理解是：它可以帮助工程人员更快进入判断和筛选阶段，而对关键项目、特殊边界条件或高风险区域，仍然需要更有针对性的计算与验证。

## 适用边界

这篇论文不应被解读为“所有城市风环境问题都可以直接秒级精确预测”。从公开信息看，它的适用性依赖几个前提：

- 城市几何、地形和边界条件需要与数据库构建逻辑匹配；
- 区块切分和过渡区域长度需要经过验证；
- 数据库覆盖的风向、风速、地貌和建筑条件会影响预测范围；
- 对特殊建筑形态、局地强干扰区域或极端风情景，仍需谨慎复核；
- WebGIS 平台集成提升的是应用效率，但不自动消除模型假设带来的不确定性。

换句话说，这项工作更适合被看作城市微尺度风环境快速评估的工程化框架，而不是脱离场景约束的通用黑箱。

## 图示与素材来源

- 使用图片: pending
- 图片优先来源: 论文原始高清图
- 建议优先检查的图片: 论文方法流程图、区块划分示意图、WebGIS 平台展示图、气象站验证结果图
- 图示来源或生成方式: 待从作者自有原始图、作者稿件图或具备复用权限的论文图中选择；未确认前不提交图片文件
- 版权说明: pending author or publisher reuse confirmation
- 清晰度预览结论: pending WeChat backend mobile preview

## 延伸阅读

- WOEAI 建筑结构抗风方向: https://winddee.cn/BuildingStructuralWindResistance.html
- WOEAI 学术成果条目: https://winddee.cn/Publications.html#ref-zhao2026-BS
- DOI: https://doi.org/10.1007/s12273-025-1379-7

## 联系入口

如果你关注城市风环境快速评估、数值风洞、复杂地形风场或工程软件化应用，可以通过以下方式联系：

- Website: https://winddee.cn
- Email: lichaosz@qq.com

## 发布前人工复核项

- [ ] 用 Zotero/PDF 核对作者、期刊、页码、DOI 和摘要理解。
- [ ] 确认是否使用论文原始高清图，以及每张图的复用权限。
- [ ] 在公众号后台手机预览图片清晰度。
- [ ] 如加入公式，确认公式不以图片形式呈现，并完成手机预览。
- [ ] 用公众号后台预览检查标题、段落长度和深色模式显示。
