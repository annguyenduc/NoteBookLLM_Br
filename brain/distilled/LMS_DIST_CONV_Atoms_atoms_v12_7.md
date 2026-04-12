---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v12_7
  title: atoms_v12_7
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là **@scout**. Dưới đây là các sự kiện kỹ thuật được chưng cất từ dữ liệu **Volume v12** liên quan đến tự động hóa và lập trình hệ thống:

- **Fact:** Có thể sử dụng Python để tự động giám sát dung lượng thư mục và thực hiện dọn dẹp (xóa file) khi dung lượng vượt ngưỡng chỉ định (ví dụ: 2GB).
- **Source:** [vv12] - Section: Script Python tự động theo dõi và xóa thư mục Temp.
- **Tag:** [vv12]

- **Fact:** Hàm `os.walk()` trong Python được sử dụng để duyệt qua toàn bộ cấu trúc cây thư mục, cho phép tính tổng dung lượng bằng cách cộng dồn kích thước từng tệp tin qua `os.path.getsize()`.
- **Source:** [vv12] - Hàm `calculate_folder_size` và `get_folder_sizes`.
- **Tag:** [vv12]

- **Fact:** Để ghi thêm dữ liệu vào file Excel hiện có mà không làm mất dữ liệu cũ, sử dụng `pd.ExcelWriter` với tham số `mode="a"` (append) và `if_sheet_exists="overlay"`.
- **Source:** [vv12] - Hàm `export_to_excel`.
- **Tag:** [vv12]

- **Fact:** Việc tự động hóa chạy script Python trên Windows có thể thực hiện thông qua **Windows Task Scheduler** bằng cách tạo một file `.bat` trung gian hoặc chỉ định trực tiếp đường dẫn script.
- **Source:** [vv12] - Section: Tạo lịch tự động trên Windows Task Scheduler.
- **Tag:** [vv12]

- **Fact:** Khi xóa các file hệ thống hoặc file trong thư mục `Temp`, script cần được thực thi với quyền **Admin** để tránh lỗi truy cập (Access Denied).
- **Source:** [vv12] - Section: Lưu ý quan trọng - Quyền truy cập.
- **Tag:** [vv12]

- **Fact:** Thư viện `shutil.rmtree()` được sử dụng để xóa toàn bộ một thư mục và tất cả nội dung bên trong nó một cách đệ quy.
- **Source:** [vv12] - Hàm `clear_temp_folder`.
- **Tag:** [vv12]

- **Fact:** Để tránh lỗi trùng tên Sheet khi xuất báo cáo Excel theo ngày, cần kiểm tra danh sách sheet hiện có qua `workbook.sheetnames` (thư viện `openpyxl`) và thêm hậu tố số thứ tự (ví dụ: `_1`, `_2`).
- **Source:** [vv12] - Hàm `get_unique_sheet_name`.
- **Tag:** [vv12]

- **Fact:** Lộ trình học tự động hóa (Automation) cơ bản gồm 4 giai đoạn: 1. Python cơ bản; 2. Thao tác File/Excel (`os`, `pandas`, `openpyxl`); 3. Xử lý lỗi và Lập lịch; 4. Ứng dụng thực tế và Tối ưu hóa.
- **Source:** [vv12] - Section: Lộ trình học lập trình tự động hóa bằng Python.
- **Tag:** [vv12]

- **Fact:** Thời gian ước tính để một người bình thường nắm bắt các kỹ năng tự động hóa cơ bản là khoảng 2-4 tháng với cường độ học 2-3 giờ/ngày.
- **Source:** [vv12] - Section: Lộ trình học lập trình tự động hóa bằng Python.
- **Tag:** [vv12]