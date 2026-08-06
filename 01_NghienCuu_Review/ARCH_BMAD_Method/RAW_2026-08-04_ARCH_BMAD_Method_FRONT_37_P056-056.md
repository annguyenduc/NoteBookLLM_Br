# HD SOURCE: ARCH_BMAD_Method_FRONT_37_P056-056
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_37
Part Title: NONE
Chapter Title: NONE
Section Title: Tham số đầu vào
Chunk Range: Pages 56 to 56
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Distillate: Không mất thông tin. Toàn bộthông tin được bảo toàn, chỉ được chuyển đổi sang định dạng dày đặc hơn, ít token hơn.

Ví dụminh họa:

Đầu vào (văn xuôi dài):

```
Tính năng xác thực sẽ sử dụng JSON Web Token với thời gian sống của access token làmười lăm phút. Refresh token sẽ cóthời gian sống là bảy ngày và phải được lưu trữ trong httpOnly cookie để tránh XSS. Rate limiting sẽ đượcáp dụng: tối đa năm lần thử sai trong mười lăm phút trước khi tài khoản bịtạm khóa.
```

Distillate (giữnguyên thông tin, ít token hơn):

```
- Xác thực: JWT, access=15min, refresh=7ngày httpOnly-cookie - Rate limiting: max 5 lần sai/15min → khóa tài khoản
```

Tỷ lệnén điển hình: 2:1 đến 4:1, không cóthông tin bịmất.

## Cơchế hoạt động

- Bước 1  -  Phân tích: Đọc tài liệu nguồn, xác định mật độthông tin và cấu trúc.

- Bước 2  -  Nén: Chuyển đổi văn xuôi thành bullet points dày đặc, loại bỏ định dạng trang trí.
- Bước 3  -  Xác minh nội bộ : Kiểm tra tính đầy đủ -  tất cả thông tin gốc còn đủ không?

Bước 4  -  Kiểm tra vòng tròn (tùy chọn): Với flag --validate -  tái tạo tài liệu gốc từ distillate và so sánh. Nếu thông tin cóthể được tái tạo đầy đủ, distillate được xác nhận là lossless.

## Tham số đầu vào

| Tham số              | Bắt buộc   | Ví dụ                                                | Môtả                                           |
|-----------------------|----------------|-------------------------------------------------------|--------------------------------------------------|
| `source_documents`    | Có             | `./research/market- research.md` hoặc `./research/` | Đường dẫn file, thưmục, hoặc glob pattern |
| `downstream_consumer` | Không          | `"Tạo PRD"`, `"Thiết kế kiến trúc"`            | AI biếtưu tiên loại thông tin nào             |
| `token_budget`        | Không          | `"Giảm50% kích thước"`                             | Kích thước đích xấp xỉ                         |