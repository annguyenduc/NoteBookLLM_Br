Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu v01 liên quan đến IoT, Arduino (Yolo UNO), Robotics và AI:

- Fact: [CONV] Mô hình Teachable Machine (TM) chạy trên trình duyệt (TensorFlow.js) vì Yolo UNO không đủ tài nguyên để chạy trực tiếp mô hình này.
- Source: [v01 - Section: Vì sao cần HTML (trang web chạy cục bộ)?]
- Tag: [vv01]

- Fact: [CONV] Trang HTML/JavaScript đóng vai trò là "ứng dụng cầu nối" để chạy mô hình AI trên máy tính và gửi kết quả xuống UNO qua giao thức Web Serial.
- Source: [v01 - Section: Vì sao cần HTML (trang web chạy cục bộ)?]
- Tag: [vv01]

- Fact: [CONV] Dữ liệu truyền từ trình duyệt xuống UNO qua cổng Serial có định dạng chuỗi cấu trúc: `TM:<label>:<score>\n`.
- Source: [v01 - Section: Vì sao cần HTML (trang web chạy cục bộ)?]
- Tag: [vv01]

- Fact: [CONV] Trên Dashboard IoT OhStem, kênh V1 thường dùng hiển thị nhãn (chuỗi), V2 dùng cho điểm tin cậy dạng phần trăm (0-100), và V3 dùng cho điểm thập phân (chuỗi).
- Source: [v01 - Section: 2) Dashboard không có Gauge thập phân → giải pháp hiển thị]
- Tag: [vv01]

- Fact: [CONV] Để chống spam và giảm tải cho server IoT, chỉ nên gửi dữ liệu khi nhãn thay đổi hoặc điểm số biến động vượt ngưỡng (ví dụ > 0.05).
- Source: [v01 - Section: 3) Gợi ý block cụ thể cho phần gửi]
- Tag: [vv01]

- Fact: [CONV] Giải pháp chạy AI cục bộ (HTML + UNO) giúp giảm độ trễ cho các hành động phần cứng (LED, servo) vì không phụ thuộc vào tốc độ phản hồi của server cloud.
- Source: [v01 - Section: Cốt lõi khác nhau]
- Tag: [vv01]

- Fact: [CONV] Camera AI V2 của OhStem tích hợp sẵn khả năng kết nối Wi-Fi và gửi kết quả nhận dạng trực tiếp lên server IoT thông qua cấu hình username và kênh dữ liệu (V1-V20).
- Source: [v01 - Section: 1) Dùng camera AI của OhStem gửi thẳng lên server IoT]
- Tag: [vv01]

- Fact: [CONV] Điện thoại di động có thể dùng làm nguồn hình ảnh (webcam) cho máy tính chạy AI thông qua các ứng dụng trung gian như DroidCam.
- Source: [v01 - Section: 1) Điện thoại chỉ là “webcam” cho máy tính chạy AI]
- Tag: [vv01]

- Fact: [CONV] Các module camera AI bên ngoài (như Grove Vision AI V2) không tự động tương thích với app OhStem và yêu cầu lập trình thủ công để giao tiếp qua UART, I2C hoặc Wi-Fi.
- Source: [v01 - Section: Nếu không mua camera AI của ohstem mà tự mua bên ngoài]
- Tag: [vv01]

- Fact: [CONV] Yolo UNO (ESP32-S3) hỗ trợ triển khai các mô hình TinyML (TensorFlow Lite Micro) cho dữ liệu cảm biến hoặc âm thanh với yêu cầu bộ nhớ RAM thấp (≤10-20 KB).
- Source: [v01 - Section: Pattern A — TinyML on UNO]
- Tag: [vv01]

- Fact: [CONV] Việc lập trình UNO nhận dữ liệu Serial yêu cầu sử dụng bộ đệm (buffer) để đọc chuỗi cho đến khi gặp ký tự xuống dòng (\n) trước khi tách chuỗi (parse).
- Source: [v01 - Section: 4. Lập trình Yolo UNO nhận dữ liệu Serial và đẩy lên IoT]
- Tag: [vv01]

- Fact: [CONV] Chip ESP32-S3 trên Yolo UNO là nền tảng phù hợp cho các dự án Edge AI nhờ khả năng xử lý mạnh mẽ hơn các dòng Arduino truyền thống.
- Source: [Kiến thức bổ trợ từ ngữ cảnh thiết bị Yolo UNO]
- Tag: [Unverified_Source]