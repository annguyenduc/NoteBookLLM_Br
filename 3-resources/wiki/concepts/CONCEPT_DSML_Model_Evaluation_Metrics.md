---
file_id: CONCEPT_DSML_MODEL_EVALUATION_METRICS
title: "Model Evaluation Metrics (Chỉ số đánh giá mô hình)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_DSML_Data_Analytics_Concepts]]"
---

## ## For future Claude
Trang này định nghĩa các chỉ số đo lường hiệu năng của mô hình Machine Learning. Việc chọn đúng chỉ số đánh giá (ví dụ: F1-Score thay vì Accuracy cho dữ liệu lệch) là yếu tố quyết định để đánh giá đúng giá trị kinh doanh mà mô hình mang lại, tránh việc đưa ra các quyết định sai lầm dựa trên các con số ảo.

## ## Key Claims / Summary
1.  **Metric Selection**: Chỉ số phải phản ánh đúng mục tiêu của bài toán (ví dụ: tối ưu hóa Recall cho y tế).
2.  **Confusion Matrix**: Nền tảng để hiểu về sai lầm của mô hình (False Positives vs False Negatives).
3.  **Beyond Accuracy**: Độ chính xác tổng thể (Accuracy) thường không đủ để đánh giá mô hình trong thực tế.

## 1. Các chỉ số cốt lõi
1. **Dành cho bài toán Phân loại (Classification):** Accuracy, Precision, Recall, F1-Score.
2. **Dành cho bài toán Hồi quy (Regression):** RMSE, MAE, R-Squared.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Sử dụng **Confusion Matrix** (Ma trận nhầm lẫn) để xem mô hình dự đoán bệnh nhân bị ung thư có bị nhầm sang người khỏe mạnh hay không (False Negative). (Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] Page 15-18).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như hệ thống báo cháy. Precision thấp có nghĩa là chuông reo liên tục nhưng không có cháy (Báo động giả). Recall thấp có nghĩa là có cháy thật nhưng chuông không reo (Thảm họa). Tùy vào mức độ nguy hiểm mà ta ưu tiên Precision hay Recall.

## ## Source Tracing
- **Nguồn**: [[SOURCE_DSML_Data_Analytics_Concepts]] — Page 15-22.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
