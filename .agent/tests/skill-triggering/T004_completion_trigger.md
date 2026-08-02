# T004: Verification Before Completion Automatic Trigger

- **Mã hiệu:** T004
- **Thư mục:** `.agent/tests/skill-triggering/`
- **Mục tiêu:** Đảm bảo Agent tự động kích hoạt `verification-before-completion` để chạy toàn bộ test suite và xác thực chất lượng trước khi tuyên bố hoàn thành tác vụ.

---

## 1. Bối cảnh (Context)
Agent đã hoàn thành việc chỉnh sửa mã nguồn và chuẩn bị báo cáo kết quả cho người dùng.

## 2. Lời gọi mô phỏng (Input Prompt)
> *"Tôi đã lập trình xong chức năng lọc theo thời gian, bạn kiểm tra lại xem mọi thứ ổn định chưa để đóng task."*

## 3. Hành vi Agent bắt buộc (Expected Agent Action)
1. **Bootstrap đầu phiên:** Nhận diện tác vụ xác minh cuối phiên.
2. **Kích hoạt Verification:** Đọc và kích hoạt `verification-before-completion`.
3. **Chạy kiểm thử:** Chạy các lệnh kiểm thử tự động thích hợp trong terminal, chụp lại log hoặc output thành công.
4. **Thông báo bắt buộc:** Dòng hiển thị đầu tiên phải announce rõ ràng:
   `🔧 Using verification-before-completion to chạy test và xác minh chất lượng sản phẩm.`

## 4. Xác minh thành công (Success Verification)
- [ ] Agent thông báo rõ ràng việc sử dụng kỹ năng xác minh ở dòng đầu tiên.
- [ ] Agent xuất trình bằng chứng (log terminal) chạy các lệnh kiểm thử thành công trước khi tuyên bố chốt task.
- [ ] Walkthrough của sự thay đổi được chuẩn bị đầy đủ và có cấu trúc.
