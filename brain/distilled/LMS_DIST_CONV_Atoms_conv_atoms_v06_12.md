---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v06_12
  title: CONV_atoms_v06_12
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là **@scout**. Dựa trên dữ liệu từ **Volume v06**, tôi xin trích xuất các sự kiện (Facts) quan trọng về khái niệm **Mock** và **Workflow** (quy trình làm việc) để bạn nắm rõ:

- Fact: [CONV] **Mock** là "bản đóng giả" của phần cứng (như Pin, PWM, Timer) được tạo ra bằng code Python để chạy và kiểm thử logic trên máy tính (PC) mà không cần cắm thiết bị thật.
- Source: [vv06 - Section: Mock là gì?]
- Tag: [vv06]

- Fact: [CONV] File `src/desktop/hw_mock.py` đóng vai trò giả lập các thư viện MicroPython (như `machine`) bằng cách in log ra màn hình (ví dụ: `[MOCK] Pin(2) <- 0`) thay vì điều khiển chân điện vật lý.
- Source: [vv06 - Section: Mock hoạt động thế nào & src/desktop/hw_mock.py]
- Tag: [vv06]

- Fact: [CONV] Quy trình phát triển (Workflow) chuẩn gồm 4 bước: **B1**-Chạy mock trên PC; **B2**-Viết unit test; **B3**-Tách file cho thiết bị (`boot.py`, `main.py`, `config.py`); **B4**-Nạp thật bằng `mpremote`.
- Source: [vv06 - Section: 4) Quy trình học trên Cursor]
- Tag: [vv06]

- Fact: [CONV] Việc sử dụng Mock giúp đồng nhất API: Code logic trong `src/desktop/boot_desktop.py` và `src/device/main.py` có thể dùng chung cấu trúc hàm, chỉ khác nhau ở nguồn import (từ `hw_mock` trên PC hoặc từ `machine` trên ESP8266).
- Source: [vv06 - Section: Mock hoạt động thế nào]
- Tag: [vv06]

- Fact: [CONV] Công cụ `mpremote` được sử dụng trong các script (`upload.ps1`, `upload.sh`) để sao chép file vào bộ nhớ flash của ESP8266 và thực hiện lệnh reset thiết bị từ xa.
- Source: [vv06 - Section: scripts/upload.ps1 & scripts/upload.sh]
- Tag: [vv06]

- Fact: [CONV] Lỗi truy cập cổng COM (`failed to access COMxx`) thường do các phần mềm khác (như Thonny, Serial Monitor) đang chiếm dụng cổng hoặc do thiếu driver (CH340/CP210x).
- Source: [vv06 - Section: Khắc phục sự cố]
- Tag: [vv06]

- Fact: [CONV] Trên hệ điều hành Linux, để nạp code thành công, người dùng cần được thêm vào nhóm `dialout` để có quyền truy cập cổng serial.
- Source: [vv06 - Section: scripts/upload.sh]
- Tag: [vv06]

- Fact: [CONV] Cấu trúc file trên thiết bị thật nên tách biệt: `boot.py` dành cho các tác vụ khởi động/kết nối Wi-Fi, còn `main.py` chứa vòng lặp logic chính của ứng dụng.
- Source: [vv06 - Section: B3 – Chuyển sang thiết bị]
- Tag: [vv06]

- Fact: [CONV] Để chạy Mock trên Cursor, người dùng sử dụng tổ hợp phím `Ctrl+Shift+B` và chọn nhiệm vụ "Run desktop mock" đã được định nghĩa trong `.vscode/tasks.json`.
- Source: [vv06 - Section: .vscode/tasks.json]
- Tag: [vv06]

**Ghi chú từ @scout:** Việc học qua Mock giúp bạn hiểu sâu về logic lập trình trước khi đối mặt với các lỗi vật lý (dây lỏng, cháy linh kiện). Khi log trên PC chạy đúng như ý muốn, việc nạp lên ESP8266 sẽ trở nên tự tin hơn rất nhiều.