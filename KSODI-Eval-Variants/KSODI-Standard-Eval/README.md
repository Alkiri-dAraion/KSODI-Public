# KSODI Standard-Eval

## Public orientation note

This folder contains public KSODI Standard-Eval materials for conceptual
review, discussion and version traceability.

The public 3.3 files are not recommended as an implementation reference. They
contain known structural issues and are being superseded by a revised private
reference line.

## Role of Standard-Eval

KSODI Standard-Eval is the numeric observation layer of the KSODI method. It is
designed to support observable, explainable and audit-capable evaluation of
interaction states over time.

Standard-Eval focuses on:

- the five KSODI operators
- state-vector observation
- interaction coherence
- relational comparability gates
- drift and stability signals

In the current v3.5 direction, interaction coherence is not resonance. `IK`
belongs to the coherence/projection layer; resonance-family interpretation
belongs only after the relevant relational gate.

R0 / R_0 belongs to this gate logic. It is used as an orientation point for
deciding whether a dyadic or n-adic relational observation is meaningful before
broader KSODI-Full resonance-family observations are interpreted.

## Current research direction

The revised private reference line distinguishes monadic observation layers
from dyadic and n-adic relational observation layers.

This distinction matters for agentic systems: a human-machine, agent-agent or
n-agent interaction may look active or even resonant while still lacking shared
direction, comparability or stable interaction coherence.

Public files in this folder should therefore be read as research-oriented
material, not as a complete or tested specification.

## v350 Preview

The reviewed v350 line is being released into this public repository step by
step after private review.

- [`operators_v350`](./operators_v350/README.md) contains reviewed v350
  operator files as they become public.
- [`KSODI_V350_ARCHITECTURE_ASCII.md`](./KSODI_V350_ARCHITECTURE_ASCII.md)
  gives a compact layer sketch for the current v350 direction.

## Related folders

- `operators_v3.3` contains public 3.3 operator material.
- `operators_v350` contains reviewed v350 operator material as it is released.
- `state-vectors_Z_v3.3` contains public 3.3 state-vector material.
- `projections_IK_v3.3` contains public 3.3 projection material.
- `operators_deprecated` preserves earlier draft material for transparency.
