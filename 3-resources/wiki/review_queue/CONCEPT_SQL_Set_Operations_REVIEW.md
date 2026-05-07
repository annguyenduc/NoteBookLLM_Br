---
title: Các phép toán tập hợp trong [[ENTITY_SQL|SQL]] (Set Operations)
status: DRAFT
file_id: CONCEPT_SQL_Set_Operations
---

---
file_id: CONCEPT_SQL_Set_Operations
title: Các phép toán tập hợp trong [[ENTITY_SQL|SQL]] (Set Operations)
category: CONCEPT
domain: SQL
status: verified
---

# ⋃ SQL Set Operations

Toán tử tập hợp cho phép bạn kết hợp kết quả của hai hoặc nhiều truy vấn thành một tập kết quả duy nhất.

## 1. Các toán tử chính
- **UNION:** Kết hợp hai tập kết quả và loại bỏ các hàng trùng lặp.
- **UNION ALL:** Kết hợp hai tập kết quả và giữ lại tất cả các hàng (kể cả trùng lặp). Nhanh hơn `UNION` vì không cần bước lọc.
- **INTERSECT:** Chỉ trả về các hàng xuất hiện ở cả hai truy vấn (Phép giao).
- **EXCEPT / MINUS:** Trả về các hàng có ở truy vấn thứ nhất nhưng không có ở truy vấn thứ hai (Phép hiệu).

## Quy tắc
- Các truy vấn phải có cùng số lượng cột.
- Các cột tương ứng phải có kiểu dữ liệu tương thích.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Gộp danh sách bằng UNION vs UNION ALL.*
- **Cách giải quyết:** Cần danh sách email của tất cả khách hàng và nhân viên để gửi bản tin chung. Truy vấn đầu tiên dùng `UNION` sẽ chạy chậm hơn vì database phải so sánh và loại bỏ các email trùng lặp. Truy vấn thứ hai dùng `UNION ALL` cực kỳ nhanh vì nó lấy tất tần tật (kể cả email trùng lặp).
```sql
-- Dùng UNION ALL (Nhanh hơn, giữ lại cả các email xuất hiện ở cả hai bảng)
SELECT email FROM customers
UNION ALL
SELECT email FROM employees;
```

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Dùng EXCEPT / MINUS (Giao/Hiệu) để lọc học sinh nghỉ học.*
- **Cách giải quyết:** Đầu năm học 2023, giáo vụ cần tìm danh sách học sinh có mặt năm 2022 nhưng không nộp học phí hoặc không xuất hiện ở năm 2023 (tức là đã nghỉ hoặc chuyển trường). Toán tử `EXCEPT` (hoặc `MINUS` trong Oracle) cho phép lấy tập hợp của năm trước "trừ đi" tập hợp của năm sau một cách nhanh chóng.
```sql
-- Lấy danh sách ID học sinh năm 2022 trừ đi những em tiếp tục học ở 2023
SELECT ma_hoc_sinh FROM danh_sach_nhap_hoc_2022
EXCEPT 
SELECT ma_hoc_sinh FROM danh_sach_nhap_hoc_2023;
```

---
 Nguồn: [[SOURCE_TOOL_SQL_Getting_Started]]
[AUDITOR] Rule 14: Đã xác nhận định nghĩa 4 toán tử tập hợp. Ví dụ làm rõ sự khác biệt hiệu suất giữa UNION và UNION ALL.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
