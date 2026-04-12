---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v24_2
  title: CONV_atoms_v24_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v24):

- **Fact:** [CONV] Trong điều khiển robot bằng Arduino, các chân analog (như A0 và A1) thường được dùng để đọc giá trị từ joystick nhằm xác định hướng di chuyển và điều khiển động cơ DC thông qua các chân đầu ra (OUTPUT).
- **Source:** Đoạn mã Arduino đầu tiên và phần giải thích về joystick.
- **Tag:** [vv24]

- **Fact:** [CONV] Việc sử dụng các câu lệnh `if` riêng lẻ thay vì `else if` khi đọc giá trị joystick có thể khiến nhiều điều kiện đúng cùng lúc, dẫn đến việc robot thực hiện nhiều hành động di chuyển đồng thời nếu joystick nằm ở vị trí trung gian hoặc chéo.
- **Source:** Phần trả lời của ASSISTANT về việc sử dụng lệnh `if` riêng lẻ.
- **Tag:** [vv24]

- **Fact:** [CONV] One-hot encoding chuyển đổi các biến hạng mục (categorical variables) thành vectơ nhị phân để tránh lỗi "ám ảnh thứ tự" (ordering bias), giúp mô hình không hiểu nhầm các nhãn lớp có tính thứ tự hoặc mức độ quan trọng khác nhau.
- **Source:** Phần "One-hot Encoding Multiclass Classification", mục 3: Tránh sự ám ảnh.
- **Tag:** [vv24]

- **Fact:** [CONV] Hàm Softmax trong Softmax Regression có nhiệm vụ chuyển đổi một vectơ đầu vào thành một vectơ xác suất mà tổng các thành phần luôn bằng 1.
- **Source:** Phần giải thích về Softmax Regression.
- **Tag:** [vv24]

- **Fact:** [CONV] Khi nhãn thực tế được mã hóa bằng one-hot, hàm lỗi cross-entropy có thể rút gọn thành $L(y\_hat, y\_true\_oh) = -log(y\_hat[i])$, trong đó $y\_hat[i]$ là xác suất dự đoán cho lớp đúng.
- **Source:** Phần giải thích công thức tính lỗi trong Softmax Regression.
- **Tag:** [vv24]

- **Fact:** [CONV] Trong thư viện Pandas (Python), phương thức `isnull().sum()` được sử dụng để thống kê số lượng giá trị bị thiếu (null) trong mỗi cột của DataFrame.
- **Source:** Phần trả lời về "In ra số lượng các dòng null của mỗi cột".
- **Tag:** [vv24]

- **Fact:** [CONV] Tham số `inplace=True` trong phương thức `fillna()` của Pandas cho phép thay thế các giá trị null trực tiếp trên DataFrame gốc mà không cần tạo ra một bản sao mới.
- **Source:** Phần giải thích về câu lệnh `df['homepage'].fillna('unknown', inplace=True)`.
- **Tag:** [vv24]

- **Fact:** [CONV] Để tránh cảnh báo "SettingWithCopyWarning" khi thay đổi dữ liệu trên một phần của DataFrame, nên sử dụng phương thức truy cập dữ liệu `df.loc` hoặc `df.iloc`.
- **Source:** Phần giải thích về thông báo "A value is trying to be set on a copy of a slice from a DataFrame".
- **Tag:** [vv24]

- **Fact:** [CONV] Tiền xử lý dữ liệu (Preprocess) bao gồm hai hoạt động chính: Bộ lọc (Filter) để loại bỏ dữ liệu nhiễu/không hợp lệ và Phân tích dữ liệu (Data Analysis) để tìm hiểu các mối quan hệ, xu hướng trong tập dữ liệu.
- **Source:** Phần trả lời về "Preprocess có liên quan Filter & Data Analysis".
- **Tag:** [vv24]

- **Fact:** [CONV] Phương thức `map()` trong Pandas được sử dụng để ánh xạ các giá trị cũ sang giá trị mới dựa trên một từ điển (dictionary), thường dùng để tạo cột mới hoặc chuyển đổi nhãn dữ liệu.
- **Source:** Phần ví dụ về `gender_mapping` và `class_mapping`.
- **Tag:** [vv24]