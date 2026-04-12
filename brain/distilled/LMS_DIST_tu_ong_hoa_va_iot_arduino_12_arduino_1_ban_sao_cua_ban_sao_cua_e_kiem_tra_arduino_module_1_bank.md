---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_1_ban_sao_cua_ban_sao_cua_e_kiem_tra_arduino_module_1_bank
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Tests tu ong hoa va iot arduino 12 arduino 1 ban sao cua ban sao cua e kiem tra arduino module 1 bank

# TEST BANK: Arduino Module 1 Assessment

**Mã tài liệu:** LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_1_ban_sao_cua_ban_sao_cua_e_kiem_tra_arduino_module_1_bank  
**Chuyên mục:** Đánh giá kiến thức Arduino  
**Trạng thái:** Đã chuẩn hóa theo tiêu chuẩn LOM v4.4 Supreme

---

## Mô tả tổng quan

Bộ câu hỏi kiểm tra này đánh giá kiến thức cơ bản về Arduino Uno R3, bao gồm các chủ đề: cấp nguồn, chân GPIO, cảm biến, mạch điều khiển LED và lập trình cơ bản. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu hỏi trắc nghiệm

### Câu 1: Cấp nguồn cho Arduino Uno R3

**Câu hỏi:** Những cách nào sau đây có thể dùng để cấp nguồn cho Arduino Uno R3?

**Lựa chọn:**
- A. Cấp nguồn từ cổng USB
- B. Cấp nguồn thông qua Adapter
- C. Cấp nguồn từ pin thông qua chân V(in)
- D. Cấp nguồn từ pin thông qua chân Digital

**Đáp án đúng:** A, B, C  
**Giải thích:** Arduino hỗ trợ cấp nguồn qua USB (5V), Jack DC (7-12V) và chân Vin. Không cấp nguồn trực tiếp vào các chân Digital vì có thể làm hỏng vi điều khiển. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 2: Chức năng chân RX và TX

**Câu hỏi:** Vì sao nên hạn chế sử dụng chân digital số 0 (RX) và 1 (TX)?

**Lựa chọn:**
- A. Hai chân 0 và 1 là hai chân giao tiếp dùng cho Arduino truyền và nhận dữ liệu nên rất dễ bị nhiễu nếu ta dùng hai chân này như các chân digital thông thường
- B. Trên phần chân digital có tổng cộng 14 chân nên không cần phải sử dụng đến hai chân 0 và 1
- C. Hai chân 0 và 1 dùng để reset chương trình cho Arduino nên không sử dụng hai chân này
- D. Hai chân 0 và 1 chỉ dùng cho cảm biến mưa

**Đáp án đúng:** A  
**Giải thích:** Chân 0 và 1 được nối với bộ chuyển đổi Serial-to-USB để nạp code và giao tiếp với máy tính. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 3: Xác định cực của đèn LED

**Câu hỏi:** Một chiếc đèn Led bị gãy chân nên không thể phân biệt các chân bằng chiều dài. Nếu quan sát bản cực bên trong đèn thì phân biệt như thế nào?

**Lựa chọn:**
- A. Phần (bản) cực bên trong nhỏ hơn là chân dương, phần (bản) cực to hơn là chân âm
- B. Phần (bản) cực bên trong nhỏ hơn là chân âm, phần (bản) cực to hơn là chân dương
- C. Không thể xác định được
- D. Cả 3 đáp án đều sai

**Đáp án đúng:** A  
**Giải thích:** Đây là đặc điểm cấu tạo vật lý chuẩn của đèn LED đơn. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 4: Nguyên lý hoạt động cảm biến hồng ngoại

**Câu hỏi:** Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc nào?

**Lựa chọn:**
- A. Thu và phát ánh sáng hồng ngoại
- B. Thu và phát ánh sáng màu hồng
- C. Phát hiện nhiệt độ của vật cản
- D. Phát hiện ánh sáng màu đỏ

**Đáp án đúng:** A  
**Giải thích:** Cảm biến IR phát tia hồng ngoại và đo lượng tia phản xạ ngược lại để xác định vật cản. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 5: Điều chỉnh độ nhạy cảm biến mưa

**Câu hỏi:** Đối với cảm biến mưa, để giảm độ nhạy (cần nhiều nước hơn mới báo mưa) thì ta cần làm như thế nào?

**Lựa chọn:**
- A. Điều chỉnh biến trở (núm vặn màu xanh) trên cảm biến
- B. Dùng băng keo dán lên mặt tấm cảm biến
- C. Nối chân VCC với 3.3V thay vì 5V
- D. Nối chân GND với 3.3V

**Đáp án đúng:** A  
**Giải thích:** Biến trở trên module cho phép điều chỉnh ngưỡng so sánh điện áp để thay đổi độ nhạy. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 6: Điều khiển LED nhấp nháy

