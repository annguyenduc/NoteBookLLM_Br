---
file_id: LMS_DIST_CONV_Atoms_atoms_v02_7
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS DIST CONV Atoms atoms v02 7

# Tài liệu học tập: Tối ưu hóa thuật toán điều khiển cảm biến trong hệ thống IoT/Robotics

## Thông tin tài liệu
- **Mã tài liệu:** LOM_v02_Sensor_Control_Optimization
- **Phiên bản:** 4.4 Supreme
- **Ngôn ngữ:** Tiếng Việt
- **Loại tài liệu:** Bài giảng kỹ thuật nâng cao
- **Thời lượng:** 90 phút
- **Đối tượng:** Kỹ sư IoT, sinh viên kỹ thuật, nhà phát triển hệ thống nhúng

---

## Mục tiêu học tập

Sau khi hoàn thành bài học này, học viên sẽ có khả năng:

1. **Hiểu rõ** các phương pháp lọc tín hiệu cảm biến phổ biến trong hệ thống IoT
2. **Áp dụng** các kỹ thuật tối ưu hóa logic điều khiển để giảm sai số
3. **Thiết kế** hệ thống điều khiển ánh sáng thông minh sử dụng thuật toán EMA, Hysteresis và Gamma Correction
4. **Triển khai** các nguyên tắc kiến trúc hệ thống không chặn (non-blocking) trong thực tế

---

## Nội dung chính

### 1. Tối ưu hóa xử lý dữ liệu cảm biến

#### 1.1. Thuật toán EMA (Exponential Moving Average)

**Khái niệm:**  
EMA là phương pháp lọc trượt theo cấp số nhân, giúp làm mịn dữ liệu cảm biến bằng cách ưu tiên các giá trị gần đây hơn.

**Công thức:**
```
L_ema_new = α × L_current + (1 - α) × L_ema_old
```

