---
file_id: "CONCEPT_TOOL_DATA_ANALYSIS_PROMPTS"
title: "Mẫu câu lệnh Phân tích dữ liệu (Data Analysis Prompts)"
category: "TOOL"
prefix: "TOOL"
tags: ["Gemini", "Data_Analysis", "[[ENTITY_Python|Python]]", "[[ENTITY_SQL|SQL]]", "Prompts"]
source: "[[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]]"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-01"
---

# Mẫu câu lệnh Phân tích dữ liệu (Data Analysis Prompts)

## 1. Định nghĩa
Đây là tập hợp các cấu trúc câu lệnh được tối ưu hóa để yêu cầu Gemini thực hiện các tác vụ từ làm sạch dữ liệu, biến đổi cấu trúc đến tạo mã nguồn trực quan hóa.

## 2. Các mẫu cốt lõi (Patterns)

### Mẫu 1: Trích xuất & Chuyển đổi (Transformation)
> **Cấu trúc**: "Acting as a Data Engineer, write a Python script using [[ENTITY_PANDAS|Pandas]] to transform [Source_Format] to [Target_Format]. Specifically, handle missing values by [Strategy] and normalize [Column_Names]."
> **Mục tiêu**: Tự động hóa công đoạn chuẩn bị dữ liệu (Data Prep).

### Mẫu 2: Phân tích Khám phá (EDA)
> **Cấu trúc**: "Analyze the provided dataset schema. Suggest 5 key hypotheses I should test and provide the Python code to generate the descriptive statistics for each."
> **Mục tiêu**: Khai phá ý tưởng phân tích từ Schema thô.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ kỹ thuật (Technical)
> **Bối cảnh**: Chuyển đổi dữ liệu JSON lồng nhau sang DataFrame phẳng.
> **Prompt**: "Gemini, flatten this nested JSON customer data. Create a column for each address field and ensure date formats are ISO-8601 compliant. Show the Pandas code."
> **Nguồn**: [SOURCE_TOOL_GEMINI_DEVELOPER_CODEX.md] — Section 4.1: Data Transformation

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Giảng dạy khái niệm "Làm sạch dữ liệu" cho sinh viên.
> **Ứng dụng**: Giáo viên có thể dùng Gemini để tạo ra các bộ dữ liệu "bẩn" có chủ đích (missing values, outliers) và sau đó cung cấp prompt mẫu để sinh viên học cách yêu cầu AI sửa lỗi. Điều này giúp sinh viên hiểu cả lý thuyết và cách giao tiếp với công cụ.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
