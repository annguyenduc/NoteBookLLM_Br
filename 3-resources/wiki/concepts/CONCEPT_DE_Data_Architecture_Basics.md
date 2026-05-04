---
file_id: "WIKI_CONCEPT_DE_DATA_ARCHITECTURE"
title: "Kiến trúc dữ liệu cơ bản (Warehouse vs Lake vs Lakehouse)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DE", "Architecture"]
source: "[[SOURCE_DE_Fundamentals_of_Data_Engineering]]"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

relationships:
  - type: "relates_to"
    target: "[[ENTITY_EXCEL]]"
  - type: "relates_to"
    target: "[[ENTITY_SQL]]"
# Kiến trúc dữ liệu cơ bản (Warehouse vs Lake vs Lakehouse)

Việc hiểu cách dữ liệu được lưu trữ ở quy mô lớn là chìa khóa để Data Analyst biết mình đang lấy dữ liệu từ đâu và chất lượng dữ liệu đó như thế nào.

## 核心 (Core Principle)
1. **Data Warehouse (Kho dữ liệu):** Lưu trữ dữ liệu có cấu trúc, đã được làm sạch và tối ưu hóa cho việc truy vấn/báo cáo. 
   - *Đặc điểm:* Schema-on-write (phải định nghĩa cấu trúc trước khi ghi).
2. **Data Lake (Hồ dữ liệu):** Lưu trữ dữ liệu ở dạng thô (Raw), bao gồm cả cấu trúc, bán cấu trúc và phi cấu trúc.
   - *Đặc điểm:* Schema-on-read (chỉ định nghĩa cấu trúc khi cần đọc). Chi phí thấp nhưng dễ trở thành "Data Swamp" (đầm lầy dữ liệu) nếu không quản lý tốt.
3. **Data Lakehouse:** Kiến trúc hiện đại kết hợp tính linh hoạt, chi phí thấp của Data Lake với khả năng quản lý dữ liệu và hiệu suất của Data Warehouse.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trong trang 32-35, tác giả giải thích rằng Data Warehouse giống như một thư viện được sắp xếp ngăn nắp, trong khi Data Lake giống như một kho chứa đồ khổng lồ nơi bạn ném mọi thứ vào và sẽ phân loại sau. Data Lakehouse ra đời để giải quyết bài toán quản lý giao dịch (ACID) ngay trên môi trường Lake.

### 2. Ứng dụng sư phạm (Pedagogical Application)
- **Data Warehouse:** Một bảng [[ENTITY_EXCEL|Excel]] báo cáo doanh thu cuối tháng đã được kế toán kiểm duyệt (Sạch, tin cậy, dùng để báo cáo ngay).
- **Data Lake:** Thư mục chứa hàng ngàn file log, ảnh chụp hóa đơn, tin nhắn khách hàng (Thô, lộn xộn, cần kỹ sư dữ liệu xử lý trước khi dùng).
- **Data Lakehouse:** Hệ thống cho phép bạn truy vấn [[ENTITY_SQL|SQL]] trực tiếp lên các file hóa đơn thô đó với tốc độ cực nhanh mà không cần đợi nạp vào Warehouse.

## Liên kết tư duy
- [[CONCEPT_DE_ETL_ELT_Workflows]]
- [[CONCEPT_DE_Data_Modeling_Star_Schema]]

## 4F — Phản tư sư phạm
- **Facts:** Data Lakehouse đang trở thành tiêu chuẩn mới, xóa nhòa ranh giới giữa kỹ sư và nhà phân tích.
- **Feelings:** Việc quản lý "Data Swamp" là nỗi sợ lớn nhất của các DA khi làm việc với môi trường Lake.
- **Findings:** Sự khác biệt lớn nhất không nằm ở công nghệ mà ở "Schema-on-write" vs "Schema-on-read".
- **Futures:** Cần đào tạo giáo viên cách phân loại dữ liệu thô (Lake) trước khi hướng dẫn học sinh làm báo cáo (Warehouse).

---
Nguồn: [[SOURCE_DE_Fundamentals_of_Data_Engineering]] (Page 32-40, Chapter 1) (Xác nhận Rule 14 từ: `DE_Fundamentals_of_Data_Engineering`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
