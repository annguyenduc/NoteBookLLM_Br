---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v23_13
  title: atoms_v23_13
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật (Facts) được trích xuất từ dữ liệu cung cấp (Volume v23) liên quan đến AI và lập trình ứng dụng phân tích dữ liệu.

- **Fact:** Logistic Regression (Hồi quy Logistic) được sử dụng để phân loại dữ liệu vào các nhóm rời rạc (ví dụ: Đậu/Rớt) dựa trên các đặc trưng đầu vào.
- **Source:** [Assistant Response 1 - Section: Giải thích về Logistic Regression]
- **Tag:** [vv23]

- **Fact:** Lỗi `ValueError: Unknown label type: continuous` xảy ra khi sử dụng mô hình phân loại (Classifier) cho biến mục tiêu có giá trị liên tục (Hồi quy).
- **Source:** [User Prompt 4 & Assistant Response 4 - Section: Xử lý lỗi mô hình]
- **Tag:** [vv23]

- **Fact:** Linear Regression (Hồi quy tuyến tính) là mô hình phù hợp để dự đoán các giá trị số thực liên tục như điểm GPA hoặc điểm S10.
- **Source:** [Assistant Response 4 - Section: Chuyển đổi sang Linear Regression]
- **Tag:** [vv23]

- **Fact:** Thư viện Plotly (go.Surface) kết hợp với `np.meshgrid` được sử dụng để vẽ mặt phẳng phân loại (Classification Plane) hoặc mặt phẳng hồi quy (Regression Plane) trong không gian 3D.
- **Source:** [User Prompt 2 & 5 - Section: Visualization code]
- **Tag:** [vv23]

- **Fact:** Cảnh báo `UserWarning: X does not have valid feature names` xuất hiện khi mô hình Scikit-learn được huấn luyện trên DataFrame có tên cột nhưng khi dự đoán lại nhận đầu vào là mảng NumPy hoặc dữ liệu thiếu thông tin tên đặc trưng.
- **Source:** [User Prompt 6 & Assistant Response 6 - Section: Debugging feature names]
- **Tag:** [vv23]

- **Fact:** Trong Scikit-learn, đối tượng `LinearRegression` không sở hữu thuộc tính `feature_names_`.
- **Source:** [Assistant Response 8 - Section: Correction on LinearRegression attributes]
- **Tag:** [vv23]

- **Fact:** Hàm `train_test_split` từ thư viện `sklearn.model_selection` cho phép chia tập dữ liệu thành hai phần huấn luyện (train) và kiểm tra (test) theo tỷ lệ phần trăm người dùng chỉ định.
- **Source:** [User Prompt 2 - Section: Data Preprocessing]
- **Tag:** [vv23]

- **Fact:** Streamlit cung cấp các widget như `st.number_input` để tương tác thay đổi tham số mô hình và `st.plotly_chart` để hiển thị biểu đồ tương tác trực tiếp trên trình duyệt.
- **Source:** [User Prompt 2 & 5 - Section: Streamlit Integration]
- **Tag:** [vv23]

- **Fact:** Độ chính xác của mô hình phân loại được đánh giá bằng `accuracy_score`, trong khi mô hình hồi quy thường dùng `mean_squared_error` (MSE) và `r2_score`.
- **Source:** [User Prompt 2 & Assistant Response 4 - Section: Model Evaluation]
- **Tag:** [vv23]