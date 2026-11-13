# Phase 0 — frozen IK v3.51 reference basis

- Initial freeze: 2026-11-05
- Public reconciliation: 2026-11-09
- Evidence-object guard reconciliation: 2026-11-12 (no formula change)

## 1. Governed public source basis

Phase 0 fixes the mathematical and identity assumptions used by the Public
reference package. The source hashes below identify the reviewed v3.51 inputs;
they do not imply empirical validation or implementation acceptance.

| Governed source | SHA-256 |
| --- | --- |
| [`KSODI_State-Vector-Z_V351.md`](../../Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md) | `63840697ba7a5676329466dc43b90d84bca278167f0b9e9368b7b52b5c756cb9` |
| [`KSODI_Monadic-Interaction-Coherence-IK_V351.md`](../KSODI_Monadic-Interaction-Coherence-IK_V351.md) | `5e9e5c640b493c747988fdf130182efba727091d78e8e17db4084e9edd8fc8f4` |
| [`KSODI_Monadic-Interaction-Coherence-IK_Implementation-Companion_V351.md`](../KSODI_Monadic-Interaction-Coherence-IK_Implementation-Companion_V351.md) | `8dbcf9b6e4ff300a8b55eedc6dd114b3151852ed42db8ed36bb7f01424638809` |
| [`IK_M2_AXIS_DEVIATION_DUAL_RESOLUTION_PUBLIC_CONCEPT_V351.md`](../IK_M2_AXIS_DEVIATION_DUAL_RESOLUTION_PUBLIC_CONCEPT_V351.md) | `d79308b09a120c154529c895809186134443fa69dcacb0fd9231ade83dceae6b` |
| [`IK_M2_V351_RESULT_CONTRACT_V01.md`](./IK_M2_V351_RESULT_CONTRACT_V01.md) | `295550486f893a4dca32ba1b2a989ee23d39d5510146c8bafeeb88d00fd8befe` |
| [`IK_QUESTION_MEASUREMENT_VIEW_MATRIX_V351.md`](./IK_QUESTION_MEASUREMENT_VIEW_MATRIX_V351.md) | `7ac54c8766f9b021c3440ac41be741f674f2e775fe1b8dabce405db075deebe4` |
| [`IK_V351_WINDOW_AGGREGATION_ORDER_CONTRACT_V01.md`](./IK_V351_WINDOW_AGGREGATION_ORDER_CONTRACT_V01.md) | `e4c0e9d1b8187f0d3b298fc75b746eeb3c948d97021a7ef85c5617bd36a7219e` |

The result reports, generators and CSV files in this directory are
reproducible evidence under this basis. Their package inventory and hashes are
checked separately so that a generated result is not mistaken for a governing
method source.

## 2. Observation object and eligibility

Coordinate order is fixed:

```text
Z = (K,S,O,D,I)
```

Canonical numeric reference input requires:

```text
Z in [0,1]^5
all five coordinates numeric and finite
coordinate identities aligned to one source-attributed evaluation unit
complete typed Z status
```

`T_Z` and its reasons remain required provenance. Phase A uses synthetic
complete binary Z only. It does not define behavior for incomplete Z through
zero filling, imputation or automatic subset renormalization.

## 3. Frozen equal-weight reference profile

```text
profile_id = ik_equal_reference_v350
coordinate_order = (K,S,O,D,I)
w_ref = (1/5,1/5,1/5,1/5,1/5)
```

The retained profile identifier is part of the reproducible fixture. The
equal-weight vector is a transparent reference axis, not an empirical optimum
or universal domain weighting.

## 4. Frozen Phase-A calculations

For complete nonnegative Z:

```text
IK_equal(Z) = w_ref dot Z
            = (K+S+O+D+I)/5

M_1(Z)      = ||Z||_1/5
            = IK_equal(Z)

IK_M2(Z)    = ||Z||_2/sqrt(5)
            = sqrt((K^2+S^2+O^2+D^2+I^2)/5)

AxisDev_eq(Z)
            = sqrt(max(0, IK_M2(Z)^2 - IK_equal(Z)^2))
            = sqrt((1/5) * sum_X (X-IK_equal(Z))^2)
```

Within Phase A, `IK_equal` is the equal-weight form of the current `IK_w` and
is numerically identical to current `IK_ref`. `AxisDev_eq` is the fixture name
for current `AxisDev_ref` under the equal-coordinate diagonal.

`max(0, ...)` is permitted only to absorb a tiny negative floating-point
residue after the radicand has been mathematically established as
nonnegative. It must not hide invalid input or a failed identity. The centered
sum is the preferred direct computation for current `AxisDev_ref`.

`AxisDev_ref` is the population standard deviation of the five represented
coordinate values. It is descriptive within this Z representation; it does
not establish cross-operator commensurability, reliability or empirical
construct validity.

## 5. General-axis geometry used by Phase G

