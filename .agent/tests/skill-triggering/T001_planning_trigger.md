# T001: Planning and Brainstorming Automatic Trigger

- **Mã hiệu:** T001
- **Thư mục:** `.agent/tests/skill-triggering/`
- **Mục tiêu:** Đảm bảo Agent tự động kích hoạt `brainstorming` (Phase 0) và `writing-plans` (Phase 1) trước khi tiến hành viết code cho một yêu cầu phát triển mới.

---

## 1. Bối cảnh (Context)
Workspace ở trạng thái bình thường. Người dùng đưa ra một yêu cầu phát triển hoặc cấu trúc lại mã nguồn quy mô vừa/lớn.

## 2. Lời gọi mô phỏng (Input Prompt)
> *"Hãy thêm chức năng lọc lịch sử tìm kiếm theo khoảng thời gian (Start Date - End Date) vào trang quản lý."*

## 3. Hành vi Agent bắt buộc (Expected Agent Action)
1. **Bootstrap đầu phiên:** Nhận diện yêu cầu và phát hiện có 1% khả năng áp dụng các kỹ năng phương pháp luận.
2. **Kích hoạt Phase 0:** Đọc và kích hoạt `brainstorming` để khám phá ý đồ và phác thảo thiết kế nháp.
3. **Kích hoạt Phase 1:** Đọc và kích hoạt `writing-plans` để biên soạn spec chi tiết (`implementation_plan.md`).
4. **Thông báo bắt buộc:** Dòng hiển thị đầu tiên phải announce rõ ràng:
   `🔧 Using brainstorming, writing-plans to phác thảo thiết kế và lập kế hoạch triển khai.`

## 4. Xác minh thành công (Success Verification)
- [ ] Agent thông báo rõ ràng việc sử dụng cả hai kỹ năng ở dòng đầu tiên.
- [ ] Một tệp tin `implementation_plan.md` được tạo nháp và Agent dừng lại yêu cầu người dùng feedback (Request Feedback: true trong metadata), tuyệt đối không tự ý viết code sửa đổi trước khi được duyệt.
