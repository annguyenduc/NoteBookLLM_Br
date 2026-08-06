# HD SOURCE: ARCH_BMAD_Method_FRONT_94_P117-117
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_94
Part Title: NONE
Chapter Title: NONE
Section Title: Bạn phải lọc kết quả Chunk Range: Pages 117 to 117
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Có ba lý do:

## Lý do 1  -  Kháng cựthiên kiến xác nhận:

Review thông thường dễ bịmắc kẹt bởi thiên kiến xác nhận (confirmation bias)  đọc lướt, không thấy gìnổi bật, approve. Quy tắc "bắt buộc tìm vấn đề " phá vỡ pattern đó hoàn toàn.

## Lý do 2  -  Phát hiện những gì còn thiếu:

Hầu hết reviews tập trung vào "cái gì sai". Review Đối nghịch chủ động hỏi "cái gì KHÔNG có?"  đây là loại vấn đề khónhận thấy nhất.

## Lý do 3  -  Tạo ra sựmất cân bằng cóchủ đích:

Hầu hết quátrình tạo artifact đã được biased về phía "tốt đẹp và hoàn chỉnh". Một review cốtình biased theo hướng ngược lại tạo ra sựcân bằng.

## Khung phân loại severity

```
NGHIÊM TRỌNG   → Lỗi logic, lỗ hổng bảo mật, data corruption tiềmẩn → Phải sửa ngay, không merge nếu chưa sửa CAO             → Vi phạm kiến trúc, thiếu error handling quan trọng → Nên sửa trước khi merge, hoặc tạo ticket ngay lập tức TRUNG BÌNH      → Cải thiện hiệu năng, vi phạm quyước nhỏ → Sửa hoặc tạo tech debt ticket THẤP            → Tái cấu trúc nhỏ , cải thiện đặt tên → Tùy chọn, cóthể ghi nhận và xử lý sau
```

## Bạn phải lọc kết quả Tài liệu chính thức nhấn mạnh:

"VìAI được hướng dẫn tìm vấn đề , nó SẼ tìm ra vấn đề -  kể cả khi không tồn tại. Hãy kỳ vọng false positives: những soi mói nhỏnhặt được ngụy trang thành vấn đề , hiểu lầm về ý định, hoặc lo lắng hoàn toàn do AI tưởng tượng ra. Bạn quyết định cái gì là thật."

## Quy trình lọc:

```
Đọc mỗi finding ↓ Hỏi: Đây là vấn đề thật hay false positive? │ ├─ Thật → Phân loại severity → Sửa hoặc track │ └─ False positive → Ghi chútại sao → Bỏ qua
```