# Phase H — Frozen v3.51 Basis

## 1. Source identity

The formula basis was first published in Public commit
`0a9238268a24dbad782061680d619c6752f5550e` dated 2026-11-10. The exact source
bytes used after the external-review reconciliation are identified below; the
companion change adds a fixture-vocabulary mapping. The 2026-11-12 method
reconciliation adds an evidence-object compatibility guard. Neither change
alters a frozen formula.

| Governed source | SHA-256 |
| --- | --- |
| `KSODI_Relational-Gate-R_0_V351.md` | `e7ee08362506a2098debbe74d191d01f0d8ad4975c3004df7c703f54143bb614` |
| `KSODI_Relational-Gate-R_0_Implementation-Companion_V351.md` | `f2f263e507fadaeb9e3e59e2798335d609862cf2948483b7960a3c158f010425` |
| `KSODI_Dyadic-Relational-Coherence-IK_rel_V351.md` | `6b69140ebf2c78002324354bc80b2f0a8f27ba3c7e0d207cc7478f15a41551b8` |
| `KSODI_Dyadic-Relational-Coherence-IK_rel_Implementation-Companion_V351.md` | `8f594992b4e35bb61fcbcff7fd4b8859357571cf806745fcc7b035537f396c82` |

These hashes bind the review to exact Public bytes. The companions remain
subordinate to their method files.

## 2. Frozen formulas

For complete five-coordinate movement `Delta Z_E`:

```text
d_E,L1 = (1/5) * sum_X |Delta X_E|
d_E,L2 = sqrt((1/5) * sum_X Delta X_E^2)
d_E,L1^g = sum_X g_X |Delta X_E|,  sum_X g_X = 1

R_0 = clip(1 - (d_A + d_B)/2, 0, 1)
gate = open iff R_0 >= theta_R0_gate_open_min

Delta IK_w,E = sum_X w_X Delta X_E
C_move = clip(1 - |Delta IK_w,A - Delta IK_w,B|/2, 0, 1)
```

The test threshold `theta_R0_gate_open_min = 0.8`, positive epsilon values,
L2 profile, coordinate-weight controls and alternative IK-weight control are
synthetic fixtures. They are not empirically calibrated defaults.

## 3. Profile boundary

- `equal_coordinate_normalized_l1_v351` is the canonical R₀ reference used in
  this review.
- `equal_coordinate_normalized_l2_test_control` is a separate norm-family
  control.
- `g_k_focus_normalized_l1_test_control` and
  `g_s_focus_normalized_l1_test_control` are fixed coordinate-weight controls.
- `ik_w_equal_coordinate_reference` is the frozen reference projection for
  these fixtures.
- `ik_w_k_focus_test_control` is an alternative named projection control.

No result from one profile may be compared or substituted as though it came
from another profile without retaining both identities.

## 4. Epsilon and calibration boundary

The exact method epsilon is zero. Every positive epsilon test records:

- epsilon kind and value;
- parameter origin;
- calibration status;
- calibration evidence reference when empirical calibration is claimed.

The synthetic positive-epsilon fixtures use
`set_not_empirically_calibrated`. A structurally complete calibration-record
test checks only field presence; it is not evidence that the synthetic value
is empirically calibrated.

## 5. Diagnostic boundary

The optional candidates

```text
max_abs_coordinate_delta_E
max_abs_coordinate_ids_E
```

retain the largest absolute coordinate movement and every tied coordinate
identity. They do not alter `R_0`, gate state, coordinate weights, `IK_w` or
`IK_rel`. The complete signed `Delta Z_E` remains authoritative.

## 6. Finding classes

Phase H uses four distinct review findings:

| Finding | Meaning |
| --- | --- |
| `contract_confirmed` | the declared contract behaves as expected |
| `profile_sensitive_expected` | a declared profile change changes the result without contradiction |
| `diagnostic_information_loss` | a valid projection compresses distinctions retained in richer evidence |
| `contract_contradiction` | calculated behavior conflicts with the frozen contract and may reopen v3.51 |

The generator's declared expectations cover the first three classes. The
fourth is reserved for an independent comparison between the method contract
and generated or runtime evidence; a self-expecting generator cannot establish
its absence merely by reproducing its own expected labels.

## 7. Reopening rule

Phase H reopens v3.51 only when it finds a contract contradiction or a
material loss for a standard question that is safely and simply repairable
without inventing an unreviewed profile. Context-, question-, resolution-,
expectation- or infrastructure-dependent tolerability remains Future Work.
