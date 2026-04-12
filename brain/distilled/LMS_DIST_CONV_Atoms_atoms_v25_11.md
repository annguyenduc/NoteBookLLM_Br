---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v25_11
  title: atoms_v25_11
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v25):

- **Fact:** Để thêm cột bias là các giá trị số thực (float) vào sau ma trận đặc trưng `x_train`, có thể sử dụng hàm `np.hstack` hoặc `np.concatenate` với `axis=1`.
- **Source:** [vv25] - Section: Assistant's response to "cột bias phải là số thực" & "sửa lại dung concentrate".
- **Tag:** [vv25]

- **Fact:** Công thức tính Mean Absolute Error (MAE) bằng thư viện NumPy là `np.mean(np.abs(y_true - y_pred))`.
- **Source:** [vv25] - Section: Assistant's response to "Viết 2 hàm tính MAE, MSE như thư viện scikit-learn".
- **Tag:** [vv25]

- **Fact:** Công thức tính Mean Squared Error (MSE) bằng thư viện NumPy là `np.mean((y_true - y_pred) ** 2)` hoặc `np.mean(np.square(y_true - y_pred))`.
- **Source:** [vv25] - Section: Assistant's response to "Viết 2 hàm tính MAE, MSE như thư viện scikit-learn".
- **Tag:** [vv25]

- **Fact:** Trong bài toán Linear Regression, bộ trọng số `w` có thể được tính toán bằng phương trình bình phương tối thiểu (Normal Equation) thông qua hàm nghịch đảo giả `np.linalg.pinv(X.T @ X) @ X.T @ y`.
- **Source:** [vv25] - Section: User's code snippet & Assistant's response to "Nếu không sử dụng thư viện skitlearn thì làm thế nào".
- **Tag:** [vv25]

- **Fact:** Hàm dự đoán (predict) trong Linear Regression thực hiện phép nhân ma trận giữa ma trận đặc trưng `X` (đã thêm bias) và vector trọng số `w`: `y_pred = X @ w` hoặc `np.dot(X, w)`.
- **Source:** [vv25] - Section: Assistant's response to "viết hàm prediction với yêu cầu như trên".
- **Tag:** [vv25]

- **Fact:** "Split data" là quá trình chia tập dữ liệu ban đầu thành các phần khác nhau, phổ biến nhất là Training Set (để huấn luyện mô hình) và Test Set (để đánh giá hiệu suất khách quan trên dữ liệu mới).
- **Source:** [vv25] - Section: Assistant's response to "Split data là gì, ví dụ chi tiết đơn giản".
- **Tag:** [vv25]

- **Fact:** Tỷ lệ phân chia dữ liệu phổ biến trong học máy thường là 70-80% cho tập huấn luyện (training) và 20-30% cho tập kiểm tra (test).
- **Source:** [vv25] - Section: Assistant's response to "Split data là gì, ví dụ chi tiết đơn giản".
- **Tag:** [vv25]

- **Fact:** Lỗi `ValueError: matmul: Input operand 1 has a mismatch in its core dimension` xảy ra khi kích thước các ma trận trong phép nhân không khớp nhau; ví dụ: số cột của ma trận `X` không bằng số hàng của vector trọng số `w`.
- **Source:** [vv25] - Section: Assistant's response to "ValueError Traceback".
- **Tag:** [vv25]

- **Fact:** Cấu trúc một class `LinearRegression` tự viết mô phỏng scikit-learn cần có ít nhất hai phương thức: `fit(X, y)` để tìm trọng số và `predict(X)` để tính toán giá trị dự báo.
- **Source:** [vv25] - Section: Assistant's response to "Tự viết class LinearRegression tương tự như class của thư viện scikit-klearn".
- **Tag:** [vv25]

- **Fact:** Trong Python, từ khóa `pass` được sử dụng như một trình giữ chỗ (placeholder) khi một hàm hoặc lớp được định nghĩa nhưng chưa có nội dung thực thi, nhằm tránh lỗi cú pháp.
- **Source:** [vv25] - Section: Assistant's response to "def predict(self, x): pass nghĩa là gì".
- **Tag:** [vv25]