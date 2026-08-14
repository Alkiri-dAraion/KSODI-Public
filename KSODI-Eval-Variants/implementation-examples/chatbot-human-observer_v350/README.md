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

- [`KSODI Standard-Eval Layer 1 operators`](../../KSODI-Standard-Eval/Standard-Eval_v350/layer-1-operators/README.md)
- [`Standard-Eval_v350`](../../KSODI-Standard-Eval/Standard-Eval_v350/README.md)
- [`Full_v350`](../../KSODI-Full/Full_v350/README.md)

Example application layer:

- human and chatbot are treated as distinguishable interaction participants
- Standard-Eval observes monadic operator, `Z` and `IK` trajectories
- KSODI-Full opens relational observation after `R0`
- `IK_rel`, `R_geom` and `R_pace` are interpreted only under the declared
  application profile

## Public Guardrails

- Do not generalize this example into the full method.
- Do not treat infrastructure choices as canonical definitions.
- Keep customer-specific PoC work outside this public repository.
- Use this example only as a public orientation for how a canonical method
  layer can be transferred into one observable setting.

Architecture overview:

[`../../../KSODI_V350_ARCHITECTURE_ASCII.md`](../../../KSODI_V350_ARCHITECTURE_ASCII.md)
