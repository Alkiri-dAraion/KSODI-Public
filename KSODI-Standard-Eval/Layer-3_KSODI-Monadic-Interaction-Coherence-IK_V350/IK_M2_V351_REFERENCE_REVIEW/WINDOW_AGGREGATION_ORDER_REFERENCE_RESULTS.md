# IK v3.51 window aggregation-order reference results

Date: 2026-11-06

## Purpose

This bounded fixture verifies the mathematical distinction between:

```text
derive_then_aggregate
aggregate_then_derive
```

under the arithmetic-mean reference profile in the
[window and aggregation-order contract](./IK_V351_WINDOW_AGGREGATION_ORDER_CONTRACT_V01.md).
It does not select a universal domain aggregator, empirical threshold or
production window.

## Reproducible artifacts

- [`calculate_window_aggregation_order_reference.py`](./calculate_window_aggregation_order_reference.py)
  calculates the four windows with Python's standard library and checks the
  declared linearity, Jensen and counterexample conditions;
- [`window_aggregation_order_reference.csv`](./window_aggregation_order_reference.csv)
  retains the exact member and aggregate Z vectors beside both result orders.

## Verified cases

| Window | Distinction | Result |
| --- | --- | --- |
| `W_CONSTANT` | identical complete Z states | both orders agree for every component |
| `W_COORDINATE_SWAP` | two different coordinate-labelled unit states | `IK_ref` agrees; both nonlinear order gaps are positive |
| `W_SAME_REFERENCE_RAY` | different states on the same positive reference ray | both order gaps are zero although the states are not identical |
| `W_CENTERED_CANCELLATION` | opposing off-axis shapes with balanced aggregate Z | aggregate-state deviation is zero while mean per-state deviation is positive |

The two-state coordinate-swap fixture reproduces:

```text
Gap_M2 ~= 0.130985829483
Gap_AxisDev_ref ~= 0.155051025722
```

The additional controls show why a gap is a bounded aggregation-order
diagnostic, not a semantic result:

- a positive gap indicates information compressed by the aggregate-state
  reading under this exact profile;
- a zero gap does not prove identical member states;
- a balanced aggregate state does not prove balanced individual states;
- none of the gaps establishes coherence, quality, conflict, volatility,
  relation, Pace or causality.

## Bounded finding

Under the arithmetic-mean reference profile:

- `IK_ref` commutes with arithmetic-mean aggregation because it is linear;
- `IK_M2` and `AxisDev_ref` are nonlinear, so their two aggregation orders can
  answer different questions;
- a positive order gap shows that the aggregate-state reading compressed
  member-level variation in the named fixture;
- a zero order gap does not establish identical members or semantic
  equivalence.

Every derived window result therefore retains a return path to the exact
member identities and order, the aggregate-Z identity, aggregator and version,
coverage, typed status partition and provenance. An aggregate window object is
not written back as the state of a participant and does not replace canonical
complete `Z`.

## Delta and trajectory guard

Window aggregation, state derivation and result derivation are distinct
operations. Their order must be named. In particular, an aggregation-order
gap is not interchangeable with `ΔZ`, `Δ²Z`, path length or a
difference between adjacent windows.

## Review boundary

The fixture supports retaining both orders as separately identified answers
in laboratory comparison. It does not decide the later coverage threshold,
minimum member count, role-specific visualization or any physical storage/API
architecture. It also does not test incomplete or nonnumeric members,
overlapping windows, event-count versus clock-time windows, PPWA profiles or a
production aggregation policy. Those require their own declared contracts and
tests.
