---
file_id: CONCEPT_THINK_Naive_Bayes_Logic
title: CONCEPT Thuật toán Naive Bayes
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Thuật toán Naive Bayes

## 1. Định nghĩa
Naive Bayes là một nhóm các thuật toán phân loại dựa trên **Định lý Bayes**. Nó được gọi là "Naive" (Ngây thơ) vì nó giả định rằng các đặc trưng (features) của dữ liệu là hoàn toàn độc lập với nhau, mặc dù trong thực tế chúng thường có liên quan.

## 2. Nguyên lý
Thuật toán tính toán xác suất hậu nghiệm (Posterior Probability) của một lớp dựa trên các bằng chứng quan sát được. Nó cực kỳ hiệu quả cho việc phân loại văn bản và xử lý các tập dữ liệu có số lượng chiều (features) lớn.

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Phân loại email là Spam hay Ham (không phải spam).
> **Ứng dụng**: Nếu email chứa từ "Viagra" và "Million dollars", Naive Bayes tính xác suất email đó là Spam dựa trên tần suất xuất hiện của các từ này trong các email spam đã biết. Dù hai từ này có thể đi cùng nhau (không độc lập), thuật toán vẫn cho kết quả phân loại rất tốt.
> **Nguồn**: [[SOURCE_Data_Science_For_Business]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Tự động phân loại câu hỏi của học sinh vào các môn học (Toán, Lý, Hóa).
> **Ứng dụng**: Nếu câu hỏi chứa từ "đạo hàm" và "tích phân", thuật toán tính xác suất và kết luận đây là câu hỏi môn Toán. Tính đơn giản của Naive Bayes giúp hệ thống phản hồi cực nhanh ngay khi học sinh vừa gõ xong câu hỏi.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_Data_Science_For_Business]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
