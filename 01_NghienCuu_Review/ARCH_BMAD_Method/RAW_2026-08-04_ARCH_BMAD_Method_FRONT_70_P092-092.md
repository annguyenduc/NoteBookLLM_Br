# HD SOURCE: ARCH_BMAD_Method_FRONT_70_P092-092
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_70
Part Title: NONE
Chapter Title: NONE
Section Title: Cấu trúc story chuẩn
Chunk Range: Pages 92 to 92
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 7.6 epics và stories

```
bmad-create-epics-and-stories # Ch
```

```
ạy sau khi đã cóarchitecture.md
```

## Epic vs story

Epic = Nhóm công việc liên quan hướng đến một mục tiêu cụthể Ví dụ :

"Epic 1: Xác thực và phân quyền ngườ

"Epic 2: Bảng điều khiển dữ liệ

"Epic 3: Báo cáo và xuất dữ liệ Story = Đơn vịcông việc cóthể triển khai trong mộ

```
i dùng" u" u" t session
```

Story không phải danh sách nhiệm vụ -  nó là đơn vị giátrị kinh doanh với đủ bối cảnh để Developer Agent triển khai mà không cần hỏi thêm câu hỏi.

## Cấu trúc story chuẩn

```
# Story 1.2: Triển khai làm mới JWT token ## Trạng thái: Sẵn sàng phát triển ## User story Với tưcách làngười dùng đã đăng nhập, Tôi muốn session tự động được gia hạn, Để tôi không bị đăng xuất trong khi đang dùng app. ## Tiêu chíchấp nhận - [ ] Access token hết hạn sau 15 phút - [ ] Refresh token hết hạn sau 7 ngày - [ ] Khi access token hết hạn, hệthống tự động request token mới - [ ] Nếu refresh token hết hạn, chuyển hướng đến trang đăng nhập -[ ] Người dùng KHÔNG bao giờ thấy lỗi "phiên đã hết hạn" khi đang dùng ## Ghi chú kỹ thuật - Dùng architecture ADR-001 (cách tiếp cận JWT được documentở đó) - Theo pattern xử lý lỗi trong project-context.md - Endpoint: POST /auth/refresh-token -Lưu refresh token trong httpOnly cookie (không phải localStorage  yêu cầu bảo mật từ PRD NFR-002) ## Phụthuộc - Story 1.1 (luồng đăng nhập) phải hoàn thành trước ## Định nghĩa hoàn thành - Tất cả tiêu chíchấp nhận đã đápứng - Unit tests cho logic làm mới token - Integration test cho luồng session hết hạn -Code review đã thông qua
```