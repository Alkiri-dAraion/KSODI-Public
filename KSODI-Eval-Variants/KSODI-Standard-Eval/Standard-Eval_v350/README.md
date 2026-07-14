# KSODI Standard-Eval v350

Status: public v350 Standard-Eval structure, released layer by layer after private review

This folder contains the public v350 Standard-Eval Observer structure for
monadic observation.

Only files explicitly marked as released should be treated as current public method material. Placeholder files mark the intended structure and remain pending until the corresponding private review is complete.

The architecture-independent operator definitions live separately under:

[`../operators_v350_canonical`](../operators_v350_canonical/README.md)

This `Standard-Eval_v350` folder describes how the canonical operator
definitions are placed into the monadic Observer structure: Layer 1 operators,
Layer 2 state vector `Z` and Layer 3 monadic `IK`.

Relational gates, dyadic / n-adic views and the R-family belong to
[`../../KSODI-Full/Full_v350`](../../KSODI-Full/Full_v350/README.md).

## Layers

- [Layer 1 - Operators](./layer-1-operators/README.md)
- [Layer 2 - State Vector Z](./layer-2-state-vector-z/README.md)
- [Layer 3 - IK](./layer-3-ik/README.md)

Architecture overview:

[`../../KSODI_V350_ARCHITECTURE_ASCII.md`](../../KSODI_V350_ARCHITECTURE_ASCII.md)
