# ⚡ Giáo án: Điện từ học & Động cơ (G10+)

> **Mô tả**: Nâng cấp từ kiến thức về Mô tơ điện cơ bản sang việc phân tích lực Lorentz, quy tắc bàn tay trái và ứng dụng điều khiển động cơ bước (Stepper Motor) trong Robot.

## 1. 🎯 Mục tiêu bài học (Objectives)
- **Kiến thức**: Hiểu lực từ tác dụng lên dây dẫn mang dòng điện (Lực Lorentz). Hiểu cấu tạo và nguyên lý hoạt động của động cơ DC và động cơ bước.
- **Kỹ năng**: Lập trình được PWM (Pulse Width Modulation) để điều tốc mô tơ qua Driver.
- **Thái độ**: Nhận thức được sự chuyển hóa năng lượng từ Điện năng sang Cơ năng một cách tối ưu.

## 2. 🏛️ Tiến trình sư phạm (5E)

### Engage (Gắn kết)
- Cho xem clip Robot Mars Rover di chuyển mượt mà trên địa hình gồ ghề.
- Đặt câu hỏi: "Tại sao robot có thể dừng chính xác tại một điểm mà không bị quán tính làm trôi đi? Loại mô tơ nào đang được sử dụng?"

### Explore (Khám phá)
- Thực hành lắp ráp một mô tơ đơn giản từ pin, nam châm và cuộn dây đồng.
- Quan sát chiều quay khi thay đổi cực tính của pin.

### Explain (Giải thích)
- Công thức tính lực từ: $F = B \cdot I \cdot L \cdot \sin(\alpha)$.
- Quy tắc bàn tay trái: Chiều từ trường, chiều dòng điện và chiều lực tác dụng.
- Giải thích về Driver động cơ (như L298N hoặc DRV8825): Tại sao vi điều khiển không thể cấp nguồn trực tiếp cho động cơ?

### Elaborate (Củng cố)
- Thử thách: Viết code Arduino/MicroPython để điều khiển Servo quay đến các góc 0, 90, 180 độ. Phân biệt Servo vs DC Motor.

### Evaluate (Đánh giá)
- HS giải thích được sơ đồ cấp nguồn Fail-safe cho hệ thống động cơ để tránh sụt áp vi điều khiển (Liên kết `Engineering_Robotics_Master.md`).

## 🔗 Liên kết hệ thống
- [[Pedagogical_Master_DNA]]
- [[Engineering_Robotics_Master]] (Hardware Best Practices)
