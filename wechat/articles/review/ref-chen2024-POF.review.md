---
publication_ref: ref-chen2024-POF
doi: 10.1063/5.0240163
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
rtd_page_checked: true
wechat_cover_image: wechat/assets/public-safe/ref-chen2024-POF/cover-wechat-900x383.png
rtd_cover_image: wechat/assets/public-safe/ref-chen2024-POF/cover-wechat-900x383.png
---

# ref-chen2024-POF 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-chen2024-POF.md`
- RTD正文: `docs/source/paper-notes/ref-chen2024-POF.rst`
- 封面素材: `wechat/assets/public-safe/ref-chen2024-POF/cover-wechat-900x383.png`
- 论文图 1 不同入流湍流施加方法示意图: `wechat/assets/public-safe/ref-chen2024-POF/fig01.png`
- 论文图 7 压力系数均值和标准差剖面沿 X 方向的对比: `wechat/assets/public-safe/ref-chen2024-POF/fig07.png`
- 论文图 11 湍流特性 NMAE 沿 X 方向的变化: `wechat/assets/public-safe/ref-chen2024-POF/fig11.png`
- 论文图 23 建筑表面压力系数 NMAE 对比: `wechat/assets/public-safe/ref-chen2024-POF/fig23.png`
- 论文图 24 总基底力和基底力矩系数频谱对比: `wechat/assets/public-safe/ref-chen2024-POF/fig24.png`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 通过
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1063/5.0240163
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 24；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `9dcb3b944803d7a71a181f9b1a7fa6f44cd9a2394330ff49162c1e1b4ad85b8a`

## 关键事实证据定位记录

- 身份、日期、作者单位映射及摘要：PDF file page 2。PDF file page 1 是出版封面，不是摘要页；旧记录少计封面的页码现已替换。
- CDRFG/IMC/DFC/LPC：PDF file page 3–5 Section II、Eqs. (1)–(11)、Fig. 1；振幅系数为 2，Eq. (8) 为 3.7β 的 −0.3 次幂。LPC 要求入口/出口压力零梯度，并合理选择建筑影响范围外的参考点。
- 网格与边界：PDF file page 6–8 Section III A–B、Tables I–II、Figs. 2–4；六个 ED/HB 工况的入口、出口、参考点和 DFC 插入层逐项对应。
- 空域压力：PDF file page 9–11 Section III C、Figs. 5–7、Eq. (12)。ED1 在 x/H=5 的压力标准差约为动压 50%，ED5 约 17%；IMC/DFC 在 x/H>2.5 后迅速衰减。Fig. 5 的纵轴是 UB0/UB(t)。
- NMAE：PDF file page 9 Eqs. (13)–(14)，分母是试验统计量极差；不是逐点相对误差均值。TKE 与湍流发展见 PDF file page 11–15 Section III D。
- 建筑风压：PDF file page 16–18 Section IV C、Figs. 15–19；PDF file page 19–21 Figs. 20–23。HB1 压力标准差的全表面 NMAE 约 108%；HB2–HB6 依次为 11.6%、10.8%、11.8%、15.0%、16.3%。
- 峰值采用基于矩的 Hermite 模型：PDF file page 17，不能读成直接取最后 8 s 时程的极值。
- 整体荷载：PDF file page 16 Fig. 14；PDF file page 20–21 Eqs. (15)–(16)、Tables IV–V；PDF file page 22 Fig. 24 与结论。对称结构积分可抵消人工压力，不能证明局部风压准确。
- 微信图：Fig. 1 / PDF file page 4；Fig. 7 / PDF file page 11；Fig. 11 / PDF file page 13；Fig. 23 / PDF file page 21；Fig. 24 / PDF file page 22。现有素材中 Fig. 7(b) 与 Fig. 23(c) 位于下方，非右侧。

## 当前事实修正与完整度

### 2026-10-05 当前全文审校与覆盖结论

- 已对 24/24 页原文完成全文阅读；本轮对现存 PDF 重新校验哈希、逐页提取，并重开公式、数字、作者单位、图注及段落合并的原页核验当前文本。覆盖判定依据当前源文及当前文件，未沿用旧内容指纹。
- RTD：`full_paper_coverage=true`，指指南规定保留的科学正文完整性；不等同于标准构建/手机预览/发布通过，也不替作者决定原文冲突数字。
- 微信：摘要、选用 NMAE 公式、五张图、定量结果及适用边界独立审校，维持短导读，不用于生成 RTD。

### 原文到 RTD 的覆盖