For one stable nonzero weight vector `w` and a declared Euclidean metric:

```text
u_w = w/||w||_2
AxisProj_w(Z) = (u_w dot Z) * u_w
AxisResidual_w(Z) = Z - AxisProj_w(Z)
AxisDev_w(Z) = ||AxisResidual_w(Z)||_2/sqrt(5)
```

The division by `sqrt(5)` is a range normalization against the containing
`[0,1]^5` cube. It does not make the value empirically calibrated. `IK_w = w
dot Z` is a linear functional; its displayed scalar is not the unscaled
orthogonal coordinate unless the relation to `u_w` and `||w||_2` is retained.

Phase G uses the following synthetic non-equal profiles as test controls, not
as method or domain weights:

```text
w_grad     = (0.30,0.25,0.20,0.15,0.10)
w_grad_rev = (0.10,0.15,0.20,0.25,0.30)
w_K_peak   = (0.60,0.10,0.10,0.10,0.10)
w_I_peak   = (0.10,0.10,0.10,0.10,0.60)
```

Each is nonnegative and sums to one. Their purpose is sensitivity,
coordinate-identity and general-axis testing. `AxisDev_w` in this fixture is
not current canonical `AxisDev_ref`; the latter always uses the fixed
equal-coordinate reference diagonal.

Every learned or adaptive-axis experiment must retain the fixed reference
geometry and must not use the same material both to fit and independently
confirm its axis.

## 6. Phase-A enumeration and ordering

Enumerate exactly all 32 binary vectors in lexicographic product order with K
as the first and I as the last coordinate:

```text
(0,0,0,0,0)
(0,0,0,0,1)
...
(1,1,1,1,1)
```

For Hamming weight `h = K+S+O+D+I`:

```text
IK_equal = M_1 = h/5
IK_M2 = sqrt(h/5)
AxisDev_eq = sqrt((h/5) * (1-h/5))
```

The last identity follows because the five coordinates are binary values
within each vector. It is a Phase-A identity, not a general formula for
continuous Z.

Expected group sizes are:

```text
h:      0  1   2   3  4  5
count:  1  5  10  10  5  1
```

## 7. Numeric and reproducibility rules

- retain exact rational or radical expressions where useful;
- emit reference CSV decimal values to 12 digits after the decimal point;
- use absolute assertion tolerance `1e-12` for independently equivalent
  floating-point expressions;
- do not round before comparisons or class assignment;
- do not clip valid values except for explicitly documented floating-point
  tolerance at a proven boundary;
- preserve full labelled Z beside every derived scalar;
- retain formula, result-kind, profile and geometry identities;
- use only the Python standard library for the reference calculators;
- keep computational values distinct from rounded human display values.

## 8. Frozen v3.51 decisions

The Public reference package uses these accepted v3.51 distinctions:

- `IK_w` remains the active declared weighted projection;
- `IK_M2` is normalized complete-vector L2 magnitude;
- `IK_ref` is position on the fixed equal-coordinate reference diagonal;
- `AxisDev_ref` is normalized deviation from that fixed diagonal;
- `IK_w`, `IK_M2`, `IK_ref` and `AxisDev_ref` are jointly inspectable but are
  never numerically added into one total IK value;
- the `IK-Gesamtbild` is a navigable view, not another calculation or
  replacement truth;
- complete typed Z, identities, statuses, profiles, geometry and provenance
  remain reconstructible;
- a fixed reference geometry remains available beside learned, adaptive or
  question-specific axes;
- raw computational values, assistive interpretation and human display remain
  distinct objects.

## 9. Open empirical and profile questions

The synthetic review establishes mathematical distinguishability,
counterexamples and reproducibility under its declared fixtures. It cannot by
itself show that a visible numerical difference corresponds to an intended
communication phenomenon.

Still requiring separate evidence or later contracts are:

- empirical commensurability and reliability across K/S/O/D/I;
- question- and domain-specific weights, corridors and thresholds;
- uncertainty propagation and evaluator disagreement;
- learned or adaptive reference geometries;
- window profiles beyond the arithmetic-mean reference case;
- point-cloud, visualization and alert contracts;
- construct, population and longitudinal validity;
- independent runtime conformance.

Any empirical arm must keep estimates, uncertainty and disagreement separate
from mathematically expected fixture values.

## 10. Phase-0 scope and completion condition

This file freezes the basis for the reproducible Phase A–G and window-order
reference package. Phase 0 is complete for that bounded purpose when:

1. the governed source hashes above match;
2. every generator reproduces its checked CSV;
3. every report links to the corresponding artifacts and states its claim
   limits;
4. the package contains no Private-only provenance or research detail;
5. link, syntax, hash and leakage checks pass as one closed package.

Completion of this reference package is not empirical validation, semantic
validation, implementation acceptance, a software release or a universal
window/profile decision.
