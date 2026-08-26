# KSODI Standard-Eval v350

Status: public v350 Standard-Eval structure, released layer by layer after private review

This folder contains the public v350 Standard-Eval Observer structure for
monadic observation.

Only files explicitly marked as released should be treated as current public method material. Placeholder files mark the intended structure and remain pending until the corresponding private review is complete.

Current release state, 2026-08-26: Layer 1 operators `K0`, `S0`, `O0`, `D0`
and `I0` are released with their conditional implementation companions; O
additionally includes its source-need / reference-space applicability gate.
These companions do not redefine their operators or establish a mandatory
production stack. The current reader-first Layer-2 state vector `Z_A(k_A)` and
Layer-3 monadic interaction-coherence projection `IK_A(k_A)`, together with
their conditional implementation companions, are released and close the
Standard-Eval line.

After `Z`, the separate relational / Full branch evaluates `R0` from
distinguishable `Z`-trajectories in parallel to monadic `IK`. Current dyadic
`IK_rel` requires an explicit dyadic pairing and an open numeric canonical
complete `R0` gate under the exact required profile. `R0`, `IK_rel` and the
further R-family are not part of Standard-Eval.

This release note describes how the canonical operator definitions are placed
into the monadic KSODI-Standard-Eval Observer structure: Layer 1 operators,
Layer 2 state vector `Z` and Layer 3 monadic `IK`.

Relational gates, dyadic / n-adic views and the R-family belong to
[`KSODI-Full`](../KSODI-Full/README.md).

## Layers

- [Layer 1 - Operators](./Layer-1_KSODI-Operators_V350/README.md)
- [Layer 2 - State Vector Z](./Layer-2_KSODI-State-Vector-Z_V350/README.md)
- [Layer 3 - Monadic Interaction Coherence IK](./Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/README.md)

Architecture overview:

[`../KSODI-Architecture_V350.md`](../KSODI-Architecture_V350.md)

Shared Sigma / Hangar method note:

[`../KSODI-Hangar_V350.md`](../KSODI-Hangar_V350.md)
