# CONTINUITY.md

## Current Objective

Tái cấu trúc NoteBookLLM_Br theo hướng học trước (learning-first), giảm context mặc định, nhưng không làm vỡ scripts vận hành.

## Current State

- Branch đang làm: `agent/20260522-routing-trace`
- Worktree: `D:\_agent_worktrees\20260522_routing_trace`
- Đang vá gap routing audit cho test case: `Tóm tắt PDF này để tôi học nhanh.`
- Đã thêm `ROUTING_DECISION` vào root dispatch, `learning-first`, `knowledge-intake`, `process-raw-resource`, và overlay `learning/source-lab`.

## Validation Evidence

- `git diff --check`: PASS
- conflict/TODO/TBD scan: PASS
- `ROUTING_DECISION` presence scan: PASS
- `synthesis_guard.py check AGENTS.md`: PASS
- `test_ingest_lifecycle_check.py`: PASS
- `test_md_auditor_outline.py`: PASS

## Next Step For AN

1. Review routing trace patch.
2. Nếu ổn, GO merge branch `agent/20260522-routing-trace` vào `main`.
3. Sau merge, chạy lại smoke test: `Tóm tắt PDF này để tôi học nhanh.`
4. Expected first block:
   ```yaml
   ROUTING_DECISION:
     selected_workspace: "workspaces/learning"
     mode: "learning-first"
     canonical_write: "NO"
     ingest_lifecycle: "NO"
   ```

## Blockers

- Main tại `D:\NoteBookLLM_Br` đang có thay đổi chưa liên quan trước khi tạo worktree: `.gitignore` modified và `00_Inbox/sources-pending/` untracked. Không chạm các thay đổi đó trong patch này.
