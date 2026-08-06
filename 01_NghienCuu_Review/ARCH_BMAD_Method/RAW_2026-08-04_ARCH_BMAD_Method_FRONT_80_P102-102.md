# HD SOURCE: ARCH_BMAD_Method_FRONT_80_P102-102
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_80
Part Title: NONE
Chapter Title: NONE
Section Title: Cập nhật sau mỗi story
Chunk Range: Pages 102 to 102
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Bắt buộc tìm ra vấn đề -  không thểapprove mà không tìm thấy gì.

## Phân loại severity:

Nghiêm trọng: Lỗi logic, lỗ hổng bảo mật, data corruption tiềmẩn  -  phải sửa ngay Cao: Vi phạm kiến trúc, thiếu error handling quan trọng  -  nên sửa trước khi merge Trung bình: Cải thiện hiệu năng, vi phạm quyước  -  sửa hoặc tạo tech debt ticket Thấp: Tái cấu trúc code nhỏ -  tùy chọn

Lọc kết quả là trách nhiệm của bạn  -  AI sẽ tìm ra cả vấn đề thật vàfalse positives. Phân biệt và quyết định cái nào cần sửa.

## Ví dụphân loại

```
THẬT  -  Nghiêm trọng: auth/middleware.ts:47  -  Không có rate limiting cho endpoint refresh Tấn công brute force cóthể làm tràn database THẬT  -  Cao: user/service.ts:23  Error type không đúng (AppError vs Error thô) Vi phạm pattern xử lý lỗi trong project-context FALSE POSITIVE (lọc bỏ ): "apiClient.ts cóthể refactor sang async/await" Code dùng Promises nhất quán với phần còn lại  -  không phải vấn đề
```

## 8.6 quản lýtiến độ sprint

```
bmad-sprint-status # Hoặc: bmad-agentdev  → gõ "SS" hoặ
```

```
c "SP"
```

## Kiểm tra trạng thái thường xuyên

Chạy bmad-sprint-status để cócái nhìn tổng quan:

Những story nào đã hoàn thành?

Story nào đang chặn bởi dependencies?

Sprint cóon track không?

Có gì cần điều chỉnh scope không?

## Cập nhật sau mỗi story

Sau khi hoàn thành mỗi story:

Developer Agent cập nhật sprint-status.yaml (thường tự động)