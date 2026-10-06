---
publication_ref: ref-chen2022-JWEIA
doi: 10.1016/j.jweia.2022.105147
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
wechat_cover_image: wechat/assets/public-safe/ref-chen2022-JWEIA/cover-wechat-900x383-imagegen-v2-selected.png
rtd_cover_image: wechat/assets/public-safe/ref-chen2022-JWEIA/cover-wechat-900x383-imagegen-v2-selected.png
---

# ref-chen2022-JWEIA 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-chen2022-JWEIA.md`
- RTD正文: `docs/source/paper-notes/ref-chen2022-JWEIA.rst`
- 封面素材: `wechat/assets/public-safe/ref-chen2022-JWEIA/cover-wechat-900x383-imagegen-v2-selected.png`
- 论文图 2 CIRFG 方法流程图: `wechat/assets/public-safe/ref-chen2022-JWEIA/fig02-cirfg-flowchart.png`
- 论文图 9 Y 方向空间相关系数对比: `wechat/assets/public-safe/ref-chen2022-JWEIA/fig09-spatial-correlation-y.png`
- 论文图 11 不同速度分量之间互相关系数对比: `wechat/assets/public-safe/ref-chen2022-JWEIA/fig11-cross-correlation-components.png`
- 论文图 17 X 方向湍流强度剖面发展: `wechat/assets/public-safe/ref-chen2022-JWEIA/fig17-turbulence-intensity-x-development.png`
- 论文图 20 建筑表面平均风压系数分布等值图: `wechat/assets/public-safe/ref-chen2022-JWEIA/fig20-mean-pressure-contours.png`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.jweia.2022.105147
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 24；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `78d8978e6af583567ab92d71d5e968c245c72e6e12052ea17470d2791ff61342`

## 关键事实证据定位记录

- 身份与摘要：PDF file page 1；题名、七名作者、期刊、年份和 DOI 与公开论文条目及两渠道相符。
- 方法目标：PDF file page 4 Section 3.1；互相关可解条件：PDF file page 5 Eq. (9)–(16)、Table 1。Eq. (15) 还依赖随机符号期望等于尺度因子及 N→∞。
- 直接施加 u 分量 Y 向相关：PDF file page 6–7 Section 3.2.3、Eq. (23)–(30)；v/w 分量和 Z 向未独立显式施加的边界见 PDF file page 9–10 Section 4.2.2。
- 均匀湍流无散度与非均匀 ABL 的近似：PDF file page 4、7–8，Sections 3.1、3.2.4。入口人工压力及 outflow/参考点条件见 PDF file page 14 Section 5.2.2。
- 压力单位：PDF file page 14 文字“最大不超过 1”，对应 PDF file page 16 Fig. 19 的压力轴单位 Pa；不是动压 1%。近壁压力标准差最大值小于 2 Pa。
- 荷载结果：PDF file page 19–21 Section 5.3、Tables 6–7；C2 平均 CD/CMx 误差约 6%；C5 阻力标准差误差 +7.38%；C5 五项带符号相对误差均值 −8.69%，不是平均绝对误差。
- 微信图：Fig. 2 / PDF file page 7；Fig. 9 / PDF file page 10；Fig. 11 / PDF file page 11；Fig. 17 / PDF file page 15；Fig. 20 / PDF file page 17。
- 微信公式：合成式 Eq. (2) / PDF file page 4；互相关 Eq. (15) 与 Taylor 波数 Eq. (17) / PDF file page 5。公式及限制直接对照 PDF，不以 RTD 译文代替证据。

## 当前事实修正与完整度

### 2026-10-05 当前全文审校与覆盖结论

- 本日已完整阅读同一份 24 页原文；本轮重建重新计算 PDF 哈希、重新提取全部 24 页，并重新打开所有更正涉及的原始页核验当前改文。未复用旧交付文件的内容指纹。
- RTD：`full_paper_coverage=false`。编号对象齐全，不能掩盖正文、符号表和附录说明仍被压缩的事实。
- 微信：摘要、三个公式、五张选图、数字和适用条件已独立对照原文修正；后台显示/上传/发布未在本轮确认。

