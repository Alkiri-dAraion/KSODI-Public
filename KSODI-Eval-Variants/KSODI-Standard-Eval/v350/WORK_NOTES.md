# Work Notes - v350 Observer Infrastructure

Status: public work guidance for the v350 Observer-layer structure

Purpose: keep the concrete Observer architecture distinct from the canonical
operator definitions.

This folder may describe how KSODI Standard-Eval is organized for the current
Observer path:

- Layer 1 operators
- Layer 2 state vector `Z`
- Layer 3 monadic `IK`
- Layer 4 `R0` gate
- Layer 5 relational `IK_rel`
- Layer 6 `R_geom`
- Layer 7 `R_pace`
- Layer 8 future signal-media extension

Allowed here:

- layer placement
- operator-level Delta / Delta2
- Sigma and Hangar views
- monitoring and comparability guardrails
- notes about the current Observer infrastructure profile

Guardrail:

Do not turn Observer-infrastructure choices into canonical method definitions.
When an operator meaning changes, update the canonical operator first under
`../operators_v350_canonical`, then adapt the layer file here.
