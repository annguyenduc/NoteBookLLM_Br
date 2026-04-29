---
file_id: "WIKI_CONCEPT_DE_DATA_MODELING_STAR_SCHEMA"
title: "Mô hình hóa dữ liệu Star Schema (Star Schema Data Modeling)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DE", "Modeling"]
source: "`DE_Fundamentals_of_Data_Engineering`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Mô hình hóa dữ liệu Star Schema

Star Schema là mô hình thiết kế cơ sở dữ liệu phổ biến nhất cho Business Intelligence, tập trung vào hiệu suất truy vấn và tính dễ hiểu cho người dùng cuối.

## 核心 (Core Principle)
1. **Fact Table (Bảng sự thật):** Chứa các số đo (Metrics) như Doanh thu, Số lượng, Điểm số.
2. **Dimension Tables (Bảng chiều):** Chứa thông tin mô tả như Thời gian, Địa điểm, Sản phẩm, Học sinh.
3. **Cấu trúc:** Một bảng Fact ở giữa kết nối với nhiều bảng Dimension xung quanh trông như một ngôi sao.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 60-65 giải thích về việc tách biệt dữ liệu giao dịch (Fact) và dữ liệu tham chiếu (Dimension). Điều này giúp giảm thiểu việc trùng lặp dữ liệu và cho phép bộ tối ưu hóa SQL thực hiện các phép JOIN cực nhanh.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hệ thống quản lý điểm thi:
- **Bảng Fact:** Lưu Điểm thi, Ngày thi, Mã học sinh, Mã môn học.
- **Bảng Dimension:** 
  - Bảng Học sinh: Tên, Lớp, Ngày sinh.
  - Bảng Môn học: Tên môn, Số tín chỉ.
Việc thiết kế này giúp Hiệu trưởng dễ dàng lọc điểm theo từng học sinh hoặc từng môn học mà không làm chậm hệ thống.

## Liên kết tư duy
- [[CONCEPT_DE_Data_Architecture_Basics]]
- [[CONCEPT_DE_ETL_ELT_Workflows]]

## 4F — Phản tư sư phạm
- **Facts:** Star Schema ưu tiên tốc độ đọc (Read-heavy) hơn là tốc độ ghi.
- **Feelings:** Nhà phân tích thường thấy "dễ thở" hơn khi làm việc với Star Schema so với các bảng phẳng (Flat tables) khổng lồ hoặc mô hình 3NF phức tạp.
- **Findings:** Việc giữ cho bảng Fact "gầy" (chỉ chứa ID và số) là chìa khóa của hiệu suất.
- **Futures:** "One Big Table" (OBT) đang dần trở thành đối thủ của Star Schema trong các kho lưu trữ Cloud hiện đại.

---
Nguồn: [[SOURCE_DE_Fundamentals_of_Data_Engineering]] (Page 60-75, Chapter 3) (Xác nhận Rule 14 từ: `DE_Fundamentals_of_Data_Engineering`)
