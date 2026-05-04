---
file_id: CONCEPT_SQL_Sublanguages
title: Các ngôn ngữ con trong [[ENTITY_SQL|SQL]] (SQL Sublanguages)
category: CONCEPT
domain: SQL
status: verified
---

# ️ SQL Sublanguages

SQL không chỉ là một ngôn ngữ đơn nhất mà bao gồm 4 nhóm ngôn ngữ con thực hiện các nhiệm vụ khác nhau trong quản trị và phân tích dữ liệu.

## 1. DQL (Data Query Language)
- **Nhiệm vụ:** Truy vấn và trích xuất dữ liệu.
- **Lệnh chính:** `SELECT`.
- **Trọng tâm:** Là phần quan trọng nhất đối với Data Analyst để trả lời các câu hỏi từ dữ liệu.

## 2. DDL (Data Definition Language)
- **Nhiệm vụ:** Định nghĩa và thay đổi cấu trúc database (schema, tables, views).
- **Lệnh chính:** `CREATE`, `ALTER`, `DROP`.
- **Lưu ý:** Ảnh hưởng đến cấu trúc nhưng không ảnh hưởng đến nội dung dữ liệu bên trong.

## 3. DML (Data Manipulation Language)
- **Nhiệm vụ:** Tương tác trực tiếp với bản ghi dữ liệu.
- **Lệnh chính:** `INSERT`, `UPDATE`, `DELETE`.
- **Ứng dụng:** Thường dùng trong bước "Load" của quy trình ETL hoặc khi làm việc với các bảng tạm (temp tables).

## 4. DCL (Data Control Language)
- **Nhiệm vụ:** Quản lý quyền truy cập.
- **Lệnh chính:** `GRANT`, `REVOKE`.
- **Ứng dụng:** Cấp quyền cho đồng nghiệp xem hoặc sửa bảng.

## 5. Ví dụ đối chiếu (Rule 17: Double Examples)

### 5.1. Ví dụ từ sách (Original)
*Tình huống: DDL và DML trong thao tác chuẩn bị dữ liệu.*
- **Cách giải quyết:** Một Data Analyst bắt đầu dự án bằng cách tạo ra bảng tạm thời (`CREATE TABLE` thuộc nhóm DDL). Sau đó, họ chèn kết quả tính toán hoặc dòng dữ liệu cứng vào (`INSERT` thuộc nhóm DML) để làm nền tảng tính toán tiếp.
```sql
-- DDL (Data Definition): Tạo cấu trúc bảng
CREATE TABLE top_customers (
    id INT, 
    total_spent DECIMAL
);

-- DML (Data Manipulation): Chèn dữ liệu vào bảng vừa tạo
INSERT INTO top_customers (id, total_spent)
VALUES (101, 5000.00);
```

### 5.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: DQL và DCL trong quy trình phân quyền quản lý điểm thi.*
- **Cách giải quyết:** Database Administrator của trường học (DBA) cần cấp quyền để giáo viên mới được phép xem bảng điểm khối 10. DBA dùng `GRANT` (thuộc DCL) để cấp quyền. Sau đó, giáo viên có thể dùng `SELECT` (thuộc DQL) để truy vấn thông tin học sinh mà không sợ ghi đè hay làm hỏng dữ liệu hệ thống.
```sql
-- DCL (Data Control): Cấp quyền đọc (chỉ xem, không được sửa/xóa)
GRANT SELECT ON bang_diem_khoi_10 TO tk_giao_vien_moi;

-- DQL (Data Query): Giáo viên thực thi truy vấn tìm học sinh điểm cao
SELECT * FROM bang_diem_khoi_10 WHERE diem_trung_binh > 8.0;
```

---
 Nguồn: [[SOURCE_TOOL_SQL_for_Data_Analysis]] — Section "What Is SQL?"
[AUDITOR] Rule 14: Xác nhận thông tin chính xác theo phân loại của Cathy Tanimura.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
