---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_e_4_trac_nghiem___arduino_m12_bank
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Tests tu ong hoa va iot arduino 12 e 4 trac nghiem   arduino m12 bank

# TEST BANK: TỰ ĐỘNG HÓA VÀ IOT ARDUINO - MODULE 1&2
**Mã tài liệu:** LMS_Tests_tu_ong_hoa_va_iot_arduino_12_e_4_trac_nghiem___arduino_m12_bank  
**Loại tài liệu:** Đánh giá/Trắc nghiệm  
**Trạng thái:** Đã chuẩn hóa theo LOM v4.4 Supreme  

---

## BẢNG MÔ TẢ CHUNG

| Thuộc tính | Giá trị |
|------------|---------|
| **Tên tài liệu** | Ngân hàng câu hỏi trắc nghiệm - Arduino Module 1 & 2 |
| **Chủ đề** | Tự động hóa và IoT với Arduino |
| **Mức độ** | Nhận biết & Thông hiểu |
| **Số lượng câu hỏi** | 13 câu |
| **Hình thức đánh giá** | Trắc nghiệm khách quan |
| **Nguồn gốc** | [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

---

## BÀI KIỂM TRA CHI TIẾT

### Câu 1: Nhận biết - Cấu trúc phần cứng Arduino
**Nội dung:** Nối tên với các bộ phận tương ứng của board mạch Arduino.

![Sơ đồ Arduino Uno](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Đề_4_Trắc_nghiệm_-_Arduino_M1,2_image37.png)

**Lựa chọn:**
- A. A-Nút reset, B-Cổng USB, C-Jack DC, D-Chân nguồn, E-Chân tín hiệu
- B. A-Cổng USB, B-Nút reset, C-Jack DC, D-Chân tín hiệu, E-Chân nguồn
- C. A-Jack DC, B-Cổng USB, C-Nút reset, D-Chân nguồn, E-Chân tín hiệu
- D. A-Nút reset, B-Jack DC, C-Cổng USB, D-Chân tín hiệu, E-Chân nguồn

**Đáp án đúng:** A  
**Giải thích:** Theo sơ đồ Arduino Uno: A là nút Reset, B là cổng USB Type B, C là Jack nguồn DC, D là dãy chân nguồn (Power), E là dãy chân tín hiệu (Digital/Analog). [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 2: Nhận biết - Cấu tạo LED
**Nội dung:** Một chiếc đèn Led bị gãy chân nên không thể phân biệt các chân của đèn Led bằng chiều dài được. Nếu quan sát bằng cách nhìn bên trong đèn thì phải phân biệt như thế nào?

**Lựa chọn:**
- A. Phần (bản) cực bên trong nhỏ hơn là chân dương, phần (bản) cực to hơn là chân âm.
- B. Phần (bản) cực bên trong nhỏ hơn là chân âm, phần (bản) cực to hơn là chân dương.
- C. Không thể xác định được chân dương hay chân âm nếu đèn Led bị gãy chân.
- D. Cả 3 đáp án đều sai.

**Đáp án đúng:** A  
**Giải thích:** Cấu tạo vật lý bên trong lớp vỏ nhựa của LED: Bản cực nhỏ là Anode (+), bản cực lớn hình cái chén là Cathode (-). [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 3: Nhận biết - Kết nối Buzzer
**Nội dung:** Phát biểu nào sau đây là đúng khi nói về còi Buzzer?

**Lựa chọn:**
- A. Chân ngắn của còi buzzer gắn với chân GND của arduino
- B. Chân dài của còi buzzer gắn với chân GND của arduino
- C. Chân ngắn của còi buzzer gắn với cực dương của pin
- D. Chân dài của còi buzzer gắn với cực âm của pin

**Đáp án đúng:** A  
**Giải thích:** Còi Buzzer có cực tính, chân ngắn là cực âm nên phải nối với GND. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 4: Nhận biết - Kết nối Servo
**Nội dung:** Cách mắc servo với mạch Arduino theo thứ tự dây nâu/dây đỏ/dây cam nào dưới đây là đúng?

**Lựa chọn:**
- A. GND/5V/D2 → D13
- B. 5V/GND/D2→D13
- C. D2→D13/GND/5V
- D. D2→D13/5V/GND

**Đáp án đúng:** A  
**Giải thích:** Quy ước màu dây Servo: Nâu = GND, Đỏ = VCC (5V), Cam = Signal (nối vào các chân Digital từ 2 đến 13). [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 5: Nhận biết - Cấu trúc Breadboard
**Nội dung:** Breadboard kết nối với nhau theo quy tắc nào?

**Lựa chọn:**
- A. Khu vực 1 và 4 dòng điện đi theo hàng dọc.
- B. Khu vực 1 và 4 dòng điện đi theo hàng ngang.
- C. Khu vực 2 và 3 dòng điện đi theo hàng dọc.
- D. Khu vực 1 và 3 dòng điện đi theo hàng ngang.

**Đáp án đúng:** B, C  
**Giải thích:** Trên breadboard thông dụng, hai dải ngoài cùng (1 và 4) thường dùng làm đường nguồn nối ngang, các dải ở giữa (2 và 3) nối dọc theo từng cột 5 lỗ. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 6: Nhận biết - Ứng dụng cảm biến hồng ngoại
**Nội dung:** Ứng dụng nào sau đây không phải của cảm biến hồng ngoại?

**Lựa chọn:**
- A. Đo thân nhiệt con người thông qua ánh sáng hồng ngoại.
- B. Robot tránh vật cản.
- C. Đèn thông minh tự phát sáng khi có người đến.
- D. Cửa tự động mở khi có người đến.

**Đáp án đúng:** A  
**Giải thích:** Cảm biến hồng ngoại trong bộ kit Arduino cơ bản thường là loại thu phát (Proximity) dùng để phát hiện vật cản, không phải loại cảm biến nhiệt độ hồng ngoại chuyên dụng để đo thân nhiệt. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 7: Nhận biết - Nguồn điện cho cảm biến
**Nội dung:** Biết điện áp hoạt động của cảm biến mưa là 5V. Nếu nối chân VCC của cảm biến mưa với chân 3,3V của Arduino thì sẽ có hiện tượng gì xảy ra?

**Lựa chọn:**
- A. Cảm biến sẽ hoạt động không chính xác.
- B. Cảm biến sẽ bị cháy ngay lập tức.
- C. Không xảy ra hiện tượng gì, cảm biến vẫn hoạt động bình thường.
- D. Nguồn điện sẽ không còn đủ năng lượng để cho đèn led hay động cơ hoạt động.

**Đáp án đúng:** A  
**Giải thích:** Khi cấp thiếu áp, các linh kiện bán dẫn và mạch so sánh trên cảm biến không đủ điều kiện hoạt động định mức dẫn đến sai số hoặc không phản hồi. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 8: Nhận biết - Lắp mạch LED
**Nội dung:** Cách lắp mạch nào dưới đây là đúng?

![Lắp mạch LED](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Đề_4_Trắc_nghiệm_-_Arduino_M1,2_image54.png)

**Lựa chọn:**
- A. Hình A
- B. Hình B
- C. Hình C
- D. Hình D

**Đáp án đúng:** A  
**Giải thích:** Hình A thể hiện đúng cực tính LED và điện trở hạn dòng. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 9: Nhận biết - Chân kết nối Joystick
**Nội dung:** Joystick gồm có bao nhiêu chân kết nối?

**Lựa chọn:**
- A. 5
- B. 4
- C. 3
- D. 2

**Đáp án đúng:** A  
**Giải thích:** Module Joystick chuẩn cho Arduino có 5 chân: GND, +5V, VRx, VRy, SW. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 10: Nhận biết - Câu lệnh Arduino
**Nội dung:** Câu lệnh nào phù hợp với cách lắp mạch dưới đây?

![Mạch LED chân 13](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Đề_4_Trắc_nghiệm_-_Arduino_M1,2_image62.png)

**Lựa chọn:**
- A. digitalWrite(13, HIGH);
- B. analogRead(A0);
- C. servo.write(90);
- D. digitalRead(7);

**Đáp án đúng:** A  
**Giải thích:** Hình ảnh hiển thị LED nối vào chân 13, câu lệnh digitalWrite dùng để xuất tín hiệu điều khiển LED. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 11: Nhận biết - Giá trị Joystick
**Nội dung:** Khi núm điều khiển trên Joystick được gạt sang trái, giá trị X sẽ thay đổi vào khoảng bao nhiêu?

**Lựa chọn:**
- A. từ 512 về 0
- B. từ 512 đến 1023
- C. từ -512 đến 0
- D. Từ -512 đến 512

**Đáp án đúng:** A  
**Giải thích:** Giá trị Analog mặc định là 512, gạt sang một hướng trục X sẽ giảm về 0, hướng ngược lại tăng lên 1023. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 12: Nhận biết - Điện áp L298
**Nội dung:** Điện áp đầu ra tối đa của mạch L298 là bao nhiêu?

**Lựa chọn:**
- A. 5V
- B. 3,3V
- C. 3V
- D. 12V

**Đáp án đúng:** D  
**Giải thích:** Mạch L298N hỗ trợ điều khiển động cơ với điện áp lên đến 12V (thậm chí cao hơn tùy phiên bản, nhưng 12V là mức phổ biến trong giáo trình). [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 13: Thông hiểu - Cấp nguồn Arduino
**Nội dung:** Phương án nào sau đây KHÔNG PHẢI là cách cấp nguồn cho Arduino? (Nhiều đáp án)

**Lựa chọn:**
- A. Gắn cực dương của nguồn điện vào chân 5V của Arduino, gắn cực âm của nguồn điện vào chân GND.
- B. Gắn cực dương của nguồn điện vào chân 3...

**Ghi chú:** Câu hỏi chưa hoàn chỉnh trong nguồn gốc. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## HƯỚNG DẪN SỬ DỤNG

### Đối với giảng viên:
- Sử dụng ngân hàng câu hỏi này để tạo đề kiểm tra module 1&2 Arduino
- Có thể trộn câu hỏi để tạo nhiều phiên bản đề khác nhau
- Kết hợp với thực hành để đánh giá toàn diện

### Đối với học viên:
- Ôn tập các kiến thức cơ bản về Arduino
- Hiểu rõ cấu trúc phần cứng và nguyên lý hoạt động
- Chuẩn bị tốt cho kỳ thi thực hành

---

## THÔNG TIN BẢN QUYỀN

**Tài liệu học tập chuẩn LOM v4.4 Supreme**  
**Phát triển bởi Content Engineering Team**  
**Nguồn tham khảo chính: [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)**