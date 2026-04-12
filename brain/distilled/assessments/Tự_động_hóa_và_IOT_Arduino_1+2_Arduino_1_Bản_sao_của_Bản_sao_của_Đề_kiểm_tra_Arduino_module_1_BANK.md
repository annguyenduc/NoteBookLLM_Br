# TEST BANK: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.md

**### Question: Những cách nào sau đây có thể dùng để cấp nguồn cho Arduino Uno R3?**
A. Cấp nguồn từ cổng USB.
B. Cấp nguồn thông qua Adapter.
C. Cấp nguồn từ pin thông qua chân V(in).
D. Cấp nguồn từ pin thông qua chân Digital.
Correct: A, B, C
Explanation: Arduino hỗ trợ cấp nguồn qua USB (5V), Jack DC (7-12V) và chân Vin. Không cấp nguồn trực tiếp vào các chân Digital vì có thể làm hỏng vi điều khiển.

**### Question: Vì sao nên hạn chế sử dụng chân digital số 0 (RX) và 1 (TX)?**
A. Hai chân 0 và 1 là hai chân giao tiếp dùng cho Arduino truyền và nhận dữ liệu nên rất dễ bị nhiễu nếu ta dùng hai chân này như các chân digital thông thường.
B. Trên phần chân digital có tổng cộng 14 chân nên không cần phải sử dụng đến hai chân 0 và 1.
C. Hai chân 0 và 1 dùng để reset chương trình cho Arduino nên không sử dụng hai chân này.
D. Hai chân 0 và 1 chỉ dùng cho cảm biến mưa.
Correct: A
Explanation: Chân 0 và 1 được nối với bộ chuyển đổi Serial-to-USB để nạp code và giao tiếp với máy tính.

**### Question: Một chiếc đèn Led bị gãy chân nên không thể phân biệt các chân bằng chiều dài. Nếu quan sát bản cực bên trong đèn thì phân biệt như thế nào?**
A. Phần (bản) cực bên trong nhỏ hơn là chân dương, phần (bản) cực to hơn là chân âm.
B. Phần (bản) cực bên trong nhỏ hơn là chân âm, phần (bản) cực to hơn là chân dương.
C. Không thể xác định được.
D. Cả 3 đáp án đều sai.
Correct: A
Explanation: Đây là đặc điểm cấu tạo vật lý chuẩn của đèn LED đơn.

**### Question: Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc nào?**
A. Thu và phát ánh sáng hồng ngoại.
B. Thu và phát ánh sáng màu hồng.
C. Phát hiện nhiệt độ của vật cản.
D. Phát hiện ánh sáng màu đỏ.
Correct: A
Explanation: Cảm biến IR phát tia hồng ngoại và đo lượng tia phản xạ ngược lại để xác định vật cản.

**### Question: Đối với cảm biến mưa, để giảm độ nhạy (cần nhiều nước hơn mới báo mưa) thì ta cần làm như thế nào?**
A. Điều chỉnh biến trở (núm vặn màu xanh) trên cảm biến.
B. Dùng băng keo dán lên mặt tấm cảm biến.
C. Nối chân VCC với 3.3V thay vì 5V.
D. Nối chân GND với 3.3V.
Correct: A
Explanation: Biến trở trên module cho phép điều chỉnh ngưỡng so sánh điện áp để thay đổi độ nhạy.

**### Question: Cho mạch Arduino và đèn Led như hình bên dưới, hỏi đoạn chương trình nào dùng để điều khiển cho đèn Led sáng nhấp nháy (sáng-tắt) với chu kỳ 1 giây?**
![image37.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image37.png)
A. Đoạn code có lệnh chờ 1 giây giữa HIGH và LOW.
B. Đoạn code có lệnh chờ 0.5 giây giữa HIGH và LOW.
C. Đoạn code không có lệnh chờ.
D. Đoạn code chỉ có lệnh HIGH.
Correct: A
Explanation: Chu kỳ 1 giây (sáng 1s, tắt 1s) yêu cầu lệnh `wait 1 seconds` sau mỗi trạng thái.

**### Question: Màn hình LCD I2C có mấy chân kết nối và tên gọi của chúng là gì?**
A. 4 chân (VCC, GND, SCL, SDA)
B. 4 chân (VCC, GND, LCD, SDA)
C. 4 chân (VCC, GND, LCD, DSA)
D. 4 chân (VCC, GND, SCL, DSA)
Correct: A
Explanation: Giao tiếp I2C tiêu chuẩn trên LCD sử dụng 2 chân nguồn và 2 chân tín hiệu (SCL, SDA).

**### Question: Nhận định nào sau đây là đúng khi nói về cảm biến siêu âm HC-SR04? (Nhiều đáp án)**
A. Cảm biến gồm 2 đầu trái, phải dùng để phát và thu âm thanh.
B. Đầu bên trái dùng để phát ra sóng siêu âm, đầu bên phải dùng để thu sóng siêu âm.
C. Chân GND của cảm biến được gắn với chân GND ở Arduino.
D. Chân Trig của cảm biến được gắn với chân Digital 2-13 ở Arduino.
Correct: A, C, D
Explanation: HC-SR04 sử dụng sóng siêu âm, chân Trig nhận tín hiệu kích hoạt (Output từ Arduino), chân Echo gửi tín hiệu phản hồi (Input vào Arduino).

**### Question: Hãy gọi tên và sắp xếp thứ tự các chân của mắt thu hồng ngoại VS1838 từ trái sang phải (mặt mắt thu hướng về phía người nhìn)?**
A. VCC - GND - Out
B. VCC - Out - GND
C. GND - VCC - Out
D. Out - GND - VCC
Correct: D
Explanation: Theo sơ đồ chân chuẩn của VS1838: Chân 1 là Out, chân 2 là GND, chân 3 là VCC.

**### Question: Khi núm điều khiển trên Joystick được gạt lên trên, giá trị trục Y sẽ thay đổi như thế nào?**
A. Từ 511 về 0
B. Từ 511 đến 1023
C. Từ -511 đến 0
D. Từ -511 đến 1023
Correct: B (Tùy thuộc vào hướng lắp đặt, nhưng thông thường gạt lên/phải sẽ tăng giá trị).
Explanation: Joystick là biến trở kép, giá trị trả về từ 0 đến 1023.

**### Question: Điền từ thích hợp để chương trình có hiệu ứng 3 đèn nhấp nháy luân phiên (Đèn 1 sáng -> Đèn 2 sáng -> Đèn 3 sáng).**
![image112.gif](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image112.gif)
A. High -