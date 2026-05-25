# ROOT_SLIMMING_CHECKLIST

Use this checklist before any physical move that reduces root clutter.

## Hard Stops

- Do not move `3-resources/`.
- Do not move raw storage directly.
- Do not move `.agent/`.
- Do not move `scripts/` until `.agent/config/paths.yaml` compatibility is implemented and regression checks pass.
- Do not move `00_Inbox/`, `1-projects/`, `2-areas/`, or `4-archive/` in the current phase.

## Preflight

- [ ] Confirm branch/worktree is not root `main`.
- [ ] List exact source path and exact target path.
- [ ] Classify each item as `generated`, `stale`, `active dependency`, or `unknown`.
- [ ] Archive first when classification is uncertain.
- [ ] Check `git status --short --ignored`.
- [ ] Check `git grep` for hard-coded references to the source path.

## Batch 1 - Config And Policy Only

- [x] Add `.code-workspace` files for IDE workspace isolation.
- [x] Add workspace-local `.vscode/settings.json` files.
- [x] Add current/future aliases to `.agent/config/paths.yaml`.
- [x] Document the physical migration plan.
- [x] Update workspace overlays with physical boundaries.

## Batch 2 - Low-Risk Runtime Cleanup

Candidate source:

```text
scratch/
```

Candidate targets:

```text
4-archive/scratch/YYYY-MM-DD_root_slimming/
workspaces/dev-lab/sandbox/
workspaces/source-lab/runs/
```

Verification:

- [ ] If Docling-related folders move, run a one-page Docling/conversion smoke test.
- [ ] Confirm no script references the moved item by exact path.
- [ ] Confirm root no longer contains the moved clutter.

Completed on 2026-05-25:

```text
scratch/ -> 4-archive/scratch/2026-05-25_root_slimming/
```

Evidence:

```text
252 moved, 0 failed
Docling smoke test returncode 0
```

## Batch 2B - Root Archive/Cache Cleanup

Completed on 2026-05-25:

```text
99_Cleanup_Rollback/ -> 4-archive/cleanup_rollback/2026-05-25_root_slimming/
.venv_virtualenv_failed/ -> 4-archive/runtime_env/2026-05-25_root_slimming/
skills_backup.zip -> 4-archive/backups/2026-05-25_root_slimming/
.pytest_cache/ -> 4-archive/cache/2026-05-25_root_slimming/
.agent_busy -> 4-archive/state_markers/2026-05-25_root_slimming/
.deepeval/ -> 4-archive/cache/2026-05-25_root_slimming/
```

Do not move these root folders in this cleanup phase:

```text
.codex/
.continue/
.deepeval/
.kiro/
.obsidian/
.venv/
.vscode/
```

Reason: they are active tool/runtime/config surfaces or have live references.

## Batch 3 - Learning Surface Migration

Candidate source:

```text
5-learning/
```

Candidate target:

```text
workspaces/learning/dashboard/
```

Prerequisites:

- [x] Move tracked learning dashboard files into `workspaces/learning/dashboard/`.
- [x] Update `scripts/learning/export_epub.py`.
- [x] Update `scripts/learning/learning_manager.py`.
- [x] Update links in learning dashboard and learning paths.
- [x] Keep a legacy note in `.agent/config/paths.yaml`.

Completed in worktree branch `agent/multi-workspace-isolation`; not yet merged to root `main`.

## Batch 4 - Code Plane Migration

Candidate sources:

```text
tools/
libs/
tests/
scripts/
```

Candidate targets:

```text
workspaces/dev-lab/tools/
workspaces/dev-lab/libs/
workspaces/dev-lab/tests/
workspaces/dev-lab/scripts/
```

Prerequisites:

- [ ] Decide whether each path is tracked, ignored, or local-only.
- [ ] Migrate commands to resolve through `.agent/config/paths.yaml`.
- [ ] Update docs and rules that currently say `scripts/`.
- [ ] Run script regression checks before and after move.

Compatibility scaffolds added:

```text
workspaces/dev-lab/scripts/.gitkeep
workspaces/dev-lab/tools/.gitkeep
workspaces/dev-lab/libs/.gitkeep
workspaces/dev-lab/tests/.gitkeep
```

Do not populate these folders by moving root code until compatibility is implemented.

Worktree import completed:

```text
workspaces/dev-lab/libs/
workspaces/dev-lab/tools/
workspaces/dev-lab/tests/
libs/__init__.py  # compatibility shim only
```

Import exclusions:

```text
**/.env
**/*.log
**/__pycache__/
**/*.pyc
tools/cache/
tests/pdf_convert_benchmark/output/*
```

Root `libs/`, `tools/`, and `tests/` are still present in `D:\NoteBookLLM_Br` because they are local-only ignored paths and `libs` has live import references. After this branch is reviewed, root `libs/` can be reduced to the shim only; root `tools/` and `tests/` can be archived or moved after comparing against `workspaces/dev-lab/`.
