---
title: TECH Engineering Reference
description: Tài liệu tham chiếu kỹ thuật cho Phần cứng (Hardware) và Phần mềm (Software) trong các dự án STEM/IoT.
category: TECH-Engineering
tags: [3D-Printing, IoT, Electronics, Signal-Processing]
version: 1.0
last_updated: 2026-04-10
---

# 🛠️ TECH Engineering Reference

Tài liệu này tổng hợp các quy tắc kỹ thuật, thông số cấu hình và quy trình bảo trì cho các thiết bị phần cứng và giải pháp phần mềm được sử dụng trong dự án.

## 1. Công nghệ In 3D (3D Printing)

### 📏 Quy tắc Bù trừ Kích thước (Tolerance)
- **Quy tắc 0.125mm:** Khi thiết kế các bộ phận lắp ghép (khớp nối, lỗ trục), cần bù trừ **0.125mm** cho mỗi mặt tiếp xúc để đảm bảo độ khít chuẩn sau khi in.

### 🌫️ Xử lý Mực in (Filament Preservation)
- **Sấy PLA bị ẩm:**
    - Sử dụng bàn nhiệt (Heatbed) của máy in để sấy.
    - **Nhiệt độ:** 45°C - 50°C.
    - **Thời gian:** 4 - 8 giờ.
    - **Lưu ý:** Tuyệt đối không để nhiệt độ vượt quá **55°C** (nhiệt độ chuyển thủy tinh của PLA) để tránh biến dạng và dính cuộn mực.

### 🔧 Bảo trì Máy in Elegoo Neptune 4
- **Xử lý kẹt mực (Filament Jam):**
    - **Cold Pull:** Làm nóng Nozzle lên 200°C -> Nạp mực -> Hạ nhiệt xuống 90°C -> Rút mạnh sợi mực để kéo theo cặn bẩn.
    - **Tháo nắp Extruder:** Tháo 2 ốc lục giác 2mm (1 ốc giữa sau cần gạt, 1 ốc cạnh bên phải).
    - **Điều chỉnh lực đùn:** Vặn ốc điều áp lò xo phía sau Extruder (siết để tăng lực kẹp, nới để giảm).

## 2. Xử lý Tín hiệu & Thuật toán (Signal Processing)

### 📈 Lọc nhiễu trung bình trượt lũy thừa (EMA)
Sử dụng EMA (Exponential Moving Average) để làm mượt dữ liệu cảm biến (như ánh sáng, khoảng cách) giúp điều khiển ổn định hơn.

- **Công thức:** `ema_t = ema_{t-1} + α * (x_t - ema_{t-1})`
- **Tính hệ số α (Alpha):** `α = 1 - exp(-Δt / τ)`
    - `Δt`: Chu kỳ lấy mẫu.
    - `τ`: Hằng số thời gian mong muốn (độ mượt).
- **Khởi tạo:** Nên đặt giá trị EMA đầu tiên bằng giá trị cảm biến đọc được để tránh hiện tượng "đuổi theo" dữ liệu lúc khởi động.

## 3. Điện tử & Cảm biến (Electronics & Sensors)

### 📡 Bảng Logic Tín hiệu (Digital Logic)
Xác định mức logic (0/1) khi cảm biến được kích hoạt trên hệ sinh thái OhStem/Yolo UNO.

| Cảm biến | Loại tín hiệu | Khi có tác động | Khi không có tác động | Đặc điểm |
| :--- | :--- | :--- | :--- | :--- |
| **PIR (Người)** | Digital | `1` (HIGH) | `0` (LOW) | Active-HIGH. Cần 20-60s khởi động. |
| **IR Obstacle** | Digital | `0` (LOW) | `1` (HIGH) | Active-LOW (do mạch transistor đảo). |
| **Nút nhấn** | Digital | `0` | `1` | Thường nối GND khi nhấn. |
| **Flame/Hall** | Digital | `0` | `1` | Thường là Active-LOW. |

### 🔦 Cảm biến PIR HC-SR501 (Hiệu chỉnh)
- **Biến trở TIME (Trái):** Xoay CW (cùng chiều kim đồng hồ) để tăng thời gian giữ HIGH (2s - 5p).
- **Biến trở SENS (Phải):** Xoay CW để tăng độ nhạy/khoảng cách quét (3m - 7m).
- **Jumper H/L:**
    - **H (Repeatable):** Tự động gia hạn thời gian HIGH nếu vẫn còn chuyển động. (Khuyên dùng cho bật đèn).
    - **L (Non-Repeatable):** Trả về LOW sau khi hết thời gian TIME dù vẫn còn chuyển động.
