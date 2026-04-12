---
title: STEAM Project Ideas (Creative Repository)
type: repository
category: projects
tags: [STEAM, IoT, robotics, AI, prototype]
last_updated: 2026-04-10
---

# 🚀 STEAM Project Ideas (Creative Repository)

Tổng hợp các ý tưởng dự án, giải pháp kỹ thuật và kịch bản thực tế trích xuất từ quá trình triển khai tại KDI Education.

## 1. Nhóm Dự án Cơ bản & IoT

### 🚗 Xe tự hành tránh vật cản (Obstacle Avoidance Car)
- **Thành phần**: Yolo:Bit, Cảm biến siêu âm, Module động cơ.
- **Tính năng**: 
    - Tự động rẽ khi gặp vật cản.
    - Chế độ điều khiển từ xa qua Bluetooth/Wi-Fi.
- **Ghi chú kỹ thuật**: Sử dụng cảm biến siêu âm với logic lọc nhiễu trung bình (Moving Average) để ổn định khoảng cách.

### 🌡️ Trạm quan trắc môi trường (Smart Environment Station)
- **Thành phần**: ESP32/Yolo:Bit, DHT11 (Nhiệt ẩm), MQ-135 (Chất lượng không khí), PIR.
- **Tính năng**: 
    - Gửi dữ liệu lên Dashboard (Easy IoT/Adafruit).
    - Cảnh báo qua đèn LED hoặc còi khi chỉ số không khí vượt ngưỡng.

---

## 2. Nhóm Dự án Kỹ thuật & Chế tạo

### 🖨️ Tối ưu hóa Máy in 3D (Neptune 4 Mastery)
- **Quy trình chuẩn**:
    1. Kiểm tra E-steps và Flow rate cho vật liệu mới.
    2. Quy tắc bù trừ lỗ hổng: **0.125mm** để các linh kiện lắp ghép vừa khít.
    3. Bảo trì: Cold-pull sạch đầu phun sau khi dùng nhựa cũ/giòn.
- **Vật tư**: PLA EN, PETG... (Xem [[TECH_Engineering_Reference]] để biết cấu hình in nhanh).

### 🛠️ Hệ thống lọc tín hiệu cảm biến
- Áp dụng **EMA (Exponential Moving Average)** để loại bỏ nhiễu cho các cảm biến Analog (như cảm biến ánh sáng, âm thanh).
- Logic Active-HIGH/LOW cho module PIR và hồng ngoại để tránh kích hoạt giả.

---

## 3. Nhóm Dự án Trí tuệ Nhân tạo (AI)

### 🍎 Nhận diện trái cây/Phân loại rác thải
- **Mô hình**: Teachable Machine hoặc YOLO.
- **Sư phạm (5E)**: 
    - *Explore*: Cho học sinh tự chụp ảnh mẫu vật với nhiều góc độ khác nhau.
    - *Explain*: Giải thích về "Dataset" và "Model Training".

### 💬 Trợ lý học tập thông minh (AI Second Brain)
- Xây dựng hệ thống quản lý tri thức cá nhân dựa trên Obsidian hoặc NotebookLM.
- Ứng dụng để tóm tắt các khóa học từ Coursera (ví dụ: Google IT Automation).

---

## 🔗 Liên kết Tri thức
- [[PEDAGOGY_Master_Handbook]]: Sử dụng để thiết kế tiến trình dạy học cho các dự án trên.
- [[LMS_KB_IOT_DEEP]]: Chi tiết về lập trình các cảm biến IoT.

---
📖 *Nguồn trích dẫn: Tổng hợp từ nhật ký v01-v26.*
