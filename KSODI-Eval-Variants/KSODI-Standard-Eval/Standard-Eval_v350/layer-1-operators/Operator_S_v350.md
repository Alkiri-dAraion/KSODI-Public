# KSODI Operator S0 - Observable Structural Coherence v3.50

Layer: KSODI Standard-Eval operator. Static `S0` belongs to Layer 1. Operator-level Delta / Delta2, Sigma and Hangar views may observe structural movement over time. Relational patterning belongs only after the relational gate in KSODI-Full.

## 1. Definition

`S0` measures observable structural coherence of a text, signal chunk, trace or interaction unit `q`.

Structural coherence means that the unit shows visible organization, ordered parts, recognizable boundaries, sequence stability or patterning sufficient for reconstruction inside the declared evaluation scope.

`S0` is architecture-agnostic inside the v3.50 Standard-Eval frame. It can be instantiated for language, UI traces, workflow traces, packet sequences, protocol states, signal motifs, action sequences or other observable carriers where a structural detector, segmentation policy and evaluation scope are explicitly defined.

This is not the later fully meta-canonical v3.6 line for arbitrary carriers. Bit patterns, waveforms, animal communication or other distant carriers require their own detector profile before `S0` can be applied.

`S0` does not measure:

- style
- aesthetics
- personality
- content truth
- grounding or evidence support
- semantic clarity / signal density
- information impulse, novelty or update value
- resonance or relational coupling

It measures whether the observable unit has reconstructable form.

## 2. Eval Scope

`S0` is calculated per declared evaluation unit.

Inputs:

- evaluated unit `q`
- declared evaluation scope
- optional explicit structure requirements `E`
- optional structural reference profile `StructRef`
- detector version
- carrier-specific segmentation policy
- weights `alpha_S`, `beta_S`, `kappa_S`, optional `gamma_S`

The evaluation unit may be:

- an answer or text chunk
- a turn container
- a log segment
- a tool-call trace
- a protocol exchange
- a packet or event sequence
- a visual / UI workflow trace
- a signal motif or repeated pattern
- another observable carrier declared by the evaluation profile

## 3. Components

### 3.1 Explicit Structure Requirement Conformance

Let `E` be the set of explicitly expected structures.

Examples:

- JSON schema
- table
- numbered steps
- required headings
- fixed section order
- protocol field order
- required event sequence
- declared message envelope
- domain-specific motif sequence

If `E` is present:

```text
C_req(q | E)
= fulfilled_structure_requirements / expected_structure_requirements
  where expected_structure_requirements > 0
```

If `E` is empty:

```text
C_req(q | E) = not_applicable
```

This replaces the older v3.42 convention `C_F(a) = 0.5`.

Reason: absence of an explicit format requirement is not a measured half-score.
It only means that this component is not applicable. The unit may still have
observable structure through visible markers, boundaries, order or patterning.

`C_req(q | E)` is bounded where applicable:

```text
C_req(q | E) in [0, 1]
```

### 3.2 Visible Structure Markers

`M_vis(q)` measures visible structure markers or boundaries.

Examples:

- paragraphs
- sections
- headings
- list markers
- ordered steps
- field boundaries
- turn boundaries
- state transitions
- packet headers
- repeated motif boundaries
- explicitly delimited phases

```text
M_vis(q) = clip(n_markers(q) / N_S, 0, 1)
```

with:

- `n_markers(q)`: number of detected visible structure markers
- `N_S > 0`: versioned structural normalizer

If no visible-marker detector is declared for the active carrier profile:

```text
M_vis(q) = not_applicable
```

`M_vis(q)` is not a quality score. It only measures observable segmentation and
formal traceability of structure.

`M_vis(q)` must not reward marker inflation. Marker-dense but disordered units
are handled by `P_order(q | StructRef)` and the active structural profile.

### 3.3 Order / Sequence Coherence

`P_order(q | StructRef)` measures whether the visible parts of `q` follow a
recognizable order under the active structural reference profile.

The structural reference profile may be:

- explicit, from `E`
- local, from the declared evaluation task
- domain-specific, from a protocol or schema
- inferred only where the detector profile explicitly allows local pattern
  extraction

Minimal carrier-agnostic form:

```text
P_order(q | StructRef)
= ordered_observed_transitions / expected_or_detected_transitions
  where expected_or_detected_transitions > 0
```

If no order relation is applicable:

```text
P_order(q | StructRef) = not_applicable
```

