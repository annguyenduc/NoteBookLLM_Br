# AGENTS.md - dev-lab

This workspace is inside NoteBookLLM_Br, but it is NON-CANONICAL.

## Workspace Context

```yaml
workspace_name: "dev-lab"
vault_root: "../.."
shared_agent_library: "../../.agent"
path_registry: "../../.agent/config/paths.yaml"
canonical_source_of_truth: "../../3-resources"
```

Read order:

1. `../../AGENTS.md`
2. `AGENTS.md` in this workspace
3. `../../.agent/rules/CORE.md`
4. only the workflow/skill listed as active or allowed below

## Purpose

- thử nghiệm script, benchmark, và patch kỹ thuật.
- tạo report kỹ thuật non-canonical trước khi sửa scripts chính.
- giảm context cho các task code không cần ingest/wiki governance đầy đủ.

## Active Workflow

Default workflow:

```text
../../.agent/workflows/autonomous-dev-task.md
```

Allowed workflows/skills:

```text
../../.agent/rules/engineer.md
../../.agent/workflows/autonomous-dev-task.md
../../.agent/config/paths.yaml
```

Escalation-only:

```text
../../.agent/workflows/ingest-lifecycle.md
../../.agent/workflows/ingest-generate.md
../../.agent/workflows/ingest-index-log.md
```

Forbidden by default:

```text
../../3-resources/raw_sources/
../../3-resources/raw_ingest/
../../3-resources/raw_assets/
../../3-resources/wiki/synthesis/
```

## Allowed

- write experiments inside `workspaces/dev-lab/`.
- inspect scripts in `../../scripts/`.
- create reports and patch plans.
- patch scripts only when AN's GO includes the exact file path or an approved scope.

## Forbidden

- write to raw storage.
- write to synthesis without exact-path GO and `synthesis_guard.py check`.
- promote, rebuild, or commit without explicit AN approval.
- use experiments here as canonical evidence.

## Handoff

- For script patches, report exact files and tests before commit.
- For canonical ingest effects, handoff to root workflow after AN GO.

