# CONTINUITY.md

## Current Objective

Tái cấu trúc NoteBookLLM_Br theo hướng học trước (learning-first), giảm context mặc định, nhưng không làm vỡ scripts vận hành.

## Current State

- Branch đang làm: `agent/20260522-layered-load-policy`
- Worktree: `D:\_agent_worktrees\20260522_layered_load_policy`
- Đang áp dụng Layered Load Policy cho `AGENTS.md` (Phase 1).
- Đã sửa đổi phần `## Startup Profiles` trong `AGENTS.md` thành `STARTUP MINIMAL` và `ROOT REFERENCE LOAD POLICY` nhằm giảm dung lượng context khởi động.
- Thiết lập này đã được User phê duyệt để tiến hành kiểm tra thực tế.

## Validation Evidence

- `git status; git diff`: PASS (chỉ có duy nhất thay đổi hợp lệ ở AGENTS.md, diff sạch sẽ).
- Không có lỗi cú pháp markdown hoặc trùng lặp heading.

## Next Step For AN

1. AN thực hiện merge nhánh `agent/20260522-layered-load-policy` vào `main` để kích hoạt chính sách tải theo tầng.
2. Kiểm tra Agent chạy trong 1-2 phiên tiếp theo xem có tuân thủ việc không tự động bulk-load các tệp markdown ở root và chỉ tra cứu khi cần hay không.
3. Sau khi chạy thử ổn định, đánh giá để thực hiện Phase 2 (hạ nhãn mandatory trong `WORKSPACE_OVERVIEW.md` hoặc SPEC).

## Blockers

- Các file chưa stage trên `main` (`.gitignore` và `00_Inbox/sources-pending/`) vẫn được giữ nguyên, không ảnh hưởng đến thay đổi này.

