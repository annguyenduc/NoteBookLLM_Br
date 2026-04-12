---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v04_12
  title: atoms_v04_12
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v04) liên quan đến IoT, Robotics, AI và kỹ thuật Maker:

- **Fact:** Cấu hình ADC trên ESP32 (MicroPython) sử dụng chân Pin(34) với độ suy giảm tín hiệu `ADC.ATTN_11DB` để mở rộng dải điện áp đo lường.
- **Source:** (v04 - Phần code MicroPython: ADC setup)
- **Tag:** [vv04]

- **Fact:** Động cơ Servo SG90 hoạt động ở tần số 50Hz, có dải xung từ 0.5ms đến 2.4ms, tương ứng với giá trị `duty_u16` từ khoảng 1638 đến 7864 khi lập trình trên vi điều khiển.
- **Source:** (v04 - Phần code MicroPython: def set_servo)
- **Tag:** [vv04]

- **Fact:** Các đặc trưng âm thanh cơ bản dùng để phân loại tiếng động bao gồm: RMS (Root Mean Square - giá trị hiệu dụng), Peak (biên độ đỉnh) và ZCR (Zero Crossing Rate - tỷ lệ vượt điểm không).
- **Source:** (v04 - Phần code MicroPython: def read_features)
- **Tag:** [vv04]

- **Fact:** Thuật toán cây quyết định (Decision Tree) có thể được triển khai dưới dạng các câu lệnh `if-else` lồng nhau để phân loại trạng thái âm thanh (QUIET, TALK, LOUD) trực tiếp trên thiết bị nhúng (on-device AI).
- **Source:** (v04 - Phần code MicroPython: def predict)
- **Tag:** [vv04]

- **Fact:** Kỹ thuật Hysteresis (trễ) giúp ổn định trạng thái điều khiển bằng cách yêu cầu một số lượng mẫu liên tiếp (ví dụ: 4 mẫu tương đương ~0.8 giây) khớp với dự đoán mới trước khi thực hiện chuyển đổi trạng thái.
- **Source:** (v04 - Phần code MicroPython: Hysteresis)
- **Tag:** [vv04]

- **Fact:** Việc triển khai Teachable Machine (TM) trên ESP32 đòi hỏi sử dụng TensorFlow Lite Micro, yêu cầu quản lý bộ nhớ tĩnh chặt chẽ và tiền xử lý dữ liệu audio (như MFCC hoặc spectrogram).
- **Source:** (v04 - Phần Teachable Machine (TM) cho âm thanh)
- **Tag:** [vv04]

- **Fact:** Thiết kế "Print-in-place" trong in 3D cho phép tạo ra các cơ cấu cơ khí (như bản lề của Infinity Cube) hoạt động được ngay sau khi in mà không cần lắp ráp thủ công.
- **Source:** (v04 - Phần Tóm tắt nhanh Infinity Cube)
- **Tag:** [vv04]

- **Fact:** Đối với máy in 3D sử dụng hệ thống đùn trực tiếp (Direct-drive) như Elegoo Neptune 4, khoảng cách rút sợi (Retraction Distance) tối ưu thường nằm trong khoảng 0.6mm đến 1.2mm.
- **Source:** (v04 - Phần 4: Tốc độ, di chuyển)
- **Tag:** [vv04]

- **Fact:** Nhựa Creality EN-PLA có dải nhiệt độ in khuyến nghị từ 195°C đến 220°C; hiện tượng dính tơ (stringing) có thể khắc phục bằng cách giảm nhiệt độ in hoặc tăng tốc độ di chuyển (Travel Speed) lên mức 200-250mm/s.
- **Source:** (v04 - Phần Thông số tốt nhất & Troubleshooting)
- **Tag:** [vv04]

- **Fact:** Kỹ thuật "Coasting" trong in 3D giúp giảm hiện tượng ứ đùn tại điểm kết thúc đường in bằng cách ngắt lực đùn sớm một khoảng nhỏ (ví dụ: 0.08–0.16 mm³) trước khi kết thúc nét vẽ.
- **Source:** (v04 - Phần 2: Chỉnh chi tiết để cắt tơ)
- **Tag:** [vv04]