Dưới đây là các sự kiện kỹ thuật về AI và Machine Learning được trích xuất từ dữ liệu cung cấp:

- **Fact:** [CONV] Hàm `np.meshgrid()` được sử dụng để tạo lưới tọa độ từ các mảng đầu vào, phục vụ cho việc tính toán hoặc trực quan hóa trong không gian hai chiều.
- **Source:** [vv25 - Đoạn đầu về np.meshgrid]
- **Tag:** [vv25]

- **Fact:** [CONV] Trong Machine Learning, `predict` trả về nhãn lớp dự đoán (label), trong khi `predict_proba` trả về ma trận chứa các giá trị xác suất tương ứng với mỗi lớp.
- **Source:** [vv25 - Section: khác biệt giữa predict và predict_proba]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm `train_test_split` từ thư viện `sklearn.model_selection` được sử dụng để chia tập dữ liệu thành tập huấn luyện (train set) và tập kiểm tra (test set) theo tỉ lệ xác định (ví dụ 80/20).
- **Source:** [vv25 - Section: Split dataset X,y]
- **Tag:** [vv25]

- **Fact:** [CONV] Lỗi `ConvergenceWarning` trong Logistic Regression xảy ra khi thuật toán tối ưu hóa không hội tụ; cách khắc phục bao gồm tăng số lần lặp (`max_iter`), chuẩn hóa dữ liệu (scaling) hoặc thay đổi bộ giải (`solver` như 'liblinear', 'sag', 'saga').
- **Source:** [vv25 - Section: ConvergenceWarning]
- **Tag:** [vv25]

- **Fact:** [CONV] Phương thức `model.score(X_test, y_test)` trong Scikit-learn tính toán trực tiếp độ chính xác (accuracy) của mô hình trên tập dữ liệu kiểm tra mà không cần dự đoán nhãn riêng lẻ.
- **Source:** [vv25 - Section: sử dụng model.score]
- **Tag:** [vv25]

- **Fact:** [CONV] Ma trận nhầm lẫn (Confusion Matrix) là công cụ đánh giá hiệu suất phân loại gồm 4 chỉ số: True Positive (TP), False Positive (FP), True Negative (TN), và False Negative (FN).
- **Source:** [vv25 - Section: cm = confusion_matrix(y, y_pred) là gì]
- **Tag:** [vv25]

- **Fact:** [CONV] Thư viện `seaborn` với hàm `heatmap` thường được sử dụng để trực quan hóa ma trận nhầm lẫn dưới dạng biểu đồ nhiệt.
- **Source:** [vv25 - Section: vẽ Confusion Matrix]
- **Tag:** [vv25]

- **Fact:** [CONV] Trong thực nghiệm phân loại chữ số MNIST (số 3 và số 5), mô hình KNN (n_neighbors=3) đạt độ chính xác (0.987) cao hơn so với mô hình Logistic Regression (0.964).
- **Source:** [vv25 - Section: Dựa vào kết quả train 2 model rút ra được kết luận gì ?]
- **Tag:** [vv25]

- **Fact:** [CONV] Để vẽ biểu đồ phân tán 3D (3D Scatter plot), cần sử dụng `Axes3D` từ `mpl_toolkits.mplot3d` kết hợp với thư viện `matplotlib`.
- **Source:** [vv25 - Section: scatter 3D các sample]
- **Tag:** [vv25]

- **Fact:** [CONV] Các tham số của mô hình Logistic Regression sau khi huấn luyện có thể truy cập qua thuộc tính `coef_` (weights/trọng số) và `intercept_` (bias/sai số).
- **Source:** [vv25 - Section: lấy ra weights & bias]
- **Tag:** [vv25]