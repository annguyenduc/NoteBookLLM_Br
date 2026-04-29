---
title: "CONCEPT: SQL Case Statements (Logic điều kiện)"
type: concept
domain: SQL
status: verified
sources:
  - "TOOL_SQL_Getting_Started.md"
tags: [sql, case-when, pivot, conditional]
created: 2026-04-29
updated: 2026-04-29
---

# 🧠 Khái niệm: SQL Case Statements (Logic điều kiện)

## 1. Định nghĩa
`CASE` statement trong SQL hoạt động tương tự như câu lệnh `IF-THEN-ELSE` trong các ngôn ngữ lập trình. Nó cho phép Data Analyst tạo ra một cột giá trị mới dựa trên các điều kiện kiểm tra (conditions) từ các cột hiện có.

📖 Nguồn: `TOOL_SQL_Getting_Started.md` — [Page 102-106]

## 2. Ứng dụng phổ biến trong Phân tích dữ liệu
1. **Categorization (Phân nhóm)**: Biến đổi các giá trị số liên tục thành các nhóm rập rạp (vd: Tuổi -> Nhóm tuổi).
2. **Data Pivoting (Thủ thuật Zero/Null CASE Trick)**: Chuyển dữ liệu từ dạng dọc (long) sang dạng ngang (wide) bằng cách kết hợp `SUM` với `CASE`.

## 3. Ví dụ minh họa (Rule 17: Double Examples)

### Ví dụ 1: Phân nhóm liên tục (Categorization)
```sql
-- Phân loại mức thu nhập của khách hàng
SELECT 
    customer_id,
    salary,
    CASE 
        WHEN salary < 30000 THEN 'Low'
        WHEN salary BETWEEN 30000 AND 80000 THEN 'Medium'
        ELSE 'High' 
    END AS income_group
FROM customers;
```
*(Giải thích: Từ 1 cột số `salary`, ta sinh ra 1 cột text `income_group` để dễ dàng làm Data Viz bằng Bar chart sau này).*

### Ví dụ 2: The "Zero/Null" CASE Trick (Kỹ thuật Pivot)
```sql
-- Đếm số lượng đơn hàng theo từng trạng thái NHƯNG trải ngang thành các cột
SELECT 
    customer_id,
    SUM(CASE WHEN status = 'Shipped' THEN 1 ELSE 0 END) AS shipped_count,
    SUM(CASE WHEN status = 'Pending' THEN 1 ELSE 0 END) AS pending_count
FROM orders
GROUP BY customer_id;
```
*(Giải thích: Thay vì dùng `COUNT()` và `GROUP BY status` (sẽ ra dạng dọc), ta dùng `CASE` trả về 1 nếu đúng điều kiện, 0 nếu sai, sau đó bọc trong hàm `SUM()`. Đây là thủ thuật kinh điển để Pivot bảng trong SQL mà không cần dùng hàm `PIVOT` phức tạp).*
📖 Nguồn: `TOOL_SQL_Getting_Started.md` — [Page 105-106]

## 4. Gotchas / Pitfalls (Những lỗi thường gặp)
- **Quên mệnh đề `END`**: Mỗi câu `CASE` bắt buộc phải kết thúc bằng `END`. Cú pháp đầy đủ là `CASE WHEN ... THEN ... ELSE ... END`.
- **Thứ tự thực thi**: `CASE` xử lý các điều kiện tuần tự từ trên xuống dưới. Nếu một record thỏa mãn `WHEN` đầu tiên, hệ thống sẽ bỏ qua các `WHEN` bên dưới. Do đó, cần đặt điều kiện hẹp nhất/nghiêm ngặt nhất lên trên cùng.

## 5. Liên kết (Wikilinks)
- Nền tảng: [[ENTITY_SQL]]
- Kết hợp với Aggregation: [[CONCEPT_SQL_Aggregations]]
