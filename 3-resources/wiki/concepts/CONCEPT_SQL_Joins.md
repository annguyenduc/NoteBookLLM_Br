---
title: "CONCEPT: SQL Joins (Kết nối bảng)"
type: concept
domain: SQL
status: verified
sources:
  - "TOOL_SQL_Getting_Started.md"
tags: [sql, join, inner-join, left-join, relational-database]
created: 2026-04-29
updated: 2026-04-29
---

# 🧠 Khái niệm: SQL Joins (Kết nối bảng)

## 1. Định nghĩa & Lý do sử dụng
Trong cơ sở dữ liệu quan hệ (RDBMS), dữ liệu thường được tách ra thành nhiều bảng riêng biệt để tránh dư thừa (quá trình này gọi là **Normalization**). 
Để lấy được thông tin hoàn chỉnh, Data Analyst phải sử dụng `JOIN` để "khâu" (stitch) các bảng này lại với nhau dựa trên một cột chung (thường là **Primary Key** của bảng này khớp với **Foreign Key** của bảng kia).

📖 Nguồn: `TOOL_SQL_Getting_Started.md` — [Page 107-114]

## 2. Các loại JOIN cốt lõi
1. **INNER JOIN**: Chỉ lấy những bản ghi có giá trị khớp nhau ở CẢ HAI bảng. (Phần giao nhau).
2. **LEFT JOIN**: Lấy TOÀN BỘ bản ghi của bảng bên trái. Nếu bảng bên phải không có dữ liệu khớp, hệ thống sẽ điền `NULL`. Đây là loại Join an toàn nhất khi không muốn mất dữ liệu gốc.

## 3. Ví dụ minh họa (Rule 17: Double Examples)

### Ví dụ 1: INNER JOIN (Tìm dữ liệu khớp hoàn toàn)
```sql
-- Lấy thông tin chi tiết các đơn hàng CÓ khách hàng tồn tại trong hệ thống
SELECT 
    orders.order_id, 
    customers.name, 
    orders.order_date
FROM orders
INNER JOIN customers 
    ON orders.customer_id = customers.customer_id;
```
*(Giải thích: Chỉ những `order` nào có `customer_id` hợp lệ nằm trong bảng `customers` mới được hiển thị).*

### Ví dụ 2: LEFT JOIN (Giữ lại dữ liệu bảng gốc)
```sql
-- Lấy toàn bộ danh sách khách hàng, kèm theo đơn hàng của họ (nếu có)
-- Những khách hàng chưa từng mua hàng sẽ hiện NULL ở phần order_id
SELECT 
    c.name, 
    o.order_id, 
    o.amount
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id;
```
*(Giải thích: Sử dụng alias `c` và `o` cho tên bảng để viết code ngắn gọn. Khách hàng không có `order` vẫn xuất hiện trên kết quả).*
📖 Nguồn: `TOOL_SQL_Getting_Started.md` — [Page 110-111]

## 4. Gotchas / Pitfalls (Những lỗi thường gặp)
- **Missing JOIN condition (Lỗi Cartesian Product / Cross Join)**: Nếu bạn dùng `JOIN` nhưng quên mệnh đề `ON` hoặc nối nhiều bảng mà thiếu mệnh đề `WHERE` nối, cơ sở dữ liệu sẽ nhân chéo các dòng lại với nhau (vd bảng 100 dòng x bảng 100 dòng = 10,000 dòng). Điều này gây treo máy hoặc trả về dữ liệu rác.
- **Null trong LEFT JOIN**: Cẩn thận khi thực hiện hàm `COUNT(cột_bảng_phải)` sau khi dùng LEFT JOIN. Bản ghi không khớp sẽ có giá trị NULL, và `COUNT()` sẽ bỏ qua nó. Tránh dùng `COUNT(*)` nếu mục tiêu là đếm số dữ liệu thực sự có của bảng phải.
- **Ambiguous Column Name**: Nếu cả 2 bảng đều có chung một tên cột (ví dụ cột `id`), bạn BẮT BUỘC phải chỉ định rõ cột đó thuộc bảng nào trong câu SELECT (ví dụ: `SELECT customers.id`).

## 5. Liên kết (Wikilinks)
- Nền tảng: [[ENTITY_SQL]]
- Ứng dụng sau Join: Lọc với [[CONCEPT_SQL_Select_And_Filter]] hoặc gom nhóm với [[CONCEPT_SQL_Aggregations]].
