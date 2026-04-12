Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (Volume v18) về lĩnh vực AI và Machine Learning:

- **Fact:** `DecisionTreeClassifier` từ thư viện `sklearn.tree` được sử dụng để xây dựng các mô hình phân loại trong học máy.
- **Source:** [v18 - Section: Coding It / Mô hình cây quyết định]
- **Tag:** [vv18]

- **Fact:** Hàm `accuracy_score` từ `sklearn.metrics` được dùng để đánh giá độ chính xác của mô hình phân loại.
- **Source:** [v18 - Section: Coding It / Đánh giá độ chính xác]
- **Tag:** [vv18]

- **Fact:** "In-sample" score là chỉ số hiệu suất được tính toán trên cùng một tập dữ liệu mà mô hình đã sử dụng để huấn luyện, điều này có thể dẫn đến đánh giá sai lệch về độ chính xác thực tế.
- **Source:** [v18 - Section: The Problem with "In-Sample" Scores]
- **Tag:** [vv18]

- **Fact:** Mô hình có thể học các mẫu ngẫu nhiên không có ý nghĩa thực tế (ví dụ: màu cửa liên quan đến giá nhà) nếu chỉ đánh giá dựa trên dữ liệu huấn luyện.
- **Source:** [v18 - Section: Door Color Example]
- **Tag:** [vv18]

- **Fact:** Dữ liệu xác thực (validation data) là dữ liệu không được sử dụng trong quá trình xây dựng mô hình, dùng để kiểm tra khả năng dự đoán của mô hình trên dữ liệu mới.
- **Source:** [v18 - Section: The Problem with "In-Sample" Scores]
- **Tag:** [vv18]

- **Fact:** Thư viện `scikit-learn` cung cấp hàm `train_test_split` để chia tập dữ liệu thành hai phần: huấn luyện (training) và xác thực (validation).
- **Source:** [v18 - Section: Coding It / train_test_split]
- **Tag:** [vv18]

- **Fact:** Tham số `random_state` trong hàm chia dữ liệu giúp đảm bảo kết quả phân tách dữ liệu giống nhau ở mỗi lần chạy mã nguồn.
- **Source:** [v18 - Section: Coding It / random_state]
- **Tag:** [vv18]

- **Fact:** `DecisionTreeRegressor` là mô hình cây quyết định được sử dụng cho các bài toán hồi quy (dự đoán giá trị số cụ thể như giá nhà).
- **Source:** [v18 - Section: Coding It / Define model]
- **Tag:** [vv18]

- **Fact:** `mean_absolute_error` (MAE) là thước đo sai số trung bình tuyệt đối giữa giá trị dự đoán và giá trị thực tế.
- **Source:** [v18 - Section: Coding It / mean_absolute_error]
- **Tag:** [vv18]

- **Fact:** Một mô hình có thể có sai số rất thấp trên dữ liệu huấn luyện (ví dụ: 500$) nhưng lại có sai số rất cao trên dữ liệu thực tế (ví dụ: 250,000$), khiến nó không thể sử dụng trong thực tiễn.
- **Source:** [v18 - Section: Result Comparison]
- **Tag:** [vv18]

- **Fact:** Khả năng tổng quát hóa (generalization) là mục tiêu quan trọng nhất để đảm bảo mô hình hoạt động tốt trên dữ liệu mới trong thực tế.
- **Source:** [v18 - Section: Conclusion]
- **Tag:** [vv18]