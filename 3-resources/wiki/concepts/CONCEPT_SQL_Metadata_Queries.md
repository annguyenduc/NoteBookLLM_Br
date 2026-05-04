---
file_id: CONCEPT_SQL_Metadata_Queries
title: Truy vấn siêu dữ liệu (Metadata Queries)
category: CONCEPT
domain: [[ENTITY_SQL|SQL]]
status: verified
---

# SQL Metadata Queries

Metadata là dữ liệu về dữ liệu. Truy vấn metadata giúp lập trình viên hiểu cấu trúc hệ thống mà không cần dùng công cụ GUI.

## 1. Information Schema (Chuẩn ANSI)
Hầu hết các RDBMS hiện đại (Postgres, SQL Server, MySQL) đều hỗ trợ `information_schema`. Nó cung cấp các view chứa siêu dữ liệu về bảng, cột, khóa.

## 2. Oracle Data Dictionary (Đặc thù)
Oracle sử dụng các view riêng biệt:
- `USER_TABLES`, `ALL_TABLES`, `DBA_TABLES`.
- `USER_TAB_COLUMNS`.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Dùng SQL để sinh ra SQL (SQL to Generate SQL) nhằm tự động hóa.*
- **Cách giải quyết:** Bạn muốn xóa nhanh hàng loạt bảng nháp có tiền tố `test_` mà không phải gõ tay từng lệnh DROP. Bằng cách truy vấn `information_schema.tables`, SQL Engine sẽ trả về một cột chứa sẵn hàng loạt câu lệnh `DROP TABLE ...;` để bạn copy/paste và thực thi ngay lập tức.
```sql
-- Tạo hàng loạt lệnh DROP TABLE
SELECT 'DROP TABLE ' || table_name || ';' 
FROM information_schema.tables 
WHERE table_name LIKE 'test_%';
```

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Khai thác Information Schema để rà soát cấu trúc CSDL của nhà trường.*
- **Cách giải quyết:** Một Data Engineer giáo dục vừa tiếp nhận hệ thống quản lý trường học cũ kỹ. Họ không có tài liệu mô tả (ERD). Để tìm xem có bao nhiêu bảng liên quan đến điểm số, họ truy vấn `information_schema.columns` để tìm mọi bảng có chứa cột mang từ khóa 'diem'.
```sql
-- Tìm tất cả các bảng và cột liên quan đến điểm số trong hệ thống
SELECT 
    table_name, 
    column_name, 
    data_type 
FROM information_schema.columns 
WHERE column_name LIKE '%diem%';
```

---
 Nguồn: [[SOURCE_TOOL_SQL_Cookbook]] — Chapter 5 "Metadata Queries"
[AUDITOR] Rule 14: Đã xác nhận các ví dụ về information_schema và Oracle dictionary.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
