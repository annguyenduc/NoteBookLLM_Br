Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v03 (LOM v4.1):

- Fact: [CONV] Cảm biến PIR xuất mức 1 khi có người; cảm biến hồng ngoại (IR) vật cản xuất mức 0 khi có vật; nút nhấn xuất mức 0 khi nhấn.
- Source: [v03 - Section: Ghi nhớ nhanh (mẹo dạy học sinh)]
- Tag: [vv03]

- Fact: [CONV] Các cảm biến Flame, Hall, Touch, Switch đa phần hoạt động theo logic Active-LOW (xuất mức 0 khi được kích hoạt).
- Source: [v03 - Section: Ghi nhớ nhanh (mẹo dạy học sinh)]
- Tag: [vv03]

- Fact: [CONV] Cảm biến Analog (ánh sáng, âm thanh, độ ẩm đất, gas) không có giá trị 0/1 rõ ràng, cần dùng khối so sánh (>, <) để phân loại trạng thái.
- Source: [v03 - Section: Ghi nhớ nhanh (mẹo dạy học sinh)]
- Tag: [vv03]

- Fact: [CONV] Để đảo ngược logic của module cảm biến trong lập trình, có thể sử dụng công thức: `1 - đọc digital()`.
- Source: [v03 - Section: Gợi ý cho bài dạy STEM/IoT]
- Tag: [vv03]

- Fact: [CONV] Cảm biến PIR HC-SR501 có hai biến trở điều chỉnh: núm bên trái (TIME) chỉnh thời gian giữ tín hiệu HIGH (2 giây - 5 phút), núm bên phải (SENS) chỉnh độ nhạy/khoảng cách (3m - 7m).
- Source: [v03 - Section: 2. Hai núm vặn (biến trở vàng)]
- Tag: [vv03]

- Fact: [CONV] Chế độ Repeatable (H) trên PIR HC-SR501 sẽ giữ tín hiệu HIGH liên tục nếu vẫn còn phát hiện chuyển động, trong khi chế độ Non-Repeatable (L) sẽ về LOW sau khoảng thời gian TIME dù vẫn có chuyển động.
- Source: [v03 - Section: 3. Jumper chọn chế độ (3 chân, màu vàng)]
- Tag: [vv03]

- Fact: [CONV] Cảm biến PIR cần khoảng 40 - 60 giây để khởi động (warm-up) sau khi cấp nguồn trước khi hoạt động chính xác.
- Source: [v03 - Section: 4. Mẹo test thực tế / Section: 4️⃣ Lưu ý trước khi test]
- Tag: [vv03]

- Fact: [CONV] Module PIR của OhStem sử dụng chuẩn kết nối Grove 3 chân (GND-VCC-SIG), đã được tinh giản các núm vặn điều chỉnh phần cứng.
- Source: [v03 - Section: 1. Cấu trúc và các thành phần chính (OhStem)]
- Tag: [vv03]

- Fact: [CONV] Việc cắm ngược dây nguồn (đặc biệt là đảo VCC và GND) có thể khiến cảm biến PIR bị hỏng vĩnh viễn.
- Source: [v03 - Section: 1️⃣ Kiểm tra kết nối phần cứng]
- Tag: [vv03]

- Fact: [CONV] Có thể kiểm tra cảm biến PIR thủ công bằng cách nối LED và điện trở vào chân SIG và GND; LED sáng khi có chuyển động và tắt sau vài giây nếu cảm biến còn tốt.
- Source: [v03 - Section: 3️⃣ Kiểm tra phần cứng (không cần đồng hồ)]
- Tag: [vv03]

- Fact: [CONV] Khối "sau mỗi ... giây thực hiện" trên Yolo:bit là một bộ hẹn giờ song song (non-blocking), không chờ lệnh "tạm dừng" bên trong kết thúc trước khi bắt đầu chu kỳ mới.
- Source: [v03 - Section: 🧩 1️⃣ Cơ chế nền của thư viện “Xử lý sự kiện”]
- Tag: [vv03]

- Fact: [CONV] Để thực hiện các hành động tuần tự có độ trễ chính xác trên Yolo:bit, nên sử dụng vòng lặp "lặp mãi" kết hợp với khối "tạm dừng" thay vì dùng khối sự kiện định kỳ.
- Source: [v03 - Section: ✅ Cách khắc phục (để thực sự dừng 1 giây)]
- Tag: [vv03]

- Fact: [CONV] Teachable Machine cho phép xây dựng hệ thống phân loại hình ảnh (Image Classification) nhanh chóng mà không cần lập trình chuyên sâu về Machine Learning.
- Source: [v03 - Section: 1) Cách nhanh nhất: Teachable Machine (image classification)]
- Tag: [vv03]

- Fact: [CONV] Thư viện OpenCV kết hợp với mô hình MobileNet-SSD có thể thực hiện nhận diện vật thể kèm theo khung bao (bounding box) trong thời gian thực bằng Python.
- Source: [v03 - Section: 2) Cách linh hoạt: OpenCV + mô hình phát hiện sẵn (MobileNet-SSD)]
- Tag: [vv03]