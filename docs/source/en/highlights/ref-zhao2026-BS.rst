Reusing CFD for urban wind assessment
=====================================

The problem
-----------

A detailed urban wind simulation can resolve how buildings redirect and accelerate flow, but repeating a high-resolution calculation for an entire city is expensive. A practical assessment tool needs a way to reuse that computation while retaining the influence of surrounding geometry.

The contribution
----------------

This study divides an urban area into computational blocks and builds a database of precomputed CFD results. Transition regions account for neighbouring buildings around each block. Stored wind-speed ratios and pressure coefficients then support rapid estimates under specified incoming wind conditions. The framework examines consistency between adjoining blocks and compares predictions with observations from meteorological stations. A WebGIS demonstration makes the resulting microscale wind information accessible through a map-based interface.

Engineering significance
------------------------

The work shows how costly flow calculations can become reusable infrastructure for urban wind assessment. The central design question is where local detail must be retained and where a database can support efficient queries. Its engineering value lies in connecting simulation, observations and spatial presentation. Results remain conditional on the simulated geometry, inflow assumptions and database coverage. The demonstration should therefore be read as a research framework for rapid assessment; it does not establish an operational forecasting or warning service.
