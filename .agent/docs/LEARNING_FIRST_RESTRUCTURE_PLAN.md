# Learning-First Restructure Plan

> Mục tiêu: tối giản vault để phục vụ học nhanh và tra cứu nhanh, đồng thời không làm vỡ scripts vận hành hiện tại.

## Nguyên tắc

- Giữ `3-resources/` là nguồn sự thật chính thức (canonical source of truth).
- Giữ nguyên các đường dẫn scripts đang phụ thuộc: `00_Inbox/`, `1-projects/`, `2-areas/`, `3-resources/`, `4-archive/`, `.agent/`, `scripts/`.
- Thêm mới theo hướng cộng thêm (additive), không di chuyển thư mục cốt lõi trong phase này.
- Chuyển default từ ingest-first sang học trước (learning-first).
- Official ingest vẫn tồn tại như chế độ chính thức/nâng cao (official/canonical mode).

## Checklist

- [x] Tạo worktree an toàn trên branch `agent/20260521-learning-first-vault`.
- [x] Kiểm kê scripts phụ thuộc vào layout cũ.
- [x] Rút gọn `AGENTS.md` thành runtime kernel learning-first.
- [x] Thêm workflow `.agent/workflows/learning-first.md`.
- [x] Giữ `knowledge-intake` làm router, không phải ingest engine.
- [x] Đánh dấu `ingest-lifecycle` là official/canonical mode, không phải default.
- [x] Thêm `.agent/config/paths.yaml` để ghi nhận frozen paths và path registry.
- [x] Thêm `workspaces/` non-canonical với `learning/` và `source-lab/`.
- [x] Thêm overlay `research-lab/` và `dev-lab/` để phân rã routing theo workspace.
- [x] Ghi rõ workspace activation: root route, workspace con chọn active/allowed/forbidden workflow.
- [x] Materialize skeleton thư mục con bằng `.gitkeep` cho learning/source-lab/research-lab/dev-lab.
- [x] Cập nhật `.gitignore` để chỉ track `README.md` và `AGENTS.md` trong workspace, còn file nháp vẫn ignored.
- [x] Cập nhật `WORKSPACE_OVERVIEW.md` để phản ánh learning-first và `workspaces/`.
- [x] Bật Tavily MCP dạng remote OAuth trong Codex config.
- [x] Chạy validation tối thiểu.

## Validation Hiện Tại

```text
git diff --check                                             PASS
conflict marker scan                                         PASS
python scripts/maintenance/test_ingest_lifecycle_check.py    PASS
D:\NoteBookLLM_Br\.venv\Scripts\python.exe scripts/maintenance/test_md_auditor_outline.py    PASS
python scripts/maintenance/synthesis_guard.py check AGENTS.md    PASS
codex mcp get tavily                                         enabled, OAuth
```

## Chưa Làm Trong Phase Này

- Chưa migrate scripts sang đọc `.agent/config/paths.yaml`.
- Chưa di chuyển thư mục cốt lõi.
- Chưa merge vào `main`.
- Chưa commit.

## Merge Gate

Chỉ merge sau khi AN review các file chính:

- `AGENTS.md`
- `.agent/workflows/learning-first.md`
- `.agent/config/paths.yaml`
- `WORKSPACE_OVERVIEW.md`
- `workspaces/*/AGENTS.md`
