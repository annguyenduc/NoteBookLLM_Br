---
file_id: "WIKI_IOT_Arduino_Logic"
title: "Tư duy Lập trình IOT Arduino"
category: "Logic Wiki"
prefix: "WIKI"
tags: ['mBlock', 'Logic', 'Programming', 'Algorithms', 'Robot_Logic']
source: "[[120_Cau_Hoi_IOT_Arduino_LMS]]"
status: "verified"
created: "2026-04-24"
---

# 🧠 Tư duy Lập trình IOT Arduino (mBlock)

Wiki này tổng hợp các mô thức logic (Design Patterns) thường gặp nhất trong 120 câu hỏi IOT Arduino, tập trung vào cách vận hành của mBlock.

---

## 1. Logic Điều khiển Tuần tự (Sequential Logic)

Đây là nền tảng của các dự án Đèn giao thông và Hệ thống cảnh báo.
- **Quy tắc**: Lệnh `Đợi (Wait)` quyết định nhịp điệu.
- **Lỗi thường gặp**: Quên khối `Đợi`, khiến mắt người không nhìn thấy sự thay đổi của LED (LED bật và tắt quá nhanh).

---

## 2. Cấu trúc Vòng lặp (Loop Architecture)

Mọi dự án Arduino đều bắt đầu với cấu trúc:
- **Khối khởi động (Setup)**: Khai báo chân Pin, Init LCD, Baudrate Serial.
- **Vòng lặp Mãi mãi (Forever/Loop)**: Nơi chứa logic chính chạy lặp đi lặp lại.

---

## 3. Logic Xe Robot (L298 / Motor Driver)

Xe robot sử dụng 2 chân Digital (IN1, IN2) để điều khiển 1 động cơ.
- **Tiến**: IN1 = CAO, IN2 = THẤP (hoặc ngược lại).
- **Lùi**: Đảo ngược trạng thái của Tiến.
- **Dừng**: IN1 = THẤP, IN2 = THẤP.
- **Xoay tại chỗ**: 1 bánh tiến, 1 bánh lùi.

---

## 4. Logic Hiển thị và Giao tiếp (LCD & Serial)

- **Serial Monitor**: Dùng tốc độ **Baudrate 9600**. Rất quan trọng để gỡ lỗi (in giá trị cảm biến ra màn hình để xem).
- **LCD I2C**: 
    - Phải có lệnh **Khởi tạo (init)** ở đầu chương trình.
    - Địa chỉ cột (0-15), dòng (0-1).
    - Phải dùng lệnh **Xóa (Clear)** khi muốn thay đổi nội dung hiển thị để không bị ghi đè chữ cũ.

---

## 5. Hệ thống Đa nhiệm Quy mô lớn (Scalable Multi-tasking)

Khi dự án có nhiều thiết bị (4+ thiết bị) hoạt động song song, chúng ta không thể dùng khối `Đợi` vì nó làm "đứng hình" toàn bộ hệ thống.

### 5.1. Kỹ thuật dùng Bộ đếm thời gian (Timer)
Thay vì dùng `Đợi`, ta dùng một biến để ghi lại thời điểm thực hiện hành động cuối cùng.
- **Logic**: `Nếu <(Thời gian hệ thống) - (Biến_Thời_Gian_Cũ) > (Khoảng_Chờ)> thì làm việc`.

### 5.2. Mô hình Đa nhiệm cho Chế độ Upload (Upload Mode)
Do mBlock ở chế độ Upload không hỗ trợ Danh sách (Lists) mặc định, chúng ta sử dụng **Chiến thuật Biến rời thông minh**:

1.  **Quy ước đặt tên (Naming Prefix)**: Đặt tên biến kèm số thứ tự để chúng tự động sắp xếp cạnh nhau trong bảng quản lý:
    - `t1_led_do`, `t2_led_xanh`, `t3_sensor`...
2.  **Mô hình My Blocks**: Chia code vào **Khối của tôi** (My Blocks) để code sạch sẽ và có thể bật/tắt các tính năng dễ dàng.

### 5.3. Dự án mẫu: 3 LED Độc lập (Red - Green - Yellow)
Mục tiêu: Đỏ (500ms), Xanh (1000ms), Vàng (2000ms) chạy song song không đợi nhau.

