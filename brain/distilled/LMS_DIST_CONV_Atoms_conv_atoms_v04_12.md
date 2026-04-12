---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v04_12
  title: CONV_atoms_v04_12
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v04):

- **Fact:** [CONV] Cấu hình ADC trên ESP32 (MicroPython) để thu âm thanh sử dụng Pin 34 với độ suy giảm tín hiệu là 11dB (ATTN_11DB).
- **Source:** [v04 - Section: MicroPython Code - ADC setup]
- **Tag:** [vv04]

- **Fact:** [CONV] Servo SG90 hoạt động ở tần số 50Hz, dải xung từ 0.5ms đến 2.4ms tương ứng với giá trị `duty_u16` từ 1638 đến 7864 trong MicroPython.
- **Source:** [v04 - Section: def set_servo(deg)]
- **Tag:** [vv04]

- **Fact:** [CONV] Các đặc trưng (features) dùng để phân loại âm thanh cơ bản bao gồm RMS (giá trị hiệu dụng), Peak (đỉnh tín hiệu) và ZCR (tỷ lệ vượt ngưỡng không).
- **Source:** [v04 - Section: def read_features()]
- **Tag:** [vv04]

- **Fact:** [CONV] Cơ chế Hysteresis (trễ) giúp ổn định trạng thái AI bằng cách yêu cầu một số lượng mẫu liên tiếp (ví dụ: 4 mẫu ~ 0.8 giây) trước khi quyết định chuyển đổi trạng thái hệ thống.
- **Source:** [v04 - Section: Hysteresis]
- **Tag:** [vv04]

- **Fact:** [CONV] Việc triển khai Teachable Machine (TM) lên ESP32 đòi hỏi sử dụng TensorFlow Lite Micro, gây tốn bộ nhớ và tài nguyên hơn so với phương pháp cây quyết định (Decision Tree) chuyển đổi thành mã if-else.
- **Source:** [v04 - Section: Chọn cách nào cho hackathon 1 ngày?]
- **Tag:** [vv04]

- **Fact:** [CONV] Phương pháp "If-else tự học ngưỡng" thực hiện bằng cách thu thập giá trị Median của RMS/ZCR trong các pha hiệu chuẩn (Calibration) để tự động xác định ranh giới giữa các lớp âm thanh (Quiet/Talk/Loud).
- **Source:** [v04 - Section: Cách làm “if–else tự học ngưỡng”]
- **Tag:** [vv04]

- **Fact:** [CONV] Mẫu in 3D "Infinity Cube v2" được thiết kế theo dạng "print-in-place", cho phép các bản lề hoạt động ngay sau khi in mà không cần lắp ráp.
- **Source:** [v04 - Section: Tóm tắt nhanh - Infinity Cube]
- **Tag:** [vv04]

- **Fact:** [CONV] Đối với máy in Elegoo Neptune 4 (hệ thống Direct Drive), thông số Retraction (rút sợi) tối ưu thường nằm trong khoảng 0.6–1.2 mm với tốc độ 25–35 mm/s.
- **Source:** [v04 - Section: 4) Tốc độ, di chuyển (quan trọng với khớp in-liền)]
- **Tag:** [vv04]

- **Fact:** [CONV] Hiện tượng dính tơ (stringing) và đùn nhựa tại mũi in thường do nhiệt độ đầu phun quá cao, nhựa bị ẩm hoặc thông số Retraction chưa đủ; có thể khắc phục bằng cách giảm nhiệt độ 5°C hoặc tăng khoảng cách rút sợi.
- **Source:** [v04 - Section: Mực in đang mỏng bị dính tơ lại và đùn tại mũi in]
- **Tag:** [vv04]

- **Fact:** [CONV] Khi in lớp đầu tiên (Initial Layer), nên tắt quạt làm mát (0%), giảm tốc độ in xuống 20-30mm/s và tăng độ rộng đường in (Line Width) lên 120% để tăng độ bám dính bàn in.
- **Source:** [v04 - Section: 6) Lớp đầu & bám dính bàn]
- **Tag:** [vv04]