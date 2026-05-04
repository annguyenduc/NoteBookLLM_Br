---
file_id: "WIKI_CONCEPT_STAT_DATA_TAXONOMY"
title: "Phân loại dữ liệu (Data Taxonomy)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Taxonomy"]
source: "[[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]]"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Phân loại dữ liệu (Data Taxonomy)

Dữ liệu không chỉ là những con số; việc phân loại đúng loại dữ liệu là bước đầu tiên để chọn phương pháp thống kê và biểu đồ phù hợp.

## 核心 (Core Principle)
1. **Dữ liệu số (Numeric):**
   - *Liên tục (Continuous):* Có thể nhận bất kỳ giá trị nào trong một khoảng (ví dụ: chiều cao, tốc độ).
   - *Rời rạc (Discrete):* Chỉ nhận các giá trị nguyên (ví dụ: số lượng học sinh).
2. **Dữ liệu phân loại (Categorical):**
   - *Danh mục (Nominal):* Không có thứ tự (ví dụ: màu sắc, giới tính).
   - *Thứ bậc (Ordinal):* Có thứ tự rõ ràng (ví dụ: xếp loại học lực: Giỏi > Khá > Trung bình).

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trong chương 1 (trang 2-5), tác giả giải thích về sự khác biệt giữa biến định tính và định lượng. Việc nhầm lẫn giữa dữ liệu Ordinal (thứ bậc) và dữ liệu Numeric (số) thường dẫn đến việc tính toán trung bình vô nghĩa trên các bảng khảo sát mức độ hài lòng.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng một bảng điểm lớp học:
- **Điểm số (0-10):** Dữ liệu Số liên tục.
- **Xếp loại (Giỏi, Khá):** Dữ liệu Phân loại thứ bậc.
- **Môn học ưa thích:** Dữ liệu Phân loại danh mục.
Việc dạy học sinh phân biệt các loại này giúp các em biết rằng không thể tính "Trung bình cộng của màu sắc" nhưng có thể tính "Tỷ lệ phần trăm của màu sắc".

## Liên kết tư duy
- [[CONCEPT_STAT_Estimates_of_Location]]
- [[CONCEPT_STAT_Probability_Distributions]]

## 4F — Phản tư sư phạm
- **Facts:** Máy tính luôn coi mọi thứ là số, nhưng nhà phân tích phải biết ý nghĩa thực của số đó.
- **Feelings:** Người mới học thường cảm thấy "rắc rối" khi phải phân loại quá chi tiết, nhưng đây là nền tảng của mọi thuật toán.
- **Findings:** Dữ liệu Ordinal là loại "lai" gây khó khăn nhất trong việc xử lý.
- **Futures:** Cần xây dựng các trò chơi phân loại dữ liệu (như kéo thả) để học sinh nắm vững kiến thức này một cách tự nhiên.

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 2-10, Chapter 1) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
