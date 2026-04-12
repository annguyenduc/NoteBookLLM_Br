Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp:

- **Fact:** [CONV] Linear Regression (Hồi quy tuyến tính) được sử dụng để xây dựng mô hình dự đoán điểm số (S10) dựa trên các biến đầu vào như điểm trung bình (S-AVG) và điểm thành phần (S6).
- **Source:** [vv23] - Section: Function phanloai.
- **Tag:** [vv23]

- **Fact:** [CONV] Logistic Regression được áp dụng cho các bài toán dự đoán phân loại nhị phân, ví dụ như dự đoán một học sinh có đăng ký khóa học MC4AI (Y/N) dựa trên GPA và dữ liệu điểm số.
- **Source:** [vv23] - Section: Class UpClassPredict.
- **Tag:** [vv23]

- **Fact:** [CONV] Ridge Regression và Lasso là các kỹ thuật hồi quy giúp cải thiện độ chính xác của mô hình bằng cách giảm hiện tượng overfitting (quá khớp) và tăng tính tổng quát hóa.
- **Source:** [vv23] - Section: ASSISTANT response về việc tăng độ chính xác mô hình.
- **Tag:** [vv23]

- **Fact:** [CONV] Hiệu suất của mô hình hồi quy được đánh giá thông qua các chỉ số như Mean Squared Error (MSE) và hệ số xác định R-squared (thông qua hàm `.score()`).
- **Source:** [vv23] - Section: Function phanloai - Đánh giá mô hình.
- **Tag:** [vv23]

- **Fact:** [CONV] Việc chia dữ liệu thành tập huấn luyện (train) và tập kiểm tra (test) bằng hàm `train_test_split` là quy trình chuẩn để kiểm tra khả năng dự báo của mô hình trên dữ liệu mới.
- **Source:** [vv23] - Section: Function phanloai.
- **Tag:** [vv23]

- **Fact:** [CONV] Thư viện Plotly (graph_objects) cho phép trực quan hóa mô hình hồi quy trong không gian 3 chiều bằng cách kết hợp biểu đồ điểm (Scatter3d) và mặt phẳng hồi quy (Surface).
- **Source:** [vv23] - Section: Function phanloai - Tạo biểu đồ 3D.
- **Tag:** [vv23]

- **Fact:** [CONV] Trong Ridge Regression, tham số `alpha` được sử dụng để điều chỉnh cường độ chính quy hóa (regularization), giúp kiểm soát độ phức tạp và tránh việc mô hình học quá chi tiết nhiễu từ tập huấn luyện.
- **Source:** [vv23] - Section: Ví dụ về Ridge Regression.
- **Tag:** [vv23]

- **Fact:** [CONV] Kết quả mô hình không ổn định (score thay đổi sau mỗi lần chạy) có thể do kích thước tập dữ liệu nhỏ hoặc sự phân bổ ngẫu nhiên của dữ liệu giữa tập train và test.
- **Source:** [vv23] - Section: Giải thích về việc model.score thay đổi.
- **Tag:** [vv23]

- **Fact:** [CONV] Tiền xử lý dữ liệu trong AI bao gồm việc xử lý giá trị rỗng (NaN) bằng phương pháp điền giá trị (fillna) và định hình lại mảng (reshape) để phù hợp với yêu cầu đầu vào của thư viện Scikit-learn.
- **Source:** [vv23] - Section: Class FinalScorePredict và GPAPredict.
- **Tag:** [vv23]

- **Fact:** [CONV] Streamlit hỗ trợ tạo giao diện tương tác cho các ứng dụng AI, cho phép người dùng thay đổi tham số mô hình (như tỷ lệ test_size) thông qua các widget như `number_input`.
- **Source:** [vv23] - Section: Function phanloai - Streamlit integration.
- **Tag:** [vv23]