Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất và chưng cất từ nguồn dữ liệu Volume v03 liên quan đến IoT, Robotics và AI:

- **Fact:** Cảm biến PIR cho giá trị 1 khi phát hiện có người; cảm biến hồng ngoại (IR) vật cản cho giá trị 0 khi có vật cản.
- **Source:** Section: Ghi nhớ nhanh (mẹo dạy học sinh)
- **Tag:** [vv03]

- **Fact:** Các loại cảm biến như Nút nhấn, Flame (lửa), Hall (từ trường), Touch (chạm), Switch (công tắc) đa phần hoạt động theo logic Active-LOW (trả về 0 khi được kích hoạt).
- **Source:** Section: Ghi nhớ nhanh (mẹo dạy học sinh)
- **Tag:** [vv03]

- **Fact:** Cảm biến Analog (ánh sáng, âm thanh, độ ẩm đất, gas) không có giá trị 0/1 rõ ràng, cần sử dụng các khối so sánh (>, <) để phân loại trạng thái.
- **Source:** Section: Ghi nhớ nhanh (mẹo dạy học sinh)
- **Tag:** [vv03]

- **Fact:** Cảm biến PIR HC-SR501 có hai biến trở điều chỉnh: núm TIME (L) chỉnh thời gian giữ tín hiệu HIGH (từ 2 giây đến 5 phút) và núm SENS (S) chỉnh độ nhạy/khoảng cách quét (từ 3m đến 7m).
- **Source:** Section: 1. Cấu trúc và các thành phần chính & Section: 2. Hai núm vặn
- **Tag:** [vv03]

- **Fact:** Jumper trên PIR HC-SR501 cho phép chọn chế độ: L (Non-Repeatable - không lặp lại) và H (Repeatable - lặp lại, giữ tín hiệu HIGH liên tục nếu còn chuyển động).
- **Source:** Section: 3. Jumper chọn chế độ (3 chân, màu vàng)
- **Tag:** [vv03]

- **Fact:** Cảm biến PIR cần khoảng 60 giây để khởi động (warm-up) sau khi cấp nguồn trước khi hoạt động ổn định.
- **Source:** Section: 4. Mẹo test thực tế
- **Tag:** [vv03]

- **Fact:** Module PIR của OhStem sử dụng chuẩn kết nối Grove 3 chân (GND-VCC-SIG), đã được tinh giản các núm chỉnh thông số và hoạt động ở mức điện áp 3V - 5V.
- **Source:** Section: 1️⃣ Hiểu đúng module bạn đang dùng (PIR OhStem)
- **Tag:** [vv03]

- **Fact:** Việc đấu ngược dây nguồn (đặc biệt là VCC và GND) có thể khiến cảm biến PIR bị hỏng vĩnh viễn.
- **Source:** Section: 1️⃣ Kiểm tra kết nối phần cứng
- **Tag:** [vv03]

- **Fact:** Có thể kiểm tra cảm biến PIR thủ công bằng cách nối LED vào chân SIG và GND; nếu LED sáng khi có chuyển động và tắt sau vài giây thì cảm biến còn hoạt động tốt.
- **Source:** Section: 3️⃣ Kiểm tra tín hiệu bằng LED thủ công
- **Tag:** [vv03]

- **Fact:** Khối lệnh "sau mỗi ... giây thực hiện" trên Yolo:bit/mBlock hoạt động theo cơ chế lập lịch song song (non-blocking scheduler), không dừng toàn bộ chương trình khi gặp lệnh "tạm dừng" bên trong.
- **Source:** Section: 🧩 Giải thích vì sao không dừng 1s & Section: 1️⃣ Cơ chế nền của thư viện “Xử lý sự kiện”
- **Tag:** [vv03]

- **Fact:** Để thực hiện trễ tuần tự (blocking delay) chính xác trên Yolo:bit, cần sử dụng vòng lặp "lặp mãi" kết hợp với khối "tạm dừng" thay vì dùng khối sự kiện định kỳ.
- **Source:** Section: ✅ Cách khắc phục (để thực sự dừng 1 giây)
- **Tag:** [vv03]

- **Fact:** Teachable Machine hỗ trợ huấn luyện mô hình phân loại hình ảnh (Image Classification) và xuất dưới dạng TensorFlow.js hoặc TensorFlow Lite.
- **Source:** Section: 1) Cách nhanh nhất: Teachable Machine
- **Tag:** [vv03]

- **Fact:** Thư viện OpenCV kết hợp với mô hình MobileNet-SSD (Caffe) cho phép phát hiện vật thể thời gian thực và vẽ khung bao (bounding box) quanh vật thể.
- **Source:** Section: 2) Cách linh hoạt: OpenCV + mô hình phát hiện sẵn (MobileNet-SSD)
- **Tag:** [vv03]

- **Fact:** Cảm biến Hall trả về giá trị 0 khi có nam châm và 1 khi không có (Active-LOW), thường dùng trong mô hình cửa an ninh.
- **Source:** DỮ LIỆU RAW (Dòng đầu tiên)
- **Tag:** [vv03]