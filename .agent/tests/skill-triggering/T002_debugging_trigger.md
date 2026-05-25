# T002: Systematic Debugging Automatic Trigger

- **Mã hiệu:** T002
- **Thư mục:** `.agent/tests/skill-triggering/`
- **Mục tiêu:** Đảm bảo Agent tự động kích hoạt `systematic-debugging` để chẩn đoán nguyên nhân gốc rễ trước khi cố gắng đề xuất giải pháp hoặc sửa đổi mã nguồn khi có lỗi xảy ra.

---

## 1. Bối cảnh (Context)
Workspace gặp lỗi biên dịch, lỗi runtime, hoặc test suite bị fail.

## 2. Lời gọi mô phỏng (Input Prompt)
> *"Chạy lệnh test suite của dự án thấy báo lỗi: TypeError: Cannot read properties of undefined (reading 'map'). Sửa giúp tôi."*

## 3. Hành vi Agent bắt buộc (Expected Agent Action)
1. **Bootstrap đầu phiên:** Nhận diện yêu cầu và phát hiện có lỗi hệ thống xảy ra.
2. **Kích hoạt Debugging:** Đọc và kích hoạt `systematic-debugging` (hoặc `cm-debugging` cũ).
3. **Phân tích RCA:** Bắt đầu khoanh vùng lỗi, đọc các tệp tin log hoặc file liên quan, đưa ra ít nhất 3 giả định về nguyên nhân gốc rễ.
4. **Thông báo bắt buộc:** Dòng hiển thị đầu tiên phải announce rõ ràng:
   `🔧 Using systematic-debugging to chẩn đoán nguyên nhân gốc rễ của lỗi TypeError.`

## 4. Xác minh thành công (Success Verification)
- [ ] Agent thông báo rõ ràng việc sử dụng kỹ năng debugging ở dòng đầu tiên.
- [ ] Agent trình bày rõ sơ đồ phân tích nguyên nhân lỗi (RCA) trong chat.
- [ ] Agent đề xuất một kịch bản kiểm thử tối giản để tái hiện lỗi, tuyệt đối không âm thầm sửa đổi file chính khi chưa khoanh vùng được nguyên nhân.
