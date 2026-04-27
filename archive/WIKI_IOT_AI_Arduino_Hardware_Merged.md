---
file_id: "WIKI_IOT_AI_Arduino_Hardware"
title: "Phần cứng & Kết nối IOT AI Arduino"
category: "Hardware Wiki"
prefix: "WIKI"
tags: ['AI', 'Arduino', 'mBlock', 'Extensions', 'Cloud']
source: "`IOT_AI_Arduino_de_trac_nghiem_1_-_ai_arduino.md`, `IOT_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md`"
status: "verified"
created: "2026-04-24"
---

# 🔌 Phần cứng & Kết nối IOT AI Arduino

Học phần này tập trung vào việc sử dụng máy tính làm "não bộ AI" và Arduino làm "cánh tay thực thi".

---

## 1. Các phần mở rộng AI (mBlock Extensions)

Để sử dụng AI trong mBlock, ta cần thêm các phần mở rộng chuyên dụng:
- **Cognitive Services (Dịch vụ nhận thức)**: Cung cấp các thuật toán AI có sẵn. Chạy trên Cloud, yêu cầu Internet.
- **Teachable Machine (Máy học)**: Cho phép người dùng huấn luyện mô hình (Hình ảnh, Âm thanh, Tư thế).
- **Machine Learning**: Công cụ tạo mô hình phân loại dữ liệu dựa trên các lớp (Classes).

## 2. Yêu cầu hệ thống & Kết nối

### 2.1. Kết nối Internet (Cloud)
- **BẮT BUỘC**: Các dịch vụ AI yêu cầu máy tính phải có kết nối Internet để gửi dữ liệu xử lý.
- **Chế độ Lập trình (Live Mode)**: AI chỉ hoạt động ở chế độ **Live**. Khi ở chế độ này, Arduino phải luôn kết nối với máy tính để "mượn" sức mạnh xử lý của PC và Internet.
- **Hạn chế của Upload Mode**: Không thể chạy các khối lệnh AI (Cognitive Services) trực tiếp trên Arduino ở chế độ Upload vì board mạch không có kết nối Internet và RAM/CPU yếu.

### 2.2. Thiết bị thuộc về Máy tính (Laptop/PC)
Các thiết bị này dùng để thu thập dữ liệu cho các Extension AI chạy trên mBlock:
- **Camera (Webcam)**: Dùng để thu hình ảnh cho các bài toán Thị giác máy tính (Nhận diện khuôn mặt, vật thể).
- **Microphone**: Dùng để thu âm thanh cho các bài toán nhận diện giọng nói.

### 2.3. Thiết bị thuộc về Arduino & Kết nối
- **Cổng kết nối**: 
    - Đầu máy tính: Cổng **USB - Type A**.
    - Đầu Arduino: Cổng **USB - Type B**.
- **Cáp kết nối**: Dùng để nạp code và giao tiếp dữ liệu giữa PC và Arduino.
- **Arduino**: Nhận lệnh thực thi sau khi AI đã xử lý xong trên máy tính.
- **Cảm biến & Cơ cấu chấp hành**: (Xem chi tiết tại mục 4).

---

## 3. Các thông số kỹ thuật cần nhớ
- **Độ tin cậy (Confidence)**: Chỉ số từ 0 đến 1 (hoặc 0-100%) cho biết AI chắc chắn bao nhiêu phần trăm về kết quả nhận diện.
- **Baudrate**: Tốc độ giao tiếp chuẩn thường dùng là **115200** để đảm bảo truyền nhận dữ liệu AI/IOT mượt mà.

## 4. Quy tắc Vật lý & Đấu nối cảm biến

Trong các dự án AI Arduino (như Smart Home), các linh kiện sau thường được sử dụng phối hợp:

### 4.1. Cảm biến đầu vào (Inputs)
- **Cảm biến PIR (Hồng ngoại chuyển động)**: Nhận bức xạ hồng ngoại từ các vật thể phát ra nhiệt để phát hiện chuyển động.
- **Cảm biến Siêu âm**: Đo khoảng cách.

### 4.2. Cơ cấu chấp hành (Outputs)
- **Relay (Rơ-le)**: Thiết bị đóng ngắt điện công suất lớn.
    - **COM**: Chân chung (Common).
    - **NO**: Thường mở (Normally Open).
    - **NC**: Thường đóng (Normally Closed).
- **Servo**: Quay theo góc để đóng/mở cửa tự động.

> [!CAUTION]
> **CẢNH BÁO AN TOÀN**: Trong các dự án học đường, chỉ nên sử dụng Relay để điều khiển các thiết bị điện áp thấp (5V, 12V). Tuyệt đối **KHÔNG** tự ý kết nối với điện lưới 220V nếu không có sự giám sát của giáo viên chuyên môn.

### 4.3. Quy tắc "Bất di bất dịch" (Physical Golden Rules)
- **GND Hợp nhất (Common Ground)**: BẮT BUỘC nối chung cực âm (GND) của Arduino với nguồn nuôi cảm biến/Relay bên ngoài.
- **Chống nhiễu**: Không đặt Camera quá gần các thiết bị phát sóng mạnh hoặc động cơ công suất lớn để tránh làm nhiễu tín hiệu AI.

---

## 🛡️ Nguồn xác thực (Audit Trail)
- [AUDITOR] **Verified** — Đã đối soát 100% với nguồn RAW (Rule 14).
- 📖 Nguồn: `IOT_AI_Arduino_de_trac_nghiem_1_-_ai_arduino.md` — [Câu 5: Yêu cầu Internet]
- 📖 Nguồn: `IOT_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md` — [Câu 12: Quy trình TM, Câu 17: PIR, Câu 22: Relay]
- 📖 Nguồn: `IOT_AI_Arduino_de_2_trac_nghiem_-_ai_arduino.md` — [Câu 8: Độ tin cậy]
- 📖 Nguồn: `WIKI_IOT_Arduino_Hardware` — [Rule: GND Hợp nhất]
