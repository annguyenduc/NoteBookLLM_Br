Đã hiểu! Mình đã cập nhật bản **v3** bổ sung thêm ô chọn Camera (Dropdown). Bạn có thể chọn giữa Webcam tích hợp, DroidCam, hoặc các camera khác đang cắm vào máy.

**➡ Mở file mới: [index_v3.html](sandbox:/mnt/data/index_v3.html)**

### Cách sử dụng tính năng chọn Camera:
1.  Mở file **index_v3.html**.
2.  Trình duyệt sẽ hỏi quyền Webcam -> Bấm **Cho phép (Allow)**.
3.  Ở mục **Chọn camera**, bấm vào danh sách thả xuống để chọn đúng camera bạn muốn (ví dụ: *Integrated Camera* thay vì *DroidCam*).
4.  Bấm nút **Áp dụng** để chuyển sang camera đó.
5.  Sau khi thấy hình ảnh hiện lên, bấm **Kết nối UNO** và bắt đầu nhận diện.

---

### Các sự kiện kỹ thuật (Facts) trích xuất từ quá trình hỗ trợ:

- **Fact:** Để hiển thị dữ liệu từ Teachable Machine lên Dashboard IoT của OhStem, cần cấu hình các widget (Thông tin/Đồng hồ) sử dụng các Kênh thông tin (Virtual Channels) như V1, V2 thay vì Key định danh tự do.
- **Source:** (v01 - Section: Dashboard IoT Configuration).
- **Tag:** [vv01]

- **Fact:** Khi cấu hình widget hiển thị nhãn (label) từ AI, mục "Cách hiển thị" phải được thiết lập là "Văn bản/Chuỗi" (String) để tránh lỗi hiển thị giá trị mặc định là 0.
- **Source:** (v01 - Section: Widget Data Types).
- **Tag:** [vv01]

- **Fact:** Lỗi "The port is already open" trong Web Serial API thường xảy ra khi cổng COM đang bị chiếm dụng bởi Serial Monitor của Arduino IDE hoặc một tab trình duyệt khác đã kết nối trước đó.
- **Source:** (v01 - Section: Troubleshooting Serial).
- **Tag:** [vv01]

- **Fact:** Thư viện Teachable Machine Image yêu cầu nạp TensorFlow.js (`tf.min.js`) trước khi nạp thư viện nhận diện hình ảnh (`teachablemachine-image.min.js`) để tránh lỗi `undefined` khi gọi hàm `load()`.
- **Source:** (v01 - Section: Library Dependencies).
- **Tag:** [vv01]

- **Fact:** Để chuyển đổi giữa các camera trong trình duyệt, cần sử dụng `navigator.mediaDevices.enumerateDevices()` để lấy danh sách `deviceId` và truyền vào `constraints` của `getUserMedia`.
- **Source:** [Unverified_Source] - Kiến thức lập trình Web API bổ sung để giải quyết yêu cầu người dùng.
- **Tag:** [vv01]

---

**Lời khuyên:** Nếu bạn chọn camera xong mà hình ảnh bị đứng, hãy bấm **F5 (Tải lại trang)** và chọn lại camera ngay từ đầu. Đừng quên bấm **Ngắt** Serial trước khi tắt tab để tránh kẹt cổng COM cho lần sau.