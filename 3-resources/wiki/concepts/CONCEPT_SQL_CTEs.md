---
file_id: "CONCEPT_SQL_CTEs"
entity: concept
type: technical
tags: [[ENTITY_SQL|sql]], cte, recursion, performance]
source: SOURCE_TOOL_SQL_COOKBOOK
status: verified
last_updated: 2026-04-29
---

# Common Table Expressions (CTEs)

## 1. Định nghĩa
Common Table Expression (CTE) là một tập kết quả tạm thời được đặt tên, tồn tại duy nhất trong phạm vi thực thi của một câu lệnh SQL (SELECT, INSERT, UPDATE, hoặc DELETE). CTE giúp mã nguồn SQL trở nên sạch sẽ, dễ đọc và hỗ trợ các truy vấn đệ quy phức tạp.

**Nguồn**: SOURCE_TOOL_SQL_COOKBOOK — Phụ lục B (Xác nhận Rule 14 từ: SOURCE_TOOL_SQL_COOKBOOK)

## 2. Cấu trúc cơ bản
```sql
WITH <cte_name> (<column_list>) AS (
    -- Truy vấn định nghĩa CTE
    SELECT ...
)
-- Truy vấn chính sử dụng CTE
SELECT * FROM <cte_name>;
```

### Đặc điểm:
- **Tên CTE**: Được sử dụng như một bảng hoặc view thực thụ trong truy vấn chính.
- **Phạm vi**: Chỉ tồn tại trong câu lệnh ngay sau khi nó được định nghĩa.
- **Tái sử dụng**: Có thể định nghĩa nhiều CTE trong cùng một mệnh đề `WITH`, ngăn cách bởi dấu phẩy.

## 3. CTE vs Subqueries
| Tiêu chí | Subqueries (Truy vấn con) | CTE (Common Table Expressions) |
| :--- | :--- | :--- |
| **Tính dễ đọc** | Dễ bị rối khi lồng nhiều lớp (Nesting). | Cấu trúc phẳng, logic tuần tự từ trên xuống. |
| **Đệ quy** | Không hỗ trợ trực tiếp. | Hỗ trợ đệ quy mạnh mẽ (Recursive CTE). |
| **Tái sử dụng** | Phải viết lại nếu dùng ở nhiều nơi. | Định nghĩa một lần, dùng nhiều lần trong câu lệnh chính. |

<!-- [AUDITOR] Rule 14: Đối soát từ trang 557-559, dòng 24325-24402. -->

## 4. CTE Đệ quy (Recursive CTE)
Đây là tính năng mạnh mẽ nhất của CTE, cho phép một truy vấn tự tham chiếu đến chính nó để xử lý các dữ liệu có cấu trúc cây hoặc chuỗi.

### Cấu trúc Recursive CTE:
1. **Anchor Member**: Truy vấn gốc (điểm bắt đầu).
2. **Recursive Member**: Truy vấn tham chiếu đến CTE (được nối với Anchor bằng `UNION ALL`).
3. **Termination Condition**: Điều kiện dừng (thường nằm ở `WHERE` của Recursive Member).

## 4. Ví dụ đối chiếu (Rule 17: Double Examples)

### 4.1. Ví dụ từ sách (Original)
*Tình huống: Tính dãy Fibonacci (20 số đầu tiên) bằng Recursive CTE.*
- **Cách giải quyết:** Đệ quy sinh ra các số tiếp theo trong dãy Fibonacci dựa trên kết quả của dòng trước đó. Cấu trúc gồm Anchor Member (khởi tạo điểm bắt đầu) và Recursive Member (gọi lại CTE).
```sql
WITH RECURSIVE Fibonacci (fibNum, NextNumber, index1) AS (
    -- Anchor Member
    SELECT 0, 1, 1
    UNION ALL
    -- Recursive Member
    SELECT fibNum + NextNumber, fibNum, index1 + 1
    FROM Fibonacci
    WHERE index1 < 20
)
SELECT fibNum FROM Fibonacci;
```

### 4.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Sử dụng CTE để làm gọn truy vấn lọc các lớp có thành tích thi xuất sắc (Non-Recursive).*
- **Cách giải quyết:** Thay vì viết Subquery lồng ghép khó đọc, giáo viên dùng CTE định nghĩa bảng tạm `Bang_Diem_Lop` trước để tính tổng điểm từng lớp. Sau đó JOIN với bảng danh sách lớp ở truy vấn chính để lọc ra các lớp có tổng điểm trên ngưỡng kỳ vọng. Cách viết này giúp logic phẳng và trong suốt.
```sql
WITH Bang_Diem_Lop AS (
    SELECT 
        ma_lop, 
        SUM(diem_thi) as tong_diem
    FROM ket_qua_thi
    GROUP BY ma_lop
)
SELECT 
    l.ten_lop, 
    b.tong_diem
FROM danh_sach_lop l
JOIN Bang_Diem_Lop b ON l.ma_lop = b.ma_lop
WHERE b.tong_diem > 800;
```

## 5. Ưu điểm và Ứng dụng
- **Phân cấp dữ liệu (Hierarchical Data)**: Rất hiệu quả để duyệt sơ đồ tổ chức (Org Chart), danh mục sản phẩm lồng nhau.
- **Thay thế View tạm thời**: Khi bạn không có quyền tạo View trong Database nhưng cần logic phức tạp.
- **Tối ưu hóa khả năng bảo trì**: Giúp các thành viên khác trong đội ngũ dễ dàng hiểu luồng xử lý logic của các câu lệnh SQL dài hàng trăm dòng.

---
**Xem thêm:**
- [[CONCEPT_SQL_Window_Functions]]
- [[CONCEPT_SQL_Advanced_Reporting]]


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
