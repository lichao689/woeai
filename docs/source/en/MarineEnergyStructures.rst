.. _en-research-direction-floating-wind:

.. _en-floating-offshore-wind-turbine:

Marine Energy Structures
=================================================================

:doc:`Research overview <Research>` · :doc:`Structural Wind Engineering <StructuralWindEngineering>`

From coupled environmental loading to a defensible floating-system design.

.. contents:: On this page
   :local:
   :depth: 2

Background
------------------------------

Floating wind turbines combine a rotor, tower, platform and moorings in a changing marine environment. A design favourable for one motion may worsen another load or fatigue measure. Long-term conditions, structural strength and cost must therefore be considered together, with numerical predictions checked against suitable physical evidence.

Research questions
------------------------------

- How do platform dimensions and moorings change long-term cost–fatigue trade-offs?
- How can a concrete platform concept connect dynamic performance to load-bearing structural assessment?
- Which wind–wave headings are adverse for different motions and component loads?

Methods and contributions
------------------------------

.. _en-floating-wind-integrated-analysis:

Integrated Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Coupled turbine–platform–mooring models, reduced-order analysis and surrogate-assisted optimisation connect long-term environments with design alternatives. Wind–wave model tests provide physical comparisons.

.. _en-concrete-floating-structures:

Concrete Floating Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Platform geometry, material choice and moorings are assessed together before structural-strength checks. Concept optimisation does not replace local-detail design.

.. _en-numerical-wave-basin:

Numerical Wave Basin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wave generation, propagation, absorption and free-surface modelling support interaction studies. Method credibility depends on boundary, mesh and benchmark validation; this page does not claim a separate demonstrated wave-basin result.

.. figure:: ../../_static/research/research-method-marine-en.svg
   :figclass: research-method
   :width: 100%
   :alt: Conceptual workflow from inputs to evidence and design; not research data.

   Original explanatory diagram, not research data. Methods span separate studies; this is not an end-to-end validation of one platform. No numerical performance is implied.

Evidence in practice
------------------------------

The studies below mirror the Chinese topic page. Original research figures remain in the linked Chinese reading notes; the schematic above explains the method without reproducing data or implying a new result.

.. _en-story-ref-zhou2023-AE:

Long-term optimisation: cost–fatigue trade-offs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Question**　Platform dimensions and moorings jointly affect manufacturing cost and fatigue across many wind–wave combinations. Comparing one fixed design per concept can conceal the alternatives each concept offers.

**Contribution**　A reduced-order dynamic model, representative environmental sampling and a Kriging surrogate support NSGA-II searches for Pareto trade-offs among manufacturing cost, tower-base fatigue and fairlead fatigue.

**Evidence**　Response comparisons with OpenFAST assess the reduced-order model. For square and Y-shaped steel semi-submersibles, long-term conditions and platform–mooring choices alter the fronts. Square designs favour tower-base fatigue, while some Y-shaped designs have lower mooring fatigue.

**Limits**　Manufacturing cost is not life-cycle cost. This is concept screening under specific environmental, turbine, cost and design assumptions; hull strength was not checked. No single metric establishes a universally best platform.

:doc:`Read the English highlight <highlights/ref-zhou2023-AE>` · :doc:`Original figures and full reading notes (Chinese) </paper-notes/ref-zhou2023-AE>` · :ref:`Full publication record <en-ref-zhou2023-AE>`

.. _en-story-ref-he2026-OE-structural:

Concrete platforms: from long-term response to strength
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Question**　Material choice changes mass, response and cost. A cheaper platform body does not necessarily make a better floating system, and a favourable dynamic design still needs structural assessment.

**Contribution**　A modular reinforced-concrete semi-submersible concept is explored using reduced-order modelling and NSGA-II for dimensions, moorings and cost–fatigue trade-offs. A selected design then undergoes finite-element analysis with prestressing.

