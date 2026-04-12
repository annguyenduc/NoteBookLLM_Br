---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v01_2
  title: CONV_atoms_v01_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ tài liệu **Volume v01** về IoT, Arduino, AI nhúng và TinyML:

**1. Giới hạn phần cứng ESP32 trong xử lý AI**
- **Fact:** [CONV] ESP32 có hạn chế về tính toán nên không thể xử lý các hình ảnh kích thước lớn một cách nhanh chóng; tuy nhiên, thiết bị này hoạt động ổn định khi xử lý âm thanh hoặc dữ liệu từ các cảm biến đơn giản.
- **Source:** (v01 - Giai đoạn 3 - L403-L411)
- **Tag:** [vv01]

**2. Cấu hình mô hình nhận diện hình ảnh cho TinyML**
- **Fact:** [CONV] Để chạy nhận diện hình ảnh trên các thiết bị tài nguyên thấp như ESP32, cần sử dụng mô hình CNN nhỏ đã lượng tử hóa hoặc mô hình từ Edge Impulse với kích thước ảnh 96x96 (trắng đen).
- **Source:** (v01 - Giai đoạn 4 - L514-L522)
- **Tag:** [vv01]

**3. Ứng dụng AI trong cảnh báo cháy thông minh**
- **Fact:** [CONV] Hệ thống báo cháy AIoT kết hợp cảm biến khí gas (MQ-2) và cảm biến nhiệt độ có khả năng phát hiện nguy cơ cháy sớm hơn phương pháp so sánh ngưỡng truyền thống nhờ việc học từ dữ liệu giả lập.
- **Source:** (v01 - Giai đoạn 4 - L395-L398)
- **Tag:** [vv01]

**4. Nhận diện hành vi qua cảm biến gia tốc**
- **Fact:** [CONV] Các board mạch như Arduino BLE Sense có thể sử dụng dữ liệu từ cảm biến gia tốc để huấn luyện mô hình AI nhận biết các động tác như vẫy tay, lắc đầu hoặc phát hiện té ngã ở người già.
- **Source:** (v01 - Giai đoạn 4 - Nội dung trọng tâm mục 2)
- **Tag:** [vv01]

**5. Nhận dạng giọng nói tiếng Việt trên hệ nhúng**
- **Fact:** [CONV] Chip ESP32-S3 có khả năng hỗ trợ nhận diện từ đánh thức (wake-word) bằng tiếng Việt và phân biệt các lệnh đơn giản (ví dụ: "tới", "lùi", "dừng") để điều khiển robot.
- **Source:** (v01 - Giai đoạn 4 - L5-L12)
- **Tag:** [vv01]

**6. Thư viện và Framework hỗ trợ AI nhúng**
- **Fact:** [CONV] Các công cụ phổ biến để triển khai AI lên vi điều khiển bao gồm thư viện `Arduino_TensorFlowLite`, framework `ESP-WHO` (nhận diện khuôn mặt của Espressif) và `ESP-IDF ML`.
- **Source:** (v01 - Tài liệu/Hướng dẫn Giai đoạn 4)
- **Tag:** [vv01]

**7. Chiến lược tối ưu hóa mô hình TinyML**
- **Fact:** [CONV] Để tối ưu mô hình chạy trên phần cứng nhúng, người lập trình nên giảm số lớp (layers), chọn kiến trúc MobileNetV1 nhẹ hoặc chuyển một phần tính toán lên máy chủ (Cloud retraining).
- **Source:** (v01 - Lưu ý trong quá trình Giai đoạn 4)
- **Tag:** [vv01]

**8. Tích hợp Teachable Machine với Yolo UNO**
- **Fact:** [CONV] Do Yolo UNO không đủ tài nguyên chạy trực tiếp mô hình Teachable Machine (TFJS), giải pháp tối ưu là chạy mô hình trên trình duyệt máy tính và gửi kết quả dự đoán qua giao tiếp Serial (UART) để UNO đẩy lên IoT Dashboard.
- **Source:** (v01 - Conversation: Yolo UNO IoT integration)
- **Tag:** [Unverified_Source] (Thông tin này nằm trong phần hội thoại bổ sung, không thuộc text raw chính của lộ trình học nhưng có trong dữ liệu cung cấp).

**9. Lộ trình đào tạo kỹ sư nhúng AI**
- **Fact:** [CONV] Một người học có thể đạt trình độ kỹ sư nhúng AI mức độ Junior sau khoảng 4-6 tháng học bài bản về lập trình nhúng kết hợp AI và thực hiện các dự án thực tế.
- **Source:** (v01 - Thời gian và cơ hội nghề nghiệp - L407-L415)
- **Tag:** [vv01]