Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu Volume v24 liên quan đến AI và xử lý dữ liệu:

- **Fact:** Thuật toán K-means (AI) được sử dụng để phân loại học sinh thành các nhóm dựa trên các đặc trưng điểm số như S6, S10 và điểm trung bình S-AVG.
- **Source:** [vv24] - Section: Dùng KMeans để phân nhóm các học sinh thành 3 nhóm theo tập X tạo ra.
- **Tag:** [vv24]

- **Fact:** Trong thư viện Scikit-learn, tham số `n_init` của KMeans kiểm soát số lần thuật toán chạy với các hạt giống (seeds) khác nhau; giá trị mặc định sẽ chuyển từ 10 sang 'auto' kể từ phiên bản 1.4.
- **Source:** [vv24] - Section: The default value of `n_init` will change from 10 to 'auto' in 1.4.
- **Tag:** [vv24]

- **Fact:** Phương thức `fit(X)` trong KMeans chỉ thực hiện huấn luyện mô hình để tìm trung tâm cụm, trong khi `fit_predict(X)` thực hiện cả huấn luyện và trả về nhãn phân nhóm cho dữ liệu đầu vào.
- **Source:** [vv24] - Section: kmeans.fit(X) và kmeans.fit_predict(X) có gì khác nhau và giải thích.
- **Tag:** [vv24]

- **Fact:** Tiền xử lý dữ liệu cho mô hình AI bao gồm việc chuyển đổi dữ liệu từ định dạng bảng (DataFrame) sang mảng NumPy (numpy array) thông qua thuộc tính `.values`.
- **Source:** [vv24] - Section: Lấy ra numpy array X gồm 3 cột S6, S10, S-AVG.
- **Tag:** [vv24]

- **Fact:** Kỹ thuật Kỹ nghệ đặc trưng (Feature Engineering) được thực hiện bằng cách tính trung bình các cột điểm thành phần (S1-S9, loại trừ S6) để tạo ra biến đầu vào mới `S-AVG` cho mô hình phân cụm.
- **Source:** [vv24] - Section: Tạo ra cột S-AVG là trung bình của các cột S1, S2, S3, S4, S5, S7, S8, S9.
- **Tag:** [vv24]

- **Fact:** Việc gán nhãn (labeling) sau khi phân cụm bằng AI cho phép thực hiện các thao tác phân tích sâu hơn như sử dụng hàm `filter()` và `lambda` để xác định nhóm có kết quả học tập cao nhất.
- **Source:** [vv24] - Section: In ra danh sách các học sinh thuộc nhóm có điểm cao nhất (dùng filter).
- **Tag:** [vv24]

- **Fact:** Thư viện Plotly Express (`px.box`) cung cấp công cụ trực quan hóa dữ liệu AI thông qua biểu đồ hộp (Box Plot) tương tác để so sánh phân phối GPA giữa các khối lớp.
- **Source:** [vv24] - Section: import plotly.express as px VẼ BIỂU ĐỒ BOX.
- **Tag:** [vv24]

- **Fact:** Xử lý dữ liệu khuyết thiếu (Data Cleaning) là bước bắt buộc trước khi huấn luyện AI, ví dụ sử dụng `fillna()` để thay thế giá trị null bằng 0 cho các cột điểm số hoặc bằng 'N' cho cột đăng ký.
- **Source:** [vv24] - Section: In ra DataFrame sau khi đã thực hiện các thay đổi (fillna).
- **Tag:** [vv24]

- **Fact:** Hàm `predict()` của mô hình KMeans đã huấn luyện được sử dụng để dự đoán nhãn nhóm cho các điểm dữ liệu mới (new data) dựa trên các trung tâm cụm đã được xác định.
- **Source:** [vv24] - Section: kmeans.fit (Ví dụ về new_data).
- **Tag:** [vv24]

- **Fact:** Thiết lập tham số `random_state` (ví dụ: `random_state=0`) trong thuật toán KMeans giúp đảm bảo tính nhất quán và khả năng tái lập kết quả phân cụm trong các lần thực thi khác nhau.
- **Source:** [vv24] - Section: Áp dụng thuật toán K-means để phân nhóm dữ liệu (random_state=0).
- **Tag:** [vv24]