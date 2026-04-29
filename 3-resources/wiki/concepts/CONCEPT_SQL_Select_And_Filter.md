---
title: "CONCEPT: SQL Select & Filter"
type: concept
domain: SQL
status: verified
sources:
  - "TOOL_SQL_Getting_Started.md"
tags: [sql, select, where, null, filtering]
created: 2026-04-29
updated: 2026-04-29
---

# 🧠 Khái niệm: SQL Select & Filter (Truy xuất và Lọc dữ liệu)

## 1. Định nghĩa
`SELECT` là câu lệnh cơ bản và quan trọng nhất trong SQL, dùng để trích xuất dữ liệu từ các bảng. Mệnh đề `WHERE` đi kèm dùng để lọc và chỉ giữ lại những bản ghi thỏa mãn điều kiện nhất định.
Việc lọc dữ liệu chính là thao tác đầu tiên trong quy trình Data Preparation của một Data Analyst.

📖 Nguồn: `TOOL_SQL_Getting_Started.md` — [Page 36-38, Page 86-90]

## 2. Kỹ thuật Lọc (Filtering) & Xử lý NULL
Trong mệnh đề `WHERE`, ta có thể sử dụng:
- Các toán tử logic: `AND`, `OR`, `IN`.
- Dữ liệu rỗng (`NULL`): Bắt buộc dùng `IS NULL` hoặc `IS NOT NULL`, không được dùng dấu bằng (`= NULL`).

## 3. Ví dụ minh họa (Rule 17: Double Examples)

### Ví dụ 1: Truy xuất cơ bản, tính toán cột mới (Expressions) và Lọc số
```sql
-- Lấy thông tin sản phẩm và tính toán giá sau thuế (TAXED_PRICE)
-- Chỉ giữ lại các sản phẩm có giá gốc trên 50
SELECT
    PRODUCT_ID,
    DESCRIPTION,
    PRICE,
    PRICE * 1.07 AS TAXED_PRICE
FROM PRODUCT
WHERE PRICE > 50;
```
*(Giải thích: Cột `TAXED_PRICE` được tính toán động (dynamically calculated) lúc chạy truy vấn nhờ alias `AS`. Nó không được lưu vật lý trong database).*
📖 Nguồn: `TOOL_SQL_Getting_Started.md` — [Page 39-41]

### Ví dụ 2: Lọc văn bản, điều kiện IN và xử lý NULL
```sql
-- Lấy danh sách khách hàng sống tại TX hoặc CA
-- Và bắt buộc phải có địa chỉ email (không được để trống)
SELECT 
    CUSTOMER_ID, 
    NAME, 
    STATE
FROM CUSTOMER
WHERE STATE IN ('TX', 'CA')
  AND EMAIL IS NOT NULL;
```
*(Giải thích: `IN ('TX', 'CA')` là cách viết ngắn gọn của `STATE = 'TX' OR STATE = 'CA'`. Kiểm tra trống dùng `IS NOT NULL` thay vì `!= NULL`).*
📖 Nguồn: `TOOL_SQL_Getting_Started.md` — [Page 89-92]

## 4. Gotchas / Pitfalls (Những lỗi thường gặp)
- **Quên ưu tiên ngoặc**: Khi kết hợp `AND` và `OR` trong mệnh đề `WHERE`, luôn dùng ngoặc `()` để bọc nhóm điều kiện. Nếu không, hệ thống sẽ ưu tiên xử lý `AND` trước `OR`, dẫn đến kết quả sai.
- **Dùng dấu `=` với NULL**: So sánh `WHERE age = NULL` sẽ không trả về lỗi cú pháp nhưng sẽ không bao giờ ra kết quả. Phải dùng `IS NULL`.

## 5. Liên kết (Wikilinks)
- Nền tảng: [[ENTITY_SQL]]
- Mở rộng logic điều kiện: [[CONCEPT_SQL_Case_Statements]]
