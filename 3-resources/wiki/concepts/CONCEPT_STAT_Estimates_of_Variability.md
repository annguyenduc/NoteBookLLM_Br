---
file_id: "WIKI_CONCEPT_STAT_ESTIMATES_VARIABILITY"
title: "Ước lượng sự biến thiên (Estimates of Variability)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Variability"]
source: "`STAT_Practical_Statistics_for_Data_Scientists`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Ước lượng sự biến thiên (Estimates of Variability)

Biến thiên đo lường mức độ dữ liệu tập trung hay phân tán xung quanh giá trị trung tâm. "Trung bình" thôi là chưa đủ để hiểu dữ liệu.

## 核心 (Core Principle)
1. **Standard Deviation (Độ lệch chuẩn):** Khoảng cách trung bình của các điểm dữ liệu đến số trung bình.
2. **Variance (Phương sai):** Bình phương của độ lệch chuẩn.
3. **IQR (Interquartile Range):** Hiệu giữa bách phân vị thứ 75 và 25. Đây là số đo **Bền vững (Robust)** vì nó bỏ qua các giá trị ngoại lai ở hai đầu.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 25-30 lấy ví dụ về việc đo lường độ ổn định của các linh kiện máy tính. Hai lô linh kiện có thể có cùng tuổi thọ trung bình, nhưng lô có độ lệch chuẩn nhỏ hơn sẽ đáng tin cậy hơn vì chất lượng đồng đều hơn.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Giả sử có hai lớp học có cùng điểm trung bình môn Tin học là 7.0:
- **Lớp A:** Tất cả học sinh đều từ 6.5 đến 7.5 (Độ biến thiên thấp).
- **Lớp B:** Có bạn 10 điểm nhưng cũng có bạn 1 điểm (Độ biến thiên cao).
Việc hiểu **Độ biến thiên** giúp giáo viên nhận ra lớp B cần sự hỗ trợ phân hóa mạnh mẽ hơn, trong khi lớp A có trình độ đồng đều hơn.

## Liên kết tư duy
- [[CONCEPT_STAT_Estimates_of_Location]]
- [[CONCEPT_STAT_Probability_Distributions]]

## 4F — Phản tư sư phạm
- **Facts:** Thế giới thực tế không vận hành dựa trên số trung bình mà vận hành dựa trên sự biến thiên.
- **Feelings:** Học sinh thường sợ các công thức tính SD/Variance vì chúng trông phức tạp.
- **Findings:** IQR là công cụ tốt nhất để phát hiện giá trị ngoại lai (Outliers) một cách định lượng.
- **Futures:** Nên sử dụng các biểu đồ trực quan (như Boxplot) để dạy về biến thiên trước khi giới thiệu công thức toán học.

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 25-35, Chapter 1) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)
