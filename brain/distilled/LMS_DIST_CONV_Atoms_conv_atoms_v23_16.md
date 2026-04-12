---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v23_16
  title: CONV_atoms_v23_16
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp:

- **Fact:** [CONV] [Mô hình Linear Regression được sử dụng để dự đoán các giá trị liên tục (như điểm S10 hoặc GPA), trong khi Logistic Regression chỉ phù hợp cho các bài toán phân loại với nhãn dữ liệu rời rạc (discrete classes).]
- **Source:** [Phần giải thích lỗi ValueError: Unknown label type: continuous]
- **Tag:** [vv23]

- **Fact:** [CONV] [Trong thư viện Scikit-learn, nếu sử dụng Logistic Regression trên tập dữ liệu có mục tiêu (target) là giá trị liên tục (số thực), hệ thống sẽ trả về lỗi "ValueError: Unknown label type: continuous".]
- **Source:** [Phần phản hồi của Assistant về lỗi của người dùng]
- **Tag:** [vv23]

- **Fact:** [CONV] [Khi sử dụng Streamlit, các widget cùng loại (như st.number_input) nếu có cấu trúc giống nhau sẽ gây lỗi xung đột khóa (key). Cần truyền tham số `key` duy nhất cho mỗi widget để khắc phục.]
- **Source:** [Phần giải thích về lỗi "multiple identical st.number_input widgets"]
- **Tag:** [vv23]

- **Fact:** [CONV] [Để trực quan hóa kết quả hồi quy trong không gian 3D, có thể sử dụng thư viện Plotly với `go.Scatter3d` để vẽ các điểm dữ liệu gốc và `go.Surface` để vẽ mặt phẳng hồi quy (regression plane).]
- **Source:** [Đoạn mã Python sử dụng plotly.graph_objects]
- **Tag:** [vv23]

- **Fact:** [CONV] [Quy trình chuẩn bị dữ liệu cho mô hình học máy bao gồm việc chia dữ liệu thành tập huấn luyện (train) và tập kiểm tra (test) thông qua hàm `train_test_split` từ thư viện `sklearn.model_selection`.]
- **Source:** [Đoạn mã Python thực hiện train_test_split]
- **Tag:** [vv23]

- **Fact:** [CONV] [Để tạo mặt phẳng dự đoán (surface) trên biểu đồ 3D, cần tạo một lưới tọa độ 2D bằng `np.meshgrid` và `np.linspace`, sau đó sử dụng phương thức `.predict()` của mô hình trên dữ liệu đã được làm phẳng bằng `.ravel()`.]
- **Source:** [Đoạn mã tạo s6_plane và s_avg_plane]
- **Tag:** [vv23]