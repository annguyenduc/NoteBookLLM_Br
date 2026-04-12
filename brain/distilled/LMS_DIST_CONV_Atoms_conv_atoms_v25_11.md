---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v25_11
  title: CONV_atoms_v25_11
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v25) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Để thêm cột bias vào ma trận đặc trưng `x_train` dưới dạng số thực, có thể sử dụng hàm `np.hstack` hoặc `np.concatenate` để nối một ma trận cột chứa toàn giá trị 1 (`np.ones`) vào sau ma trận gốc.
- **Source:** [vv25 - Section: ASSISTANT response regarding bias column and np.hstack]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm tính Mean Absolute Error (MAE) không dùng thư viện scikit-learn được triển khai bằng NumPy theo công thức: `np.mean(np.abs(y_true - y_pred))`.
- **Source:** [vv25 - Section: ASSISTANT response regarding MAE, MSE functions]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm tính Mean Squared Error (MSE) không dùng thư viện scikit-learn được triển khai bằng NumPy theo công thức: `np.mean((y_true - y_pred) ** 2)` hoặc `np.mean(np.square(y_true - y_pred))`.
- **Source:** [vv25 - Section: ASSISTANT response regarding MAE, MSE functions]
- **Tag:** [vv25]

- **Fact:** [CONV] Trong bài toán Hồi quy tuyến tính (Linear Regression), bộ trọng số $w$ có thể được tính toán bằng phương trình bình phương tối thiểu thông qua hàm `np.linalg.pinv` (giả nghịch đảo) hoặc `np.linalg.inv` (nghịch đảo) theo công thức: $w = (X^T X)^{-1} X^T y$.
- **Source:** [vv25 - Section: ASSISTANT response regarding weight calculation]
- **Tag:** [vv25]

- **Fact:** [CONV] Lỗi `ValueError: matmul` xảy ra khi có sự sai lệch kích thước giữa các ma trận trong phép nhân (ví dụ: ma trận đặc trưng $X$ và vector trọng số $w$ không khớp số chiều core dimension).
- **Source:** [vv25 - Section: USER error log and ASSISTANT explanation]
- **Tag:** [vv25]

- **Fact:** [CONV] "Split data" là quá trình chia tập dữ liệu ban đầu thành các phần: Training Set (huấn luyện mô hình) và Test Set (kiểm tra/đánh giá hiệu suất). Tỷ lệ phân chia phổ biến thường là 70-80% cho huấn luyện và 20-30% cho kiểm tra.
- **Source:** [vv25 - Section: Conversation: Chia tách dữ liệu]
- **Tag:** [vv25]

- **Fact:** [CONV] Một lớp `LinearRegression` tự triển khai tương tự scikit-learn cần có hai phương thức chính: `fit(X, y)` để huấn luyện (tính toán trọng số và bias) và `predict(X)` để dự đoán giá trị đầu ra.
- **Source:** [vv25 - Section: ASSISTANT response regarding custom LinearRegression class]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm `np.column_stack` hoặc `np.c_` là các phương thức thay thế hiệu quả để thêm cột bias (cột giá trị 1) vào ma trận dữ liệu đầu vào.
- **Source:** [vv25 - Section: ASSISTANT response regarding custom LinearRegression class]
- **Tag:** [vv25]

- **Fact:** [CONV] Trong Python, từ khóa `pass` được sử dụng như một trình giữ chỗ (placeholder) trong các hàm hoặc lớp khi chưa có nội dung triển khai cụ thể để tránh lỗi cú pháp.
- **Source:** [vv25 - Section: ASSISTANT response regarding 'pass' keyword]
- **Tag:** [vv25]

- **Fact:** [CONV] Phép toán dự đoán trong mô hình tuyến tính được thực hiện bằng tích vô hướng giữa ma trận đặc trưng $X$ và vector trọng số $w$, cộng với bias $b$: `y_pred = X @ w + b` hoặc `np.dot(X, w) + b`.
- **Source:** [vv25 - Section: ASSISTANT response regarding prediction function]
- **Tag:** [vv25]