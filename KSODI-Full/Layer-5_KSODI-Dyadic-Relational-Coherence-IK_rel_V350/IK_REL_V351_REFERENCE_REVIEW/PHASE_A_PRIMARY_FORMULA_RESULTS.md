# Phase A — primary IK_rel formula, range and projection collisions

Basis: [Phase 0 frozen basis](./PHASE_0_FROZEN_BASIS.md)

## 1. Reproducible artifacts

- [`calculate_phase_a_primary_reference.py`](./calculate_phase_a_primary_reference.py)
  generates both dependency-free fixture tables and checks their invariants;
- [`phase_a_primary_grid.csv`](./phase_a_primary_grid.csv) contains the 25
  algebraic pairs over `{-1,-1/2,0,1/2,1}^2`;
- [`phase_a_projection_collisions.csv`](./phase_a_projection_collisions.csv)
  contains six complete labelled-Z trajectory pairs consistent with a
  synthetic open R0 handoff at `theta_R0_stable=1/2`.

Stable generated hashes after the repeated assertion run:

```text
phase_a_primary_grid.csv
  SHA-256 442c5f578015dd26cc1b8ad9715518b79f0213c20fd7abf0397a5e7c999da55b

phase_a_projection_collisions.csv
  SHA-256 cd869dd1b6bc1ea3dbb53536a71bd2d41317056e66891ed9d65111e734435628
```

The algebraic grid and the R0-consistent fixtures answer different questions.
No claim is made that every algebraic grid point passes one common positive R0
threshold.

## 2. Algebraic formula result

For:

```text
g_move = |Delta IK_w,A - Delta IK_w,B|
C_move = 1 - g_move/2
```

the enumerated grid verifies:

```text
g_move in [0,2]
C_move in [0,1]
C_move(a,b) = C_move(b,a)
```

The five exact score classes are:

| `g_move` | `C_move` | ordered grid pairs |
| ---: | ---: | ---: |
| `0` | `1` | 5 |
| `1/2` | `3/4` | 8 |
| `1` | `1/2` | 6 |
| `3/2` | `1/4` | 4 |
| `2` | `0` | 2 |

Under the transparent Phase-A test value `epsilon_move=0`, the exact `(0,0)`
pair is `not_applicable` by the current joint-zero policy. Its raw formula
value remains recorded as `1` but is not a valid current primary IK_rel method
result. The other 24 rows are numeric under this isolated status test.

## 3. What symmetry does and does not mean

The numeric expression is symmetric under operand exchange. The method object
is not thereby an unordered or merged relation:

```text
C_move(Delta IK_A, Delta IK_B)
= C_move(Delta IK_B, Delta IK_A)

ordered_dyad_AB != ordered_dyad_BA
pairing/provenance_AB != pairing/provenance_BA
```

The same value preserves neither role direction, event identity, source-local
predecessor nor causal/response order.

## 4. Projection collisions

The six full-Z fixtures demonstrate four collision classes:

1. Positive movement on K and positive movement on S both project to
   `Delta IK_w=1/5`; current primary `C_move=1` although the complete movement
   vectors differ.
2. The corresponding negative coordinate movements also produce
   `Delta IK_w=-1/5` and `C_move=1`.
3. Two disjoint zero-sum coordinate transfers both produce `Delta IK_w=0`.
   Their raw formula value is `1`, but the current joint projected-zero policy
   makes primary IK_rel `not_applicable` despite substantial complete-Z
   movement.
4. Complete stillness on one side and a zero-sum coordinate transfer on the
   other also collapse to joint projected zero and `not_applicable`.

Two further dyadic pairs produce the same `C_move=9/10` through differently
placed projected movements. Therefore the primary score identifies an
absolute projected movement gap class, not the two absolute movements or their
complete coordinate paths.

## 5. R0 feasibility boundary

The algebraic endpoint:

```text
Delta IK_w,A = 1
Delta IK_w,B = -1
C_move = 0
```

requires, under equal complete weights and `[0,1]^5`, maximal oppositely
directed coordinate movement. Both L1 drifts equal `1`, so current canonical:

```text
R0 = 1 - (1+1)/2 = 0
```

This can pass only a threshold profile that opens at zero. Consequently:

> The algebraic range of the IK_rel formula is not automatically the observed
> post-gate range under a selected positive R0 threshold.

Phase D must calculate the joint feasible region under explicit R0 norm and
threshold profiles. Phase A does not use this dependency to redefine either
formula.

## 6. Bounded finding

The current primary formula is correctly normalized and symmetric as a scalar
absolute-gap compatibility function. It deliberately compresses:

- absolute projected movement levels;
- coordinate identity and complete movement direction;
- role/order identity;
- within-axis path and off-axis movement;
- R0 feasibility under a concrete threshold.

These losses do not make the formula incorrect. They delimit its valid claim:

> After the exact compatible open gate and all identity/status checks, current
> primary IK_rel describes compatibility of two paired movements along one
> shared declared `IK_w` axis.

It does not describe complete-vector movement compatibility, relation strength,
agreement, response, coupling, resonance, shared direction toward a target or
successful communication.

### 6.1 Question-led diagnostic bundle

The narrow primary value should not be asked to carry distinctions that its
projection intentionally removes. The v3.51 diagnostic bundle
therefore keeps the following readings adjacent without combining them into a
new universal scalar:

```text
IK_rel
|- axial movement compatibility
|- raw Delta IK_w,A / Delta IK_w,B
|- complete Delta Z_A / Delta Z_B
|- componentwise paired differences
`- R_geom direction diagnostic, only if separately selected and valid
```

Componentwise differences require an explicit order/sign convention and retain
both labelled source vectors. `R_geom` remains a separate staged branch; its
absence, invalidity or non-selection is never recoded as zero and it is not a
silent component of current `IK_rel`.

This is a first diagnostic bundle, not yet the answer for every investigation.
Every later bundle must state the question it serves, the claim it permits,
its selected components and statuses, and what remains outside its scope.

### 6.2 Three distinct result consumers

"Machine distinguishability" is not one undifferentiated requirement:

1. the deterministic Observer calculation path requires typed raw operands,
   identities, profiles, statuses, formulas and provenance and must not
   calculate from presentation rounding;
2. an assistive evaluating LLM requires a bounded, semantically explained and
   reconstructible context package with question, evidence, status,
   uncertainty and explicit claim limits; its interpretation remains a
   separately attributable output and never rewrites the method result;
3. a human governance or expert view requires an understandable projection,
   declared rounding and a visible return path to the complete typed basis.

These are three projections of attributable evidence, not three competing
method authorities.

## 7. Contract conclusions

- Algebraic-grid coverage and post-`R_0` feasibility are separate checks.
- Projected joint zero remains `not_applicable` while complete-Z movement
  remains diagnostically visible.
- Every numeric primary result retains raw `Delta IK_w,A/B` and complete
  `Delta Z_A/B` references.
- The six collision fixtures form the Phase-A implementation-conformance
  reference basis.
