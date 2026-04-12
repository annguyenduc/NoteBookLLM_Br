Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v25) về AI và Machine Learning:

- **Fact:** Trong mô hình Logistic Regression của thư viện sklearn, thuộc tính `model.coef_` trả về ma trận trọng số (weights) của các đặc trưng và `model.intercept_` trả về giá trị bias của mô hình.
- **Source:** [v25 - Section: Lấy weights và bias từ mô hình]
- **Tag:** [vv25]

- **Fact:** Đối với bài toán phân loại có 3 đặc trưng, đường biên quyết định (decision boundary) là một mặt phẳng được xác định bởi phương trình: $w_1x_1 + w_2x_2 + w_3x_3 + bias = 0$.
- **Source:** [v25 - Section: Vẽ decision boundary]
- **Tag:** [vv25]

- **Fact:** Hàm `predict_proba(X)` trả về ma trận xác suất dự đoán cho tất cả các lớp của mẫu dữ liệu, trong đó `predict_proba(X)[:, 1]` là mảng chứa xác suất dự đoán riêng cho lớp positive (thường là lớp có chỉ số 1).
- **Source:** [v25 - Section: scores = model.predict_proba(X)[:, 1] và y_pred_prob = model.predict_proba(X)]
- **Tag:** [vv25]

- **Fact:** Ma trận nhầm lẫn (Confusion Matrix) cho bài toán phân loại nhị phân là một ma trận 2x2 thể hiện số lượng các điểm dữ liệu được dự đoán đúng và sai cho từng lớp (ví dụ: versicolor và virginica).
- **Source:** [v25 - Section: Giải thích output Confusion Matrix]
- **Tag:** [vv25]

- **Fact:** Kỹ thuật thresholding cho phép tìm ngưỡng xác suất tối ưu (thay vì mặc định 0.5) để phân loại nhãn, nhằm đạt được mục tiêu không có sai số dự đoán cho một trong hai lớp (FP = 0 hoặc FN = 0).
- **Source:** [v25 - Section: Dùng kỹ thuật thresholding chọn ra threshold]
- **Tag:** [vv25]

- **Fact:** Trong bài toán phân loại tập dữ liệu Iris cụ thể này, nhãn lớp 2 tương ứng với loài "versicolor" và nhãn lớp 3 tương ứng với loài "virginica".
- **Source:** [v25 - Section: lớp 3 và lớp 2 tương ứng với gì]
- **Tag:** [vv25]

- **Fact:** Thư viện Plotly có thể được sử dụng để trực quan hóa 3D với `go.Surface` để vẽ mặt phẳng biên quyết định và `go.Scatter3d` để vẽ các điểm dữ liệu mẫu theo các đặc trưng như sepal_width, sepal_length, và petal_width.
- **Source:** [v25 - Section: Vẽ decision boundary bằng plotly]
- **Tag:** [vv25]

- **Fact:** Để tìm threshold tối ưu bằng lập trình, có thể sử dụng vòng lặp qua một dải giá trị (ví dụ: `np.linspace(0, 1, 100)`) và kiểm tra các giá trị FP, FN từ `confusion_matrix` cho đến khi đạt điều kiện mong muốn.
- **Source:** [v25 - Section: Code tìm threshold tối ưu]
- **Tag:** [vv25]