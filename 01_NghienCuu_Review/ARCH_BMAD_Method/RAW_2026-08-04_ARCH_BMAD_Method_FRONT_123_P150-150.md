# HD SOURCE: ARCH_BMAD_Method_FRONT_123_P150-150
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_123
Part Title: NONE
Chapter Title: NONE
Section Title: Quick flow - cho thay đổi nhỏ, rõ ràng
Chunk Range: Pages 150 to 150
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

"Feature flags được quản lý qua LaunchDarkly, không hardcode"

"Transaction amounts luôn stored làintegers (cents, không phải dollars)"

"Business rule: Không bao giờ xóa user  -  chỉ soft delete với deleted\_at" Những thứnày không nhìn thấy từ code nhưng là "common knowledge" trong team -  và chính xác là thứcác agents cần biết.

## Bước 3: Lấy hướng dẫn

```
bmad-help # Hoặc hỏi bằng ngôn ngữ tựnhiên: bmad-help Tôi cómộtứng dụng Rails hiện có, tôi nên bắt đầu từ đâu? bmad-help Sự khác biệt giữa quick-flow vàfull method là gì? bmad-help Tôi muốn thêm tính năng mới vào app đang chạy
```

bmad-help quét project của bạn, nhìn thấy những gì đã tồn tại, và đề xuất bước tiếp theo phù hợp nhất.

## 13.3 chọn cách tiếp cận: Quick flow hay full method?

Sau khi setup xong, dự án hiện cócó hai cách tiếp cận chính cho công việc ongoing:

## Quick flow  cho thay đổi nhỏ , rõ ràng

bmad-quick-dev

## Phù hợp nhất khi:

Bug fix với nguyên nhân đã biết rõ Thêm tính năng nhỏ với requirements hoàn toàn rõ ràng

Refactoring trong phạm vi xác định

Configuration changes

Tài liệu chính thức về Quick Flow cho dự án hiện có:

"Quick Flow hoạt động tốt cho dự án hiện có. Nó sẽ tự động phát hiện tech stack hiện có, phân tích patterns code hiện có, phát hiện quyước và hỏi xác nhận, tạo spec phong phú về bối cảnh tôn trọng code hiện có."

Điểm đặc biệt: Quick Dev không chỉ generate code  -  nó hỏi bạn xác nhận conventions nóphát hiện được trước khiáp dụng. Ví dụ :

```
Quick Dev phát hiện: "Codebase này dùng Promises (không phải async/await) nhất quán. Tôi cónên theo pattern này cho implementation mới không?" Bạn: Có (maintain consistency) hoặc Không (establish new standard, document why)
```