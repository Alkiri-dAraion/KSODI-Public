# Phase G — stable non-equal profiles and general-axis geometry

Date: 2026-11-05

Basis: frozen Phase-0 reference profile. Its final Public basis record is
added after all reference blocks and source hashes are fixed.

Machine-readable binary grid:
[`phase_g_general_axis_binary_grid.csv`](./phase_g_general_axis_binary_grid.csv)

Machine-readable selected cases:
[`phase_g_general_axis_cases.csv`](./phase_g_general_axis_cases.csv)

Reproducer:
[`calculate_phase_g_general_axis_reference.py`](./calculate_phase_g_general_axis_reference.py)

CSV SHA-256:

```text
binary grid: e2380fe45e83d27b389618cab271f68720cc00ad9efb101e15149ff3d1f63cbf
cases:       141613114eeab0fdda6adebb096a9ca32febdcad1a12e7e66da1b4143101a198
```

## 1. Question and design

Phase G asks whether the equal-profile joint view generalizes cleanly when
`IK_w` uses a stable non-equal weight profile, and which geometric objects
must remain distinguishable from the fixed v3.51 reference geometry.

The independent standard-library calculation applies five profiles to all 32
binary states and ten selected continuous/edge cases:

```text
w_equal    = (0.20,0.20,0.20,0.20,0.20)
w_grad     = (0.30,0.25,0.20,0.15,0.10)
w_grad_rev = (0.10,0.15,0.20,0.25,0.30)
w_K_peak   = (0.60,0.10,0.10,0.10,0.10)
w_I_peak   = (0.10,0.10,0.10,0.10,0.60)
```

These are synthetic sensitivity controls, not domain weights or empirical
preferences. Every output row retains complete labelled Z and exact profile
weights.

## 2. General orthogonal decomposition

For one stable non-zero `w`, define:

```text
u_w = w / ||w||_2
IK_w(Z) = w dot Z
A_w(Z) = (u_w dot Z) / sqrt(5)
       = IK_w(Z) / (||w||_2 * sqrt(5))
AxisDev_ray,w(Z) = ||Z - (u_w dot Z)u_w||_2 / sqrt(5)
IK_M2(Z) = ||Z||_2 / sqrt(5)
```

Then the verified geometric identity is:

```text
IK_M2(Z)^2 = A_w(Z)^2 + AxisDev_ray,w(Z)^2
```

The raw displayed `IK_w` is not generally the normalized orthogonal axial
component `A_w`. Therefore this substitution is generally false:

```text
IK_M2^2 != IK_w^2 + AxisDev_ray,w^2
```

It works under the frozen equal profile because
`||w_equal||_2 = 1/sqrt(5)`, so `A_w = IK_equal`. With non-negative weights
that sum to one, that norm equality is the equal-weight boundary; the
non-equal controls have larger weight norms.

All 210 generated rows satisfy the correct Pythagorean identity within the
frozen `1e-12` absolute tolerance.

## 3. Weighting functional and geometric ray are not automatically one method object

`IK_w = w dot Z` defines a linear functional. Geometrically, `w` is normal to
its equal-value hyperplanes. Reusing the same vector as a ray through the
origin is an additional modelling decision, not a consequence of weighted
summation alone.

The upper cube corner makes the distinction visible:

| Profile | `IK_w(1,1,1,1,1)` | `A_w` | `IK_M2` | `AxisDev_ray,w` |
| --- | ---: | ---: | ---: | ---: |
| equal | `1` | `1` | `1` | `0` |
| gradient | `1` | `0.942809041582` | `1` | `0.333333333333` |
| K-peak | `1` | `0.707106781187` | `1` | `0.707106781187` |

Thus a complete all-one state has maximal `IK_w=1` under every normalized
weight profile but lies away from every non-equal weight ray. The same effect
appears at the balanced half-state: `IK_w=IK_M2=0.5` for every profile while
ray deviation rises from `0` under equal weights to `0.353553390593` under a
peak profile.

This is mathematically consistent. It exposes a semantic choice between
deviation from the **weight ray**, deviation from a fixed diagonal and another
declared affine/reference corridor. The v3.51 method selects the fixed
equal-coordinate diagonal; the other geometries remain separately named
research possibilities rather than implicit meanings of `AxisDev_ref`.

## 4. Profile-aligned states verify the ray calculation

The selected continuous controls include states proportional to each
non-equal weight vector. Their `AxisDev_ray,w` is exactly zero within the
numeric contract under the matching profile. For example:

```text
Z_grad = (0.60,0.50,0.40,0.30,0.20)
       = 2 * w_grad
```

Under `w_grad`:

```text
IK_w = 0.45
A_w = IK_M2 = 0.424264068712
AxisDev_ray,w = 0
```

The raw weighted score still differs from the normalized axial magnitude.
This confirms that the discrepancy is a scale/object distinction rather than
an implementation error.

## 5. Coordinate identity and reversed profiles

