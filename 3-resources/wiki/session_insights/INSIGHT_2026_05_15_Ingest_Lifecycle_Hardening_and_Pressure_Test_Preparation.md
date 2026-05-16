# Session Insight: Ingest Lifecycle Hardening and Pressure Test Preparation

**Date**: 2026-05-15  
**Scope**: Parent ingest lifecycle, operational blocker remediation, lifecycle pressure testing, and cleanup of legacy raw staging artifacts.

## What Was Completed

1. The ingest workflow was decomposed into a full lifecycle chain:
   1. `prepare-source`
   2. `audit-promote-source`
   3. `lock-ingest-input`
   4. `ingest`
   5. `ingest-generate`
   6. `ingest-index-log`
2. `ingest.md` was refactored into orchestration-only form.
   - It now checks upstream artifacts instead of redoing upstream work.
   - It hands off atom creation and closeout to downstream workflows.
3. A parent workflow entrypoint was added:
   - `.agent/workflows/ingest-lifecycle.md`
   - This is now the single lifecycle entrypoint for official ingest runs.
4. Operational blockers in ingest-adjacent scripts were remediated:
   - `scripts/maintenance/md_auditor.py`
   - `scripts/maintenance/promote.py`
   - `.kiro/circuit_breaker.py`
   - `scripts/maintenance/synthesis_guard.py`
   - `scripts/maintenance/vram_guard.py`
5. Pressure-test infrastructure was added for the parent lifecycle:
   - `scripts/maintenance/ingest_lifecycle_check.py`
   - `scripts/maintenance/test_ingest_lifecycle_check.py`
6. Lifecycle tests were executed successfully.
   - happy path
   - blocked path
   - resume path
   - invalid mid-chain start path
   - blocked input-lock path
   - blocked generate path
   - fast-path mode reporting
7. Legacy raw outputs from the old ingest workflow were archived out of active staging.

## Critical Current Understanding

- The user should think in terms of one lifecycle entrypoint, not six unrelated workflow choices.
- Child workflows still matter because they define artifact contracts and clean resume boundaries.
- Full-chain execution is required for a fresh official ingest run.
- Mid-chain resume is allowed only when upstream artifacts already exist and are valid.
- `ARCH_TIS` is still not ready to enter `ingest`.
- The parent lifecycle checker currently resolves the real next stage for `ARCH_TIS` as:
  - `prepare-source`
- Existing `ARCH_TIS` control artifacts:
  - `STRUCTURE_ARCH_TIS.md`
  - `FIGURES_ARCH_TIS.md`
  - `MAP_ARCH_TIS.md`
  - `NAMING_LOCK_ARCH_TIS.md`
  are still draft scaffolding, not proof that upstream lifecycle gates were completed.
- One ad hoc staged chunk for `ARCH_TIS` existed from the old workflow and has now been archived to avoid contaminating the next pressure-test session.

## Verified Improvements

- `md_auditor.py` now fails with non-zero exit status when `--fix` does not produce a promotable result.
- `md_auditor.py` now resolves `verify_convert.py` from the actual skill path instead of silently skipping it due to a broken relative path.
- `promote.py` no longer blocks at import time, which allows direct testing while keeping runtime gate checks.
- `circuit_breaker.py` now supports both invocation styles:
  - `python .kiro/circuit_breaker.py <path>`
  - `python .kiro/circuit_breaker.py promote <path>`
- `synthesis_guard.py scan` now returns non-zero when issues are found.
- `vram_guard.py` now clears stale locks instead of waiting blindly until timeout.

## Pressure Test Outcome This Session

### Synthetic Lifecycle Harness

The lifecycle checker and tests passed for:
- happy path completion
- blocked audit path
- resume-to-ingest path
- invalid skip path
- blocked input-lock path
- blocked generate path
- fast-path mode reporting

### Real ARCH_TIS Artifact Check

Real-state lifecycle pressure test for `ARCH_TIS` shows:
- source evidence exists:
  - `00_Inbox/ARCH_Thinking_in_Systems.pdf`
- upstream lifecycle artifacts do not yet exist:
  - `SOURCE PREP REPORT`
  - `SOURCE AUDIT REPORT`
  - `INGEST INPUT LOCK`
- therefore the correct next stage remains:
  - `prepare-source`

This is the desired result.

The new lifecycle is correctly refusing to infer readiness from:
- draft control artifacts
- ad hoc staged chunk leftovers

## Cleanup Performed

The following legacy raw/staging artifacts were moved out of active staging and into:
- `4-archive/inbox/old_ingest_workflow_2026_05_15/`

Archived groups:
- old `Converted_Sources/OSTEP_Operating_Systems`
- old `00_Inbox/3-resources/raw_assets` spillover
- ad hoc `ARCH_TIS` staging chunk from the old workflow

Preserved on purpose:
- `00_Inbox/ARCH_Thinking_in_Systems.pdf`

This keeps the source evidence in place for the next-session pressure test while removing known staging noise.

## Recommended Next Step For Next Session

Start the real pressure test for `ARCH_TIS` from the true lifecycle entrypoint:

1. Create a real `SOURCE PREP REPORT` for `ARCH_TIS`
2. Create a real `SOURCE AUDIT REPORT`
3. Create a real `INGEST INPUT LOCK`
4. Re-run `ingest_lifecycle_check.py` on those real artifacts
5. Only then continue into `ingest`

## Guardrails For Next Agent

- Do not treat archived legacy raw outputs as active staging inputs.
- Do not reuse the archived `ARCH_TIS` chunk as evidence that lifecycle gates were passed.
- Do not start `ARCH_TIS` from `ingest` or `ingest-generate`.
- Do not infer `primary_ingest_file` from old ad hoc files without a formal `INGEST INPUT LOCK`.
- Keep `00_Inbox/ARCH_Thinking_in_Systems.pdf` as the canonical source evidence until the new lifecycle produces real upstream artifacts.
