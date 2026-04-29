---
file_id: "WIKI_CONCEPT_DSML_EVALUATION_METRICS"
title: "Đánh giá mô hình (Model Evaluation Metrics)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DSML", "Evaluation"]
source: "`DSML_Data_Analytics_Concepts`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Đánh giá mô hình (Model Evaluation Metrics)

Xây dựng mô hình chỉ là một nửa chặng đường; nửa còn lại là biết mô hình đó hoạt động tốt đến mức nào.

## 核心 (Core Principle)
1. **Dành cho bài toán Phân loại (Classification):** Accuracy, Precision, Recall, F1-Score.
2. **Dành cho bài toán Hồi quy (Regression):** RMSE, MAE, R-Squared.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Tài liệu (trang 15-18) giải thích về **Confusion Matrix** (Ma trận nhầm lẫn). Nó chỉ ra mô hình bị nhầm lẫn giữa các nhãn nào. Việc chỉ dựa vào Accuracy có thể gây sai lầm nếu tập dữ liệu bị mất cân bằng.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng hệ thống báo cháy:
- **Precision thấp:** Chuông reo liên tục nhưng không có cháy (Báo động giả).
- **Recall thấp:** Có cháy thật nhưng chuông không reo (Thảm họa).

## Liên kết tư duy
- [[CONCEPT_DSML_Supervised_vs_Unsupervised]]
- [[CONCEPT_DSML_Overfitting_Prevention]]

## 4F — Phản tư sư phạm
- **Facts:** Không có chỉ số nào là hoàn hảo cho mọi bài toán, cần chọn chỉ số dựa trên chi phí của sai lầm.
- **Feelings:** Người mới thường chỉ quan tâm đến Accuracy (Độ chính xác tổng thể) và dễ bị đánh lừa bởi dữ liệu lệch.
- **Findings:** F1-Score là sự thỏa hiệp tốt nhất khi không biết nên ưu tiên Precision hay Recall.
- **Futures:** Cần xây dựng các bộ dữ liệu "bẫy" (Skewed data) để học sinh tự nhận thấy sự thất bại của chỉ số Accuracy.

---
Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] (Page 15-22) (Xác nhận Rule 14 từ: `DSML_Data_Analytics_Concepts`)
