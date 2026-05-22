# CONTINUITY.md

## Current Objective

Tái cấu trúc NoteBookLLM_Br theo hướng học trước (learning-first), giảm context mặc định, nhưng không làm vỡ scripts vận hành.

## Current State

- **Trạng thái**: Đã merge thành công nhánh `agent/20260522-layered-load-policy` vào `main`.
- **Thay đổi chính**: Cập nhật phần `## Startup Profiles` trong `AGENTS.md` thành `STARTUP MINIMAL` và `ROOT REFERENCE LOAD POLICY` nhằm giảm dung lượng context khởi động (Phase 1).
- **Trước đó**: Đã merge thành công nhánh `agent/20260522-on-demand-script-policy` vào `main`, chuyển đổi MCP Profile mặc định về `micro` (chỉ bật `filesystem` MCP).
- **Worktree**: Đã dọn dẹp và xóa các worktree cũ (`20260522_on_demand_script_policy`, `20260522_layered_load_policy`).

## Next Step For AN

1. Theo dõi hoạt động của Agent khi thực thi các script on-demand qua rule mới [.agent/rules/on-demand-script-policy.md](file:///D:/NoteBookLLM_Br/.agent/rules/on-demand-script-policy.md).
2. Kiểm tra Agent chạy trong 1-2 phiên tiếp theo xem có tuân thủ việc không tự động bulk-load các tệp markdown ở root và chỉ tra cứu khi cần hay không.
3. Sau khi chạy thử ổn định, đánh giá để thực hiện Phase 2 (hạ nhãn mandatory trong `WORKSPACE_OVERVIEW.md` hoặc SPEC).

## Blockers

- Các file chưa stage trên `main` (`.gitignore` và `00_Inbox/sources-pending/`) vẫn được giữ nguyên, không ảnh hưởng đến thay đổi này.

