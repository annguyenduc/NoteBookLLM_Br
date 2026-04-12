---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v12_6
  title: CONV_atoms_v12_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp, tập trung vào nền tảng lập trình Python (công cụ cốt lõi trong AI, IoT và Robotics) để quản lý dữ liệu và hệ thống.

- **Fact:** [CONV] `os.walk` là hàm trong module `os` của Python dùng để lặp đệ quy qua tất cả các thư mục và tệp tin trong một cây thư mục.
- **Source:** [vv12 - Section: ASSISTANT: os.walk là gì]
- **Tag:** [vv12]

- **Fact:** [CONV] Giá trị trả về của `os.walk` là một generator, mỗi lần lặp cung cấp một tuple gồm 3 phần: `root` (đường dẫn hiện tại), `dirs` (danh sách thư mục con), và `files` (danh sách tệp tin).
- **Source:** [vv12 - Section: Giá trị trả về]
- **Tag:** [vv12]

- **Fact:** [CONV] Để tính dung lượng tệp tin trong Python, sử dụng hàm `os.path.getsize(file_path)`, thường kết hợp với `os.path.join(root, file)` để lấy đường dẫn đầy đủ.
- **Source:** [vv12 - Section: Ví dụ minh họa 2]
- **Tag:** [vv12]

- **Fact:** [CONV] Lỗi `PermissionError: [Errno 13]` xảy ra khi chương trình không có quyền ghi vào file hoặc file đó đang được mở bởi một ứng dụng khác (như Excel).
- **Source:** [vv12 - Section: ASSISTANT: Lỗi PermissionError]
- **Tag:** [vv12]

- **Fact:** [CONV] Thư viện `pandas` hỗ trợ ghi thêm sheet mới vào file Excel hiện có bằng cách sử dụng `pd.ExcelWriter` với tham số `mode="a"` (append) và `if_sheet_exists="overlay"`.
- **Source:** [vv12 - Section: Giải thích các thay đổi (trong code tạo sheet mới)]
- **Tag:** [vv12]

- **Fact:** [CONV] Hàm `shutil.rmtree(path)` trong Python được sử dụng để xóa toàn bộ một thư mục bao gồm tất cả các thư mục con và tệp tin bên trong nó.
- **Source:** [vv12 - Section: Script Python tự động xóa nội dung thư mục Temp]
- **Tag:** [vv12]

- **Fact:** [CONV] Việc tự động hóa các script Python trên Windows có thể thực hiện thông qua **Task Scheduler** bằng cách tạo một file `.bat` để thực thi file `.py`.
- **Source:** [vv12 - Section: Hướng dẫn cài đặt tự động hóa (Task Scheduler)]
- **Tag:** [vv12]

- **Fact:** [CONV] Python là ngôn ngữ lập trình phổ biến nhất để xử lý dữ liệu lớn (Big Data) và xây dựng các thuật toán trí tuệ nhân tạo (AI) nhờ các thư viện mạnh mẽ như `pandas`.
- **Source:** [Nội dung tổng quát về xử lý dữ liệu trong hội thoại]
- **Tag:** [Unverified_Source]

- **Fact:** [CONV] Trong các hệ thống IoT và Robotics, việc quản lý dung lượng bộ nhớ và dọn dẹp file tạm (Temp files) bằng script tự động là cực kỳ quan trọng để duy trì tính ổn định của hệ