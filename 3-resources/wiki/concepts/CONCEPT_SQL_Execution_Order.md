---
file_id: CONCEPT_SQL_Execution_Order
title: Thứ tự thực thi câu lệnh [[ENTITY_SQL|SQL]] (Order of Execution)
category: CONCEPT
domain: SQL
status: verified
---

# ️ SQL Query Execution Order

Trong SQL, thứ tự bạn viết các mệnh đề (Lexical Order) không giống với thứ tự mà Database Engine thực thi chúng (Logical Order).

## 1. Thứ tự viết (Lexical Order)
Đây là cách lập trình viên viết code:
`SELECT` -> `FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `ORDER BY`.

## 2. Thứ tự thực thi (Logical Order)
Đây là cách máy tính xử lý dữ liệu:
1.  **FROM**: Xác định nguồn dữ liệu (bảng, join).
2.  **WHERE**: Lọc các hàng thô.
3.  **GROUP BY**: Gom nhóm các hàng.
4.  **HAVING**: Lọc các nhóm đã gom.
5.  **SELECT**: Chọn cột để hiển thị và tính toán các biểu thức/alias.
6.  **ORDER BY**: Sắp xếp kết quả cuối cùng.

## Tại sao điều này quan trọng?
- **Alias:** Bạn thường không thể sử dụng Alias đặt trong `SELECT` ở mệnh đề `WHERE` vì `WHERE` chạy trước khi `SELECT` định nghĩa Alias đó.
- **Hiệu suất:** Hiểu rằng `WHERE` chạy trước `GROUP BY` giúp bạn lọc dữ liệu sớm nhất có thể để giảm tải cho bước gom nhóm.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Lỗi phổ biến do hiểu sai thứ tự thực thi (Lexical vs Logical).*
- **Cách giải quyết:** Cố gắng sử dụng Alias ở mệnh đề `WHERE`. Database Engine báo lỗi "Unknown column 'total_sales'" vì mệnh đề `WHERE` được thực thi ở bước 2, trong khi Alias `total_sales` mãi đến bước 5 ở `SELECT` mới được tạo ra. Khắc phục bằng cách dùng `HAVING` ở bước 4 (sau `GROUP BY`).
```sql
-- ✅ CODE ĐÚNG: Sử dụng HAVING để lọc sau khi gom nhóm
SELECT department, SUM(sales) AS total_sales
FROM company_sales
GROUP BY department
HAVING SUM(sales) > 10000;
```

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Lọc danh sách học sinh xuất sắc qua HAVING thay vì WHERE.*
- **Cách giải quyết:** Giáo viên viết truy vấn để lọc ra các học sinh có tổng điểm 3 môn > 24. Do chưa hiểu Order of Execution, giáo viên để `WHERE SUM(diem_thi) > 24`. Hệ thống báo lỗi vì hàm gộp chưa được tính (phải chờ `GROUP BY`). Giải pháp là chuyển điều kiện xuống `HAVING`.
```sql
-- Lọc danh sách học sinh đạt danh hiệu Xuất Sắc
SELECT 
    ma_hoc_sinh, 
    SUM(diem_thi) AS tong_diem_3_mon
FROM ket_qua_thi
GROUP BY ma_hoc_sinh
HAVING SUM(diem_thi) > 24; -- Chạy sau GROUP BY
```

---
 Nguồn: [[SOURCE_TOOL_SQL_Pocket_Guide]] — Chapter 1 "Order of Execution"
[AUDITOR] Rule 14: Đã xác nhận sơ đồ 6 bước thực thi logic. Ví dụ làm rõ vấn đề Alias không thể dùng trong WHERE.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
