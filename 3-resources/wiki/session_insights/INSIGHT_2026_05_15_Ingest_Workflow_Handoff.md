# Session Insight: Ingest Workflow Handoff

**Date**: 2026-05-15  
**Scope**: Workflow architecture for ingest, naming drift control, and MCP operating modes.

## What Was Completed

1. MCP profile switching was hardened and documented.
   - Script supports: `full`, `micro`, `vault`, `dev`, `ingest`
   - Current canonical config path is documented in `AGENTS.md`
2. `AGENTS.md` was expanded with:
   - `MICRO` mode for small local models
   - `Automation MCP Policy`
   - `MCP Switching Operations`
   - `Recommended MCP Sets`
   - `Ingest Source Policy`
3. Ingest design was hardened in `.agent/workflows/ingest.md` and supporting docs.
4. Three workflow prerequisites were created:
   - `.agent/workflows/prepare-source.md`
   - `.agent/workflows/audit-promote-source.md`
   - `.agent/workflows/lock-ingest-input.md`
5. Supporting ingest design docs were created/updated:
   - `.agent/docs/INGEST_MAP_NAMING_LOCK_SPEC.md`
   - `.agent/docs/PENDING_PROJECTS.md`
6. Golden test case control artifacts for `ARCH_TIS` were created:
   - `1-projects/STRUCTURE_ARCH_TIS.md`
   - `1-projects/FIGURES_ARCH_TIS.md`
   - `1-projects/MAP_ARCH_TIS.md`
   - `1-projects/NAMING_LOCK_ARCH_TIS.md`

## Critical Current Understanding

- `ingest.md` should not start from raw file preparation anymore.
- Correct workflow chain is now:
  1. `prepare-source`
  2. `audit-promote-source`
  3. `lock-ingest-input`
  4. `ingest`
- `ingest.md` should become orchestration-only in the next session.
- `PDF` is evidence, not the default ingest-reading file.
- A source must have exactly one `primary_ingest_file` per ingest run.
- Large PDFs must be handled as:
  - `STRUCTURE` first
  - `FIGURES` second when visuals matter
  - chunked evidence extraction after that
- Chunking priority is:
  1. chapter boundary first
  2. section boundary second
  3. page window last

## Known Unresolved Issues

1. `ingest.md` is still too large and mixes orchestration with detailed policy.
2. `ARCH_TIS` control artifacts are useful but should be treated as draft operational scaffolding, not final extracted truth.
3. `primary_ingest_file` for `ARCH_TIS` has not been locked yet.
4. Existing drift remains in the wiki/index for `ARCH_TIS` aliases such as:
   - `SOURCE_SYS_ARCH_TIS`
   - `SOURCE_SYS_Thinking_in_Systems`
   - `CONCEPT_SYS_ARCH_TIS_*`
   - `ENTITY_SYS_ARCH_TIS_*`

## Recommended Next Step For Next Session

Do **not** continue ingest generation yet.

Next agent should do this in order:

1. Refactor `.agent/workflows/ingest.md` into orchestration-only form.
   - Keep phase order
   - Add precheck against:
     - `SOURCE PREP REPORT`
     - `SOURCE AUDIT REPORT`
     - `INGEST INPUT LOCK`
   - Remove duplicated detail already covered by the new workflow chain and specs
2. After workflow refactor, determine and lock the real `primary_ingest_file` for `ARCH_TIS`.
3. Only then continue with valid `Phase 0` execution.

## Guardrails For Next Agent

- Do not treat previous ad hoc reads of the PDF as valid official extraction.
- Do not create more `ARCH_TIS` atoms before `primary_ingest_file` is locked.
- Do not reintroduce `PREFIX` as a parallel naming anchor.
- Do not let `page-first` chunking replace `chapter/section-first` chunking.
