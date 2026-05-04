---
file_id: CONCEPT_SQL_Hierarchical_Queries
title: Truy vấn phân cấp và đệ quy (Hierarchical & Recursive Queries)
category: CONCEPT
domain: [[ENTITY_SQL|SQL]]
status: verified
---

# SQL Hierarchical Queries

Làm việc với dữ liệu có cấu trúc cây (ví dụ: sơ đồ tổ chức công ty, danh mục sản phẩm lồng nhau) yêu cầu các kỹ thuật truy vấn đặc biệt.

## 1. Recursive Common Table Expressions (CTE)
Đây là cách tiếp cận chuẩn (Postgres, SQL Server, MySQL 8.0+) để duyệt cây.
- **Cấu trúc:**
    1. **Anchor member:** Điểm bắt đầu (ví dụ: tìm sếp tổng).
    2. **Recursive member:** Liên kết hàng hiện tại với hàng cha/con của nó.
    3. **Terminating condition:** Điều kiện dừng (khi không còn node con).

## 2. Các nhiệm vụ phổ biến
- **Tìm toàn bộ con (Descendants):** Tìm tất cả nhân viên cấp dưới của một quản lý.
- **Tìm đường dẫn (Path Enumeration):** Hiển thị đường dẫn từ gốc đến node hiện tại (ví dụ: `CEO -> Manager -> Employee`).
- **Phân loại Node:** Xác định node là Gốc (Root), Nhánh (Branch) hay Lá (Leaf - không có con).

## 3. Cách tiếp cận đặc thù (Oracle)
Oracle cung cấp cú pháp `START WITH ... CONNECT BY PRIOR` cực kỳ mạnh mẽ và ngắn gọn cho các truy vấn phân cấp trước khi CTE đệ quy trở thành chuẩn.

## 4. Ví dụ đối chiếu (Rule 17: Double Examples)

### 4.1. Ví dụ từ sách (Original)
*Tình huống: Duyệt cây nhân sự công ty bằng Recursive CTE (Chuẩn ANSI).*
- **Cách giải quyết:** Cần tìm tất cả nhân viên cấp dưới (trực tiếp và gián tiếp) của Quản lý có ID = 1. Ta dùng CTE đệ quy: phần Anchor lấy Quản lý gốc, phần Recursive thực hiện `JOIN` ngược lại CTE để bóc tách từng lớp nhân sự.
```sql
WITH RECURSIVE OrgChart AS (
    -- Anchor: Quản lý gốc
    SELECT emp_id, emp_name, manager_id FROM employees WHERE manager_id = 1
    UNION ALL
    -- Recursive: Nối nhân viên với bảng CTE
    SELECT e.emp_id, e.emp_name, e.manager_id 
    FROM employees e
    JOIN OrgChart o ON e.manager_id = o.emp_id
)
SELECT * FROM OrgChart;
```

### 4.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Truy xuất chuỗi Môn học Tiên quyết (Prerequisite Graph) cho sinh viên.*
- **Cách giải quyết:** Để đăng ký môn "AI Nâng cao" (ID: 500), sinh viên phải hoàn thành hàng loạt môn học nền tảng trước đó. Hệ thống học tập sử dụng CTE đệ quy để quét ngược từ môn ID 500, truy ra tất cả các môn cha (Toán rời rạc, Lập trình C), tạo thành cây phả hệ học phần.
```sql
WITH RECURSIVE PrerequisiteChain AS (
    -- Anchor: Môn học đích (AI Nâng cao)
    SELECT course_id, course_name, req_id FROM courses WHERE course_id = 500
    UNION ALL
    -- Recursive: Lần ngược về các môn tiên quyết (những môn cha)
    SELECT c.course_id, c.course_name, c.req_id 
    FROM courses c
    JOIN PrerequisiteChain p ON c.course_id = p.req_id
)
SELECT * FROM PrerequisiteChain;
```

---
 Nguồn: [[SOURCE_TOOL_SQL_Cookbook]] — Chapter 13 "Hierarchical Queries"
[AUDITOR] Rule 14: Đã xác nhận sự khác biệt giữa CTE đệ quy và CONNECT BY.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
