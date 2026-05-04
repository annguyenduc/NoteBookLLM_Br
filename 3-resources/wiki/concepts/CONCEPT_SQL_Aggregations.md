---
title: "CONCEPT: [[ENTITY_SQL|SQL]] Aggregations (Gom nhóm & Thống kê)"
type: concept
domain: SQL
status: verified
sources:
  - [[SOURCE_TOOL_SQL_Getting_Started]]
tags: [sql, group-by, order-by, aggregations, having]
created: 2026-04-29
updated: 2026-04-29
---

# Khái niệm: SQL Aggregations (Gom nhóm & Thống kê)

## 1. Định nghĩa
**Aggregations** là quá trình gom nhóm nhiều bản ghi (rows) lại với nhau để thực hiện các phép toán thống kê (như Đếm, Tính tổng, Lấy trung bình). Các mệnh đề lõi đi kèm bao gồm:
- `GROUP BY`: Khai báo cột dùng để gom nhóm.
- `ORDER BY`: Sắp xếp kết quả (ASC - Tăng dần, DESC - Giảm dần).
- `HAVING`: Bộ lọc dành riêng cho kết quả sau khi đã gom nhóm (khác với `WHERE` lọc trước khi gom nhóm).

Các hàm tổng hợp phổ biến: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`.

 Nguồn: [[SOURCE_TOOL_SQL_Getting_Started]] (Xác nhận Rule 14 từ: `TOOL_SQL_Getting_Started`) — [Page 95-101]

## 2. Ví dụ đối chiếu (Rule 17: Double Examples)

### 2.1. Ví dụ từ sách (Original)
*Tình huống: Thống kê số lượng và sắp xếp kết quả kinh doanh cơ bản.*
- **Cách giải quyết:** Dùng `GROUP BY` để gom nhóm các nhân viên theo phòng ban. Hàm `COUNT(*)` đếm số dòng trong mỗi `department` tương ứng. Sau đó `ORDER BY ... DESC` hỗ trợ sắp xếp kết quả đếm theo chiều giảm dần để tìm ra phòng ban đông người nhất.
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

### 2.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Thống kê và lọc các lớp có điểm trung bình ngoại ngữ thấp với HAVING.*
- **Cách giải quyết:** Giám hiệu nhà trường yêu cầu rà soát các lớp có chất lượng học ngoại ngữ yếu. Giáo viên dùng `AVG(Diem_Anh)` để tính trung bình từng lớp (`GROUP BY Lop`). Không thể dùng `WHERE avg_score < 5` vì `WHERE` chạy trước khi SQL tính trung bình. Bắt buộc phải dùng `HAVING` để lọc sau khi gom nhóm.
```sql
-- Lọc danh sách các lớp có điểm trung bình tiếng Anh dưới 5.0
SELECT 
    Lop, 
    AVG(Diem_Anh) AS Diem_Trung_Binh
FROM ket_qua_thi
GROUP BY Lop
HAVING AVG(Diem_Anh) < 5.0;
```

## 3. Gotchas / Pitfalls (Những lỗi thường gặp)
- **Thiếu cột trong GROUP BY**: Mọi cột nằm trong câu `SELECT` (trừ các cột bị bọc trong hàm Aggregate) đều **BẮT BUỘC** phải có mặt trong mệnh đề `GROUP BY`. Nếu không, truy vấn sẽ báo lỗi.
- **Nhầm lẫn WHERE và HAVING**: `WHERE` lọc dữ liệu thô *trước* khi gom nhóm. `HAVING` lọc dữ liệu tổng hợp *sau* khi gom nhóm. Nếu dùng sai vị trí sẽ báo lỗi hoặc sai logic phân tích.
- **Kỹ thuật `COUNT(column)` vs `COUNT(*)`**: `COUNT(*)` đếm toàn bộ số dòng, bao gồm cả dòng chứa NULL. `COUNT(cột_A)` chỉ đếm những dòng mà `cột_A` có giá trị (bỏ qua NULL).

---
[AUDITOR] Rule 14: Nguồn được xác nhận từ [[SOURCE_TOOL_SQL_Getting_Started]], các hàm COUNT, SUM, AVG tại p.95-101.

## 4. Liên kết (Wikilinks)
- Nền tảng: [[ENTITY_SQL]]
- Tư duy phân tích: [[SYNTHESIS_THINK_Analytical_Thinking]] (Các hàm Aggregate dùng để trả lời câu hỏi "Bao nhiêu", "Tỷ lệ nào").


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
