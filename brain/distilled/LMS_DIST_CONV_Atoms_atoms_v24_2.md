---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v24_2
  title: atoms_v24_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v24:

- **Fact:** Điều khiển xe robot bằng joystick sử dụng hai chân analog A0 (trục X) và A1 (trục Y) để đọc giá trị điện áp, từ đó xác định hướng di chuyển.
- **Source:** [vv24] - Section: Arduino Joystick Control (Code snippet).
- **Tag:** [vv24]

- **Fact:** Trong lập trình Arduino cho robot, việc sử dụng các câu lệnh `if` riêng lẻ thay vì `else if` cho phép kiểm tra nhiều điều kiện hướng cùng lúc, nhưng có thể khiến xe thực hiện đồng thời nhiều hành động nếu joystick nằm ở vị trí trung gian giữa các hướng.
- **Source:** [vv24] - Section: Arduino Joystick Control (Assistant's response).
- **Tag:** [vv24]

- **Fact:** One-hot encoding là phương pháp chuyển đổi các biến hạng mục (categorical variables) thành vector nhị phân để mô hình Machine Learning có thể xử lý dưới dạng số học.
- **Source:** [vv24] - Conversation: One-Hot Encoding Multiclass Classification (Reason 1).
- **Tag:** [vv24]

- **Fact:** Sử dụng One-hot encoding giúp loại bỏ "sự ám ảnh thứ tự" (ordering bias), ngăn chặn mô hình hiểu lầm rằng các nhãn được đánh số (1, 2, 3...) có tính thứ bậc hoặc mức độ quan trọng khác nhau.
- **Source:** [vv24] - Conversation: One-Hot Encoding Multiclass Classification (Reason 3).
- **Tag:** [vv24]

- **Fact:** Hàm Softmax trong Softmax Regression chuyển đổi một vector đầu vào thành một vector xác suất mà tổng các thành phần luôn bằng 1.
- **Source:** [vv24] - Conversation: One-Hot Encoding Multiclass Classification (Softmax explanation).
- **Tag:** [vv24]

- **Fact:** Hàm lỗi Cross-entropy được sử dụng để đo lường sự sai khác giữa xác suất dự đoán ($y_{hat}$) và nhãn thực tế ($y_{true}$); khi kết hợp với One-hot encoding, công thức rút gọn thành $L = -\log(y_{hat}[i])$.
- **Source:** [vv24] - Conversation: One-Hot Encoding Multiclass Classification (Cross-entropy loss).
- **Tag:** [vv24]

- **Fact:** Trong thư viện Pandas (Python), phương thức `isnull().sum()` được dùng để thống kê số lượng giá trị rỗng (null) trong mỗi cột của DataFrame.
- **Source:** [vv24] - Section: Data Preprocessing with Pandas (In ra số lượng các dòng null).
- **Tag:** [vv24]

- **Fact:** Tham số `inplace=True` trong phương thức `fillna()` của Pandas cho phép thay thế trực tiếp các giá trị null vào DataFrame gốc mà không cần tạo bản sao mới.
- **Source:** [vv24] - Section: Data Preprocessing with Pandas (Assistant's response to fillna).
- **Tag:** [vv24]

- **Fact:** Để tránh cảnh báo "SettingWithCopyWarning" khi thay đổi dữ liệu trên một phần của DataFrame, nên sử dụng phương thức truy xuất `.loc` hoặc `.iloc` để tác động trực tiếp lên DataFrame gốc.
- **Source:** [vv24] - Section: Data Preprocessing with Pandas (Assistant's response to "A value is trying to be set...").
- **Tag:** [vv24]

- **Fact:** Tiền xử lý dữ liệu (Preprocess) bao gồm hai bước chính: Bộ lọc (Filter) để loại bỏ dữ liệu nhiễu/không cần thiết và Phân tích dữ liệu (Data Analysis) để tìm hiểu mối quan hệ và xu hướng của dữ liệu.
- **Source:** [vv24] - Section: Preprocess có liên quan Filter & Data Analysis.
- **Tag:** [vv24]