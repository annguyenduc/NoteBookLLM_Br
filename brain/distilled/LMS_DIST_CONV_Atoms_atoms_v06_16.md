---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v06_16
  title: atoms_v06_16
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn Dữ liệu Raw (Volume v06) theo quy tắc LOM v4.1:

- **Fact:** Kiến trúc phần mềm IoT hiệu quả yêu cầu tách biệt hoàn toàn giữa "Logic" (thuần Python) và "HAL" (Hardware Abstraction Layer - lớp truy cập phần cứng) để có thể kiểm thử trên Desktop trước khi nạp xuống thiết bị.
- **Source:** [vv06] - Section: Rules cho Cursor IDE (.cursorrules)
- **Tag:** [vv06]

- **Fact:** Trên chip ESP8266, chân GPIO2 thường được sử dụng cho LED tích hợp (LED_BUILTIN) và thường hoạt động theo logic đảo (giá trị 1 là TẮT, giá trị 0 là BẬT).
- **Source:** [vv06] - File: `app/hal/esp_hal.py`
- **Tag:** [vv06]

- **Fact:** MicroPython cung cấp thư viện `machine` để điều khiển phần cứng (như `machine.Pin`) và thư viện `time` với hàm `sleep_ms()` để tạo độ trễ tính bằng miligiây.
- **Source:** [vv06] - File: `app/hal/esp_hal.py`
- **Tag:** [vv06]

- **Fact:** Sử dụng `Protocol` từ thư viện `typing` hoặc `ABC` (Abstract Base Class) cho phép định nghĩa giao diện HAL chung, giúp code logic có thể tương tác với cả phần cứng thật (`ESPHAL`) và mô phỏng (`MockHAL`).
- **Source:** [vv06] - File: `app/hal/base.py` & `app/core/controller.py`
- **Tag:** [vv06]

- **Fact:** Công cụ `mpremote` hỗ trợ quy trình phát triển MicroPython thông qua các lệnh kết nối, cài đặt gói (`mip install`), sao chép file (`fs cp`) và khởi động lại thiết bị (`reset`) từ dòng lệnh.
- **Source:** [vv06] - Section: 3) Tác vụ nhanh trong Cursor (tasks.json)
- **Tag:** [vv06]

- **Fact:** Quy trình "Desktop-first Workflow" trong lập trình nhúng khuyến nghị: Viết logic -> Chạy Mock trên Desktop -> Chạy Unit Test (PyTest) -> Cập nhật HAL cho phần cứng -> Upload lên thiết bị thật.
- **Source:** [vv06] - Section: 5) Quy trình hằng ngày (tóm tắt)
- **Tag:** [vv06]

- **Fact:** Để tối ưu hóa cho MicroPython trên thiết bị có tài nguyên hạn chế, cần hạn chế việc cấp phát bộ nhớ trong vòng lặp để giảm tần suất dọn rác (Garbage Collection - GC).
- **Source:** [vv06] - Section: 4) Rules cho Cursor IDE (MicroPython Constraints)
- **Tag:** [vv06]

- **Fact:** Các thư viện nặng của Python Desktop (như pandas, requests chuẩn) không tương thích với MicroPython; thay vào đó phải dùng các phiên bản rút gọn như `urequests` hoặc `umqtt.simple`.
- **Source:** [vv06] - Section: 4) Rules cho Cursor IDE (MicroPython Constraints)
- **Tag:** [vv06]