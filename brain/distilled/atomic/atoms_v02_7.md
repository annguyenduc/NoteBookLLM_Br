Dựa trên nguồn dữ liệu **Volume v02**, dưới đây là các sự kiện (Facts) kỹ thuật đã được trích xuất và tổng hợp để tối ưu hóa thuật toán cho hệ thống IoT/Robotics của bạn:

### 1. Tối ưu hóa xử lý dữ liệu cảm biến (Filtering)
- **Fact:** Thuật toán **EMA (Exponential Moving Average)** với hệ số $\alpha \approx 0.25$ giúp triệt nhiễu ánh sáng nhỏ, tránh tình trạng LED nhấp nháy.
  - **Source:** [vv02 - Section: Tại sao thuật toán này tối ưu? / 8) Checklist lỗi thường gặp]
  - **Tag:** [vv02]
- **Fact:** Sử dụng **Median-3 (Trung vị của 3 mẫu)** cho cảm biến siêu âm để loại bỏ các giá trị đo "nhảy" do phản xạ bề mặt hoặc nhiễu tức thời.
  - **Source:** [vv02 - Section: Tại sao thuật toán này tối ưu?]
  - **Tag:** [vv02]
- **Fact:** Cơ chế **Lọc Outlier**: Nếu $|L_x - L_{ema}| > L_{outlier}$ (ngưỡng thường từ 20-50), mẫu đó sẽ bị bỏ qua để tránh các giá trị sai lệch cực mạnh làm vọt EMA.
  - **Source:** [vv02 - Section: 3) Cách xử lý đúng / I. Biến cho cảm biến ánh sáng]
  - **Tag:** [vv02]

### 2. Tối ưu hóa logic điều khiển (Control Logic)
- **Fact:** Áp dụng **Hysteresis (Trễ nhiệt/ngưỡng)** cho cả ánh sáng và siêu âm để hệ thống không bị đổi trạng thái liên tục khi giá trị ở vùng biên (lưng chừng ngưỡng).
  - **Source:** [vv02 - Section: Tại sao thuật toán này tối ưu?]
  - **Tag:** [vv02]
- **Fact:** Sử dụng logic **AND** (Chỉ bật khi TỐI **và** CÓ NGƯỜI) để giảm tỷ lệ báo sai (FPR - False Positive Rate), giúp hệ thống ổn định hơn.
  - **Source:** [vv02 - Section: Tại sao thuật toán này tối ưu?]
  - **Tag:** [vv02]
- **Fact:** **Hiệu chuẩn thích nghi (Auto-calibration)**: Đo giá trị sáng nhất ($L_{bright}$) và tối nhất ($L_{dark}$) trong 10-15 giây đầu để tính toán ngưỡng động: $mid = (L_{bright} + L_{dark})/2$ và $gap = max(120, 0.1 \times dải\_thực)$.
  - **Source:** [vv02 - Section: 6) Hiệu chuẩn nhanh]
  - **Tag:** [vv02]

### 3. Tối ưu hóa đầu ra PWM (Output Smoothing)
- **Fact:** **Slew Rate (Giới hạn tốc độ thay đổi)**: Sử dụng biến `pwm_step` (ví dụ = 8) để LED tăng/giảm độ sáng từ từ, chống nhảy số đột ngột khi có vật lướt qua cảm biến.
  - **Source:** [vv02 - Section: 3) Tính độ sáng LED theo môi trường]
  - **Tag:** [vv02]
- **Fact:** **Gamma Correction**: Sử dụng công thức $L_{norm} = L_{norm}^{L_{gamma}}$ (với $L_{gamma} \approx 1.4 - 2.0$) để điều chỉnh độ sáng mượt mà hơn theo cảm nhận của mắt người.
  - **Source:** [vv02 - Section: 3) Tính độ sáng LED theo môi trường]
  - **Tag:** [vv02]
- **Fact:** **Mapping PWM**: Khối "xuất ra giá trị analog" trên app.ohstem.vn dùng thang 0-100. Cần chuyển đổi từ dải cảm biến (0-4095) sang 0-100 bằng công thức: $pwm = (L_{val} / 4095) \times 100$.
  - **Source:** [vv02 - Section: Câu này giá trị tự động map...]
  - **Tag:** [vv02]

### 4. Tối ưu hóa kiến trúc hệ thống (Architecture)
- **Fact:** **Non-blocking (Không chặn)**: Thay thế các lệnh `delay` dài bằng cơ chế lập lịch theo sự kiện hoặc kiểm tra định kỳ (ví dụ: mỗi 0.1s - 0.2s) để đảm bảo hệ thống phản ứng nhanh.
  - **Source:** [vv02 - Section: 10 tối ưu quan trọng / 8) Checklist lỗi thường gặp]
  - **Tag:** [vv02]
- **Fact:** **Lựa chọn chân cắm (Pinout)**: Trên Yolo UNO, chân **D13** hỗ trợ PWM tốt cho LED, trong khi chân **D3** thường được dành cho I2C SDA (có điện trở kéo lên) nên không chạy được PWM.
  - **Source:** [vv02 - Section: Tôi dùng chân D13 được, D3 thì lại không chạy]
  - **Tag:** [vv02]
- **Fact:** **Fail-safe**: Nếu mất kết nối Internet/AI, hệ thống phải tự động rơi về chế độ điều khiển bằng luật cục bộ (if-else/hysteresis) để duy trì hoạt động.
  - **Source:** [vv02 - Section: 7) Cơ chế fail-safe & tự phục hồi]
  - **Tag:** [vv02]

---
**Gợi ý từ @scout:** Để tối ưu nhất, bạn nên kết hợp **EMA + Outlier Rejection** ở tầng đọc dữ liệu, sau đó dùng **Hysteresis** ở tầng logic, và cuối cùng là **Slew Rate** ở tầng xuất lệnh PWM. Điều này tạo ra một "chuỗi xử lý sạch" từ đầu vào đến đầu ra.