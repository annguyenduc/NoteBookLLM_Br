# TEST BANK: Tự_động_hóa_và_IOT_Arduino_1+2_Đề_4_Trắc_nghiệm_-_Arduino_M1,2.md

### Question: Câu 1 (Nhận biết): Nối tên với các bộ phận tương ứng của board mạch Arduino.
![image37.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Đề_4_Trắc_nghiệm_-_Arduino_M1,2.docx_image37.png)
A. A-Nút reset, B-Cổng USB, C-Jack DC, D-Chân nguồn, E-Chân tín hiệu
B. A-Cổng USB, B-Nút reset, C-Jack DC, D-Chân tín hiệu, E-Chân nguồn
C. A-Jack DC, B-Cổng USB, C-Nút reset, D-Chân nguồn, E-Chân tín hiệu
D. A-Nút reset, B-Jack DC, C-Cổng USB, D-Chân tín hiệu, E-Chân nguồn
Correct: A
Explanation: Theo sơ đồ Arduino Uno: A là nút Reset, B là cổng USB Type B, C là Jack nguồn DC, D là dãy chân nguồn (Power), E là dãy chân tín hiệu (Digital/Analog).

### Question: Câu 2 (Nhận biết): Một chiếc đèn Led bị gãy chân nên không thể phân biệt các chân của đèn Led bằng chiều dài được. Nếu quan sát bằng cách nhìn bên trong đèn thì phải phân biệt như thế nào?
A. Phần (bản) cực bên trong nhỏ hơn là chân dương, phần (bản) cực to hơn là chân âm.
B. Phần (bản) cực bên trong nhỏ hơn là chân âm, phần (bản) cực to hơn là chân dương.
C. Không thể xác định được chân dương hay chân âm nếu đèn Led bị gãy chân.
D. Cả 3 đáp án đều sai.
Correct: A
Explanation: Cấu tạo vật lý bên trong lớp vỏ nhựa của LED: Bản cực nhỏ là Anode (+), bản cực lớn hình cái chén là Cathode (-).

### Question: Câu 3 (Nhận biết): Phát biểu nào sau đây là đúng khi nói về còi Buzzer?
A. Chân ngắn của còi buzzer gắn với chân GND của arduino
B. Chân dài của còi buzzer gắn với chân GND của arduino
C. Chân ngắn của còi buzzer gắn với cực dương của pin 
D. Chân dài của còi buzzer gắn với cực âm của pin
Correct: A
Explanation: Còi Buzzer có cực tính, chân ngắn là cực âm nên phải nối với GND.

### Question: Câu 4 (Nhận biết): Cách mắc servo với mạch Arduino theo thứ tự dây nâu/dây đỏ/dây cam nào dưới đây là đúng ?
A. GND/5V/D2 → D13
B. 5V/GND/D2→D13
C. D2→D13/GND/5V
D. D2→D13/5V/GND
Correct: A
Explanation: Quy ước màu dây Servo: Nâu = GND, Đỏ = VCC (5V), Cam = Signal (nối vào các chân Digital từ 2 đến 13).

### Question: Câu 5 (Nhận biết): Breadboard kết nối với nhau theo quy tắc nào?
A. Khu vực 1 và 4 dòng điện đi theo hàng dọc.
B. Khu vực 1 và 4 dòng điện đi theo hàng ngang. 
C. Khu vực 2 và 3 dòng điện đi theo hàng dọc.
D. Khu vực 1 và 3 dòng điện đi theo hàng ngang.
Correct: B, C
Explanation: Trên breadboard thông dụng, hai dải ngoài cùng (1 và 4) thường dùng làm đường nguồn nối ngang, các dải ở giữa (2 và 3) nối dọc theo từng cột 5 lỗ.

### Question: Câu 6 (Nhận biết): Ứng dụng nào sau đây không phải của cảm biến hồng ngoại?
A. Đo thân nhiệt con người thông qua ánh sáng hồng ngoại.
B. Robot tránh vật cản.
C. Đèn thông minh tự phát sáng khi có người đến.
D. Cửa tự động mở khi có người đến.
Correct: A
Explanation: Cảm biến hồng ngoại trong bộ kit Arduino cơ bản thường là loại thu phát (Proximity) dùng để phát hiện vật cản, không phải loại cảm biến nhiệt độ hồng ngoại chuyên dụng để đo thân nhiệt.

### Question: Câu 7 (Nhận biết): Biết điện áp hoạt động của cảm biến mưa là 5V. Nếu nối chân VCC của cảm biến mưa với chân 3,3V của Arduino thì sẽ có hiện tượng gì xảy ra?
A. Cảm biến sẽ hoạt động không chính xác.
B. Cảm biến sẽ bị cháy ngay lập tức.
C. Không xảy ra hiện tượng gì, cảm biến vẫn hoạt động bình thường.
D. Nguồn điện sẽ không còn đủ năng lượng để cho đèn led hay động cơ hoạt động.
Correct: A
Explanation: Khi cấp thiếu áp, các linh kiện bán dẫn và mạch so sánh trên cảm biến không đủ điều kiện hoạt động định mức dẫn đến sai số hoặc không phản hồi.

### Question: Câu 8 (Nhận biết): Cách lắp mạch nào dưới đây là đúng?
![image54.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Đề_4_Trắc_nghiệm_-_Arduino_M1,2.docx_image54.png)
A. Hình A
B. Hình B
C. Hình C
D. Hình D
Correct: A
Explanation: (Dựa trên hình ảnh thực tế của đề bài - Hình A thường thể hiện đúng cực tính LED và điện trở hạn dòng).

### Question: Câu 9 (Nhận biết): Joystick gồm có bao nhiêu chân kết nối?
A. 5
B. 4
C. 3
D. 2
Correct: A
Explanation: Module Joystick chuẩn cho Arduino có 5 chân: GND, +5V, VRx, VRy, SW.

### Question: Câu 10 (Nhận biết): Câu lệnh nào phù hợp với cách lắp mạch dưới đây?
![image62.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Đề_4_Trắc_nghiệm_-_Arduino_M1,2.docx_image62.png)
A. digitalWrite(13, HIGH);
B. analogRead(A0);
C. servo.write(90);
D. digitalRead(7);
Correct: A
Explanation: Hình ảnh hiển thị LED nối vào chân 13, câu lệnh digitalWrite dùng để xuất tín hiệu điều khiển LED.

### Question: Câu 11 (Nhận biết): Khi núm điều khiển trên Joystick được gạt sang trái, giá trị X sẽ thay đổi vào khoảng bao nhiêu?
A. từ 512 về 0
B. từ 512 đến 1023
C. từ -512 đến 0 
D. Từ -512 đến 512
Correct: A
Explanation: Giá trị Analog mặc định là 512, gạt sang một hướng trục X sẽ giảm về 0, hướng ngược lại tăng lên 1023.

### Question: Câu 12 (Nhận biết): Điện áp đầu ra tối đa của mạch L298 là bao nhiêu?
A. 5V
B. 3,3V
C. 3V
D. 12V
Correct: D
Explanation: Mạch L298N hỗ trợ điều khiển động cơ với điện áp lên đến 12V (thậm chí cao hơn tùy phiên bản, nhưng 12V là mức phổ biến trong giáo trình).

### Question: Câu 13 (Thông hiểu): Phương án nào sau đây KHÔNG PHẢI là cách cấp nguồn cho Arduino? (Nhiều đáp án)
A. Gắn cực dương của nguồn điện vào chân 5V của Arduino, gắn cực âm của nguồn điện vào chân GND.
B. Gắn cực dương của nguồn điện vào chân 3