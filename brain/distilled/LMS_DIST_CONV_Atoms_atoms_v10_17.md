---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_17
  title: atoms_v10_17
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu **Volume v10** liên quan đến hệ thống, lập trình Python và các công cụ hỗ trợ (nền tảng cho IoT/Robotics/AI).

--------------------------------------------------

- **Fact:** Hệ điều hành (OS) là phần mềm quản lý mọi hoạt động của máy tính, bao gồm hai phần chính: kernel (nhân) và user space (không gian người dùng).
- **Source:** [vv10] - Section: Glossary (O)
- **Tag:** [vv10]

- **Fact:** Piping là quá trình kết nối đầu ra của một chương trình với đầu vào của một chương trình khác để tạo thành một đường ống xử lý dữ liệu (data processing pipeline).
- **Source:** [vv10] - Section: Glossary (P)
- **Tag:** [vv10]

- **Fact:** Regular expression (RegEx) là một truy vấn tìm kiếm văn bản được thể hiện bằng một mẫu chuỗi (string pattern).
- **Source:** [vv10] - Section: Glossary (R)
- **Tag:** [vv10]

- **Fact:** Thư viện `psutil` trong Python được sử dụng để giám sát các thông số hệ thống, ví dụ như hàm `psutil.cpu_percent()` dùng để đo tỉ lệ phần trăm sử dụng CPU.
- **Source:** [vv10] - Section: Applying Changes (cpu_usage.py)
- **Tag:** [vv10]

- **Fact:** Lệnh `diff` dùng để so sánh sự khác biệt giữa các tệp tin, trong đó `diff -u` (unified diff) cung cấp định dạng so sánh có ngữ cảnh giúp lập trình viên dễ dàng theo dõi các thay đổi mã nguồn.
- **Source:** [vv10] - Section: Diffing Files
- **Tag:** [vv10]

- **Fact:** Lệnh `patch` được sử dụng để áp dụng các thay đổi từ một tệp `.diff` vào tệp gốc để cập nhật mã nguồn một cách tự động.
- **Source:** [vv10] - Section: Applying Changes
- **Tag:** [vv10]

- **Fact:** Thư viện `shutil` cung cấp các công cụ quản lý tệp tin và hệ thống, như hàm `shutil.disk_usage(disk)` để kiểm tra dung lượng đĩa cứng (tổng dung lượng, dung lượng trống).
- **Source:** [vv10] - Section: Practical Application of diff and patch (disk_usage.py)
- **Tag:** [vv10]

- **Fact:** Trong Python, để kết thúc một script và trả về mã trạng thái cho hệ thống, lập trình viên sử dụng `sys.exit(0)` cho thành công và `sys.exit(1)` cho lỗi (thay vì dùng `return` bên ngoài hàm).
- **Source:** [vv10] - Section: Practical Application of diff and patch
- **Tag:** [vv10]

- **Fact:** Virtual environment là công cụ cho phép tạo ra các môi trường cô lập cho các dự án Python, giúp quản lý các thư viện riêng biệt mà không ảnh hưởng đến hệ thống chung.
- **Source:** [vv10] - Section: Glossary (V)
- **Tag:** [vv10]

- **Fact:** Unit tests là các bài kiểm tra dùng để xác minh rằng các phần nhỏ, riêng biệt của một chương trình hoạt động chính xác; trong Python thường dùng bộ công cụ `unittest` hoặc `pytest`.
- **Source:** [vv10] - Section: Glossary (U, P)
- **Tag:** [vv10]

- **Fact:** [Unverified_Source] Trong các dự án IoT và Robotics, việc sử dụng `psutil` và `shutil` rất quan trọng để giám sát tài nguyên phần cứng hạn chế trên các máy tính nhúng như Raspberry Pi.

--------------------------------------------------
Tôi đã lưu các thông tin này. Bạn có muốn tôi trích xuất thêm các chi tiết kỹ thuật cụ thể về cách viết RegEx trong các ví dụ trên không?