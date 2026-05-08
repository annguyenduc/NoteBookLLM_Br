---
file_id: CONCEPT_TOOL_SQL_Query_Prompts
title: Mẫu câu lệnh Tối ưu hóa [[ENTITY_SQL|SQL]] (SQL Query Prompts)
type: concept
status: VERIFIED
tags: 
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-01
---

# Mẫu câu lệnh Tối ưu hóa SQL (SQL Query Prompts)

## 1. Định nghĩa
Tập hợp các prompt giúp Gemini đóng vai trò chuyên gia cơ sở dữ liệu để viết, giải thích và tối ưu hóa các truy vấn phức tạp (SQL/NoSQL).

## 2. Các mẫu cốt lõi (Patterns)

### Mẫu 1: Tối ưu hóa hiệu năng (Performance Tuning)
> **Cấu trúc**: "Act as a Database Expert. Context: [Paste complex SQL query]. Task: Refactor this query for maximum performance. Focus on: reducing nested subqueries, ensuring correct use of window functions, and indexing strategy recommendations."
> **Mục tiêu**: Chuyển đổi các truy vấn chậm thành truy vấn hiệu quả cao.

### Mẫu 2: Bảo mật & Tuân thủ (Security & Compliance)
> **Cấu trúc**: "Role: Lead Data Engineer. Context: [Table Schema]. Task: Outline a data masking and encryption strategy using [Target_DB, e.g., BigQuery] features to ensure GDPR compliance for this specific schema."
> **Mục tiêu**: Thiết kế lớp bảo mật cho dữ liệu nhạy cảm thông qua SQL.

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ kỹ thuật (Technical)
> **Bối cảnh**: Tối ưu hóa một câu lệnh JOIN phức tạp trong PostgreSQL.
> **Prompt**: "Gemini, analyze the execution plan of this SQL. It's taking 5 seconds to run. Suggest 3 indexing strategies and rewrite the JOINs to avoid full table scans."
> **Nguồn**: [SOURCE_TOOL_GEMINI_DEVELOPER_CODEX.md] — Section 4.1.1: SQL Optimization

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Bài tập thực hành SQL cho khóa học Data Engineering.
> **Ứng dụng**: Học sinh được yêu cầu tự viết một câu query giải quyết bài toán kinh doanh, sau đó dùng Gemini để "Code Review" và giải thích tại sao câu query của mình chưa tối ưu. Điều này tạo ra một vòng phản hồi học tập tức thì (Immediate Feedback Loop).


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
