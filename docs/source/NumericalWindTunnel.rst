数值风洞 Numerical Wind Tunnel
==============================

数值风洞方向关注大气边界层湍流、城市风环境、复杂地形风场和工程结构风效应模拟。目标是在可追溯的数值模型中生成合理的入流、边界层和局部风场，为结构抗风、城市风环境评估和工程咨询提供基础。

湍流风场生成 Turbulent Inflow
-----------------------------

团队围绕大气边界层湍流生成、散度自由速度场合成和大涡模拟入口条件开展方法研究。相关论文包括：

- :ref:`A novel vector potential random flow generation method <ref-li2024-POF>`，用于合成满足散度自由约束的均匀各向同性湍流；
- :ref:`A coherence-improved and mass-balanced inflow turbulence generation method <ref-chen2024-JCP>`，用于大涡模拟中的入口湍流生成；
- :ref:`A new controllable weak recycling inflow turbulence generator <ref-wang2024-ES>`，用于建筑风效应评估中的 LES 入流。

城市风环境 Urban Wind Environment
---------------------------------

城市风环境研究关注建筑几何、城市尺度风场和台风天气条件下的多尺度模拟。AI 方法被用于降低建模门槛、提升风场重建和仿真效率。

相关证据包括：

- :ref:`Precomputed CFD database framework for urban microscale wind prediction <ref-zhao2026-BS>`，面向城市微尺度风环境快速预测；
- :ref:`Satellite-imagery urban geometry reconstruction framework <ref-zhao2026-BE>`，面向城市风环境评估中的建筑几何快速重建；
- :ref:`Temporal super-resolution of wind in urban energy applications <ref-tang2026-RE>`，面向城市风场时间超分辨率重建；
- :ref:`3D Gaussian Splatting building geometry framework <ref-zhao2025-SCS>`，面向城市风模拟中的建筑几何构建。

复杂地形 Complex Terrain
------------------------

复杂地形风场研究关注地形、边界层和局部风环境之间的尺度连接，可服务输电线路、城市片区和能源设施等工程场景。

相关项目实践 Related Projects
--------------------------------

- 数值大气湍流边界层生成方法的改进与验证；
- 基于粗糙壁面修正的平衡大气边界层紊流风场大涡模拟研究；
- 三维自平衡紊流边界层风场的大涡模拟研究；
- 微地形下输电线路微尺度台风风场特性及模型研究；
- 再生能源发电厂风洞试验及风振分析。

完整项目记录见 :ref:`projects-numerical-wind-tunnel`。

与其他方向的连接
----------------

数值风洞方法为 :doc:`WindResistance` 提供风荷载和响应分析基础，也为 :doc:`OffshoreWindEnergy` 中浮式风机系统风浪作用研究提供环境输入。
