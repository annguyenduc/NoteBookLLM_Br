---
file_id: "WIKI_CONCEPT_STAT_ESTIMATES_LOCATION"
title: "Ước lượng vị trí (Estimates of Location)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Location"]
source: "[[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]]"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Ước lượng vị trí (Estimates of Location)

Ước lượng vị trí (hay còn gọi là số đo xu hướng trung tâm) giúp tóm tắt dữ liệu bằng một con số "điển hình" nhất.

## 核心 (Core Principle)
1. **Mean (Trung bình cộng):** Tổng giá trị chia cho số lượng. Nhạy cảm với giá trị ngoại lai (Outliers).
2. **Median (Trung vị):** Giá trị nằm chính giữa khi sắp xếp dữ liệu. Có tính **Bền vững (Robustness)** cao hơn Mean.
3. **Trimmed Mean (Trung bình cắt bỏ):** Loại bỏ một tỷ lệ phần trăm các giá trị ở hai đầu trước khi tính trung bình.
4. **Weighted Mean (Trung bình có trọng số):** Gán tầm quan trọng khác nhau cho từng giá trị.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 10-15 giải thích về việc tính thu nhập trung bình của một khu phố. Nếu có một tỷ phú chuyển đến, Mean sẽ tăng vọt nhưng Median vẫn giữ nguyên, phản ánh đúng hơn mức sống của đa số người dân.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Giả sử giáo viên tính điểm trung bình lớp:
- Nếu cả lớp điểm 8, 9 nhưng có 1 bạn bị 0 điểm -> Mean sẽ bị kéo xuống thấp.
- Sử dụng **Median** sẽ giúp giáo viên đánh giá đúng hơn thực lực của đại đa số học sinh trong lớp mà không bị ảnh hưởng quá mức bởi một bài thi hỏng duy nhất.

## Liên kết tư duy
- [[CONCEPT_STAT_Estimates_of_Variability]]
- [[CONCEPT_STAT_Data_Taxonomy]]

## 4F — Phản tư sư phạm
- **Facts:** Median luôn "thông minh" hơn Mean trong các tập dữ liệu thực tế có nhiều nhiễu.
- **Feelings:** Học sinh thường chỉ nhớ công thức Mean vì nó được dạy sớm nhất, dẫn đến thói quen dùng sai công thức.
- **Findings:** Tính "Robustness" (độ bền vững) là yếu tố sống còn của phân tích dữ liệu chuyên nghiệp.
- **Futures:** Cần dạy học sinh cách đặt câu hỏi "Con số này có bị ảnh hưởng bởi giá trị cực đoan không?" trước khi tin vào bất kỳ báo cáo nào.

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 10-20, Chapter 1) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
