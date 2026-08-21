# Layer 4 — KSODI Relational Gate (`R_0`)

Status: public v3.50 reference release

Naming convention: `R_0` is the canonical textual and filename label. It
preserves the original mathematical convention in which `0` is a subscript.
Legacy prose, formulas and code-compatible identifiers may use
`R0`; both forms denote this same relational gate, never separate elements.

`R_0` is the relational gate for dyadic or n-adic observation. It is evaluated
from distinguishable `Z`-trajectories and runs in parallel to monadic `IK`.

It asks whether distinguishable trajectories are stable enough for relational
comparison. It is not full resonance, is not downstream of `IK`, and must not
be collapsed into `IK`.

Released method file:

[`KSODI_Relational-Gate-R_0_V350.md`](./KSODI_Relational-Gate-R_0_V350.md)
