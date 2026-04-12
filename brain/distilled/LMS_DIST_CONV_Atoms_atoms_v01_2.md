---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v01_2
  title: atoms_v01_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dựa trên nguồn dữ liệu **Volume v01** và nội dung thảo luận, tôi xin trích xuất các sự kiện kỹ thuật (Facts) liên quan đến yêu cầu của bạn về IoT, AI nhúng và quy trình triển khai:

- **Fact:** Việc tích hợp AI vào hệ thống nhúng đòi hỏi hiểu rõ giới hạn phần cứng; ví dụ ESP32 không thể xử lý ảnh lớn nhanh nhưng xử lý tốt âm thanh và cảm biến đơn giản.
- **Source:** (v01 - Giai đoạn 3: Tích hợp mô hình AI vào hệ thống nhúng)
- **Tag:** [vv01]

- **Fact:** Để nhận diện hình ảnh trên thiết bị tài nguyên thấp (như ESP32, Arduino), cần sử dụng mô hình nhỏ như mạng CNN đã lượng tử hóa hoặc mô hình 96x96 pixel (trắng đen) từ Edge Impulse.
- **Source:** (v01 - Giai đoạn 4: Nhận diện hình ảnh trên thiết bị nhúng)
- **Tag:** [vv01]

- **Fact:** Quy trình xây dựng hệ thống AIoT cơ bản bao gồm 4 bước: thu thập dữ liệu (cảm biến/hình ảnh), huấn luyện mô hình, triển khai lên thiết bị và kiểm thử thực tế.
- **Source:** (v01 - Giai đoạn 4: Mục tiêu)
- **Tag:** [vv01]

- **Fact:** Có thể tối ưu hóa xử lý bằng cách đưa một phần tính toán lên máy chủ (thiết bị chụp ảnh rồi gửi về server AI phân tích) thay vì xử lý cục bộ hoàn toàn, đây là hướng tiếp cận thiên về IoT hơn TinyML.
- **Source:** (v01 - Tài liệu/Hướng dẫn: Lưu ý trong quá trình)
- **Tag:** [vv01]

- **Fact:** Teachable Machine (TM) chạy trên trình duyệt (JavaScript) có thể đóng vai trò bộ xử lý AI, sau đó gửi kết quả dự đoán qua giao tiếp Serial (USB) để vi điều khiển (như Yolo UNO) nhận và đẩy lên dashboard IoT.
- **Source:** (Conversation: Yolo UNO IoT integration - Ý tưởng tổng quát)
- **Tag:** [Unverified_Source]

- **Fact:** Để truyền dữ liệu từ trình duyệt web xuống vi điều khiển qua cổng USB, có thể sử dụng Web Serial API với định dạng chuỗi văn bản (ví dụ: `TM:label:score\n`).
- **Source:** (Conversation: Yolo UNO IoT integration - Bước 2)
- **Tag:** [Unverified_Source]

- **Fact:** Trên các nền tảng như OhStem, việc xử lý dữ liệu từ AI gửi về thường dùng các khối lệnh (Blockly) để tách chuỗi (split), chuyển đổi kiểu dữ liệu và gửi lên Cloud qua các Data Keys.
- **Source:** (Conversation: Yolo UNO IoT integration - Bước 3)
- **Tag:** [Unverified_Source]

--------------------------------------------------
**Tóm tắt quy trình thực hiện cho bạn (Dựa trên tri thức đã trích xuất):**

1.  **Phía Máy tính (AI):** Mở link Teachable Machine của bạn trên trình duyệt Chrome/Edge. Sử dụng một đoạn mã JavaScript (Web Serial) để "bắn" kết quả nhận diện ra cổng USB.
2.  **Phía Yolo UNO (Cầu nối):** Lập trình cho UNO lắng nghe cổng Serial. Khi thấy dữ liệu có tiền tố "TM:", nó sẽ tách lấy tên vật thể và độ tin cậy.
3.  **Phía IoT (Hiển thị):** UNO sử dụng kết nối Wi-Fi để gửi các thông tin vừa tách được lên server OhStem (app.ohstem.vn) thông qua các "Key" dữ liệu đã tạo sẵn.