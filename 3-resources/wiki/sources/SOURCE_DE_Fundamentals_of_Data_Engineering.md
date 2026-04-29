---
source_id: SOURCE_DE_Fundamentals_of_Data_Engineering
title: "ACAD Fundamentals of Data Engineering"
author: "Joe Reis & Matt Housley"
category: ACAD
domain: "Data Engineering / Data Architecture"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# ACAD Fundamentals of Data Engineering

## 📝 1. Phân tích Ingest (Analysis - Step 1)
- **Thực thể & Khái niệm then chốt:** Data Engineering Lifecycle, Ingestion patterns, Storage (Lakehouse, Mesh), Transformation (Batch/Stream), Data Serving, Security & Governance.
- **Kết nối Wiki:** Cung cấp tư duy hệ thống cho nhóm [[DE]]. Kết nối mật thiết với [[CONCEPT_DE_Data_Architecture_Basics]] và [[CONCEPT_DE_ETL_ELT_Workflows]].
- **Điểm khác biệt/Mâu thuẫn:** Nhấn mạnh rằng công nghệ (Spark, Airflow...) chỉ là thứ yếu so với việc làm chủ vòng đời dữ liệu và các yêu cầu về quản trị (Governance).
- **Đề xuất cấu trúc:** Bắt buộc xây dựng trang [[CONCEPT_DE_Data_Engineering_Lifecycle]] và các trang về [[CONCEPT_DE_Data_Governance]] để lấp đầy các khoảng trống đã phát hiện.

## 📖 2. Tổng quan nguồn (Overview - Step 2)
Tài liệu định nghĩa lại ngành kỹ thuật dữ liệu bằng cách tập trung vào vòng đời dữ liệu thay vì các công cụ cụ thể. Sách giúp các Data Analyst hiểu sâu về cách dữ liệu "chảy" qua các hệ thống, từ khi sinh ra cho đến khi sẵn sàng để phân tích, giúp họ phối hợp tốt hơn với đội ngũ Data Engineer.

## 🚀 3. Các Concept đã trích xuất (Rule 14 & 17)
- [[CONCEPT_DE_Data_Architecture_Basics]] | **Cơ sở kiến trúc dữ liệu** - Các thành phần trong một hệ thống hiện đại.
- [[CONCEPT_DE_ETL_ELT_Workflows]] | **Luồng ETL/ELT** - Sự khác biệt và khi nào nên dùng cái nào.
- [[CONCEPT_DE_Data_Modeling_Star_Schema.md]] | **Mô hình hóa dữ liệu** - Cách thiết kế kho dữ liệu hiệu quả.

## 🔍 4. Review Items (Dành cho Human)
- [ ] Xem xét việc áp dụng "Data Engineering Lifecycle" vào việc tối ưu hóa kho dữ liệu nội bộ của dự án.
- [ ] Kiểm tra xem các tiêu chuẩn về "Data Quality" trong sách có khớp với bộ khung hiện tại không.

--- 
**Nguồn thô:** `DE_Fundamentals_of_Data_Engineering`
**Deep Research Query:** `Data engineering lifecycle Joe Reis summary for analysts`