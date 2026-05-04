# 📊 Research Analysis: SQL Cookbook (Anthony Molinaro & Robert de Graaf)

## 📋 Thông tin chung
- **Tác giả:** Anthony Molinaro & Robert de Graaf (O'Reilly, 2nd Edition 2020).
- **Trọng tâm:** Các giải pháp thực tế (recipes) cho 5 hệ quản trị phổ biến (DB2, Oracle, Postgres, SQL Server, MySQL).
- **Phạm vi Ingest:** Toàn bộ mục lục và các kỹ thuật nâng cao (Metadata, Strings, Hierarchical).

## 🧩 Các thực thể & Khái niệm then chốt (Atoms Candidate)

### 1. Truy vấn Metadata (Metadata Queries)
- **Kỹ thuật:** Sử dụng `information_schema` hoặc các view đặc thù (Oracle Data Dictionary) để liệt kê bảng, cột, ràng buộc (constraints).
- **SQL to generate SQL:** Dùng kết quả truy vấn để tạo ra các lệnh SQL động.

### 2. Xử lý chuỗi (String Manipulation)
- **Walking a String:** Kỹ thuật duyệt từng ký tự trong chuỗi bằng cách join với một bảng số (pivot table).
- **Delimited Lists:** Chuyển đổi giữa định dạng hàng và danh sách phân tách bằng dấu phẩy (CSV-like strings in SQL).

### 3. Truy vấn phân cấp (Hierarchical Queries)
- **Recursive CTEs:** Kỹ thuật chuẩn hóa để truy vấn mối quan hệ Cha-Con-Ông cháu.
- **Leaf/Branch/Root Detection:** Xác định vị trí của một node trong cây phân cấp.

### 4. Báo cáo nâng cao (Reporting)
- **Bucketing:** Chia dữ liệu thành các nhóm có kích thước cố định (Fixed size) hoặc số lượng nhóm cố định.
- **Subtotals:** Sử dụng `ROLLUP`, `CUBE` để tính toán tổng phụ cho mọi tổ hợp biểu thức.
- **Benford's Law & Outlier Detection:** Ứng dụng thống kê trong SQL để phát hiện bất thường.

## 📈 Đóng góp cho Master Synthesis (SQL Mastery)
- Bổ sung chương **Metadata & Dynamic SQL**.
- Bổ sung chương **Hierarchical & Recursive Queries**.
- Bổ sung kỹ thuật **Advanced Reporting (Rollup/Cube)**.

## 🛠️ Mining Stats
- **Total Lines Scanned:** ~800 lines (Table of Contents & Preface).
- **Key Concepts Identified:** 6.
- **Entities Identified:** 1 (Book Source).
