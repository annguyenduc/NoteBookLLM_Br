---
file_id: CONCEPT_THINK_Ensemble_Methods
title: CONCEPT Các phương pháp Kết hợp Mô hình (Ensemble Methods)
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Các phương pháp Kết hợp Mô hình (Ensemble Methods)

## 1. Định nghĩa
Ensemble Methods là kỹ thuật kết hợp dự báo từ nhiều mô hình khác nhau để tạo ra một mô hình tổng hợp có độ chính xác cao hơn và ổn định hơn bất kỳ mô hình đơn lẻ nào. Triết lý là "Trí tuệ tập thể" (The wisdom of the crowd).

## 2. Các kỹ thuật phổ biến
- **Bagging (Bootstrap Aggregating)**: Huấn luyện nhiều mô hình song song trên các tập con dữ liệu khác nhau (ví dụ: Random Forest).
- **Boosting**: Huấn luyện các mô hình nối tiếp nhau, mô hình sau tập trung sửa lỗi cho mô hình trước (ví dụ: XGBoost, Gradient Boosting).
- **Stacking**: Sử dụng một mô hình "Meta" để tổng hợp kết quả từ các mô hình cơ sở khác nhau.

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Dự báo thị trường chứng khoán.
> **Ứng dụng**: Thay vì tin vào một thuật toán duy nhất, nhà đầu tư kết hợp kết quả từ 10 mô hình khác nhau. Mặc dù từng mô hình có thể sai, nhưng giá trị trung bình hoặc kết quả theo số đông (Voting) thường bám sát diễn biến thực tế hơn.
> **Nguồn**: [[SOURCE_Data_Science_For_Business]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Đánh giá năng lực của một giáo viên.
> **Ứng dụng**: Thay vì chỉ dựa vào điểm số của học sinh (mô hình 1), nhà trường kết hợp thêm: (2) Kết quả dự giờ của đồng nghiệp, (3) Khảo sát mức độ hài lòng của phụ huynh, (4) Đánh giá từ hội đồng chuyên môn. Việc kết hợp nhiều "nguồn đánh giá" (Ensemble) giúp đưa ra kết luận công bằng và chính xác hơn về năng lực thực tế của giáo viên.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_Data_Science_For_Business]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
