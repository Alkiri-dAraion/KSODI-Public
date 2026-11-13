# IK v3.51 question–measurement–view matrix

## 1. Purpose

This matrix helps readers select the smallest sufficient IK view without
mistaking a projection for the complete observation object. It asks:

> For one declared investigation question, which retained object and
> calculation are required, which human or machine view is useful, and what
> may not be inferred from that view?

It is subordinate to the
[v3.51 IK method](../KSODI_Monadic-Interaction-Coherence-IK_V351.md), the
[public concept companion](../IK_M2_AXIS_DEVIATION_DUAL_RESOLUTION_PUBLIC_CONCEPT_V351.md)
and the
[reference result contract](./IK_M2_V351_RESULT_CONTRACT_V01.md).
It does not define new formulas, thresholds, runtime fields or action
authority.

The evidence basis is the synthetic mathematical Phase A–G and window-order
reference suite. These tests establish formal distinctions under their exact
inputs and profiles. They do not establish empirical communication validity,
cross-operator commensurability, truth, intention, safety or causality.

## 2. Current v3.51 routing matrix

| ID | Investigation question | Required retained object | Calculation | Useful view | Claim boundary |
| --- | --- | --- | --- | --- | --- |
| Q01 | What is the complete observable monadic state? | complete typed and labelled `Z`, coordinate statuses, evidence, profile and provenance | none | labelled K/S/O/D/I detail or point/cloud with drill-down | not a complete account of communication, cognition or truth |
| Q02 | Where is the state on the declared weighted axis? | Q01 plus weighting-profile identity | `IK_w = w dot Z` | governance line with profile/version and reverse link | weighted projection only; not magnitude, balance or overall quality |
| Q03 | How large is the complete normalized state vector? | complete eligible numerical Z and metric identity | `IK_M2 = \|\|Z\|\|₂/sqrt(5)` | magnitude marker beside the projection | no axial direction, coordinate identity or coherence truth |
| Q04 | Where is Z on the fixed reference diagonal, and how far is it from that diagonal? | Q01 plus fixed-reference identity | `IK_ref=mean(Z)` and `AxisDev_ref` | fixed reference line, reference position and visible deviation | not active `IK_w`, error, harm or a context-free anomaly score |
| Q05 | Are the fixed-reference values internally consistent? | exact Q03/Q04 inputs, formulas and numeric policy | verify `IK_M2²=IK_ref²+AxisDev_ref²` | QA indicator | mathematical consistency, not communication quality |
| Q06 | Which coordinates produced a displayed value? | complete labelled Z and coordinate evidence | no scalar inverse exists | coordinate profile and evidence drill-down | equal scalar values do not imply equal states |
| Q07 | What changed and in which coordinate direction? | comparable ordered `Z_start`, `Z_target` and identities | signed `Delta Z` | coordinate arrows plus both endpoint states | no cause, intention or improvement claim |
| Q08 | How large was one transition? | Q07 plus declared metric | `\|\|Delta Z\|\|` with declared normalization | step-size marker linked to signed `Delta Z` | size does not identify direction or affected coordinate |
| Q09 | How much of a transition was visible on the active weighted axis? | Q07 plus stable comparable weighting profile | `Delta IK_w` | arrow on the weighted governance line | zero axial movement can hide off-axis movement |
| Q10 | Did magnitude or fixed-reference deviation change? | ordered comparable Q03/Q04 states | `Delta IK_M2`, `Delta IK_ref`, `Delta AxisDev_ref` | paired before/after markers with signed `Delta Z` | increase/decrease is diagnostic, not good/bad |
| Q11 | Where did a trajectory end relative to its beginning? | comparable ordered endpoints and identities | net `Delta Z` and net component changes | explicitly labelled start/end connector | endpoint difference does not reveal the path |
| Q12 | How much path occurred between endpoints? | all ordered comparable states and steps | `sum_j \|\|Delta Z_j\|\|` | path trace beside net displacement | no direction, elapsed-time pace or causal mechanism |
| Q13 | Did the step vector change across ordinal positions? | at least three comparable ordered states | ordinal `Delta²Z` | turn/change marker with signed-vector drill-down | not physical acceleration, rhythm or R-family Pace without a time contract |
| Q14 | Can identical scalar histories hide different coordinate paths? | complete labelled state and transition sequences | compare scalar and labelled-Z sequences separately | synchronized scalar and coordinate views | scalar equality is not trajectory identity |
| Q15 | What changes when results are derived before aggregation rather than after it? | exact window membership, complete eligible Z records, aggregator and order identity | compare `derive_then_aggregate` with `aggregate_then_derive` | paired window summaries plus member drill-down | an order gap is not automatically semantic conflict or error |
| Q16 | Should an observation open diagnostic review? | versioned trigger plus every source object needed by that trigger | declared diagnostic condition | alert as entry point into an IK-Gesamtbild and evidence drill-down | never a verdict, intervention requirement or Controller permission |

