Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu RAW (Volume v25) về AI và Machine Learning:

- **Fact:** [CONV] Trong mô hình Logistic Regression của thư viện sklearn, `model.coef_` trả về ma trận trọng số (weights) của các đặc trưng và `model.intercept_` trả về giá trị bias của mô hình.
- **Source:** [Đoạn mã đầu tiên và phần giải thích của ASSISTANT]
- **Tag:** [vv25]

- **Fact:** [CONV] Đối với bài toán phân loại nhị phân, `model.coef_[0]` là một mảng một chiều chứa các trọng số đại diện cho độ ảnh hưởng của từng đặc trưng đối với lớp đầu tiên (lớp 0).
- **Source:** [Phần giải thích "weights = model.coef_[0] là gì"]
- **Tag:** [vv25]

- **Fact:** [CONV] Trong bài toán có 3 đặc trưng ($x_1, x_2, x_3$), đường biên quyết định (decision boundary) là một mặt phẳng được xác định bởi phương trình: $w_1x_1 + w_2x_2 + w_3x_3 + bias = 0$.
- **Source:** [Phần USER: # YOUR CODE HERE: Vẽ decision boundary]
- **Tag:** [vv25]

- **Fact:** [CONV] Để trực quan hóa biên quyết định 3D, có thể sử dụng thư viện `matplotlib` với `plot_surface` hoặc thư viện `plotly` với `go.Surface`.
- **Source:** [Các đoạn mã Python trong phần hướng dẫn vẽ decision boundary]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm `predict_proba(X)` trả về ma trận xác suất dự đoán cho tất cả các lớp, trong đó cột thứ hai (index 1) thường đại diện cho xác suất của lớp positive.
- **Source:** [Phần giải thích sự khác biệt giữa scores và y_pred_prob]
- **Tag:** [vv25]

- **Fact:** [CONV] Ma trận nhầm lẫn (Confusion Matrix) cung cấp chi tiết về số lượng mẫu dự đoán đúng và sai cho từng lớp, giúp đánh giá hiệu suất mô hình (ví dụ: số lượng mẫu thực tế là 'versicolor' nhưng bị dự đoán sai là 'virginica').
- **Source:** [Phần giải thích output Confusion Matrix [[48 2] [4 46]]]
- **Tag:** [vv25]

- **Fact:** [CONV] Kỹ thuật thresholding (điều chỉnh ngưỡng) có thể được sử dụng để tìm ra ngưỡng xác suất tối ưu nhằm triệt tiêu hoàn toàn sai số False Positive (FP = 0) hoặc False Negative (FN = 0).
- **Source:** [Phần giải thích và code tìm threshold tối ưu]
- **Tag:** [vv25]

- **Fact:** [CONV] Trong tập dữ liệu Iris được lọc để phân loại, nhãn lớp 2 tương ứng với loài "versicolor" và nhãn lớp 3 tương ứng với loài "virginica".
- **Source:** [Phần giải thích lớp 3 và lớp 2 tương ứng với gì]
- **Tag:** [vv25]

- **Fact:** [CONV] Công thức để tính toán tọa độ điểm trên mặt phẳng biên quyết định 3D từ hai trục $x_1, x_2$ là: $x_3 = (-w_1x_1 - w_2x_2 - bias) / w_3$.
- **Source:** [Đoạn mã trong hàm visualize_decision_boundary]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm `classification_report` từ `sklearn.metrics` được sử dụng để hiển thị các chỉ số đo lường mô hình bao gồm precision, recall và f1-score dựa trên một ngưỡng (threshold) cụ thể.
- **Source:** [Phần USER: # YOUR CODE HERE from sklearn.metrics import classification_report]
- **Tag:** [vv25]