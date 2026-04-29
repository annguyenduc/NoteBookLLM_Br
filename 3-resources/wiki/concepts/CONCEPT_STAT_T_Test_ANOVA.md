---
file_id: "WIKI_CONCEPT_STAT_T_TEST_ANOVA"
title: "Kiểm định T-Test và ANOVA"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Testing"]
source: "`STAT_Practical_Statistics_for_Data_Scientists`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Kiểm định T-Test và ANOVA

Đây là các công cụ quan trọng để so sánh sự khác biệt giữa các nhóm dữ liệu và xác định xem sự khác biệt đó có ý nghĩa thống kê hay không.

## 核心 (Core Principle)
1. **T-Test (Kiểm định T):** Dùng để so sánh giá trị trung bình của **hai nhóm** (ví dụ: Nhóm A vs Nhóm B).
2. **ANOVA (Analysis of Variance):** Dùng khi bạn cần so sánh giá trị trung bình của **ba nhóm trở lên**. 

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 110-115 mô tả thí nghiệm về thời gian tải trang web. T-Test được dùng để so sánh thời gian tải trung bình giữa người dùng dùng trình duyệt Chrome và Safari. Nếu P-value < 0.05, ta kết luận trình duyệt có ảnh hưởng đến tốc độ trải nghiệm.

### 2. Ứng dụng sư phạm (Pedagogical Application)
- **T-Test:** So sánh điểm trung bình môn Toán giữa lớp 10A và lớp 10B sau một bài kiểm tra chung.
- **ANOVA:** So sánh hiệu quả của 3 phương pháp dạy học khác nhau (Học qua dự án, Học truyền thống, Học qua Game).

## Liên kết tư duy
- [[CONCEPT_STAT_Hypothesis_Testing_PValue]]
- [[CONCEPT_STAT_Confidence_Intervals]]

## 4F — Phản tư sư phạm
- **Facts:** T-Test chỉ dùng cho 2 nhóm, nếu dùng cho >2 nhóm sẽ gây ra sai số tích lũy (Alpha inflation).
- **Feelings:** Học sinh thường cảm thấy bối rối giữa việc khi nào dùng T-Test và khi nào dùng ANOVA.
- **Findings:** ANOVA không chỉ ra nhóm nào khác biệt, cần thực hiện Post-hoc test sau đó.
- **Futures:** Cần thiết kế các bảng tính Excel tự động hóa việc tính toán T-Test để học sinh tập trung vào việc đọc hiểu kết quả P-value thay vì công thức.

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 110-120, Chapter 3) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)
