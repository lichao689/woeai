# ref-tang2025-JBE 封面简报

## 文章标题

结构抗风 | 用图神经网络预测高层建筑结构响应

## 视觉目标

封面应表达“高层建筑结构图 + 风荷载响应 + GNN 代理模型”的技术路线。不要直接使用论文正文图作为封面，不嵌入文字、logo、合作方名称、真实可识别建筑或未经确认的工程项目身份。画面主体保持在中间区域，适配微信公众号首图 `900 x 383 px` 及可能的方形裁切。

## 候选概念 1: 高层结构受风与响应曲线

- 核心画面: 中央是一栋抽象化高层结构框架，左右两侧有风场流线和响应曲线，楼层节点以微亮点提示结构响应采样位置。
- 设计重点: 让读者第一眼看到“高层建筑抗风响应预测”，而不是泛泛的 AI 图形。
- 生成提示词方向: abstract tall building structural frame under wind-flow curves, subtle response traces along floors, clean academic engineering visualization, cool blue and teal palette, centered composition for WeChat cover crop, no text, no logo, no real landmark.
- 风险控制: 不出现真实工程项目、具体城市天际线或合作方标识；风线和响应线保持简洁，避免过度科幻化。

## 候选概念 2: 图神经网络节点映射到高层建筑

- 核心画面: 高层建筑框架上叠加节点和边，右侧或背景中出现抽象图网络，表现节点、边、楼层和构件关系如何进入 GNN。
- 设计重点: 突出本文的方法贡献，即把高层建筑结构组织成图数据并用于 TBGNN 预测。
- 生成提示词方向: graph neural network nodes and edges mapped onto a tall building structural frame, floor-level nodes glowing softly, engineering research cover, precise structural lines, blue teal with small warm accents, no embedded text, no logo.
- 风险控制: 图网络不要像通用科技背景；节点和边应与楼层结构有关系；不要生成公式文字或乱码标签。

## 候选概念 3: 快速结构响应筛选

- 核心画面: 中央高层结构一侧是有限元式框架，另一侧是简化的预测曲线和图网络，暗示从重复有限元分析走向快速代理模型筛选。
- 设计重点: 表达工程影响，即在多轮构件尺寸探索中快速筛选结构响应，但不暗示已经替代所有工程复核。
- 生成提示词方向: clean engineering concept image showing a tall building structural frame, simplified response curves, graph surrogate model visualization, rapid screening for wind-resistant design, centered composition, no text, no logos, no commercial software interface.
- 风险控制: 不出现商业软件界面、性能数字或“自动设计”字样；避免夸大为完整生产部署。

## 当前状态

- 最终封面: `wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v2.png`
- 生成方式: image-gen public-safe candidate selected after upgraded batch `wechat-cover` comparison
- 本地裁剪预览: `wechat/.local/cover-previews/batch-2026-06-10-v2-quality-board.html`
- 预览结果: local ratio, file-size, small-thumbnail, crop-safety, and text-quality checks passed (`900 x 383 px`, ratio delta `0.0`)
- 微信后台预览: pending

## 推荐

已采用 v2 封面。它保留候选概念 2 的核心：高层建筑结构图、楼层节点和 GNN 信息传递，并加入受风响应曲线；短文字为“结构抗风 / 高层响应快速预测”。这版比原无文字封面更适合公众号列表和分享缩略图。
