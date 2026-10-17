Better inflow for large eddy simulation
=======================================

The problem
-----------

Large eddy simulation needs incoming turbulence that represents more than a target wind-speed profile. Spatial coherence and mass conservation affect how a synthetic velocity field evolves and how pressure responds. An inflow can reproduce selected statistics yet still introduce unwanted behaviour into the computational domain.

The contribution
----------------

The coherence-improved and mass-balanced random flow generation method, CMRFG, addresses these linked requirements. Its construction combines a divergence-free velocity field with coherence control and mass-balance constraints under a frozen-turbulence assumption. The study examines relationships among the generation parameters and the pressure behaviour that can arise from unsuitable inflow construction. Validation considers turbulence statistics, spectra, spatial coherence and the transport of velocity and pressure fluctuations. These checks connect the mathematical form of the inlet field to its behaviour after entering a flow solver.

Engineering significance
------------------------

For numerical wind engineering, credible loading predictions begin with credible environmental inputs. This work provides a method for improving those inputs and a set of checks for judging them. The constraints are coupled: the method does not imply that every component of spatial coherence can be chosen independently. Grid resolution and downstream evolution also matter. Applying it to a new structure requires checking the generated flow in the intended simulation, rather than relying solely on agreement at the inlet.
