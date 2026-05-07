---
title: So sánh cú pháp giữa các hệ quản trị RDBMS
status: DRAFT
file_id: CONCEPT_SQL_RDBMS_Comparison
---

---
file_id: CONCEPT_SQL_RDBMS_Comparison
title: So sánh cú pháp giữa các hệ quản trị RDBMS
category: CONCEPT
domain: [[ENTITY_SQL|SQL]]
status: verified
---

# ️ RDBMS Syntax Comparison

Mặc dù SQL có chuẩn chung (ANSI SQL), mỗi hệ quản trị cơ sở dữ liệu (RDBMS) vẫn có những biến thể cú pháp riêng (Dialects).

| Tính năng | PostgreSQL | MySQL | SQL Server | Oracle | SQLite |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Giới hạn hàng** | `LIMIT n` | `LIMIT n` | `TOP n` | `ROWNUM <= n` | `LIMIT n` |
| **Nối chuỗi** | `\|\|` | `CONCAT()` | `+` | `\|\|` | `\|\|` |
| **Lấy ngày hiện tại** | `NOW()` | `NOW()` | `GETDATE()` | `SYSDATE` | `DATE('now')` |
| **Boolean** | `TRUE/FALSE` | `1/0` | `1/0` | (Không có) | `1/0` |

## Lưu ý cho Analyst
- Khi viết các truy vấn phức tạp như Window Functions hoặc Regex, hãy luôn tra cứu tài liệu đặc thù của hệ thống bạn đang dùng.
- PostgreSQL thường là hệ thống tuân thủ chuẩn ANSI SQL nghiêm ngặt nhất.

## 2. Ví dụ đối chiếu (Rule 17: Double Examples)

### 2.1. Ví dụ từ sách (Original)
*Tình huống: Khác biệt khi giới hạn kết quả (LIMIT vs TOP) để lọc Top 5 nhân viên.*
- **Cách giải quyết:** Mỗi RDBMS có từ khóa riêng biệt để ngắt kết quả truy vấn. Lập trình viên Data phải viết `LIMIT 5` nếu dùng Postgres, nhưng phải đổi thành `TOP 5` nếu hệ thống chuyển sang SQL Server.
```sql
-- Trong PostgreSQL / MySQL / SQLite
SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

-- Trong SQL Server
SELECT TOP 5 * FROM employees ORDER BY salary DESC;
```

### 2.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Khác biệt khi nối chuỗi (String Concatenation) để tạo danh sách lớp.*
- **Cách giải quyết:** Hệ thống giáo dục trường học cần in bảng tên học sinh, ghép `ho_lot` và `ten`. Tuỳ thuộc vào hệ quản trị cơ sở dữ liệu nhà trường đang dùng, giáo viên CNTT phải linh hoạt dùng toán tử `||` (Postgres) hoặc dấu `+` (SQL Server) để nối chuỗi chính xác.
```sql
-- Trong PostgreSQL / SQLite / Oracle (Chuẩn ANSI)
SELECT ma_hoc_sinh, ho_lot || ' ' || ten AS ho_va_ten FROM hoc_sinh;

-- Trong SQL Server
SELECT ma_hoc_sinh, ho_lot + ' ' + ten AS ho_va_ten FROM hoc_sinh;
```

---
 Nguồn: [[SOURCE_TOOL_SQL_Pocket_Guide]] — Chapter 2 "RDBMS Nuances"
[AUDITOR] Rule 14: Đã xác nhận bảng so sánh cú pháp 5 hệ thống.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
