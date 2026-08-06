# HD SOURCE: ARCH_BMAD_Method_FRONT_121_P140-140
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_121
Part Title: NONE
Chapter Title: NONE
Section Title: 12.4 công cụ 3: Bmad-index-docs - tạo chỉmục
Chunk Range: Pages 140 to 140
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Tóm tắt (Summary): Chọn thông tin quan trọng, bỏ phần còn lại → Mất thông tin.

Distillate: Toàn bộthông tin được bảo toàn, chỉ được chuyển đổi sang format dày đặc hơn → Không mất thông tin.

Ví dụ :

```
Tài liệu gốc (120 dòng văn xuôi): "Hệthống xác thực sẽ sử dụng JSON Web Token. Access token sẽ cóthời gian sống làmười lăm phút. Điều này cân bằng giữa bảo mật và trải nghiệm người dùng. Refresh token sẽ cóthời gian sống là bảy ngày..." (tiếp tục chi tiết trong nhiều đoạn) Distillate (8 dòng bullet points): - Xác thực: JWT, access=15min, refresh=7ngày httpOnly-cookie - Rate limiting: 5 lần sai/15min → khóa - Password: bcrypt rounds=12, min 8 chars - Sessions: Redis store, timeout 30min inactive
```

Tất cả thông tin vẫnở đó -  không bịmất  -  chỉ ở dạng cô đọng hơn.

## Tham số quan trọng: Downstream\_consumer

Khi bạn cung cấp downstream\_consumer , AI biếtưu tiên loại thông tin nào khi nén:

```
bmad-distillator source_documents: ./research/ downstream_consumer: "Tạo PRD  -  Architect cần biết tech constraints" token_budget: "Giảm còn 30% kích thước gốc" --validate
```

Nếu bạn không cung cấp downstream\_consumer , AI nén tổng quát  -  cóthể giảm bớt thông tin quan trọng với downstream workflow.

## Xác nhận tính lossless

Flag --validate chạy kiểm tra vòng tròn:

```
1. Nén tài liệu gốc → Distillate 2. Tái tạo tài liệu từ distillate → Tài liệu phục hồi 3. So sánh tài liệu gốc ↔ Tài liệu phục hồi 4. Report: Tỷ lệphần trăm thông tin được bảo toàn
```

Sử dụng --validate cho tài liệu quan trọng nhưPRD vàArchitecture Document.

## 12.4 công cụ 3: Bmad-index-docs  -  tạo chỉmục