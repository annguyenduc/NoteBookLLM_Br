# T003: Test-Driven Development Automatic Trigger

- **Mã hiệu:** T003
- **Thư mục:** `.agent/tests/skill-triggering/`
- **Mục tiêu:** Đảm bảo Agent tự động kích hoạt `test-driven-development` (hoặc `cm-tdd` cũ) để thiết kế kịch bản test trước khi viết mã nguồn logic cho bất kỳ hàm hoặc module mới nào.

---

## 1. Bối cảnh (Context)
Người dùng yêu cầu lập trình một hàm tiện ích, một lớp hoặc một module logic độc lập mới.

## 2. Lời gọi mô phỏng (Input Prompt)
> *"Hãy viết một hàm utils trong python để kiểm tra xem một chuỗi mật khẩu có đủ mạnh hay không (tối thiểu 8 ký tự, có chữ hoa, chữ thường và chữ số)."*

## 3. Hành vi Agent bắt buộc (Expected Agent Action)
1. **Bootstrap đầu phiên:** Nhận diện tác vụ tạo hàm logic mới.
2. **Kích hoạt TDD:** Đọc và kích hoạt `test-driven-development` (hoặc `cm-tdd` cũ).
3. **Quy trình TDD bắt buộc:**
   - Bước 1: Thiết kế kịch bản test kiểm thử (mô tả các input kiểm thử và expected output).
   - Bước 2: Viết mã nguồn kiểm thử chạy fail (RED).
   - Bước 3: Chỉ sau khi test fail được tạo lập, mới viết mã nguồn chính để đạt GREEN.
4. **Thông báo bắt buộc:** Dòng hiển thị đầu tiên phải announce rõ ràng:
   `🔧 Using test-driven-development to thực hiện quy trình kiểm thử trước khi lập trình.`

## 4. Xác minh thành công (Success Verification)
- [ ] Agent thông báo rõ ràng việc sử dụng kỹ năng TDD ở dòng đầu tiên.
- [ ] Agent xuất trình mã nguồn kiểm thử và kịch bản test trước khi viết mã nguồn chính.
- [ ] Quy trình self-healing đệ quy tự chạy kiểm thử được chuẩn bị sẵn sàng.
