---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v03_5
  title: atoms_v03_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v03):

- **Fact:** Lỗi `ValueError: duty must be from 0 to 1023` phát sinh khi hàm `write_analog()` nhận giá trị nằm ngoài khoảng 0-1023 hoặc nhận giá trị không phải là số nguyên (float).
- **Source:** (v03 - Traceback log & Assistant Explanation)
- **Tag:** [vv03]

- **Fact:** Yolo UNO sử dụng chip ESP32S3, chạy phiên bản MicroPython v1.22.2 (phát hành ngày 06-03-2024).
- **Source:** (v03 - REPL Header)
- **Tag:** [vv03]

- **Fact:** Các chân hỗ trợ xuất tín hiệu PWM trên Yolo UNO bao gồm: D3, D5, D6, D9, D10, D11.
- **Source:** (v03 - Section: 5) Kiểm tra chân & phần cứng)
- **Tag:** [vv03]

- **Fact:** Chip ESP32S3 mặc định sử dụng ADC 12-bit, trả về giá trị cảm biến analog trong khoảng từ 0 đến 4095.
- **Source:** (v03 - Section: Thông số ADC của ESP32)
- **Tag:** [vv03]

- **Fact:** Trong giao diện REPL của MicroPython, tổ hợp phím `Ctrl + D` thực hiện lệnh "Soft reboot", giúp khởi động lại board và xóa các tác vụ (tasks/coroutines) đang chạy mà không cần ngắt nguồn.
- **Source:** (v03 - Section: 2) Các phím tắt quan trọng trong REPL)
- **Tag:** [vv03]

- **Fact:** Tổ hợp phím `Ctrl + B` dùng để thoát khỏi chế độ "raw REPL" để quay về chế độ nhập lệnh tương tác bình thường (interactive REPL).
- **Source:** (v03 - Section: 2) Các phím tắt quan trọng trong REPL)
- **Tag:** [vv03]

- **Fact:** Để tránh lỗi vượt ngưỡng 1023 khi chuyển đổi giá trị từ cảm biến (0-4095) sang PWM, công thức an toàn là sử dụng phép chia lấy phần nguyên cho 4096: `tmp = (light * 1023) // 4096`.
- **Source:** (v03 - Section: 3) Công thức an toàn)
- **Tag:** [vv03]

- **Fact:** Module Tiny RGB (WS2812/NeoPixel) kết nối với Yolo UNO qua 3 chân: VCC (5V), GND và DIN (Data). Chân D13 thường được khuyến nghị để kết nối chân DIN.
- **Source:** (v03 - Section: 2) Cắm dây với Yolo UNO)
- **Tag:** [vv03]

- **Fact:** Thư viện `neopixel` tích hợp sẵn trong MicroPython được sử dụng để điều khiển LED RGB địa chỉ trên Yolo UNO.
- **Source:** (v03 - Section: 3) Lập trình nhanh)
- **Tag:** [vv03]

- **Fact:** Khi sử dụng dải LED RGB dài với ESP32-S3, nên thêm điện trở 330 Ω nối tiếp trên đường dữ liệu (DATA) và tụ điện 1000 µF song song với nguồn 5V-GND để ổn định tín hiệu.
- **Source:** (v03 - Section: 2) Cắm dây với Yolo UNO)
- **Tag:** [vv03] [Unverified_Source] (Thông số linh kiện bổ trợ thường là kiến thức chuẩn ngành nhưng được Assistant bổ sung thêm).