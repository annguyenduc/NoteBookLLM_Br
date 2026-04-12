Dưới đây là các sự kiện kỹ thuật về AI và xử lý dữ liệu được trích xuất từ nguồn cung cấp:

- **Fact:** Linear Regression (Hồi quy tuyến tính) được sử dụng để dự đoán các giá trị mục tiêu liên tục, trong khi Logistic Regression (Hồi quy Logistic) được sử dụng cho các bài toán phân loại với nhãn rời rạc hoặc nhị phân.
- **Source:** [vv23] - Đoạn trả lời của ASSISTANT về sự khác biệt giữa Linear và Logistic Regression.
- **Tag:** [vv23]

- **Fact:** Phương thức `model.score()` trong thư viện Scikit-learn mặc định đánh giá hiệu suất của mô hình trên tập dữ liệu kiểm tra (test set) để đo lường khả năng tổng quát hóa trên dữ liệu mới.
- **Source:** [vv23] - Section: ASSISTANT trả lời về "thông thường model.score sẽ đánh giá trên tập nào".
- **Tag:** [vv23]

- **Fact:** Lỗi `ValueError: Classification metrics can't handle a mix of multiclass and continuous targets` xảy ra khi cố gắng sử dụng các thước đo phân loại (như accuracy_score) cho các biến mục tiêu có giá trị liên tục.
- **Source:** [vv23] - Đoạn hội thoại về lỗi ValueError và giải thích của ASSISTANT.
- **Tag:** [vv23]

- **Fact:** Trong quy trình tiền xử lý dữ liệu cho AI, các giá trị thiếu (NaN) thường được xử lý bằng phương thức `.fillna(0)` để tránh lỗi khi thực hiện các phép toán ma trận hoặc huấn luyện mô hình.
- **Source:** [vv23] - Phần giải thích về cách tạo ma trận đầu vào `X` (Cách 2).
- **Tag:** [vv23]

- **Fact:** Để trực quan hóa mặt phẳng hồi quy (regression plane) trong không gian 3D, có thể sử dụng thư viện Plotly với hàm `go.Scatter3d` để vẽ các điểm dữ liệu và `go.Surface` để vẽ mặt phẳng dự đoán dựa trên một lưới tọa độ (meshgrid).
- **Source:** [vv23] - Đoạn mã nguồn Python cung cấp bởi ASSISTANT để vẽ biểu đồ 3D.
- **Tag:** [vv23]

- **Fact:** Hàm `train_test_split` được sử dụng để chia dữ liệu gốc thành tập huấn luyện (training set) và tập kiểm tra (test set) theo tỷ lệ được xác định bởi tham số `test_size`.
- **Source:** [vv23] - Section: ASSISTANT giải thích về quy trình chia dữ liệu.
- **Tag:** [vv23]