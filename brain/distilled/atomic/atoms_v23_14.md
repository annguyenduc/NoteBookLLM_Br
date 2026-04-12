Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** Mô hình Linear Regression (Hồi quy tuyến tính) được sử dụng để dự đoán các giá trị liên tục như điểm số học sinh (S10) dựa trên các đặc trưng đầu vào (features) như 'S-AVG' và 'S6'.
- **Source:** [vv23] - Section: Hàm `phanloai` và lớp `FinalScorePredict`.
- **Tag:** [vv23]

- **Fact:** Ridge Regression là một phương pháp cải thiện độ chính xác của mô hình hồi quy bằng cách thêm tham số `alpha` để giảm hiện tượng quá khớp (overfitting) và tăng tính tổng quát hóa.
- **Source:** [vv23] - Section: Giải thích về cải thiện độ chính xác và ví dụ về `Ridge`.
- **Tag:** [vv23]

- **Fact:** Logistic Regression (Hồi quy Logistic) được áp dụng cho các bài toán phân loại (classification), ví dụ như dự đoán khả năng học sinh đăng ký khóa học (REG-MC4AI: Y/N) dựa trên điểm GPA và dữ liệu điểm số.
- **Source:** [vv23] - Section: Lớp `UpClassPredict`.
- **Tag:** [vv23]

- **Fact:** Việc đánh giá hiệu suất mô hình hồi quy trong AI thường sử dụng chỉ số Mean Squared Error (MSE) và phương thức `.score()` (hệ số xác định R-squared).
- **Source:** [vv23] - Section: Hàm `phanloai` và phần đánh giá mô hình.
- **Tag:** [vv23]

- **Fact:** Thư viện Plotly (sử dụng `go.Scatter3d` và `go.Surface`) cho phép trực quan hóa mặt phẳng hồi quy (Regression Plane) trong không gian 3 chiều để quan sát mối quan hệ giữa hai biến độc lập và một biến phụ thuộc.
- **Source:** [vv23] - Section: Hàm `phanloai` - Phần tạo biểu đồ 3D.
- **Tag:** [vv23]

- **Fact:** Tiền xử lý dữ liệu (Data Preprocessing) bao gồm việc xử lý giá trị thiếu bằng phương thức `.fillna(0)` và kỹ thuật Feature Engineering như tính tổng các cột điểm thành phần để làm đầu vào cho mô hình.
- **Source:** [vv23] - Section: Lớp `FinalScorePredict` và `UpClassPredict`.
- **Tag:** [vv23]

- **Fact:** Hiện tượng Overfitting (Quá khớp) xảy ra khi mô hình học quá chi tiết dữ liệu huấn luyện nhưng không tổng quát hóa tốt cho dữ liệu kiểm tra, dẫn đến kết quả dự đoán không ổn định.
- **Source:** [vv23] - Section: Giải thích về nguyên nhân `model.score` thay đổi và dưới 0.7.
- **Tag:** [vv23]

- **Fact:** Công cụ `train_test_split` từ thư viện `sklearn.model_selection` được sử dụng để chia dữ liệu thành tập huấn luyện (train) và tập kiểm tra (test) theo tỷ lệ xác định (ví dụ: `test_size=0.3`).
- **Source:** [vv23] - Section: Các đoạn mã khởi tạo mô hình và chia dữ liệu.
- **Tag:** [vv23]