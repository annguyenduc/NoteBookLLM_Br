Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v23) liên quan đến phân tích dữ liệu trong lộ trình Python4AI:

- **Fact:** [CONV] Sử dụng thư viện Pandas để tạo cột mới 'ROOM' bằng cách lọc tiền tố chuỗi (startswith) từ cột 'PYTHON-CLASS' để phân loại phòng học 114, 115 hoặc các phòng khác.
- **Source:** [Section: viết một hàm tạo một cột [ROOM] để lọc phòng học 114 và 115]
- **Tag:** [vv23]

- **Fact:** [CONV] Streamlit hỗ trợ tạo menu lựa chọn tương tác thông qua hàm `st.selectbox`, cho phép người dùng chuyển đổi giữa các loại biểu đồ như Giới tính, Phòng học, Khối học.
- **Source:** [Section: Tạo selectbox để chọn loại biểu đồ]
- **Tag:** [vv23]

- **Fact:** [CONV] Thư viện Plotly Express (`px.pie`) được dùng để trực quan hóa tỷ lệ học sinh dưới dạng biểu đồ tròn dựa trên các cột dữ liệu phân loại.
- **Source:** [Section: ĐƯA VÀO HÀM]
- **Tag:** [vv23]

- **Fact:** [CONV] Module `re` (Regular Expression) trong Python được sử dụng để tìm kiếm và phân loại dữ liệu lớp học phức tạp (ví dụ: 'CV' là Chuyên Văn, 'CTIN' là Chuyên Tin, '11|12' để lọc khối lớp).
- **Source:** [Section: Giải hticsh câu lệnh / Phân bố điểm (từng Session & GPA)]
- **Tag:** [vv23]

- **Fact:** [CONV] Biểu đồ Histogram (`px.histogram`) và Boxplot (`px.box`) được sử dụng để phân tích sự phân bố điểm số (GPA và các Session) theo các nhóm đối tượng như giới tính (Nam vs Nữ) hoặc buổi học (Sáng vs Chiều).
- **Source:** [Section: Phân bố điểm (từng Session & GPA)]
- **Tag:** [vv23]

- **Fact:** [CONV] Có thể tích hợp nhận xét tự động vào ứng dụng Streamlit bằng cách sử dụng `st.write()` để hiển thị các kết quả tính toán thống kê (như số lượng, tỷ lệ phần trăm, hoặc điểm trung bình) ngay sau khi vẽ biểu đồ.
- **Source:** [Section: tôi muốn thêm nhận xét dựa vào kết quả biểu đồ]
- **Tag:** [vv23]

- **Fact:** [CONV] Sử dụng `plotly.graph_objects` (go) thay cho `plotly.express` khi cần tùy chỉnh sâu biểu đồ Histogram, chẳng hạn như thiết lập chế độ hiển thị chồng lấp (`barmode='overlay'`) và chuẩn hóa dữ liệu theo tỷ lệ phần trăm (`histnorm='percent'`).
- **Source:** [Section: Trong hàm draw_student_ratio_chart, ta sẽ sử dụng plotly.graph_objects]
- **Tag:** [vv23]

- **Fact:** [CONV] Cấu trúc một ứng dụng phân tích dữ liệu Python4AI thường bao gồm việc tách biệt các module: `data_cleaning.py` (làm sạch dữ liệu), `analyze.py` (xử lý logic biểu đồ) và `main.py` (giao diện chính).
- **Source:** [Section: Đưa vào một hàm để gọi từ file main.py]
- **Tag:** [vv23]

- **Fact:** [CONV] Trong Plotly Express, tham số `range_x` được sử dụng trong hàm `px.histogram` để giới hạn phạm vi hiển thị của trục hoành (ví dụ: từ 0 đến 10 cho thang điểm).
- **Source:** [Section: def phan_bo_diem(data, s)]
- **Tag:** [vv23]