# AGENTS.md - research-lab

This workspace is inside NoteBookLLM_Br, but it is NON-CANONICAL.

## Workspace Context

```yaml
workspace_name: "research-lab"
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

- tìm bối cảnh bên ngoài bằng Tavily.
- so sánh nhiều nguồn ở mức preview.
- chuẩn bị câu hỏi, keyword, source triage cho học nhanh.

## Active Workflow

Default workflow:

```text
../../.agent/workflows/learning-first.md
```

Allowed workflows/skills:

```text
../../.agent/workflows/knowledge-intake.md
../../.agent/skills/process-raw-resource/SKILL.md
Tavily MCP
SQLite MCP
NotebookLM MCP
```

Forbidden by default:

```text
../../.agent/workflows/ingest-lifecycle.md
../../3-resources/
```

## Allowed

- create non-canonical research notes inside `workspaces/research-lab/`.
- use Tavily for external context.
- query SQLite read-only for existing vault context.
- compare sources and recommend `SKIP | KEEP_SUMMARY | PROMOTE`.

## Forbidden

- write directly to `../../3-resources/`.
- create canonical Atom files.
- set `VERIFIED`.
- set `SYNTHESIZED`.
- treat Tavily/web output as source truth.

## Handoff

- If a source deserves vault ingestion, report `PROMOTE` and stop.
- Official ingest must be approved by AN and routed through `../../.agent/workflows/ingest-lifecycle.md`.

