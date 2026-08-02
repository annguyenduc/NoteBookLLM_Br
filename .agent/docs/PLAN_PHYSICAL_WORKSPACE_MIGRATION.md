# PLAN_PHYSICAL_WORKSPACE_MIGRATION

> Mục tiêu: giảm tải root `D:\NoteBookLLM_Br` bằng cấu trúc vật lý theo workspace, nhưng không làm vỡ ingest, scripts, registry, hoặc canonical vault.

## Routing Decision

```yaml
ROUTING_DECISION:
  cwd_context: "vault_root"
  selected_workspace: "NONE"
  mode: "physical-migration-plan"
  reason: "Root is too large; AN wants daily work to happen by opening workspace-specific folders."
  loaded_overlay: "NONE"
  action_type: "write-preview-artifact"
  write_artifact: "YES"
  canonical_write: "NO"
  ingest_lifecycle: "NO"
```

## Current Evidence

- `AGENTS.md` freezes these root paths during the current phase: `00_Inbox/`, `1-projects/`, `2-areas/`, `3-resources/`, `4-archive/`, `.agent/`, `scripts/`.
- `.agent/config/paths.yaml` also lists the same frozen paths and says they must not move until scripts are migrated to the registry and regression checks pass.
- `scripts/` has many hard-coded references across `.agent/`, `WORKSPACE_OVERVIEW.md`, README, rules, and scripts themselves.
- `runs/` is part of official ingest runtime contracts.
- `5-learning/` is referenced by `scripts/learning/export_epub.py`, `scripts/learning/learning_manager.py`, and learning dashboard artifacts.
- `scratch/` is large and mostly untracked runtime/debug material; it is the safest first candidate for root cleanup after archive-first verification.

## Target Topology

```text
D:\NoteBookLLM_Br\
  AGENTS.md
  CONTINUITY.md
  README.md
  .agent\
  .git\
  .vscode\

  00_Inbox\        # root anchor: intake and staged source boundary
  1-projects\      # root anchor: source registry, source-scoped plans, governance
  2-areas\         # root anchor: durable areas
  3-resources\     # root anchor: canonical vault; never nested under workspaces
  4-archive\       # root anchor: archive and rollback storage
  scripts\         # root anchor until path registry migration is complete

  workspaces\
    learning\
      notes\
      flashcards\
      questions\
      outputs\
      preview\
      dashboard\       # future home for 5-learning replacement, after compatibility

    source-lab\
      inbox\
      converted\
      runs\            # preview/source-lab runs only; official ingest root runs remains until migrated
      reports\

    dev-lab\
      scripts\         # future production code plane, after compatibility
      tools\
      libs\
      tests\
      sandbox\
      reports\

    research-lab\
      notes\
      comparisons\
      sources\
      reports\
```

## Migration Strategy

### Track A - Stabilize And Slim Root Without Breaking Paths

This track is safe-first and mostly additive.

1. Keep all frozen anchors in root.
2. Keep `scripts/` in root until commands and docs can resolve script paths through `.agent/config/paths.yaml`.
3. Move or archive only low-risk runtime clutter after classification:
   - `scratch/*`
   - stale folders under `runs/`
   - old rollback/debug packages under `99_Cleanup_Rollback/`
4. Add README/AGENTS notes that future scratch work belongs under:
   - `workspaces/dev-lab/sandbox/`
   - `workspaces/source-lab/runs/`
5. Verify no canonical path is modified.

### Track B - Compatibility Before Physical Code Move

This track prepares the eventual code-plane move.

1. Add path aliases to `.agent/config/paths.yaml`:
   - `code.current_scripts: "scripts"`
   - `code.future_scripts: "workspaces/dev-lab/scripts"`
   - `learning.current_root: "5-learning"`
   - `learning.future_root: "workspaces/learning/dashboard"`
   - `runtime.current_runs: "runs"`
   - `runtime.future_source_runs: "workspaces/source-lab/runs"`
2. Update dev/source/learning workspace overlays to describe current and future physical homes.
3. Do not move `scripts/` yet.
4. Create a regression checklist for the script commands that currently assume root `scripts/`.

### Track C - Controlled Physical Moves

Only after Track B is reviewed.

Candidate moves:

```text
scratch/*        -> 4-archive/scratch/YYYY-MM-DD_root_slimming/ or workspaces/dev-lab/sandbox/
99_Cleanup_Rollback/* -> 4-archive/cleanup_rollback/YYYY-MM-DD_root_slimming/
5-learning/*     -> workspaces/learning/dashboard/   # requires script compatibility first
tools/*          -> workspaces/dev-lab/tools/         # if tracked/used
libs/*           -> workspaces/dev-lab/libs/          # if tracked/used
tests/*          -> workspaces/dev-lab/tests/         # if tracked/used
scripts/*        -> workspaces/dev-lab/scripts/       # last, only after alias/regression pass
```

