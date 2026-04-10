# 📐 Giáo án: Hình học Giải tích & Đồ họa (G10+)

> **Mô tả**: Nâng cấp từ bài học về Hình chữ nhật cơ bản sang việc biểu diễn hình học trong mặt phẳng Oxy và ứng dụng trong thiết kế đồ họa/máy in 3D.

## 1. 🎯 Mục tiêu bài học (Objectives)
- **Kiến thức**: Hiểu cách xác định tọa độ các đỉnh của hình chữ nhật, tính diện tích bằng tích vô hướng/độ dài vectơ.
- **Kỹ năng**: Lập trình được thuật toán vẽ hình chữ nhật trên OLED hoặc G-code cơ bản.
- **Thái độ**: Nhận thức được tầm quan trọng của toán học trong công nghệ sản xuất.

## 2. 🏛️ Tiến trình sư phạm (5E)

### Engage (Gắn kết)
- Đặt câu hỏi: "Làm thế nào máy in 3D biết cách di chuyển để tạo ra một mặt đáy hình chữ nhật hoàn hảo?"
- Giới thiệu mối liên hệ giữa tọa độ (x, y) và các điểm đầu cuối của động cơ bước.

### Explore (Khám phá)
- Cho học sinh tọa độ 3 điểm A(0,0), B(a,0), D(0,b). Yêu cầu tìm tọa độ điểm C để ABCD là hình chữ nhật.
- Sử dụng Python để tính độ dài các cạnh và đường chéo.

### Explain (Giải thích)
- Định nghĩa hình chữ nhật qua Vectơ: $\vec{AB} \cdot \vec{AD} = 0$.
- Công thức diện tích: $S = |\vec{AB}| \times |\vec{AD}|$.
- Giải thích về dung sai (Tolerance) trong thực tế: Tại sao hình chữ nhật 10x10 in ra có thể là 9.8x10.2? (Liên kết tới `Engineering_Robotics_Master.md`).

### Elaborate (Củng cố)
- Thử thách: Viết hàm Python nhận vào 2 điểm (góc dưới trái và góc trên phải) và xuất ra chuỗi lệnh G-code để đầu in di chuyển theo khung hình đó.

### Evaluate (Đánh giá)
- Đánh giá dựa trên độ chính xác của tọa độ và khả năng giải thích lỗi sai khi gặp sai số cơ khí.

## 🔗 Liên kết hệ thống
- [[Pedagogical_Master_DNA]]
- [[Engineering_Robotics_Master]] (Dung sai & Bù trừ)
