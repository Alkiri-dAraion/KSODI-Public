# KSODI Standard-Eval

## Public orientation note

This folder contains public KSODI Standard-Eval materials for conceptual
review, discussion and version traceability.

The public 3.3 files are archived as historical material. They are not
recommended as an implementation reference. They contain known structural issues
and are being superseded by the reviewed v350 line.

## Role of Standard-Eval

KSODI Standard-Eval is the numeric observation layer of the KSODI method. It is
designed to support observable, explainable and audit-capable evaluation of
interaction states over time.

Standard-Eval focuses on:

- the five KSODI operators
- state-vector observation
- interaction coherence
- drift and stability signals

In the current v3.5 direction, interaction coherence is not resonance. `IK`
belongs to the monadic coherence/projection layer. Relational gates and
resonance-family interpretation belong to KSODI-Full.

R0 / R_0 belongs to KSODI-Full gate logic. It is used as an orientation point
for deciding whether a dyadic or n-adic relational observation is meaningful
before broader resonance-family observations are interpreted.

## Current research direction

The revised private reference line distinguishes monadic observation layers
from dyadic and n-adic relational observation layers.

This distinction matters for agentic systems: a human-machine, agent-agent or
n-agent interaction may look active or even resonant while still lacking shared
direction, comparability or stable interaction coherence.

Public files in this folder should therefore be read as research-oriented
material, not as a complete or tested specification.

Action-adjacent material such as controlled intervention, policy-defined
responses or controller boundaries belongs under KSODI-Full, not under
Standard-Eval.

## v350 Preview

The reviewed v350 line is being released into this public repository step by
step after private review.

As of 2026-07-21, the public v350 Standard-Eval release contains all five
Layer-1 operators, the Layer-2 state vector `Z` and the Layer-3 monadic `IK`
projection.

- [`Standard-Eval_v350`](./Standard-Eval_v350/README.md) contains the active
  layer-based public Standard-Eval structure.
- [`KSODI_V350_ARCHITECTURE_ASCII.md`](../KSODI_V350_ARCHITECTURE_ASCII.md)
  gives a compact layer sketch for the current v350 direction.

## Related folders

- `Standard-Eval_v350` contains the current monadic layer-based v350 public
  Standard-Eval structure.
- `archive_historical-v33` preserves public 3.3 operator, state-vector,
  projection and deprecated draft material for provenance and transparency.
