# KSODI v350 Eval Architecture Sketch

Status: public orientation sketch for the v350 research architecture

Current release boundary: the public v3.5 Standard-Eval release extends through
Layer 3, the monadic interaction-coherence projection `IK`, which closes
Standard-Eval. `R0` is released separately as KSODI-Full Layer 4, and `IK_rel`
is released separately as KSODI-Full Layer 5. Later R-family layers remain
visible here as staged research structure; their presence in this sketch does
not mark them as released.

Purpose: show the intended layer order shared by the Standard-Eval and Full
research lines while keeping release status separate from architectural
orientation.

Position: this sketch sits at the `KSODI-Eval-Variants` root because the layer
order crosses the public Standard-Eval folder and the R-family / KSODI-Full
research boundary. `KSODI Standard-Eval` and `KSODI-Full` are public-facing
variant names; the underlying architecture must keep the method boundary
between operator observation, state vector, coherence projection, relational
gate and R-family observation visible.

Boundary:

- `KSODI-Light-Agent` is Layer 0 and belongs to the local agent / prompt side.
- `KSODI Standard-Eval` maps the complete monadic Observer line:
  `K/S/O/D/I -> Z -> IK`. It ends with `IK`, and the current public release
  includes that complete line.
- After `Z`, the architecture branches. `KSODI-Full` evaluates `R0` from
  distinguishable `Z`-trajectories in parallel to monadic `IK`. Stable `R0`
  gates `IK_rel`, followed by the further R-family. `R0`, `IK_rel` and the
  further R-family are not part of Standard-Eval. Public folder presence does
  not imply release. `R0` is released separately as the public Layer 4 gate;
  `IK_rel` is released separately as public Layer 5; later R-family layers
  remain staged.
- Pace, Voice and rhythm/timing belong to an optional overlay research layer.
  Historical `Takt` labels are not active v3.5 core terms. These overlays are
  not prerequisites for the monadic or relational core.

```text
KSODI-Light-Agent

Layer 0 - KSODI-Light
  reflective working agreement / prompt orientation
  may run on its own agent where available
  no external Observer calculation by itself

        |
        v

Observer architecture

Layer 1 - Operators
  K0  S0  O0  D0  I0
   |   |   |   |   |
   |   |   |   |   +--> I, Delta I, Delta2 I, ISigma, ISigma(Hangar)
   |   |   |   +------> D, Delta D, Delta2 D, DSigma, DSigma(Hangar)
   |   |   +----------> O, Delta O, Delta2 O, OSigma, OSigma(Hangar)
   |   +--------------> S, optional S0_ext/P_dup, Delta S, Delta2 S, SSigma, SSigma(Hangar)
   +------------------> K, Delta K, Delta2 K, KSigma, KSigma(Hangar)

        |
        v

Layer 2 - Z
  state vector over the operator values

      Z(t)
      Delta Z / Delta2 Z
      ZSigma / ZSigma(Hangar)

        |-------------------------------|
        v                               v

Layer 3 - IK                    Layer 4 - R0 / R_0 gate
  monadic interaction             gate based on Z-trajectories:
  coherence projection            are distinguishable trajectories
  for each party / entity          stable enough for relational
  coherence is not resonance      comparison?

      IK
      Delta IK / Delta2 IK
      IKSigma / IKSigma(Hangar)

                                        |
                                        v

Layer 5 - IK_rel
  dyadic / n-adic relational coherence projection
  only inside the relational branch after stable R0

      IK_rel
      Delta IK_rel / Delta2 IK_rel
      IK_relSigma / IK_relSigma(Hangar)

        |
        v

Layer 6 - R_geom
  geometric coupling in KSODI state space

      R_geom
      R_geomSigma / R_geomSigma(Hangar)
      Delta R_geom / Delta2 R_geom

        |
        v

Layer 7 - optional Pace overlay research
  readable-language or sign-visible pacing structure
  only where pacing is made visible and explicitly defined

      R_pace
      R_paceSigma / R_paceSigma(Hangar)
      Delta R_pace / Delta2 R_pace

        |
        v

Layer 8 - optional Voice / rhythm/timing and signal-media research
  future-work line associated with v3.60
  may include voice, timing, audio recordings, radio,
  Morse-like signals or other wave/signal forms
  not part of the current public v3.5 method release
```

## Scope And Application Selection

Not every application needs every aggregation, Hangar view, drift value or
second-order drift value. Select the active observations layer by layer for the
use case.

For many ordinary applications, the main observation focus may be:

- `Z(t)` and its corridor behavior
- `IK`
- `IK_rel` where relational comparison is justified
- the relevant R-family variants
- `O0` / reference-space visibility where grounding matters

