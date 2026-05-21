# CONTINUITY.md

## Current Objective

Tái cấu trúc NoteBookLLM_Br theo hướng học trước (learning-first), giảm context mặc định, nhưng không làm vỡ scripts vận hành.

## Current State

- Branch: `agent/20260521-learning-first-vault`
- Worktree: `D:\_agent_worktrees\20260521_learning_first_vault`
- Đã có 3 commit:
  - `dc77f11 chore: add learning-first vault structure`
  - `5d6dc43 chore: split workspace activation overlays`
  - `99adaab chore: add workspace folder skeletons`
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

Review nhanh branch `agent/20260521-learning-first-vault`, đặc biệt:

1. `AGENTS.md`
2. `.agent/workflows/learning-first.md`
3. `workspaces/*/AGENTS.md`
4. `WORKSPACE_OVERVIEW.md`
5. `.agent/docs/LEARNING_FIRST_RESTRUCTURE_PLAN.md`

Nếu ổn, bước tiếp theo là GO merge branch này vào `main`, rồi mở phiên mới để kiểm tra runtime thực tế với root `AGENTS.md` mới.

## Blockers

- Chưa merge vào `main`.
- Tavily MCP đã thêm vào config, nhưng tool surface trong phiên hiện tại có thể cần restart/new session để hiện tool.

