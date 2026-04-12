Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v14:

- **Fact:** [CONV] Để cài đặt môi trường Python, người dùng cần tải phiên bản phù hợp từ trang chủ python.org và bắt buộc chọn tùy chọn **"Add Python to PATH"** để có thể chạy lệnh từ Terminal/Command Prompt.
- **Source:** [vv14] - Section: 1. Cài đặt môi trường phát triển Python.
- **Tag:** [vv14]

- **Fact:** [CONV] Việc chạy một tệp Python từ dòng lệnh yêu cầu sử dụng lệnh `cd` để điều hướng đến thư mục chứa tệp, sau đó thực thi bằng lệnh `python tên_tệp.py`.
- **Source:** [vv14] - Section: 3. Chạy chương trình.
- **Tag:** [vv14]

- **Fact:** [CONV] Trong Visual Studio Code, để hỗ trợ lập trình Python, người dùng cần cài đặt **Python Extension** từ Microsoft và thiết lập **Python Interpreter** thông qua Command Palette (`Ctrl + Shift + P`).
- **Source:** [vv14] - Section: 2. Cài đặt Python Extension cho VS Code & 3. Cài đặt Python Interpreter.
- **Tag:** [vv14]

- **Fact:** [CONV] Để xác định vị trí tuyệt đối của một tệp đang chạy trong mã nguồn Python, có thể sử dụng thư viện `os` với câu lệnh `os.path.abspath(__file__)`.
- **Source:** [vv14] - Section: 3. In đường dẫn trong chương trình.
- **Tag:** [vv14]

- **Fact:** [CONV] Thư viện **Pygame** (thường dùng trong lập trình game và mô phỏng robot đơn giản) được cài đặt thông qua trình quản lý gói pip bằng lệnh `pip install pygame`.
- **Source:** [vv14] - Section: 1. Cài đặt Python và Pygame.
- **Tag:** [vv14]

- **Fact:** [CONV] Một thuật toán để tự động chọn màu chữ (đen hoặc trắng) dựa trên độ sáng của màu nền sử dụng công thức tính độ sáng: `brightness = (R * 299 + G * 587 + B * 114) / 1000`. Nếu giá trị > 128, màu nền được coi là sáng.
- **Source:** [vv14] - Section: Hàm xác định độ sáng của màu để chọn màu chữ.
- **Tag:** [vv14]

- **Fact:** [CONV] Trong lập trình giao diện Pygame, để căn giữa một đối tượng văn bản vào giữa một hình khối, ta sử dụng phương thức `get_rect(center=(x, y))` của đối tượng surface văn bản đó.
- **Source:** [vv14] - Section: Điểm đã chỉnh sửa (trong phần phản hồi về lỗi tràn chữ).
- **Tag:** [vv14]

- **Fact:** [CONV] IDLE là môi trường phát triển tích hợp sẵn khi cài đặt Python; trên Linux, nếu chưa có, có thể cài đặt bổ sung qua lệnh `sudo apt-get install idle3`.
- **Source:** [vv14] - Section: 3. Linux (trong phần hướng dẫn mở IDLE).
- **Tag:** [vv14]