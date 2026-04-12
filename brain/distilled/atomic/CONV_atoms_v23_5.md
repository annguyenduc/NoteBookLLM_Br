Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v23):

- **Fact:** [CONV] Quy trình làm sạch dữ liệu cho hệ thống điểm AI (py4ai) bao gồm việc xóa các dòng trống, điền giá trị mặc định 'N' cho cột 'REG-MC4AI', và điền giá trị 0 cho các cột điểm 'BONUS' cũng như các cột từ 'S1' đến 'S10'.
- **Source:** [vv23 - Section: clean_data function]
- **Tag:** [vv23]

- **Fact:** [CONV] Việc phân nhóm lớp học trong dữ liệu AI được thực hiện bằng thư viện `re` (Regular Expression) để lọc các mã lớp như 'CV' (Chuyên Văn), 'CTIN' (Chuyên Tin), 'CT' (Chuyên Toán), 'CL' (Chuyên Lý), 'CH' (Chuyên Hóa), 'CA' (Chuyên Anh), 'CSD' (Sử Địa).
- **Source:** [vv23 - Section: group_filter function]
- **Tag:** [vv23]

- **Fact:** [CONV] Trong Streamlit (phiên bản >= 1.0.0), tham số `label_visibility` của các widget có ba chế độ: "visible" (hiển thị mặc định), "auto" (tự động điều chỉnh theo ngôn ngữ), và "hidden" (ẩn nhãn nhưng vẫn giữ widget).
- **Source:** [vv23 - Section: label_visibility explanation]
- **Tag:** [vv23]

- **Fact:** [CONV] Thư viện Plotly Express (`px.histogram`) cho phép tùy chỉnh phạm vi trục X bằng tham số `range_x` (ví dụ: `range_x=(0,10)`) để đồng bộ tỉ lệ giữa nhiều biểu đồ phân bổ điểm số.
- **Source:** [vv23 - Section: phan_bo_diem function]
- **Tag:** [vv23]

- **Fact:** [CONV] Để tạo gợi ý (placeholder) cho `st.selectbox` trong các phiên bản Streamlit không hỗ trợ trực tiếp tham số này, lập trình viên thường sử dụng giá trị `None` ở vị trí `index=0` trong danh sách tùy chọn.
- **Source:** [vv23 - Section: Streamlit selectbox workaround]
- **Tag:** [vv23]

- **Fact:** [CONV] Hàm `np.stack((...)).T` trong Numpy được sử dụng để gộp các mảng một chiều (như giá trị lặp lại, mảng duy nhất và khóa) thành một mảng đa chiều và chuyển vị nó để tạo cấu trúc dữ liệu dạng bảng.
- **Source:** [vv23 - Section: to_stack function explanation]
- **Tag:** [vv23]

- **Fact:** [CONV] Việc hiển thị dữ liệu AI trên giao diện web Streamlit yêu cầu tách biệt logic xử lý dữ liệu (script Python thông thường) và logic hiển thị (Streamlit app) để tránh lỗi phạm vi biến và môi trường thực thi.
- **Source:** [vv23 - Section: Assistant's advice on data_cleaning.py vs main.py]
- **Tag:** [vv23]

- **Fact:** [CONV] Biểu đồ tròn (`px.pie`) trong phân tích dữ liệu học sinh AI thường sử dụng tham số `names` để xác định cột phân loại (như giới tính, lớp) và có thể tích hợp vào các Tab của Streamlit để tăng tính tương tác.
- **Source:** [vv23 - Section: Data Analysis / draw_pie_chart]
- **Tag:** [vv23]