For `Z_K=(1,0,0,0,0)` and `Z_I=(0,0,0,0,1)`:

- the equal profile gives identical `IK_w`, `IK_M2` and axis deviation;
- the gradient and reversed-gradient profiles exchange the K/I readings;
- the K-peak and I-peak profiles exchange the corresponding peak readings;
- `IK_M2=1/sqrt(5)` remains invariant because the state magnitude is unchanged.

The weighted projection therefore makes declared coordinate preference
visible, while complete labelled Z remains necessary to distinguish what
produced the scalar. Reversal symmetry is a useful fixture for later
implementation conformance.

## 6. State movement and axis movement must remain separate

For the fixed asymmetric state

```text
Z = (0.8,0.6,0.4,0.2,0.1)
```

changing only the profile produces:

| Profile | `IK_w` | `A_w` | `IK_M2` | `AxisDev_ray,w` |
| --- | ---: | ---: | ---: | ---: |
| equal | `0.42` | `0.42` | `0.491934955050` | `0.256124969497` |
| gradient | `0.51` | `0.480832611207` | `0.491934955050` | `0.103923048454` |
| reversed gradient | `0.33` | `0.311126983722` | `0.491934955050` | `0.381051177665` |
| K-peak | `0.61` | `0.431335136524` | `0.491934955050` | `0.236537523450` |
| I-peak | `0.26` | `0.183847763109` | `0.491934955050` | `0.456289381862` |

No state movement occurred: complete Z and `IK_M2` are unchanged. The change
belongs to the observation profile/reference geometry. A learned or adaptive
axis must therefore retain axis versions and decompose state movement from
axis movement before any trajectory, corridor or alert claim.

## 7. Consequences for IK-Gesamtbild, R_0 and IK_rel

The human-facing `IK-Gesamtbild` remains viable, but a non-equal profile must
not draw raw `IK_w` and `AxisDev_ray,w` as if they were the two orthogonal
components of `IK_M2`. It must either:

1. display both raw `IK_w` and the separately named normalized axial component
   `A_w`; or
2. use a different explicitly declared reference geometry whose coordinate is
   directly compatible with the displayed axis value.

Current `R_0` remains unchanged because it consumes complete comparable
signed `ΔZ` under its own norm and gate profile. Current primary dyadic
`IK_rel` remains unchanged because it compares paired raw `ΔIK_w` under
the exact same stable monadic profile after the compatible open `R_0` gate.
Phase G strengthens the requirement that both sides use the exact same `w`
and profile version; it does not turn `A_w`, `IK_M2` or ray deviation into
implicit `IK_rel` components.

## 8. Geometric alternatives exposed by Phase G

The mathematics exposes at least three distinguishable geometric routes:

| Route | Meaning | Consequence |
| --- | --- | --- |
| weight-ray deviation | distance from the line spanned by `w` | preserve `A_w`; do not store it as `AxisDev_ref` |
| fixed-reference deviation | distance from a separately fixed diagonal/reference axis while `IK_w` remains a weighting functional | two independent profile identities must be retained |
| question-specific reference geometry | distance from a declared affine line, curve, corridor or distribution | requires question, estimation, uncertainty and empirical validation |

These routes need not be mutually exclusive as separately declared diagnostic
profiles, but they must not share one unlabeled `AxisDev_w` field.

The reviewed v3.51 method decision is:

- v3.51 selects the fixed equal-coordinate diagonal as the stable geometric
  reference, independently of the active weighting profile;
- its derived reference coordinate is `IK_ref=mean(Z)`;
- `AxisDev_ref` denotes normalized distance from that fixed diagonal;
- weight-ray deviation remains a separately named research object for
  questions where proportionality to `w` is substantively intended;
- question-specific affine, corridor or distribution geometry requires a
  separate question, profile, evidence and validation contract.

This decision is sufficient to continue the v3.51 result and visualization
contract without asserting that later reference geometries are invalid.

## 9. Bounded Phase-G finding

Under stable non-equal weights, the raw projection `IK_w`, normalized
geometric axial magnitude `A_w`, total state magnitude `IK_M2` and
weight-ray deviation are distinct objects. The correct orthogonal identity
uses `A_w`, not raw `IK_w`. Treating the IK weight vector as a geometric
reference ray is an explicit modelling choice. Preserve complete Z, both state
and axis/profile identity, and do not interpret profile change as state
movement.

## 10. Reopening and research boundary

The exact `IK_ref`/`AxisDev_ref` result identity, technical names and
range/status/comparability rules are defined by the reviewed v3.51 method and
result contract. Later weight-ray and question-specific geometry must retain
their own question, profile, evidence and version boundaries.

No production implementation, empirical corpus or external numeric package
was used.

Compatibility note: the historical Phase-G fixture field `axis_dev_w`
denotes normalized distance from the active weight ray. For a non-equal
profile it is not the v3.51 `AxisDev_ref` result and must not be relabelled as
such. The generated field remains unchanged for exact reproducibility.
