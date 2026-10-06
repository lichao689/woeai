---
publication_ref: ref-chen2024-JCP
doi: 10.1016/j.jcp.2023.112706
wechat_status: awaiting_review
wechat_author: Chen Lingwei
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
wechat_cover_image: wechat/assets/public-safe/ref-chen2024-JCP/cover-wechat-900x383-imagegen-v1.png
rtd_cover_image: wechat/assets/public-safe/ref-chen2024-JCP/cover-wechat-900x383-imagegen-v1.png
---

# ref-chen2024-JCP 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-chen2024-JCP.md`
- RTD正文: `docs/source/paper-notes/ref-chen2024-JCP.rst`
- 封面素材: `wechat/assets/public-safe/ref-chen2024-JCP/cover-wechat-900x383-imagegen-v1.png`
- 论文图 7 CMRFG 方法流程图: `wechat/assets/public-safe/ref-chen2024-JCP/fig-07-cmrfg-workflow.png`
- 论文图 4 SW1 至 SW4 工况流场统计脉动: `wechat/assets/public-safe/ref-chen2024-JCP/fig-04-statistical-flow-fluctuations.png`
- 论文图 17 不同空间间距下的 Y 方向空间相干函数对比: `wechat/assets/public-safe/ref-chen2024-JCP/fig-17-spatial-coherence-validation.png`
- 论文图 28 脉动压力系数分布云图: `wechat/assets/public-safe/ref-chen2024-JCP/fig-28-pressure-fluctuation-contours.png`
- 论文图 30 8 s 时刻 Q=1000 的等值面，按瞬时速度大小着色（流向从左到右）: `wechat/assets/public-safe/ref-chen2024-JCP/fig-30-q-criterion-vortices.png`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.jcp.2023.112706
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 31；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `60ab26625848c6c428b15f221a4f2a3a647ad34bc29c1aaea3e00ad777e16693`

## 关键事实证据定位记录

- 身份与摘要：PDF file page 1；期刊卷年为 2024，在线发表日为 2023-12-05，DOI 和五名作者一致。
- 单波验证：PDF file page 4–9 Section 2、Eqs. (1)–(18)、Table 1。SW1 的入口边缘最大压力标准差约为动压 0.84 倍，X=2 m 处约 15%；SW4 双向周期修正使初始 TKE 从约 1.64 降为 1.53 m²/s²，降低约 6.7%。
- 相干输入范围：PDF file page 13 Eq. (48) 后段直接选定 u 分量的 Y 向相干函数；PDF file page 16 说明共用波数可能造成 v/w 三维互谱偏差。实部与绝对值的区别及负相干见 PDF file page 17–18。
- 入口质量平衡式：PDF file page 5 Eq. (8)；波数周期修正：PDF file page 14–15 Eq. (54)–(55)。均匀网格质量通量严格恒定；非均匀网格可能仍需小幅修正。
- 随机实现筛选：PDF file page 20–22 Section 4.4、5.1.1，CBC 每工况 50 次并保留最佳拟合随机参数；PDF file page 26 Section 5.2.2，KCM 入流独立 20 次。
- HA2 在 x/M=30 约 12%，HA1 中心区域约 1.5%，但入口/侧边交线仍有局部人工压力：PDF file page 27；只验证均匀湍流：PDF file page 29 Section 6。
- 微信图：Fig. 4 / PDF file page 8；Fig. 7 / PDF file page 14；Fig. 17 / PDF file page 21；Fig. 28 / PDF file page 25；Fig. 30 / PDF file page 26。最后一图保留 Q=1000、8 s、按瞬时速度着色和从左到右的流向。

## 当前事实修正与完整度

### 2026-10-05 当前全文审校与覆盖结论

- 本日已完整阅读同一份 31 页原文；本轮重新校验 PDF 哈希和全部页面，重新打开恢复的 Eq. (43)/(46) 及微信事实定位页核对当前文本。当前输出不是旧文件字节恢复。
- RTD：`full_paper_coverage=false`。主 PDF 的各节与全部编号公式/图表/参考文献有对应，但被引用的附录 A/B 源文不在本 PDF 中，部分分图及图中文字仍须补齐。
- 微信：已独立按原文修正积分符号、相干范围、实部/负值、50/20 次随机筛选以及 SW4 的 TKE 代价；没有用 RTD 代替源文。

### 原文到 RTD 的覆盖

