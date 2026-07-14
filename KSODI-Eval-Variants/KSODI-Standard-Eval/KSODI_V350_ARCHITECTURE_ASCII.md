# KSODI v350 Architecture Sketch

Status: public orientation sketch for the current v350 direction

Purpose: show the current layer order before the full v350 Standard-Eval / Full specification is public.

```text
Layer 1 - KSODI-Light
  reflective working agreement / prompt orientation
  may run on its own agent where available
  no external Observer calculation by itself

        |
        v

Layer 2 - Operators and state vector
  K0  S0  O0  D0  I0
   |   |   |   |   |
   |   |   |   |   +--> I, Delta I, Delta2 I, ISigma, ISigma(Hangar)
   |   |   |   +------> D, Delta D, Delta2 D, DSigma, DSigma(Hangar)
   |   |   +----------> O, Delta O, Delta2 O, OSigma, OSigma(Hangar)
   |   +--------------> S, Delta S, Delta2 S, SSigma, SSigma(Hangar)
   +------------------> K, Delta K, Delta2 K, KSigma, KSigma(Hangar)
              |
              v
            Z(t)
              |
              +--> Delta Z / Delta2 Z
              +--> ZSigma / ZSigma(Hangar)

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

Layer 5 - IK_rel and R_geom
  IK_rel:
    relational coherence projection after stable R0

  R_geom:
    geometric coupling in KSODI state space
    R_geomSigma / R_geomSigma(Hangar)
    Delta R_geom / Delta2 R_geom

        |
        v

Layer 6 - R_pace
  readable-language or sign-visible pacing structure
  only where pacing is made visible inside the interaction

      R_pace
      R_paceSigma / R_paceSigma(Hangar)
      Delta R_pace / Delta2 R_pace

        |
        v

Layer 7 - future signal-media extension
  not active v350
  later research may include audio recordings, radio,
  Morse-like signals or wave/signal forms
```

## Active v350 Boundary

- `IK` is monadic coherence projection, not resonance.
- `R0` is the relational gate before relational projection.
- `IK_rel` is evaluated only after stable `R0`.
- `R_geom` is the current geometric core term inside the R-family.
- `R_pace` may remain only as pacing dynamics where explicitly defined.
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
