---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_10
  title: atoms_v10_10
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v10 (Module 6: Python & Linux Streams/Processes):

- **Fact:** Module 6 của khóa học tập trung vào kỹ năng xử lý file (Reading and Writing Files) bao gồm các hàm cơ bản: `open()` để mở file, `read()`, `readline()`, `readlines()` để đọc dữ liệu và `write()` để ghi dữ liệu.
- **Source:** (vv10 - Section: Reading and Writing Files)
- **Tag:** [vv10]

- **Fact:** Trong hệ thống Linux, có 3 luồng dữ liệu tiêu chuẩn (Standard Streams): STDOUT (Standard Output - dòng ra chuẩn, mặc định là màn hình), STDIN (Standard Input - dòng vào chuẩn, mặc định là bàn phím) và STDERR (Standard Error - dòng lỗi chuẩn, mặc định in lỗi ra màn hình).
- **Source:** (vv10 - Section: Review: Redirecting Streams - Các khái niệm chính)
- **Tag:** [vv10]

- **Fact:** Các ký hiệu điều hướng (Redirect) luồng dữ liệu bao gồm: `>` (ghi đè STDOUT vào file), `>>` (ghi thêm/append STDOUT vào cuối file), `<` (lấy nội dung file làm STDIN) và `2>` (điều hướng luồng lỗi STDERR vào file).
- **Source:** (vv10 - Section: Review: Redirecting Streams - Tóm tắt các lệnh redirect)
- **Tag:** [vv10]

- **Fact:** Mỗi luồng dữ liệu trong hệ thống được gán một số hiệu (File Descriptor): STDIN là số 0, STDOUT là số 1 và STDERR là số 2.
- **Source:** (vv10 - Section: Review: Redirecting Streams - Một điểm cực kỳ quan trọng)
- **Tag:** [vv10]

- **Fact:** Lệnh Pipe (`|`) được sử dụng để kết nối các chương trình bằng cách truyền kết quả đầu ra (STDOUT) của lệnh đứng trước làm đầu vào (STDIN) cho lệnh kế tiếp.
- **Source:** (vv10 - Section: Review: Pipes and Pipelines - Các khái niệm chính)
- **Tag:** [vv10]

- **Fact:** Một chuỗi pipeline phức tạp kết hợp các lệnh Linux như `cat`, `tr` (thay thế ký tự), `sort` (sắp xếp), `uniq -c` (đếm các dòng trùng lặp) và `head` có thể được dùng để phân tích tần suất xuất hiện của từ trong văn bản.
- **Source:** (vv10 - Section: Review: Pipes and Pipelines - Ví dụ xử lý dữ liệu dạng pipeline nhiều bước)
- **Tag:** [vv10]

- **Fact:** Trong Python, thư viện `sys` cho phép script đọc dữ liệu trực tiếp từ luồng vào chuẩn thông qua đối tượng `sys.stdin`, giúp script có thể nhận dữ liệu từ các pipeline hoặc file điều hướng.
- **Source:** (vv10 - Section: Review: Pipes and Pipelines - File capitalize.py)
- **Tag:** [vv10]

- **Fact:** Để một file script Python có thể chạy trực tiếp trong terminal Linux bằng cú pháp `./filename.py`, file đó cần được cấp quyền thực thi thông qua lệnh `chmod +x [tên_file]`.
- **Source:** (vv10 - Section: 4. Đảm bảo file Python có quyền thực thi)
- **Tag:** [vv10]

- **Fact:** Tín hiệu SIGINT (Interrupt) được gửi đến một tiến trình đang chạy khi người dùng nhấn tổ hợp phím `Ctrl+C`, khiến tiến trình đó dừng lại ngay lập tức.
- **Source:** (vv10 - Section: Review: Signaling Processes - Nhấn Control C)
- **Tag:** [vv10]

- **Fact:** Tổ hợp phím `Ctrl+Z` gửi tín hiệu SIGTSTP (Terminal Stop) đến tiến trình, khiến nó tạm dừng và chuyển vào trạng thái chạy nền (background). Lệnh `fg` (foreground) được dùng để gọi tiến trình này quay lại chạy ở nền trước.
- **Source:** (vv10 - Section: Review: Signaling Processes - Nhấn Control Z & Gọi tiến trình trở lại foreground)
- **Tag:** [vv10]

- **Fact:** Triết lý của hệ thống Linux/Unix là "mỗi chương trình chỉ làm tốt một việc" (programs do one thing well), và Pipeline chính là công cụ để kết nối các công cụ nhỏ đó thành một dây chuyền xử lý dữ liệu mạnh mẽ.
- **Source:** (vv10 - Section: Mục đích của bài này là gì? pipes and pipelines)
- **Tag:** [vv10]