Non-candidates:

```text
.agent/
00_Inbox/
1-projects/
2-areas/
3-resources/
4-archive/
```

These remain root anchors.

## First Implementation Batch

Batch 1 should not move `scripts/`, `runs/`, `5-learning`, or `3-resources`.

1. Keep the `.code-workspace` and workspace-local `.vscode/settings.json` files from this branch.
2. Extend `.agent/config/paths.yaml` with current/future alias names only.
3. Update `workspaces/dev-lab/AGENTS.md`, `workspaces/source-lab/AGENTS.md`, and `workspaces/learning/AGENTS.md` to state where new physical work should be created.
4. Add a root-slimming checklist under `.agent/docs/ROOT_SLIMMING_CHECKLIST.md`.
5. Run verification:
   - JSON parse for workspace config files.
   - `git grep` for root path references.
   - `git diff --check`.

## Batch 2 Preview

Batch 2 may archive `scratch/*`, but only with exact-path GO.

Required preflight:

```text
list scratch top-level items
classify likely dependency / generated / stale
create archive target under 4-archive/scratch/YYYY-MM-DD_root_slimming/
move only approved items
run one smoke test for Docling/conversion if any Docling-related folders are moved
```

## Completed Root Slimming On 2026-05-25

```text
scratch/* archived to 4-archive/scratch/2026-05-25_root_slimming/
99_Cleanup_Rollback/ archived to 4-archive/cleanup_rollback/2026-05-25_root_slimming/
.venv_virtualenv_failed/ archived to 4-archive/runtime_env/2026-05-25_root_slimming/
skills_backup.zip archived to 4-archive/backups/2026-05-25_root_slimming/
.pytest_cache/ archived to 4-archive/cache/2026-05-25_root_slimming/
.agent_busy archived to 4-archive/state_markers/2026-05-25_root_slimming/
.deepeval/ archived to 4-archive/cache/2026-05-25_root_slimming/
```

The next phase is not another blind archive. It is compatibility work for:

```text
runs/
tools/
libs/
tests/
scripts/
```

These paths have live references or operational meaning and require path-registry migration plus regression checks.

Compatibility scaffolds have been created for the future homes:

```text
workspaces/dev-lab/scripts/
workspaces/dev-lab/tools/
workspaces/dev-lab/libs/
workspaces/dev-lab/tests/
workspaces/learning/dashboard/
```

The root paths remain the active compatibility paths until the migration is explicitly executed and verified.

## Dev-Lab Code Plane Import Completed In Worktree

Completed in branch `agent/multi-workspace-isolation`:

```text
root-local libs/  -> workspaces/dev-lab/libs/   # source only; excludes .env, logs, __pycache__, pyc
root-local tools/ -> workspaces/dev-lab/tools/  # source/docs only; excludes cache, __pycache__, pyc
root-local tests/ -> workspaces/dev-lab/tests/  # benchmark contract only; excludes generated output artifacts
```

Root copies have not been removed yet because multiple production and archived scripts still import `libs.core.*` from root. Removing root `libs/` requires either:

```text
1. updating script import/search paths to workspaces/dev-lab/libs, or
2. using the temporary compatibility shim at root libs/__init__.py, or
3. keeping root libs until scripts/ is migrated.
```

The worktree now includes a tiny root compatibility shim:

```text
libs/__init__.py -> extends package lookup to workspaces/dev-lab/libs/
```

This lets old imports like `from libs.core.logger import get_logger` keep working after the real library files move to `workspaces/dev-lab/libs/`. Do not keep a full root `libs/` tree after merge; root should only retain the shim during the transition.

## Learning Dashboard Migration Completed In Worktree

Completed in branch `agent/multi-workspace-isolation`:

```text
5-learning/LEARNING_DASHBOARD.md -> workspaces/learning/dashboard/LEARNING_DASHBOARD.md
5-learning/packs/ -> workspaces/learning/dashboard/packs/
5-learning/paths/ -> workspaces/learning/dashboard/paths/
```

Updated references:

```text
.agent/config/paths.yaml
.agent/skills/wiki-export-reader/SKILL.md
.agent/skills/wiki-learning-pack/SKILL.md
scripts/learning/export_epub.py
scripts/learning/learning_manager.py
WORKSPACE_OVERVIEW.md
workspaces/learning/AGENTS.md
workspaces/learning/dashboard/*.md
.gitignore
```

Remaining `5-learning` references are historical log entries or explicit legacy notes.

## Definition Of Done

- Daily work can start by opening one of:
  - `workspaces/learning`
  - `workspaces/source-lab`
  - `workspaces/dev-lab`
  - `workspaces/research-lab`
- Root contains only governance, canonical anchors, and compatibility entrypoints.
- `3-resources/` is untouched.
- Official ingest still works.
- Existing script commands still work or have documented compatibility commands.
- Broken link/path check has zero critical findings.
