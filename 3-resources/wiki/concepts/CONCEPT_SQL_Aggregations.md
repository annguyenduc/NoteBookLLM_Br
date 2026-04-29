---
title: "CONCEPT: SQL Aggregations (Gom nhóm & Thống kê)"
type: concept
domain: SQL
status: verified
sources:
  - "TOOL_SQL_Getting_Started.md"
tags: [sql, group-by, order-by, aggregations, having]
created: 2026-04-29
updated: 2026-04-29
---

# 🧠 Khái niệm: SQL Aggregations (Gom nhóm & Thống kê)

## 1. Định nghĩa
**Aggregations** là quá trình gom nhóm nhiều bản ghi (rows) lại với nhau để thực hiện các phép toán thống kê (như Đếm, Tính tổng, Lấy trung bình). Các mệnh đề lõi đi kèm bao gồm:
- `GROUP BY`: Khai báo cột dùng để gom nhóm.
- `ORDER BY`: Sắp xếp kết quả (ASC - Tăng dần, DESC - Giảm dần).
- `HAVING`: Bộ lọc dành riêng cho kết quả sau khi đã gom nhóm (khác với `WHERE` lọc trước khi gom nhóm).

Các hàm tổng hợp phổ biến: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`.

📖 Nguồn: `TOOL_SQL_Getting_Started.md` — [Page 95-101]

## 2. Ví dụ minh họa (Rule 17: Double Examples)

### Ví dụ 1: Thống kê số lượng và sắp xếp cơ bản
```sql
-- Đếm số lượng nhân viên trong từng phòng ban
-- Sắp xếp phòng ban có nhiều nhân viên nhất lên đầu
SELECT 
    department, 
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC;
```
*(Giải thích: `COUNT(*)` đếm số dòng trong mỗi `department`. Sau đó `ORDER BY ... DESC` sắp xếp giảm dần).*

### Ví dụ 2: Lọc sau khi gom nhóm với HAVING
```sql
-- Tính doanh thu trung bình của từng khu vực
-- CHỈ lấy những khu vực có doanh thu trung bình > 100,000
SELECT 
    region, 
    AVG(revenue) AS avg_revenue
FROM sales
GROUP BY region
HAVING AVG(revenue) > 100000;
```
*(Giải thích: Không thể dùng `WHERE avg_revenue > 100000` vì `WHERE` chạy trước khi SQL tính `AVG`. Phải dùng `HAVING`).*

## 3. Gotchas / Pitfalls (Những lỗi thường gặp)
- **Thiếu cột trong GROUP BY**: Mọi cột nằm trong câu `SELECT` (trừ các cột bị bọc trong hàm Aggregate) đều **BẮT BUỘC** phải có mặt trong mệnh đề `GROUP BY`. Nếu không, truy vấn sẽ báo lỗi.
- **Nhầm lẫn WHERE và HAVING**: `WHERE` lọc dữ liệu thô *trước* khi gom nhóm. `HAVING` lọc dữ liệu tổng hợp *sau* khi gom nhóm. Nếu dùng sai vị trí sẽ báo lỗi hoặc sai logic phân tích.
- **Kỹ thuật `COUNT(column)` vs `COUNT(*)`**: `COUNT(*)` đếm toàn bộ số dòng, bao gồm cả dòng chứa NULL. `COUNT(cột_A)` chỉ đếm những dòng mà `cột_A` có giá trị (bỏ qua NULL).

## 4. Liên kết (Wikilinks)
- Nền tảng: [[ENTITY_SQL]]
- Tư duy phân tích: [[THINK_Analytical_Thinking]] (Các hàm Aggregate dùng để trả lời câu hỏi "Bao nhiêu", "Tỷ lệ nào").
