# CONTINUITY.md

## Current Objective

Triển khai chính sách On-Demand Script Policy cho Agent (`SPEC_ON_DEMAND_SCRIPT_POLICY`) nhằm giảm RAM nền khi chạy MCP server, thay thế các tác vụ nặng bằng Python/PowerShell scripts chạy ngắn hạn chỉ khi cần thiết.

## Current State

- Branch đang làm: `agent/20260522-on-demand-script-policy`
- Worktree: `D:\_agent_worktrees\20260522_on_demand_script_policy`
- Đã triển khai và kiểm thử thành công 8 script helper trong `scripts/tasks/` hoạt động on-demand tự thoát:
  1. `check_ram_processes.py`: Đo đạc RAM nền của các tiến trình liên quan (~675 MB khi bật full).
  2. `inspect_mcp_config.py`: Đọc file `mcp_config.json` của Antigravity client.
  3. `git_status_report.py`: Báo cáo git status ngắn gọn.
  4. `sqlite_query_once.py`: Truy vấn SQLite read-only dưới dạng Markdown table, chặn SQL sửa đổi cấu trúc/dữ liệu.
  5. `query_wiki.py`: Tìm kiếm spine wiki nhanh bằng FTS5.
  6. `tavily_search_once.py`: Tìm kiếm web nhanh qua Tavily API (không dùng MCP server nền).
  7. `notebooklm_query_once.py`: Gửi truy vấn tới NotebookLM qua API client bằng token cached.
  8. `lint_report.py`: Quét dry-run kiểm tra broken links và stale files trên các thư mục wiki thực tế.
- Đã cập nhật file `AGENTS.md` trong worktree để chuyển Bộ MCP Mặc Định sang profile `micro` (chỉ bật `filesystem` MCP).
- Đã chạy kiểm thử và đảm bảo cả 8 script in đúng cấu trúc báo cáo YAML `SCRIPT_RUN_REPORT`.

## Next Step For AN

1. Kiểm tra các script helper trong `scripts/tasks/` trên worktree.
2. Review và phê duyệt merge branch `agent/20260522-on-demand-script-policy` vào `main`.
3. Kiểm tra báo cáo chi tiết trong `walkthrough.md`.

## Blockers

- Không có.
