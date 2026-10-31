.. _en-floating-wind-integrated-analysis:

Integrated Analysis
========================================

:doc:`Marine Energy Structures <MarineEnergyStructures>` · :doc:`Research overview <Research>`

Motion and loads of a floating wind turbine depend jointly on the turbine, platform, moorings and environment. Improving one component can change the response of the whole system. Integrated analysis connects coupled dynamics, load transfer, long-term conditions, optimisation and physical comparisons to assess design trade-offs and their validation limits.

- How do platform dimensions and moorings jointly change long-term cost–fatigue trade-offs?
- Which wind–wave headings are adverse for different motions and component loads?
- What can comparisons with scaled tests establish, and what scaling or control limitations remain?

.. contents:: On this page
   :local:
   :depth: 2

.. _en-floating-wind-integrated-analysis-methods:

Methods and contributions
--------------------------------------------------

Coupled turbine–platform–mooring models, reduced-order analysis and surrogate-assisted optimisation connect long-term environments with design alternatives. Wind–wave model tests provide physical comparisons.

Evidence in practice
----------------------------------------

.. _en-story-ref-zhou2023-AE:

Long-term optimisation: cost–fatigue trade-offs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Question**　Platform dimensions and moorings jointly affect manufacturing cost and fatigue across many wind–wave combinations. Comparing one fixed design per concept can conceal the alternatives each concept offers.

**Contribution**　A reduced-order dynamic model, representative environmental sampling and a Kriging surrogate support NSGA-II searches for Pareto trade-offs among manufacturing cost, tower-base fatigue and fairlead fatigue.

**Evidence**　Response comparisons with OpenFAST assess the reduced-order model. For square and Y-shaped steel semi-submersibles, long-term conditions and platform–mooring choices alter the fronts. Square designs favour tower-base fatigue, while some Y-shaped designs have lower mooring fatigue.

**Limits**　Manufacturing cost is not life-cycle cost. This is concept screening under specific environmental, turbine, cost and design assumptions; hull strength was not checked. No single metric establishes a universally best platform.

:doc:`Read the English highlight <highlights/ref-zhou2023-AE>` · :doc:`Original figures and full reading notes (Chinese) </paper-notes/ref-zhou2023-AE>` · :ref:`Full publication record <en-ref-zhou2023-AE>`

.. _en-story-ref-zheng2023-JRSE:

1:70 wind–wave testing: heading and system response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Question**　The geometry of a Y-shaped platform and its moorings is directional. Changing wind–wave heading can change motions, tower-base loads and nacelle acceleration in different ways.

**Contribution**　A 1:70 wind-tunnel and wave-flume model represents a 10 MW reference turbine. Thrust matching and calibrated inputs support three-heading comparisons of still-water, wind-only, wave-only and combined conditions alongside OpenFAST.

**Evidence**　Experimental and simulated regular-wave responses generally follow consistent trends. Adverse heading changes with wave period and response measure, supporting a system-level view of motions and component loads.

**Limits**　These are laboratory model tests, not full-scale offshore validation. Wind and waves are co-directional and the rotor faces the wind. Thrust matching cannot reproduce every aerodynamic/control effect; free-decay data also support calibration rather than wholly independent blind validation.

:doc:`Read the English highlight <highlights/ref-zheng2023-JRSE>` · :doc:`Original figures and full reading notes (Chinese) </paper-notes/ref-zheng2023-JRSE>` · :ref:`Full publication record <en-ref-zheng2023-JRSE>`

Open questions
----------------------------------------

Site-specific extremes, fatigue, coupling and control effects require further checks. Evidence concerns the stated semi-submersible cases and test conditions, not every platform type. See :doc:`ConcreteFloatingStructures` for material and strength questions and :doc:`NumericalWaveBasin` for numerical wave and free-surface methods.

Publications and projects
--------------------------------------------------

- :ref:`Long-term dynamic optimisation <en-ref-zhou2023-AE>`
- :ref:`Platform global sensitivity <en-ref-zhou2021-OE>`
- :ref:`Y-shaped platform orientation <en-ref-zhou2020-RE>`
- :ref:`Equivalent static wave loads <en-ref-zheng2025-OE>`
- :ref:`Wind-tunnel and wave-flume tests <en-ref-zheng2023-JRSE>`
- :ref:`Fixed-bottom jacket optimisation (related foundation study) <en-ref-zheng2023-MS>`

Related public project records (dates and roles do not imply ongoing funding):

- 2022–2025 · Provincial project · Integrated analysis and optimisation of floating wind turbines across design stages · Principal investigator.
- 2018–2020 · Municipal project · Equilibrium and vibration-control systems for floating offshore wind turbines · Core member.
- 2016–2018 · Municipal project · Key technologies for column-stabilised floating wind turbine foundations · Principal investigator.
- 2013–2015 · Municipal project · Optimisation of active/passive pitch control for vertical-axis wind turbines · Principal investigator.

:ref:`Full family project records <en-floating-wind-project-support>`.

.. raw:: html

   <span id="en-floating-wind-figures"></span><span id="en-floating-wind-dimensions-figure"></span><span id="en-floating-wind-coupling-figure"></span>

:doc:`System-analysis framework diagrams (Chinese) </IntegratedAnalysis>`.
