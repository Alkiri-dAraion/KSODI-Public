# Chatbot-Human Observer v350 Example

Status: public transfer example, not a production implementation

Purpose: show how the canonical v350 KSODI method can be instantiated for one
concrete observable setting without turning that setting into the canonical
method itself.

This example concerns a dyadic human-chatbot interaction observed by an
external Observer. It is intentionally public and minimal. It may refer to the
general infrastructure profile used in the historical KSODI work, but it does
not publish customer-specific implementation details, deployment secrets,
private prompts, proprietary evaluation data or non-public client variants.

## Transfer Boundary

Canonical method layer:

- [`KSODI-Standard-Eval Layer 1 operators`](../../../KSODI-Standard-Eval/layer-1-operators/README.md)
- [`KSODI-Standard-Eval`](../../../KSODI-Standard-Eval/README.md)
- [`KSODI-Full`](../../../KSODI-Full/README.md)

Example application layer:

- human and chatbot are treated as distinguishable interaction participants
- Standard-Eval observes monadic operator, `Z` and `IK` trajectories
- KSODI-Full opens relational observation after `R0`
- `IK_rel`, `R_geom` and `R_pace` are interpreted only under the declared
  application profile

## Required Event Separation

This example presupposes the root
[KSODI Implementation Guardrails](../../../IMPLEMENTATION_GUARDRAILS.md).

Human-side and chatbot-side contributions are retained as distinguishable
events before K/S/O/D/I evaluation. They share a conversation and may share an
exchange identifier, but they keep separate event, entity, trajectory and local
trajectory identifiers.

Minimal example:

| Contribution | Event | Trajectory | Local index | Exchange | Replies to |
| --- | --- | --- | ---: | --- | --- |
| human contribution | `H-17` | `T-H` | 17 | `X-09` | — |
| chatbot response | `M-09` | `T-M` | 9 | `X-09` | `H-17` |

The chatbot response may use the human contribution as evaluation context, but
the response remains the explicit evaluation target. Monadic differences are
calculated human-to-previous-human contribution and chatbot-to-previous-chatbot
contribution. The `exchange_id` or `reply_to_event_id` supplies the later
relational pairing.

Do not aggregate the human contribution and chatbot response into one state
vector before operator evaluation if the resulting data is intended for
source-separated trajectories, `R0`, `IK_rel` or later relational layers.

## Public Guardrails

- Do not generalize this example into the full method.
- Do not treat infrastructure choices as canonical definitions.
- Keep customer-specific PoC work outside this public repository.
- Use this example only as a public orientation for how a canonical method
  layer can be transferred into one observable setting.

Architecture overview:

[`../../../KSODI_V350_ARCHITECTURE_ASCII.md`](../../../KSODI_V350_ARCHITECTURE_ASCII.md)
