# KSODI Standard-Eval v350

Status: public v350 structure, released layer by layer after private review

This folder contains the public v350 Standard-Eval Observer-infrastructure
layer structure.

Only files explicitly marked as released should be treated as current public method material. Placeholder files mark the intended structure and remain pending until the corresponding private review is complete.

The architecture-independent operator definitions live separately under:

[`../operators_v350_canonical`](../operators_v350_canonical/README.md)

This `v350` folder describes how those definitions are placed into the current
Observer structure: Layer 1 operators, Layer 2 state vector `Z`, monadic `IK`,
the `R0` gate, relational `IK_rel` and the active R-family layers.

## Layers

- [Layer 0 - KSODI-Light-Agent](./layer-0-ksodi-light-agent/README.md)
- [Layer 1 - Operators](./layer-1-operators/README.md)
- [Layer 2 - State Vector Z](./layer-2-state-vector-z/README.md)
- [Layer 3 - IK](./layer-3-ik/README.md)
- [Layer 4 - R0 Gate](./layer-4-r0-gate/README.md)
- [Layer 5 - IK_rel](./layer-5-ik-rel/README.md)
- [Layer 6 - R_geom](./layer-6-r-geom/README.md)
- [Layer 7 - R_pace](./layer-7-r-pace/README.md)
- [Layer 8 - Future Signal-Media](./layer-8-future-signal-media/README.md)

Architecture overview:

[`../KSODI_V350_ARCHITECTURE_ASCII.md`](../KSODI_V350_ARCHITECTURE_ASCII.md)
