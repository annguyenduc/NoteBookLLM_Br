Dưới đây là các sự kiện (Facts) kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v10) liên quan đến kỹ năng lập trình Python và quản trị hệ thống Linux/WSL - nền tảng quan trọng cho AI và Robotics:

- **Fact:** [CONV] Để chạy trực tiếp một script Python trong môi trường Linux/WSL bằng lệnh `./filename.py`, file đó bắt buộc phải có dòng shebang (ví dụ: `#!/usr/bin/env python3`) ở dòng đầu tiên và được cấp quyền thực thi bằng lệnh `chmod +x`.
- **Source:** [ASSISTANT - Section: 2. Kiểm tra quyền thực thi của file & 3. Kiểm tra nội dung file]
- **Tag:** [vv10]

- **Fact:** [CONV] Lỗi "cannot execute: required file not found" trên WSL thường do file được lưu ở định dạng Windows (CRLF) thay vì Unix (LF). Cách khắc phục là sử dụng công cụ `dos2unix` để chuyển đổi định dạng file.
- **Source:** [ASSISTANT - Section: 4. Kiểm tra lỗi đường dẫn (dành cho WSL)]
- **Tag:** [vv10]

- **Fact:** [CONV] Trong Python, việc chuẩn hóa chuỗi văn bản thường kết hợp các phương thức: `.strip()` (xóa khoảng trắng đầu cuối), `.split()` (tách từ), và `.title()` (viết hoa chữ cái đầu mỗi từ).
- **Source:** [ASSISTANT - Section: Bài 1: Chuẩn hóa tên]
- **Tag:** [vv10]

- **Fact:** [CONV] Để xử lý lỗi hiển thị hoặc nhập liệu ký tự Unicode (như tiếng Việt) trong terminal WSL, cần cấu hình locale của hệ thống sang `en_US.UTF-8` thông qua các lệnh `locale-gen` và thiết lập biến môi trường `LANG`, `LC_ALL`.
- **Source:** [ASSISTANT - Section: Cách khắc phục lỗi Unicode & Bước 2: Cài đặt locale UTF-8]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `cat` trong Linux được dùng để hiển thị hoặc ghép nối nội dung file ra terminal, trong khi `nano` là một trình soạn thảo văn bản (Text Editor) cho phép chỉnh sửa nội dung file trực tiếp.
- **Source:** [ASSISTANT - Section: cat khác gì so với nano]
- **Tag:** [vv10]

- **Fact:** [CONV] Module `subprocess` trong Python cung cấp hàm `subprocess.run()` để thực thi các lệnh của hệ điều hành (như `ls`, `date`) và quản lý các tiến trình con (child processes).
- **Source:** [ASSISTANT - Section: subprocess là gì]
- **Tag:** [vv10]

- **Fact:** [CONV] Giá trị `returncode` từ một tiến trình được thực thi qua `subprocess` cho biết trạng thái kết thúc: giá trị `0` đại diện cho việc thực thi thành công, các giá trị khác `0` báo hiệu lỗi.
- **Source:** [ASSISTANT - Section: returncode là gì]
- **Tag:** [vv10]

- **Fact:** [CONV] Thiết lập biến môi trường `PYTHONUTF8=1` giúp ép buộc Python sử dụng mã hóa UTF-8 cho các luồng nhập/xuất dữ liệu (stdin/stdout), giúp tránh lỗi `UnicodeDecodeError`.
- **Source:** [ASSISTANT - Section: Cách 2: Chạy script với mã hóa UTF-8]
- **Tag:** [vv10]