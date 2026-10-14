# WOEAI 制作论文分类复核（44 篇）

审计基准：2026-10-14 读取 main 的注册表（文件 SHA 75a00d1a5f3c232c9bc86fb66cb0d2aa521c79bd）。75 条研究论文记录中，44 条 content_production=included、31 条 excluded；本表逐一覆盖 44 条 included，无重复无遗漏。作者次序与通信作者身份不参与判断。只读复核，未修改仓库。

一级保留“工程结构抗风 / 海上漂浮风电”，二级使用“数值风洞 / 结构抗风 / 一体化分析 / 混凝土浮体 / 数值水池”。固定式风电与风机气动仍按用户既有决定作为“海上漂浮风电”的关联基础研究。

## 结论

- 40 篇可保留原归属后简名，其中 3 篇需明确关联基础研究边界、1 篇需说明跨领域减振基础边界
- 建议 4 篇调整二级：ref-zheng2025-OE（S355 钢浮体）从混凝土浮体改一体化分析；ref-zheng2025-QHDXXB、ref-zheng2023-JRSE、ref-zhou2017-E 从数值水池改一体化分析
- 调整后：数值风洞 21、结构抗风 10、一体化分析 11、混凝土浮体 2、数值水池 0
- 数值水池保留为研究方向；不能为凑齐栏目把物理水池试验、所有含水动力或 OpenFAST 的论文放入其中。现有 44 篇没有以数值波浪/水流生成、传播、吸收或水池求解方法为主要贡献的直接证据
- 如一体化分析严格限定“浮式整机耦合分析”，3 篇固定式/气动基础论文不能字面完全落入。因此建议在方向说明中明示包括支撑整机分析的气动、控制与支撑结构优化基础；不新增第六类，不把基础论文称作已完成浮式验证

## 证据与限制

44 篇均读取了工作区已有授权 PDF 的题名、摘要和必要正文；非仅按题名猜测。2025 等效静力波浪荷载另核 §2.2 材料。31 份副本匹配既有源文件清单哈希、1 份匹配清单传输副本哈希、3 份匹配现行注册表审计副本哈希；其余 9 份核对题名/DOI 与内容身份，但未建立与历史原件字节一致性。分类复核不等于完成全文制作审核，也不改 source.status 或内容证据。原文、私有源文件路径、私有清单未置入本报告。ref-feng2023-HKXYGC 的注册表标识 21213/dfdg234 不是有效 DOI，本报告使用注册表来源链接；书目标识待上游核实，未修改注册表。

## 分类判据与交叉边界

- 数值风洞：风场/入流/湍流、CFD 几何前处理、多尺度与 AI 风场重建；建筑或塔线作为应用不自动转结构抗风
- 结构抗风：结构风荷载、响应、极值、易损性与减振部件；采用 CFD 不自动转数值风洞。2026 He 的海上平台 TLD 暂保留为跨领域减振基础；这是待确认的归类建议。若一级严格按实际应用对象归类，可改为海上漂浮风电的一体化分析关联基础；但论文本身未做浮式整机耦合分析，不能因采用 CFD/自由面追踪就改数值水池，也不能写成已验证高层建筑抗风或海上浮式整机
- 一体化分析：风机平台、塔架、系泊、气水弹控、长期响应、载荷传递与系统优化；按已确认的关联基础规则容纳固定式和气动论文，并显式注明其研究对象
- 混凝土浮体：混凝土材料、浮体结构设计与强度，或混凝土/钢浮体材料对照为核心；仅为平台结构计算不足以归此类
- 数值水池：以数值波浪/流场、自由面水动力求解与方法验证为核心；物理风洞浪槽联试不是该类的充分条件

## 全量核对表

