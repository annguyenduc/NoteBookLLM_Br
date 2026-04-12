---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v01_1
  title: CONV_atoms_v01_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v01:

- **Fact:** [CONV] Khi thiết lập Horizontal Expansion = +0.125 mm trong phần mềm in 3D, biên XY sẽ dịch ra ngoài 0.125 mm mỗi phía, làm tăng kích thước ngoài thêm 0.25 mm và giảm kích thước lỗ/rãnh đi 0.25 mm.
- **Source:** v01 - Section: Conversation: Điều chỉnh bản vẽ 0.125
- **Tag:** [vv01]

- **Fact:** [CONV] Quy tắc bù trừ CAD khi in 3D với Horizontal Expansion +0.125 mm: Kích thước ngoài (CAD) = Mục tiêu - 0.25 mm; Kích thước trong (CAD) = Mục tiêu + 0.25 mm.
- **Source:** v01 - Section: Conversation: Điều chỉnh bản vẽ 0.125
- **Tag:** [vv01]

- **Fact:** [CONV] Trục nhựa trắng (trục encoder/phụ) của động cơ TT thường có đường kính thực tế là tròn Ø2.00 mm.
- **Source:** v01 - Section: Conversation: Điều chỉnh bản vẽ 0.125
- **Tag:** [vv01]

- **Fact:** [CONV] Để đạt kiểu "lắp vừa" (snug fit) cho lỗ rỗng hình chữ nhật khi in 3D (với Horizontal Expansion +0.125), kích thước CAD cần vẽ = Mục tiêu + 0.35 mm (bao gồm 0.25 mm bù co và 0.10 mm độ hở).
- **Source:** v01 - Section: Conversation: Điều chỉnh bản vẽ 0.125
- **Tag:** [vv01]

- **Fact:** [CONV] Kỹ thuật "dog-bone relief" (bo tròn góc nhỏ r ≈ 0.3–0.5 mm hướng chéo) tại 4 góc trong của lỗ rỗng giúp các chi tiết có góc vuông lắp vào dễ dàng hơn do đặc tính FDM luôn bo nhẹ góc trong.
- **Source:** v01 - Section: Conversation: Điều chỉnh bản vẽ 0.125
- **Tag:** [vv01]

- **Fact:** [CONV] TinyML (Tiny Machine Learning) là lĩnh vực triển khai các mô hình học máy đã tối ưu hóa lên các thiết bị nhúng có tài nguyên hạn chế như vi điều khiển (vài chục KB RAM).
- **Source:** v01 - Section: Giai đoạn 3 (Tháng 3): TinyML
- **Tag:** [vv01]

- **Fact:** [CONV] TensorFlow Lite for Microcontrollers (TFLM) là framework cho phép chạy mô hình AI trên vi điều khiển mà không cần hệ điều hành và không cần cấp phát bộ nhớ động.
- **Source:** v01 - Section: Giai đoạn 3 (Tháng 3): TinyML
- **Tag:** [vv01]

- **Fact:** [CONV] Edge Impulse là nền tảng trực tuyến hỗ trợ quy trình TinyML từ thu thập dữ liệu cảm biến, huấn luyện mô hình đến xuất thư viện C++ tối ưu cho các board như Arduino, ESP32.
- **Source:** v01 - Section: Giai đoạn 3 (Tháng 3): TinyML
- **Tag:** [vv01]

- **Fact:** [CONV] Lượng tử hóa (Quantization) là kỹ thuật nén mô hình AI (ví dụ xuống 8-bit) để giảm dung lượng và phù hợp với bộ nhớ của vi điều khiển trong ứng dụng TinyML.
- **Source:** v01 - Section: Giai đoạn 3 (Tháng 3): TinyML
- **Tag:** [vv01]

- **Fact:** [CONV] Các loại cảm biến phổ biến trong hệ thống nhúng bao gồm: DHT11/LM35 (nhiệt độ), HC-SR04 (siêu âm), PIR (chuyển động), MQ-2 (khí gas), MPU-6050 (gia tốc).
- **Source:** v01 - Section: Giai đoạn 1 (Tháng 1): Kiến thức nền tảng
- **Tag:** [vv01]

- **Fact:** [CONV] ESP32 là bo mạch vi điều khiển được khuyến nghị sử dụng thay cho Arduino Uno khi cần triển khai các mô hình AI nhúng nhờ hiệu năng cao hơn.
- **Source:** v01 - Section: Giai đoạn 1 (Tháng 1): Kiến thức nền tảng
- **Tag:** [vv01]