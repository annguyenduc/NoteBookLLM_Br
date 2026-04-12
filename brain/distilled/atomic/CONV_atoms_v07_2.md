Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn cung cấp (v07) về các chủ đề IoT, Arduino, Robotics và AI theo quy tắc LOM v4.1:

- **Fact:** [CONV] Chế độ Live mode trong mBlock 5 cho phép Stage/Sprite và thiết bị (Arduino) chia sẻ biến số (Variables) và truyền nhận thông tin theo thời gian thực.
- **Source:** [v07 - Section: Ghi chú quan trọng & Phần 0: Phần cứng & chế độ]
- **Tag:** [vv07]

- **Fact:** [CONV] Việc nhận diện cử chỉ tay (như số lượng ngón tay) trong mBlock có thể thực hiện thông qua extension Teachable Machine hoặc Machine Learning 2.0 (Image Classification).
- **Source:** [v07 - Section: Phần Stage / Sprite (UI + AI)]
- **Tag:** [vv07]

- **Fact:** [CONV] mBlock không hỗ trợ khối so sánh "khác" (≠) trực tiếp; lập trình viên phải sử dụng kết hợp khối `not` (không phải) và khối `=` (bằng) để tạo logic so sánh khác.
- **Source:** [v07 - Section: Cách 1 (khuyên dùng): NOT + “=”]
- **Tag:** [vv07]

- **Fact:** [CONV] Trong các ứng dụng Robotics cơ bản, Servo (như SG90/MG90S) thường được cấu hình góc 0° để biểu thị trạng thái đóng và 90° để biểu thị trạng thái mở.
- **Source:** [v07 - Section: 0) Phần cứng & chế độ (Bài tập 3)]
- **Tag:** [vv07]

- **Fact:** [CONV] Công nghệ STT (Speech-to-Text) trong mBlock được sử dụng để chuyển đổi giọng nói từ microphone thành dữ liệu văn bản (string) nhằm thực hiện các lệnh điều khiển bằng giọng nói.
- **Source:** [v07 - Section: [điều kiện: đã có kết quả STT] vậy stt là gì]
- **Tag:** [vv07]

- **Fact:** [CONV] Để tránh việc chương trình bị dừng (blocking) khi đếm thời gian, nên sử dụng biến lưu mốc thời gian kết hợp với khối `timer` thay vì sử dụng khối `wait`.
- **Source:** [v07 - Section: Cách 2 (không chặn): chụp mốc thời gian, không dùng reset timer]
- **Tag:** [vv07]

- **Fact:** [CONV] Khi điều khiển thiết bị ngoại vi qua Arduino trong mBlock, các chân Digital (như D2, D3, D4) phải được thiết lập ở chế độ "output" trước khi thực hiện lệnh ghi tín hiệu (digital write).
- **Source:** [v07 - Section: Phần Device (Arduino) – điều khiển chân D2/D3/D4]
- **Tag:** [vv07]

- **Fact:** [CONV] Việc lồng các khối điều kiện IF trong phần ELSE (Nested IF) là kỹ thuật cần thiết trong mBlock để xử lý nhiều trạng thái của một biến số khi thiết bị không hỗ trợ khối "else if" trực tiếp.
- **Source:** [v07 - Section: Nhận cử chỉ (chọn 1 trong 2 cách) & Phần 5: Device (Arduino)]
- **Tag:** [vv07]

- **Fact:** [CONV] Để đảm bảo tính ổn định cho mô hình AI nhận diện hình ảnh, cần thu thập dữ liệu ở nhiều điều kiện ánh sáng khác nhau, khoảng cách từ 20-40cm và sử dụng tính năng "mirror video".
- **Source:** [v07 - Section: Ghi chú quan trọng (Phần nhận diện ngón tay)]
- **Tag:** [vv07]

- **Fact:** [CONV] Biến số dùng để giao tiếp giữa giao diện (Stage) và phần cứng (Arduino) trong mBlock bắt buộc phải được thiết lập ở chế độ "For all sprites".
- **Source:** [v07 - Section: Biến dùng chung (For all sprites)]
- **Tag:** [vv07]