| 序号 | publication_ref | 题名 | 一级 | 当前二级 | 建议二级 | 判断 | 证据概述 | 证据位置 | 来源链接 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ref-zhao2026-BE | A novel framework for urban geometry rapid reconstruction utilizing high-resolution stereo satellite imagery for wind environment assessment | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 卫星立体影像重建 CFD 可用城市几何；贡献是风场模拟前处理与城市风环境评估 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.buildenv.2026.114811 |
| 2 | ref-he2026-OE | Numerical research on the impact of built-in rectangular poles on the dynamic characteristics of rectangular liquid tanks | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 跨领域减振基础；需说明边界 | 内置矩形立柱 TLD 的非线性液舱晃荡、CLS-VOF 与等效机械模型；以结构减振部件方法为归类依据，摘要应用背景为海上平台 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.oceaneng.2026.124728 |
| 3 | ref-zhao2026-BS | A fast prediction framework for urban microscale wind environment based on precomputed CFD database | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 城市分块 CFD 预计算数据库、风速比与风压系数的快速风环境预测 | PDF file page 1, 摘要 | https://doi.org/10.1007/s12273-025-1379-7 |
| 4 | ref-he2026-OE-structural | Structural design and optimization of a novel semi-submersible floating offshore wind turbine platform using reinforced concrete | 海上漂浮风电 | 浮式混凝土平台结构设计 | 混凝土浮体 | 归类保留 | 钢筋混凝土半潜浮体模块化方案、主尺度优化、预应力筋及极限强度校核；混凝土材料与浮体设计是核心 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.oceaneng.2025.123951 |
| 5 | ref-tang2026-RE | A novel framework for temporal super-resolution of wind in urban energy applications | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 边界层湍流时间超分辨率、注意力机制、物理约束与时空统计检验；不是风机系统动力学 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.renene.2025.124336 |
| 6 | ref-he2025-POF | Numerical investigation of nonlinear sloshing features and vibration mitigation efficiency of the implanted pole tuned liquid damper | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 归类保留 | 植入立柱 TLD、结构与液体双向耦合，并验证高层建筑风致振动减振效果 | PDF file page 2, 摘要 | https://doi.org/10.1063/5.0293483 |
| 7 | ref-yang2025-JBE | Statistical extremes of 2D vectorial response for wind-excited tall buildings | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 归类保留 | 高层建筑风致二维矢量响应极值、方向相关性和设计响应估计 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.jobe.2025.113635 |
| 8 | ref-zheng2025-OE | Evaluating equivalent static wave loads for a delta-shaped semi-submersible 10-MW wind turbine | 海上漂浮风电 | 浮式混凝土平台结构设计 | 一体化分析 | 建议调整二级 | 波压、塔基及导缆孔荷载耦合的等效静力波浪荷载与浮体强度评估；§2.2 明确 S355 钢板，非混凝土浮体 | PDF file page 1, 摘要；PDF file page 3, §2.2 | https://doi.org/10.1016/j.oceaneng.2025.121336 |
| 9 | ref-zheng2025-QHDXXB | 中心与偏心布置半潜风机动力特性的模型试验 | 海上漂浮风电 | 数值风浪流水池 | 一体化分析 | 建议调整二级 | 中心与偏心风机平台和系泊优化、风浪联合缩尺试验、系统动力响应与平台选型；物理水池不等于数值水池 | PDF file page 1, 摘要；PDF file page 4, §2–3 缩尺模型/模型试验设置 | https://doi.org/10.16511/j.cnki.qhdxxb.2025.27.037 |
| 10 | ref-tang2025-JBE | Training and application of graph neural networks for predicting structural responses targeted at tall building structures | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 归类保留 | 高层建筑 GNN 结构分析代理，预测位移、层间位移与周期并服务抗风优化 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.jobe.2025.112131 |
| 11 | ref-zhao2025-SCS | A novel framework utilizing 3D Gaussian Splatting to construct building geometry for urban wind simulations | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 3D Gaussian Splatting 城市建筑几何重建，输出 CFD 可用模型并检验行人风环境 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.scs.2025.106237 |
| 12 | ref-chen2024-POF | Comparing methods for reducing artificial pressure fluctuations using large eddy simulation in high-rise building wind load assessment | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 比较入口质量修正、无散修正及局部压力修正对 LES 人工压力波动的影响；建筑荷载为验证算例 | PDF file page 2, 摘要 | https://doi.org/10.1063/5.0240163 |
| 13 | ref-tang2024-POF | Super-resolution reconstruction of wind fields with a swin-transformer-based deep learning framework | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | Swin-Transformer 湍流风场空间超分辨率，理想流与真实边界层风验证 | PDF file page 2, 摘要 | https://doi.org/10.1063/5.0237112 |
| 14 | ref-wang2024-ES | A new controllable weak recycling inflow turbulence generator for evaluating wind effects on building in LES | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 可控弱循环湍流入流生成与粗糙地表边界层保持；高层建筑风压仅验证方法 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.engstruct.2024.118742 |
| 15 | ref-he2024-JBE | Numerical research on nonlinear liquid sloshing and vibration control performance of tuned liquid damper | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 归类保留 | 消防水箱 TLD 与高层结构双向耦合，量化全尺寸建筑风致减振效果 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.jobe.2024.110660 |
| 16 | ref-li2024-POF | A novel vector potential random flow generation method for synthesizing divergence-free homogeneous isotropic turbulence with arbitrary spectra | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 通过矢量势旋度合成无散、任意谱均匀各向同性湍流；数值入流基础方法 | PDF file page 2, 摘要 | https://doi.org/10.1063/5.0194006 |
| 17 | ref-chen2024-JCP | A coherence-improved and mass-balanced inflow turbulence generation method for large eddy simulation | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | CMRFG 相干改进、质量守恒与无散湍流生成，解决 LES 入口与人工压力问题 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.jcp.2023.112706 |
| 18 | ref-zhou2023-AE | Evaluation of floating wind turbine substructure designs by using long-term dynamic optimization | 海上漂浮风电 | 浮式风机系统一体化分析与优化 | 一体化分析 | 归类保留 | 浮式风机降阶动力模型、Kriging 长期响应代理及平台和系泊多目标优化 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.apenergy.2023.121941 |
| 19 | ref-zhao2023-BS | Multiscale simulation of the urban wind environment under typhoon weather conditions | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 台风下 NWP-CFD 多尺度嵌套、局地观测同化与城市风场预测 | PDF file page 1, 摘要 | https://doi.org/10.1007/s12273-023-0991-7 |
| 20 | ref-zheng2023-MS | Efficient optimization design method of jacket structures for offshore wind turbines | 海上漂浮风电 | 浮式风机系统一体化分析与优化 | 一体化分析 | 关联基础研究；二级扩展边界 | 固定式导管架结构代理优化，并用耦合动力、屈曲及疲劳验证；作为漂浮风电关联基础研究 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.marstruc.2023.103372 |
| 21 | ref-zhang2023-S | Estimation of dynamic wind forces on a steel lattice tower based on generalized wind force spectra | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 归类保留 | 由广义风力谱和相干函数估计钢格构塔动力风荷载，并以气弹试验响应验证 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.istruc.2022.12.073 |
| 22 | ref-wang2023-JWEIA | Large eddy simulation of turbulent atmospheric boundary layer flow based on a synthetic volume forcing method | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 合成体积力作为动量方程源项生成自保持大气边界层湍流，抑制非物理压力波动 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.jweia.2023.105326 |
| 23 | ref-zheng2023-JRSE | Wind tunnel and wave flume testing on directionality dynamic responses of a 10 MW Y-shaped semi-submersible wind turbine | 海上漂浮风电 | 数值风浪流水池 | 一体化分析 | 建议调整二级 | 10 MW Y 型半潜风机风洞浪槽联合模型试验与 OpenFAST 气水弹控耦合验证；核心为方向性系统响应 | PDF file page 2, 摘要；PDF file page 4, §II 模型试验设置 | https://doi.org/10.1063/5.0131279 |
| 24 | ref-zhang2023-ES | Reconstruction of dynamic wind forces on a transmission steel lattice tower using aeroelastic wind tunnel test data | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 归类保留 | 有限结构位移、模态模型和 Kalman 反演重建输电格构塔动力风荷载 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.engstruct.2022.115167 |
| 25 | ref-feng2023-HKXYGC | 基于数值风洞试验的核电厂微地形风场分析与验证 | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 核电厂复杂地形和建筑群 LES 风场，与物理风洞风速、风压验证并识别风灾风险区域 | PDF file page 1, 摘要 | https://github.com/lichao689/woeai/blob/main/docs/data/publications.json |
| 26 | ref-zhao2023-GYJZ | 基于首次超越破坏的输电塔强风易损性分析 | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 归类保留 | 输电塔风荷载能力曲线、首次超越破坏限态与强风易损性 | PDF file page 2, 摘要 | https://github.com/lichao689/woeai/blob/main/docs/data/publications.json |
| 27 | ref-chen2022-JWEIA | Consistency improved random flow generation method for large eddy simulation of atmospheric boundary layer | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | CIRFG 同时满足空间相关和速度分量互相关的大气边界层 LES 入流生成 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.jweia.2022.105147 |
| 28 | ref-li2022-SOS | Dynamics of a Y-shaped semi-submersible floating wind turbine: a comparison of concrete and steel support structures | 海上漂浮风电 | 浮式混凝土平台结构设计 | 混凝土浮体 | 归类保留 | 同型混凝土与钢 Y 型半潜平台的材料效应对照，联合风浪试验与多体耦合模拟；材料比较优先归混凝土浮体 | PDF file page 2, 摘要 | https://doi.org/10.1080/17445302.2021.1937801 |
| 29 | ref-yang2022-AS | Research on Equivalent Static Load of High-Rise/Towering Structures Based on Wind-Induced Responses | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 归类保留 | 高层和高耸结构风致响应分解、阵风荷载系数及等效静力风荷载 | PDF file page 1, 摘要 | https://doi.org/10.3390/app12083729 |
| 30 | ref-zhao2021-EFM | Multiscale modelling of planetary boundary layer flow over complex terrain: implementation under near-neutral conditions | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 复杂地形近中性 PBL 的 NWP-CFD 单向嵌套、湍黏一致性和边界插值 | PDF file page 1, 摘要 | https://doi.org/10.1007/s10652-021-09796-4 |
| 31 | ref-zhao2021-AR | New consideration of lateral boundary treatment for meso- and micro-scale nested PBL simulations over complex terrain | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 中小尺度嵌套侧边界松弛，解决复杂地形 PBL 模拟过约束与数值稳定性 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.atmosres.2021.105507 |
| 32 | ref-zhou2021-OE | Global sensitivity study on the semisubmersible substructure of a floating wind turbine: Manufacturing cost, structural properties and hydrodynamics | 海上漂浮风电 | 浮式风机系统一体化分析与优化 | 一体化分析 | 归类保留 | 浮式风机平台主尺度与系泊参数对成本、结构属性及水动力响应的全局敏感性 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.oceaneng.2021.108585 |
| 33 | ref-zhao2021-TYNXB | 基于NWP/CFD嵌套的复杂地形风场模拟研究 | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | NWP/CFD 嵌套与插值重建复杂地形风场日变化；风电场选址为应用，核心为风场计算 | PDF file page 1, 摘要 | https://github.com/lichao689/woeai/blob/main/docs/data/publications.json |
| 34 | ref-li2020-JWEIA | RANS simulation of horizontal homogeneous atmospheric boundary layer over rough terrains by an enriched canopy drag model | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 扩展冠层阻力模型保持粗糙地表 RANS 水平均匀大气边界层 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.jweia.2020.104281 |
| 35 | ref-zhou2020-RE | Importance of platform mounting orientation of Y-shaped semi-submersible floating wind turbines: A case study by using surrogate models | 海上漂浮风电 | 浮式风机系统一体化分析与优化 | 一体化分析 | 归类保留 | FAST 气水弹控耦合、代理模型及长期海况，评估半潜平台安装方向对全寿命性能影响 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.renene.2020.04.014 |
| 36 | ref-li2018-AE | Optimization of blade pitch in H-rotor vertical axis wind turbines through computational fluid dynamics simulations | 海上漂浮风电 | 浮式风机系统一体化分析与优化 | 一体化分析 | 关联基础研究；二级扩展边界 | 垂直轴风机可变桨距控制和 CFD-遗传算法优化；属于风机气动与控制关联基础，不是浮式整机案例 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.apenergy.2017.12.035 |
| 37 | ref-xiao2018-KXJSYGC | 复杂地形下基于计算流体动力学的风速比计算 | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 复杂地形全风向 CFD 风速比方法和数据库基础；服务塔线抗风，但研究输出为地形风场 | PDF file page 1, 摘要 | https://github.com/lichao689/woeai/blob/main/docs/data/publications.json |
| 38 | ref-zhou2017-E | Directionality Effects of Aligned Wind and Wave Loads on a Y-Shape Semi-Submersible Floating Wind Turbine under Rated Operational Conditions | 海上漂浮风电 | 数值风浪流水池 | 一体化分析 | 建议调整二级 | 联合风浪试验与耦合多体模型解释 Y 型半潜风机方向性，识别一、二阶水动力对系统响应的贡献 | PDF file page 1, 摘要；PDF file pages 5/10–13, §3/4 试验与耦合数值模型 | https://doi.org/10.3390/en10122097 |
| 39 | ref-li2017-BS | Effects of inflow conditions on mountainous/urban wind environment simulation | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 经验剖面和多尺度插值两种入流条件对山地城市 CFD 风环境结果的影响 | PDF file page 1, 摘要 | https://doi.org/10.1007/s12273-017-0348-1 |
| 40 | ref-li2017-AS | Passive Vibration Control of a Semi-Submersible Floating Offshore Wind Turbine | 海上漂浮风电 | 浮式风机系统一体化分析与优化 | 一体化分析 | 归类保留 | 半潜浮式风机平台-塔架-TMD 动力学与参数优化，评估极值和疲劳减振 | PDF file page 1, 摘要 | https://doi.org/10.3390/app7060509 |
| 41 | ref-li2013-RE | 2.5D large eddy simulation of vertical axis wind turbine in consideration of high angle of attack flow | 海上漂浮风电 | 浮式风机系统一体化分析与优化 | 一体化分析 | 关联基础研究；二级扩展边界 | 比较 2D/2.5D URANS 与 2.5D LES 对垂直轴风机高攻角失速和气动力的预测；风机气动关联基础 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.renene.2012.09.011 |
| 42 | ref-li2012-JWEIA | A revised empirical model and CFD simulations for 3D axisymmetric steady-state flows of downbursts and impinging jets | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | 修正下击暴流/冲击射流经验速度场，以 RSM CFD 校核；属于非标准来流建模 | PDF file page 1, 摘要 | https://doi.org/10.1016/j.jweia.2011.12.004 |
| 43 | ref-li2012-GCLX | 基于超越阈值概率的行人风环境数值评估 | 工程结构抗风 | 数值风洞与湍动入流 | 数值风洞 | 归类保留 | CFD 数值风洞与超越阈值概率结合，评估行人风舒适度和危险度 | PDF file page 1, 摘要 | https://github.com/lichao689/woeai/blob/main/docs/data/publications.json |
| 44 | ref-li2010-WAS | Large eddy simulation of wind loads on a long-span spatial lattice roof | 工程结构抗风 | 工程结构抗风与优化 | 结构抗风 | 归类保留 | 大跨空间屋盖风压、峰值、谱和空间相关性评估；采用 LES/DSRFG 是手段，结构风荷载为主输出 | PDF file page 1, 摘要 | https://doi.org/10.12989/was.2010.13.1.057 |

