---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v06_13
  title: atoms_v06_13
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu **Volume v06** theo quy tắc LOM v4.1:

- **Fact:** Lệnh để reset ESP8266 từ xa thông qua công cụ mpremote là: `mpremote connect <PORT> run "import machine; machine.reset()"`.
- **Source:** [vv06] - Section: ESP Setup/Troubleshooting
- **Tag:** [vv06]

- **Fact:** Khi gặp lỗi `failed to access COMxx`, các bước xử lý bao gồm: đóng ứng dụng đang chiếm cổng (Thonny/Serial Monitor), kiểm tra driver (CH340/CP210x), kiểm tra cáp USB và thêm user vào nhóm `dialout` trên Linux.
- **Source:** [vv06] - Section: ESP Setup/Troubleshooting
- **Tag:** [vv06]

- **Fact:** Mocking (giả lập) trên PC chỉ kiểm chứng được logic phần mềm (tốc độ logic, API); nó không thể kiểm tra các yếu tố phần cứng như điện áp (3.3V), nhiễu, driver, timing cứng (ISR), hay kết nối Wi-Fi/MQTT thật.
- **Source:** [vv06] - Section: Những gì mock không kiểm chứng
- **Tag:** [vv06]

- **Fact:** Quy trình học tập (Workflow) tiêu chuẩn cho mỗi Lab gồm 5 bước: Chạy Mock -> Nạp thật -> Ghi bằng chứng vào Learning Tracker -> Tự giải thích 60s (Feynman) -> Làm Mini-quiz.
- **Source:** [vv06] - Section: Lộ trình mỗi lab
- **Tag:** [vv06]

- **Fact:** NodeMCU v1.0 (Amica) thường sử dụng chip nạp CP2102 và có kích thước hẹp (vừa breadboard), trong khi NodeMCU v3 (LoLin) thường dùng chip CH340 và có kích thước rộng hơn.
- **Source:** [vv06] - Section: Xác định NodeMCU v bao nhiêu
- **Tag:** [vv06]

- **Fact:** LED on-board trên đa số các dòng NodeMCU thường nằm ở chân D4 (GPIO2) và hoạt động theo cơ chế **Active LOW** (mức logic 0 là BẬT, mức 1 là TẮT).
- **Source:** [vv06] - Section: Probe LED on-board & Lưu ý quan trọng
- **Tag:** [vv06]

- **Fact:** Trong cấu trúc file của MicroPython, `boot.py` được dùng để cấu hình hệ thống (Wi-Fi, log) và chạy trước, sau đó mới đến `main.py` chứa logic ứng dụng chính.
- **Source:** [vv06] - Section: Hiểu bằng Feynman
- **Tag:** [vv06]

- **Fact:** Để nạp file từ máy tính lên thư mục gốc của ESP8266 bằng command line, sử dụng cú pháp: `mpremote connect <PORT> fs cp <tên_file> :`.
- **Source:** [vv06] - Section: Nạp code lên esp8266 bằng command
- **Tag:** [vv06]

- **Fact:** Để dọn dẹp các cổng COM Bluetooth ảo chiếm dụng trên Windows, có thể sử dụng PowerShell (Admin) với lệnh `pnputil /remove-device` kết hợp với `InstanceId` của thiết bị.
- **Source:** [vv06] - Section: Cách 3 — Gỡ bằng PowerShell
- **Tag:** [vv06]

- **Fact:** Chân GPIO16 (D0) trên NodeMCU đôi khi cũng được sử dụng làm chân LED on-board trên một số phiên bản biến thể.
- **Source:** [vv06] - Section: Probe LED on-board
- **Tag:** [vv06]