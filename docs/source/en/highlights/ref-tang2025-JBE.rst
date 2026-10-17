Learning structural response from graphs
========================================

The problem
-----------

Structural optimisation repeatedly changes member dimensions and recalculates response. For tall buildings, the accumulated cost of finite-element analysis can limit how broadly a designer explores alternatives. A useful surrogate must represent the connections between members as well as loads and section properties.

The contribution
----------------

This study represents reinforced-concrete building frames as graphs, with structural information assigned to nodes and edges. Parametric finite-element models supply training examples and response labels. A storey-feature fusion mechanism adds information shared across a floor, while a loss formulation informed by structural displacement behaviour guides training. The resulting TBGNN models predict displacements, inter-storey drifts and the first natural period. Tests explore changes in building dimensions and loading; a CAARC building example examines transfer to a further structural configuration and different member sizes.

Engineering significance
------------------------

The study brings structural connectivity into data-driven response prediction, making it relevant to repeated design evaluation rather than only isolated numerical examples. It also makes the scope of a surrogate important: the training structures, assumed frame system and load range shape what can be predicted reliably. The reported tests support exploration within the studied setting. They do not establish a universal substitute for finite-element analysis or engineering verification. Designs selected with a surrogate still require appropriate structural checks.
