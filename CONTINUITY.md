# CONTINUITY.md

## Current Objective

Triển khai kế hoạch tự động hóa khép kín: di chuyển kích hoạt lại skill `prompt-master`, viết script điều phối `scripts/tasks/produce_and_query_notebooklm.py` để kết nối FreeLLMAPI (cổng 3001) và NotebookLM MCP, sau đó kiểm thử dry-run an toàn 100% không có tác dụng phụ.

## Current State

- **Trạng thái**: Đã hoàn thành 100% việc kích hoạt lại skill `prompt-master`, khởi tạo và viết code hoàn chỉnh cho script điều phối `scripts/tasks/produce_and_query_notebooklm.py`, và chạy kiểm thử dry-run đầu tiên thành công tuyệt đối mà không có bất kỳ file mock nào ghi ra đĩa hay gọi API thực tế.
- **Nhánh làm việc**: `agent/20260523-freellm-notebooklm-pipeline` tại Git worktree `D:\_agent_worktrees\20260523_freellm_notebooklm_pipeline`.
- **Thay đổi chính**:
  1. Di chuyển thư mục `prompt-master` từ `.agent/skills_lazy/prompt-master` sang `.agent/skills/prompt-master/` để kích hoạt lại kỹ năng chính thức.
  2. Tạo script `scripts/tasks/produce_and_query_notebooklm.py` tích hợp logic trích xuất Core Rubric từ skill `prompt-master`, tự động đọc API key SQLite của FreeLLMAPI, nạp môi trường ảo `.venv` động, sinh prompt thông qua FreeLLMAPI local proxy và đẩy qua NotebookLM MCP client.
  3. Bổ sung cờ `--dry-run` thực sự: Không gọi API thực tế, không đọc SQLite database, không ghi bất kỳ mock file nào ra đĩa. Chỉ in Core Rubric và Mock Prompt ra màn hình.
  4. Chạy kiểm thử dry-run thành công tuyệt đối.
  5. Cập nhật `task.md` và `walkthrough.md` trong thư mục artifact của cuộc hội thoại.

## Next Step For AN

1. **Nghiệm thu kiểm toán**:
   - Kiểm tra mã nguồn của script điều phối tại [produce_and_query_notebooklm.py](file:///D:/_agent_worktrees/20260523_freellm_notebooklm_pipeline/scripts/tasks/produce_and_query_notebooklm.py).
   - Kiểm tra cấu trúc skill tại thư mục [prompt-master](file:///D:/_agent_worktrees/20260523_freellm_notebooklm_pipeline/.agent/skills/prompt-master/SKILL.md).
   - Xem chi tiết báo cáo nghiệm thu tại tệp [walkthrough.md](file:///C:/Users/anngu/.gemini/antigravity/brain/e2e7ef1e-5ac5-46c0-bf78-6ba17bc85772/walkthrough.md).
2. **Chạy thực tế (Khi AN cấp GO và các service local đã bật)**:
   - Đảm bảo FreeLLMAPI local đã được khởi động tại cổng `3001` và NotebookLM token đã được cached.
   - Thực thi lệnh:
     ```powershell
     python scripts/tasks/produce_and_query_notebooklm.py "Hãy giúp tôi bóc tách 3 điểm cốt lõi nhất về quy trình ingest từ tài liệu nguồn" --title "Ingest Core Breakdown" --use-first-notebook
     ```
3. **Commit và Merge nhánh vào main**:
   - Agent hoặc AN thực hiện lệnh commit trong worktree:
     ```bash
     git add .
     git commit -m "feat: reactivate prompt-master and integrate produce_and_query_notebooklm.py pipeline"
     ```
   - Merge nhánh `agent/20260523-freellm-notebooklm-pipeline` vào `main` tại repo chính.

## Blockers

- **Không có blockers.** Mọi tác vụ được yêu cầu đều đã hoàn thành xuất sắc và kiểm thử dry-run pass hoàn hảo!
