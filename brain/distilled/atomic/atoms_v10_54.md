Dưới đây là các sự kiện (Facts) về kỹ năng lập trình Python và thiết lập môi trường (nền tảng cho AI/Robotics) được trích xuất từ dữ liệu cung cấp:

- **Fact:** Để thực thi một script Python trực tiếp bằng lệnh `./filename.py` trên Linux/WSL, file phải chứa dòng shebang (ví dụ: `#!/usr/bin/env python3`) ở dòng đầu tiên và được cấp quyền thực thi qua lệnh `chmod +x`.
- **Source:** [v10 - Section: 3️⃣ Kiểm tra nội dung file]
- **Tag:** [vv10]

- **Fact:** Lỗi "cannot execute: required file not found" khi chạy script trên WSL thường do file đang ở định dạng DOS (CRLF); có thể khắc phục bằng cách chuyển sang định dạng Unix (LF) bằng công cụ `dos2unix`.
- **Source:** [v10 - Section: 4️⃣ Kiểm tra lỗi đường dẫn (dành cho WSL)]
- **Tag:** [vv10]

- **Fact:** Module `subprocess` trong Python được sử dụng để chạy các lệnh hệ thống, quản lý các chương trình con (process) và tương tác với các lệnh shell (như `ls`, `date`, `grep`) từ bên trong mã nguồn Python.
- **Source:** [v10 - Section: subprocess là gì]
- **Tag:** [vv10]

- **Fact:** Thuộc tính `returncode` trong module `subprocess` đại diện cho mã trạng thái kết thúc của một process; giá trị `0` biểu thị thành công, trong khi các giá trị khác `0` báo hiệu chương trình gặp lỗi.
- **Source:** [v10 - Section: returncode là gì]
- **Tag:** [vv10]

- **Fact:** Trong môi trường terminal Linux, lệnh `cat` (concatenate) dùng để hiển thị hoặc ghép nối nội dung file, trong khi `nano` là một trình soạn thảo văn bản (Text Editor) cho phép chỉnh sửa nội dung file trực tiếp.
- **Source:** [v10 - Section: cat khác gì so với nano]
- **Tag:** [vv10]

- **Fact:** Để xử lý lỗi hiển thị hoặc giải mã ký tự Unicode (tiếng Việt) trong terminal WSL, cần cài đặt gói `locales` và thiết lập biến môi trường hệ thống sang `en_US.UTF-8` hoặc `C.UTF-8`.
- **Source:** [v10 - Section: Bước 2: Cài đặt locale UTF-8 / Cách 3: Dùng LANG=C.UTF-8]
- **Tag:** [vv10]

- **Fact:** Biến môi trường `PYTHONUTF8=1` có thể được sử dụng để ép buộc Python sử dụng mã hóa UTF-8 cho các thao tác nhập/xuất dữ liệu, giúp khắc phục lỗi `UnicodeDecodeError`.
- **Source:** [v10 - Section: Cách 2: Chạy script với mã hóa UTF-8]
- **Tag:** [vv10]

- **Fact:** Phương thức `.split