This component must not be used to reward verbosity. It asks whether visible
parts are reconstructably ordered, not whether there are many parts.

### 3.4 Optional Structural Duplication / Fragmentation Penalty

`P_dup(q)` is an optional structural penalty for disruptive duplication,
fragmentation or copy-like repetition.

Default:

```text
gamma_S = 0
P_dup(q) is disabled
```

This component remains optional because repetition can have different meanings:

- structural reinforcement
- deliberate motif recurrence
- repair
- confirmation
- empty duplication
- copy artifact
- structural collapse

Repetition must not be treated as an automatic failure. Enable `P_dup(q)` only
when the evaluation profile defines which repetitions count as structurally
disruptive.

Example implementation shape:

```text
P_dup(q) = clip(disruptive_duplicate_segments / comparable_segments, 0, 1)
where comparable_segments > 0
```

Do not confuse `P_dup(q)` with `I0`. `I0` asks whether an observable
information impulse is added relative to `Ref_t`. `P_dup(q)` asks only whether
the visible structure is disrupted by duplication or fragmentation.

## 4. Minimal Static Formula

Let the active S components be:

```text
S_active(q) = {C_i(q) | C_i(q) is applicable}
```

where applicable components may include:

```text
C_req(q | E)
M_vis(q)
P_order(q | StructRef)
```

Minimal applicability-aware formula:

```text
S0(q)
= clip(
    (sum_i w_i * C_i(q)) / (sum_i w_i)
    where C_i(q) in S_active(q),
    0, 1
  )
```

If no S component is applicable:

```text
S0(q) = not_applicable
```

Start weights:

```text
alpha_S = weight(C_req)
beta_S  = weight(M_vis)
kappa_S = weight(P_order)
```

Default starting policy:

```text
alpha_S = 0.4
beta_S  = 0.3
kappa_S = 0.3
```

Weights are renormalized over applicable components. They are workbench start
values, not empirical final weights.

## 5. Extended Formula

Optional precision variant:

```text
S0_ext(q)
= clip(S0(q) - gamma_S * P_dup(q), 0, 1)
```

If `S0(q) = not_applicable`, then:

```text
S0_ext(q) = not_applicable
```

Default:

```text
gamma_S = 0
```

Use the extended variant only when structural repetition, fragmentation or
duplication is explicitly part of the evaluation task.

## 6. Interpretation

| Value | Meaning |
| --- | --- |
| high | visibly organized, reconstructably ordered and structurally coherent under the active profile |
| medium | partly structured, but with weak boundaries, partial order or incomplete conformance |
| low | weakly ordered, structurally fragmented or difficult to reconstruct |
| `not_applicable` | no declared or detectable structural component under the active profile |

Low `S0` does not mean untrue, unclear, useless or low information. It means
that the visible form is structurally weak under the active evaluation profile.

## 7. Comparability

`S0` values are comparable only under stable conditions:

- same evaluation unit type
- same carrier type or declared carrier mapping
- same structure requirements `E`
- same structural reference profile `StructRef`
- same segmentation policy
- same detector version
- same `N_S`
- same applicability policy
- same weights `alpha_S`, `beta_S`, `kappa_S`, `gamma_S`
- same choice of minimal or extended formula

Values with different active component sets must not be compared naively unless
the comparison explicitly accounts for applicability.

## 8. Orthogonality / Non-Redundancy Boundary

The five base operators are semantically distinct and functionally
non-redundant. This is not a claim of proven mathematical orthogonality.

| Operator | Measures | Difference from S0 |
| --- | --- | --- |
| `K0` | context availability and completeness | `S0` evaluates visible structural form, not whether required context exists |
| `O0` | grounding in a visible reference space | `S0` evaluates structure, not evidence support or source traceability |
| `D0` | observable clarity, discernibility and local signal acceptability | `S0` evaluates ordered form and patterning, not whether the signal is clear or dense enough |
| `I0` | observable information impulse | `S0` evaluates organization, not novelty, update-relevance or information movement |

Important boundary:

```text
coherence is not resonance
structure is not clarity
order is not information impulse
format is not grounding
```

## 9. Symbol Discipline

This version avoids global symbol collisions:

