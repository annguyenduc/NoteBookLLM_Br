# Workspaces

`workspaces/` là vùng làm việc phụ bên trong vault.

Các workspace này giúp giảm context và thử nghiệm nhanh, nhưng luôn là non-canonical.

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

