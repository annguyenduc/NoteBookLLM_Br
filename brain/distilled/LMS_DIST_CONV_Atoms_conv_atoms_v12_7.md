---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v12_7
  title: CONV_atoms_v12_7
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v12) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Windows Task Scheduler cho phép tự động hóa việc chạy các script Python (thông qua file .bat) theo lịch trình hàng ngày hoặc hàng tuần để thực hiện các tác vụ hệ thống như dọn dẹp thư mục Temp.
- **Source:** Section: Tạo lịch tự động trên Windows Task Scheduler
- **Tag:** [vv12]

- **Fact:** [CONV] Thư viện `os.walk` trong Python được sử dụng để duyệt qua toàn bộ cây thư mục, cho phép tính toán dung lượng tổng cộng của các file bằng cách cộng dồn kết quả từ hàm `os.path.getsize`.
- **Source:** Section: USER: import os ... def get_folder_sizes
- **Tag:** [vv12]

- **Fact:** [CONV] Để xóa toàn bộ nội dung trong một thư mục mà không xóa chính thư mục đó, Python sử dụng kết hợp `os.listdir` để liệt kê, `os.remove` cho file và `shutil.rmtree` cho các thư mục con.
- **Source:** Section: Hàm xóa nội dung thư mục Temp (clear_temp_folder)
- **Tag:** [vv12]

- **Fact:** [CONV] Khi sử dụng `pandas.ExcelWriter` với `mode="a"` (append) và `engine="openpyxl"`, người dùng có thể thêm các sheet mới vào file Excel hiện có mà không làm mất dữ liệu cũ.
- **Source:** Section: Cách hoạt động chi tiết (if_sheet_exists="overlay")
- **Tag:** [vv12]

- **Fact:** [CONV] Việc kiểm tra sự tồn tại của sheet trong file Excel được thực hiện thông qua thuộc tính `workbook.sheetnames` của thư viện `openpyxl`, giúp tránh lỗi ghi đè dữ liệu quan trọng.
- **Source:** Section: Hàm get_unique_sheet_name
- **Tag:** [vv12]

- **Fact:** [CONV] Một quy trình tự động hóa dọn dẹp hệ thống tiêu chuẩn thường bao gồm 3 bước: Kiểm tra dung lượng hiện tại (threshold check), thực thi lệnh xóa nếu vượt ngưỡng (ví dụ: 2GB), và xuất báo cáo kết quả ra Excel.
- **Source:** Section: Script Python tự động theo dõi và xóa thư mục Temp nếu dung lượng vượt ngưỡng
- **Tag:** [vv12]

- **Fact:** [CONV] Lộ trình học kỹ thuật tự động hóa (Automation) tập trung vào 4 trụ cột: Python cơ bản (vòng lặp/hàm), Thao tác hệ thống (thư viện os/shutil), Xử lý dữ liệu (Pandas/OpenPyXL) và Quản lý tác vụ hệ điều hành.
- **Source:** Section: Lộ trình học lập trình tự động hóa bằng Python
- **Tag:** [vv12]

- **Fact:** [CONV] Quyền Admin (Administrator privileges) là điều kiện bắt buộc để script Python có thể can thiệp và xóa các file hệ thống hoặc file tạm đang bị khóa trong thư mục Temp của Windows.
- **Source:** Section: Lưu ý quan trọng - Quyền truy cập
- **Tag:** [vv12]