# KSODI Standard-Eval

## Public orientation note

This folder contains public KSODI Standard-Eval materials for conceptual
review, discussion and version traceability.

The shared structural and method boundary with KSODI-Full is documented in
the root
[KSODI-Standard-Eval / KSODI-Full Transition V350](../KSODI-Standard-Eval_Full-Transition_V350.md).

The public 3.3 files and the later v3.42 working / implementation line are
historical material. They are not recommended as current implementation
references. They contain or reveal known structural issues and are superseded
by the reviewed v350 line.

## Role of Standard-Eval

KSODI Standard-Eval is the numeric observation layer of the KSODI method. It is
designed to support observable, explainable and audit-capable evaluation of
interaction states over time.

Standard-Eval focuses on:

- the five KSODI operators
- state-vector observation
- interaction coherence
- drift and stability signals

In the current v3.5 direction, interaction coherence is not resonance. The
complete monadic Standard-Eval line is `K/S/O/D/I -> Z -> IK`; Standard-Eval
ends with `IK`.

After `Z`, the architecture branches. `R0 / R_0` belongs to KSODI-Full gate
logic and is evaluated from distinguishable `Z`-trajectories in parallel to
monadic `IK`. Only after a stable `R0` does `IK_rel` open the relational
projection branch, followed by the further R-family. `R0`, `IK_rel` and the
further R-family are not part of Standard-Eval.

## Current research direction

The revised private reference line distinguishes monadic observation layers
from dyadic and n-adic relational observation layers.

This distinction matters for agentic systems: a human-machine, agent-agent or
n-agent interaction may look active or even resonant while still lacking
observable direction, comparability or stable interaction coherence.

Public files in this folder should therefore be read as public method
documentation for the released monadic Standard-Eval line, not as a complete
software implementation or empirical validation claim.

Action-adjacent material such as controlled intervention, policy-defined
responses or controller boundaries belongs under KSODI-Full, not under
Standard-Eval.

## v350 Public Release

The reviewed v350 line is being released into this public repository step by
step after private review.

As of 2026-07-21, the public v350 Standard-Eval release contains all five
Layer-1 operators, the Layer-2 state vector `Z` and the Layer-3 monadic `IK`
projection.

- [`KSODI-Standard-Eval-Release_V350.md`](./KSODI-Standard-Eval-Release_V350.md)
  records the active v3.5 release boundary.
- [`Layer-1_KSODI-Operators_V350/`](./Layer-1_KSODI-Operators_V350/README.md),
  [`Layer-2_KSODI-State-Vector-Z_V350/`](./Layer-2_KSODI-State-Vector-Z_V350/README.md) and
  [`Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/`](./Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/README.md) contain the current
  layer-based public KSODI-Standard-Eval structure.
- [`KSODI-Architecture_V350.md`](../KSODI-Architecture_V350.md)
  gives a compact layer sketch for the current v350 direction.

## Related folders

- The Layer 1-3 folders contain the current monadic v3.5 public
  KSODI-Standard-Eval structure.
- [`method-history-v33`](../archive/method-history-v33/README.md) preserves public 3.3 operator, state-vector,
  projection and deprecated draft material for provenance and transparency.
- The historical v3.42 Observer assets are preserved separately under
  [`historical-observer-v342`](../archive/assets-archive/historical-observer-v342/README.md).
  They document implementation and dashboard work from the v3.3 to v3.42 line,
  not current v350 implementation guidance.
