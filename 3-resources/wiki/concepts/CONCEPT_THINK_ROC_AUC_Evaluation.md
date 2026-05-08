---
file_id: CONCEPT_THINK_ROC_AUC_Evaluation
title: CONCEPT Đánh giá Mô hình bằng ROC và AUC (ROC/AUC Evaluation)
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Đánh giá Mô hình bằng ROC và AUC (ROC/AUC Evaluation)

## 1. Định nghĩa
- **ROC Curve** (Receiver Operating Characteristic): Đồ thị biểu diễn hiệu suất của mô hình phân loại tại tất cả các ngưỡng (thresholds) khác nhau. Nó vẽ tỷ lệ **True Positive Rate (TPR)** so với **False Positive Rate (FPR)**.
- **AUC** (Area Under the Curve): Diện tích dưới đường cong ROC. AUC cung cấp một giá trị duy nhất (từ 0 đến 1) để tóm tắt hiệu suất của mô hình. AUC càng gần 1, mô hình càng tốt.

## 2. Tại sao quan trọng?
ROC/AUC giúp Analyst đánh giá khả năng phân biệt (Separation power) của mô hình giữa hai lớp (ví dụ: Churn vs No Churn) mà không bị phụ thuộc vào việc chọn một ngưỡng cụ thể nào đó. Điều này rất hữu ích khi tập dữ liệu bị mất cân bằng (Imbalanced data).

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Mô hình phát hiện gian lận thẻ tín dụng.
> **Ứng dụng**: Sử dụng AUC để so sánh hai thuật toán khác nhau. Thuật toán A có AUC = 0.85, thuật toán B có AUC = 0.75. Kết luận: Thuật toán A có khả năng phát hiện gian lận tốt hơn trên mọi ngưỡng lựa chọn.
> **Nguồn**: [[SOURCE_Data_Science_For_Business]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Mô hình dự báo học sinh sẽ trượt kỳ thi cuối kỳ.
> **Ứng dụng**: Nhà trường có thể chọn ngưỡng "an toàn" cao (để không bỏ sót ai) hoặc ngưỡng "chi phí thấp" (chỉ hỗ trợ những em chắc chắn trượt). Đường cong ROC cho thấy sự đánh đổi giữa việc "Bắt đúng học sinh trượt" và "Bắt nhầm học sinh đỗ". AUC cao chứng tỏ mô hình có độ tin cậy tốt để nhà trường đầu tư nguồn lực can thiệp.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_Data_Science_For_Business]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
