---
file_id: "WIKI_CONCEPT_STAT_SAMPLING_BIASES"
title: "Các loại sai lệch khi lấy mẫu (Sampling Biases)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Bias"]
source: "[[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]]"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Các loại sai lệch khi lấy mẫu (Sampling Biases)

Dữ liệu chất lượng kém dẫn đến kết quả sai lầm ("Garbage in, Garbage out"). Hiểu về sai lệch giúp chúng ta thiết kế các cuộc khảo sát và lấy mẫu chính xác hơn.

## 核心 (Core Principle)
1. **Selection Bias:** Mẫu không đại diện cho quần thể.
2. **Self-Selection Bias:** Đối tượng tự nguyện tham gia thường có ý kiến cực đoan.
3. **Survivor Bias:** Chỉ tập trung vào những thực thể còn tồn tại.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Dự đoán bầu cử Mỹ năm 1936 sai vì chỉ khảo sát qua điện thoại (lúc đó điện thoại là món đồ xa xỉ, chỉ dành cho tầng lớp giàu có).

### 2. Ứng dụng sư phạm (Pedagogical Application)
Giáo viên hỏi "Bài tập có khó không?" vào lúc 5 giờ sáng. Chỉ những bạn **dậy sớm/chăm chỉ nhất** trả lời -> Kết quả là "Dễ". Đây là Selection Bias.

## Liên kết tư duy
- [[CONCEPT_STAT_Central_Limit_Theorem]]
- [[CONCEPT_STAT_Data_Taxonomy]]

## 4F — Phản tư sư phạm
- **Facts:** Dữ liệu lớn (Big Data) không giúp xóa bỏ sai lệch nếu phương pháp lấy mẫu bị lỗi từ đầu.
- **Feelings:** Nhà phân tích thường có xu hướng "chọn lọc dữ liệu" (Cherry-picking) để ủng hộ giả thuyết của mình mà không hề hay biết.
- **Findings:** Survivor Bias là loại sai lệch khó phát hiện nhất vì những dữ liệu "thất bại" đã biến mất hoàn toàn khỏi hệ thống.
- **Futures:** Cần dạy học sinh cách đặt câu hỏi "Ai là người KHÔNG có mặt trong bộ dữ liệu này?" trước khi đưa ra kết luận.

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 50-55, Chapter 2) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
