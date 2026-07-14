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
