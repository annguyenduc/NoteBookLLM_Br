# INSIGHT: Rollback Governance Lockdown (Session Lock & ACL)
**Date:** 2026-05-11
**Context:** Ingestion Pipeline Hardening Phase

## 1. Quan sát (Observations)
- Việc triển khai cơ chế **Lock cứng bằng ACL (Windows icacls)** đã gây ra các tác dụng phụ không mong muốn:
    - Làm mất khả năng hiển thị danh sách file trong các công cụ quản lý file (Obsidian/File Explorer) do xung đột quyền List Directory.
    - Gây khó khăn cho trải nghiệm người dùng (UX) khi cần kiểm tra trực quan các tệp tin thô.
- Cơ chế **Session Lock** tuy an toàn về mặt kỹ thuật nhưng làm phức tạp hóa luồng thực thi trong môi trường tương tác.

## 2. Quyết định (Decisions)
- **Rollback**: Gỡ bỏ hoàn toàn các ràng buộc ACL (`icacls /remove:d`) trên các thư mục `3-resources/raw_*`.
- **Simplification**: Loại bỏ cơ chế `session.lock` và kiểm tra biến môi trường bắt buộc trong `promote.py` để khôi phục tính linh hoạt.
- **Retention**: GIỮ LẠI logic **Routing & Flattening** trong `promote.py` vì đây là cấu trúc hạ tầng đúng đắn, không gây ảnh hưởng đến UX.

## 3. Bài học (Learnings)
- Các biện pháp bảo mật mức OS (ACL) quá mạnh có thể gây cản trở các luồng làm việc tích hợp (integrated workflows) và các công cụ bên thứ ba (Obsidian).
- Nên ưu tiên các biện pháp bảo mật mức Agent (Rules R1-R23) và kiểm tra logic (Origin/Audit Check) thay vì khóa cứng quyền truy cập của người dùng trên chính máy tính của họ.

## 4. Trạng thái hiện tại
- Kho lưu trữ `raw_*` đã có thể truy cập bình thường.
- `promote.py` hoạt động ở chế độ mở (Open), vẫn thực hiện audit check nhưng không yêu cầu lock file.
