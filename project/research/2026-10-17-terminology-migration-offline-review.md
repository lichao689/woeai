> 后续状态更新：13篇既有草稿分类同步已完成，另31篇已官方回查未变；见[实际同步记录](2026-10-17-family13-classification-sync.md)。下文保留离线复核时点的缺口与未同步描述，不再作为当前阻塞。

# WOEAI 一级方向命名迁移：44篇离线复核结果

本次离线命名迁移复核已完成。仅在隔离预览修改，未写原工作区、未提交/推送/上线、未调用公众号后台。

## 已完成的本地复核

- 44篇均通过注册表一级/二级映射、现行结构和二级方向H1检查。
- 31篇文章文件逐字节未变；13篇分类行从“海上漂浮风电”改为“海洋能源结构”，原二级方向不变。其中ref-zheng2025-QHDXXB另精确保留main已批准的“一体化分析 | ”标题前缀修复。科学正文、摘要、数字、公式、图注、作者及链接未改变。
- 共享writing-standards仅3处一级名称替换；natural-scientific-writing字节未变；封面规范仅1处名称替换。既有科学与来源审查通过正文、来源对象、review及全部素材的字节等价复用，没有重新声称PDF审计。
- 44篇academic-clean/MathJax SVG离线生成成功：561个不同公式输入，共794处SVG、177处正文图。前后HTML只在精确分类行变化；H1按既有投递规则不重复渲染进正文。
- 浏览器逐篇检查44篇正文与44张既有封面，图像/SVG无加载错误；13篇分类行前后几何相同，44篇没有新增几何或溢出回归。6篇原有DOI等内容引起1–9px的小范围滚动仍保留，未修改渲染器来掩盖它。
- 官方离线preflight：36篇通过，8篇在已有正文图上传许可门禁处停止；没有补造许可或绕过门禁。
- 262项Python测试通过（1项可选环境检查跳过）；11项前端/公式测试通过；公开安全、注册表/派生视图与严格Sphinx构建通过。

## main标题修复兼容

