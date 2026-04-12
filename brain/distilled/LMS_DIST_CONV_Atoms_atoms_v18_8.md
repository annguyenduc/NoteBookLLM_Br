---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v18_8
  title: atoms_v18_8
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật (Facts) được chưng cất từ nguồn dữ liệu **Volume v18** liên quan đến AI và Machine Learning:

- **Fact:** Lệnh `iowa_model.predict(val_X)` sử dụng mô hình đã được huấn luyện để dự đoán biến mục tiêu trên tập dữ liệu kiểm định (validation set), kết quả thường được lưu vào một mảng như `val_predictions`.
- **Source:** Đoạn 1 - Section: `iowa_model.predict(val_X)`
- **Tag:** [vv18]

- **Fact:** Độ chính xác dự đoán (predictive accuracy) là thước đo phổ biến nhất để đánh giá chất lượng mô hình, xác định xem dự đoán có gần với thực tế hay không.
- **Source:** Đoạn 5 - Section: USER: You'll want to evaluate...
- **Tag:** [vv18]

- **Fact:** Một sai lầm nghiêm trọng trong học máy là đo lường độ chính xác bằng cách sử dụng chính dữ liệu đào tạo để dự đoán và so sánh với giá trị mục tiêu của chính nó.
- **Source:** Đoạn 6 - Section: USER: Many people make a huge mistake...
- **Tag:** [vv18]

- **Fact:** Hàm `train_test_split` từ thư viện `sklearn.model_selection` được sử dụng để chia tách tập dữ liệu gốc thành hai phần: tập huấn luyện (training set) và tập kiểm định (validation set).
- **Source:** Đoạn 10 - Section: ASSISTANT: Import train_test_split
- **Tag:** [vv18]

- **Fact:** Tham số `random_state` (ví dụ: `random_state=1`) đảm bảo tính nhất quán và khả năng tái lập kết quả bằng cách giữ cho việc chia tách dữ liệu giống nhau ở mỗi lần chạy mã.
- **Source:** Đoạn 11 - Section: ASSISTANT: Split the Dataset
- **Tag:** [vv18]

- **Fact:** Biến đặc trưng (Features - X) là các thuộc tính đầu vào dùng để mô tả quan sát, trong khi biến mục tiêu (Target - y) là giá trị mà mô hình cố gắng dự đoán hoặc phân loại.
- **Source:** Đoạn 18 - Section: ASSISTANT: Biến đặc trưng và biến mục tiêu
- **Tag:** [vv18]

- **Fact:** `DecisionTreeRegressor` là một mô hình hồi quy dựa trên cây quyết định, chuyên dùng để dự đoán các giá trị liên tục (như giá nhà).
- **Source:** Đoạn 32 - Section: ASSISTANT: DecisionTreeRegressor
- **Tag:** [vv18]

- **Fact:** Hiện tượng Overfitting (quá khớp) xảy ra khi mô hình "nhớ" dữ liệu huấn luyện quá mức, dẫn đến việc dự đoán cực kỳ chính xác trên tập huấn luyện nhưng không tổng quát hóa tốt trên dữ liệu mới.
- **Source:** Đoạn 21 - Section: ASSISTANT: Overfitting
- **Tag:** [vv18]

- **Fact:** Phương thức `dropna(axis=0)` trong pandas loại bỏ các hàng có chứa giá trị thiếu (NaN), trong khi `dropna(axis=1)` loại bỏ các cột có chứa giá trị thiếu.
- **Source:** Đoạn 38, 40 - Section: ASSISTANT: dropna(axis=0) / dropna(axis=1)
- **Tag:** [vv18]

- **Fact:** Trong thư viện scikit-learn, `sklearn.tree` cung cấp các công cụ xây dựng mô hình cây, còn `sklearn.metrics` cung cấp các hàm để đánh giá hiệu suất của mô hình (như tính độ chính xác hoặc sai số).
- **Source:** Đoạn 44 - Section: ASSISTANT: sklearn.tree và sklearn.metrics có gì khác nhau
- **Tag:** [vv18]

- **Fact:** Thuộc tính `.shape[0]` của một DataFrame trong pandas được sử dụng để kiểm tra tổng số hàng của tệp dữ liệu (ví dụ: tệp CSV sau khi load).
- **Source:** Đoạn 42 - Section: ASSISTANT: kiểm tra csv có bao nhiêu hàng
- **Tag:** [vv18]