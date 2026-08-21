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

## Current Public State - 2026-07-21

The public v350 Standard-Eval structure has been consolidated under this
folder. Public canonical operator files belong in Layer 1, not in separate
competing operator folders.

Released in public Layer 1:

- `KSODI_Operator-K_Observable-Context-Completeness_V350.md` - `K0`, Observable Context Completeness
- `KSODI_Operator-I_Observable-Information-Impulse_V350.md` - `I0`, Observable Information Impulse
- `KSODI_Operator-D_Observable-Clarity_V350.md` - `D0`, Observable Clarity
- `KSODI_Operator-O_Observable-Grounded-Objectivity_V350.md` - `O0`, Observable Grounded Objectivity
- `KSODI_Operator-O_Source-Need-Gate_V350.md` - `O0` source-need / reference-space
  applicability companion note
- `KSODI_Operator-S_Observable-Structural-Coherence_V350.md` - `S0`, Observable Structural Coherence

Released in public Layer 2:

- `KSODI_State-Vector-Z_V350.md` - KSODI State Vector Z

Released in public Layer 3:

- `KSODI_Monadic-Interaction-Coherence-IK_V350.md` - monadic Interaction Coherence Projection

Architecture guardrail: Standard-Eval is monadic. `Z(t)` feeds both monadic
`IK` and the relational `R0` gate, but `R0`, `IK_rel` and the R-family belong in
KSODI-Full.