只读取得公开提交[f88f3fa](https://github.com/lichao689/woeai/commit/f88f3faea879b81ee68b9d3539ecd6dbac44ec21)，其直接父提交为本预览基线3730fa1。五个文件在隔离区局部兼容：review-checklist、check-wechat-content、test_wechat_editorial、editorial模块及QHDXXB标题行。四个规则/测试文件与该提交精确相同；QHDXXB文件只额外保留本次新一级分类。未覆盖原工作区，旧标题检查不会回归。

## 证据记录方式

44篇分别新增`wechat/articles/review/<ref>.terminology-20261017.review.md`，注册表新增`evidence.terminology_review_20261017`和`terminology_migration.status=local_review_complete`。新作用域指纹实际核对为当前值；所有旧stage、checks、旧指纹、旧review与草稿回执完整保留。没有自动重哈希旧审批，没有新增verified/ready_to_publish/published声明；渠道总状态仍按保守的awaiting_review保留，不能据此误读为此次命名等价核对未做。

用户已确认完成的人工验收按原适用范围保留，本次不重复要求、不把历史false字段升级成新的单篇验收声明，也不将其列为命名迁移阻塞。源身份对象未改，17篇既有RTD verified证据仍有效。9组旧时间冲突、13篇历史原件与当前审查副本不等价的既有记录均保留，不借此次改名清账。

## 后续是否只剩同步/发布授权

本轮新增的本地内容、映射、标题、等价和渲染复核已完成。31篇文章投递内容未变，不需要因本轮命名更改重传。

13篇实际正文分类变化需要以后按授权同步到准确的既有草稿。当前仍有明确的投递前事项，不能说只剩“发布授权”：

- 9篇缺可用既有草稿映射：`ref-zheng2025-QHDXXB`、`ref-zheng2023-MS`、`ref-zheng2023-JRSE`、`ref-zhou2021-OE`、`ref-zhou2020-RE`、`ref-li2018-AE`、`ref-zhou2017-E`、`ref-li2017-AS`、`ref-li2013-RE`。不得把preflight计划显示create理解为允许新建替代草稿。
- 本轮13篇中的上传许可缺口只有`ref-zheng2023-MS`；该篇亦在上述9篇内。其余12篇preflight已通过。
- 全44篇中原有的8篇上传许可缺口：`ref-tang2024-POF`、`ref-he2024-JBE`、`ref-zhao2023-BS`、`ref-zheng2023-MS`、`ref-zhang2023-S`、`ref-zhang2023-ES`、`ref-yang2022-AS`、`ref-li2010-WAS`。除上述1篇外，其余7篇文章未变，本轮不需投递，因此不是命名迁移的新增阻塞。
- 所有后台同步、目标核实和后续发布仍未执行；本阶段没有读取凭据。发布是之后独立决定，并非当前必须执行的步骤。

## 逐篇结果

|论文ref|文章变化|本地复核|preflight|本轮需后台同步|
|---|---|---|---|---|
|ref-zhao2026-BE|字节未变|完成|通过|否|
|ref-he2026-OE|字节未变|完成|通过|否|
|ref-zhao2026-BS|字节未变|完成|通过|否|
|ref-he2026-OE-structural|分类元数据|完成|通过|是|
|ref-tang2026-RE|字节未变|完成|通过|否|
|ref-he2025-POF|字节未变|完成|通过|否|
|ref-yang2025-JBE|字节未变|完成|通过|否|
|ref-zheng2025-OE|分类元数据|完成|通过|是|
|ref-zheng2025-QHDXXB|分类元数据＋main既有H1修复|完成|通过|是|
|ref-tang2025-JBE|字节未变|完成|通过|否|
|ref-zhao2025-SCS|字节未变|完成|通过|否|
|ref-chen2024-POF|字节未变|完成|通过|否|
|ref-tang2024-POF|字节未变|完成|既有上传许可缺口|否|
|ref-wang2024-ES|字节未变|完成|通过|否|
|ref-he2024-JBE|字节未变|完成|既有上传许可缺口|否|
|ref-li2024-POF|字节未变|完成|通过|否|
|ref-chen2024-JCP|字节未变|完成|通过|否|
|ref-zhou2023-AE|分类元数据|完成|通过|是|
|ref-zhao2023-BS|字节未变|完成|既有上传许可缺口|否|
|ref-zheng2023-MS|分类元数据|完成|既有上传许可缺口|是|
|ref-zhang2023-S|字节未变|完成|既有上传许可缺口|否|
|ref-wang2023-JWEIA|字节未变|完成|通过|否|
|ref-zheng2023-JRSE|分类元数据|完成|通过|是|
|ref-zhang2023-ES|字节未变|完成|既有上传许可缺口|否|
|ref-feng2023-HKXYGC|字节未变|完成|通过|否|
|ref-zhao2023-GYJZ|字节未变|完成|通过|否|
|ref-chen2022-JWEIA|字节未变|完成|通过|否|
|ref-li2022-SOS|分类元数据|完成|通过|是|
|ref-yang2022-AS|字节未变|完成|既有上传许可缺口|否|
|ref-zhao2021-EFM|字节未变|完成|通过|否|
|ref-zhao2021-AR|字节未变|完成|通过|否|
|ref-zhou2021-OE|分类元数据|完成|通过|是|
|ref-zhao2021-TYNXB|字节未变|完成|通过|否|
|ref-li2020-JWEIA|字节未变|完成|通过|否|
|ref-zhou2020-RE|分类元数据|完成|通过|是|
|ref-li2018-AE|分类元数据|完成|通过|是|
|ref-xiao2018-KXJSYGC|字节未变|完成|通过|否|
|ref-zhou2017-E|分类元数据|完成|通过|是|
|ref-li2017-BS|字节未变|完成|通过|否|
|ref-li2017-AS|分类元数据|完成|通过|是|
|ref-li2013-RE|分类元数据|完成|通过|是|
|ref-li2012-JWEIA|字节未变|完成|通过|否|
|ref-li2012-GCLX|字节未变|完成|通过|否|
|ref-li2010-WAS|字节未变|完成|既有上传许可缺口|否|

证据包包含44篇独立review、当前阶段指纹清单、规格等价、f88兼容、逐篇结果、浏览器/几何结果及完整性报告。没有私有PDF、凭据或后台ID。
