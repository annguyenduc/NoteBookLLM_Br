# Workspaces

`workspaces/` là vùng làm việc phụ bên trong vault.

Các workspace này giúp giảm context và thử nghiệm nhanh, nhưng luôn là non-canonical.

Current overlays:

```text
learning/      # học nhanh, learning map, ghi chú học
source-lab/    # preview tài liệu dài, NotebookLM recon, source triage
research-lab/  # Tavily/web context, so sánh nguồn, research notes
dev-lab/       # thử nghiệm script, benchmark, patch kỹ thuật
```

Allowed:

- tạo preview, learning note, report, experiment.
- giữ tài liệu đang xử lý tạm thời.
- chuẩn bị candidate để AN quyết định có promote vào vault chính không.

Forbidden:

- ghi trực tiếp vào `../3-resources/`.
- tạo Atom canonical.
- set `VERIFIED` hoặc `SYNTHESIZED`.
- coi NotebookLM/Tavily output là source of truth.

Canonical knowledge vẫn nằm ở:

```text
3-resources/
```

Shared rules, workflows, and skills live at:

```text
../.agent/
```

Workspace overlays select what is active; they do not copy `.agent/`.
