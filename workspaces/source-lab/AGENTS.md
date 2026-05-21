# AGENTS.md - source-lab

This workspace is inside NoteBookLLM_Br, but it is NON-CANONICAL.

## Workspace Context

```yaml
workspace_name: "source-lab"
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

- xử lý thử nguồn dài.
- convert/OCR/preview ở mức nháp.
- hỏi NotebookLM để lập cấu trúc tài liệu.
- chuẩn bị đề xuất có nên ingest chính thức không.

## Active Workflow

Default workflow:

```text
../../.agent/skills/process-raw-resource/SKILL.md
```

Allowed workflows:

```text
../../.agent/workflows/learning-first.md
../../.agent/workflows/knowledge-intake.md
NotebookLM MCP
Tavily MCP
```

Escalation-only workflow:

```text
../../.agent/workflows/ingest-lifecycle.md
```

Forbidden by default:

```text
../../.agent/workflows/audit-promote-source.md
../../.agent/workflows/lock-ingest-input.md
../../.agent/workflows/ingest-generate.md
../../3-resources/
```

## Allowed

- read/write inside `workspaces/source-lab/`.
- create temporary preview files.
- create handoff recommendation in chat or local draft.
- use NotebookLM as reconnaissance (trinh sát) for long documents.
- use Tavily for external background checks.

## Forbidden

- write directly to `../../3-resources/`.
- write directly to `../../3-resources/raw_sources/`.
- write directly to `../../3-resources/raw_ingest/`.
- write directly to `../../3-resources/raw_assets/`.
- write directly to `../../3-resources/wiki/`.
- create official lifecycle artifacts unless AN explicitly starts official ingest.
- create canonical Atom files.
- set `VERIFIED`.
- set `SYNTHESIZED`.
- treat NotebookLM/Tavily output as source truth.

## Handoff

- Default output is `SKIP | KEEP_SUMMARY | PROMOTE`.
- If `PROMOTE`, report why and stop.
- Only route to `../../.agent/workflows/ingest-lifecycle.md` after AN gives GO for official ingest.

