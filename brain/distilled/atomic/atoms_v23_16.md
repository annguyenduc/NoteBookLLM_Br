Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v23):

- **Fact:** Thuật toán Linear Regression (Hồi quy tuyến tính) được sử dụng để dự đoán các biến liên tục như điểm GPA hoặc điểm thành phần (S10) dựa trên các đặc trưng đầu vào.
- **Source:** [vv23] - Section: Assistant response to "ValueError: Unknown label type: continuous".
- **Tag:** [vv23]

- **Fact:** Thuật toán Logistic Regression là một thuật toán phân loại (classification), được thiết kế cho các tác vụ mà biến mục tiêu (target variable) là các lớp rời rạc (discrete classes).
- **Source:** [vv23] - Section: Assistant response to "ValueError: Unknown label type: continuous".
- **Tag:** [vv23]

- **Fact:** Việc sử dụng thuật toán phân loại (như Logistic Regression) cho một mục tiêu hồi quy có giá trị liên tục sẽ gây ra lỗi "ValueError: Unknown label type: continuous" trong thư viện Scikit-learn.
- **Source:** [vv23] - Section: User error report and Assistant explanation.
- **Tag:** [vv23]

- **Fact:** Trong thư viện Streamlit, khi tạo nhiều widget có cấu trúc giống hệt nhau (ví dụ: `st.number_input`), cần phải cung cấp tham số `key` duy nhất cho mỗi widget để tránh lỗi xung đột mã định danh nội bộ (internal key).
- **Source:** [vv23] - Section: Assistant response to "There are multiple identical st.number_input widgets...".
- **Tag:** [vv23]

- **Fact:** Hàm `train_test_split` từ thư viện `sklearn.model_selection` được sử dụng để chia tập dữ liệu thành hai phần: tập huấn luyện (train set) và tập kiểm tra (test set) theo tỷ lệ người dùng chỉ định (test_size).
- **Source:** [vv23] - Section: Python code blocks in phanloai function.
- **Tag:** [vv23]

- **Fact:** Để trực quan hóa mặt phẳng hồi quy (regression plane) trong không gian 3 chiều, có thể sử dụng thư viện Plotly với các đối tượng `go.Scatter3d` (cho các điểm dữ liệu) và `go.Surface` (cho mặt phẳng dự đoán).
- **Source:** [vv23] - Section: Python code blocks (phanloai function).
- **Tag:** [vv23]

- **Fact:** Việc tạo lưới 2D cho mặt phẳng dự đoán trong đồ thị 3D thường sử dụng hàm `np.linspace` để tạo các khoảng giá trị và `np.meshgrid` để tạo ma trận tọa độ.
- **Source:** [vv23] - Section: Python code blocks (phanloai function).
- **Tag:** [vv23]