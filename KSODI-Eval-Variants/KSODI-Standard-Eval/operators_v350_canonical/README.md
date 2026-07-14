# KSODI Standard-Eval Operators v350 Canonical

Status: canonical public v350 operator line

This folder contains architecture-independent KSODI Standard-Eval operator
definitions for the v350 line.

Canonical operator definitions must avoid assumptions about a particular
Observer infrastructure, database layout, orchestration stack, deployment
boundary or monitoring implementation. They define what the operator means,
what it observes, which reference spaces are required and which comparability
conditions apply.

The current Observer-infrastructure adaptation lives separately under:

[`../Standard-Eval_v350/layer-1-operators`](../Standard-Eval_v350/layer-1-operators/README.md)

Released operator:

- [`I0 - Observable Information Impulse`](./operator-I_v350.md)

Pending public review:

- `K0 - Observable Context Completeness`
- `S0 - Observable Structural Coherence`
- `O0 - Observable Grounded Objectivity`
- `D0 - Observable Clarity`

Working rule:

1. Write and review the canonical operator here first.
2. Then adapt the reviewed operator into the Observer-layer structure under
   `../Standard-Eval_v350/layer-1-operators`.
3. Keep implementation-specific terms out of the canonical definition unless
   they are explicitly marked as examples or non-normative notes.

Historical 3.3 and deprecated public drafts are archived separately under:

[`../archive/historical-v33`](../archive/historical-v33/README.md)
