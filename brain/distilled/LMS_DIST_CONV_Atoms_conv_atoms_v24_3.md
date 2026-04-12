---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v24_3
  title: CONV_atoms_v24_3
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật về AI và xử lý dữ liệu được trích xuất từ nguồn cung cấp:

- **Fact:** [CONV] Thuật toán K-means (từ thư viện `sklearn.cluster`) được sử dụng để phân nhóm (clustering) các đối tượng dữ liệu dựa trên các đặc trưng số học đầu vào.
- **Source:** [vv24] - Section: Dùng KMeans để phân nhóm các học sinh thành 3 nhóm theo tập X tạo ra.
- **Tag:** [vv24]

- **Fact:** [CONV] Trong thư viện Scikit-learn, tham số `n_init` của thuật toán KMeans (xác định số lần chạy thuật toán với các hạt giống trung tâm khác nhau) có giá trị mặc định thay đổi từ 10 sang 'auto' kể từ phiên bản 1.4.
- **Source:** [vv24] - Section: The default value of n_init will change from 10 to 'auto' in 1.4.
- **Tag:** [vv24]

- **Fact:** [CONV] Sự khác biệt giữa `fit(X)` và `fit_predict(X)` trong KMeans: `fit(X)` chỉ thực hiện huấn luyện để tìm trung tâm cụm tối ưu, trong khi `fit_predict(X)` thực hiện huấn luyện và trả về ngay mảng nhãn phân nhóm của các điểm dữ liệu.
- **Source:** [vv24] - Section: kmeans.fit(X) và kmeans.fit_predict(X) có gì khác nhau và giải thích.
- **Tag:** [vv24]

- **Fact:** [CONV] Quá trình huấn luyện của K-means bao gồm việc lặp lại hai bước chính: gán nhãn cho các điểm dữ liệu và cập nhật vị trí trung tâm cụm (centroids) nhằm tối thiểu hóa tổng bình phương khoảng cách giữa các điểm và trung tâm của chúng.
- **Source:** [vv24] - Section: kmeans.fit.
- **Tag:** [vv24]

- **Fact:** [CONV] Sau khi mô hình KMeans đã được huấn luyện bằng phương thức `fit()`, có thể sử dụng phương thức `predict()` để dự đoán nhãn phân nhóm cho các điểm dữ liệu mới (new data) có cùng cấu trúc đặc trưng.
- **Source:** [vv24] - Section: kmeans.fit (Ví dụ code minh họa).
- **Tag:** [vv24]

- **Fact:** [CONV] Trong quy trình chuẩn bị dữ liệu cho AI, thuộc tính `.values` của thư viện Pandas được sử dụng để chuyển đổi các cột dữ liệu từ dạng DataFrame sang mảng Numpy (Numpy array), định dạng tiêu chuẩn cho các thuật toán học máy.
- **Source:** [vv24] - Section: Lấy ra numpy array X gồm 3 cột S6, S10, S-AVG.
- **Tag:** [vv24]

- **Fact:** [CONV] Thư viện `plotly.express` hỗ trợ trực quan hóa dữ liệu AI thông qua hàm `px.box`, cho phép vẽ biểu đồ hộp để phân tích phân bố và so sánh các đặc trưng (như GPA) giữa các nhóm dữ liệu khác nhau.
- **Source:** [vv24] - Section: import plotly.express as px VẼ BIỂU ĐỒ BOX.
- **Tag:** [vv24]

- **Fact:** [CONV] Phương thức `mean(axis=1)` trong Pandas cho phép tính toán giá trị trung bình theo hàng ngang, thường dùng để tạo ra các đặc trưng tổng hợp (feature engineering) từ nhiều cột dữ liệu số khác nhau.
- **Source:** [vv24] - Section: Tạo ra cột S-AVG là trung bình của các cột S1, S2, S3, S4, S5, S7, S8, S9.
- **Tag:** [vv24]