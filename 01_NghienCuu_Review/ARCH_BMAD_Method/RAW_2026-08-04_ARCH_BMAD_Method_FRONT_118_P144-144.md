# HD SOURCE: ARCH_BMAD_Method_FRONT_118_P144-144
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_118
Part Title: NONE
Chapter Title: NONE
Section Title: 12.8 kết hợp ba công cụ: Kịch bản thực tếChunk Range: Pages 144 to 144
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 12.7 project-context.md  -  quản lý đặc biệt

File project-context.md làmột trường hợp đặc biệt cần quy tắc riêng:

## Không sharding

File này phải làmột single file  tám workflows khác đọc nó, và chúng mong đợi một file đơn. Không bao giờ chia nhỏ project-context.md .

## Giữnhỏ gọn

Mục tiêu: Dưới ba trăm dòng. Nếu vượt quá: Loại bỏentries lỗi thời Tóm tắt các quy tắc quáchi tiết Xem xét distillate nếu cần giữ thông tin

## Cập nhật thường xuyên

Mỗi retrospective là cơhội: Thêm patterns mới được khám phátrong sprint Cập nhật quyước đã được cải tiến Loại bỏ quy tắc không còn relevant

## Template kiểm tra chất lượng

Sau mỗi lần cập nhật, tự hỏi: Developer Agent đọc file này có biết đủ để bắt đầu triển khai không? Cóthông tin nào lỗi thời cần xóa không? Có quyước nào team đang dùng nhưng chưa document chưa?

## 12.8 kết hợp ba công cụ : Kịch bản thực tế Kịch bản: Dự án analytics dashboard sau sáu tháng phát triển.

## Hiện trạng:

```
architecture.md : Tám trăm dòng Thưmục research/ : Mười hai files, tổng cộng ba nghìn dòng sprint-status.yaml : Rất lớn với tất cả stories đã hoàn thành Không cóindex nào trong _bmad-output/
```

## Quy trình xử lý: