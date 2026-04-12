---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v25_3
  title: atoms_v25_3
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật về AI và Machine Learning được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** Hàm `np.meshgrid()` được sử dụng để tạo lưới tọa độ từ các mảng đầu vào, phục vụ cho việc tính toán hoặc trực quan hóa trong không gian hai chiều.
- **Source:** [vv25] - Section: np.meshgrid()
- **Tag:** [vv25]

- **Fact:** Trong Machine Learning, `predict` trả về nhãn lớp dự đoán (label), trong khi `predict_proba` trả về giá trị xác suất của điểm dữ liệu thuộc về mỗi lớp.
- **Source:** [vv25] - Section: khác biệt giữa predict và predict_proba
- **Tag:** [vv25]

- **Fact:** Dữ liệu hình ảnh MNIST (pixel từ 0-255) thường được chuẩn hóa bằng cách chia cho 255 để đưa về khoảng giá trị [0, 1] trước khi huấn luyện.
- **Source:** [vv25] - Section: import numpy as np from sklearn.datasets import fetch_openml
- **Tag:** [vv25]

- **Fact:** Hàm `train_test_split` từ thư viện `sklearn.model_selection` cho phép chia bộ dữ liệu thành tập huấn luyện (train set) và tập kiểm tra (test set) theo tỉ lệ tùy chỉnh (ví dụ 80/20) và hỗ trợ `random_state` để cố định kết quả chia.
- **Source:** [vv25] - Section: Hãy Split dataset X,y thành trainset, testset theo tỉ lệ 80%-20%
- **Tag:** [vv25]

- **Fact:** Cảnh báo `ConvergenceWarning` trong Logistic Regression xuất hiện khi thuật toán tối ưu (như lbfgs) đạt giới hạn số lần lặp (`max_iter`) mà chưa hội tụ.
- **Source:** [vv25] - Section: Accuracy on test set: 0.959866220735786 / ConvergenceWarning
- **Tag:** [vv25]

- **Fact:** Để khắc phục lỗi không hội tụ trong Logistic Regression, có thể tăng `max_iter`, chuẩn hóa dữ liệu (Scaling) hoặc thay đổi thuật toán giải (solver) như 'liblinear', 'sag', hoặc 'saga'.
- **Source:** [vv25] - Section: Kết quả độ chính xác trên tập kiểm tra là 0.959866220735786... (Phần giải quyết ConvergenceWarning)
- **Tag:** [vv25]

- **Fact:** Ma trận nhầm lẫn (Confusion Matrix) là bảng hai chiều dùng đánh giá mô hình phân loại, gồm 4 thành phần: True Positive (TP), False Positive (FP), True Negative (TN), và False Negative (FN).
- **Source:** [vv25] - Section: cm = confusion_matrix(y, y_pred) là gì
- **Tag:** [vv25]

- **Fact:** Phương thức `model.score(X_test, y_test)` trong Scikit-learn tính toán trực tiếp độ chính xác (accuracy) của mô hình trên tập dữ liệu mà không cần thực hiện bước `predict` riêng biệt.
- **Source:** [vv25] - Section: sử dụng model.score
- **Tag:** [vv25]

- **Fact:** Trong bài toán phân loại chữ số MNIST (số 3 và 5), mô hình KNN (K-Nearest Neighbors) với `n_neighbors=3` có thể đạt độ chính xác cao hơn (khoảng 98.7%) so với mô hình Logistic Regression (khoảng 96.4%).
- **Source:** [vv25] - Section: Dựa vào kết quả train 2 model rút ra được kết luận gì ?
- **Tag:** [vv25]

- **Fact:** Trọng số (weights) và sai số chệch (bias) của mô hình Logistic Regression sau khi huấn luyện có thể được truy xuất lần lượt qua các thuộc tính `.coef_` và `.intercept_`.
- **Source:** [vv25] - Section: lấy ra weights & bias
- **Tag:** [vv25]

- **Fact:** Thư viện `mpl_toolkits.mplot3d` kết hợp với `matplotlib` cho phép vẽ biểu đồ phân tán 3D (scatter 3D) để trực quan hóa dữ liệu đa chiều.
- **Source:** [vv25] - Section: Dùng filter lấy ra dataframe... scatter 3D
- **Tag:** [vv25]