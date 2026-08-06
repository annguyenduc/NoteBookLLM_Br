# HD SOURCE: ARCH_BMAD_Method_FRONT_100_P123-123
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_100
Part Title: NONE
Chapter Title: NONE
Section Title: Không phải review - là cải thiện
Chunk Range: Pages 123 to 123
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Tham số reader\_type

Tham sốnày xác định đang viết cho ai vàoptimizer cho mục tiêu nào:

| Giátrị              | Tốiưu cho                                         | Áp dụng khi                              |
|-----------------------|-----------------------------------------------------|--------------------------------------------|
| `humans` (mặc định) | Sự rõ ràng, luồng đọc, khảnăng scan            | Tài liệu người đọc: PRD, docs, readme    |
| `llm`                 | Sựchính xác, nhất quán, tham chiếu không mơhồ | Prompts, system instructions, specs cho AI |

Khi viết spec cho agent đọc: reader\_type: llm .

Khi viết PRD cho PM và developer đọc: reader\_type: humans .

## Định dạng đầu ra: Bảng ba cột

```
| Văn bản gốc                              | Văn bản sửa               | Thay đổi | |------------------------------------------|---------------------------|------------------------| | "Điều quan trọng cần lưuý làngười dùng | "Người dùng phải xác nhận | Bỏ câu đệm mở đầu | |  phải xác nhận email của họtrước khi..." |  email trước khi..."       | Rút ngắn 40% | |                                          |                           | | | "Mặc dù cóthể hơi phức tạp nhưng chức  | "Chức năng này yêu cầu    | Bỏ qualifier không cần | |  năng này cóthểyêu cầu..."             | ..."                       | Câu trực tiếp hơn      |
```

Bảng này giúp bạn dễ dàng đánh giátừng thay đổi và áp dụng cóchọn lọc.

## 10.6 advanced elicitation  làm sâu đầu ra

bmad-advanced-elicitation

## Không phải review  -  là cải thiện

Advanced Elicitation khác với bốn công cụ reviewở điểm then chốt này: Nó không tìm vấn đề trong đầu ra hiện tại  -  nó làm sâu thêm và cải thiện đầu ra bằng cácháp dụng một phương pháp tưduy cụthể .

Tài liệu giải thích: