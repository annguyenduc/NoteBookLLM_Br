---
file_id: "WIKI_CONCEPT_STAT_CONFIDENCE_INTERVALS"
title: "Khoảng tin cậy (Confidence Intervals)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Estimation"]
source: "[[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]]"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Khoảng tin cậy (Confidence Intervals)

Thay vì chỉ đưa ra một con số ước lượng duy nhất, khoảng tin cậy cung cấp một phạm vi giá trị kèm theo một mức độ chắc chắn.

## 核心 (Core Principle)
1. **Định nghĩa:** Một khoảng $(a, b)$ sao cho chúng ta tin tưởng $X\%$ rằng giá trị thực của quần thể nằm trong đó.
2. **Mức tin cậy (Confidence Level):** Thường là 95%. Điều này nghĩa là nếu chúng ta lặp lại việc lấy mẫu 100 lần, thì khoảng 95 lần khoảng tin cậy sẽ chứa giá trị thực.
3. **Mối quan hệ:** Khoảng tin cậy càng hẹp thì ước lượng càng chính xác. Khoảng hẹp hơn khi kích thước mẫu tăng lên.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 85-90 giải thích về việc ước lượng mức chi tiêu trung bình của khách hàng. Thay vì nói "Khách hàng chi 50 USD", báo cáo thống kê sẽ nói: "Chúng tôi tin tưởng 95% rằng mức chi tiêu trung bình nằm trong khoảng từ 45 USD đến 55 USD".

### 2. Ứng dụng sư phạm (Pedagogical Application)
Giả sử giáo viên ước lượng thời gian học sinh làm bài kiểm tra:
- "Dựa trên mẫu 10 học sinh, tôi tin tưởng 95% rằng thời gian trung bình cả lớp làm xong bài là từ 35 đến 45 phút."
Điều này giúp giáo viên dự phòng được trường hợp học sinh làm bài chậm nhất và nhanh nhất để sắp xếp thời gian tiết học hợp lý.

## Liên kết tư duy
- [[CONCEPT_STAT_Central_Limit_Theorem]]
- [[CONCEPT_STAT_Hypothesis_Testing_PValue]]

## 4F — Phản tư sư phạm
- **Facts:** Khoảng tin cậy 95% KHÔNG có nghĩa là có 95% xác suất giá trị thực nằm trong đó (đó là cách hiểu sai phổ biến).
- **Feelings:** Nhiều người cảm thấy "mất tự tin" khi đưa ra một khoảng thay vì một con số cụ thể, nhưng đó mới là sự trung thực trong dữ liệu.
- **Findings:** Biên sai số (Margin of Error) là một nửa độ rộng của khoảng tin cậy.
- **Futures:** Cần dạy học sinh cách đọc các biểu đồ có "Error bars" để hiểu về sự không chắc chắn (Uncertainty).

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 80-90, Chapter 2) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
