---
file_id: ROBOT_Rover_MCQ_De1_Q30
type: MCQ
difficulty: Thông hiểu
topic: Tổng hợp IoT và Lập trình Rover
answer: B
tags: [Rover, IoT, MQTT, Dashboard]
source: Robot_Rover_Đề_trắc_nghiệm_1_-_Rover.md:737
---

# ❓ Câu hỏi
Cho một bảng điều khiển có widget joystick như hình sau:
![Image](../assets/ASSET_ROBOT_Rover_rId77.png)
![Image](../assets/ASSET_ROBOT_Rover_rId78.png)

Đoạn lệnh nào sau đây giúp Rover thực hiện yêu cầu sau:
- Robot di chuyển hình vuông liên tục, lặp lại cho đến khi nhấn nút B trên Yolobit thì dừng lại
- Mỗi 2 giây, robot gửi thông tin nhiệt độ đo được đến widget biểu đồ trên dashboard
- Robot có chức năng bật/tắt đèn pha bằng công tắc trên dashboard

# 📝 Đáp án lựa chọn
A. [Hình ảnh đoạn lệnh A]
B. [Hình ảnh đoạn lệnh B]
C. [Hình ảnh đoạn lệnh C]
D. [Hình ảnh đoạn lệnh D]

# 🔗 Liên kết tư duy
- Phân tích logic: Sử dụng vòng lặp (loop) cho hình vuông, sự kiện nhấn nút B để dừng (break/stop).
- Sử dụng khối lệnh gửi dữ liệu MQTT mỗi 2 giây (timer).
- Sử dụng khối lệnh "Khi nhận dữ liệu từ Dashboard" để điều khiển đèn pha.

# 📖 Nguồn
- [Rule 14] Đã mở file nguồn `3-resources/raw/Robot_Rover_Đề_trắc_nghiệm_1_-_Rover.md` và xác nhận fact tại dòng 737-762.
