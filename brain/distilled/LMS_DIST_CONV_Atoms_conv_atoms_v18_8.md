---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v18_8
  title: CONV_atoms_v18_8
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu cung cấp liên quan đến AI và xử lý dữ liệu:

- **Fact:** [CONV] [Độ chính xác dự đoán (predictive accuracy) là thước đo phổ biến nhất để đánh giá chất lượng mô hình trong hầu hết các ứng dụng.]
- **Source:** [USER: You'll want to evaluate almost every model... - Đoạn 1]
- **Tag:** [vv18]

- **Fact:** [CONV] [Việc sử dụng chính dữ liệu đào tạo để đo lường độ chính xác dự đoán là một sai lầm lớn vì nó không phản ánh khả năng dự đoán thực tế trên dữ liệu mới.]
- **Source:** [USER: Many people make a huge mistake... - Đoạn 2]
- **Tag:** [vv18]

- **Fact:** [CONV] [Hàm `train_test_split` từ thư viện `sklearn.model_selection` được sử dụng để chia tập dữ liệu thành hai phần: tập huấn luyện (training set) và tập kiểm chứng (validation set).]
- **Source:** [ASSISTANT: Giải thích chi tiết về đoạn mã trên - Mục 1]
- **Tag:** [vv18]

- **Fact:** [CONV] [Tham số `random_state` trong quá trình chia dữ liệu giúp đảm bảo tính nhất quán và khả năng tái lập kết quả (reproducibility) trong mỗi lần chạy mã.]
- **Source:** [ASSISTANT: Giải thích chi tiết về đoạn mã trên - Mục 2]
- **Tag:** [vv18]

- **Fact:** [CONV] [Biến đặc trưng (Features - X) là các thông tin đầu vào dùng để mô tả quan sát, trong khi biến mục tiêu (Target - y) là giá trị mà mô hình cố gắng dự đoán.]
- **Source:** [ASSISTANT: Biến đặc trưng (features) và biến mục tiêu (target variable)...]
- **Tag:** [vv18]

- **Fact:** [CONV] [Mô hình `DecisionTreeRegressor` (Cây quyết định) có xu hướng dễ gặp hiện tượng Overfitting (quá khớp), khi đó mô hình "nhớ" dữ liệu đào tạo quá mức và dự đoán chính xác tuyệt đối trên tập huấn luyện nhưng kém trên dữ liệu mới.]
- **Source:** [ASSISTANT: Khi các giá trị được dự đoán bởi iowa_model... - Mục 1]
- **Tag:** [vv18]

- **Fact:** [CONV] [Phương thức `dropna(axis=0)` trong pandas dùng để loại bỏ các hàng có chứa giá trị thiếu (NaN), trong khi `dropna(axis=1)` dùng để loại bỏ các cột có giá trị thiếu.]
- **Source:** [ASSISTANT: Giải thích dropna(axis=0) và dropna(axis=1)]
- **Tag:** [vv18]

- **Fact:** [CONV] [Module `sklearn.tree` cung cấp các thuật toán xây dựng mô hình (như DecisionTree), còn `sklearn.metrics` cung cấp các hàm để đánh giá hiệu suất của mô hình đó (như tính độ chính xác hoặc sai số).]
- **Source:** [ASSISTANT: sklearn.tree và sklearn.metrics có gì khác nhau]
- **Tag:** [vv18]

- **Fact:** [CONV] [Thuộc tính `df.shape[0]` trong thư viện pandas được sử dụng để xác định tổng số hàng hiện có trong một DataFrame (hoặc tệp CSV sau khi đọc).]
- **Source:** [ASSISTANT: kiểm tra csv có bao nhiêu hàng]
- **Tag:** [vv18]