## 3. Minimum IK-Gesamtbild

Where the investigation needs a joint monadic overview, retain:

```text
IK-Gesamtbild
├── IK_w and weighting-profile identity
├── IK_M2
├── IK_ref
├── AxisDev_ref
├── complete typed Z
├── comparison/window identity
└── provenance and evidence return path
```

This is a navigable view, not a fourth measurement or total score. `IK_ref`
is a support coordinate in the fixed geometry and is not an independent
confirmation of `IK_M2` or `AxisDev_ref`.

## 4. Permitted statements and forbidden compression

| Object or view | Permitted bounded statement | Forbidden compression or inference |
| --- | --- | --- |
| complete typed Z | declared K/S/O/D/I observations are retained for one attributed unit under one profile | complete communication state, hidden cognition, truth or universal sufficiency |
| `IK_w` | position under the named weighting profile | total coherence, magnitude, relation or goal success |
| `IK_M2` | normalized Euclidean magnitude of complete numerical Z | direction, balance, quality or operator identity |
| `IK_ref` / `AxisDev_ref` | fixed-reference position and deviation | active weighted position, error, harm or universal anomaly threshold |
| IK-Gesamtbild | the required monadic views can be inspected together with reverse links | independent multiple confirmation or replacement of complete Z |
| signed `Delta Z` | labelled movement between comparable states | cause, intention or improvement |
| `\|\|Delta Z\|\|` | unsigned movement size under the declared metric | direction, affected coordinate or progress |
| net displacement | endpoint difference over the declared window | path, monotonicity or absence of detours |
| path length | accumulated movement over ordered positions | direction, elapsed-time pace or usefulness |
| ordinal `Delta²Z` | change between consecutive step vectors | physical acceleration or R-family result without a time contract |
| window-order gap | nonlinear summaries differ across the two declared processing orders | semantic conflict, incoherence or member-state inequality by itself |
| alert | a declared diagnostic condition was met | error verdict, intervention requirement or action authority |

## 5. Retention and recomputation

Preserve every non-losslessly-reconstructible base object, identity and
provenance item required by the investigation. A derived result may be
recomputed only when the exact admissible inputs, formula, profile, reference,
numeric policy and version remain available.

Persist an executed derived result when it informed a decision or when later
reconstruction would be unreliable because inputs may be deleted, formula or
evaluator versions may change, or exact execution evidence is required.

Laboratory retention may be deliberately richer than productive retention.
Productive retention remains purpose-, requirement-, access-, security- and
law-bound. Neither route authorizes indefinite retention by default.

## 6. Minimum reverse-navigation route

Every displayed value, window summary or alert must support the permitted
return path:

```text
displayed value or alert
-> exact question and view version
-> result kind, formula and numeric status
-> profile, metric, reference and window where applicable
-> ordered complete typed Z and signed transitions
-> evaluation-unit identity and source/evidence provenance
```

If a hop was not retained, the stopping point and information loss must be
named. Visual equality or scalar equality is not object equality.

## 7. Connection to R₀ and IK_rel

The enriched monadic view does not redefine the relational contracts:

```text
complete typed source-local Z_A and Z_B
├── monadic views: IK_w, IK_M2, IK_ref, AxisDev_ref
├── source-local signed movement: Delta Z_A and Delta Z_B
│   └── exact pairing and R₀ profile -> R₀ gate
└── paired Delta IK_w plus the exact compatible open R₀ gate
    └── current primary IK_rel
```

Current `R₀` consumes separately attributed comparable complete movements,
not the IK-Gesamtbild. Current primary `IK_rel` retains its own exact pairing,
shared-profile and gate conditions. `Delta IK_M2`, `Delta IK_ref`,
`Delta AxisDev_ref` or other later diagnostics must not be folded into either
contract silently.

Thus:

```text
monadic enrichment != R₀ redefinition != IK_rel redefinition
```

## 8. Evidence map

| Reference phase | Main distinction tested |
| --- | --- |
| Phase A | complete binary state grid and exact identities |
| Phase B | equal reference position with different concentration/deviation |
| Phase C | equal magnitude with different weighted position |
| Phase D | position-conditioned deviation range |
| Phase E | equal-size perturbations with different direction and effect |
| Phase F | endpoint, path and ordinal trajectory distinctions |
| Phase G | active weighting functional versus fixed-reference geometry |
| window-order fixtures | derive-before-aggregate versus aggregate-before-derive |

The reference package supports these formal distinctions only. Domain meaning,
thresholds, reference corridors and empirical utility require separately
declared instruments and validation.
