# KSODI Standard-Eval

## Public orientation note

This folder contains public KSODI Standard-Eval materials for conceptual
review, discussion and version traceability.

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

- [`Standard-Eval_v350`](./Standard-Eval_v350/README.md) contains the active
  layer-based public Standard-Eval structure.
- [`KSODI_V350_ARCHITECTURE_ASCII.md`](../../KSODI_V350_ARCHITECTURE_ASCII.md)
  gives a compact layer sketch for the current v350 direction.

## Related folders

- `Standard-Eval_v350` contains the current monadic layer-based v350 public
  Standard-Eval structure.
- `archive_historical-v33` preserves public 3.3 operator, state-vector,
  projection and deprecated draft material for provenance and transparency.
- The historical v3.42 Observer assets are preserved separately under
  [`../archive_assets_historical-observer-v342`](../archive_assets_historical-observer-v342/README.md).
  They document implementation and dashboard work from the v3.3 to v3.42 line,
  not current v350 implementation guidance.
