---
file_id: "WIKI_CONCEPT_DE_INDEXING_OPTIMIZATION"
title: "Tối ưu hóa chỉ mục (Indexing & Optimization)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DE", "Optimization"]
source: "[[SOURCE_DE_Fundamentals_of_Data_Engineering]]"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Tối ưu hóa chỉ mục (Indexing & Optimization)

Chỉ mục (Index) là cấu trúc dữ liệu giúp tăng tốc độ tìm kiếm bản ghi trong cơ sở dữ liệu mà không cần phải quét toàn bộ bảng.

## 核心 (Core Principle)
1. **B-Tree Index:** Phổ biến nhất, hiệu quả cho các phép so sánh `=`, `>`, `<`.
2. **Hash Index:** Cực nhanh cho phép so sánh bằng `=`, nhưng không dùng được cho khoảng.
3. **Bitmap Index:** Hiệu quả cho các cột có ít giá trị (Low cardinality) như Giới tính, Trạng thái.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 80-85 giải thích rằng việc tạo quá nhiều Index sẽ làm chậm tốc độ ghi dữ liệu (INSERT/UPDATE) vì hệ thống phải cập nhật cả bảng chính và các file Index. Index giống như mục lục của một cuốn sách; nó giúp tìm trang nhanh hơn nhưng làm cuốn sách dày lên.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng thư viện trường học:
- **Không có Index:** Thủ thư phải đi từng kệ sách từ đầu đến cuối để tìm cuốn "Lập trình Scratch" (Full Table Scan).
- **Có Index:** Thủ thư tra cứu thẻ catalog (Index), biết ngay cuốn sách nằm ở Kệ 5, Ngăn 2.
Việc dạy học sinh về Index giúp các em hiểu tại sao việc đặt tên file có cấu trúc hoặc đánh số thứ tự lại quan trọng.

## Liên kết tư duy
- [[CONCEPT_DE_Data_Modeling_Star_Schema]]
- [[CONCEPT_DE_Data_Partitioning]]

## 4F — Phản tư sư phạm
- **Facts:** Index là "con dao hai lưỡi" – tăng tốc độ đọc nhưng giảm tốc độ ghi.
- **Feelings:** Nhà phân tích thường có xu hướng yêu cầu IT tạo Index cho mọi cột, điều này có thể làm tê liệt hệ thống.
- **Findings:** Việc chọn đúng cột để Index (thường là các cột trong điều kiện WHERE hoặc JOIN) là một nghệ thuật.
- **Futures:** Các hệ thống cơ sở dữ liệu hiện đại đang phát triển tính năng "Auto-indexing" dựa trên AI.

---
Nguồn: [[SOURCE_DE_Fundamentals_of_Data_Engineering]] (Page 80-95, Chapter 4) (Xác nhận Rule 14 từ: `DE_Fundamentals_of_Data_Engineering`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
