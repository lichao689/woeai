.. _en-numerical-wind-tunnel:

Numerical Wind Tunnel
==========================================

:doc:`Structural Wind Engineering <StructuralWindEngineering>` · :doc:`Research overview <Research>`

Buildings and terrain alter local wind conditions, while inflow turbulence and boundary treatment determine how credibly a numerical wind tunnel develops the flow. This subdirection connects atmospheric inflow, geometry and reusable CFD for urban and complex-terrain assessment: where the wind comes from and how it moves.

- How can turbulence statistics and spatial coherence be retained without artificial inlet pressure?
- How can block-based CFD retain surrounding-building effects while reducing repeated computation?
- Which simulations must be updated when geometry or meteorological inputs change?

.. contents:: On this page
   :local:
   :depth: 2

.. _en-numerical-wind-tunnel-methods:

Methods and contributions
--------------------------------------------------

Synthetic turbulent inflow and explicit boundary conditions underpin CFD. Urban block databases and geometry reconstruction make high-cost simulations reusable while retaining the influence of surrounding conditions.

Evidence in practice
----------------------------------------

.. _en-story-ref-chen2024-JCP:

CMRFG: coherent, mass-balanced inflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Question**　Matching a velocity spectrum does not establish credible pressure behaviour. Spatial-coherence errors and unbalanced instantaneous inlet flux can affect downstream flow development.

**Contribution**　CMRFG combines target coherence, a divergence-free field and inlet mass balance during random-flow generation, rather than relying only on corrections after generation.

**Evidence**　Homogeneous isotropic and spatially decaying homogeneous anisotropic cases examine velocity statistics, coherence and pressure development. Coherence follows the target more closely, while mass-balance correction suppresses non-physical pressure contamination inside the domain.

**Limits**　The prescribed coherence concerns a particular velocity component and direction, not independently arbitrary functions for every component. Local residual pressure remains at inlet–side-boundary intersections. Buildings and complex terrain require further validation.

:doc:`Read the English highlight <highlights/ref-chen2024-JCP>` · :doc:`Original figures and full reading notes (Chinese) </paper-notes/ref-chen2024-JCP>` · :ref:`Full publication record <en-ref-chen2024-JCP>`

.. _en-story-ref-zhao2026-BS:

Urban CFD: precompute once, query locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Question**　Urban assessment needs building-scale flow detail without repeating expensive simulations. Dividing a city into blocks can reduce the computation but also omit surrounding buildings and terrain.

**Contribution**　For part of Shenzhen, core blocks are surrounded by transition regions. Precomputed CFD wind-speed ratios and pressure coefficients form a reusable database for queries and WebGIS display with meteorological inputs.

**Evidence**　Tests compare transition lengths, shared interfaces and separate versus combined simulations, then check wind-speed ratios against filtered station observations. They support the block-based approach in the studied setting while exposing local differences and the need for interface treatment.

**Limits**　Evidence is limited to neutral atmospheric boundary-layer conditions and selected stations, headings and high-wind samples. Geometry changes require recomputation of affected blocks and their surroundings. The WebGIS demonstration does not establish operational warning accuracy, AI-surrogate performance or digital-twin performance.

:doc:`Read the English highlight <highlights/ref-zhao2026-BS>` · :doc:`Original figures and full reading notes (Chinese) </paper-notes/ref-zhao2026-BS>` · :ref:`Full publication record <en-ref-zhao2026-BS>`

Open questions
----------------------------------------

New terrain, building groups, non-neutral boundary layers and unsteady conditions require renewed checks of boundaries, local pressure and data coverage. The urban database evidence does not establish operational warning performance. Structural-response assessment continues in :doc:`StructuralWindResistance`.

Publications and projects
--------------------------------------------------

- :ref:`Urban CFD database <en-ref-zhao2026-BS>`
- :ref:`Satellite-based urban geometry <en-ref-zhao2026-BE>`
- :ref:`Temporal wind super-resolution <en-ref-tang2026-RE>`
- :ref:`3D Gaussian building reconstruction <en-ref-zhao2025-SCS>`
- :ref:`Vector-potential flow generation <en-ref-li2024-POF>`
- :ref:`Coherent, mass-balanced inflow <en-ref-chen2024-JCP>`

Related public project records (dates and roles do not imply ongoing funding):

- 2018–2021 · National project · Improvement and validation of numerical atmospheric turbulent boundary-layer generation methods · Principal investigator.
- 2014–2016 · National project · LES of equilibrium atmospheric boundary-layer turbulence with rough-wall correction · Principal investigator.
- 2014–2016 · University project · LES of three-dimensional self-balanced turbulent boundary-layer flow · Principal investigator.
- 2013–2015 · University project · LES of three-dimensional turbulence in an atmospheric boundary-layer numerical wind tunnel · Principal investigator.

:ref:`Full family project records <en-building-wind-project-support>`.