- `C_req(q | E)` replaces older `C_F(a)` where explicit requirements are meant.
- `M_vis(q)` replaces older `M(a)` where visible markers are meant.
- `P_order(q | StructRef)` names order / sequence coherence explicitly.
- `P_dup(q)` replaces older `D_dup(a)` to avoid visual confusion with operator `D0`.
- `N_S` remains the structure normalizer and must not be confused with operator `K0`.
- Do not use `R_red`, `R_frag` or similar `R` terms for structural penalties, because `R` is reserved for the relational / resonance family.

## 10. Operator-Level Delta / Sigma / Hangar Reminder

Static `S0` remains a value for one declared evaluation unit.

For a time-indexed stream, `S(t)` denotes `S0(q_t)` under the active structural
profile.

Structural persistence, repair, decay or collapse over time should be observed
through operator-level change and aggregation views rather than by silently
changing the static `S0` formula.

```text
Delta S(t) = S(t) - S(t-1)
Delta2 S(t) = Delta S(t) - Delta S(t-1)
SΣ(W) = aggregate({S(t), Delta S(t), Delta2 S(t) | t in W_app})
SΣ(Hangar) = distribution_view({S(t), Delta S(t), Delta2 S(t) | t in W_app})
```

`W_app` denotes the subset of the window where `S` is applicable under the
active structural profile.

`Delta S(t)` is only defined where both `S(t)` and the comparison value
`S(t-1)` are applicable under the same structural profile. Otherwise the delta
view records `not_applicable` or skips the pair according to the declared
window policy.

These views are useful when long-running or multi-agent interactions keep an
acceptable composite score while structural order degrades, repairs, oscillates
or collapses.

## 11. Relation To KSODI-Full

`S0`, `Delta S`, `Delta2 S`, `SΣ` and `SΣ(Hangar)` can describe monadic
structural behavior.

They do not measure relational resonance.

Relational patterning between multiple trajectories belongs after `R0`, for
example in `IK_rel`, `R_geom`, `R_pace` or later R-family views where justified.

## 12. Compact Formula Block

```text
if |E| > 0:
    C_req(q | E) = fulfilled_structure_requirements / expected_structure_requirements
else:
    C_req(q | E) = not_applicable

if visible-marker detector is declared:
    M_vis(q) = clip(n_markers(q) / N_S, 0, 1)
else:
    M_vis(q) = not_applicable

P_order(q | StructRef)
= ordered_observed_transitions / expected_or_detected_transitions
  where applicable and expected_or_detected_transitions > 0

S_active(q) = {C_i(q) | C_i(q) is applicable}

S0(q)
= clip((sum_i w_i * C_i(q)) / (sum_i w_i), 0, 1)
  for C_i(q) in S_active(q)

if S_active(q) is empty:
    S0(q) = not_applicable

S0_ext(q)
= clip(S0(q) - gamma_S * P_dup(q), 0, 1)
  where S0(q) is applicable and P_dup(q) is enabled

Delta S(t) = S(t) - S(t-1)
  where both values are applicable under the same structural profile
Delta2 S(t) = Delta S(t) - Delta S(t-1)
SΣ(W) = aggregate({S(t), Delta S(t), Delta2 S(t) | t in W_app})
SΣ(Hangar) = distribution_view({S(t), Delta S(t), Delta2 S(t) | t in W_app})
```

## 13. Variable Reference

| Variable | Semantic role |
| --- | --- |
| `q` | Evaluated text, signal chunk, trace or interaction unit |
| `E` | Explicit structure requirements |
| `StructRef` | Structural reference profile |
| `C_req(q \| E)` | Explicit structure requirement conformance |
| `M_vis(q)` | Visible structure marker score |
| `n_markers(q)` | Count of detected visible structure markers |
| `N_S` | Structural normalizer for marker counts |
| `P_order(q \| StructRef)` | Order / sequence coherence |
| `P_dup(q)` | Optional disruptive duplication / fragmentation penalty |
| `alpha_S` | Weight of explicit requirement conformance |
| `beta_S` | Weight of visible structure markers |
| `kappa_S` | Weight of order / sequence coherence |
| `gamma_S` | Weight of optional structural duplication penalty |
| `S_active(q)` | Applicable S component set |
| `S0(q)` | Static observable structural coherence |
| `S0_ext(q)` | Extended structural coherence with optional duplication penalty |
| `Delta S(t)` | First difference of S over time |
| `Delta2 S(t)` | Second difference / acceleration of S |
| `SΣ(W)` | Window aggregation of S behavior |
| `SΣ(Hangar)` | Hangar distribution view of S behavior |
