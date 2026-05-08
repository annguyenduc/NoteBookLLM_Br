---
file_id: CONCEPT_VIZ_PowerBI_Basics
title: Power BI Basics (Cơ bản về Power BI)
type: concept
status: VERIFIED
tags:
  - Wiki Page
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-03
last_updated: 2026-05-03
---

## ## For future Claude
Trang này định nghĩa các kiến thức cơ bản về Power BI - công cụ BI hàng đầu của Microsoft. Chúng ta tập trung vào quy trình "End-to-End" từ nạp dữ liệu, biến đổi dữ liệu (Power Query), xây dựng mô hình (Data Modeling) đến trực quan hóa (Visualization). Đây là công cụ chủ đạo trong mảng Business Intelligence của lộ trình Data Analyst.

## ## Key Claims / Summary
1.  **Self-Service BI**: Power BI cho phép người dùng nghiệp vụ tự tạo báo cáo mà không cần sự can thiệp sâu của bộ phận IT.
2.  **Power Query (ETL)**: Khả năng làm sạch và biến đổi dữ liệu mạnh mẽ thông qua ngôn ngữ M.
3.  **DAX (Data Analysis Expressions)**: Ngôn ngữ tính toán mạnh mẽ tương tự Excel nhưng được tối ưu hóa cho mô hình dữ liệu lớn.

## ## Ví dụ đối chiếu (R18)
-   **Ví dụ thực tế (Original)**: Sử dụng Power Query để "Unpivot" dữ liệu từ dạng bảng chéo (Matrix) sang dạng danh sách (Flat table) để có thể xây dựng các biểu đồ linh hoạt.
-   **Ẩn dụ sư phạm (Pedagogical)**: Giống như một xưởng chế biến thực phẩm. Dữ liệu thô là "nguyên liệu" chưa sơ chế (Nạp dữ liệu). Power Query là "dao và máy thái" (Làm sạch). DAX là "gia vị" (Tính toán chỉ số). Và Dashboard cuối cùng là "món ăn" được trình bày đẹp mắt trên đĩa cho thực khách (Người dùng báo cáo) thưởng thức.

## ## Detailed Analysis
Các thành phần cốt lõi của Power BI:
- **Power BI Desktop**: Ứng dụng cài đặt trên máy tính để thiết kế báo cáo.
- **Power BI Service**: Nền tảng đám mây để chia sẻ và quản lý báo cáo.
- **Power BI Mobile**: Ứng dụng xem báo cáo trên điện thoại.
- **Workflow**: Get Data -> Transform (Power Query) -> Model (Relationships) -> Visualize -> Publish.

## ## Relationships
- `part_of` -> [[ENTITY_Data_Science]]
- `uses` -> [[ENTITY_SQL]]
- `relates_to` -> CONCEPT_VIZ_Data_Storytelling_Framework

## ## Source Tracing
- **Nguồn**: SOURCE_VIZ_INTRODUCING_POWER_BI — Section 1: Introduction.
- **Nguồn**: SOURCE_VIZ_ANALYZING_DATA_POWER_BI — Chapter 2: Data Transformation.

## ## History / Revisions
- **2026-05-03**: [@engineer] Chuyển đổi từ stub sang verified, bổ sung R18 và Rule 20.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
