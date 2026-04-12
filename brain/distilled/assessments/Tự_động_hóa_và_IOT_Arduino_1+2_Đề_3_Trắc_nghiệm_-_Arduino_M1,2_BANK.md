# TEST BANK: Tự_động_hóa_và_IOT_Arduino_1+2_Đề_3_Trắc_nghiệm_-_Arduino_M1,2.md

### Question 1: Những cách cấp nguồn cho Arduino Uno R3? (Nhiều đáp án)
A. Cấp nguồn từ cổng USB.
B. Cấp nguồn thông qua Adapter.
C. Cấp nguồn từ pin thông qua chân V(in).
D. Cấp nguồn từ pin thông qua chân Digital.
E. Cấp nguồn từ pin thông qua chân Analog.
F. Cấp nguồn không dây qua tín hiệu bluetooth.
**Correct:** A, B, C
**Explanation:** Arduino hỗ trợ cấp nguồn qua USB (5V), Jack DC (7-12V) và chân Vin (7-12V). Các chân Digital/Analog và Bluetooth không có chức năng nhận nguồn nuôi mạch.

### Question 2: Phát biểu nào sau đây là sai khi nói về đèn LED đơn?
A. Phần bản to hơn là cực dương, phần bản nhỏ là cực âm
B. Đèn LED là thiết bị output
C. Cực âm của đèn LED được cắm vào chân GND của Arduino
D. Cực dương của đèn LED được cắm vào chân D2-D13 của Arduino
**Correct:** A
**Explanation:** Trong cấu tạo nội tại của LED, phần bản kim loại to hơn là cực âm (Cathode), phần bản nhỏ hơn là cực dương (Anode).

### Question 3: Phát biểu về còi buzzer nào sau đây là SAI ?
A. Còi buzzer có 2 chân kết nối. Chân dài là chân âm; chân ngắn là chân dương.
B. Còi buzzer là một thiết bị có thể phát ra âm thanh.
C. Còi buzzer có khả năng tiếp nhận điện năng và chuyển chúng thành tín hiệu âm thanh.
D. Chân dương của còi buzzer được nối với chân digital từ 2 đến 13 trên Arduino, chân âm được nối với GND.
**Correct:** A
**Explanation:** Quy ước linh kiện điện tử chân dài luôn là cực dương (+), chân ngắn là cực âm (-).

### Question 4: Dây màu cam của servo cắm với chân nào của Arduino?
A. D2-D13
B. 5V
C. GND
D. VIN
**Correct:** A
**Explanation:** Dây màu cam là dây tín hiệu (Signal), cần kết nối với các chân Digital (đặc biệt là các chân PWM) để điều khiển góc quay.

### Question 5: Trong breadboard, những hàng cột nào được nối với nhau?
A. Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng NGANG (25 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng DỌC (5 lỗ) dẫn điện với nhau.
B. Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong từng khu vực A/B/C/D, tất cả các lỗ trong khu vực đó đều dẫn điện với nhau.
C. Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng DỌC (2 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng NGANG (30 lỗ) dẫn điện với nhau.
D. Tất cả các lỗ ở cả 4 khu vực A, B, C, D đều dẫn điện with nhau.
**Correct:** A
**Explanation:** Đây là cấu tạo chuẩn của breadboard: hàng ngang ngoài cùng cho nguồn và hàng dọc ở giữa cho linh kiện.

### Question 6: Để kết nối các chân của Arduino với các các chân của cảm biến hồng ngoại ta sử dụng dây jumper loại nào?
A. Dây âm (-), âm (-).
B. Dây dương (+), dương (+).
C. Dây âm (-), dương (+).
D. Nối trực tiếp chân của cảm biến với Arduino mà không cần dây điện trung gian.
**Correct:** A
**Explanation:** (Lưu ý: Trong ngữ cảnh đề bài này, "âm" tương ứng với đầu Cái/Female, "dương" tương ứng với đầu Đực/Male). Cảm biến hồng ngoại thường có chân đực, Arduino có lỗ cái, nên dùng dây Cái-Cái (Female-Female) nếu cắm trực tiếp.

### Question 7: Cách điều chỉnh độ nhạy của các loại cảm biến là:
A. Dùng tua vít điều chỉnh biến trở (núm vặn màu xanh) trên cảm biến.
B. Dùng băng keo dán lên mặt tấm cảm biến.
C. Nối chân VCC của cảm biến với chân 3,3V để giảm điện áp của cảm biến.
D. Nối chân GND của cảm biến với chân 3,3V để giảm mức chênh lệch điện áp so với chân VCC.
**Correct:** A
**Explanation:** Biến trở tối ưu trên module cảm biến dùng để thay đổi ngưỡng so sánh điện áp, từ đó thay đổi độ nhạy.

### Question 8: Màn hình LCD I2C có mấy chân kết nối và tên gọi của chúng là gì?
A. 4 chân (VCC, GND, SCL, SDA)
B. 4 chân (VCC, GND, LCD, SDA)
C. 4 chân (VCC, GND, LCD, DSA)
D. 4 chân (VCC, GND, SCL, DSA)
**Correct:** A
**Explanation:** Giao tiếp I2C chuẩn gồm 2 dây nguồn (VCC, GND) và 2 dây tín hiệu (SCL - Clock, SDA - Data).

### Question 9: Khi núm điều khiển trên Joystick được gạt lên