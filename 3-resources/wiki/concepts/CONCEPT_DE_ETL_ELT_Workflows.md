---
file_id: "WIKI_CONCEPT_DE_ETL_ELT_WORKFLOWS"
title: "Quy trình ETL và ELT (ETL vs ELT Workflows)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DE", "Workflow"]
source: "[[SOURCE_DE_Fundamentals_of_Data_Engineering]]"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Quy trình ETL và ELT (ETL vs ELT Workflows)

ETL và ELT là hai phương pháp chính để di chuyển và biến đổi dữ liệu từ nguồn thô vào kho lưu trữ để phân tích.

## 核心 (Core Principle)
1. **ETL (Extract, Transform, Load):** Dữ liệu được biến đổi *trước* khi nạp vào Warehouse. Phù hợp với dữ liệu có cấu trúc và cần tính bảo mật cao.
2. **ELT (Extract, Load, Transform):** Dữ liệu được nạp vào Lake/Warehouse trước, sau đó mới biến đổi bằng sức mạnh của Cloud. Phù hợp với Big Data và yêu cầu tốc độ nạp nhanh.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Tác giả giải thích sự chuyển dịch từ ETL (truyền thống, On-premise) sang ELT (hiện đại, Cloud). ELT cho phép lưu trữ mọi thứ ở dạng thô trước, giúp nhà phân tích có thể thay đổi logic biến đổi sau này mà không cần nạp lại dữ liệu từ đầu.

### 2. Ứng dụng sư phạm (Pedagogical Application)
- **ETL:** Giống như việc bạn rửa rau và thái sẵn ở siêu thị trước khi mang về nhà (Rau đã sạch và sẵn sàng nấu, nhưng bạn không thể đổi ý thái kiểu khác).
- **ELT:** Giống như việc bạn mua cả bó rau về nhà, nạp vào tủ lạnh, khi nào cần nấu món gì mới bắt đầu rửa và thái theo ý muốn.

## Liên kết tư duy
- [[CONCEPT_DE_Data_Architecture_Basics]]
- [[CONCEPT_DE_Data_Quality_Framework]]

## 4F — Phản tư sư phạm
- **Facts:** Cloud Computing (BigQuery, Snowflake) là yếu tố chính thúc đẩy sự phổ biến của ELT.
- **Feelings:** Nhà phân tích thường cảm thấy tự do hơn với ELT vì họ có quyền truy cập vào dữ liệu thô.
- **Findings:** ETL vẫn cực kỳ quan trọng trong các ngành tài chính/y tế vì dữ liệu cần được ẩn danh (Anonymized) trước khi lưu trữ.
- **Futures:** Xu hướng "Data Mesh" đang làm thay đổi cách chúng ta nghĩ về các Pipeline tập trung.

---
Nguồn: [[SOURCE_DE_Fundamentals_of_Data_Engineering]] (Page 45-55, Chapter 2) (Xác nhận Rule 14 từ: `DE_Fundamentals_of_Data_Engineering`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
