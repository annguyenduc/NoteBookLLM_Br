# AGENTS.md - learning workspace

This workspace is inside NoteBookLLM_Br, but it is NON-CANONICAL.

## Workspace Context

```yaml
workspace_name: "learning"
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

- học nhanh từ tài liệu hoặc atom có sẵn.
- tạo bản đồ học (learning map).
- tạo ghi chú học nhanh (learning note).
- giúp AN quyết định `SKIP | KEEP_SUMMARY | PROMOTE`.

## Physical Workspace Boundary

Learning drafts and preview artifacts belong here:

```text
notes/
flashcards/
questions/
outputs/
preview/
```

Learning dashboard path:

```text
dashboard/
```

Learning output home:

```text
outputs/
```

The legacy root `../../5-learning/` has been migrated into this workspace. Do not recreate it at root.

## Active Workflow

Default workflow:

```text
../../.agent/workflows/learning-first.md
```

Required routing trace:

```yaml
ROUTING_DECISION:
  selected_workspace: "workspaces/learning"
  mode: "learning-first"
  loaded_overlay: "workspaces/learning/AGENTS.md"
  canonical_write: "NO"
  ingest_lifecycle: "NO"
```

This overlay only defines the learning route. The global workspace list lives in:

```text
../../.agent/config/workspace-routing.yaml
```

Allowed skills/workflows:

```text
../../.agent/skills/process-raw-resource/SKILL.md
../../.agent/workflows/knowledge-intake.md
NotebookLM MCP
SQLite MCP
Tavily MCP
```

Forbidden by default:

```text
../../.agent/workflows/ingest-lifecycle.md
../../.agent/contracts/ingest-stage-contracts.md (parent-only via ingest-lifecycle.md)
../../3-resources/
```

## Allowed

- read files inside `workspaces/learning/`.
- write learning drafts inside `workspaces/learning/`.
- create non-canonical reports and notes.
- use NotebookLM as reconnaissance (trinh sát) for long documents.
- query SQLite read-only for existing wiki context.
- use Tavily for external context, with source uncertainty stated.

## Forbidden

- write directly to `../../3-resources/`.
- write directly to `../../3-resources/raw_sources/`.
- write directly to `../../3-resources/raw_ingest/`.
- write directly to `../../3-resources/raw_assets/`.
- write directly to `../../3-resources/wiki/`.
- create canonical Atom files.
- set `VERIFIED`.
- set `SYNTHESIZED`.
- treat NotebookLM/Tavily output as source truth.

## Handoff

- If a learning note deserves canonical ingest, report `PROMOTE`.
- Do not load or run ingest lifecycle details unless AN explicitly says GO for official ingest.
- Official ingest must go through `../../.agent/workflows/ingest-lifecycle.md`.
