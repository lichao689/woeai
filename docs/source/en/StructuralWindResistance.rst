.. _en-structural-wind-resistance:

Structural Wind Resistance
====================================================

:doc:`Structural Wind Engineering <StructuralWindEngineering>` · :doc:`Research overview <Research>`

Credible wind input is the starting point, not the end, of wind-resistant design. Building form, connectivity and member dimensions determine how loads become displacements, vibration and extreme response. This subdirection studies loading, response, optimisation and control for tall buildings and related structures, seeking efficient comparisons that retain essential mechanics.

- Which structural features must a surrogate retain as dimensions and loading change?
- How should response, extremes and control performance be assessed without generalising one case to every structure?
- How should rapid screening connect to finite-element, experimental and code-based checks?

.. contents:: On this page
   :local:
   :depth: 2

.. _en-structural-wind-resistance-methods:

Methods and contributions
--------------------------------------------------

Wind loads, structural response and aerodynamic or vibration-control choices form a connected assessment. Graph-based surrogates use structural connectivity and storey information to support repeated design comparison.

Evidence in practice
----------------------------------------

.. _en-story-ref-tang2025-JBE:

TBGNN: structural connectivity meets storey features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Question**　Tall-building design comparisons repeatedly change member dimensions. A useful surrogate must retain member connectivity, wind loads and storey information while estimating changing responses.

**Contribution**　Parametric finite-element models provide training data, and reinforced-concrete frames become graphs. TBGNN adds storey-feature fusion to message passing and an engineering-informed loss to guide displacement curves.

**Evidence**　Storey-feature fusion improves displacement and inter-storey drift predictions in the reported validation set. Wind-pressure variations and CAARC member-sizing examples using the transfer-learning variant TBGNN-TL test response trends, supporting screening within the studied frame setting.

**Limits**　Validation mainly concerns static responses of reinforced-concrete frames. Errors increase beyond the training storey range; shear walls, cores and dynamic histories need separate treatment. Selected designs still require finite-element and code-based checks.

:doc:`Read the English highlight <highlights/ref-tang2025-JBE>` · :doc:`Original figures and full reading notes (Chinese) </paper-notes/ref-tang2025-JBE>` · :ref:`Full publication record <en-ref-tang2025-JBE>`

Open questions
----------------------------------------

Training coverage, structural system and loading limit present response surrogates. Static-frame results do not replace validation for shear walls, cores or dynamic histories. Vibration and flow-control evidence must retain its actual application setting. See :doc:`NumericalWindTunnel` for inflow and local wind modelling.

Publications and projects
--------------------------------------------------

- :ref:`Graph-based structural response <en-ref-tang2025-JBE>`
- :ref:`Vectorial response extremes <en-ref-yang2025-JBE>`
- :ref:`Implanted-pole liquid damping <en-ref-he2025-POF>`
- :ref:`Learning-based active flow control <en-ref-yan2025-POF>`
- :ref:`LES of tall-building wind loads <en-ref-chen2024-POF>`
- :ref:`Tower–line coupling in strong winds <en-ref-liu2024-JWEIA>`

Related public project records (dates and roles do not imply ongoing funding):

- 2020–2023 · Municipal project · Aerodynamic shape optimisation of tall buildings considering wind loads and responses · Principal investigator.

:ref:`Full family project records <en-building-wind-project-support>`.
