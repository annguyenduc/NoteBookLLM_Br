---
source_id: SOURCE_DE_Data_Warehouse_Toolkit
title: "ACAD The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling"
author: "Ralph Kimball & Margy Ross"
category: ACAD
domain: "Data Engineering / Data Modeling"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

relationships:
  - type: "relates_to"
    target: "[[ENTITY_SQL]]"
# ACAD The Data Warehouse Toolkit

## 📝 1. Phân tích Ingest (Analysis - Step 1)
- **Thực thể & Khái niệm then chốt:** Star Schema, Fact Tables, Dimension Tables, Bus Matrix, Slowly Changing Dimensions (SCD), Grain of the table, Junk/Degenerate dimensions.
- **Kết nối Wiki:** Cung cấp lý thuyết nền tảng cho việc thiết kế Database của nhóm [[index]]. Kết nối trực tiếp với [[CONCEPT_DE_Data_Modeling_Star_Schema]].
- **Điểm khác biệt/Mâu thuẫn:** Phản biện lại mô hình chuẩn hóa 3NF trong phân tích dữ liệu, ủng hộ mô hình "Phẳng hóa" có kiểm soát để tối ưu hóa hiệu năng BI.
- **Đề xuất cấu trúc:** Cần xây dựng trang [[CONCEPT_DE_SCD_Types]] để hướng dẫn cách quản lý dữ liệu thay đổi theo thời gian (ví dụ: học viên chuyển lớp, giáo viên đổi tên).

## 📖 2. Tổng quan nguồn (Overview - Step 2)
Cuốn sách định nghĩa lại cách thế giới xây dựng kho dữ liệu. Ralph Kimball giới thiệu phương pháp tiếp cận hướng người dùng, nơi dữ liệu được tổ chức thành các "Fact" (sự kiện) và "Dimension" (bối cảnh), giúp việc truy vấn bằng [[ENTITY_SQL|SQL]] trở nên trực quan và nhanh chóng hơn bao giờ hết.

## 🚀 3. Các Concept đã trích xuất (Rule 14 & 17)
- [[CONCEPT_DE_Data_Modeling_Star_Schema]] | **Sơ đồ hình sao** - Cách kết nối Fact và Dimension.
- [[CONCEPT_DE_Data_Architecture_Basics]] | **Kiến trúc dữ liệu** - Vai trò của Warehouse trong hệ thống.
- [[CONCEPT_DE_Indexing_Optimization]] | **Tối ưu hóa Index** - Ứng dụng trong việc truy vấn Fact Tables lớn.

## 🔍 4. Review Items (Dành cho Human)
- [ ] Đánh giá lại cấu trúc database của hệ thống LMS hiện tại: Có đang theo chuẩn Star Schema không hay vẫn để 3NF?
- [ ] Xác định Grain (độ hạt) của dữ liệu báo cáo EdTech để tránh việc tổng hợp sai (Double counting).

--- 
**Nguồn thô:** `DE_Data_Warehouse_Toolkit`
**Deep Research Query:** `Kimball dimensional modeling techniques summary for data analysts`

## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
