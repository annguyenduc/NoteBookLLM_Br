---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v03_4
  title: CONV_atoms_v03_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dựa trên dữ liệu từ **Volume v03** (bao gồm các đoạn hội thoại và log lỗi bạn cung cấp), tôi trích xuất các sự kiện kỹ thuật quan trọng để giải quyết vấn đề của bạn:

- **Fact:** [CONV] [Lỗi `ValueError: duty must be from 0 to 1023` xảy ra do giá trị truyền vào hàm `write_analog` (khối xuất analog) nằm ngoài khoảng 0 đến 1023.]
- **Source:** [vv03 - Section: Traceback log lỗi từ USER]
- **Tag:** [vv03]

- **Fact:** [CONV] [Yolo UNO sử dụng chip ESP32S3, chạy MicroPython v1.22.2; ADC (đọc analog) có độ phân giải 12-bit (0-4095) nhưng PWM (xuất analog) chỉ nhận dải 10-bit (0-1023).]
- **Source:** [vv03 - Section: Phân tích lỗi hệ thống]
- **Tag:** [vv03]

- **Fact:** [CONV] [Để lấy thời gian thực khi không có khối NTP, có thể sử dụng HTTP GET gọi đến `http://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh` và giải mã JSON.]
- **Source:** [vv03 - Section: Hướng dẫn HTTP/NTP]
- **Tag:** [vv03]

- **Fact:** [CONV] [Hàm `gc.collect()` thường được gọi trước khi thực hiện HTTP request để tối ưu bộ nhớ RAM trên vi điều khiển.]
- **Source:** [vv03 - Section: Dữ liệu RAW đầu tiên]
- **Tag:** [vv03]

---

### 🛠 GIẢI PHÁP DỨT ĐIỂM LỖI PWM CHO DỰ ÁN ĐÈN CỦA BẠN

Lý do bạn "chỉnh đúng công thức" nhưng vẫn lỗi là vì **chỉ cần 1 khoảnh khắc giá trị vọt lên 1024 hoặc xuống -1** (do nhiễu cảm biến hoặc làm tròn số), chương trình sẽ crash ngay lập tức.

Bạn hãy sửa lại các khối theo đúng thứ tự "Bọc lót 3 lớp" này:

1.  **Đọc giá trị:** `biến_ánh_sáng = đọc giá trị analog chân A0`
2.  **Tính toán & Ép kiểu (Lớp 1):** 
    *   `biến_tạm = (biến_ánh_sáng * 1023) / 4095`
    *   `biến_pwm = 1023 - làm_tròn(biến_tạm)` (Nếu muốn tối -> sáng đèn)
3.  **Kẹp biên an toàn (Lớp 2 - Quan trọng nhất):**
    *   Sử dụng khối Toán học: `biến_pwm = max(0, min(1023, biến_pwm))`
    *   *Giải thích:* Khối này đảm bảo dù `biến_pwm` có là 1024 hay -5 thì nó cũng bị ép về 1023 hoặc 0.
4.  **Xuất lệnh (Lớp 3):**
    *   `xuất ra giá trị analog (biến_pwm) cho chân D3`

**Tại sao log của bạn có dòng "Connected to broker"?**
Vì bạn đang dùng extension IoT/MQTT. Khi chương trình bị lỗi PWM, nó dừng toàn bộ "Task", dẫn đến việc kết nối MQTT cũng bị ngắt. Khi bạn sửa xong lỗi PWM, hệ thống sẽ chạy ổn định cả phần đèn và phần gửi dữ liệu lên dashboard.

Bạn hãy thử thêm khối **`max(0, min(1023, ...))`** vào ngay trước khối xuất analog, lỗi sẽ biến mất 100%.