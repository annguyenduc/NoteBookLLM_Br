# AGENTS.md - learning workspace

This workspace is inside NoteBookLLM_Br, but it is NON-CANONICAL.

Purpose:

- đọc nhanh (preview) tài liệu.
- tạo bản đồ học (learning map).
- tạo ghi chú học nhanh (learning note).
- giúp AN quyết định `SKIP | KEEP_SUMMARY | PROMOTE`.

Allowed:

- read files inside `workspaces/learning/`.
- write learning drafts inside `workspaces/learning/`.
- create non-canonical reports and notes.
- use NotebookLM as reconnaissance (trinh sát) for long documents.

Forbidden:

- write directly to `../../3-resources/`.
- write directly to `../../3-resources/raw_sources/`.
- write directly to `../../3-resources/raw_ingest/`.
- write directly to `../../3-resources/raw_assets/`.
- write directly to `../../3-resources/wiki/`.
- create canonical Atom files.
- set `VERIFIED`.
- set `SYNTHESIZED`.

Handoff:

- If a learning note deserves canonical ingest, report `PROMOTE`.
- Official ingest must go through `../../.agent/workflows/ingest-lifecycle.md`.

