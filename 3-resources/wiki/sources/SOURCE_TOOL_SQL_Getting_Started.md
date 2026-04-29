---
title: "Source: Getting Started with SQL"
type: source
domain: SQL
status: verified
sources:
  - "TOOL_SQL_Getting_Started.md"
tags: [sql, book, thomas-nield, sqlite]
created: 2026-04-29
updated: 2026-04-29
---

# 📖 Source: Getting Started with SQL (Thomas Nield)

## 1. Tổng quan
Cuốn sách "Getting Started with SQL" (Thomas Nield) cung cấp nền tảng cơ bản về SQL và cơ sở dữ liệu quan hệ (RDBMS). Tác giả sử dụng **SQLite** và công cụ GUI **SQLiteStudio** để giúp người học thực hành ngay mà không cần cấu hình server phức tạp.

## 2. Các thực thể & Khái niệm chính
- **Thực thể**: [[ENTITY_SQL]] (RDBMS, SQLite, MySQL).
- **Trích xuất dữ liệu**: [[CONCEPT_SQL_Select_And_Filter]] (Lấy và lọc dữ liệu bằng SELECT, WHERE).
- **Gom nhóm dữ liệu**: [[CONCEPT_SQL_Aggregations]] (Tổng hợp dữ liệu với GROUP BY).
- **Xử lý logic**: [[CONCEPT_SQL_Case_Statements]] (Phân loại dữ liệu linh hoạt).
- **Kết nối bảng**: [[CONCEPT_SQL_Joins]] (Nối dữ liệu từ nhiều nguồn).

## 3. Điểm đáng chú ý (Tensions / Notes)
- Cuốn sách thiên về **SQLite**, là một Lightweight Database. Trong môi trường doanh nghiệp thực tế, Data Analyst thường dùng **Centralized Databases** như PostgreSQL, MySQL, hoặc Cloud DBs. Tuy nhiên, ANSI SQL (cú pháp cơ bản) gần như giống nhau.
- Cuốn sách hướng dẫn cơ sở về **Normalization** (Thiết kế dữ liệu). Nhưng đối với Data Analyst khi truy vấn Data Warehouse, dữ liệu thường đã được **Denormalization** (phi chuẩn hóa) để tăng tốc độ phân tích.

---
[AUDITOR] Rule 14: Tóm tắt này được tạo từ file raw `3-resources/raw/sources/TOOL_SQL_Getting_Started.md`.
