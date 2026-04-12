---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v23_6
  title: CONV_atoms_v23_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** [CONV] Quy trình làm sạch dữ liệu (Data Cleaning) cho hệ thống quản lý điểm Python4AI bao gồm việc điền giá trị mặc định cho các trường thiếu: 'REG-MC4AI' được điền là 'N', 'BONUS' và các cột điểm từ 'S1' đến 'S10' được điền giá trị 0.
- **Source:** Hàm `clean_data(input_file)` trong đoạn mã Python.
- **Tag:** [vv23]

- **Fact:** [CONV] Việc phân nhóm học sinh (Class Grouping) được thực hiện bằng cách sử dụng biểu thức chính quy (Regular Expression) để lọc cột 'CLASS' thành các nhóm chuyên biệt như: Chuyên Văn (CV), Chuyên Tin (CTIN), Trung Nhật (CTRN), Chuyên Toán (CT), Chuyên Lý (CL), Chuyên Hoá (CH), Chuyên Anh (CA), Sử Địa (CSD), và TH/SN.
- **Source:** Hàm `group_filter(row)` trong đoạn mã Python.
- **Tag:** [vv23]

- **Fact:** [CONV] Thư viện `plotly.express` (px) được sử dụng để vẽ biểu đồ tròn (`px.pie`) nhằm hiển thị tỷ lệ học sinh theo các đại lượng như giới tính (GENDER), nhóm lớp (CLASS-GROUP), hoặc phòng học (PYTHON-CLASS).
- **Source:** Hàm `draw_pie_chart` và `draw_student_ratio_chart`.
- **Tag:** [vv23]

- **Fact:** [CONV] Trong lập trình Python với thư viện Pandas, để lọc dữ liệu theo nhiều điều kiện logic "hoặc" (OR) trên các chuỗi ký tự, cần sử dụng toán tử bit-wise `|` thay vì từ khóa `or`. Ví dụ: `df[df['PYTHON-CLASS'].str.startswith('114') | df['PYTHON-CLASS'].str.startswith('115')]`.
- **Source:** Phần giải thích sửa lỗi của ASSISTANT cho câu lệnh lọc dữ liệu.
- **Tag:** [vv23]

- **Fact:** [CONV] Ứng dụng phân tích điểm Python4AI được xây dựng trên nền tảng Streamlit, sử dụng cấu trúc Tab (`st.tabs`) để phân chia các tính năng: Danh sách, Phân tích thống kê, Phân nhóm và Phân loại.
- **Source:** Đoạn mã khởi tạo giao diện Streamlit (`st.set_page_config`, `st.tabs`).
- **Tag:** [vv23]

- **Fact:** [CONV] Để vẽ biểu đồ so sánh tỷ lệ giữa hai đối tượng cụ thể (ví dụ phòng học 114 và 115), phương pháp hiệu quả là tạo một cột dữ liệu mới hoặc sử dụng phương thức `.isin(['114', '115'])` để lọc tập dữ liệu trước khi truyền vào hàm vẽ biểu đồ.
- **Source:** Phần thảo luận về việc tạo cột 'PHONG-HOC' và sử dụng hàm `isin`.
- **Tag:** [vv23]