**Evidence**　Under the study’s turbine, environmental and cost assumptions, numerical comparison with OO-Star indicates lower accumulated tower-base and fairlead fatigue and lower estimated construction cost for the selected design. Prestressing improves overall stress distribution.

**Limits**　This is a numerically assessed concept, not a constructed or certified design. Local peaks differ from the overall stress range. Joints, stress concentrations and future scale-model tests require further work; cost estimates are not project quotations.

:doc:`Read the English highlight <highlights/ref-he2026-OE-structural>` · :doc:`Original figures and full reading notes (Chinese) </paper-notes/ref-he2026-OE-structural>` · :ref:`Full publication record <en-ref-he2026-OE-structural>`

.. _en-story-ref-zheng2023-JRSE:

1:70 wind–wave testing: heading and system response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Question**　The geometry of a Y-shaped platform and its moorings is directional. Changing wind–wave heading can change motions, tower-base loads and nacelle acceleration in different ways.

**Contribution**　A 1:70 wind-tunnel and wave-flume model represents a 10 MW reference turbine. Thrust matching and calibrated inputs support three-heading comparisons of still-water, wind-only, wave-only and combined conditions alongside OpenFAST.

**Evidence**　Experimental and simulated regular-wave responses generally follow consistent trends. Adverse heading changes with wave period and response measure, supporting a system-level view of motions and component loads.

**Limits**　These are laboratory model tests, not full-scale offshore validation. Wind and waves are co-directional and the rotor faces the wind. Thrust matching cannot reproduce every aerodynamic/control effect; free-decay data also support calibration rather than wholly independent blind validation.

:doc:`Read the English highlight <highlights/ref-zheng2023-JRSE>` · :doc:`Original figures and full reading notes (Chinese) </paper-notes/ref-zheng2023-JRSE>` · :ref:`Full publication record <en-ref-zheng2023-JRSE>`

Open questions
------------------------------

Concept selection must progress to local-detail strength, site-specific extreme and fatigue assessment, and validation of coupled models. Numerical wave-basin methods need their own benchmarks; fixed-bottom studies and damping foundations support the field but do not establish floating-system validation. Evidence here concerns the stated semi-submersible cases, not demonstrated results for every platform type or ocean-energy technology.

Publications and projects
------------------------------

Full titles, authors, journals and DOI links are retained in the publication records and reading pages. The short links below are navigation labels, not replacements for the original titles.

- :ref:`Long-term dynamic optimisation <en-ref-zhou2023-AE>`
- :ref:`Platform global sensitivity <en-ref-zhou2021-OE>`
- :ref:`Y-shaped platform orientation <en-ref-zhou2020-RE>`
- :ref:`Equivalent static wave loads <en-ref-zheng2025-OE>`
- :ref:`Wind-tunnel and wave-flume tests <en-ref-zheng2023-JRSE>`
- :ref:`Fixed-bottom jacket optimisation (related foundation study) <en-ref-zheng2023-MS>`
- :ref:`Concrete floater design and optimisation <en-ref-he2026-OE-structural>`
- :ref:`Concrete and steel support comparison <en-ref-li2022-SOS>`

.. _en-floating-wind-project-support:

.. raw:: html

   <span id="research-project"></span>

Project support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following public project records support the questions above; their dates and roles do not imply ongoing funding or current partnerships.

- 2022–2025 · Provincial project · Integrated analysis and optimisation of floating wind turbines across design stages · Principal investigator.
- 2022–2025 · Provincial project · Semi-submersible foundation design using FRP–steel composite reinforcement and seawater sea-sand concrete · Participant.
- 2018–2020 · Municipal project · Equilibrium and vibration-control systems for floating offshore wind turbines · Core member.
- 2016–2018 · Municipal project · Key technologies for column-stabilised floating wind turbine foundations · Principal investigator.
- 2013–2015 · Municipal project · Optimisation of active/passive pitch control for vertical-axis wind turbines · Principal investigator.

:doc:`Engineering applications and enterprise project evidence (Chinese) </EngineeringApplications>`.
