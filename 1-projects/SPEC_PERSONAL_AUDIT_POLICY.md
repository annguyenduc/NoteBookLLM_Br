# SPEC - Personal Audit Policy

Source context: `NoteBookLLM_Br` personal vault promote workflow  
Scope owner: `@pm`  
Status: `DRAFT`  
Phase target: `Post-HMAC-contract blocker remediation`  

## 1. Problem Statement

Current promote gating assumes one strict audit contract:
- valid audit stamp
- origin under `00_Inbox`
- freshness check
- HMAC signature verification

For a personal vault, this can become operationally heavy when:
- audit semantics evolve faster than promote verification
- local workflow changes create temporary HMAC contract mismatch
- the user needs a practical path to promote personally audited content without weakening all other gates

The current blocker demonstrates this:
- chunk audit now passes under `verify_scope: chunk`
- staged file under `00_Inbox` still cannot promote
- reason is not content failure, but HMAC contract mismatch between audit and promote

## 2. Objective

Introduce an explicit audit policy layer for promote:
- `strict`
- `personal`

This must unblock personal vault promote while preserving the option to retain strict governance.

## 3. Scope

This spec covers:
- audit policy selection for promote
- rules for `strict` vs `personal`
- CLI and environment contract for audit policy
- minimum required audit stamp fields

## 4. Non-Goals

This spec does not:
- change promote routing
- change origin gate
- change folder promote semantics
- introduce `raw_ingest/[source_id]`
- change `ingest.py --package`
- change atomization flow
- start package-native ingest
- remove the audit gate entirely

## 5. Policy Modes

### 5.1 Strict

Purpose:
- preserve current high-governance behavior

Rules:
- require valid audit stamp
- require origin under `00_Inbox`
- require freshness check
- require HMAC verification
- require status to be `PASSED`
- require score to meet threshold
- require `verify_result` to be acceptable
- require `verify_scope` to be valid

### 5.2 Personal

Purpose:
- support personal-vault operation when audit has passed but HMAC alignment is temporarily not available or not desired

Rules:
- require valid audit stamp
- require origin under `00_Inbox`
- require freshness check
- do not require HMAC verification
- require status to be `PASSED`
- require score to meet threshold
- require `verify_result` to be `PASS`
- require `verify_scope` to be valid

Important:
- personal mode skips mandatory HMAC verification
- personal mode does not skip the audit gate
- personal mode does not weaken origin validation

## 6. Default Policy

Recommended default:
- `strict`

Recommended local override for this repo when operating as a personal vault:
- `AUDIT_POLICY=personal`

Rationale:
- preserves backward-safe governance
- allows explicit local relaxation without silently changing security semantics for all workflows

## 7. CLI Contract

Preferred CLI:

```text
python .kiro/circuit_breaker.py promote "<path>" --audit-policy personal
```

Promote wrapper should pass the selected policy through to `promote.py`.

Fallback environment contract:

```text
AUDIT_POLICY=personal
```

Resolution rule:
1. CLI flag wins if present
2. environment variable is fallback
3. default is `strict`

Allowed values:
- `strict`
- `personal`

## 8. Required Audit Stamp Fields

Regardless of policy, promote must require:
- `audit_stamp: true`
- `audit.score`
- `audit.date`
- `audit.status`
- `audit.verify_result`
- `audit.verify_scope`

Valid `verify_scope` values:
- `full-source`
- `chunk`
- `package`

Additional rule for `personal`:
- `verify_result` must be `PASS`

Additional rule for `strict`:
- `verify_result` must satisfy current verification acceptance rules
- HMAC must validate

## 9. Acceptance Criteria

### 9.1 Strict Acceptance

Strict mode is acceptable only if:
- existing HMAC behavior remains enforced
- existing promote routing remains unchanged
- origin gate under `00_Inbox` remains enforced

### 9.2 Personal Acceptance

Personal mode is acceptable only if:
- a file with PASSED audit stamp can promote without HMAC match
- the file still must have `status: PASSED`
- score still must meet threshold
- `verify_result` must be `PASS`
- `verify_scope` must be one of `full-source|chunk|package`
- origin gate still must require `00_Inbox`

## 10. Risks

- personal mode could be overused and become an implicit global default
- mixed policy use could confuse debugging if the active policy is not visible
- relaxing HMAC may hide stamp tampering in local workflows

## 11. Mitigations

- keep default policy as `strict`
- require explicit CLI or env override for `personal`
- log active audit policy during promote
- keep strict mode fully available for high-governance runs

## 12. Recommended Design Direction

This spec prefers:
- retain strict mode
- add personal mode
- do not remove HMAC support entirely

Rationale:
- preserves existing governance option
- avoids turning one local blocker into a permanent global downgrade
- matches personal vault needs without opening Phase B or routing changes

## 13. Required Handoff

After spec approval:
- handoff to `@engineer` to implement policy selection in `.kiro/circuit_breaker.py` and `scripts/maintenance/promote.py`

Implementation boundary for later handoff:
- no workflow redesign
- no folder promote changes
- no ingest changes

## 14. Definition of Done

This spec is done when:
- `strict` and `personal` policy behavior are defined clearly
- CLI and env selection rules are explicit
- required audit stamp checks are explicit
- origin gate and audit gate remain preserved
- boundaries against Phase B stay intact
