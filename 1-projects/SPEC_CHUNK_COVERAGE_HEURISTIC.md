# SPEC - Chunk Coverage Heuristic

Source context: `NoteBookLLM_Br` chunk-scope audit pipeline  
Scope owner: `@pm`  
Status: `DRAFT`  
Phase target: `Post-stabilization audit heuristic remediation`  

## 1. Problem Statement

Current chunk-scope audit uses a page coverage heuristic that treats low section-marker density as a hard failure signal.

Observed failure:
- `RAW_2026-05-15_ARCH_Thinking_in_Systems_CH01_SEC03_P034-041.md`
- expected page range: `34-41`
- actual outcome: `FAIL`
- current reason: `chunk page coverage below threshold`

Why this is wrong:
- the chunk has valid source trace
- the chunk has strong text retention
- the chunk has extracted images
- the chunk resolves cleanly to a known manifest entry
- the chunk only has sparse headings/section markers

This means the heuristic is currently overfitting to heading density rather than actual evidence of chunk completeness.

## 2. Objective

Redefine chunk-scope coverage so it becomes evidence-based rather than section-marker-based.

The new heuristic must:
- stop hard-failing multi-page chunks solely because they have few headings
- treat section marker density as a supporting signal only
- keep hard failures for genuinely broken chunk evidence

## 3. Scope

This spec covers:
- chunk-scope audit coverage heuristic only
- failure versus warning thresholds for chunk completeness
- signals used by `md_auditor.py` when `--verify-scope chunk`

## 4. Non-Goals

This spec does not:
- change full-source audit semantics
- change package-scope audit interface
- change personal promote policy
- change `promote.py`
- change `ingest.py`
- change folder promote semantics
- start Phase B

`SPEC_PERSONAL_VERIFY_RESULT_POLICY.md` remains deferred.

## 5. Current Heuristic Failure

Current logic effectively treats:
- number of `##` section markers
- relative section-marker density per expected page range

as a primary coverage metric.

This creates a false hard-fail on chunks that are:
- structurally sparse
- image-heavy
- narrative-heavy with long continuous prose
- multi-page but intentionally grouped under one section heading

## 6. Design Principle

Chunk coverage must be based on evidence of meaningful content presence, not just heading frequency.

Rule:
- section marker density is a secondary signal
- section marker density alone is never sufficient for hard failure

## 7. Evidence-Based Coverage Model

Chunk-scope audit should evaluate a weighted set of signals:

### 7.1 Primary Signals

These are strong signals of valid chunk coverage:
- chunk page range resolves successfully
- manifest entry matches chunk file
- source trace exists
- Markdown body has substantial text for the expected page range
- extracted images and/or asset references are consistent with the chunk

### 7.2 Secondary Signals

These may influence `WARN`, but should not independently force `FAIL`:
- low section marker density
- sparse headings
- low explicit page marker count
- uncertain image count when text retention is otherwise healthy

## 8. Hard-Fail Conditions

Chunk-scope audit may hard-fail only when one or more of these is true:
- page range cannot be resolved
- manifest range mismatch exists
- required source trace is missing
- body text is near-empty for the expected page range
- broken links or assets are critical
- verification finds severe evidence that the chunk does not correspond to its declared range

Low heading density alone must not be a hard-fail condition.

## 9. Warning Conditions

Chunk-scope audit should produce `WARN` rather than `FAIL` when:
- heading density is low
- section marker count is sparse for a multi-page chunk
- page-structure evidence is weaker than ideal but text retention is healthy
- image certainty is incomplete but not contradictory
- chunk appears plausible but structurally under-signaled

## 10. Target Case

### 10.1 Case Under Test

File:
- `RAW_2026-05-15_ARCH_Thinking_in_Systems_CH01_SEC03_P034-041.md`

Current failure:
- `chunk page coverage below threshold`

Expected after fix:
- `PASS` or `WARN`

Forbidden after fix:
- hard `FAIL` solely because only two section markers exist for an eight-page chunk

## 11. Acceptance Criteria

This spec is satisfied only if future implementation can demonstrate:
- `CH01_SEC03_P034-041` no longer hard-fails only because section markers are sparse
- a chunk with strong text retention and valid range mapping can end in `PASS` or `WARN`
- hard-fail remains reserved for evidence-backed integrity failures
- short sparse chunks and multi-page sparse chunks are distinguished correctly
- section marker density is treated as secondary evidence, not a primary fail gate

## 12. Risks

- relaxing the heuristic too much could allow weak chunks to pass
- warning thresholds may become noisy if evidence weighting is not explicit
- image-heavy chunks may still need special-case handling later

## 13. Mitigations

- keep hard-fail list explicit and narrow
- prefer text/range/source evidence over structure density
- degrade to `WARN` before `FAIL` when evidence is mixed but not broken
- keep future heuristic tuning scoped to chunk audit only

## 14. Required Handoff

After spec approval:
- handoff to `@engineer` to adjust `md_auditor.py` chunk coverage logic

Implementation boundary:
- do not change promote policy
- do not change routing
- do not change package-native ingest

## 15. Definition of Done

This spec is done when:
- the heuristic problem is isolated clearly
- hard-fail versus warning conditions are explicit
- the target case is named and bounded
- boundaries against personal-policy changes and Phase B remain intact
