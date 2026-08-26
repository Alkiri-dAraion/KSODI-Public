# KSODI — Observability and the Separate Controlled-Action Boundary

This file is conceptual boundary orientation, not a canonical operator or
relational method, implementation profile, governance policy or Controller
specification. Its examples are illustrative and do not validate a deployment.

## 1. Why the boundary matters

KSODI produces structured observations about attributable events,
source-local trajectories and, where separately admitted, relational patterns.
An observation can inform a later governed decision. It does not become an
instruction merely because it is numeric, unusual or outside a declared
corridor.

The earlier label “From Observability to Controlled Action” could be read as a
method-internal transition or guaranteed progression. The v3.50 contract is
stricter: observability and controlled action are separated by governance,
authority and a distinct Controller decision.

```text
observable events
  -> KSODI Observer records
  -> governed interpretation / policy check
  -> separate authorized Controller decision
  -> permitted action or explicit no-action
  -> new attributable events available for later observation
```

The return path creates new evidence. It does not prove that the decision was
correct, that KSODI caused an improvement or that an earlier observation was
complete.

## 2. Responsibility and authority map

| Component | May do | Must not be inferred |
| --- | --- | --- |
| KSODI Observer | emit typed, attributable method results and diagnostics under declared profiles | decision, command, intervention, truth or intent |
| Governance policy | define permissible uses, evidence requirements, corridors, escalation paths and accountable roles | that a KSODI value alone supplies the policy |
| Controller | validate an authorized input envelope and select a permitted response or no-action | that it is part of a KSODI formula |
| Human or executing system | approve or perform an authorized action and record the outcome | that execution validates the observation or policy |

Human responsibility is not removed by automation. A deployment must state
who owns profile choice, policy approval, Controller behavior, exception
handling, audit review and shutdown authority.

## 3. What the KSODI layers contribute

KSODI-Light is a local prompt-facing orientation layer using disclosed 0–5
working values. KSODI-Standard-Eval is the formal monadic line:

```text
K/S/O/D/I -> typed Z_A(k_A) -> monadic IK_A(k_A)
```

Its valid formal numeric results use `[0,1]` under declared profiles. Light
values and formal values are not direct rescalings and must not be converted
into one another mechanically.

KSODI-Full begins with separately declared relational observation. `R_0`
receives distinguishable typed Z movements plus an explicit pairing or
constellation map. A numeric R0 result has a separate gate state:

```text
numeric R0 at/above its valid threshold -> open
numeric R0 below its valid threshold    -> closed
non-numeric R0                          -> not_evaluable
incomparable input                      -> no valid R0 result
```

An open R0 gate means only that one declared stability/comparability contract
admits a compatible relational calculation. It is not permission to act and
is not evidence of relation, coupling, resonance, agreement or success.

Current dyadic `IK_rel` additionally requires explicit dyadic pairing and an
open numeric canonical complete dyadic R0 gate under the exact required
profile. Reduced or n-adic R0 does not open that branch.

## 4. Observer output is not a command

The following observations may be reportable under their own contracts:

- a typed non-numeric operator, Z, IK or R0 result;
- a numeric value or comparable source-local difference;
- a numeric R0 result with open or closed gate state;
- a window coverage or gate-open rate with a valid positive denominator;
- a governed corridor departure or other separately defined diagnostic.

None of them independently selects an action. In particular:

- numeric zero is not a substitute for missing or incomparable evidence;
- a closed or non-evaluable R0 gate does not automatically pause a system;
- an open R0 gate does not authorize relational scoring or intervention beyond
  a compatible downstream method and separate governance policy;
- a high or low IK, R0 or IK_rel value does not establish correctness,
  desirability, safety or intent.

## 5. Minimum controlled-action envelope

A Controller-facing integration should receive an explicit envelope rather
than an unlabelled score:

```text
ControlledActionInput {
  observer_record_ids
  method_and_profile_versions
  source_event_and_trajectory_scope
  result_statuses_and_values
  comparability_and_coverage_evidence
  policy_id_and_version
  authorized_controller_id
  permitted_action_set
  human_approval_requirement
  freshness_and_expiry
  provenance_and_audit_reference
}
```

Before any action, the Controller validates identity, policy authority,
profile compatibility, evidence freshness, coverage, permitted action set and
required human approval. Invalid, stale, incomparable or unauthorized input
does not become a default KSODI action. A governance policy may specify
logging, clarification or human review, but that response is external to the
KSODI calculation.

## 6. Bounded customer-support example

Suppose an external Observer reports a source-attributed sequence with
declining numeric coverage and several `not_observable` operator results. The
Observer records those facts and their reasons. It does not conclude that the
agent is wrong or select a remedy.

A separately approved support policy might require a human review when the
evidence envelope satisfies its own conditions. An authorized Controller may
then create a review task. The reviewer may request missing order evidence,
clarify the desired outcome, continue without intervention or select another
permitted response.

Any subsequent interaction is evaluated as new attributable evidence. A later
change in KSODI values does not by itself prove that the intervention caused
the change or that the outcome was beneficial.

## 7. Feedback and anti-circularity controls

When Observer outputs can influence the observed system, the implementation
must preserve:

- separate Observer and Controller identities and logs;
- the exact policy and evidence envelope used for each decision;
- attributable records for Controller commands and system responses;
- delay, cooldown and rate-limit policies outside method formulas;
- protection against a Controller rewriting the evidence it consumed;
- explicit evaluation of feedback effects as new observations;
- independent human override, audit and shutdown paths where required.

Without this separation, a system may optimize against its own observer,
confuse intervention effects with organic trajectory movement or create an
unreviewable feedback loop.

## 8. Non-claims and release boundary

This note does not claim that:

- autonomous systems always require a full KSODI Observer;
- KSODI proves correctness, truth, safety, alignment or successful action;
- an R0 or later relational result is an action threshold;
- one universal Controller policy fits every domain;
- monitoring alone prevents drift or harm.

Production use requires domain-specific validation, data governance, security,
fairness review, accountable authority and appropriate human oversight. This
orientation note changes no KSODI formula and creates no Controller canon. It
does not authorize software merge, deployment, threshold choice, intervention,
a GitHub tag, GitHub Release, DOI or Zenodo artifact.
