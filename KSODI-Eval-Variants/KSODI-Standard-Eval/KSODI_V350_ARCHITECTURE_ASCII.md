# KSODI v350 Architecture Sketch

Status: public orientation sketch for the current v350 direction

Purpose: show the current layer order before the full v350 Standard-Eval / Full specification is public.

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
   |   +--------------> S, Delta S, Delta2 S, SSigma, SSigma(Hangar)
   +------------------> K, Delta K, Delta2 K, KSigma, KSigma(Hangar)

        |
        v

Layer 2 - Z
  state vector over the operator values

      Z(t)
      Delta Z / Delta2 Z
      ZSigma / ZSigma(Hangar)

        |
        v

Layer 3 - IK
  monadic interaction coherence projection
  coherence is not resonance

      IK
      Delta IK / Delta2 IK
      IKSigma / IKSigma(Hangar)

        |
        v

Layer 4 - R0 / R_0 gate
  relational gate for dyadic or n-adic observation:
  are distinguishable trajectories stable enough
  for relational comparison?

        |
        v

Layer 5 - IK_rel
  relational coherence projection after stable R0

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

Layer 7 - R_pace
  readable-language or sign-visible pacing structure
  only where pacing is made visible inside the interaction

      R_pace
      R_paceSigma / R_paceSigma(Hangar)
      Delta R_pace / Delta2 R_pace

        |
        v

Layer 8 - future signal-media extension
  not active v350
  later research may include audio recordings, radio,
  Morse-like signals or wave/signal forms
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

## Active v350 Boundary

- `IK` is monadic coherence projection, not resonance.
- `R0` is the relational gate before relational projection.
- `IK_rel` is evaluated only after stable `R0`.
- `R_geom` is the current geometric core term inside the R-family.
- `R_pace` may remain only as readable-language or sign-visible pacing dynamics where explicitly defined.
- Audio, radio, Morse and wave/signal forms belong to later research, not to the active v350 core.

## Inactive Terms For v350

Do not use these as active v350 terms:

```text
R_phase
R_struc
R_struct
R_takt
R_freq
Voice overlay
Takt overlay
```

Older public files may contain these terms as historical or deprecated material. They must not be read as current v350 structure.

## Layer Files

- [Canonical v350 operator pointer](./operators_v350_canonical/README.md)
- [Layer 0 - KSODI-Light-Agent](./v350/layer-0-ksodi-light-agent/README.md)
- [Layer 1 - Operators](./v350/layer-1-operators/README.md)
- [Layer 2 - State Vector Z](./v350/layer-2-state-vector-z/README.md)
- [Layer 3 - IK](./v350/layer-3-ik/README.md)
- [Layer 4 - R0 Gate](./v350/layer-4-r0-gate/README.md)
- [Layer 5 - IK_rel](./v350/layer-5-ik-rel/README.md)
- [Layer 6 - R_geom](./v350/layer-6-r-geom/README.md)
- [Layer 7 - R_pace](./v350/layer-7-r-pace/README.md)
- [Layer 8 - Future Signal-Media](./v350/layer-8-future-signal-media/README.md)

Historical 3.3 and deprecated public drafts are preserved under
[`archive/historical-v33`](./archive/historical-v33/README.md).
