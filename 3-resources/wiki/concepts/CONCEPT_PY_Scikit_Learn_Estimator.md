---
file_id: CONCEPT_PY_Scikit_Learn_Estimator
title: CONCEPT Đối tượng Estimator trong Scikit-Learn
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Đối tượng Estimator trong Scikit-Learn

## 1. Định nghĩa
Trong thư viện Scikit-Learn, **Estimator** là một giao diện (Interface) thống nhất cho mọi thuật toán học máy. Bất kể bạn đang dùng Linear Regression hay Random Forest, cách tương tác với mô hình đều tuân theo một bộ quy tắc chung.

## 2. Các phương thức cốt lõi
- **`fit()`**: Huấn luyện mô hình từ dữ liệu. Luôn nhận tham số là `(X, y)` (cho học có giám sát) hoặc chỉ `(X)` (cho học không giám sát).
- **`predict()`**: Dự báo kết quả trên dữ liệu mới sau khi đã `fit`.
- **`score()`**: Đánh giá chất lượng của mô hình (thường là Accuracy hoặc R-squared).

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ lập trình (Original)
```python
from sklearn.linear_model import LinearRegression
# 1. Khởi tạo
model = LinearRegression()
# 2. Huấn luyện
model.fit(X_train, y_train)
# 3. Dự báo
predictions = model.predict(X_test)
```
> **Nguồn**: [[SOURCE_PY_Python_for_Data_Analysis]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Dạy học sinh về quy trình "Học".
> **Tư duy Estimator**:
> 1. **Khởi tạo**: Giống như việc học sinh chuẩn bị sách vở và tâm thế học tập.
> 2. **`fit()`**: Học sinh đọc sách và làm bài tập mẫu để hiểu quy luật (Học từ dữ liệu quá khứ).
> 3. **`predict()`**: Học sinh làm bài kiểm tra mới dựa trên những kiến thức đã học.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_PY_Python_for_Data_Analysis]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