- 身份、摘要、关键词：PDF file page 1；符号表：PDF file page 2–3，已对应。bulk velocity 已按面积分定义改为截面平均速度。
- Section 1：PDF file page 1、3–4，文献综述与引用、论文结构均在。
- Sections 2.1–2.3.2：PDF file page 4–9，单波、质量修正公式、Table 1、四个工况、设置及正负结果均在。
- Sections 3.1–3.2.3：PDF file page 9–16，回顾、相干推导、质量平衡、截断/符号调整及限制均在。本轮恢复 PDF file page 12 Eq. (43) 的同相/正交谱与 Dirac 比值展开、PDF file page 13 Eq. (46) 的 Fourier/Dirac 中间步骤。
- Sections 4.1–4.4：PDF file page 16–21，CBC 数据、实部/负相干、非遍历性、50 次集合与最佳实现筛选均在。
- Sections 5.1–5.2.4：PDF file page 21–29，HI1–HI5、HA1–HA2、LES/准 DNS、20 次筛选、边界压力、能谱局限均在。
- Section 6：PDF file page 29，四段结论及仅验证均匀湍流的边界均在。
- Fig. 1–35 全部在。源页：PDF file page 5（1）、6（2）、7（3）、8（4）、9（5–6）、14（7）、16（8–9）、17（10–11）、18（12）、19（13–14）、20（15–16）、21（17–18）、22（19–21）、23（22–23）、24（24–25）、25（26–28）、26（29–30）、27（31–33）、28（34）、29（35）。部分分图说明如 Fig. 4、8–9、11、14–17、19–22、25–26、31、34–35 未逐项中文转写；流程/边界图的关键英文还需全量对照。
- Table 1–5 为中文可编辑表，源页为 PDF file page 7、18（2–3）、21、24；全部原表参数在。
- Eq. (1)–(64) 均在，补回上述两个被缩写的推导链。
- 参考文献 [1]–[58] 来自 PDF file page 30–31，均在，正文引用编号有对应。
- 附录 A/B：正文 PDF file page 10、15–18、23–24 多次引用，至少涉及 A12、B18；PDF file page 29 结论之后直接是声明及参考文献，当前源中无附录正文。未凭理论自行补写，不能声称附录已读/已译。
- 结论/参考文献之间未混入禁止的出版尾注；封面位置及稳定完整引用保留。

### 更正及需要保留的边界

1. Eq. (43)/(46) 补齐中间式；微信质量平衡改为 u1(x,t) 的面积分，保持空间依赖（PDF file page 5 Eq. (8)）。
2. 微信补清只有 u 分量/Y 向相干直接输入、保留相干实部及负值、CBC 50 次/KCM 20 次及最佳实现筛选（PDF file page 13、17–18、20、26）。
3. SW4 双向周期修正的 TKE 降低约 6.7% 不能省略（PDF file page 7–9）；Fig. 30 的 Q=1000、8 s、速度着色及流向已补。
4. 摘要“没有人工压力”按原文保留；正文 PDF file page 27、29 的入口/侧边交界残余压力必须同时保留。
5. Table 5 的 256×256×128 = 8,388,608，而 PDF file page 25 正文为 8.34 million，未擅自统一。PDF file page 17 Fig. 10、正文及 PDF file page 18 Table 3 对附录 A 的式号有 A8/A9/A11/A12 的不同指向，需附录源文才能判定。

剩余项：取得获准的 Appendix A/B 并审校翻译；补齐分图/关键图中文字。主 PDF 正文覆盖与含附录完整性分开判定。

### 2026-10-06 全部原图边界校准与图内文字补译

- 逐一打开核对 Fig. 1–35 的最终图像和上述对应 PDF 原页。35 幅原图均为完整嵌入位图；逐图检查原图范围内无额外 PDF 文本层或矢量标记，直接无损提取原生像素，避免旧页面截图边框切入图内。未重绘曲线、改变配色、补画标记或拉伸比例。
- 原生宽度按源图保留，例如 Fig. 3 为 1450 像素、Fig. 4 为 1582 像素、Fig. 7 为 980 像素、Fig. 17/28/30 为 1800 像素。旧截图部分左右边缘有裁入；此次恢复完整坐标、图例、色标末端、子图标记及图中说明。图片不带相邻正文、出版页眉或总图题。
- 全部 35 幅 RTD 图与公众号所用 Fig. 4、7、17、28、30 的五份对应素材均同步为完整原图；路径不变，封面未改，未上传或更新公众号后台。
- 全部图题之后补齐中文子图说明、关键坐标/图例及单位。Fig. 7 的八步流程逐项转写为中文及可编辑数学表达，保留原流程图条件；Fig. 10 的 A8/A9/B7 引用按原图保留，不据缺失附录猜改。
- 主 PDF 图像与图中文字遗漏已完成本轮修订；当前独立复核尚在进行。附录 A/B 仍不在已获授权的 31 页 PDF 内，PDF 也没有嵌入附件；因此此条记录不将含附录全文完整度改为通过。

- 独立审校逐项核对主 PDF 全部实质正文段落、64 个编号公式、5 张表及 58 条参考文献，确认没有实质正文遗漏。审校指出的 Fig. 7 两个负号、作者单位对应、出版信息译文、符号表用语及连续段落边界已修正。
- 新保留的源内差异：PDF file page 2 符号表称 k′₂,n 为“修正后”，而 PDF file page 13–15 正文称其为预生成值；PDF file page 7、26 正文把色标括号次序写为“最大、最小”，Fig. 4、28 实际为左侧最小、右侧最大。正文、图注各自忠实保留对应来源，不据此改动图像。


