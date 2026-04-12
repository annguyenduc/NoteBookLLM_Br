Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu v23 theo quy tắc LOM v4.1:

- **Fact:** [CONV] Thuật toán Pledge khi sử dụng 1 cảm biến siêu âm sẽ điều khiển robot dựa trên khoảng cách phía trước: nếu > 10cm thì đi thẳng, nếu <= 10cm thì quay phải và tiếp tục đi thẳng.
- **Source:** [vv23 - Section: Thuật toán Pledge với một cảm biến siêu âm]
- **Tag:** [vv23]

- **Fact:** [CONV] Trong thuật toán Pledge sử dụng 2 cảm biến, robot sẽ quẹo trái nếu cảm biến bên trái đo được khoảng cách > 10cm và quẹo phải nếu cả cảm biến trước và trái đều gặp vật cản (< 10cm).
- **Source:** [vv23 - Đoạn đầu DỮ LIỆU RAW]
- **Tag:** [vv23]

- **Fact:** [CONV] Cấu trúc dữ liệu bảng điểm học sinh (`py4ai-score.csv`) quy định cột S6 là điểm Midterm và cột S10 là điểm Final.
- **Source:** [vv23 - Section: Conversation: Python Project: Dataset Analysis]
- **Tag:** [vv23]

- **Fact:** [CONV] Quy trình làm sạch dữ liệu (Data Cleaning) cho tập dữ liệu học tập bao gồm việc sử dụng `fillna` để thay thế giá trị NaN bằng 'N' cho cột đăng ký (REG-MC4AI) và bằng 0 cho các cột điểm số (S1-S10, BONUS).
- **Source:** [vv23 - Section: Sửa lỗi sai trong code Python]
- **Tag:** [vv23]

- **Fact:** [CONV] Thư viện `re` (Regular Expression) trong Python được sử dụng để phân loại nhóm lớp (CLASS-GROUP) bằng cách tìm kiếm các mẫu ký tự như 'CV' (Chuyên Văn), 'CTIN' (Chuyên Tin), 'CT' (Chuyên Toán) trong dữ liệu thô.
- **Source:** [vv23 - Section: Hàm group_filter]
- **Tag:** [vv23]

- **Fact:** [CONV] Một dự án phân tích dữ liệu AI hoàn chỉnh thường bao gồm các thư viện: `streamlit` (tạo giao diện), `pandas` (xử lý dữ liệu), `plotly`/`matplotlib` (biểu đồ) và `scikit-learn` (mô hình Kmeans, Regression, Classify).
- **Source:** [vv23 - Section: Conversation: Python Project: Dataset Analysis]
- **Tag:** [vv23]

- **Fact:** [CONV] Biểu thức chính quy `(TH|SN)` được sử dụng để lọc đồng thời các lớp có ký hiệu 'TH' hoặc 'SN' trong chuỗi văn bản.
- **Source:** [vv23 - Section: Sửa lỗi sai trong code Python]
- **Tag:** [vv23]

- **Fact:** [CONV] Việc điều khiển robot di chuyển thực tế (hàm `move_forward`) đòi hỏi giao tiếp với phần cứng hoặc sử dụng các thư viện điều khiển động cơ cụ thể thay vì chỉ in thông báo (print).
- **Source:** [vv23 - Section: Triển khai hàm move_forward() cho robot]
- **Tag:** [vv23]