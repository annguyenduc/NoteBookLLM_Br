# HD SOURCE: ARCH_BMAD_Method_FRONT_40_P059-059
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_40
Part Title: NONE
Chapter Title: NONE
Section Title: Lọc kết quả: Trách nhiệm của bạn
Chunk Range: Pages 59 to 59
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

"Bạn bắt buộc phải tìm ra vấn đề . Không tìm thấy vấn đềnào sẽ kích hoạt trạng thái dừng  -  phân tích lại hoặc giải thích tại sao."

Đây là điểm khác biệt căn bản so với review thông thường: reviewer thông thường cóthểapprove nếu không thấy gì rõ ràng. Review đối nghịch bắt buộc phải tìm ra vấn đề -  zero findings không được phép.

## Tại sao điều này hiệu quả ?

Review thông thường thất bại vì thiên kiến xác nhận : Bạn đọc lướt qua, không thấy gìnổi bật, gật đầu approve. Review đối nghịch phá vỡ pattern đótheo ba cách:

Tính cưỡng bức toàn diện: Không thểapprove cho đến khi tìm đủ vấn đề .

Bắt những gì còn thiếu: Câu hỏi "Cái gì KHÔNG có ở đây?" trở thành câu hỏi tựnhiên.

Thông tin bất đối xứng: Review được thực hiện với bối cảnh mới đánh giátài liệu, không đánh giá ý định của người tạo.

## Ví dụthực tế Review thông thường:

"Cách triển khai xác thực này trôngổn. Đã duyệt."

## Review đối nghịch:

```
1. NGHIÊM TRỌNG  -  login.ts dòng 47  -  Không có rate limiting cho các lần thất bại Tác động: Tấn công brute force dễ dàng thực hiện Cách sửa: Thêm rate limiter middleware, tối đa 5 lần/15 phút 2. NGHIÊM TRỌNG  Session token lưu trong localStorage Tác động: Tấn công XSS cóthể đánh cắp token Cách sửa: Chuyển sang httpOnly cookie 3. TRUNG BÌNH  -  Validation mật khẩu chỉ ở phía client Tác động: Gọi API trực tiếp bỏ qua validation Cách sửa: Cần validation phía server 4. TRUNG BÌNH  -  Không cóaudit log cho các lần đăng nhập thất bại Tác động: Không phát hiện được các sựcố bảo mật 5. THẤP  -  Magic number 3600 nên là hằng số SESSION_TIMEOUT_SECONDS
```

## Lọc kết quả : Trách nhiệm của bạn

Tài liệu chính thức lưuý quan trọng: