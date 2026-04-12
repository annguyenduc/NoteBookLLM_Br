Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v06:

- **Fact:** [CONV] Lệnh `mpremote connect <PORT> run "import machine; machine.reset()"` được sử dụng để khởi động lại (reset) bo mạch ESP8266 từ xa qua terminal.
- **Source:** [v06 - Section: Setup]
- **Tag:** [vv06]

- **Fact:** [CONV] Khi gặp lỗi `failed to access COMxx`, các bước xử lý bao gồm: đóng ứng dụng đang chiếm cổng (Thonny/Serial Monitor), kiểm tra driver CH340/CP210x, kiểm tra cáp/cổng USB, và thêm user vào nhóm `dialout` trên Linux.
- **Source:** [v06 - Section: Setup]
- **Tag:** [vv06]

- **Fact:** [CONV] Phương pháp "Mocking" (chạy giả lập trên PC) chỉ giúp kiểm chứng tốc độ logic và API, không thể kiểm tra các yếu tố phần cứng như điện áp (3.3V), nhiễu, driver, cổng COM, hay các phản hồi thời gian thực (ISR/Timing cứng).
- **Source:** [v06 - Section: Mocking]
- **Tag:** [vv06]

- **Fact:** [CONV] Lộ trình Lab chuẩn bao gồm 5 bước: Chạy Mock -> Nạp thật -> Ghi bằng chứng vào Learning Tracker -> Giải thích Feynman 60s + Quiz -> Quay lại nếu sai.
- **Source:** [v06 - Section: Lab Workflow]
- **Tag:** [vv06]

- **Fact:** [CONV] NodeMCU v1.0 (Amica) thường sử dụng chip nạp CP2102 và có kích thước hẹp vừa breadboard; trong khi NodeMCU v3 (LoLin) thường dùng chip CH340 và có kích thước rộng hơn.
- **Source:** [v06 - Section: NodeMCU Identification]
- **Tag:** [vv06]

- **Fact:** [CONV] LED on-board trên đa số các dòng NodeMCU thường được kết nối với chân GPIO2 (D4) và hoạt động theo logic Active LOW (mức 0 là BẬT, mức 1 là TẮT).
- **Source:** [v06 - Section: NodeMCU Identification]
- **Tag:** [vv06]

- **Fact:** [CONV] Để kiểm tra thông tin phiên bản MicroPython đang chạy trên thiết bị, sử dụng lệnh: `mpremote connect <PORT> exec "import sys,os;print(sys.implementation);print(os.uname())"`.
- **Source:** [v06 - Section: Tools]
- **Tag:** [vv06]

- **Fact:** [CONV] Script `upload.ps1` thực hiện quy trình tự động hóa gồm: copy các file `boot.py`, `main.py`, `config.py` lên thư mục gốc của ESP8266 và thực hiện lệnh reset board.
- **Source:** [v06 - Section: Scripting]
- **Tag:** [vv06]

- **Fact:** [CONV] Trong VS Code/Cursor, tham số truyền từ `tasks.json` (ví dụ `-Port COM26`) sẽ ghi đè (override) giá trị biến mặc định được khai báo trong script PowerShell.
- **Source:** [v06 - Section: Scripting]
- **Tag:** [vv06]

- **Fact:** [CONV] Để dọn dẹp các cổng COM ảo do Bluetooth chiếm dụng trên Windows, có thể sử dụng lệnh `bthprops.cpl` để quản lý thiết bị hoặc dùng `pnputil /remove-device` trong PowerShell với quyền Admin để gỡ bỏ hàng loạt.
- **Source:** [v06 - Section: OS Cleanup]
- **Tag:** [vv06]

- **Fact:** [CONV] Chân GPIO16 (D0) là vị trí thay thế phổ biến của LED on-board trên một số biến thể bo mạch ESP8266 không theo chuẩn thông thường.
- **Source:** [v06 - Section: NodeMCU Identification]
- **Tag:** [vv06]

- **Fact:** [CONV] Việc kết nối LED ngoài nên ưu tiên các chân an toàn như D1 (GPIO5) hoặc D2 (GPIO4) để tránh gây xung đột với quá trình khởi động (boot) của chip ESP8266.
- **Source:** [v06 - Section: Hardware Tips]
- **Tag:** [Unverified_Source] (Thông tin bổ sung để đảm bảo an toàn kỹ thuật dựa trên ngữ cảnh chân nhạy boot trong text).