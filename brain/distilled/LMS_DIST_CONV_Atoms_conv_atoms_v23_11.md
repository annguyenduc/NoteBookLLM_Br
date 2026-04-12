---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v23_11
  title: CONV_atoms_v23_11
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v23) về lĩnh vực AI và xử lý dữ liệu:

- **Fact:** [CONV] Quy trình huấn luyện mô hình Linear Regression (Hồi quy tuyến tính) bao gồm các bước: chọn đặc trưng (features) và mục tiêu (target), chia dữ liệu train/test bằng `train_test_split`, huấn luyện mô hình bằng `model.fit()`, dự đoán bằng `model.predict()` và đánh giá qua chỉ số MSE (Mean Squared Error) và R-squared.
- **Source:** [vv23] - Section: ASSISTANT (Phản hồi 1).
- **Tag:** [vv23]

- **Fact:** [CONV] Trong thư viện Pandas, có thể xác định vị trí của một cột trong DataFrame bằng phương thức `data.columns.get_loc('tên_cột')` và trích xuất chỉ số của các hàng dữ liệu thông qua thuộc tính `.index.tolist()`.
- **Source:** [vv23] - Section: ASSISTANT (Phản hồi 3 & 5).
- **Tag:** [vv23]

- **Fact:** [CONV] Streamlit cho phép tạo giao diện tương tác cho các bài toán AI bằng cách sử dụng widget `st.number_input` hoặc `st.slider` để người dùng tùy chỉnh tham số `test_size` (tỷ lệ dữ liệu kiểm tra) một cách linh hoạt.
- **Source:** [vv23] - Section: ASSISTANT (Phản hồi 7).
- **Tag:** [vv23]

- **Fact:** [CONV] Thuật toán K-means là một phương pháp học máy không giám sát (unsupervised learning), dùng để phân cụm dữ liệu dựa trên sự tương đồng về đặc trưng (như điểm số S6, S10, GPA) bằng cách tính khoảng cách Euclidean đến các điểm trung tâm (centroids).
- **Source:** [vv23] - Section: ASSISTANT (Phản hồi 9 & 11).
- **Tag:** [vv23]

- **Fact:** [CONV] Quy trình hoạt động của K-means gồm 4 bước: (1) Khởi tạo centroid, (2) Gán điểm dữ liệu vào nhóm có centroid gần nhất, (3) Cập nhật vị trí centroid bằng giá trị trung bình của nhóm, (4) Lặp lại cho đến khi đạt điều kiện dừng.
- **Source:** [vv23] - Section: ASSISTANT (Phản hồi 11).
- **Tag:** [vv23]

- **Fact:** [CONV] Để trực quan hóa kết quả phân cụm hoặc hồi quy trong không gian 3D, có thể sử dụng thư viện Plotly với hàm `px.scatter_3d` (Plotly Express) hoặc `go.Scatter3d` (Graph Objects) để biểu diễn mối quan hệ giữa ba biến số.
- **Source:** [vv23] - Section: ASSISTANT (Phản hồi 9 & 14).
- **Tag:** [vv23]

- **Fact:** [CONV] Kỹ thuật lọc dữ liệu theo nhãn phân cụm trong Pandas có thể thực hiện tối ưu bằng List Comprehension: `datatables = [d[label == i] for i in range(n)]`, giúp tạo ra danh sách các DataFrame con tương ứng với từng nhóm.
- **Source:** [vv23] - Section: ASSISTANT (Phản hồi 13).
- **Tag:** [vv23]

- **Fact:** [CONV] Trong bài toán hồi quy, việc so sánh trực tiếp giữa giá trị thực tế (`S10_actual`) và giá trị dự đoán (`S10_predicted`) trong cùng một DataFrame giúp đánh giá trực quan độ chính xác của mô hình.
- **Source:** [vv23] - Section: ASSISTANT (Phản hồi 2).
- **Tag:** [vv23]

- **Fact:** [CONV] Trước khi đưa dữ liệu vào mô hình K-means, cần thực hiện bước tiền xử lý như lọc các cột cần thiết và xử lý giá trị thiếu bằng phương thức `.fillna(0)`.
- **Source:** [vv23] - Section: USER (Đoạn code hàm classify).
- **Tag:** [vv23]

- **Fact:** [CONV] Để minh họa mô hình hồi quy tuyến tính 3D, ngoài việc vẽ các điểm dữ liệu (scatter plot), có thể sử dụng Surface Plot (biểu đồ mặt phẳng) để thể hiện đường/mặt dự đoán của mô hình.
- **Source:** [vv23] - Section: ASSISTANT (Phản hồi 15).
- **Tag:** [vv23]