## 2026-10-06 读者来源范围提示

- 在论文信息后明确说明本页覆盖 31 页主文 PDF，原文引用的附录 A、B 不在该来源中，相关推导未收入本页。
- 原文身份、正文与图片内容不变；未补写无来源附录，完整覆盖继续受阻。


## 2026-10-06 附录 A/B 来源补齐与全文复核

本节替代前述“附录来源缺失”的当前结论；旧记录保留为各阶段的实际核验历史。

### 补充来源身份与覆盖

- 主文仍为前述 31 页期刊 PDF，正文、35 幅校准原图、5 张表、式 (1)–(64) 与参考文献 [1]–[58] 保留。
- 用户另行提供的 Appendix A, “Spatial coherence function and spatial correlation function”：3 页；当前核验副本 SHA-256：`f67843a2b23458f311f0dd3230304c38bc7b6d37af66cd46e0843d95c5626f84`。
- 用户另行提供的 Appendix B, “Calculation of homogeneous isotropic turbulence characteristics”：4 页；当前核验副本 SHA-256：`36e0371d69ad18a1319d1c44a89cbcc593b2fe6ca4b3b9316cc6f5f9a0419117`。
- 依据用户提供的配套附录、标题、CMRFG 主文所引用的式号及定义逐项关联来源；这两份独立 PDF 不带主文 DOI 页，不把它们称为主文 PDF 内嵌页，也不推断为未经核验的历史原始字节。
- 总来源阅读范围为 31+3+4=38 页。附录 A 的 3 页、附录 B 的 4 页均逐页渲染查阅；两附录无图、无表。新增式 (A1)–(A13)、(B1)–(B18)，连同主文共 95 个编号公式。附录 A 的 5 条、附录 B 的 1 条参考文献保留独立编号和链接，避免与主文编号冲突。
- 附录放在第 6 节结论之后、主文参考文献之前；封面、主文原图及稳定论文链接未改。不增加出版声明性尾注，不公开上传来源 PDF。

### 源内差异的处理

- Appendix A file page 2，式 (A9) 后两处 prose 写 spatial correlation function，但式 (A9) 的绝对值作用于空间相干函数 Coh。译文保留原术语，并在独立校核注中说明对象差异。
- Appendix A file page 3，式 (A11)–(A13) 的单侧表达没有显式写 Re，虽然 file page 1 的式 (A6) 定义的是复相干。保留原式；校核注说明一般复相干情形需取实部，正文均匀各向同性算例按 Appendix B 的实函数结论使用，不静默改写来源。
- Appendix B file page 3，式 (B13) 第二个积分分母印为 2πk²，与 file page 1 式 (B1) 的 4πk² 及 file page 3 式 (B15) 中的起始因子不一致。按像素保留原式并明示差异；没有把疑似排印问题擅自当作作者勘误。
- 主文 PDF file page 17 Fig. 10 的 A8/A9/B7、邻近正文 A12、file page 18 Table 3 的 A11/B7/B8 均保留原号并链接到对应附录式。A8 为双侧积分、A11 为单侧积分、A12 为离散求和，三者并非同一编号的误写；这些式给出相关函数 R，成为系数 ρ 还需零间距归一化，B8 明确列出了这一操作。图例简写 B7 不等于 B8 缺失。

### 验证结论

- 独立审校完整比对最终 RST 与附录全部 7 页源图：A 的 16 个、B 的 21 个正文段落及 31 式全部通过；中间推导、六条参考文献、假设与限制无遗漏。原文与译校说明明确分开，正文既有 31 页覆盖审校仍有效，当前 `full_paper_coverage=true`。
- 最终正文 SHA-256：`d5ae5840d3bac5f862df80383d3a29fa3f63a5a9d69cb107f9033402ca48675c`。95 个编号公式、35 幅图、5 张表、58 条主文文献及 6 条附录文献全部保留；公式/文献锚点唯一且无悬空引用。
- 公共安全检查、清单与生成物校验、168 项 Python 测试、7 项前端测试通过。17 篇实际 Sphinx HTML 的行内角色、引用和完整 mailto 链接回归通过；全部 4,998 个数学片段经 MathJax SVG 渲染无错误，其中本篇 892 个。
- 本地标准站点构建到 sitemap 扩展时受环境 socket 权限限制；保留原配置，另以仅移除 sitemap 的诊断构建确认 HTML 无警告成功。诊断构建不充当标准门禁通过；发布验收仍需最终提交对应的完整 CI 与 RTD 构建成功。
- 公众号保持 awaiting_review；本次附录工作未上传后台，未做手机公式/图片/封面预览，不继承旧版发布准备状态。
