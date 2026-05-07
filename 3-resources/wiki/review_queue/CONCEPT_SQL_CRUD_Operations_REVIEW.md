---
title: Các thao tác CRUD trong [[ENTITY_SQL|SQL]]
status: DRAFT
file_id: CONCEPT_SQL_CRUD_Operations
---

---
file_id: CONCEPT_SQL_CRUD_Operations
title: Các thao tác CRUD trong [[ENTITY_SQL|SQL]]
category: CONCEPT
domain: SQL
status: verified
---

# SQL CRUD Operations

CRUD là viết tắt của 4 thao tác cơ bản nhất mà bạn có thể thực hiện trên bất kỳ hệ thống lưu trữ dữ liệu nào.

| Viết tắt | Ý nghĩa | Lệnh SQL tương ứng | Đối tượng sử dụng chính |
| :--- | :--- | :--- | :--- |
| **C**reate | Tạo mới dữ liệu | `INSERT` | Developers, DBAs |
| **R**ead | Đọc/Truy vấn dữ liệu | `SELECT` | Data Analysts, Scientists |
| **U**pdate | Cập nhật dữ liệu | `UPDATE` | Developers, App Systems |
| **D**elete | Xóa dữ liệu | `DELETE` | DBAs, Maintenance Scripts |

## 1. SQL Statements vs SQL Queries
- **SQL Statements:** Là thuật ngữ chung cho mọi câu lệnh thực hiện bất kỳ thao tác CRUD nào (bao gồm cả tạo bảng `CREATE TABLE`).
- **SQL Queries:** Là thuật ngữ chuyên biệt cho thao tác **Read (SELECT)**. Data Analyst chủ yếu viết Queries.

## 2. Transaction Management
Khi thực hiện các thao tác thay đổi dữ liệu (C, U, D), cần lưu ý đến:
- **COMMIT:** Lưu vĩnh viễn các thay đổi.
- **ROLLBACK:** Hoàn tác các thay đổi nếu có lỗi xảy ra.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Tạo và Đọc dữ liệu khách hàng (CREATE và READ).*
- **Cách giải quyết:** Các Developer thêm mới dữ liệu bằng `INSERT`, sau đó Data Analyst kiểm tra lại bằng `SELECT`.
```sql
-- C (Create): Thêm mới dữ liệu
INSERT INTO customers (id, name, status) 
VALUES (101, 'Nguyen Van A', 'Active');

-- R (Read): Đọc dữ liệu ra
SELECT id, name, status 
FROM customers 
WHERE id = 101;
```

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Quản lý trạng thái học sinh trong hệ thống E-Learning (UPDATE và DELETE).*
- **Cách giải quyết:** Khi kết thúc năm học, admin hệ thống LMS (Learning Management System) cần cập nhật học sinh đã tốt nghiệp thành 'Alumni', và xóa các tài khoản thử nghiệm.
```sql
-- U (Update): Cập nhật trạng thái tốt nghiệp
UPDATE hoc_sinh 
SET trang_thai = 'Alumni' 
WHERE khoi_hoc = 12;

-- D (Delete): Xóa tài khoản test
DELETE FROM hoc_sinh 
WHERE loai_tai_khoan = 'Test_Account';
```

---
 Nguồn: [[SOURCE_TOOL_SQL_Pocket_Guide]] — Chapter 1 "A SQL Query"
[AUDITOR] Rule 14: Đã xác nhận định nghĩa CRUD và phân biệt Statement/Query. Ví dụ bao phủ đầy đủ 4 thao tác cốt lõi.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
