---
file_id: "WIKI_CONCEPT_DE_DATA_QUALITY_FRAMEWORK"
title: "Khung quản lý chất lượng dữ liệu (Data Quality Framework)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DE", "Governance"]
source: "[[SOURCE_DE_Fundamentals_of_Data_Engineering]]"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Khung quản lý chất lượng dữ liệu (Data Quality Framework)

Chất lượng dữ liệu quyết định sự tin cậy của các báo cáo và quyết định kinh doanh. "Garbage in, Garbage out" (Rác vào, Rác ra) là cảnh báo hàng đầu cho mọi nhà phân tích.

## 核心 (Core Principle)
6 trụ cột của chất lượng dữ liệu:
1. **Accuracy (Độ chính xác):** Dữ liệu có phản ánh đúng thực tế không?
2. **Completeness (Độ đầy đủ):** Có bị thiếu giá trị (NULL) không?
3. **Consistency (Tính nhất quán):** Dữ liệu ở các nguồn khác nhau có khớp nhau không?
4. **Timeliness (Tính kịp thời):** Dữ liệu có mới nhất không?
5. **Validity (Tính hợp lệ):** Dữ liệu có đúng định dạng yêu cầu không? (ví dụ: email phải có @).
6. **Uniqueness (Tính duy nhất):** Có bị trùng lặp không?

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 120-130 thảo luận về việc triển khai "Data Contracts" giữa kỹ sư và nhà phân tích để đảm bảo rằng nếu hệ thống nguồn thay đổi định dạng dữ liệu, các báo cáo bên dưới sẽ không bị hỏng đột ngột.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Quản lý sổ điểm học sinh:
- **Accuracy:** Nhập nhầm điểm 9 thành 6.
- **Completeness:** Quên nhập điểm cho một học sinh.
- **Validity:** Nhập điểm là "A" thay vì số từ 0-10.
Việc cho học sinh tự kiểm tra lỗi (Peer-audit) trong bộ dữ liệu của nhau là cách tốt nhất để dạy về 6 trụ cột này.

## Liên kết tư duy
- [[CONCEPT_DE_ETL_ELT_Workflows]]
- [[CONCEPT_DE_Data_Architecture_Basics]]

## 4F — Phản tư sư phạm
- **Facts:** Không bao giờ có dữ liệu sạch 100% trong thực tế.
- **Feelings:** Nhà phân tích thường mất 80% thời gian để làm sạch dữ liệu và chỉ 20% để phân tích.
- **Findings:** Chất lượng dữ liệu phải được kiểm soát ngay từ nguồn (Data entry) thay vì đợi đến lúc vào Warehouse.
- **Futures:** Kiểm thử dữ liệu tự động (như dbt tests) đang trở thành kỹ năng bắt buộc.

---
Nguồn: [[SOURCE_DE_Fundamentals_of_Data_Engineering]] (Page 120-140, Chapter 5) (Xác nhận Rule 14 từ: `DE_Fundamentals_of_Data_Engineering`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
