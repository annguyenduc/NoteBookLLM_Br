---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v03_3
  title: atoms_v03_3
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (v03) về IoT, AI và phần cứng Yolo UNO/YoloBit:

**1. Cấu tạo phần cứng Yolo UNO**
- Fact: Yolo UNO là bo mạch vi điều khiển IoT dựa trên chip ESP8266 (ESP-12F), kiến trúc 32-bit, hỗ trợ Wi-Fi 2.4 GHz và có bộ nhớ Flash 4 MB.
- Source: [v03 - Section: 🧩 1. Yolo UNO được làm từ gì?]
- Tag: [vv03]

**2. Giao tiếp và mở rộng trên Yolo UNO**
- Fact: Mạch tích hợp chip chuyển đổi USB-UART CH340G và các cổng kết nối Grove 4-pin (SDA/SCL/VCC/GND) giúp kết nối cảm biến theo dạng Plug-and-Play.
- Source: [v03 - Section: 🧩 1. Yolo UNO được làm từ gì?]
- Tag: [vv03]

**3. Phương pháp nhận diện vật thể cho Yolo UNO**
- Fact: Do không có camera tích hợp, Yolo UNO thực hiện nhận diện vật thể gián tiếp bằng cách nhận nhãn (label) từ điện thoại hoặc máy tính thông qua giao thức MQTT (broker: broker.hivemq.com) hoặc HTTP.
- Source: [v03 - Section: A) Dùng thiết bị khác để nhận diện, Yolo UNO chỉ nhận kết quả]
- Tag: [vv03]

**4. Lấy thời gian thực qua Wi-Fi (NTP)**
- Fact: Để lấy giờ thực trên Yolo UNO có Wi-Fi, cần cấu hình NTP server (pool.ntp.org) và thiết lập độ lệch múi giờ cho Việt Nam là 25200 giây (GMT+7).
- Source: [v03 - Section: Cách 1 — Dùng khối NTP (đơn giản & chuẩn nhất)]
- Tag: [vv03]

**5. Lấy thời gian thực bằng phần cứng (RTC)**
- Fact: Trong điều kiện không có Wi-Fi, Yolo UNO sử dụng module RTC DS3231 kết nối qua giao tiếp I2C (chân SDA/SCL) để duy trì thời gian bằng pin dự phòng.
- Source: [v03 - Section: 🕐 1. Không có Wi-Fi: dùng module RTC (DS1307 / DS3231)]
- Tag: [vv03]

**6. Tối ưu hóa mô hình AI (Detection)**
- Fact: Để tăng tốc độ xử lý (inference), nên giảm kích thước ảnh đầu vào xuống mức 224–320px và sử dụng các dòng mô hình nhẹ như MobileNet hoặc YOLO bản Nano.
- Source: [v03 - Section: Lời khuyên dữ liệu & đánh giá (rất quan trọng)]
- Tag: [vv03]

**7. Kỹ thuật tăng cường dữ liệu (Augmentation)**
- Fact: Augmentation trong huấn luyện AI bao gồm các thao tác: xoay, lật, làm mờ nhẹ (blur), và thay đổi độ sáng/tương phản để mô hình nhận diện tốt hơn trong nhiều bối cảnh.
- Source: [v03 - Section: Lời khuyên dữ liệu & đánh giá (rất quan trọng)]
- Tag: [vv03]

**8. Triển khai TinyML "on-device"**
- Fact: Có thể chạy mô hình AI trực tiếp bằng cách kết nối ESP32-CAM (đã nạp model TensorFlow Lite Micro từ Edge Impulse) với Yolo UNO qua giao tiếp UART hoặc I2C.
- Source: [v03 - Section: B) TinyML “on-device” (chỉ khi bạn có camera/SoC phù hợp)]
- Tag: [vv03]

**9. Nền tảng lập trình**
- Fact: Yolo UNO tương thích với hệ sinh thái OhStem, cho phép lập trình bằng kéo thả khối (Blockly) tại app.ohstem.vn hoặc viết mã nguồn bằng MicroPython/Arduino IDE.
- Source: [v03 - Section: 🧩 1. Yolo UNO được làm từ gì?]
- Tag: [vv03]

**10. Thông tin thị trường và giá thành**
- Fact: Giá bán lẻ của mạch Yolo UNO tại thị trường Việt Nam dao động trong khoảng từ 270.000 ₫ đến 341.000 ₫.
- Source: [v03 - Section: ASSISTANT (Giá của yolo uno bao nhiêu tiền)]
- Tag: [vv03]