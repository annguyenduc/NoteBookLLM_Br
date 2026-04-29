---
title: "CONCEPT: SQL Select & Filter"
type: concept
domain: SQL
status: verified
sources:
  - [[SOURCE_TOOL_SQL_Getting_Started]]
tags: [sql, select, where, null, filtering]
created: 2026-04-29
updated: 2026-04-29
---

# Khái niệm: SQL Select & Filter (Truy xuất và Lọc dữ liệu)

## 1. Định nghĩa
`SELECT` là câu lệnh cơ bản và quan trọng nhất trong SQL, dùng để trích xuất dữ liệu từ các bảng. Mệnh đề `WHERE` đi kèm dùng để lọc và chỉ giữ lại những bản ghi thỏa mãn điều kiện nhất định.
Việc lọc dữ liệu chính là thao tác đầu tiên trong quy trình Data Preparation của một Data Analyst.

 Nguồn: [[SOURCE_TOOL_SQL_Getting_Started]] (Xác nhận Rule 14 từ: `TOOL_SQL_Getting_Started`) — [Page 36-38, Page 86-90]

## 2. Kỹ thuật Lọc (Filtering) & Xử lý NULL
Trong mệnh đề `WHERE`, ta có thể sử dụng:
- Các toán tử logic: `AND`, `OR`, `IN`.
- Dữ liệu rỗng (`NULL`): Bắt buộc dùng `IS NULL` hoặc `IS NOT NULL`, không được dùng dấu bằng (`= NULL`).

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Truy xuất cơ bản, tính toán cột mới (Expressions) và Lọc dữ liệu.*
- **Cách giải quyết:** Data Analyst lọc báo cáo doanh số, loại bỏ các mặt hàng rẻ tiền (`PRICE > 50`) và linh hoạt sinh ra một cột tính thuế mới ngay trong quá trình Select (`PRICE * 1.07`).
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

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Lọc danh sách học viên rớt môn và xử lý trạng thái Null.*
- **Cách giải quyết:** Hệ thống giáo vụ cần lập danh sách những em thi rớt (Điểm < 5.0) tại hai khu vực 'CS1' hoặc 'CS2'. Tuy nhiên, một số sinh viên đã bảo lưu (Ghi chú = NULL). Cán bộ dùng `IN` để gom khối ngành, và dùng `IS NOT NULL` để đảm bảo bỏ qua các sinh viên bảo lưu.
```sql
-- Lấy danh sách sinh viên rớt ở CS1 và CS2, bỏ qua những em đang bảo lưu
SELECT 
    ma_sinh_vien, 
    ho_ten, 
    diem_thi
FROM ket_qua_thi
WHERE co_so IN ('CS1', 'CS2')
  AND diem_thi < 5.0
  AND ghi_chu_bao_luu IS NULL;
```
 Nguồn: [[SOURCE_TOOL_SQL_Getting_Started]] (Xác nhận Rule 14 từ: `TOOL_SQL_Getting_Started`) — [Page 89-92]

## 4. Gotchas / Pitfalls (Những lỗi thường gặp)
- **Quên ưu tiên ngoặc**: Khi kết hợp `AND` và `OR` trong mệnh đề `WHERE`, luôn dùng ngoặc `()` để bọc nhóm điều kiện. Nếu không, hệ thống sẽ ưu tiên xử lý `AND` trước `OR`, dẫn đến kết quả sai.
- **Dùng dấu `=` với NULL**: So sánh `WHERE age = NULL` sẽ không trả về lỗi cú pháp nhưng sẽ không bao giờ ra kết quả. Phải dùng `IS NULL`.

## 5. Liên kết (Wikilinks)
- Nền tảng: [[ENTITY_SQL]]
- Mở rộng logic điều kiện: [[CONCEPT_SQL_Case_Statements]]