- PDF file page 2 的身份、七位作者及单位编号映射、日期、摘要、通讯说明均在；没有编造关键词/符号表。PDF file page 1 的平台推荐内容不属正文。
- I 引言（PDF file page 2–3）：完整 ITG/SRFM 谱系、四类 RAPF、VBIC 网格限制、综述引用和结构说明均在；恢复被拆开的 RFG 与 RAPF 原文自然段。
- II A–D（PDF file page 3–5）：CDRFG、IMC、DFC、LPC 的定义、公式、系数勘误、插入层实施及压力边界条件全部对应。
- III A–D（PDF file page 5–15）：目标统计、网格/边界、六个 ED 工况、压力、NMAE、速度/湍强/TKE/频谱完整；原目标特性、初始 TI/TKE、频谱发展等被图表拆开的自然段已重新合并。
- IV A–D（PDF file page 15–21）：建筑设置、求解时间、均值/STD/Hermite 峰值、整体荷载全在；风压及整体荷载分析中被图表隔断的原自然段已合并。
- V（PDF file page 20、22）：三段结论完整；原文无附录。
- Fig. 1–24 全部存在，中文主图题、分图、关键坐标/图例说明均有。源页：PDF file page 4（1）、6（2）、7（3）、8（4）、9（5）、10（6）、11（7–8）、12（9）、13（10–11）、14（12）、15（13）、16（14–15）、17（16–17）、18（18–19）、19（20–21）、20（22）、21（23）、22（24）。
- Table I–V 全部为中文可编辑表，源页为 PDF file page 6、8、16、21（IV–V）。Table IV 的负号（试验 CMz、HB4 CFy/CMy、HB5 CMz）按源页图像核对。
- Eq. (1)–(16) 全部保留；源页：PDF file page 4 为 (1)–(9)，PDF file page 5 为 (10)–(11)，PDF file page 9 为 (12)–(14)，PDF file page 20 为 (15)–(16)；Table I 三个 von Kármán 谱亦完整。
- [1]–[64] 参考文献来自 PDF file page 23–24，正文引用链保留；无附录遗漏。
- 封面紧跟微信短版链接；结论直接进入参考文献；规定排除的致谢、贡献/利益声明与数据可用性未混入；稳定锚点/完整引用保留。

### 已核验修正与源文差异记录

1. 标题加入论文精解；作者单位映射补为 Chen1、Li1/2、Jinghan1、Xin1、Xiangjie3、Hu1/2/4、Xiaolu5（PDF file page 2）。
2. bulk velocity 改为面积分定义的截面平均速度；Fig. 5 纵轴恢复 UB0/UB(t)；Fig. 14 Mx/My 按原文顺风/横风弯矩方向约定，不按下标臆定旋转轴。
3. 5.30%−3.05%=2.25 与 15.0%−10.8%=4.2 改写为百分点，避免与相对增幅混淆。
4. PDF file page 13 Section III D 对 ED6、x/H=5 的 TKE NMAE 报 23.4%；PDF file page 17 Section IV C 报 21.6%。两处均保留，并在正文明确矛盾。微信未采用该冲突数字。
5. 原文 PDF file page 13 引用 Fig. 11(b)–(c)，讨论却包含位于 (d) 的竖向 TI；保留原引用并邻句指出差异。原文 HD6/HD2–HD4 与工况表 HB6/HB2–HB4 的不一致也明确记录。
6. 书目排印整理明确公开：[8] 按源图恢复 π-shaped；[53] 原末尾“LES, flow”的冗余 flow 被删；[63] 原印“Win T Erstein”整理为 Winterstein；[13] 期刊标点及 [52] 会议格式统一。未新增文献或不可检索的译名。
7. 微信将“系数幅值为动压百分比”改为压力标准差/动压；说明 NMAE 极差归一化、LPC 边界与参考点、Hermite 峰值估计；Fig. 7/23 的实际上下读图方向已纠正。

剩余项：原文 23.4%/21.6% 需作者原始结果确认；公众号后台手机预览及草稿同步不在本轮完成范围内。当前规定保留的正文、图表、公式、参考文献未发现遗漏。


### 2026-10-06 页面内联语法复核

- 对照最终生成 HTML 检查内联引用与公式，修正全角括号旁的 RST 角色边界，避免引用或公式源码以普通文字显示；所有公式及引用角色内部文本保持不变。
- 新增实际 Sphinx 渲染回归，覆盖当前全部已核验全文页面，并检查页面可见文本中不存在字面 :ref: 或 :math: 残留；参考文献链接目标保持有效。
