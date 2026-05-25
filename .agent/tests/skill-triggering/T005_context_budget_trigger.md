# T005: Context Budget Automatic Trigger

- **Mã hiệu:** T005
- **Thư mục:** `.agent/tests/skill-triggering/`
- **Mục tiêu:** Đảm bảo Agent tự động kích hoạt `cm-context-budget` khi số lượng tệp tin liên quan quá lớn hoặc có dấu hiệu phình context đầu phiên, nhằm tối ưu hóa chi phí token và tránh quá tải context window.

---

## 1. Bối cảnh (Context)
Lịch sử hội thoại dài, hoặc người dùng yêu cầu phân tích một danh sách lớn hàng chục tệp tin cùng lúc.

## 2. Lời gọi mô phỏng (Input Prompt)
> *"Hãy kiểm tra toàn bộ cấu trúc của 14 kỹ năng trong thư mục workspaces/refs/superpowers/skills/ và 7 nhóm test để xem kỹ năng nào có thể gộp lại được."*

## 3. Hành vi Agent bắt buộc (Expected Agent Action)
1. **Bootstrap đầu phiên:** Phát hiện yêu cầu xử lý lượng thông tin cực kỳ đồ sộ có nguy cơ gây context bloat.
2. **Kích hoạt Context Budget:** Đọc và kích hoạt `cm-context-budget`.
3. **Phân tích ngân sách Token:** Ước lượng dung lượng token của các file cần đọc, đề xuất phương án đọc từng phần hoặc lọc file trước khi dùng `view_file` hàng loạt.
4. **Thông báo bắt buộc:** Dòng hiển thị đầu tiên phải announce rõ ràng:
   `🔧 Using cm-context-budget to kiểm tra và tối ưu hóa ngân sách Token đầu phiên.`

## 4. Xác minh thành công (Success Verification)
- [ ] Agent thông báo rõ ràng việc sử dụng kỹ năng quản lý token budget ở dòng đầu tiên.
- [ ] Agent đề xuất một danh mục đọc có chọn lọc, tuyệt đối không gọi `view_file` hay `read_file` vô tội vạ trên tất cả các file cùng lúc.
