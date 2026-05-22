# CONTINUITY.md

## Current Objective

Hoàn tất hợp nhất `cm-instinct-learning` và `.agent/instincts/` vào `session_insights` và `skill_reviews/SIP` theo Option A (ADR-001) có kèm điều chỉnh từ người dùng.

## Current State

- **Trạng thái**: Đã hoàn thành xuất sắc việc tích hợp Instincts và Promote Rule vào [INSIGHT_TEMPLATE.md](file:///D:/_agent_worktrees/20260522_deprecate_instinct/.agent/skills/references/INSIGHT_TEMPLATE.md).
- **Nhánh làm việc**: `agent/20260522-deprecate-instinct` tại Git worktree `D:\_agent_worktrees\20260522_deprecate_instinct`.
- **Thay đổi chính**:
  1. Di chuyển hoàn toàn `cm-instinct-learning` skill và `.agent/instincts/` ra ngoài thư mục active và lưu trữ an toàn trong `.agent/archive/` (giải quyết triệt để routing confusion mà không vi phạm nguyên tắc `Cấm xóa`).
  2. Tích hợp định nghĩa **Instinct candidate** và **Promote Rule** trực tiếp vào section `## 4. Bài học hệ thống / Instincts` trong `INSIGHT_TEMPLATE.md`.
  3. Cập nhật `SKILLS_INDEX.md` để đánh dấu trạng thái `[ARCHIVED / DEPRECATED]` cho skill này.
  4. Đã commit sạch sẽ tất cả các thay đổi vào nhánh `agent/20260522-deprecate-instinct` (mã commit `c081e42`).

## Next Step For AN

1. **Merge nhánh vào main**: AN kiểm tra lại và merge nhánh `agent/20260522-deprecate-instinct` vào `main`.
2. **Xóa Git Worktree (Tùy chọn)**: Sau khi merge, AN có thể chạy các lệnh dọn dẹp worktree:
   ```bash
   git worktree remove D:\_agent_worktrees\20260522_deprecate_instinct --force
   git branch -D agent/20260522-deprecate-instinct
   ```
3. **Áp dụng trong các phiên sau**: Sử dụng section `## 4. Bài học hệ thống / Instincts` trong các Session Insight kế tiếp khi có các bài học atomic mới.

## Blockers

- Không có blockers.
