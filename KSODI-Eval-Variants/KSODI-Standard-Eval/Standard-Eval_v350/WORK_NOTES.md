# Work Notes - Standard-Eval v350

Status: public work guidance for the v350 Standard-Eval structure

Purpose: keep Standard-Eval monadic and distinct from KSODI-Full.

This folder may describe how KSODI Standard-Eval is organized for monadic
observation:

- Layer 1 operators
- Layer 2 state vector `Z`
- Layer 3 monadic `IK`

Allowed here:

- layer placement
- operator-level Delta / Delta2
- Sigma and Hangar views
- monitoring and comparability guardrails
- notes about monadic Observer infrastructure profiles

Guardrail:

Do not turn Observer-infrastructure choices into canonical method definitions,
and do not pull relational / R-family layers back into Standard-Eval. When an
operator meaning changes, update the corresponding Layer 1 operator file here.

## Current Public State - 2026-07-14

The public v350 Standard-Eval structure has been consolidated under this
folder. Public canonical operator files belong in Layer 1, not in separate
competing operator folders.

Released in public Layer 1:

- `Operator_I_v350.md` - `I0`, Observable Information Impulse
- `Operator_D_v350.md` - `D0`, Observable Clarity
- `Operator_O_v350.md` - `O0`, Observable Grounded Objectivity

Not yet released:

- `S0` - Observable Structural Coherence
- `K0` - Observable Context Completeness

`S0` and `K0` remain private review items. Do not add public canonical S/K files
until Anne explicitly releases the corrected private versions.

Architecture guardrail: Standard-Eval is monadic. `Z(t)` feeds both monadic
`IK` and the relational `R0` gate, but `R0`, `IK_rel` and the R-family belong in
KSODI-Full.