## 分类迁移记录

本轮把五个短名称写入统一分类定义，并同步75条当前分类、17篇公众号正文中的方向行、研究/学术成果/工程应用页面和生成视图。历史书目与旧提交证据保留原文，制作决策不变。

额外修正未纳入制作的 ref-zhang2025-CSICM：归入“海上漂浮风电 / 一体化分析”，保持 excluded。原文 PDF file page 1 摘要、page 4贡献说明、page 5§2.1 表明研究重点是台风下单桩风机整机载荷响应及偏航减载；使用SWAN/ADCIRC不等于数值水池方法贡献。它是固定式风电关联基础研究，不作为浮式整机实证。调整后全部75条及44篇制作论文均无数值水池直接归类，研究方向保留。

公众号方向文字已改变，因此当前17篇状态回到 awaiting_review。此前官方草稿成功更新记录逐字保存在 confirmed_draft_update_history，未重写提交时间、原文指纹或手机预览情况；本轮尚未重新投递。17篇RTD全文正文和资产未变，原有核验证据仍有效。

封面与STYLE修订为后续独立批次；此分类迁移不声称封面、微信实际合集或远端草稿已更新。新纳入的27篇原文共473页，尚需逐篇全文制作与独立覆盖审核，不用摘要核对替代全文验收。
