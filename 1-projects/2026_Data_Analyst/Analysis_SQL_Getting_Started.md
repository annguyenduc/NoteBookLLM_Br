# 🕵️ Analysis Report: Getting Started with SQL (Thomas Nield)

> **Agent**: `@scout`
> **Nguồn**: `3-resources/raw/sources/SQLDB_SQL_Getting_Started.md`
> **Mục tiêu**: Trích xuất 20% cốt lõi của SQL dành cho Data Analyst (phục vụ Ingest 80/20).

---

## 1. 📋 Key Entities & Concepts (Thực thể & Khái niệm cốt lõi)

**Entities:**
- **SQL / RDBMS**: Ngôn ngữ truy vấn có cấu trúc và Hệ quản trị CSDL quan hệ (SQLite, MySQL, PostgreSQL).
- **SQLiteStudio**: Công cụ GUI để tương tác với SQLite được sử dụng xuyên suốt sách.

**Concepts (Được map theo danh sách Ingest 80/20):**
- **Truy xuất cơ bản (SELECT, WHERE)**: Toán tử, lọc số/chữ/boolean, xử lý `NULL`, `AND/OR/IN`.
- **Gom nhóm & Sắp xếp (GROUP BY, ORDER BY)**: Các hàm Aggregate (`SUM`, `COUNT`, `AVG`, `MIN`, `MAX`), mệnh đề `HAVING`, lấy bản ghi `DISTINCT`.
- **Logic điều kiện (CASE Statements)**: Cú pháp `CASE WHEN`, nhóm dữ liệu bằng CASE, và thủ thuật *"Zero/Null CASE Trick"* (Kỹ thuật Pivot dữ liệu).
- **Kết nối bảng (JOINs)**: `INNER JOIN`, `LEFT JOIN`, cách kết nối nhiều bảng, Foreign Keys và Primary Keys.
- **Thiết kế & Quản lý dữ liệu (DDL / DML)**: Lược đồ (Schema), `CREATE TABLE`, `INSERT`, `UPDATE`, `DELETE`, `Views`.

---

## 2. 🔗 Connections (Liên kết với Wiki hiện có)

- **`ENTITY_SQL.md`**: Đã tồn tại nhưng đang sơ sài. Nguồn này sẽ cung cấp "da thịt" (cú pháp, định nghĩa) để làm phong phú trang Entity này.
- **`THINK_Data_Mining_Tasks.md`**: SQL chính là công cụ thực thi các tác vụ Data Mining ở bước Data Preparation (Lọc, làm sạch, gom nhóm).
- **`THINK_Analytical_Thinking.md`**: SQL giúp trả lời các câu hỏi phân tích thông qua Aggregate functions.

---

## 3. ⚡ Contradictions & Tensions (Xung đột & Điểm đáng chú ý)

- **SQLite vs Centralized DBs**: Sách dùng SQLite cho dễ học, nhưng Data Analyst thực chiến thường dùng Centralized DBs (PostgreSQL, BigQuery, Snowflake). *Giải pháp:* Khi viết Wiki, `@engineer` phải nhấn mạnh **ANSI SQL Standard**, tránh phụ thuộc quá nhiều vào quirk riêng của SQLite.
- **Normalization vs Denormalization**: Chương 9 dạy về Chuẩn hóa (Normalization) - chia nhỏ bảng để tránh dư thừa. Tuy nhiên, trong Data Warehouse của DA, đôi khi lại ưu tiên Denormalization (gom bảng) để truy vấn nhanh. Cần lưu ý điều này để không làm người học bối rối sau này.

---

## 4. 🔍 Deep Research Queries (Cần nghiên cứu thêm)

Sách này là "Beginner", nên có thể thiếu một vài concept nâng cao mà một DA cần (nằm trong Ingest 80/20):
1. *Window Functions (`OVER`, `PARTITION BY`, `ROW_NUMBER`)* có được cover đủ sâu trong sách này không? Nếu không, cần dùng Web Search bổ sung.
2. *Common Table Expressions (CTEs - `WITH` clause)* có xuất hiện không? (Sách chủ yếu nhắc đến Views).

---

## 5. 📐 Wiki Structure Recommendations (Đề xuất cấu trúc Wiki)

Đề xuất `@engineer` tạo/cập nhật các file sau trong `3-resources/wiki/`:

1. **`sources/SOURCE_SQLDB_SQL_Getting_Started.md`**: Tóm tắt sách.
2. **`entities/ENTITY_SQL.md`**: Cập nhật tổng quan về SQL, RDBMS.
3. **`concepts/CONCEPT_SQL_Select_And_Filter.md`**: `SELECT`, `WHERE`, `NULL` handling.
4. **`concepts/CONCEPT_SQL_Aggregations.md`**: `GROUP BY`, `HAVING`, Aggregation functions.
5. **`concepts/CONCEPT_SQL_Case_Statements.md`**: Logic điều kiện & Pivot trick.
6. **`concepts/CONCEPT_SQL_Joins.md`**: Lược đồ quan hệ, Primary/Foreign keys, `INNER` vs `LEFT JOIN`.
*(Lưu ý: Các concept này cần tuân thủ Rule 17 - Double Examples, có code block mẫu và comment rõ ràng theo chuẩn `CLAUDE.md`).*