**Thông số khuyến nghị:**
- Hệ số α ≈ 0.25 giúp triệt nhiễu ánh sáng nhỏ, tránh hiện tượng LED nhấp nháy [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### 1.2. Bộ lọc trung vị (Median Filter)

**Nguyên lý:**  
Sử dụng **Median-3 (Trung vị của 3 mẫu)** cho cảm biến siêu âm để loại bỏ các giá trị đo "nhảy" do phản xạ bề mặt hoặc nhiễu tức thời [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

**Ví dụ mã giả:**
```cpp
int median3(int a, int b, int c) {
    if ((a >= b && a <= c) || (a >= c && a <= b)) return a;
    if ((b >= a && b <= c) || (b >= c && b <= a)) return b;
    return c;
}
```

#### 1.3. Cơ chế lọc ngoại lệ (Outlier Rejection)

**Công thức phát hiện ngoại lệ:**
```
Nếu |L_x - L_ema| > L_outlier (thường từ 20-50) → Bỏ qua mẫu dữ liệu
```

**Lợi ích:** Tránh các giá trị sai lệch cực mạnh làm vọt EMA [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

### 2. Tối ưu hóa logic điều khiển

#### 2.1. Hysteresis (Trễ nhiệt/ngưỡng)

**Nguyên lý:**  
Sử dụng hai ngưỡng khác nhau để bật và tắt thiết bị, tránh hiện tượng dao động liên tục ở vùng biên.

**Ví dụ:**
- Bật khi: ánh sáng < 200
- Tắt khi: ánh sáng > 300

**Lợi ích:** Giảm hiện tượng "rung lắc" khi giá trị cảm biến ở gần ngưỡng [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### 2.2. Logic AND trong điều khiển

**Nguyên tắc:**  
Chỉ bật thiết bị khi đồng thời thỏa mãn nhiều điều kiện (ví dụ: TỐI **và** CÓ NGƯỜI).

**Lợi ích:**  
Giảm tỷ lệ báo sai (FPR - False Positive Rate), giúp hệ thống ổn định hơn [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### 2.3. Hiệu chuẩn thích nghi (Auto-calibration)

**Quy trình:**
1. Đo giá trị sáng nhất (L_bright) và tối nhất (L_dark) trong 10-15 giây đầu
2. Tính toán ngưỡng động:
   ```
   mid = (L_bright + L_dark) / 2
   gap = max(120, 0.1 × dải_thực)
   ```

**Lợi ích:**  
Tự động điều chỉnh ngưỡng phù hợp với môi trường thực tế [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

### 3. Tối ưu hóa đầu ra PWM

#### 3.1. Giới hạn tốc độ thay đổi (Slew Rate)

**Nguyên lý:**  
Sử dụng biến `pwm_step` (ví dụ = 8) để LED tăng/giảm độ sáng từ từ, chống nhảy số đột ngột.

**Ví dụ mã giả:**
```cpp
if (target_pwm > current_pwm) {
    current_pwm = min(target_pwm, current_pwm + pwm_step);
} else if (target_pwm < current_pwm) {
    current_pwm = max(target_pwm, current_pwm - pwm_step);
}
```

#### 3.2. Hiệu chỉnh Gamma (Gamma Correction)

**Công thức:**
```
L_norm_corrected = L_norm^L_gamma
```
- L_gamma thường nằm trong khoảng 1.4 - 2.0

**Lợi ích:**  
Điều chỉnh độ sáng mượt mà hơn theo cảm nhận của mắt người [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### 3.3. Chuyển đổi thang đo PWM

**Phạm vi:**  
- Cảm biến: 0-4095
- Giao diện người dùng: 0-100

**Công thức chuyển đổi:**
```
pwm = (L_val / 4095) × 100
```

---

### 4. Kiến trúc hệ thống tối ưu

#### 4.1. Cơ chế không chặn (Non-blocking)

**Nguyên tắc:**  
Thay thế các lệnh `delay` dài bằng cơ chế lập lịch theo sự kiện hoặc kiểm tra định kỳ (mỗi 0.1s - 0.2s).

**Lợi ích:**  
Đảm bảo hệ thống phản ứng nhanh, không bị treo [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### 4.2. Lựa chọn chân cắm (Pinout)

**Khuyến nghị cho Yolo UNO:**
- Chân **D13**: Hỗ trợ PWM tốt cho LED
- Chân **D3**: Dành cho I2C SDA, không nên dùng cho PWM [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### 4.3. Cơ chế an toàn (Fail-safe)

**Nguyên tắc:**  
Nếu mất kết nối Internet/AI, hệ thống phải tự động rơi về chế độ điều khiển bằng luật cục bộ (if-else/hysteresis) để duy trì hoạt động [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## Quy trình tích hợp hoàn chỉnh

![Quy trình xử lý tín hiệu](../../brain/assets/LMS_IMG_sensor_processing_flow_image1.png)

**Bước 1:** Đọc dữ liệu cảm biến  
**Bước 2:** Áp dụng EMA + Outlier Rejection  
**Bước 3:** Xử lý logic điều khiển với Hysteresis  
**Bước 4:** Điều chỉnh đầu ra với Slew Rate và Gamma Correction  

---

## Bài tập thực hành

### Worksheet 1: Thiết kế bộ lọc cảm biến

**Yêu cầu:**  
Thiết kế hàm lọc dữ liệu cảm biến ánh sáng sử dụng kết hợp EMA và Outlier Rejection.

**Mẫu mã:**
```cpp
float filterLightSensor(float raw_value, float last_ema, float outlier_threshold) {
    // TODO: Hoàn thiện hàm lọc
}
```

### Worksheet 2: Cài đặt logic điều khiển đèn

**Yêu cầu:**  
Viết chương trình điều khiển đèn LED theo nguyên tắc: chỉ bật khi TỐI và CÓ NGƯỜI, sử dụng Hysteresis.

---

## Câu hỏi kiểm tra

### Câu 1
Hệ số α trong thuật toán EMA nên chọn giá trị nào để triệt nhiễu ánh sáng nhỏ hiệu quả?
- A) 0.05
- B) 0.25
- C) 0.8
- D) 1.0

### Câu 2
Tại sao cần sử dụng cơ chế Outlier Rejection trong xử lý cảm biến?
- A) Tăng tốc độ xử lý
- B) Giảm tiêu thụ điện năng
- C) Ngăn chặn giá trị sai lệch làm vọt EMA
- D) Tăng độ phân giải cảm biến

### Câu 3
Logic AND trong điều khiển giúp đạt được lợi ích gì?
- A) Tăng tốc độ phản hồi
- B) Giảm tỷ lệ báo sai (FPR)
- C) Tiết kiệm pin
- D) Tăng độ sáng LED

---

## Tài liệu tham khảo

- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- Tài liệu Volume v02 - Tối ưu thuật toán IoT/Robotics
- Hướng dẫn lập trình cảm biến ánh sáng và siêu âm
- Tài liệu về kiến trúc hệ thống không chặn (non-blocking architecture)

---

## Ghi chú giảng viên

> **Lưu ý quan trọng:** Học viên cần thực hành trên phần cứng thật để hiểu rõ ảnh hưởng của từng thuật toán. Việc mô phỏng trên phần mềm chỉ mang tính chất minh họa ban đầu.

> **Gợi ý tích hợp:** Kết hợp EMA + Outlier Rejection ở tầng đọc dữ liệu, sau đó dùng Hysteresis ở tầng logic, và cuối cùng là Slew Rate ở tầng xuất lệnh PWM [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).