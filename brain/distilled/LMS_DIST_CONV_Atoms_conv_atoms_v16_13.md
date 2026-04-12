---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v16_13
  title: CONV_atoms_v16_13
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v16) về chủ đề Tự động hóa với Python (nền tảng cho AI và Robotics):

- **Fact:** [CONV] [Hàm `os.path.join()` được sử dụng để nối các thành phần đường dẫn, tự động xử lý dấu phân cách (`\` trên Windows, `/` trên Linux/macOS) phù hợp với hệ điều hành đang sử dụng.]
- **Source:** [v16 - Section: os.path.join hàm này nghĩa là gì]
- **Tag:** [vv16]

- **Fact:** [CONV] [Phương thức `os.mkdir()` là lệnh chuyên dụng trong module `os` để tạo một thư mục mới.]
- **Source:** [v16 - Section: Quiz: Which method creates a new directory]
- **Tag:** [vv16]

- **Fact:** [CONV] [Hàm `os.chdir(path)` dùng để thay đổi thư mục làm việc hiện tại (Current Working Directory) của chương trình sang một đường dẫn mới.]
- **Source:** [v16 - Section: os.chdir được dùng làm gì]
- **Tag:** [vv16]

- **Fact:** [CONV] [Thư viện `pathlib` cung cấp cách tiếp cận hướng đối tượng để quản lý đường dẫn thông qua lớp `Path`, hỗ trợ các phương thức như `.exists()`, `.mkdir()`, và `.rename()`.]
- **Source:** [v16 - Section: Sử dụng Pathlib]
- **Tag:** [vv16]

- **Fact:** [CONV] [Để tránh lỗi `FileNotFoundError` khi di chuyển hoặc đổi tên tệp bằng `os.rename()`, cần kiểm tra sự tồn tại của tệp nguồn bằng `os.path.exists()`.]
- **Source:** [v16 - Section: Xử lý lỗi FileNotFoundError]
- **Tag:** [vv16]

- **Fact:** [CONV] [Hàm `os.path.getsize(filename)` cho phép lấy kích thước của một tệp tin cụ thể tính theo đơn vị byte.]
- **Source:** [v16 - Section: Question 1: create_python_script]
- **Tag:** [vv16]

- **Fact:** [CONV] [Hàm `os.path.getctime(filename)` được sử dụng để lấy dấu thời gian (timestamp) thời điểm tệp tin được tạo ra trên hệ thống.]
- **Source:** [v16 - Section: file_date function]
- **Tag:** [vv16]

- **Fact:** [CONV] [Việc sử dụng cấu trúc `with open(filename, 'w') as file:` là phương pháp an toàn để tạo tệp mới hoặc ghi đè, tự động đóng tệp sau khi hoàn tất thao tác.]
- **Source:** [v16 - Section: Tạo file mới và di chuyển]
- **Tag:** [vv16]

- **Fact:** [CONV] [Hàm `os.listdir(dir)` trả về một danh sách chứa tên của tất cả các tệp và thư mục con nằm trong thư mục được chỉ định.]
- **Source:** [v16 - Section: Giải thích code Python duyệt thư mục]
- **Tag:** [vv16]

- **Fact:** [CONV] [Để định dạng dấu thời gian từ hệ thống thành chuỗi ngày tháng năm (yyyy-mm-dd) trong Python, có thể sử dụng `datetime.datetime.fromtimestamp()` kết hợp với phương thức `.strftime('%Y-%m-%d')`.]
- **Source:** [v16 - Section: file_date function implementation]
- **Tag:** [vv16]