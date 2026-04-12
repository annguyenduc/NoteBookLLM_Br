---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v12_6
  title: atoms_v12_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp, tập trung vào khía cạnh lập trình hệ thống và tự động hóa (nền tảng cho Robotics và AI):

- **Fact:** `os.walk` là một hàm trong module `os` của Python dùng để lặp đệ quy qua cây thư mục, trả về một generator chứa bộ ba (tuple): root (đường dẫn hiện tại), dirs (danh sách thư mục con) và files (danh sách tệp tin).
- **Source:** [vv12] - Section: `os.walk` là gì / Giá trị trả về.
- **Tag:** [vv12]

- **Fact:** Hàm `os.path.getsize(path)` được sử dụng để lấy kích thước của một tệp tin tính theo đơn vị byte.
- **Source:** [vv12] - Section: Ví dụ minh họa (2. Tính tổng dung lượng).
- **Tag:** [vv12]

- **Fact:** Thư viện `pandas` (thường được alias là `pd`) hỗ trợ chuyển đổi cấu trúc dữ liệu list/dictionary thành DataFrame để sắp xếp và xuất dữ liệu ra định dạng Excel (.xlsx).
- **Source:** [vv12] - Section: Giải thích các câu trên theo dạng bảng.
- **Tag:** [vv12]

- **Fact:** Lỗi `PermissionError: [Errno 13]` trong Python thường xuất hiện khi tệp tin mục tiêu đang được mở bởi một ứng dụng khác (như Excel) hoặc do script không có đủ quyền ghi vào thư mục hệ thống.
- **Source:** [vv12] - Section: Cách khắc phục (PermissionError).
- **Tag:** [vv12]

- **Fact:** Để ghi thêm một sheet mới vào file Excel đã tồn tại mà không xóa dữ liệu cũ, Python sử dụng `pd.ExcelWriter` với tham số `mode="a"` (append) và `if_sheet_exists="overlay"`.
- **Source:** [vv12] - Section: Giải thích các thay đổi (Ghi thêm vào file Excel cũ).
- **Tag:** [vv12]

- **Fact:** Thư viện `shutil` với hàm `shutil.rmtree()` cho phép xóa toàn bộ một cây thư mục (bao gồm thư mục gốc và tất cả nội dung bên trong) một cách tự động.
- **Source:** [vv12] - Section: Script Python tự động xóa nội dung thư mục Temp.
- **Tag:** [vv12]

- **Fact:** Trong các hệ thống IoT hoặc Robotics chạy trên Linux/Windows, việc tự động hóa dọn dẹp thư mục Temp bằng Python giúp duy trì dung lượng bộ nhớ trống cho các tác vụ ghi log hoặc xử lý dữ liệu AI.
- **Source:** [Unverified_Source] (Bổ sung dựa trên ứng dụng thực tế của script xóa Temp trong dữ liệu).
- **Tag:** [vv12]

- **Fact:** Việc sử dụng `try...except OSError` khi duyệt file giúp chương trình không bị dừng đột ngột khi gặp các file hệ thống hoặc file đang bị khóa mà script không có quyền truy cập.
- **Source:** [vv12] - Section: Giải thích các câu trên theo dạng bảng (Dòng `except OSError`).
- **Tag:** [vv12]