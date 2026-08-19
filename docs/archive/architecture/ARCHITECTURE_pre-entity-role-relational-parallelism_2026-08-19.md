# KSODI Architecture

Status: public root orientation sketch for first-time readers, crawlers and AI
agents. The canonical detailed architecture sketch is
[KSODI_V350_ARCHITECTURE_ASCII.md](./KSODI_V350_ARCHITECTURE_ASCII.md).
The cross-layer data, trajectory and composition conditions are defined in the
[KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md).

## Short Version

All five Layer-1 operators are strictly monadic and source-attributed. Each
static value belongs to one identified event in one declared trajectory, and
temporal comparisons use only comparable positions within that same
trajectory. A declared context or reference space may include visible material
from outside the trajectory without merging sources or creating a relational
value.

```text
e_A(k)
  -> K_A / S_A / O_A / D_A / I_A
  -> Z_A(k)
       |-> IK_A(k)
       +-> R0(A,B,...) -> IK_rel -> R-family
```

`A` and `B` remain distinguishable through the operators, `Z` and monadic
`IK`. Relational interpretation begins only at the separately declared `R0`
gate.

KSODI v3.5 uses one canonical Layer 0-8 map. `KSODI-Light` is the local
prompt-facing entry layer, not the whole or larger KSODI system.
Standard-Eval and KSODI-Full are the observer-oriented method layers for
observable interaction states.

Current public boundary:

- Standard-Eval is public through Layer 3: `K/S/O/D/I -> Z -> IK`.
- `R0` is public separately as KSODI-Full Layer 4.
- `IK_rel` is public separately as KSODI-Full Layer 5.
- `R_geom`, `R_pace` and later signal-media work remain staged unless their own
  release status says otherwise.

After `Z(t)`, the architecture branches: `IK` is the monadic projection, while
`R0` is evaluated in parallel as the relational comparability gate over
distinguishable `Z`-trajectories. `R0` is not calculated from `IK`.

Layer-1 operators may be inspected individually through monadic trajectory,
projection or aggregation views. After stable `R0`, explicitly defined
operator-specific relational comparison views may be added. These are optional
diagnostics and are neither complete `Z`, canonical `IK`, `IK_rel` nor
resonance. A one-operator projection must not be reported as full `IK`, and one
operator-specific relational signal is not by itself an R-family result.

## Layer Map

| Layer | Variant | Component | Status | Meaning |
| --- | --- | --- | --- | --- |
| 0 | [KSODI-Light](./KSODI-Light/README.md) | Local reflective layer | public | Reflective working agreement for learning, prompting, training and agent guidance. |
| 1 | [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md) | K/S/O/D/I operators | public | Observable context, structure, grounding, clarity and information impulse. |
| 2 | [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md) | `Z(t)` / `Z_vec` | public | State vector over the five operator values. |
| 3 | [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md) | `IK` | public | Monadic interaction-coherence projection; closes Standard-Eval. |
| 4 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | `R0` / `R_0` gate | public | Relational comparability gate over distinguishable `Z`-trajectories. |
| 5 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | `IK_rel` | public | Relational coherence projection after stable `R0`. |
| 6 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | `R_geom` | staged | Geometric coupling in KSODI state space. |
| 7 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | `R_pace` | staged | Optional pacing overlay where pacing dynamics are explicitly defined. |
| 8 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | Future signal-media layer | future research | Voice, rhythm/timing, audio, radio, Morse-like or other signal-media work; historical `Takt` labels are not active v3.5 terms. |

## Handshake and Coupling Boundary

`R0` is the SYN/ACK-like Handshake boundary of relational observation. The
Observer declares the pair or group; `R0` checks whether its distinguishable
trajectories are stable enough for relational observation. It is not coupling
and does not mark the beginning of coupling.

Strong observable coupling requires sustained high `IK_rel` together with
sustained high branch-specific R-family evidence across a declared observation
window. Coupling strength does not determine intended direction, desirability
or alignment. See the
[R0 relational gate](./KSODI-Eval-Variants/KSODI-Full/Full_v350/layer-4-r0-gate/R0_Relational-Gate.md)
and [Hangar note](./KSODI-Eval-Variants/Hangar_350.md).

## Method Position

KSODI is a baseline radar for observable communication. It does not replace
communication theory, signal theory, AI observability, explainability,
governance frameworks, safety methods or domain-specific analysis.

KSODI adds a layered method for asking whether an event or interaction remains
observable, reconstructable, coherent, comparable and safely connectable across
time.

## Minimal Flow

```text
Layer 0: KSODI-Light
   local reflection / prompt guidance

Layer 1: K/S/O/D/I
   observable operator values

Layer 2: Z(t)
   state vector

After Z(t), KSODI branches:

   Layer 3: IK
      monadic coherence projection

   Layer 4: R0
      relational comparability gate

Only after stable R0:

   Layer 5: IK_rel
      relational coherence projection

Layer 6+: R_geom -> R_pace -> future signal-media work
   staged R-family research
```

For choosing the right entry point, see
[Which KSODI Variant Do I Need?](./WHICH_KSODI.md). Before translating this
topology into storage, evaluation or code, read the
[KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md).
