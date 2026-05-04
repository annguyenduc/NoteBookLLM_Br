---
file_id: "WIKI_CONCEPT_STAT_LINEAR_REGRESSION"
title: "Hồi quy tuyến tính (Linear Regression)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Regression"]
source: "[[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]]"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Hồi quy tuyến tính (Linear Regression)

Hồi quy tuyến tính là phương pháp thống kê để mô tả mối quan hệ giữa một biến phụ thuộc (Target) và một hoặc nhiều biến độc lập (Predictors).

## 核心 (Core Principle)
1. **Phương trình:** $Y = b_0 + b_1X + e$.
2. **Hệ số ($b_1$):** Thể hiện sự thay đổi của $Y$ khi $X$ tăng 1 đơn vị.
3. **Mục tiêu:** Tìm đường thẳng sao cho tổng bình phương các sai số (Residuals) là nhỏ nhất.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Chương 4 mô tả việc dự báo giá nhà dựa trên diện tích. Hệ số hồi quy cho biết mỗi mét vuông tăng thêm sẽ làm giá nhà tăng bao nhiêu USD. Đây là cơ sở cho các mô hình định giá bất động sản tự động.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Giả sử học sinh theo dõi "Số giờ chơi game" (X) và "Điểm thi" (Y):
- Mô hình trả về hệ số âm (ví dụ: -0.2). Nghĩa là cứ chơi thêm 1 giờ mỗi ngày, điểm thi dự kiến giảm 0.2 điểm.
Điều này giúp học sinh hiểu về mối quan hệ nghịch biến một cách định lượng thay vì chỉ nói chung chung.

## Liên kết tư duy
- [[CONCEPT_STAT_Probability_Distributions]]
- [[CONCEPT_DSML_Supervised_vs_Unsupervised]]

## 4F — Phản tư sư phạm
- **Facts:** Hồi quy tuyến tính chỉ đo lường mối quan hệ tuyến tính, không xử lý được các mối quan hệ phức tạp hơn (phi tuyến).
- **Feelings:** Việc nhìn thấy các điểm dữ liệu thô biến thành một đường thẳng "dự báo" thường tạo ra cảm giác quyền năng cho người học.
- **Findings:** Phải luôn kiểm tra các giả định của hồi quy (như tính độc lập của sai số) trước khi tin vào mô hình.
- **Futures:** Cần dạy học sinh phân biệt giữa "Dự báo" (Prediction) và "Suy luận nhân quả" (Causal inference).

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 141-155, Chapter 4) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
