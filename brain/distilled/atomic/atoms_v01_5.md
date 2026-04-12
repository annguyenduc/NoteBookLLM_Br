Dưới đây là các sự kiện kỹ thuật được trích xuất từ nội dung cung cấp (Volume v01) về hệ sinh thái IoT, Arduino (Yolo UNO) và AI:

- **Fact:** Teachable Machine (TM) không thể chạy trực tiếp trên Yolo UNO do hạn chế tài nguyên; mô hình này chạy trên trình duyệt máy tính (TensorFlow.js) và gửi kết quả qua "cầu nối" HTML.
- **Source:** [Phần: Vì sao cần HTML (trang web chạy cục bộ)?]
- **Tag:** [vv01]

- **Fact:** Giao thức Web Serial cho phép trình duyệt (Chrome/Edge) gửi dữ liệu chuỗi (ví dụ: `TM:<label>:<score>\n`) trực tiếp xuống Yolo UNO qua cổng USB (COM).
- **Source:** [Phần: Vì sao cần HTML (trang web chạy cục bộ)?]
- **Tag:** [vv01]

- **Fact:** Trên Dashboard IoT OhStem, widget Gauge (Đồng hồ đo) thường hiển thị số nguyên (0-100); để hiển thị số thập phân (ví dụ 0.97), nên sử dụng widget Văn bản/Thông tin (Text).
- **Source:** [Phần: 2) Dashboard không có Gauge thập phân → giải pháp hiển thị]
- **Tag:** [vv01]

- **Fact:** Để giảm tải cho server IoT và tránh lag khi nhiều người dùng, chỉ nên gửi dữ liệu khi nhãn (label) thay đổi hoặc điểm tin cậy (score) biến động lớn hơn 0.05.
- **Source:** [Phần: Cách “giảm lag” khi vẫn dùng OhStem IoT]
- **Tag:** [vv01]

- **Fact:** Camera AI V2 của OhStem có khả năng kết nối Wi-Fi và gửi kết quả nhận dạng trực tiếp lên server IoT (thông qua username và kênh V1-V20) mà không cần máy tính trung gian.
- **Source:** [Phần: Nếu không cắm trực tiếp yolo uno với máy tính...]
- **Tag:** [vv01]

- **Fact:** Điện thoại di động có thể đóng vai trò làm webcam cho máy tính chạy AI thông qua các ứng dụng như DroidCam để cung cấp nguồn hình ảnh cho mô hình Teachable Machine.
- **Source:** [Phần: Dùng cam điện thoại thay cho camera AI được hay không?]
- **Tag:** [vv01]

- **Fact:** Yolo UNO (chip ESP32-S3) hỗ trợ chạy các mô hình TinyML (TensorFlow Lite Micro) cho dữ liệu cảm biến (nhiệt độ, ánh sáng, âm thanh) với giới hạn bộ nhớ RAM khoảng 10–20 KB.
- **Source:** [Phần: Pattern A — TinyML on UNO]
- **Tag:** [vv01]

- **Fact:** Module Grove Vision AI V2 (Seeed Studio) sử dụng chip Cortex-M55 và Ethos-U55 là một lựa chọn phần cứng AI thay thế, hỗ trợ TensorFlow và PyTorch nhưng cần lập trình thủ công để tương thích với hệ sinh thái OhStem.
- **Source:** [Phần: Nếu không mua camera AI của ohstem...]
- **Tag:** [vv01]

- **Fact:** Quy trình xử lý dữ liệu Serial trên UNO bao gồm: đọc vào bộ đệm (buffer), kiểm tra ký tự xuống dòng (`\n`), và tách chuỗi (parse) dựa trên ký tự phân cách (ví dụ dấu `:`).
- **Source:** [Phần: 4. Lập trình Yolo UNO nhận dữ liệu Serial...]
- **Tag:** [vv01]