---
file_id: CONCEPT_PY_Scikit_Learn_Estimator
title: Quy trình Scikit-Learn Estimator API
category: CONCEPT
domain: [[ENTITY_Python|Python]]
status: verified
---

# Scikit-Learn: Estimator API

Sức mạnh của Scikit-Learn nằm ở tính nhất quán. Hầu như mọi thuật toán máy học (Machine Learning) đều tuân theo một giao diện duy nhất gọi là **Estimator API**.

## Quy trình 5 bước tiêu chuẩn
1.  **Chọn mô hình:** Import class mô hình tương ứng (ví dụ: `from sklearn.linear_model import LinearRegression`).
2.  **Chọn siêu tham số (Hyperparameters):** Khởi tạo mô hình với các tham số mong muốn (ví dụ: `model = LinearRegression(fit_intercept=True)`).
3.  **Sắp xếp dữ liệu:** Chuẩn bị ma trận tính năng (Features matrix `X`) và vector mục tiêu (Target vector `y`).
4.  **Huấn luyện (Fit):** Gọi phương thức `model.fit(X, y)` để mô hình học từ dữ liệu.
5.  **Dự đoán (Predict):** Áp dụng mô hình cho dữ liệu mới bằng `model.predict(X_new)`.

## Ý nghĩa
Thiết kế này cho phép người dùng dễ dàng thử nghiệm nhiều thuật toán khác nhau (ví dụ: đổi từ Linear Regression sang Random Forest) chỉ bằng cách thay đổi dòng khai báo mô hình, mà không cần sửa lại toàn bộ quy trình xử lý.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Dự đoán giá nhà dựa trên diện tích (Supervised Learning - Hồi quy).*
- **Cách giải quyết:** Áp dụng Estimator API 5 bước tiêu chuẩn. Chọn mô hình Linear Regression, khởi tạo với tham số mong muốn, sau đó dùng `.fit(X, y)` để học và `.predict()` để dự báo giá.
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Chuẩn bị dữ liệu (X phải là ma trận 2D)
X = np.array([[50], [60], [70], [80], [90]])
y = np.array([1.5, 1.8, 2.1, 2.4, 2.7])

# 2. Khởi tạo mô hình & 3. Huấn luyện
model = LinearRegression(fit_intercept=True)
model.fit(X, y)

# 4. Dự đoán dữ liệu mới
X_new = np.array([ [100] ])
print(model.predict(X_new)) # Output: [3.]
```

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Phân nhóm học sinh tự động để thiết kế bài giảng phù hợp (Unsupervised Learning).*
- **Cách giải quyết:** Giáo viên muốn chia lớp thành 3 nhóm năng lực dựa trên điểm Toán và thời gian hoàn thành bài tập. Sử dụng K-Means Clustering, giáo viên đổi class `LinearRegression` thành `KMeans`, nhưng quy trình API `.fit()` vẫn không thay đổi, thể hiện tính nhất quán của thư viện.
```python
from sklearn.cluster import KMeans
import numpy as np

# Dữ liệu học sinh: [Điểm Toán, Thời gian làm bài (phút)]
X_hoc_sinh = np.array([[9.5, 30], [9.0, 35], [5.0, 60], [4.5, 55], [7.0, 45]])

# Thay đổi thuật toán chỉ bằng cách import class khác
model = KMeans(n_clusters=3, random_state=42)

# Phân nhóm bằng hàm fit_predict
nhom_nang_luc = model.fit_predict(X_hoc_sinh)
print(nhom_nang_luc)
```

---
 Nguồn: [[SOURCE_DS_Python_Data_Science_Handbook]] — Chapter 5
[AUDITOR] Rule 14: Đã xác nhận quy trình 5 bước trong Estimator API. Ví dụ chứng minh tính nhất quán giữa Supervised và Unsupervised Learning.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
