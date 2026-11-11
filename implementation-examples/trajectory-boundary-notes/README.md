# Trajectory Boundary Notes

This folder holds implementation notes that matter for correct moving-Public
KSODI v3.51 interpretation, especially when a project is designing an Observer
or analytics pipeline. The notes are documentation, not an executable
implementation or conformance result.

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
5. a typed unavailable, inapplicable, incomparable or failure result is encoded
   as `0` or another ordinary numeric value

These mistakes do not just change numbers. They change the meaning of the method.

## Required boundary conditions

Before a system computes any operator trajectory, it should store or reconstruct at least:

- `evaluation_unit_id`
- `event_id`
- `entity_id`
- `trajectory_id`
- `local_trajectory_index`
- `global_event_index`
- `reply_to_event_id`
- `exchange_id` when a relational comparison is declared
- target-object and evidence-window identity
- applicable operator, state-assembly and downstream profile/version metadata
- component mask/set and typed status where applicable

## Monadic rule

For one trajectory `A`:

```text
Delta Z_A(k) = Z_A(k) - Z_A(k - 1)
```

The predecessor must belong to the same trajectory. If it does not, the local
monadic movement is not valid. The versioned Layer-2 method controls whether
the two typed `Z` objects are numerically comparable; this shorthand does not
coerce missing or non-numeric components into a movement value.

## Relational rule

The relational layer starts only after a pair is declared:

```text
pi(j) = (k_A(j), k_B(j))
```

This is a separate comparison map. It does not replace the monadic identity
model and does not itself open `R_0` or establish an `IK_rel` result.

## Implementation reading guide

Use the notes in this folder together with:

- [KSODI Implementation Guardrails](../../IMPLEMENTATION_GUARDRAILS_V351.md)
- [Operator I v3.51](../../KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/KSODI_Operator-I_Observable-Information-Impulse_V351.md)
- [KSODI Standard-Eval README](../../KSODI-Standard-Eval/README.md)
- [State Vector Z v3.51](../../KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md)
- [Relational Gate R_0 v3.51](../../KSODI-Full/Layer-4_KSODI-Relational-Gate-R_0_V350/KSODI_Relational-Gate-R_0_V351.md)

This folder is intended as a practical location for implementation guidance, not as a replacement for the canonical method definitions.
