---
title: "Khái niệm: SQL Joins (Kết nối bảng)"
status: DRAFT
file_id: CONCEPT_SQL_Joins
---

---
file_id: CONCEPT_SQL_Joins
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
title: "Khái niệm: SQL Joins (Kết nối bảng)"
source: "[[SOURCE_TOOL_SQL_Getting_Started]]"
created: "2026-05-03"
---

﻿---
title: "CONCEPT: [[ENTITY_SQL|SQL]] Joins (Kết nối bảng)"
type: concept
domain: SQL
status: verified
sources:
  - [[SOURCE_TOOL_SQL_Getting_Started]]
tags: [sql, join, inner-join, left-join, relational-database]
created: 2026-04-29
updated: 2026-04-29
---

# Khái niệm: SQL Joins (Kết nối bảng)

## 1. Định nghĩa & Lý do sử dụng
Trong cơ sở dữ liệu quan hệ (RDBMS), dữ liệu thường được tách ra thành nhiều bảng riêng biệt để tránh dư thừa (quá trình này gọi là **Normalization**). 
Để lấy được thông tin hoàn chỉnh, Data Analyst phải sử dụng `JOIN` để "khâu" (stitch) các bảng này lại với nhau dựa trên một cột chung (thường là **Primary Key** của bảng này khớp với **Foreign Key** của bảng kia).

 Nguồn: [[SOURCE_TOOL_SQL_Getting_Started]] (Xác nhận Rule 14 từ: `TOOL_SQL_Getting_Started`) — [Page 107-114]

## 2. Các loại JOIN cốt lõi
1. **INNER JOIN**: Chỉ lấy những bản ghi có giá trị khớp nhau ở CẢ HAI bảng. (Phần giao nhau).
2. **LEFT JOIN**: Lấy TOÀN BỘ bản ghi của bảng bên trái. Nếu bảng bên phải không có dữ liệu khớp, hệ thống sẽ điền `NULL`. Đây là loại Join an toàn nhất khi không muốn mất dữ liệu gốc.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: INNER JOIN (Tìm dữ liệu khớp hoàn toàn).*
- **Cách giải quyết:** Khi phòng kinh doanh cần phân tích hành vi mua hàng, họ chỉ quan tâm đến những người *đã từng mua*. Bằng cách dùng `INNER JOIN` nối bảng `orders` và bảng `customers`, hệ thống sẽ tự động lọc ra danh sách các đơn hàng có `customer_id` hợp lệ và lấy kèm tên khách hàng.
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

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: LEFT JOIN (Giữ lại dữ liệu bảng gốc) để kiểm tra tình trạng nộp bài.*
- **Cách giải quyết:** Giáo viên cần xuất danh sách toàn bộ học sinh trong lớp, xem ai đã nộp bài tập và nộp khi nào. Nếu dùng `INNER JOIN`, các em chưa nộp sẽ bị "biến mất" khỏi danh sách. Giáo viên bắt buộc phải dùng `LEFT JOIN` lấy gốc từ `danh_sach_lop`. Em nào chưa nộp bài sẽ hiện `NULL` ở cột ngày nộp.
```sql
-- Lấy toàn bộ học sinh, kèm ngày nộp bài (nếu có)
SELECT 
    hs.ten_hoc_sinh, 
    hs.ma_hoc_sinh,
    bt.ngay_nop_bai
FROM danh_sach_lop hs
LEFT JOIN bai_tap_nop bt 
    ON hs.ma_hoc_sinh = bt.ma_hoc_sinh;
```
 Nguồn: [[SOURCE_TOOL_SQL_Getting_Started]] (Xác nhận Rule 14 từ: `TOOL_SQL_Getting_Started`) — [Page 110-111]

## 4. Gotchas / Pitfalls (Những lỗi thường gặp)
- **Missing JOIN condition (Lỗi Cartesian Product / Cross Join)**: Nếu bạn dùng `JOIN` nhưng quên mệnh đề `ON` hoặc nối nhiều bảng mà thiếu mệnh đề `WHERE` nối, cơ sở dữ liệu sẽ nhân chéo các dòng lại với nhau (vd bảng 100 dòng x bảng 100 dòng = 10,000 dòng). Điều này gây treo máy hoặc trả về dữ liệu rác.
- **Null trong LEFT JOIN**: Cẩn thận khi thực hiện hàm `COUNT(cột_bảng_phải)` sau khi dùng LEFT JOIN. Bản ghi không khớp sẽ có giá trị NULL, và `COUNT()` sẽ bỏ qua nó. Tránh dùng `COUNT(*)` nếu mục tiêu là đếm số dữ liệu thực sự có của bảng phải.
- **Ambiguous Column Name**: Nếu cả 2 bảng đều có chung một tên cột (ví dụ cột `id`), bạn BẮT BUỘC phải chỉ định rõ cột đó thuộc bảng nào trong câu SELECT (ví dụ: `SELECT customers.id`).

## 5. Liên kết (Wikilinks)
- Nền tảng: [[ENTITY_SQL]]
- Ứng dụng sau Join: Lọc với [[CONCEPT_SQL_Select_And_Filter]] hoặc gom nhóm với [[CONCEPT_SQL_Aggregations]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
