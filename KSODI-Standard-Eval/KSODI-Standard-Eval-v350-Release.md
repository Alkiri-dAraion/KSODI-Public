# KSODI Standard-Eval v350

Status: public v350 Standard-Eval structure, released layer by layer after private review

This folder contains the public v350 Standard-Eval Observer structure for
monadic observation.

Only files explicitly marked as released should be treated as current public method material. Placeholder files mark the intended structure and remain pending until the corresponding private review is complete.

Current release state: Layer 1 operators `K0`, `S0`, `O0`, `D0` and `I0`
are released. The `O0` source-need / reference-space applicability companion
note is released. Layer 2, the monadic state vector `Z(t)` (`Z_vec`), and Layer
3, the monadic interaction-coherence projection `IK`, are released. `IK` closes
the Standard-Eval line.

After `Z`, the separate relational / Full branch evaluates `R0` from
distinguishable `Z`-trajectories in parallel to monadic `IK`. Stable `R0` gates
`IK_rel`, followed by the further R-family. `R0`, `IK_rel` and the further
R-family are not part of Standard-Eval.

This release note describes how the canonical operator definitions are placed
into the monadic KSODI-Standard-Eval Observer structure: Layer 1 operators,
Layer 2 state vector `Z` and Layer 3 monadic `IK`.

Relational gates, dyadic / n-adic views and the R-family belong to
[`KSODI-Full`](../KSODI-Full/README.md).

## Layers

- [Layer 1 - Operators](./layer-1-operators/README.md)
- [Layer 2 - State Vector Z](./layer-2-state-vector-z_v350/README.md)
- [Layer 3 - IK](./layer-3-ik_v350/README.md)

Architecture overview:

[`../KSODI-Architecture_V350.md`](../KSODI-Architecture_V350.md)

Shared Sigma / Hangar method note:

[`../KSODI-Hangar_V350.md`](../KSODI-Hangar_V350.md)
