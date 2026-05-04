---
file_id: CONCEPT_DSML_BIAS_VARIANCE_TRADEOFF
title: "Bias-Variance Tradeoff (Sự đánh đổi Bias-Variance)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_STAT_Intro_to_Statistical_Learning]]"
---

## ## For future Claude
Trang này giải thích về Bias-Variance Tradeoff - khái niệm nền tảng trong Machine Learning để hiểu về sự đánh đổi giữa tính đơn giản và tính phức tạp của mô hình. Việc nắm vững khái niệm này giúp lập trình viên điều chỉnh mô hình để tránh hiện tượng Underfitting và Overfitting, từ đó tối ưu hóa khả năng tổng quát hóa trên dữ liệu mới.

## ## Key Claims / Summary
1.  **Bias (Độ chệch)**: Sai số do giả định đơn giản hóa quá mức (Underfitting).
2.  **Variance (Phương sai)**: Sai số do quá nhạy cảm với biến động nhỏ trong dữ liệu huấn luyện (Overfitting).
3.  **The Tradeoff**: Tổng sai số (Total Error) đạt cực tiểu tại điểm cân bằng giữa Bias và Variance.

## 1. Định nghĩa
Sự cân bằng giữa sai số do các giả định đơn giản hóa (Bias) và sai số do sự nhạy cảm quá mức với biến động của dữ liệu huấn luyện (Variance).

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Trong mô hình hồi quy đa thức, bậc của đa thức càng cao thì Bias càng thấp nhưng Variance càng cao (Overfitting). Để cân bằng, ta thường dùng Regularization (L1/L2) để giảm bớt Variance. (Nguồn: [[SOURCE_STAT_Intro_to_Statistical_Learning]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc học thi. Nếu bạn chỉ học vẹt 10 câu hỏi trong đề cương (High Variance), bạn sẽ thất bại nếu đề thi thật có câu thứ 11 khác đi một chút. Nếu bạn không học gì và chỉ đoán mò (High Bias), bạn sẽ thất bại trong mọi câu hỏi. Bạn cần hiểu bản chất để có thể trả lời được các biến thể khác nhau của vấn đề.

## ## Source Tracing
- **Nguồn**: [[SOURCE_STAT_Intro_to_Statistical_Learning]] — Chapter 2.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
