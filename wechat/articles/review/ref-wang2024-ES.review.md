---
publication_ref: ref-wang2024-ES
doi: 10.1016/j.engstruct.2024.118742
wechat_status: awaiting_review
wechat_author: Wang Jinghan
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
wechat_cover_image: wechat/assets/public-safe/ref-wang2024-ES/cover-wechat-900x383-imagegen-v1.png
rtd_cover_image: wechat/assets/public-safe/ref-wang2024-ES/cover-wechat-900x383-imagegen-v1.png
---

# ref-wang2024-ES 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-wang2024-ES.md`
- RTD正文: `docs/source/paper-notes/ref-wang2024-ES.rst`
- 封面素材: `wechat/assets/public-safe/ref-wang2024-ES/cover-wechat-900x383-imagegen-v1.png`
- 论文图 3 CWR 方法获得指定湍流大气边界层风场的示意图: `wechat/assets/public-safe/ref-wang2024-ES/fig-03-cwr-schematic.jpg`
- 论文图 13 不同粗糙地形下湍流大气边界层风场的瞬时涡量: `wechat/assets/public-safe/ref-wang2024-ES/fig-13-rough-terrain-vorticity.jpg`
- 论文图 19 建筑周围平均风场和流动结构: `wechat/assets/public-safe/ref-wang2024-ES/fig-19-building-flow-structures.jpg`
- 论文图 21 建筑表面风压系数云图: `wechat/assets/public-safe/ref-wang2024-ES/fig-21-wind-pressure-contours.jpg`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.engstruct.2024.118742
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 22；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `784571951eef0b9c0106c9a519fc8356e400b5aafa4f7d9ea57342e8c2ba4405`

## 关键事实证据定位记录

- 摘要与作者：PDF file page 1；Chao Li、Shengtao Zhou均为通讯作者。
- 预设均值、仅纵向脉动反馈：PDF file page 9式（15）–（16）、PDF file page 10解释；倍率为1+λ，λ不是完整倍率。
- 比例控制公式：PDF file page 13式（20）；|1+λ|≤2.5限制：PDF file page 12 Section 3.1；镜像重引入：PDF file page 13。
- −80及整体MARE低于10%：PDF file page 15 Section 3.3.1，限本文城市地形参数研究。
- 三地形RS均值MARE＝3.28/4.07/5.45%，纵向TI MARE＝6.16/8.47/7.41%：PDF file page 18 Section 4.2。
- 建筑为1:400缩尺、深宽高1:1:4孤立高层：PDF file page 19 Section 5；TPU来流RS/TP纵向TI MARE＝12.39/15.68%，均值MARE＝4.77/5.34%，谱匹配主要低于20 Hz：PDF file page 20 Section 5.2。
- 风压20%/30%指脉动风压系数：PDF file page 20式（26）及Section 5.4、PDF file page 18 Fig.20；未控制相干性和近地面SECD问题：PDF file pages 20–21。
- Fig.21上八幅TPU、下八幅LES，左侧均值、右侧脉动系数；图文对应正确。

### 当前选图与公式

- 原Fig.3：PDF file page 4；已重新比对现有公开素材、原图及中文说明。
- 原Fig.13：PDF file page 12；已重新比对现有公开素材、原图及中文说明。
- 原Fig.19：PDF file page 17；已重新比对现有公开素材、原图及中文说明。
- 原Fig.21：PDF file page 19；已重新比对现有公开素材、原图及中文说明。

- 原式（15）：PDF file page 9；当前使用的符号、符号方向与条件已核对。
- 原式（20）：PDF file page 13；当前使用的符号、符号方向与条件已核对。

## 当前事实修正与完整度

### 2026-10-05 重建审计结果

### 阅读范围与当前复核

- PDF file pages 1–4：摘要、引言和WR背景；4–10：WR/CWR、PID、SECD；11：风谱图；12–17：调参与验证；18–19：三地形；19–20：建筑风压；20–21：结论；21–22：参考文献。无附录。
- 本次重建以已完成逐页全文阅读的保留结论为起点，重新抽取现存全文、计算PDF校验值，并重新回查上述证据页、现有选图和公式。没有复用已丢失文件的旧指纹或旧验收状态。
- 图像核对范围是现有导读采用的原图及相关量化证据，不宣称所有原图逐一完成全文译制；微信后台手机预览未执行。

### RTD独立事实修正

1. 补Zhou Shengtao通讯星号，包括RTD完整引用，作者顺序不变。
2. 明确预设均值与SECD作用、仅纵向TI直接反馈，增加误差容限而非严格对齐措辞。
3. 保留原式（20），补1+λ实际倍率、限幅和镜像重引入，防止控制律误读。
4. −80及10%限定为论文参数案例；补建筑验证12.39%/15.68%和20 Hz范围，避免把前述10%套到所有应用。
5. 明确1:400、1:1:4建筑算例，保留侧面脉动风压最大30%的负面结果。

### 公众号独立事实核对

- 公众号源稿直接对照原论文摘要、方法、结果、图题、公式及限制，逐项执行与上述问题对应的修正；未由RTD转换生成，也未用公众号覆盖RTD。
- 忠实中文摘要保留原论文报告值；需要限定的统计单位、样本、网格、频率或适用条件在正文中明确。原文内部冲突不擅自统一。

### 原文疑点

- PDF file page 8 Table 5乡村/郊区SECD系数为0.35/0.65 m⁻¹，PDF file page 9式（19）后正文为0.4/0.7 m⁻¹；保留冲突，不擅选实现参数。
- PDF file page 19 Q定义印刷为旋转与应变张量平方之和，与旋转优势解释不一致；导读不重抄该定义，不改原图标签。
- PDF file page 17精细网格叙述写UC4，而Table 4/Fig.9为UC5；不复制可疑工况关联。
- PDF file page 20统计窗先写1–11 s，Section 5.4又写1–10 s；当前导读不把其中一个时间窗写成新的确定值。
- PDF file page 9式（17）阻尼函数符号与抑制自由流脉动的文字含义需进一步澄清；旧WR背景式（8）混合权重亦需作者校对，未据此改动CWR式（20）。

### 忠实度与完整度分别判定

- 现有导读文本事实及所用图/公式已重新对照并修正；原文疑点按页定位保留，图像后台可读性仍需预览。
- RTD仍为历史选择性导读，尚缺完整1–6节、21幅图、6张表、式（1）–（26）和78条参考文献；全文完整度为false，仍需按原文顺序扩写，不能因事实审计通过改称全文精解完成。
- 当前本地修訂未自动更新微信后台；无新增上传、发布、提交或推送。历史转换、预览及检查日志不能充当当前构建结果。
