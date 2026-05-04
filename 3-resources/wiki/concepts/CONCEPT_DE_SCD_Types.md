---
file_id: "WIKI_CONCEPT_DE_SCD_TYPES"
title: "Chiều thay đổi chậm (Slowly Changing Dimensions - SCD)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["DE", "Data_Modeling", "Warehouse", "History"]
source: "Data_Warehouse_Toolkit"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-02"
agent_id: "@engineer"
---

# Chiều thay đổi chậm (Slowly Changing Dimensions - SCD)

SCD là tập hợp các kỹ thuật quản lý cách dữ liệu trong các bảng Dimension (chiều) thay đổi theo thời gian, đảm bảo tính toàn vẹn của báo cáo lịch sử.

## 核心 (Core Principle)
Bản chất của SCD là sự cân bằng giữa **Dung lượng lưu trữ** và **Khả năng truy vết lịch sử**.
1. **Type 1 (Overwrite):** Luôn giữ giá trị mới nhất. Không lưu lịch sử.
2. **Type 2 (New Row):** Thêm dòng mới cho mỗi lần thay đổi. Đây là cách phổ biến nhất để lưu lịch sử trọn vẹn.
3. **Type 3 (New Column):** Lưu giá trị cũ và mới trên cùng một hàng. Hạn chế về số lượng phiên bản lịch sử.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trong cuốn *The Data Warehouse Toolkit*, Ralph Kimball đưa ra ví dụ về việc khách hàng thay đổi địa chỉ:
- **Type 1:** Cập nhật địa chỉ mới đè lên địa chỉ cũ. Mọi đơn hàng trong quá khứ sẽ bị gán sai vào địa chỉ mới.
- **Type 2:** Tạo dòng mới cho khách hàng đó với địa chỉ mới và các cột `start_date`, `end_date`. Đơn hàng cũ vẫn liên kết với dòng chứa địa chỉ cũ.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng về việc thay đổi giáo viên chủ nhiệm của một lớp học:
- **Type 1 (Ghi đè):** Bạn xóa tên giáo viên cũ trong sổ liên lạc và ghi tên giáo viên mới. Sau 5 năm, bạn sẽ không biết ai đã dạy mình năm lớp 1.
- **Type 2 (Dòng mới):** Bạn gạch dòng cũ, ghi dòng mới xuống dưới. Bạn có thể nhìn lại và thấy: "Từ 2020-2021 là cô A, từ 2021-nay là thầy B". Đây chính là cách SCD Type 2 hoạt động để bảo vệ lịch sử học tập.

## Liên kết tư duy
- [[CONCEPT_DE_Data_Modeling_Star_Schema]]
- [[SOURCE_DE_Data_Warehouse_Toolkit]]

## 4F — Phản tư sư phạm
- **Facts:** Type 2 là "tiêu chuẩn vàng" trong Data Warehousing nhưng tốn nhiều không gian lưu trữ và phức tạp khi truy vấn.
- **Feelings:** Việc chọn sai loại SCD (ví dụ dùng Type 1 cho địa chỉ giao hàng) có thể gây ra thảm họa cho báo cáo doanh thu vùng miền, khiến người phân tích cảm thấy bế tắc vì dữ liệu không còn trung thực.
- **Findings:** SCD không chỉ là kỹ thuật, nó là về việc hiểu "ý nghĩa" của dữ liệu. Nếu sự thay đổi đó quan trọng cho phân tích tương lai, hãy dùng Type 2.
- **Futures:** Trong thế giới Big Data, các kỹ thuật như **Snapshotting** (trong dbt) đang đơn giản hóa việc triển khai SCD Type 2, giúp các kỹ sư tập trung vào logic kinh doanh hơn là code vận hành.

---
Nguồn: [[SOURCE_DE_Data_Warehouse_Toolkit]] (Ralph Kimball)
Xác nhận Rule 14 từ NotebookLM Query (2026-05-02).


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
