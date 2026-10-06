---
publication_ref: ref-li2024-POF
doi: 10.1063/5.0194006
wechat_status: awaiting_review
wechat_author: Li Chao
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
wechat_cover_image: wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png
rtd_cover_image: wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png
---

# ref-li2024-POF 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-li2024-POF.md`
- RTD正文: `docs/source/paper-notes/ref-li2024-POF.rst`
- 封面素材: `wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png`
- 论文图 3 VPRFG 方法流程图: `wechat/assets/public-safe/ref-li2024-POF/fig3-vprfg-flowchart.png`
- 论文图 4 以 von Karman 能谱为目标生成湍流的能谱: `wechat/assets/public-safe/ref-li2024-POF/fig4-von-karman-energy-spectrum.jpg`
- 论文图 7 初始时刻不同网格的 Q 准则等值面: `wechat/assets/public-safe/ref-li2024-POF/fig7-q-criterion-isosurfaces.jpg`
- 论文图 9 衰减盒湍流能谱: `wechat/assets/public-safe/ref-li2024-POF/fig9-decaying-box-energy-spectra.jpg`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1063/5.0194006
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 15；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `855a45aad06339d34c5f411f2a075eb1b8bf1acc903dccfb695ca273bdbe05c3`
- 当前核验副本与历史原始副本的字节等价性未建立；不混同两者哈希

## 关键事实证据定位记录

- 题名、DOI及通讯作者Chen Lingwei：PDF file pages 1–2；中文摘要对应PDF file page 2。
- 矢量势、旋度及分量式：PDF file page 5式（15）–（18）；现有两组构造公式符号与原图一致。
- 频率必须与正号相位配套取负号：PDF file page 6式（25）；同页式（27）、（29）确认连续无散和t−τ/x+Uτ方向。
- 谱与湍动能：PDF file page 8式（47）–（48）；谱限在PDF file pages 8–9式（49）–（51），有限域和网格有截谱。
- von Karman验证：PDF file page 9 Section III.A，128³/256³/384³；盒湍流：PDF file pages 9–10 Section III.B，0.2π m域、128³/256³、CBC时刻42/98/171。
- C1/C3采用式（17），C2/C4采用式（18）：PDF file page 10 Table I；面通量与单元速度散度不同：PDF file page 11 Table II及正文。
- C4初始能量偏高、离散式改变初始统计：PDF file pages 11–13、Figs.7–11；空间相关参考由目标谱及式（5）、（8）推算。
- 图7当前素材缺原子图标签：图注已补左上C1、右上C2、左下C3、右下C4，上排128³/Q=500，下排256³/Q=2000，不能把全部视觉差异仅归因于网格。
- 当前仅HIT，未解决任意非均匀各向异性CSD构造：PDF file pages 13–14。

### 当前选图与公式

- 原Fig.3：PDF file page 8；已重新比对现有公开素材、原图及中文说明。
- 原Fig.4：PDF file page 9；已重新比对现有公开素材、原图及中文说明。
- 原Fig.7：PDF file page 12；已重新比对现有公开素材、原图及中文说明。
- 原Fig.9：PDF file page 13；已重新比对现有公开素材、原图及中文说明。

- 原式（15）：PDF file page 5；当前使用的符号、符号方向与条件已核对。
- 原式（16）：PDF file page 5；当前使用的符号、符号方向与条件已核对。
- 原式（25）：PDF file page 6；当前使用的符号、符号方向与条件已核对。
- 原式（27）：PDF file page 6；当前使用的符号、符号方向与条件已核对。
- 原式（29）：PDF file page 6；当前使用的符号、符号方向与条件已核对。
- 原式（47）：PDF file page 8；当前使用的符号、符号方向与条件已核对。
- 原式（48）：PDF file page 8；当前使用的符号、符号方向与条件已核对。

## 当前事实修正与完整度

### 2026-10-05 重建审计结果

### 阅读范围与当前复核

- PDF file page 1：出版封面；2–4：摘要、引言与HIT统计；5–9：构造、无散/Taylor证明、统计推导与算法；9–13：验证；11–14：结论及边界；14–15：参考文献。无附录。
- 本次重建以已完成逐页全文阅读的保留结论为起点，重新抽取现存全文、计算PDF校验值，并重新回查上述证据页、现有选图和公式。没有复用已丢失文件的旧指纹或旧验收状态。
- 图像核对范围是现有导读采用的原图及相关量化证据，不宣称所有原图逐一完成全文译制；微信后台手机预览未执行。

### RTD独立事实修正

1. 收紧“天然无散”为连续数学构造，区分单元中心离散速度散度与面通量守恒；补均匀无散平均速度条件。
2. 重新核对六组展示公式，并补原式（25）的频率负号；保留原Taylor平移方向。
3. 补有限域/网格/时间步截谱边界，统计量必须相容，不能彼此独立任意指定。
4. 明示式（18）C2/C4初始统计偏离和C4能量过高，避免所有工况均准确的泛化。
5. 对图7缺失子图标签用正文图注补全工况、网格、Q阈值；说明空间相关参照由参考谱推得。

### 公众号独立事实核对

- 公众号源稿直接对照原论文摘要、方法、结果、图题、公式及限制，逐项执行与上述问题对应的修正；未由RTD转换生成，也未用公众号覆盖RTD。
- 忠实中文摘要保留原论文报告值；需要限定的统计单位、样本、网格、频率或适用条件在正文中明确。原文内部冲突不擅自统一。

### 原文疑点

- 当前PDF下载哈希不同于历史原始源哈希。题名、作者、DOI、正文公式与所选图匹配，事实审计可基于当前获准PDF；未取得历史原始字节，不能确认字节或全部页像素等价，亦不猜测差异原因。
- PDF file page 11将衰减描述为exponentially，但式（56）为关于移位无量纲时间的幂律；导读未照搬“指数衰减”。
- 原文“严格零散度”在Table II实际为浮点量级而非数学零，导读明确连续/离散区别。

### 忠实度与完整度分别判定

- 现有导读文本事实及所用图/公式已重新对照并修正；原文疑点按页定位保留，图像后台可读性仍需预览。
- RTD仍为历史选择性导读，尚缺完整I–IV节、57个编号公式、11幅图、2张表和60条参考文献；全文完整度为false，仍需按原文顺序扩写，不能因事实审计通过改称全文精解完成。
- 当前本地修訂未自动更新微信后台；无新增上传、发布、提交或推送。历史转换、预览及检查日志不能充当当前构建结果。
