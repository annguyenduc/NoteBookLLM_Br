Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (Volume v02) liên quan đến việc quản lý và tổ chức dữ liệu cho các lớp học kỹ thuật/STEM:

- **Fact:** [CONV] Sử dụng thư viện Pandas và Openpyxl trong Python để tự động hóa việc tạo cấu trúc quản lý lớp học (có thể áp dụng cho các môn Robotics/IoT) dưới dạng file Excel với nhiều sheet tương ứng với từng lớp.
- **Source:** [Dữ liệu RAW - Đoạn mã Python: `import pandas as pd`, `with pd.ExcelWriter(out_path, engine="openpyxl") as writer`]
- **Tag:** [vv02]

- **Fact:** [CONV] Cấu trúc chương trình học kỹ thuật (Lớp 10) được thiết kế bao gồm 4 học phần, triển khai trong 32 tuần (mỗi học phần 8 tuần).
- **Source:** [Dữ liệu RAW - Phần phản hồi của Assistant: "4 học phần × 8 tuần = 32 tuần"]
- **Tag:** [vv02]

- **Fact:** [CONV] Mô hình quản lý lớp học STEM thực hành thường chia quy mô 8 nhóm mỗi lớp để theo dõi tiến độ và điểm số.
- **Source:** [Dữ liệu RAW - Phần phản hồi của Assistant: "8 nhóm / lớp (Nhóm 1 → Nhóm 8)"]
- **Tag:** [vv02]

- **Fact:** [CONV] Các trường dữ liệu quan trọng để theo dõi học tập kỹ thuật bao gồm: Học phần, Tuần, Nhóm, Tên bài học, Điểm cộng (+), Điểm trừ (-) và Tổng điểm.
- **Source:** [Dữ liệu RAW - Danh sách cột trong hàm `build_class_template`: "Học phần", "Tuần", "Nhóm", "Tên bài học", "Điểm +", "Điểm -", "Tổng điểm"]
- **Tag:** [vv02]

- **Fact:** [CONV] Khi xử lý dữ liệu xuất ra Excel bằng code, tên sheet phải được làm sạch: giới hạn tối đa 31 ký tự và không chứa các ký tự đặc biệt như `[]:*?/ \`.
- **Source:** [Dữ liệu RAW - Đoạn mã xử lý `clean_name`: `sheet[:31].replace("/","-").replace("\\","-")...`]
- **Tag:** [vv02]

- **Fact:** [CONV] Chương trình học lớp 10 có thể được cấu trúc hóa để theo dõi điểm số tự động theo công thức: Tổng điểm = Điểm cộng - Điểm trừ. [Unverified_Source: Giả định dựa trên gợi ý tính toán của Assistant trong văn bản].
- **Source:** [Dữ liệu RAW - Phần gợi ý của Assistant: "tự động tính Tổng điểm = Điểm + − Điểm -"]
- **Tag:** [vv02]