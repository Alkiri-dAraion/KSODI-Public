# Trajectory Boundary Notes

Status: public implementation notes for monadic boundary discipline

This folder holds implementation notes that matter for correct KSODI v3.50 interpretation, especially when a project is building an actual Observer or analytics pipeline.

The most important rule is simple:

- monadic movement remains inside one declared trajectory
- relational pairing is declared separately
- shared context is not the same as shared state
- trajectory identity is not optional metadata

## Why this matters

A lot of implementation problems in interaction analysis come from collapsing these differences:

1. one conversation thread is mistaken for one entity trajectory
2. adjacent events are treated as monadic changes without checking source identity
3. a question and an answer are merged into one state before trajectory separation
4. a dyadic comparison is silently evaluated even though the pair was never declared
5. `not_applicable` is encoded as `0` or a default value

These mistakes do not just change numbers. They change the meaning of the method.

## Required boundary conditions

Before a system computes any operator trajectory, it should store or reconstruct at least:

- `event_id`
- `entity_id`
- `trajectory_id`
- `trajectory_index`
- `global_event_index`
- `reply_to_event_id`
- `exchange_id` when a relational comparison is declared
- applicable operator profile and version metadata

## Monadic rule

For one trajectory `A`:

```text
Delta Z_A(k) = Z_A(k) - Z_A(k - 1)
```

The predecessor must belong to the same trajectory. If it does not, the local monadic movement is not valid.

## Relational rule

The relational layer starts only after a pair is declared:

```text
pi(j) = (k_A(j), k_B(j))
```

This is a separate comparison map. It does not replace the monadic identity model.

## Implementation reading guide

Use the notes in this folder together with:

- [KSODI Implementation Guardrails](../../../IMPLEMENTATION_GUARDRAILS.md)
- [Operator I v3.50](../../../KSODI-Standard-Eval/layer-1-operators/Operator_I_v350.md)
- [KSODI Standard-Eval README](../../../KSODI-Standard-Eval/README.md)

This folder is intended as a practical location for implementation guidance, not as a replacement for the canonical method definitions.
