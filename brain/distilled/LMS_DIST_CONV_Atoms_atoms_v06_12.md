---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v06_12
  title: atoms_v06_12
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là **@scout**. Dựa trên nguồn dữ liệu **Volume v06** bạn cung cấp, tôi xin trích xuất các sự kiện kỹ thuật (Facts) để làm rõ khái niệm **Mock** và **Workflow** (quy trình làm việc) mà bạn đang thắc mắc:

- **Fact:** Mock là việc tạo ra các lớp (class) và hàm giả lập các thành phần phần cứng (như `Pin`, `PWM`, `Timer`) trong môi trường Python trên máy tính (Desktop) để kiểm thử logic mà không cần thiết bị thật.
- **Source:** `src/desktop/hw_mock.py`
- **Tag:** [vv06]

- **Fact:** Quy trình phát triển (Workflow) chuẩn trên Cursor gồm 4 bước: (B1) Chạy Mock trên Desktop để kiểm tra logic và xem log; (B2) Viết Unit Test nhỏ; (B3) Tách code thành các file `boot.py`, `main.py`, `config.py`; (B4) Nạp thật vào ESP8266 qua `mpremote`.
- **Source:** Mục 4: Quy trình học trên Cursor
- **Tag:** [vv06]

- **Fact:** Để đảm bảo code chạy được trên cả Desktop (Mock) và thiết bị thật (Real) mà không cần sửa đổi nhiều, lớp `Led` và các hàm như `read_temp()` được thiết kế với API (tên hàm, tham số) hoàn toàn giống nhau.
- **Source:** So sánh `src/desktop/boot_desktop.py` và `src/device/main.py`
- **Tag:** [vv06]

- **Fact:** Đèn LED tích hợp (on-board) trên ESP8266 (thường là chân D4/GPIO2) hoạt động theo cơ chế **Active LOW**, nghĩa là xuất giá trị `0` để BẬT và `1` để TẮT.
- **Source:** `src/device/main.py` (đoạn: `def on(self): self.pin.value(0) # thường active LOW`)
- **Tag:** [vv06]

- **Fact:** Công cụ `mpremote` thực hiện việc kết nối tới cổng COM/tty, sao chép file vào bộ nhớ flash của ESP8266 và thực hiện lệnh reset thiết bị từ xa (`machine.reset()`).
- **Source:** `scripts/upload.ps1` và `scripts/upload.sh`
- **Tag:** [vv06]

- **Fact:** File `boot.py` đóng vai trò khởi tạo hệ thống, thường dùng để thiết lập kết nối Wi-Fi (STA mode) trước khi chương trình chính (`main.py`) bắt đầu.
- **Source:** `src/device/boot.py`
- **Tag:** [vv06]

- **Fact:** Khi gặp lỗi `failed to access COMxx`, các bước xử lý bao gồm: đóng các ứng dụng đang chiếm cổng (Thonny, Serial Monitor), kiểm tra driver CH340/CP210x, hoặc thêm user vào nhóm `dialout` (trên Linux).
- **Source:** Ghi chú dưới mục `scripts/upload.sh`
- **Tag:** [vv06]

- **Fact:** Việc sử dụng `.vscode/tasks.json` cho phép người dùng kích hoạt nhanh các kịch bản nạp code hoặc chạy mock thông qua phím tắt `Ctrl+Shift+B` trong Cursor/VS Code.
- **Source:** `.vscode/tasks.json`
- **Tag:** [vv06]

- **Fact:** Dữ liệu cảm biến trong môi trường Mock (`read_fake_sensor`) được tạo ra bằng công thức toán học (hàm sin theo thời gian) để mô phỏng sự biến thiên của nhiệt độ thực tế.
- **Source:** `src/desktop/hw_mock.py` (hàm `read_fake_sensor`)
- **Tag:** [vv06]

- **Fact:** File `config.py` được dùng để tách biệt các thông số cấu hình (SSID, Password, Pin mapping) khỏi logic xử lý chính, giúp việc bảo trì và thay đổi thiết bị dễ dàng hơn.
- **Source:** `src/device/config.py`
- **Tag:** [vv06]