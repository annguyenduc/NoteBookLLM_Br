---
file_id: "ENTITY_SQL"
title: "Thực thể: SQL (Structured Query Language)"
type: entity
domain: SQL
status: verified
sources:
  - SOURCE_TOOL_SQL_GETTING_STARTED
tags: [sql, data-science, database, rdbms]
created: 2026-04-29
updated: 2026-04-29
---

# Thực thể: SQL (Structured Query Language)

## 1. Định nghĩa cốt lõi
**SQL (Structured Query Language)** là ngôn ngữ tiêu chuẩn dùng để giao tiếp, quản lý và thao tác với các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS). 
RDBMS là loại cơ sở dữ liệu tổ chức dữ liệu thành các bảng (Tables) có quan hệ với nhau (thông qua Primary Keys và Foreign Keys), giúp dữ liệu không bị dư thừa (Normalization).

 Nguồn: `SQLDB_SQL_Getting_Started.md` — [Page 19-20]

## 2. Vai trò trong Data Analyst / [[ENTITY_Data_Science|Data Science]]
- **Truy vấn dữ liệu**: Trích xuất dữ liệu thô từ các cơ sở dữ liệu. Mọi tác vụ khai thác dữ liệu đều bắt đầu bằng câu lệnh `SELECT`.
- **Tiền xử lý (Data Prep)**: Lọc (WHERE), gom nhóm (GROUP BY), nối bảng (JOIN) trước khi đưa vào các công cụ phân tích (như Tableau, PowerBI) hoặc Python/R.
- **Khám phá dữ liệu (EDA)**: Nhanh chóng thống kê và xem xét các mẫu (patterns) cơ bản thông qua các hàm Aggregate (SUM, AVG).

## 3. Phân loại Database Engines
SQL là ngôn ngữ chuẩn, nhưng có nhiều nền tảng (Engines) triển khai nó:
1. **Lightweight Databases**: (vd: SQLite, Microsoft Access). Dùng cho ứng dụng cá nhân, mobile, prototyping. File dữ liệu lưu cục bộ, không có server.
2. **Centralized Databases**: (vd: MySQL, PostgreSQL, Microsoft SQL Server, Oracle). Triển khai trên máy chủ (Client-Server), hỗ trợ xử lý hàng ngàn request đồng thời. Đây là môi trường làm việc chính của Data Analyst.

 Nguồn: `SQLDB_SQL_Getting_Started.md` — [Page 21-22]

## 4. Các thực thể & Concept liên quan (Cross-References)
-   **Ngôn ngữ/Công cụ khác**: ENTITY_Python, [[ENTITY_Data_Science]]
-   **Khái niệm lõi SQL**: [[CONCEPT_SQL_Select_And_Filter]], [[CONCEPT_SQL_Joins]], [[CONCEPT_SQL_Aggregations]]

---
[AUDITOR] Rule 14: Trang thực thể được cập nhật từ nội dung cốt lõi của sách SQL Getting Started, kết hợp với góc nhìn Data Analyst.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