**Câu hỏi:** Cho mạch Arduino và đèn Led như hình bên dưới, hỏi đoạn chương trình nào dùng để điều khiển cho đèn Led sáng nhấp nháy (sáng-tắt) với chu kỳ 1 giây?

![Sơ đồ mạch Arduino và LED](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image37.png)

**Lựa chọn:**
- A. Đoạn code có lệnh chờ 1 giây giữa HIGH và LOW
- B. Đoạn code có lệnh chờ 0.5 giây giữa HIGH và LOW
- C. Đoạn code không có lệnh chờ
- D. Đoạn code chỉ có lệnh HIGH

**Đáp án đúng:** A  
**Giải thích:** Chu kỳ 1 giây (sáng 1s, tắt 1s) yêu cầu lệnh `delay(1000)` sau mỗi trạng thái. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 7: Kết nối màn hình LCD I2C

**Câu hỏi:** Màn hình LCD I2C có mấy chân kết nối và tên gọi của chúng là gì?

**Lựa chọn:**
- A. 4 chân (VCC, GND, SCL, SDA)
- B. 4 chân (VCC, GND, LCD, SDA)
- C. 4 chân (VCC, GND, LCD, DSA)
- D. 4 chân (VCC, GND, SCL, DSA)

**Đáp án đúng:** A  
**Giải thích:** Giao tiếp I2C tiêu chuẩn trên LCD sử dụng 2 chân nguồn và 2 chân tín hiệu (SCL, SDA). [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 8: Cảm biến siêu âm HC-SR04

**Câu hỏi:** Nhận định nào sau đây là đúng khi nói về cảm biến siêu âm HC-SR04? (Nhiều đáp án)

**Lựa chọn:**
- A. Cảm biến gồm 2 đầu trái, phải dùng để phát và thu âm thanh
- B. Đầu bên trái dùng để phát ra sóng siêu âm, đầu bên phải dùng để thu sóng siêu âm
- C. Chân GND của cảm biến được gắn với chân GND ở Arduino
- D. Chân Trig của cảm biến được gắn với chân Digital 2-13 ở Arduino

**Đáp án đúng:** A, C, D  
**Giải thích:** HC-SR04 sử dụng sóng siêu âm, chân Trig nhận tín hiệu kích hoạt (Output từ Arduino), chân Echo gửi tín hiệu phản hồi (Input vào Arduino). [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 9: Sắp xếp chân mắt thu hồng ngoại VS1838

**Câu hỏi:** Hãy gọi tên và sắp xếp thứ tự các chân của mắt thu hồng ngoại VS1838 từ trái sang phải (mặt mắt thu hướng về phía người nhìn)?

**Lựa chọn:**
- A. VCC - GND - Out
- B. VCC - Out - GND
- C. GND - VCC - Out
- D. Out - GND - VCC

**Đáp án đúng:** D  
**Giải thích:** Theo sơ đồ chân chuẩn của VS1838: Chân 1 là Out, chân 2 là GND, chân 3 là VCC. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 10: Giá trị trục Y của Joystick

**Câu hỏi:** Khi núm điều khiển trên Joystick được gạt lên trên, giá trị trục Y sẽ thay đổi như thế nào?

**Lựa chọn:**
- A. Từ 511 về 0
- B. Từ 511 đến 1023
- C. Từ -511 đến 0
- D. Từ -511 đến 1023

**Đáp án đúng:** B  
**Giải thích:** Joystick là biến trở kép, giá trị trả về từ 0 đến 1023. Gạt lên/phải sẽ tăng giá trị. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 11: Hiệu ứng 3 đèn nhấp nháy luân phiên

**Câu hỏi:** Điền từ thích hợp để chương trình có hiệu ứng 3 đèn nhấp nháy luân phiên (Đèn 1 sáng -> Đèn 2 sáng -> Đèn 3 sáng).

![Hiệu ứng 3 đèn nhấp nháy](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image112.gif)

**Lựa chọn:**
- A. High - Low - Low
- B. Low - High - Low  
- C. Low - Low - High
- D. High - High - High

**Đáp án đúng:** A, B, C (theo thứ tự)  
**Giải thích:** Chương trình tuần tự bật từng đèn một và tắt các đèn còn lại để tạo hiệu ứng luân phiên. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Thống kê bài kiểm tra

| Số lượng câu hỏi | Loại câu hỏi | Thời gian khuyến nghị |
|------------------|--------------|----------------------|
| 11 câu | Trắc nghiệm đa lựa chọn | 45 phút |

**Mức độ khó:** Cơ bản  
**Đối tượng học viên:** Người mới bắt đầu với Arduino  
**Kỹ năng đánh giá:** Kiến thức phần cứng, lập trình cơ bản, hiểu biết cảm biến [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)