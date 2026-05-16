# PLAN — Run Package Ingest Runtime

Related spec: `1-projects/SPEC_RUN_PACKAGE_INGEST.md`  
Owner: `@pm`  
Execution target: `@engineer` after approval  
Status: `DRAFT`

## 1. Decision

Implement `Phase A` only.

Phase A outcome:
- introduce `runs/` as transient ingest runtime workspace
- add stateful orchestration scripts
- generate `manifest.md` and `outline.md`
- stop before major downstream refactor

This is the minimum change that improves runtime durability without breaking current ingest governance.

## 2. Why Phase A First

Advantages:
- solves the main operational pain now: long-run state loss
- keeps compatibility with current `audit -> promote -> raw_ingest -> ingest.py`
- avoids mixing orchestration redesign with package-native atomization redesign

Deferred to Phase B:
- `raw_ingest/[source_id]/` package layout
- folder promotion semantics
- `ingest.py --package`

## 3. Deliverables

Required deliverables:
- `runs/.gitkeep`
- `runs/README.md`
- `scripts/ingest/ingest_runner.py`
- `scripts/ingest/build_manifest.py`
- `scripts/ingest/build_outline.py`

Likely supporting updates:
- `WORKSPACE_OVERVIEW.md`
- `.agent/workflows/ingest-lifecycle.md`
- `.agent/skills/wiki-hd-convert/SKILL.md`
- `AGENTS.md`

Optional in Phase A if needed:
- `scripts/ingest/__init__.py`
- `scripts/ingest/helpers.py`

## 4. Execution Phases

### Phase 1 — Contract Freeze

Goal:
- lock terminology and boundaries before code

Tasks:
- confirm `runs/` is transient, not knowledge storage
- confirm Phase A stop stage is `READY_FOR_AUDIT`
- confirm downstream remains file-oriented for now

Exit criteria:
- spec approved
- no ambiguity on current vs deferred scope

### Phase 2 — Filesystem Skeleton

Goal:
- create stable run package layout

Tasks:
- create `runs/`
- add `runs/README.md`
- define canonical run directory naming
- define initial `state.json` schema

Exit criteria:
- empty run package can be created deterministically

### Phase 3 — Manifest Builder

Goal:
- produce whole-source inventory artifact

Tasks:
- scan converter output
- detect chunk filenames and page ranges
- write deterministic `manifest.md`
- record engine, chunk size, source metadata

Exit criteria:
- one run can always produce a manifest without LLM

### Phase 4 — Outline Builder

Goal:
- recover document structure before atomization

Tasks:
- parse headings from chunk files
- map sections/chapters to page ranges and chunk files
- write deterministic `outline.md`

Exit criteria:
- output gives enough whole-document context for later chunk processing

### Phase 5 — Runner Orchestration

Goal:
- move execution state out of IDE session

Tasks:
- implement `INIT -> CONVERT -> BUILD_MANIFEST -> BUILD_OUTLINE -> PACKAGE_REPORT -> READY_FOR_AUDIT`
- persist stage changes in `state.json`
- support `--resume`
- support `--mode dry-run|review|apply`

Exit criteria:
- interrupted run can be resumed from filesystem state

### Phase 6 — Documentation and Workflow Wiring

Goal:
- make repo doctrine consistent with the new runtime

Tasks:
- update `WORKSPACE_OVERVIEW.md`
- add rule in `AGENTS.md` for PDF > 50 pages
- update `wiki-hd-convert` usage notes
- clarify Antigravity role as review/control surface

Exit criteria:
- docs no longer imply IDE-context execution for long ingest runs

### Phase 7 — Pressure Test

Goal:
- verify runtime stability on real PDFs

Tasks:
- small PDF happy path
- medium PDF resume path
- large PDF interruption + resume path
- confirm no premature writes to `raw_ingest`

Exit criteria:
- Phase A survives interruption and resume on real data

## 5. Work Breakdown

### Workstream A — Runtime State

Files:
- `scripts/ingest/ingest_runner.py`
- `runs/README.md`

Focus:
- state transitions
- run directory lifecycle
- resume logic

### Workstream B — Source Context Artifacts

Files:
- `scripts/ingest/build_manifest.py`
- `scripts/ingest/build_outline.py`

Focus:
- deterministic source inventory
- structure recovery

### Workstream C — Governance Alignment

Files:
- `AGENTS.md`
- `WORKSPACE_OVERVIEW.md`
- relevant workflow docs

Focus:
- make runtime expectations explicit
- prevent direct chunk-to-atom misuse

## 6. Open Decisions For Engineer

Engineer may implement, but should not redefine:
- exact `state.json` schema fields beyond the minimum contract
- exact regex set for heading detection
- exact converter adapter abstraction for `fast/structured/ocr`

Engineer must not change in Phase A:
- `promote.py` semantics to folder-level package promote
- `ingest.py` input contract
- Human Gate / synthesis rules

## 7. Success Metrics

Minimum success:
- 1 interrupted large PDF run can resume without depending on IDE memory
- `manifest.md` and `outline.md` exist for every Phase A run
- current raw audit/promote flow still works unchanged

Preferred success:
- source context is visibly clearer during review
- fewer manual interventions in long ingest runs
- fewer context-loss errors in chunk handling

## 8. Known Tradeoffs

Accepted tradeoffs in Phase A:
- duplicate storage between `Converted_Sources` and `runs/`
- still file-oriented downstream ingest
- no folder-package promote yet

These are acceptable because they reduce immediate implementation risk.

## 9. Next Step After Approval

If approved, `@engineer` should implement in this order:
1. `runs/` skeleton and `README`
2. `build_manifest.py`
3. `build_outline.py`
4. `ingest_runner.py`
5. doc updates
6. pressure tests