In adversarial, safety-sensitive or drift-sensitive settings, operator-level
drift may become important as well. For example, `I` stagnation, bursts or
oscillation may reveal attack patterns, prompt injection pressure, repetitive
collapse or missing update-relevant information.

Decision rule: do not enable Sigma / Hangar / Delta / Delta2 everywhere by
default. Decide per layer, per application field and per concrete use case.

## Sigma And Hangar Views

`Sigma` means window aggregation inside a given layer. It is not a separate
main layer in the architecture.

`Sigma(Hangar)` means a distribution or comparison view over windows,
trajectories, aggregated values or point-cloud-like observation objects. The
Hangar is therefore an observation view for comparing patterns, not an
additional metaphysical space and not a second architecture.

In practical terms:

- a single value describes a current state;
- a sequence describes movement;
- a window describes a pattern;
- a Hangar view describes where such patterns sit inside an observation space.

This supports corridor monitoring, anomaly detection, distribution comparison
and later governance-oriented review without treating single outputs as
isolated events.

## Weighted Axis Modes

For `IK` and R-family variants, two weighting modes should remain visible:

1. Fixed directed operator axes in the normalized variant, with each operator
   initially readable as a `0.2` contribution in the five-operator state space.
2. Interaction-derived axes, where rough corridors are learned or calibrated
   after Mode 1 observation and then adapted to the application field and use
   case.

## Future Work: Controller Architecture

Name not final.

The controller architecture must be separated more precisely than the minimal
v350 Observer architecture. The controller must not collapse back into the
Observer.

Future direction:

- the governance team defines permitted corridors before deployment, matched
  to the application case
- layer feedback can be routed automatically to agents only within those
  approved corridors
- Observer outputs should not be fed back in a way that lets the Observer
  influence itself without a separate control boundary

## Core Sequence And Optional Research Boundary

- The current public v3.5 method release includes the complete monadic
  Standard-Eval line `K/S/O/D/I -> Z -> IK` and the separately released
  KSODI-Full `R0` gate and `IK_rel`.
- `IK` is the intended monadic coherence projection, not resonance, and closes
  Standard-Eval.
- `R0` is evaluated from `Z` and runs in parallel to monadic `IK`; it is not
  downstream of `IK`.
- `IK_rel` belongs inside the dyadic / n-adic branch and is evaluated only
  after stable `R0`.
- `R0`, `IK_rel` and the further R-family are not part of Standard-Eval. `R0`
  and `IK_rel` are released separately; later R-family layers remain staged.
- `R_geom` remains a research term inside the further R-family.
- Pace, Voice and rhythm/timing remain optional overlay research. Historical
  `Takt` labels are not active v3.5 core terms. These overlays are neither core
  prerequisites nor part of the current public v3.5 method release.
- The optional signal-media Observer work is associated with the v3.60
  future-work line.

## Deprecated Identifiers

Do not use these legacy identifiers as current v3.5 core terms:

```text
R_phase
R_struc
R_struct
R_takt
R_freq
```

Voice, rhythm/timing and Pace as optional overlays must not be conflated with
those legacy R-family identifiers. Older public files may contain `Takt` or the
deprecated terms as historical material.

## Layer Files

- [Layer 0 - KSODI-Light-Agent](./KSODI-Light-Agent_v350.md)
- [Layer 1 - Operators](./KSODI-Standard-Eval/Standard-Eval_v350/layer-1-operators/README.md)
- [Layer 2 - State Vector Z](./KSODI-Standard-Eval/Standard-Eval_v350/layer-2-state-vector-z_v350/README.md)
- [Layer 3 - IK](./KSODI-Standard-Eval/Standard-Eval_v350/layer-3-ik_v350/README.md)
- [Layer 4 - R0 Gate](./KSODI-Full/Full_v350/layer-4-r0-gate/README.md)
- [Layer 5 - IK_rel](./KSODI-Full/Full_v350/layer-5-ik-rel/README.md)
- [Layer 6 - R_geom](./KSODI-Full/Full_v350/layer-6-r-geom/README.md)
- [Layer 7 - Optional Pace Overlay Research](./KSODI-Full/Full_v350/layer-7-r-pace/README.md)
- [Layer 8 - Optional Voice / Rhythm-Timing and Signal-Media Research](./KSODI-Full/Full_v350/layer-8-future-signal-media/README.md)
- [Shared Sigma / Hangar Method Note](./Hangar_350.md)

Historical 3.3 and deprecated public drafts are preserved under
[`KSODI-Standard-Eval/archive_historical-v33`](./KSODI-Standard-Eval/archive_historical-v33/README.md).
Historical v3.42 Observer assets are preserved under
[`archive_assets_historical-observer-v342`](./archive_assets_historical-observer-v342/README.md).