**1. Biến số:**
- `t_do`, `t_xanh`, `t_vang` (Lưu thời gian cũ).
- `s_do`, `s_xanh`, `s_vang` (Lưu trạng thái 0/1).

**2. Logic trong My Blocks (Ví dụ đèn Đỏ):**
- Định nghĩa `Chớp_Đèn_Đỏ`:
    - `Nếu <(Thời gian hệ thống) - t_do > 0.5> thì:`
        - `Đặt s_do = 1 - s_do` (Logic đảo trạng thái)
        - `Xuất tín hiệu Digital chân [9] giá trị (s_do)`
        - `Đặt t_do = (Thời gian hệ thống)`

**3. Chương trình chính:**
- `Mãi mãi:`
    - `Gọi Chớp_Đèn_Đỏ`
    - `Gọi Chớp_Đèn_Xanh`
    - `Gọi Chớp_Đèn_Vàng`

**Kết quả:** Hệ thống chạy mượt mà, các đèn không đợi nhau, phản ứng tức thì.

> [!IMPORTANT]
> **Lưu ý về quy mô:** Khi quản lý từ 10 thiết bị đa nhiệm trở lên ở chế độ Upload, số lượng biến số sẽ bùng nổ (cần ít nhất 20-30 biến). Lúc này, kỷ luật đặt tên biến (Prefix như `t1_`, `t2_`) là yếu tố sống còn để tránh sai sót.

---

## 6. Cẩm nang Gỡ lỗi (Common Debugging Patterns)

Khi gặp câu hỏi "Tại sao chương trình không chạy?", hãy kiểm tra 4 điểm:
1.  **Sai chân (Pin Mismatch):** Khai báo chân 9 nhưng cắm dây chân 10.
2.  **Ngược logic:** Cảm biến hồng ngoại có vật cản trả về **0**, không vật trả về **1** (hoặc ngược lại).
3.  **Thiếu khối Đợi:** Các hành động đè lên nhau khiến thiết bị không kịp phản hồi.
4.  **Thiếu khối nạp nguồn:** Chưa nối chung GND giữa Arduino và nguồn ngoài (Pin 9V).

---

## 7. Quy trình Máy học & AI (Machine Learning Workflow)

Để triển khai trí tuệ nhân tạo trên Arduino, chúng ta tuân thủ quy trình 3 bước:

### 7.1. Giai đoạn 1: Lấy mẫu (Learning)
- Thu thập dữ liệu hình ảnh/âm thanh theo các **Lớp (Classes)**. 
- Mẫu càng đa dạng (nhiều góc độ, điều kiện ánh sáng), mô hình càng thông minh.

### 7.2. Giai đoạn 2: Huấn luyện (Training)
- Máy sẽ tự tìm quy luật từ các mẫu đã học.
- **Epochs**: Số lần máy quét lại toàn bộ dữ liệu để học. Epochs cao giúp máy học kỹ nhưng tốn thời gian. (Nguồn: Đề AI 4 - Câu 10).

### 7.3. Giai đoạn 3: Nhận diện (Recognition)
- Khi đưa một vật thể mới vào, máy sẽ trả về kết quả kèm chỉ số **Độ tin cậy (Confidence)** từ 0 đến 1 (hoặc 0-100%). (Nguồn: Đề AI 2 - Câu 8).

## 8. Dịch vụ Trí tuệ Đám mây (Cognitive Services)
- **OCR (Optical Character Recognition)**: Nhận diện chữ viết từ ảnh, trả về kiểu dữ liệu **String**. (Nguồn: Đề AI 2 - Câu 12).
- **TTS (Text-to-Speech)**: Máy tính "đọc" văn bản thành tiếng nói.
- **STT (Speech-to-Text)**: Máy tính "nghe" giọng nói và chuyển thành văn bản.

---

## 📖 Nguồn tham khảo (Traceability)
- [Rule 14] Đã xác nhận fact từ 120 câu hỏi LMS và 238 câu hỏi AI Arduino.
- **Trích dẫn:** `MCQ_IOT_AI_De1_Q18`, `MCQ_IOT_AI_De2_Q08`, `MCQ_IOT_AI_De4_Q10`, `MCQ_IOT_AI_De2_Q12`.
