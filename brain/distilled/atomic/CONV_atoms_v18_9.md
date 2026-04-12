Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v18 liên quan đến AI và Machine Learning:

- **Fact:** [CONV] `DecisionTreeClassifier` từ thư viện `sklearn.tree` được sử dụng để xây dựng mô hình phân loại, trong khi `accuracy_score` từ `sklearn.metrics` dùng để đánh giá độ chính xác.
- **Source:** [vv18] - Section: DỮ LIỆU RAW (đoạn mã Python đầu tiên).
- **Tag:** [vv18]

- **Fact:** [CONV] "In-sample" score là chỉ số hiệu suất được tính toán trên cùng một mẫu dữ liệu đã dùng để huấn luyện mô hình, điều này dễ dẫn đến việc đánh giá sai lệch về độ chính xác thực tế.
- **Source:** [vv18] - Section: The Problem with "In-Sample" Scores.
- **Tag:** [vv18]

- **Fact:** [CONV] Mô hình có thể học các mẫu ngẫu nhiên (noise) trong dữ liệu huấn luyện (ví dụ: màu cửa liên quan đến giá nhà) mà không phản ánh đúng thực tế, dẫn đến việc dự đoán sai trên dữ liệu mới.
- **Source:** [vv18] - Section: The Problem with "In-Sample" Scores (Ví dụ Door Color).
- **Tag:** [vv18]

- **Fact:** [CONV] Dữ liệu xác thực (validation data) là phần dữ liệu được tách ra và không sử dụng trong quá trình xây dựng mô hình để kiểm tra khả năng dự đoán của mô hình trên dữ liệu chưa từng thấy.
- **Source:** [vv18] - Section: The Problem with "In-Sample" Scores.
- **Tag:** [vv18]

- **Fact:** [CONV] Hàm `train_test_split` trong thư viện `scikit-learn` được sử dụng để chia dữ liệu thành hai phần: tập huấn luyện (training data) và tập xác thực (validation data).
- **Source:** [vv18] - Section: Coding It.
- **Tag:** [vv18]

- **Fact:** [CONV] Tham số `random_state` trong hàm chia dữ liệu đảm bảo kết quả chia dữ liệu là nhất quán (giống nhau) trong mỗi lần chạy mã nguồn.
- **Source:** [vv18] - Section: Coding It (Phần chú thích trong code).
- **Tag:** [vv18]

- **Fact:** [CONV] Sai số trung bình tuyệt đối (MAE) có thể chênh lệch cực lớn giữa dữ liệu trong mẫu (ví dụ 500 USD) và dữ liệu ngoài mẫu (ví dụ hơn 250.000 USD), cho thấy mô hình bị quá khớp (overfitting) và không thể sử dụng thực tế.
- **Source:** [vv18] - Section: Coding It (Phần kết quả Wow!).
- **Tag:** [vv18]

- **Fact:** [CONV] Các phương pháp để cải thiện mô hình bao gồm việc thử nghiệm tìm kiếm các đặc trưng (features) tốt hơn hoặc thay đổi các loại mô hình khác nhau.
- **Source:** [vv18] - Section: Coding It (Đoạn cuối).
- **Tag:** [vv18]