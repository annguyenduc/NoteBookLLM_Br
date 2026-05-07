---
file_id: CONCEPT_DE_DATA_MODELING_STAR_SCHEMA
title: "Star Schema Data Modeling (Mô hình hóa dữ liệu hình sao)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "SOURCE_DE_FUNDAMENTALS_OF_DATA_ENGINEERING"
  - "SOURCE_TOOL_PYTHON_FOR_DATA_ANALYSIS"
---

## ## For future Claude
Trang này định nghĩa mô hình Star Schema - kỹ thuật mô hình hóa dữ liệu tối ưu cho các bài toán phân tích (OLAP). Bằng cách tách biệt các chỉ số đo lường (Fact) và thông tin mô tả (Dimension), Star Schema giúp đơn giản hóa các truy vấn SQL phức tạp và tăng tốc độ xử lý báo cáo trong Data Warehouse.

## ## Key Claims / Summary
1.  **Fact-Dimension Split**: Phân tách rõ ràng giữa sự kiện (Fact) và bối cảnh (Dimension).
2.  **Denormalization**: Chấp nhận dư thừa dữ liệu ở mức độ nhẹ để đổi lấy tốc độ truy vấn vượt trội.
3.  **Simplicity**: Cấu trúc dễ hiểu cho người dùng kinh doanh khi thực hiện Self-service BI.

## 1. Đặc điểm cấu trúc
- **Bảng Fact**: Chứa các số liệu đo lường (ví dụ: Số tiền bán hàng, Số lượng) và các khóa ngoại.
- **Bảng Dimension**: Chứa thông tin mô tả chi tiết (ví dụ: Tên sản phẩm, Địa chỉ khách hàng).
- **Cấu trúc**: Một bảng Fact ở giữa kết nối với nhiều bảng Dimension xung quanh tạo thành hình ngôi sao.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Bảng `Fact_Sales` ở giữa chứa các cột `Quantity`, `Revenue`. Xung quanh là các bảng `Dim_Product` (Tên sản phẩm, Màu sắc), `Dim_Date` (Ngày, Tháng, Năm), `Dim_Store` (Tên cửa hàng, Thành phố).
- **Ẩn dụ sư phạm (Pedagogical)**: [Phóng tác] Giống như một động từ trong câu. Bảng Fact là "Động từ" (Hành động: Bán hàng). Các bảng Dimension là các "Trạng từ" trả lời cho câu hỏi: Ai mua? Mua cái gì? Mua ở đâu? Mua khi nào? Nếu không có trạng từ, động từ trở nên vô nghĩa.

## ## Source Tracing
- **Nguồn**: SOURCE_DE_FUNDAMENTALS_OF_DATA_ENGINEERING — Chapter 4: Data Modeling.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
