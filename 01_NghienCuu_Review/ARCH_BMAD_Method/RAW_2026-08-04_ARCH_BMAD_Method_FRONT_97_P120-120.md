# HD SOURCE: ARCH_BMAD_Method_FRONT_97_P120-120
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_97
Part Title: NONE
Chapter Title: NONE
Section Title: Định dạng đầu ra JSON
Chunk Range: Pages 120 to 120
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Các loại edge case phổ biến bị bắt gặp

| Loại                  | Môtả                                 | Ví dụcụthể                                   |
|-------------------------|----------------------------------------|---------------------------------------------------|
| Thiếu else            | Nhánh không cófallback                | `if (isLoggedIn) {...}` - không cóelse           |
| Đầu vào không validate | Input chưa kiểmtra                    | Hàm nhận string không có sanitize               |
| Off-by-one              | Điều kiện ranh giới sai           | `index < array.length` vs `index <= array.length` |
| Tràn số học          | Giới hạn sốnguyên vượt          | `uint32` overflow khi cộng dồn số lớn      |
| Ép kiểu ngầm        | Type mismatch                          | `"5" == 5` true trong JavaScript                  |
| Race condition          | Thay đổi state đồng thời            | Hai requests cùng modify cùng record              |
| Thiếu timeout         | Không có giới hạn thời gian chờ | HTTP request không cótimeout                     |
| Vòng lặp vôtận     | Điều kiện thoát không đạt được      | while loop với điều kiện không bao giờfalse |

## Định dạng đầu ra JSON

Mỗi finding trả vềobject với bốn trường:

```
[ { "location": "auth/token.ts:47", "trigger_condition": "Hai requests refresh đồng thời với cùng refresh token", "guard_snippet": null, "potential_consequence": "Hai access tokens hợp lệ được cấp, tấn công replay token cóthể xảy ra" }, { "location": "users/repository.ts:23", "trigger_condition": "userId là chuỗi rỗng hoặc chỉ có khoảng trắng", "guard_snippet": "if (!userId)", "potential_consequence": "Guard không bắt chuỗi chỉ cówhitespace, query DB với giátrị không hợp lệ " } ]
```

## Giải thích bốn trường:

location : File và dòng  nơi đường đi chưa được xử lý