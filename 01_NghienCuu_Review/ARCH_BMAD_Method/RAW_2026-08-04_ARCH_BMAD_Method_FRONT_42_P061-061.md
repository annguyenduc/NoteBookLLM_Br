# HD SOURCE: ARCH_BMAD_Method_FRONT_42_P061-061
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_42
Part Title: NONE
Chapter Title: NONE
Section Title: Môtả Chunk Range: Pages 61 to 61
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Dùng cả hai để cócoverage toàn diện.

## Các loại edge cases được kiểm tra

| Loại edge case              | Môtả                         | Ví dụ                                    |
|-------------------------------|--------------------------------|-------------------------------------------|
| Thiếu else/default          | Nhánh không cófallback        | Switch không cócase default              |
| Đầu vào không được bảo vệ | Input người dùng chưa validate | Hàm nhận chuỗi chưa sanitize           |
| Off-by-one                    | Điều kiện biên              | `< array.length` vs `<= array.length`     |
| Tràn số học                | Giới hạn sốnguyên        | Integer overflow trong tính toán          |
| Ép kiểu ngầm định         | Type mismatch                  | JavaScript `"5" == 5`                     |
| Race condition                | Thay đổi đồng thời          | Async operations cùng modify shared state |
| Khoảng trống timeout      | Thiếu xử lýtimeout         | API call không cótimeout                 |

## Quy trình

```
1. Liệt kêtất cả các đường rẽ (if/else, switch, try/catch, ternary) 2. Phân loại cơhọc các edge classes từmỗi nhánh 3. Kiểm tra từng đường đi với các guards hiện có 4. Chỉ báo cáo các đường đi CHƯA ĐƯỢC XỬ LÝ  -  âm thầm bỏ qua các trường hợp đã xử lý
```

## Định dạng đầu ra JSON

```
[ { "location": "auth/jwt.ts:47", "trigger_condition": "Hai requests refresh đồng thời với cùng refresh token", "guard_snippet": null, "potential_consequence": "Hai access token hợp lệ được cấp, tấn công replay cóthể xảy ra" } ]
```

Mỗi finding có bốn trường: vịtrí, điều kiện kích hoạt, đoạn guard (null nếu không có guard), và hậu quả tiềmẩn.

## 4.9 bmad-editorial-review-prose  -  biên tập văn xuôi

## Môtả