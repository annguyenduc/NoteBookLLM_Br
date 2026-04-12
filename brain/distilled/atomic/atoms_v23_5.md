Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu cung cấp, tập trung vào lĩnh vực AI (Xử lý dữ liệu và Dashboard phân tích):

- **Fact:** Quy trình làm sạch dữ liệu cho AI (py4ai) bao gồm việc xử lý giá trị khuyết thiếu (NaN) bằng phương thức `fillna`: chuyển cột 'REG-MC4AI' trống thành 'N', 'BONUS' và các cột điểm từ 'S1' đến 'S10' trống thành 0.
- **Source:** Đoạn mã trong hàm `clean_data` và phần giải thích về `data_cleaning.py`.
- **Tag:** [vv23]

- **Fact:** Sử dụng thư viện `re` (Regular Expression) trong Python để phân loại dữ liệu thô từ cột 'CLASS' thành các nhóm chuyên biệt (như Chuyên Văn, Chuyên Tin, Chuyên Toán,...) nhằm chuẩn hóa thuộc tính 'CLASS-GROUP'.
- **Source:** Hàm `group_filter(row)` trong mã nguồn Python.
- **Tag:** [vv23]

- **Fact:** Thư viện Streamlit được sử dụng để xây dựng ứng dụng web tương tác hiển thị dữ liệu AI, nhưng không thể chạy trực tiếp như một script Python thông thường mà cần môi trường thực thi của Streamlit.
- **Source:** Phần giải thích của ASSISTANT về lỗi sử dụng `st.dataframe`.
- **Tag:** [vv23]

- **Fact:** Trong Streamlit (phiên bản >= 1.0.0), tham số `label_visibility` của các widget (như `selectbox`, `slider`) có 3 chế độ hiển thị: `"visible"` (mặc định), `"auto"` (tự động theo ngôn ngữ), và `"hidden"` (ẩn nhãn).
- **Source:** Phần giải thích về `label_visibility="visible"`.
- **Tag:** [vv23]

- **Fact:** Plotly Express (`px.histogram`) hỗ trợ trực quan hóa phân phối điểm số trong AI với các tham số tùy chỉnh như `range_x` để cố định trục tọa độ (ví dụ: từ 0 đến 10) và `color` để phân tách dữ liệu theo thuộc tính (ví dụ: giới tính 'GENDER').
- **Source:** Hàm `phan_bo_diem` và phần giải thích về `px.histogram`.
- **Tag:** [vv23]

- **Fact:** Để tạo bố cục Dashboard AI chuyên nghiệp, Streamlit sử dụng `st.columns` để chia màn hình thành nhiều cột, cho phép sắp xếp nhiều biểu đồ histogram hoặc pie chart trên cùng một hàng.
- **Source:** Hàm `analyze(data)` và các phản hồi về chia cột/hàng.
- **Tag:** [vv23]

- **Fact:** Việc tích hợp các module xử lý dữ liệu vào ứng dụng chính (main.py) có thể thực hiện bằng cách `import` hàm từ file `.py` khác và nhận kết quả trả về dưới dạng DataFrame của Pandas.
- **Source:** Phần hướng dẫn gọi kết quả từ `data_cleaning.py` sang `main.py`.
- **Tag:** [vv23]

- **Fact:** Biểu đồ tròn (`px.pie`) trong Plotly Express được sử dụng để phân tích tỷ lệ các đại lượng trong tập dữ liệu AI, với các tham số `names` để xác định nhãn phân loại.
- **Source:** Hàm `draw_pie_chart` trong phần phân tích tỷ lệ học sinh.
- **Tag:** [vv23]