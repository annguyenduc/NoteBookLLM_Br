# Superpowers Skill Inventory

Báo cáo này liệt kê toàn bộ các kỹ năng thực tế của Superpowers kiểm đếm được tại thời điểm chạy audit, so sánh đối chiếu với hệ thống kỹ năng hiện tại của vault theo nguyên tắc: **Lấy Superpowers làm chuẩn chính cho Core Method Skills, các skill `cm-*` tương đương chỉ đóng vai trò là nguồn bổ sung thích nghi hoặc ứng viên thay thế (legacy candidates).**

## Summary

- Total Superpowers skills inspected: **14**
- Total matching vault equivalents: **12**
- Total missing in vault: **2**
- Total reference-only: **2** (Bao gồm các kỹ năng mang tính Git/PR-specific không phù hợp với ranh giới của vault)

## Skill Inventory Table

| Superpowers skill | Purpose | Vault equivalent (Legacy/Adaptation Source) | Match type | Initial decision |
| :--- | :--- | :--- | :--- | :--- |
| **using-superpowers** | Bootstrap chọn và kích hoạt skill đầu phiên cho Antigravity. | `using-superpowers` | exact_equivalent | port/normalize |
| **brainstorming** | Khám phá ý định người dùng và phác thảo ý tưởng Phase 0. | `cm-planning`/`brainstorming` | partial_equivalent | port/normalize |
| **writing-plans** | Thiết kế kỹ thuật chi tiết bằng implementation_plan.md Phase 1. | `writing-plans` | exact_equivalent | merge |
| **executing-plans** | Triển khai code và cập nhật tiến độ task.md. | `executing-plans` | exact_equivalent | merge |
| **test-driven-development** | Kiểm thử đệ quy tự sửa lỗi. | `cm-tdd` | exact_equivalent | port/normalize |
| **systematic-debugging** | Khoanh vùng và chẩn đoán lỗi hệ thống chính. | `systematic-debugging`/`cm-debugging` | partial_equivalent | port/normalize |
| **verification-before-completion** | Xác minh và thu thập bằng chứng kiểm thử trước khi báo DONE. | `verification-before-completion` | exact_equivalent | merge |
| **using-git-worktrees** | Thiết lập Git Worktree cô lập nhánh agent. | `cm-git-flow`/`AGENTS.md` (worktree clause) | partial_equivalent | reference_only |
| **subagent-driven-development** | Phân rã công việc cho các subagent chạy độc lập. | `subagent-driven-development` | exact_equivalent | merge |
| **dispatching-parallel-agents** | Điều phối và giám sát nhiều tác nhân song song. | None | missing | port |
| **requesting-code-review** | Yêu cầu review cấu trúc code trước khi hoàn tất. | `cm-code-review` | partial_equivalent | port/normalize |
| **receiving-code-review** | Xử lý feedback review của con người. | `cm-code-review` | partial_equivalent | port/normalize |
| **finishing-a-development-branch** | Đóng PR, dọn dẹp Git branch sau khi merge. | None | missing | reference_only |
| **writing-skills** | Chuẩn hóa quy trình biên soạn/chỉnh sửa kỹ năng. | `write-skill` | exact_equivalent | port/normalize |
