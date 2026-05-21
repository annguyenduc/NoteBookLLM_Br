# CONTINUITY.md

## Current Objective

Tái cấu trúc NoteBookLLM_Br theo hướng học trước (learning-first), giảm context mặc định, nhưng không làm vỡ scripts vận hành.

## Current State

- Branch: `agent/20260521-learning-first-vault`
- Worktree: `D:\_agent_worktrees\20260521_learning_first_vault`
- Đã merge vào `main`.
- Các commit chính:
  - `dc77f11 chore: add learning-first vault structure`
  - `5d6dc43 chore: split workspace activation overlays`
  - `99adaab chore: add workspace folder skeletons`
  - `c18bb61 chore: add session continuity handoff`
  - `c8dcb90 chore: trim workspace doc eof whitespace`
- `AGENTS.md` đã chuyển root runtime sang learning-first.
- `workspaces/` đã có overlay cho `learning`, `source-lab`, `research-lab`, `dev-lab`.
- `.agent/config/paths.yaml` đã ghi frozen paths để tránh làm vỡ scripts.

## Validation Evidence

- `git diff --check`: PASS
- `test_ingest_lifecycle_check.py`: PASS
- `test_md_auditor_outline.py`: PASS
- `synthesis_guard.py check AGENTS.md`: PASS
- `codex mcp get tavily`: enabled, OAuth

## Next Step For AN

Mở phiên mới từ `D:\NoteBookLLM_Br` để kiểm tra runtime thực tế với root `AGENTS.md` mới:

1. Test một request học nhanh trong `workspaces/learning`.
2. Test một request preview tài liệu trong `workspaces/source-lab`.
3. Xác nhận Tavily tool surface có hiện sau restart/new session.
4. Nếu ổn, cleanup worktree `D:\_agent_worktrees\20260521_learning_first_vault`.

Không cần chạy official ingest trong smoke test đầu tiên.

## Blockers

- Tavily MCP đã thêm vào config, nhưng tool surface trong phiên hiện tại có thể cần restart/new session để hiện tool.
- Chưa cleanup worktree sau merge.
