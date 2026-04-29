---
title: "CONCEPT: SQL Case Statements (Logic điều kiện)"
type: concept
domain: SQL
status: verified
sources:
  - [[SOURCE_TOOL_SQL_Getting_Started]]
tags: [sql, case-when, pivot, conditional]
created: 2026-04-29
updated: 2026-04-29
---

# Khái niệm: SQL Case Statements (Logic điều kiện)

## 1. Định nghĩa
`CASE` statement trong SQL hoạt động tương tự như câu lệnh `IF-THEN-ELSE` trong các ngôn ngữ lập trình. Nó cho phép Data Analyst tạo ra một cột giá trị mới dựa trên các điều kiện kiểm tra (conditions) từ các cột hiện có.

 Nguồn: [[SOURCE_TOOL_SQL_Getting_Started]] (Xác nhận Rule 14 từ: `TOOL_SQL_Getting_Started`) — [Page 102-106]

## 2. Ứng dụng phổ biến trong Phân tích dữ liệu
1. **Categorization (Phân nhóm)**: Biến đổi các giá trị số liên tục thành các nhóm rập rạp (vd: Tuổi -> Nhóm tuổi).
2. **Data Pivoting (Thủ thuật Zero/Null CASE Trick)**: Chuyển dữ liệu từ dạng dọc (long) sang dạng ngang (wide) bằng cách kết hợp `SUM` với `CASE`.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Phân nhóm dữ liệu liên tục (Categorization) thành các nhóm kinh doanh.*
- **Cách giải quyết:** Khách hàng có độ phân tán mức lương rất lớn (biến số liên tục). Việc sử dụng `CASE WHEN` cho phép biến đổi các mốc số liệu này thành 3 nhóm rập rạp rõ ràng (Low, Medium, High). Việc biến đổi cột số sinh ra 1 cột text mới giúp Data Analyst dễ dàng thực hiện vẽ biểu đồ Bar chart sau đó.
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

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Ứng dụng kỹ thuật "Zero/Null CASE Trick" (Kỹ thuật Pivot) để lập bảng điểm danh.*
- **Cách giải quyết:** Nhà trường lưu dữ liệu điểm danh theo định dạng dọc (Long format) gồm cột `Hoc_Sinh` và cột `Trang_Thai` (Đi học, Vắng, Trễ). Giáo viên chủ nhiệm cần một báo cáo trải ngang ra (Wide format) để đếm tổng số buổi vắng/trễ của từng em. Thay vì dùng `PIVOT` phức tạp, giáo viên dùng `CASE` kết hợp `SUM` để chuyển đổi dọc thành ngang.
```sql
-- Chuyển trạng thái điểm danh dọc thành các cột thống kê ngang
SELECT 
    Hoc_Sinh,
    SUM(CASE WHEN Trang_Thai = 'Đi học' THEN 1 ELSE 0 END) AS So_Buoi_Hoc,
    SUM(CASE WHEN Trang_Thai = 'Vắng' THEN 1 ELSE 0 END) AS So_Buoi_Vang,
    SUM(CASE WHEN Trang_Thai = 'Trễ' THEN 1 ELSE 0 END) AS So_Buoi_Tre
FROM Bang_Diem_Danh
GROUP BY Hoc_Sinh;
```
 Nguồn: [[SOURCE_TOOL_SQL_Getting_Started]] (Xác nhận Rule 14 từ: `TOOL_SQL_Getting_Started`) — [Page 105-106]

## 4. Gotchas / Pitfalls (Những lỗi thường gặp)
- **Quên mệnh đề `END`**: Mỗi câu `CASE` bắt buộc phải kết thúc bằng `END`. Cú pháp đầy đủ là `CASE WHEN ... THEN ... ELSE ... END`.
- **Thứ tự thực thi**: `CASE` xử lý các điều kiện tuần tự từ trên xuống dưới. Nếu một record thỏa mãn `WHEN` đầu tiên, hệ thống sẽ bỏ qua các `WHEN` bên dưới. Do đó, cần đặt điều kiện hẹp nhất/nghiêm ngặt nhất lên trên cùng.

## 5. Liên kết (Wikilinks)
- Nền tảng: [[ENTITY_SQL]]
- Kết hợp với Aggregation: [[CONCEPT_SQL_Aggregations]]
