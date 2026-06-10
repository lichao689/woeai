# ref-zhao2025-SCS 封面简报

## 文章标题

数值风洞 | 用 3D Gaussian Splatting 重建城市建筑几何

## 视觉目标

封面应表达“从城市影像和 3DGS 点云到 CFD 可用建筑几何”的技术路线。不要直接使用论文正文图作为封面，不嵌入文字、logo、合作方名称或未经确认的具体地名。画面主体保持在中间区域，适配微信公众号首图 `900 x 383 px` 及可能的方形裁切。

## 候选概念 1: 城市街区与风场叠加

- 核心画面: 一个抽象化城市街区，白色或浅灰建筑群从鸟瞰角度展开，透明蓝绿色风场流线和速度等值面穿过街巷。
- 设计重点: 让读者第一眼看到“城市建筑几何 + 风场模拟”。
- 生成提示词方向: aerial view of a dense urban block, clean white building massing, translucent blue-green wind-flow simulation overlay, subtle CFD contour field, realistic but not tied to a named place, academic engineering visualization, no text, no logo.
- 风险控制: 不使用真实可识别城市地标；避免过度科幻化的霓虹风格；不要生成中文或英文文字。

## 候选概念 2: 高斯点云变成建筑几何

- 核心画面: 左侧是由彩色 Gaussian 点云和半透明椭球组成的建筑轮廓，向右逐步过渡为规则的白色 LoD 建筑几何模型。
- 设计重点: 突出 3D Gaussian Splatting 从视觉重建走向 CFD 几何前处理的“方法感”。
- 生成提示词方向: 3D Gaussian Splatting point cloud of urban buildings transforming into clean simulation-ready building geometry, colored translucent ellipsoids on the left, precise white LoD building model on the right, neutral background, engineering research cover, no text, no logo.
- 风险控制: 点云不要像娱乐特效；建筑几何需要规则、干净、可计算；避免出现无法解释的机械结构。

## 候选概念 3: 从视觉数据到仿真模型

- 核心画面: 中心是一条清晰的视觉流程：无人机影像纹理、点云、建筑几何、风场结果四个元素在同一画面中从左到右连接，但不使用文字标签。
- 设计重点: 表达本文的工程影响，即把视觉数据更快转化为城市风模拟可用模型。
- 生成提示词方向: cinematic but clean engineering workflow, drone imagery tiles becoming point cloud, point cloud becoming simplified urban building geometry, geometry surrounded by blue-green CFD wind contours, centered composition for WeChat cover crop, no embedded text, no logos, no named city.
- 风险控制: 不出现品牌化无人机或平台界面；流程符号保持简洁，不做复杂小字说明。

## 推荐

优先尝试候选概念 2，因为它最能区别于一般“城市风场”封面，并且直接对应本文的 3D Gaussian Splatting 方法贡献。若生成图在小尺寸下点云过碎，可退回候选概念 1，以更稳定的城市风场叠加画面保证封面可读性。
