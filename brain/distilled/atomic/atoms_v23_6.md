Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (Volume v23) về chủ đề Phân tích dữ liệu/AI:

- **Fact:** Trong quy trình làm sạch dữ liệu điểm Python4AI, các giá trị thiếu (NaN) tại cột 'REG-MC4AI' được điền là 'N', cột 'BONUS' và các cột điểm từ 'S1' đến 'S10' được điền giá trị 0.
- **Source:** Hàm `clean_data(input_file)` trong mã nguồn Python.
- **Tag:** [vv23]

- **Fact:** Việc phân nhóm học sinh ('CLASS-GROUP') được thực hiện bằng cách sử dụng biểu thức chính quy (Regex) để lọc cột 'CLASS', phân loại thành các nhóm: Chuyên Văn (CV), Chuyên Tin (CTIN), Trung Nhật (CTRN), Chuyên Toán (CT), Chuyên Lý (CL), Chuyên Hoá (CH), Chuyên Anh (CA), Sử Địa (CSD), và TH/SN.
- **Source:** Hàm con `group_filter(row)` bên trong hàm `clean_data`.
- **Tag:** [vv23]

- **Fact:** Thư viện Plotly Express (`px.pie`) được tích hợp trong ứng dụng Streamlit để vẽ biểu đồ tròn hiển thị tỷ lệ học sinh theo các đại lượng như giới tính, nhóm lớp, hoặc phòng học.
- **Source:** Hàm `draw_pie_chart` và `draw_student_ratio_chart`.
- **Tag:** [vv23]

- **Fact:** Để lọc dữ liệu trong DataFrame Pandas theo nhiều điều kiện (ví dụ: lọc học sinh thuộc phòng 114 hoặc 115), phải sử dụng toán tử bit-wise OR (`|`) thay vì từ khóa logic `or` thông thường.
- **Source:** Phần giải thích sửa lỗi câu lệnh lọc dữ liệu `df[(df['PYTHON-CLASS'].str.startswith('114')) | (df['PYTHON-CLASS'].str.startswith('115'))]`.
- **Tag:** [vv23]

- **Fact:** Phương thức `.isin()` trong Pandas được sử dụng để lọc các dòng có giá trị thuộc một danh sách cho trước, ví dụ như lọc các phòng học cụ thể: `df['PYTHON-CLASS'].isin(['114', '115'])`.
- **Source:** Phần giải thích câu lệnh `draw_student_ratio_chart(df[df['PYTHON-CLASS'].isin(['114', '115'])], 'PYTHON-CLASS')`.
- **Tag:** [vv23]

- **Fact:** Ứng dụng phân tích điểm Python4AI sử dụng Streamlit để tổ chức giao diện theo dạng tab (`st.tabs`), bao gồm các mục: Danh sách, Phân tích thống kê, Phân nhóm, và Phân loại.
- **Source:** Cấu trúc giao diện trong phần `if __name__ == "__main__":` của file main.
- **Tag:** [vv23]

- **Fact:** Để vẽ biểu đồ so sánh tỷ lệ giữa các nhóm cụ thể (như phòng 114 và 115), một kỹ thuật hiệu quả là tạo thêm cột mới (ví dụ 'PHONG-HOC') bằng hàm `.apply()` và `lambda` để gán nhãn lại dữ liệu trước khi lọc và vẽ.
- **Source:** Đoạn mã cuối cùng hướng dẫn tạo cột 'PHONG-HOC' từ cột 'PYTHON-CLASS'.
- **Tag:** [vv23]