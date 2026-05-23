# CONTINUITY.md

## Current Objective

Tinh giản triệt để bề mặt quy trình tiếp xúc người dùng (User-facing Surface), bảo toàn 6 cổng kiểm soát (Gates) Ingest dưới dạng **Bản Đặc tả Chắt lọc Tinh hoa (Condensed Stage Contracts)**, và cấu trúc lại quy trình học phi tuyến tính (Semantic Learning Map Mode) trong Vault.

## Current State

- **Trạng thái**: Đã hoàn thành 100% việc tái cấu trúc, di chuyển, dọn dẹp hệ thống trong worktree an toàn và **chạy thành công 3 ca kiểm thử Canary với file thật** (kiểm thử learning-first cấm ghi 3-resources, định tuyến knowledge-intake, và ingest-lifecycle chống trùng lặp qua tệp contract mới).
- **Nhánh làm việc**: `agent/20260523-workflow-cleanup` tại Git worktree `D:\_agent_worktrees\20260523_workflow_cleanup`.
- **Thay đổi chính**:
  1. Tinh giản số lượng file quy trình trong `.agent/workflows/` từ **15 xuống còn đúng 7 file cốt lõi** thực sự có thể gọi trực tiếp bởi người dùng/Agent.
  2. Gom toàn bộ 6 file stage gates con của Ingest Lifecycle vào một tệp đặc tả hợp đồng duy nhất: `.agent/contracts/ingest-stage-contracts.md` nằm ngoài thư mục workflows làm **Bản Đặc tả Chắt lọc Tinh hoa (Condensed Stage Contracts)**, trộn Frontmatter an toàn và bảo toàn 100% trường `description` gốc.
  3. Cập nhật `ingest-lifecycle.md` để nó trỏ và điều phối trực tiếp thông qua tệp contract tổng mới.
  4. Di chuyển 2 file tĩnh `setup-notebooklm-mcp.md` and `source-first-ingest.md` sang thư mục tài liệu tham chiếu `docs/`.
  5. Bảo vệ và giữ nguyên `autonomous-dev-task.md` tại workflows để tránh gãy các liên kết hoạt động của `dev-lab`.
  6. Tích hợp sâu sắc `Semantic Learning Map Mode` vào workflow mặc định `learning-first.md`, cấm ghi đè vào `3-resources/`.
  7. Đồng bộ hóa Overlay `AGENTS.md` của 3 workspace con (`source-lab`, `learning`, `dev-lab`) để chuyển các stage files cũ thành quy chuẩn *"parent-only via ingest-lifecycle.md"*.
  8. Cập nhật bản quy hoạch trong Vault: `workspaces/learning/NON_LINEAR_WORKFLOW_PLAN.md` và tạo báo cáo nghiệm thu `workspaces/learning/walkthrough.md` trực tiếp trong Vault.
  9. Đã staged toàn bộ các tệp tin modified và new vào Git Index sạch sẽ và nhất quán.

## Next Step For AN

1. **Nghiệm thu kiểm toán**:
   - Mở tệp [walkthrough.md](file:///D:/_agent_worktrees/20260523_workflow_cleanup/workspaces/learning/walkthrough.md) trực tiếp trong Obsidian Vault để kiểm tra báo cáo nghiệm thu và `TASK_REPORT` mới nhất.
   - Xác nhận thư mục `.agent/workflows/` trong worktree chỉ còn đúng 7 tệp hoạt động.
   - Xác nhận tệp contract tổng [ingest-stage-contracts.md](file:///D:/_agent_worktrees/20260523_workflow_cleanup/.agent/contracts/ingest-stage-contracts.md) đã được staged.
2. **Tiến hành Commit (Sau khi AN cấp GO)**:
   - Agent hoặc AN thực hiện lệnh commit an toàn trong worktree:
     ```bash
     git commit -m "refactor: simplify workflows and consolidate stage gates to contracts"
     ```
3. **Merge nhánh vào main**:
   - Sau khi commit thành công, chạy `git log main..HEAD` để xác nhận nhánh cục bộ đã có commit vượt trước `main`.
   - Tiến hành merge nhánh `agent/20260523-workflow-cleanup` vào `main` tại repo chính.
4. **Dọn dẹp worktree an toàn (Quy trình không force)**:
   ```bash
   cd /d D:\NoteBookLLM_Br
   git worktree remove D:\_agent_worktrees\20260523_workflow_cleanup
   git branch -d agent/20260523-workflow-cleanup
   ```

## Blockers

- **Không có blockers.** Mọi tệp tin đã được staged an toàn và kiểm thử Canary thành công rực rỡ!