### 原文到 RTD 覆盖及剩余项

- PDF file page 1：论文身份、摘要、关键词、收稿/修回/录用/上线日期已对应；作者单位及通讯脚注仍未完整译入。已修正标题，明确为论文精解。
- PDF file page 2：符号/缩写表只保留主要条目，缺 ci、Cj、概率密度、三维谱、网格无量纲量及若干缩写，不满足全文要求。
- PDF file page 1、3–4 Sections 1–2：综述、谱定义、边界兼容性讨论及文内引用大量压缩。本轮把 Eq. (1) 移回 Section 2，补明原始 RFG/PRFG 的例外，但没有伪称已重译整段综述。
- PDF file page 4–8 Section 3：各子节和 Eq. (2)–(36) 均存在；四步推导解释及 Eq. (15)、(20)、(26) 的中间展开仍被缩写。Table 1 可解性和 N→∞ 限制已补。
- PDF file page 8–11 Section 4：基本、空间及分量互相关验证仍为概括；验证的 20 s、20000 步、0.001 s 等设置及逐分量解释未全部译入。
- PDF file page 11–13 Section 5.1：本轮补网格尺寸/层数/首层厚度、y+、边界、压力参考点、求解器/格式、时间步/后处理及 C4/C5 目标不是实测标定值的说明。
- PDF file page 13–21 Sections 5.2–5.3：主要结果在，但原文逐段分析仍有缩写。已纠正压力单位与表 7 的例外/误差统计口径。
- PDF file page 21 Section 6：现为重组五点总结，未对应原文四个自然段的逐句翻译。
- Fig. 1–24 全部存在。源页顺序：PDF file page 6（1）、7（2）、8（3–4）、9（5–7）、10（8–10）、11（11）、12（12）、13（13–14）、14（15–16）、15（17）、16（18–19）、17（20）、18（21）、19（22–23）、20（24）。部分分图标题、图中英文未完整中文转写。
- Table 1–7 以图片存在。源页：PDF file page 5、8（2–3）、14（4–5）、19、20。表内完整中文译文仍缺，不把图片存在算作译文完成。
- Eq. (1)–(39)、(A1)–(A8)、(B1)–(B3)、(C1)–(C9)、(D1)–(D6)，共 65 个编号均存在；中间推导仍有上述缺口。
- 附录 A–D：PDF file page 21–23 的全部编号式已保留，但参数解释大幅压缩。
- 参考文献：PDF file page 23–24 的 52 条都在；正文遗漏的引用链尚需恢复。
- 封面紧跟微信短链接；附录在参考文献前；规定排除的出版声明尾节未混入；稳定锚点与完整引用保留。

### 本轮重建的已核验更正与原文差异

1. PDF file page 22 Eq. (C8)：把减法 `3.7β−0.3` 改回幂函数 `3.7β^{-0.3}`。
2. PDF file page 14、16 Section 5.2.2/Fig. 19：将无证据的“动压 1%”改为 1 Pa，保留近壁标准差小于 2 Pa。
3. PDF file page 4 Eq. (6) 原印 Si×Si，而 Eq. (7) 为 Si×Sj；PDF file page 5 Eq. (18) 第二行原排频率下标 n+t；PDF file page 22 Eq. (C5) 第二行重复 qx。现保留原排式并明确指出差异，不把理论推测当作作者勘误。PDF file page 7 Eq. (32) 原印末尾 Δf 仍保留。
4. PDF file page 20 Table 7：C5 阻力标准差 +7.38% 是“全部低估”的例外；−8.69% 是五项带符号误差的均值。两个渠道均澄清。
5. PDF file page 11 正文的 H/8、H/20、H/40、H/80 与 PDF file page 13 Fig. 14 的 H/10、H/25、H/50、H/100 不同，RTD 保留两处记录。PDF file page 8 Table 3 A3 起点 0.05、终点 1.6、间距 0.1、数量 16 不完全自洽，原表未擅改。

剩余工作是实质性的逐句补译、表格/图注翻译及引用恢复；构建通过也不能关闭这些缺口。
