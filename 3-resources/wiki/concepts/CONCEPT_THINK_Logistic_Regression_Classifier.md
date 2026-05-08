---
file_id: CONCEPT_THINK_Logistic_Regression_Classifier
title: CONCEPT Mô hình Phân loại Logistic Regression
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Mô hình Phân loại Logistic Regression

## 1. Định nghĩa
Mặc dù có tên là "Regression" (Hồi quy), Logistic Regression thực chất là một thuật toán **Phân loại (Classification)**. Nó được sử dụng để dự báo xác suất của một biến mục tiêu nhị phân (có 2 trạng thái: Đúng/Sai, 0/1, Có/Không).

## 2. Nguyên lý
Thuật toán sử dụng hàm **Sigmoid** để nén kết quả của một phương trình tuyến tính vào khoảng giá trị từ 0 đến 1. 
- Nếu kết quả > 0.5 (hoặc một ngưỡng tùy chọn), chúng ta phân loại là lớp 1.
- Nếu kết quả < 0.5, chúng ta phân loại là lớp 0.

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Dự báo khả năng một khách hàng sẽ nhấp vào quảng cáo (CTR).
> **Ứng dụng**: Mô hình tính toán dựa trên lịch sử duyệt web, độ tuổi, và thiết bị của khách hàng. Kết quả đầu ra là xác suất (ví dụ: 0.15). Vì 0.15 < 0.5, hệ thống quyết định không hiển thị quảng cáo đó cho người dùng này để tiết kiệm chi phí.
> **Nguồn**: [[SOURCE_Data_Science_For_Business]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Dự báo học sinh có hoàn thành bài tập về nhà hay không.
> **Ứng dụng**: Các biến số đầu vào gồm: (1) Số giờ học trên lớp, (2) Điểm số bài trước, (3) Số lượng bài tập chưa hoàn thành trong quá khứ. Mô hình cho ra xác suất 0.85. Giáo viên có thể yên tâm rằng học sinh này rất có khả năng sẽ nộp bài đúng hạn.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_Data_Science_For_Business]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
