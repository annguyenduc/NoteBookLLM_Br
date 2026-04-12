Chào bạn, tôi là @scout. Dựa trên nguồn dữ liệu **Volume v02** và các thông tin bổ sung từ quá trình thảo luận, tôi xin trích xuất các sự kiện kỹ thuật (Facts) theo quy tắc LOM v4.1 như sau:

### 1. Nhóm Fact về Xử lý dữ liệu & AI (TinyML)
- **Fact:** Hiệu chỉnh (calibrate) cảm biến giúp mô hình AI học được đặc trưng thực tế thay vì lỗi hệ thống.
  - **Source:** v02 - Section: Dữ liệu đầu vào
  - **Tag:** [vv02]
- **Fact:** Trích xuất đặc trưng (Feature Extraction) như MFCC (âm thanh) hoặc FFT (rung động) giúp giảm khối lượng tính toán và nhiễu so với việc dùng dữ liệu thô.
  - **Source:** v02 - Section: Trích xuất đặc trưng (L98-L106)
  - **Tag:** [vv02]
- **Fact:** Tăng cường dữ liệu (Data Augmentation) bằng cách thêm nhiễu nhân tạo hoặc thay đổi góc chụp giúp mô hình bền bỉ (robust) hơn và tránh overfit.
  - **Source:** v02 - Section: Tăng cường dữ liệu
  - **Tag:** [vv02]
- **Fact:** Chip ESP32-S3 trên Yolo UNO hỗ trợ tập lệnh vector tăng tốc AI thông qua thư viện ESP-NN và ESP-DSP, giúp xử lý ma trận nhanh hơn CPU thuần.
  - **Source:** v02 - Section: Tận dụng tăng tốc phần cứng (L222-L228)
  - **Tag:** [vv02]
- **Fact:** Edge Impulse cung cấp công cụ EON Tuner để tìm cấu hình mô hình AI tối ưu nhất cho tài nguyên phần cứng của vi điều khiển.
  - **Source:** v02 - Section: Công cụ, thư viện (L249-L258)
  - **Tag:** [vv02]

### 2. Nhóm Fact về Truyền thông IoT & Hiệu suất
- **Fact:** Giao thức MQTT nhanh hơn HTTP REST từ 20–25 lần trong việc truyền dữ liệu IoT liên tục trên ESP32.
  - **Source:** v02 - Section: Sử dụng giao thức nhẹ (L522-L530)
  - **Tag:** [vv02]
- **Fact:** Đóng gói dữ liệu dạng CSV (chuỗi ngắn) thay vì JSON giúp giảm kích thước gói tin đáng kể (ví dụ từ 27 byte xuống 6 byte).
  - **Source:** v02 - Section: Đóng gói và nén dữ liệu
  - **Tag:** [vv02]
- **Fact:** ESP-NOW là giao thức không dây riêng của Espressif cho phép các chip ESP32 truyền dữ liệu trực tiếp cho nhau rất nhanh mà không cần qua tầng TCP/IP.
  - **Source:** v02 - Section: Lựa chọn công nghệ truyền
  - **Tag:** [vv02]
- **Fact:** ESP32-S3 sở hữu lõi phụ ULP (Ultra-low-power) có thể theo dõi cảm biến khi CPU chính đang ở chế độ Deep Sleep.
  - **Source:** v02 - Section: Quản lý năng lượng (L239-L244)
  - **Tag:** [vv02]
- **Fact:** Việc tách tác vụ AI và tác vụ truyền thông (WiFi/MQTT) sang hai lõi CPU khác nhau của ESP32 giúp tăng thông lượng và độ phản hồi hệ thống.
  - **Source:** v02 - Section: Sử dụng lõi kép và RTOS
  - **Tag:** [vv02]

### 3. Nhóm Fact về Tối ưu hóa trên app.ohstem.vn (Lập trình khối)
- **Fact:** Lọc mũ (Exponential Smoothing - EMA) với công thức `ema = α*mới + (1-α)*ema` giúp làm mịn dữ liệu cảm biến hiệu quả hơn lọc trung bình đơn giản.
  - **Source:** User Interaction - Section 1B
  - **Tag:** [Unverified_Source]
- **Fact:** Cơ chế Hysteresis (sử dụng 2 ngưỡng cao/thấp) giúp ngăn chặn tình trạng thiết bị đầu ra (như Relay) bị bật/tắt liên tục khi dữ liệu cảm biến dao động quanh một ngưỡng đơn.
  - **Source:** User Interaction - Section 2A
  - **Tag:** [Unverified_Source]
- **Fact:** Sử dụng khối lệnh "Mỗi ... ms" thay vì lệnh "Chờ (delay)" cho phép Yolo UNO thực hiện đa nhiệm (multitasking) giả lập trên giao diện lập trình khối.
  - **Source:** User Interaction - Section 3A
  - **Tag:** [Unverified_Source]

### 4. Nhóm Fact về Combo thiết bị & Chủ đề Hackathon
- **Fact:** Các thiết bị Input phổ biến trong Hackathon bao gồm: Cảm biến ánh sáng (LDR), Siêu âm (HC-SR04), DHT20 (Nhiệt độ/Độ ẩm), và Nút nhấn.
  - **Source:** User Interaction - Section 1 (Input)
  - **Tag:** [Unverified_Source]
- **Fact:** Các thiết bị Output phổ biến bao gồm: LED đơn, LED RGB, Servo, Relay, LCD 1602, và Động cơ DC.
  - **Source:** User Interaction - Section 2 (Output)
  - **Tag:** [Unverified_Source]
- **Fact:** Combo "Siêu âm + Servo" thường được ứng dụng trong các chủ đề về **An toàn** hoặc **Giao thông** (ví dụ: Cửa tự động, Barie thông minh).
  - **Source:** User Interaction - Section 3 & 4
  - **Tag:** [Unverified_Source]
- **Fact:** Combo "DHT20 + Quạt DC/Relay" là giải pháp điển hình cho chủ đề **Môi trường** hoặc **Nông nghiệp** (ví dụ: Hệ thống làm mát, tưới tiêu tự động).
  - **Source:** User Interaction - Chủ đề: Môi trường
  - **Tag:** [Unverified_Source]
- **Fact:** Các chủ đề Hackathon rút gọn thường gặp: Môi trường, Y tế, Giáo dục, An toàn, Năng lượng, Giao thông.
  - **Source:** User Interaction - Chủ đề rút gọn
  - **Tag:** [Unverified_Source]

---
**Ghi chú:** Các thông tin từ [vv02] được trích xuất trực tiếp từ tài liệu bạn cung cấp. Các thông tin [Unverified_Source] được tổng hợp từ nội dung trao đổi để đảm bảo tính đầy đủ cho nhiệm vụ lập trình combo của bạn.