# 📊 Research Analysis: SQL Pocket Guide (Alice Zhao)

## 📋 Thông tin chung
- **Tác giả:** Alice Zhao (O'Reilly, 4th Edition 2021).
- **Trọng tâm:** Hướng dẫn tra cứu nhanh cú pháp và sự khác biệt giữa các hệ quản trị (Postgres, MySQL, Oracle, SQL Server, SQLite).
- **Phạm vi Ingest:** Toàn bộ mục lục và các khái niệm nền tảng (Execution Order, CRUD).

## 🧩 Các thực thể & Khái niệm then chốt (Atoms Candidate)

### 1. Thứ tự thực thi truy vấn (Order of Execution)
- **Concept:** Thứ tự viết code (Select -> From) khác với thứ tự máy tính thực thi (From -> Where -> Group By -> Having -> Select -> Order By).
- **Lưu ý:** Hiểu điều này giúp giải thích tại sao không thể dùng Alias trong `WHERE` ở một số DBMS.

### 2. So sánh RDBMS (RDBMS Nuances)
- **Entity:** So sánh đặc điểm của 5 hệ quản trị phổ biến.
- **Cú pháp khác biệt:** Cách giới hạn số hàng (`LIMIT` vs `TOP` vs `ROWNUM`).

### 3. Nguyên tắc CRUD
- **Concept:** Phân biệt SQL Statements (DBA dùng để quản trị) và SQL Queries (Data Analyst dùng để đọc dữ liệu).

### 4. Kiểu dữ liệu chuẩn (Data Types)
- Phân nhóm kiểu dữ liệu: Numeric (Integer, Decimal, Floating), String (Char, Unicode), Datetime.

## 📈 Đóng góp cho Master Synthesis (SQL Mastery)
- Bổ sung chương **Query Execution Order** (Giải thích cơ chế hoạt động của Engine).
- Bổ sung bảng **RDBMS Nuance Comparison**.
- Chuẩn hóa phần **CRUD Operations**.

## 🛠️ Mining Stats
- **Total Lines Scanned:** ~800 lines.
- **Key Concepts Identified:** 4.
- **Entities Identified:** 1 (Book Source).
