---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v23_15
  title: CONV_atoms_v23_15
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v23) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Có hai phương pháp chính để tạo ma trận đầu vào `X` từ DataFrame: (1) Chọn trực tiếp các cột bằng `.values` (giữ nguyên NaN) hoặc (2) Biến đổi phức tạp bằng cách tính tổng các cột (S1-S9 loại bỏ S6), điền giá trị 0 vào NaN bằng `.fillna(0)`, sau đó nối với cột S6 bằng `np.append`.
- **Source:** [vv23] - Section: Dữ liệu RAW (đoạn 1 và 2).
- **Tag:** [vv23]

- **Fact:** [CONV] Mặc dù cách thực hiện khác nhau, cả hai phương pháp tạo ma trận `X` (chọn trực tiếp hoặc biến đổi/tính tổng) đều trả về mảng Numpy 2D có cùng kích thước (shape) là (n, 2), với n là số lượng mẫu dữ liệu.
- **Source:** [vv23] - Section: ASSISTANT trả lời về shape của 2 đoạn.
- **Tag:** [vv23]

- **Fact:** [CONV] Trong thư viện Scikit-learn, hàm `model.score(X_test, y_test)` được sử dụng để đánh giá hiệu suất của mô hình trên tập dữ liệu kiểm tra (test set) mà mô hình chưa từng thấy trong quá trình huấn luyện.
- **Source:** [vv23] - Section: ASSISTANT trả lời về model.score.
- **Tag:** [vv23]

- **Fact:** [CONV] Mô hình `LinearRegression` thực hiện quá trình huấn luyện (`fit`) trên tập huấn luyện (training set) để học các hệ số (coefficients) và sai số (intercept), sau đó mới dùng tập kiểm tra để đánh giá khả năng tổng quát hóa.
- **Source:** [vv23] - Section: ASSISTANT trả lời về LinearRegression thường fit trên tập nào.
- **Tag:** [vv23]

- **Fact:** [CONV] Logistic Regression là thuật toán dành cho bài toán phân loại (classification) với đầu ra là các nhãn rời rạc, trong khi Linear Regression dành cho bài toán dự đoán giá trị liên tục (regression).
- **Source:** [vv23] - Section: ASSISTANT trả lời về sửa lỗi Logistic Regression.
- **Tag:** [vv23]

- **Fact:** [CONV] Lỗi `ValueError: Classification metrics can't handle a mix of multiclass and continuous targets` xảy ra khi người dùng cố gắng sử dụng các thước đo phân loại (như `accuracy_score`) cho một biến mục tiêu chứa các giá trị số liên tục.
- **Source:** [vv23] - Section: ASSISTANT giải thích lỗi ValueError.
- **Tag:** [vv23]

- **Fact:** [CONV] Để sử dụng Logistic Regression cho các biến mục tiêu liên tục (như điểm số), cần phải thực hiện bước rời rạc hóa dữ liệu, ví dụ: sử dụng hàm lambda để phân loại điểm thành 0 và 1 dựa trên một ngưỡng (threshold) nhất định (ví dụ: 5.5).
- **Source:** [vv23] - Section: Ví dụ code Logistic Regression (đoạn xử lý biến y).
- **Tag:** [vv23]

- **Fact:** [CONV] Việc trực quan hóa mô hình hồi quy đa biến (2 đặc trưng đầu vào) có thể thực hiện bằng biểu đồ 3D của Plotly, sử dụng `go.Scatter3d` để vẽ các điểm dữ liệu gốc và `go.Surface` để vẽ mặt phẳng hồi quy (Regression Plane).
- **Source:** [vv23] - Section: Code mẫu trong ASSISTANT trả lời về vẽ biểu đồ.
- **Tag:** [vv23]

- **Fact:** [CONV] Độ chính xác (Accuracy) 0.2 (20%) trong bài toán phân loại được coi là rất thấp, cho thấy mô hình hoạt động không tốt hoặc dữ liệu đầu vào không có mối quan hệ phù hợp với biến mục tiêu.
- **Source:** [vv23] - Section: ASSISTANT trả lời về độ chính xác 0.2.
- **Tag:** [vv23]