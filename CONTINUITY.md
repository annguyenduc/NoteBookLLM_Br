# CONTINUITY.md

## Current Objective

Học nhanh và tra cứu nhanh thông tin thông qua cơ chế On-Demand Script Policy đã được tích hợp vào nhánh main.

## Current State

- **Trạng thái**: Đã merge thành công nhánh `agent/20260522-on-demand-script-policy` vào `main`.
- **Đã kiểm thử**: Đã chạy thử nghiệm và sửa lỗi phân tích (parse) git status đầu ra trong [git_status_report.py](file:///D:/NoteBookLLM_Br/scripts/tasks/git_status_report.py) (không bị mất chữ cái đầu).
- **Cấu hình**: MCP Profile đã được chuyển đổi mặc định về `micro` (chỉ bật `filesystem` MCP), các MCP khác chuyển thành chạy script on-demand để tiết kiệm RAM.
- **Worktree**: Đã dọn dẹp và xóa worktree `D:\_agent_worktrees\20260522_on_demand_script_policy`.

## Next Step For AN

1. Theo dõi hoạt động của Agent khi thực thi các script on-demand qua rule mới [.agent/rules/on-demand-script-policy.md](file:///D:/NoteBookLLM_Br/.agent/rules/on-demand-script-policy.md).
2. Kiểm tra báo cáo kiểm thử chi tiết trong [walkthrough.md](file:///C:/Users/anngu/.gemini/antigravity/brain/3928c136-b64f-4bec-9e11-0c156bf448b6/walkthrough.md).

## Blockers

- Không có.
