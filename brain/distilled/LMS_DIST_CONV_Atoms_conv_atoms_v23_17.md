---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v23_17
  title: CONV_atoms_v23_17
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v23):

- **Fact:** [CONV] Mô hình Logistic Regression yêu cầu biến mục tiêu (target) phải là các lớp rời rạc (discrete classes); việc sử dụng giá trị liên tục (continuous values) sẽ dẫn đến lỗi `ValueError: Unknown label type: continuous`.
- **Source:** [Phần giải thích lỗi Logistic Regression với dữ liệu liên tục]
- **Tag:** [vv23]

- **Fact:** [CONV] Regression (Hồi quy) được dùng để dự đoán giá trị liên tục (số thực), trong khi Classification (Phân loại) dùng để đưa dữ liệu vào các nhóm hoặc lớp đã xác định trước.
- **Source:** [Phần phân biệt Regression và Classify]
- **Tag:** [vv23]

- **Fact:** [CONV] Linear Regression là thuật toán dự đoán giá trị liên tục bằng cách tìm mô hình tuyến tính xấp xỉ các điểm dữ liệu.
- **Source:** [Phần so sánh Linear và Logistic Regression]
- **Tag:** [vv23]

- **Fact:** [CONV] Logistic Regression sử dụng hàm logistic để giới hạn kết quả dự đoán trong khoảng [0, 1], đại diện cho xác suất thuộc về một lớp nhất định.
- **Source:** [Phần so sánh Linear và Logistic Regression]
- **Tag:** [vv23]

- **Fact:** [CONV] Trong Pandas, thuộc tính `.values` được sử dụng để chuyển đổi các cột được chọn từ DataFrame thành một ma trận NumPy (ndarray).
- **Source:** [Giải thích câu lệnh X = data[['S6', 'S10']].values]
- **Tag:** [vv23]

- **Fact:** [CONV] Khi tạo một Series từ mảng NumPy, việc chỉ định `index=X_test.index` giúp đảm bảo các giá trị dự đoán khớp chính xác với chỉ mục của tập dữ liệu kiểm tra ban đầu.
- **Source:** [Giải thích câu lệnh y_test = pd.Series(...)]
- **Tag:** [vv23]

- **Fact:** [CONV] `secrets.toml` là tệp định dạng TOML được Streamlit sử dụng để lưu trữ các thông tin cấu hình nhạy cảm như khóa API, mật khẩu hoặc thông tin xác thực.
- **Source:** [Giải thích về secrets.toml]
- **Tag:** [vv23]

- **Fact:** [CONV] Bài toán dự đoán một học sinh "đậu" hay "không đậu" lớp tiếp theo thuộc loại bài toán Phân loại (Classification).
- **Source:** [Ví dụ về dự đoán học sinh đậu lớp]
- **Tag:** [vv23]

- **Fact:** [CONV] Lệnh `git clone <URL>` được sử dụng để sao chép một kho lưu trữ (repository) từ máy chủ Git về máy tính cá nhân.
- **Source:** [Hướng dẫn clone dự án git]
- **Tag:** [vv23]

- **Fact:** [CONV] Để tránh giá trị `None` trong tập dữ liệu kiểm tra, có thể sử dụng hàm `data.dropna(subset=['GPA'])` để loại bỏ các dòng thiếu dữ liệu ở cột mục tiêu trước khi chia tập train/test.
- **Source:** [Xử lý GPA_actual bị None]
- **Tag:** [vv23]

- **Fact:** [CONV] Phương thức `reset_index(drop=True, inplace=True)` giúp đồng bộ lại chỉ mục của các DataFrame/Series về dạng mặc định [0, 1, 2...] sau khi thực hiện các thao tác lọc hoặc chia dữ liệu.
- **Source:** [Khắc phục lỗi index làm GPA bị None]
- **Tag:** [vv23]

- **Fact:** [CONV] Lỗi `ValueError` liên quan đến "concatenation axis" xảy ra khi cố gắng nối các mảng NumPy có kích thước không khớp nhau ở các chiều không phải chiều nối.
- **Source:** [Giải thích lỗi ValueError về kích thước mảng]
- **Tag:** [vv23]