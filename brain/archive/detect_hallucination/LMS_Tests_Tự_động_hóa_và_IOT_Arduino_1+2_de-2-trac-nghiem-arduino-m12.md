ĐỀ KIỂM TRA TRẮC NGHIỆM - Arduino M1+2
(Đề 2)
- 30 câu: 12 nhận biết (40%) - 18 thông hiểu (60%)
- Câu trắc nghiệm 1 đáp án: 1 điểm
- Câu trắc nghiệm nhiều đáp án: Số điểm = số đáp án đúng, đúng 1 câu được 1 điểm
- Điểm đạt: 70% điểm tối đa

Các kiến thức cần đạt
60% M1 = 12 câu
40% M2 = 18 câu | Giáo viên 1 | Giáo viên 1
Các kiến thức cần đạt
60% M1 = 12 câu
40% M2 = 18 câu | Nhận biết
(12 câu) | Thông hiểu / Vận dụng
(18 câu)
Cấu tạo Arduino | 1 | 13
Cấu tạo, cách sử dụng và lập trình các thiết bị output
- Đèn LED
- Còi Buzzer
- Động cơ Servo
(Lập trình: Câu lệnh thực thi + Hiệu ứng  vòng lặp) | 2
3
4 | 14, 15
16
17
Cấu tạo, cách sử dụng Breadboard để lắp mạch Arduino | 5 | 18, 19
Cấu tạo và lập trình thiết bị Input
- Cảm biến hồng ngoại
- Cảm biến ánh sáng
- Cảm biến mưa | 6

7 | 20, 21
22
23
Cấu tạo, cách sử dụng và lập trình màn hình LCD | 8 | 24, 25
Cấu tạo, cách sử dụng và lập trình cảm biến nhiệt độ độ ẩm DHT11 |  | 
Cảm biến siêu âm | 10 | 27
Remote và mắt thu hồng ngoại |  | 
Joystick | 9,11 | 28, 29
Mạch L298 và động cơ vàng, động cơ bơm | 12 | 26,30

Câu 1 (Nhận biết)
Bộ phận nào dùng để gắn dây kết nối với máy tính?
![Visual](media/de-2-trac-nghiem-arduino-m12/rId6.png)
- A/ D
- B/ B
- C/ C
- D/ A
Câu 2 (Nhận biết)
Trong trường hợp chân đèn led bị gãy làm không biết được chân âm - dương qua độ dài của chân đèn thì ta còn có thể dựa vào đặc điểm nào dưới đây?
(Nhiều đáp án)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId7.png)
- A/ Nhìn vào phần (bản) cực bên trong đèn nhỏ hơn là chân dương, phần (bản) cực to hơn là chân âm.
- B/ Nhìn vào phần (bản) cực bên trong đèn nhỏ hơn là chân âm, phần (bản) cực to hơn là chân dương.
- C/ Không thể xác định được chân dương hay chân âm nếu đèn Led bị gãy chân.
- D/ Nối 2 chân gãy vào 2 dây điện đen, đỏ của đế pin 2. Nếu đèn sáng lên thì chân đèn LED nối với dây điện đen là cực âm, chân còn lại là cực dương. 
E/ Nối 2 chân gãy vào 2 dây điện đen, đỏ của đế pin 2. Nếu đèn sáng lên thì chân đèn LED nối với dây điện đen là cực dương, chân còn lại là cực âm.
Câu 3 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về còi Buzzer?
- A/ Chân ngắn của còi buzzer gắn với chân GND của arduino
- B/ Chân dài của còi buzzer gắn với chân GND  của arduino
- C/ Chân ngắn của còi buzzer gắn với cực dương của pin 
- D/ Chân dài của còi buzzer gắn với cực âm của pin
Câu 4 (Nhận biết)
Chọn phát biểu đúng khi nói về động cơ Servo?
- A. Động cơ Servo MG90S có thể xoay từ 0 đến 180 độ và ngược lại.
- B. Động cơ Servo có cấu tạo hoàn toàn giống động cơ DC bình thường, chỉ khác là được tích hợp thêm 1 chân tín hiệu để lập trình thay đổi góc.
- C. Động cơ Servo chỉ có thể xoay góc từ 0 đến 180 độ.
- D. Chân tín hiệu của động cơ Servo được nối với chân tín hiệu analog của Arduino.
Câu 5 (Nhận biết)
Trong breadboard, các dây điện được nối với nhau như thế nào?
![Visual](media/de-2-trac-nghiem-arduino-m12/rId8.png)
- A/ Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng ngang được cách điện với hàng còn lại. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột dọc được cách điện với các cột còn lại.
- B/ Khu vực A và D các lỗ được nối theo cột dọc, mỗi cột được cách điện với cột còn lại. Khu vực B và C các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với các hàng còn lại.
- C/ Khu vực A và D các lỗ được nối theo hàng ngang và theo từng cặp, 5 cặp theo hàng là cách điện nhau . Khu vực B và C các lỗ được nối theo cột, mỗi cột được cách điện với các cột còn lại.
- D/ Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với hàng còn lại và bắt buộc phải nối thiết bị theo cực (+) và cực (-) đã ký hiệu. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột được cách điện với các cột còn lại.
Câu 6 (Nhận biết)
Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc nào?
- A. Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc thu và phát ánh sáng hồng ngoại.
- B. Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc thu và phát ánh sáng màu hồng.
- C. Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc phát hiện nhiệt độ của vật cản.
- D. Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc phát hiện ánh sáng màu đỏ do vật cản phát ra.
Câu 7 (Nhận biết)
Để cảm biến mưa có thể hoạt động được thì cần phải cung cấp lượng điện áp bao nhiêu?
- A/ 5V
- B/ 3V 
- C/ 3,3V
- D/ 1,5V
Câu 8 (Nhận biết)
Đáp án nào sau đây là đúng khi nói về cách kết nối màn hình LCD với Arduino?
- A/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId9.png)
- B/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId10.png)
- C/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId11.png)
- D/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId12.png)
Câu 9 (Nhận biết)
Chân VRx của joystick có tác dụng gì?
- A/ Đo mức độ di chuyển của joystick theo trục X (trục song song với phương của các chân kết nối trên joystick)
- B/ Đo mức độ di chuyển của joystick theo trục X (trục vuông góc với phương của các chân kết nối trên joystick)
- C/ Đo mức độ di chuyển của joystick theo trục Y (trục vuông góc với phương của các chân kết nối trên joystick)
- D/ Đo mức độ di chuyển của joystick theo trục Y (trục song song với phương của các chân kết nối trên joystick)
Câu 10 (Nhận biết)
Nhận định nào sau đây là đúng khi nói về cảm biến siêu âm HC-SR04?
(Nhiều đáp án)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId13.png)
- A/ Đầu bên trái dùng để phát ra sóng siêu âm, đầu bên phải dùng để thu sóng siêu âm.
- B/ Chân GND của cảm biến được gắn với chân GND ở Arduino.
- C/ Chân Trig của cảm biến được gắn với chân Digital 2-13 ở Arduino.
- D/ Chân Echo của cảm biến được gắn với chân Analog 0-5 ở Arduino.
E/ Cảm biến siêu âm HC-SR04 có thể đo khoảng cách đến vật cản từ  2cm đến vô hạn.
F/ Cảm biến gồm 2 đầu trái, phải dùng để phát và thu âm thanh.
G/ Chân VCC của cảm biến được gắn với chân GND ở Arduino.
Câu 11 (Nhận biết)
Khi núm điều khiển trên Joystick được gạt sang trái, giá trị X sẽ thay đổi vào khoảng bao nhiêu?
![Visual](media/de-2-trac-nghiem-arduino-m12/rId14.png)
- A/ từ 512 về 0
- B/ từ 512 đến 1023
- C/ từ -512 đến 0 
- D/ Từ -512 đến 1023
Câu 12 (Nhận biết)
Phát biểu nào sau đây là đúng?
- A/ Tổng số chân kết nối của mạch L298 là 11 chân
- B/ Điện áp hoạt động tối đa của mạch L298 là 5V
- C/ Mạch L298 chỉ điều khiển được 1 thiết bị 
- D/ Điện áp mạch L298 cấp cho thiết bị tối đa là 12V
Câu 13 (Thông hiểu)
Vì sao người ta thường hạn chế sử dụng hai chân số 0 (RX) và 1 (TX) để lấy tín hiệu Digital?
- A/ Hai chân 0 và 1 là hai chân giao tiếp dùng cho Arduino truyền và nhận dữ liệu nên rất dễ bị nhiễu nếu ta dùng hai chân này như các chân digital thông thường.
- B/ Trên phần chân digital có tổng cộng 14 chân nên không cần phải sử dụng đến hai chân 0 và 1.
- C/ Hai chân 0 và 1 dùng để reset chương trình cho Arduino nên không sử dụng hai chân này.
- D/ Hai chân 0 và 1 chỉ dùng cho cảm biến mưa nên phải hạn chế dùng cho các loại cảm biến khác.
Câu 14 (Thông hiểu)
Cho mạch Arduino và đèn Led như hình bên dưới, hỏi đoạn chương trình nào dùng để điều khiển cho đèn Led sáng nhấp nháy (sáng-tắt) với chu kỳ 1 giây?
![Visual](media/de-2-trac-nghiem-arduino-m12/rId15.png)
- A.  B.
![Visual](media/de-2-trac-nghiem-arduino-m12/rId16.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId17.png)
- C. D.
![Visual](media/de-2-trac-nghiem-arduino-m12/rId18.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId19.png)
Câu 15 (Thông hiểu)
Đoạn chương trình nào dưới đây thực hiện yêu cầu sau:
Mạch điện gồm 2 đèn LED xanh, đỏ
Khi khởi động, 2 đèn LED sáng tắt luân phiên nhau mỗi 1 giây. Sau 10 lần sáng tắt luân phiên, đèn LED xanh sáng còn đèn LED đỏ tắt mãi mãi.
Biết các chân tín hiệu được nối như bảng bên dưới.

Linh kiện điện tử | Arduino
Chân dương của LED xanh | D9
Chân dương của LED đỏ | D10

- A/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId20.png)
- B/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId21.png)
- C/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId22.png)
- D/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId23.png)
Câu 16 (Thông hiểu)
Cho mạch điện gồm 2 đèn LED xanh, đỏ và yêu cầu lập trình như sau:
Khi khởi động, 2 đèn LED xanh, đỏ lặp lại 5 lần hành động 2 đèn LED sáng tắt luân phiên mỗi 1 giây. (Khi đèn xanh sáng thì đèn đỏ tắt và ngược lại). Sau 5 lần sáng tắt luân phiên, đèn xanh sáng mãi mãi, trong khi đèn đỏ tắt.
Cho đoạn chương trình như sau:
![Visual](media/de-2-trac-nghiem-arduino-m12/rId24.png)
Biết rằng các chân tín hiệu được nối như bảng bên dưới.

Linh kiện điện tử | Arduino
Chân dương của đèn LED xanh | D9
Chân dương của đèn LED đỏ | D10

Phần chương trình 1, 2 còn thiếu lần lượt là gì để có thể thực hiện yêu cầu trên.
- A/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId25.png)
- B/
- C/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId26.png)
- D/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId27.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId28.png)
Câu 17 (Thông hiểu)
Tìm đoạn chương trình cho kết quả quan sát được động cơ servo MG90S quay theo góc từ góc 0 độ đến góc 150 độ, sau đó, quay ngược lại từ góc 150 độ về góc 0 độ (thời gian ngắt quãng là 1 giây)
- A. B.
![Visual](media/de-2-trac-nghiem-arduino-m12/rId29.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId30.png)
- C.  D.
![Visual](media/de-2-trac-nghiem-arduino-m12/rId31.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId32.png)
Câu 18 (Thông hiểu)
Một bạn học sinh mắc mạch gồm Arduino, đèn Led và breadboard, (quy ước các chân đèn Led được minh họa như hình. Hỏi khi bạn thực hiện chương trình sau thì có những đèn nào phát sáng?
![Visual](media/de-2-trac-nghiem-arduino-m12/rId33.png)
Đây là đoạn chương trình của học sinh đã thực hiện. Hỏi những đèn nào phát sáng với đoạn chương trình trên?
![Visual](media/de-2-trac-nghiem-arduino-m12/rId34.png)
- A. Cả 5 đèn đều sáng.
- B. Chỉ có đèn đỏ và đèn xanh dương sáng.
- C. Chỉ có đèn xanh dương sáng.
- D. Chỉ có đèn đỏ sáng.
E. Chỉ có đèn vàng không sáng.
F. Đèn đỏ, đèn xanh lá và đèn xanh dương sáng.
Câu 19 (Thông hiểu)
Giáo viên cho đoạn chương trình sau và yêu cầu học sinh lắp mạch gồm 1 cảm biến hồng ngoại, 1 breadboard, 1 đèn led hoạt động như sau:
Khi có vật cản thì đèn led sáng
Khi không có vật cản thì đèn led tắt
![Visual](media/de-2-trac-nghiem-arduino-m12/rId35.png)
Một học sinh thực hiện lắp mạch như sau và mạch không hoạt động theo yêu cầu của giáo viên. Hỏi học sinh đã lắp mạch sai ở đâu ?  (Nhiều đáp án)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId36.png)
- A/ Chân dương của đèn Led
- B/ Chân GND của cảm biến
- C/ Chân OUT của cảm biến 
- D/ Chân VCC của cảm biến
Câu 20 (Thông hiểu)
Với mạch điện và đoạn chương trình sau sẽ có hiệu ứng như thế nào?
![Visual](media/de-2-trac-nghiem-arduino-m12/rId37.png)
- A/ Khi không có vật cản, đèn LED tắt. Khi có vật cản, đèn LED sáng - tắt mỗi 0,5s và lặp lại mãi mãi
- B/ Khi không có và có vật cản, đèn LED đều tắt.
- C/ Khi không có vật cản: đèn LED tắt. Khi có vật cản: đèn LED sáng.
- D/ Khi không có và có vật cản, đèn LED đều sáng.
Câu 21 (Thông hiểu)
Yêu cầu lập trình cho cảm biến hồng ngoại như sau:
Khi phát hiện vật cản thì cho đèn Led được nối với chân D8 sáng.
Không có vật cản thì cho đèn Led đó tắt.
Hỏi đoạn chương trình nào dưới đây cho kết quả đúng với yêu cầu của giáo viên, biết chân DO của cảm biến được nối với chân D7.
- A/  B/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId38.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId39.png)
- C/  D/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId40.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId41.png)
Câu 22 (Thông hiểu)
Cho các linh kiện điện tử và các chân kết nối như bảng dưới đây:

Tên linh kiện | Chân kết nối của linh kiện | Chân kết nối của Arduino
Cảm biến ánh sáng | VCC | 5V
Cảm biến ánh sáng | GND | GND
Cảm biến ánh sáng | D0 | D8
Đèn Led | Chân dương | D7
Đèn Led | Chân âm | GND

Chọn chương trình thực hiện đúng yêu cầu nếu trời sáng thì đèn tắt, nếu trời tối thì đèn sáng.
- A/ B/ 
- C/D/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId42.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId43.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId44.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId45.png)
Câu 23 (Thông hiểu)
Cho các linh kiện điện tử và các chân kết nối như bảng dưới đây:

Tên linh kiện | Chân kết nối của linh kiện | Chân kết nối của Arduino
Cảm biến mưa | VCC | 5V
Cảm biến mưa | GND | GND
Cảm biến mưa | D0 | D8
Đèn Led xanh | Chân dương | D7
Đèn Led xanh | Chân âm | GND
Đèn Led đỏ | Chân dương | D6
Đèn Led đỏ | Chân âm | GND
Còi buzzer | Chân dương | D5
Còi buzzer | Chân âm | GND

Cho đoạn chương trình sau, mô tả nào dưới đây đúng với kết quả của chương trình nhất:
![Visual](media/de-2-trac-nghiem-arduino-m12/rId46.png)
- A. Khi trời không mưa thì đèn xanh sáng, đèn đỏ và còi tắt. Khi trời mưa thì đèn xanh sáng tiếp trong 3 giây sau đó tắt;  đèn đỏ sáng lên; còi buzzer báo động hú tắt liên tục (thời gian hú tắt đứt quãng là 1 giây) cho đến khi hết mưa.
- B. Khi trời không có mưa thì đèn đỏ sáng, đèn xanh và còi tắt. Khi trời mưa thì đèn đỏ sáng tiếp trong 3 giây sau đó tắt;  đèn xanh sáng lên và còi buzzer báo động hú tắt liên tục (thời gian hú ngắt quãng là 1 giây) cho đến khi hết mưa.
- C. Khi trời không mưa thì đèn xanh sáng, đèn đỏ tắt, còi tắt. Khi trời mưa thì đèn xanh sáng trong 3 giây sau đó tắt; đèn đỏ sáng lên, sau đó tắt và còi buzzer báo động hú tắt liên tục (thời gian hú ngắt quãng là 1 giây) cho đến khi hết mưa.
- D. Khi trời mưa thì đèn Led màu xanh sáng, đèn đỏ và còi tắt. Khi trời không mưa mưa thì đèn xanh sáng trong 3 giây sau đó tắt;  đèn đỏ sáng lên và còi buzzer báo động hú tắt liên tục (thời gian mỗi lần hú, tắt là 1 giây) cho đến khi trời mưa.
Câu 24 (Thông hiểu)
Đoạn lệnh nào sau đây làm cho màn hình LCD hiện lên dòng chữ như sau?
![Visual](media/de-2-trac-nghiem-arduino-m12/rId47.png)
- A/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId48.png)
- B/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId49.png)
- C/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId50.png)
- D/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId51.png)
Câu 25 (Thông hiểu)
TÌm lỗi sai của đoạn chương trình sau sao cho có hiệu ứng màn hình hiển thị thời gian đếm ngược từ 3 -1.
![Visual](media/de-2-trac-nghiem-arduino-m12/rId52.png)
- A/ Thiếu câu lệnh  trước mỗi lần đổi số.
![Visual](media/de-2-trac-nghiem-arduino-m12/rId53.png)
- B/ Thiếu câu lệnh cho toàn bộ đoạn chương trình
![Visual](media/de-2-trac-nghiem-arduino-m12/rId54.png)
- C/ Thiếu câu lệnh  sau mỗi lần đổi số
![Visual](media/de-2-trac-nghiem-arduino-m12/rId55.png)
- D/ Dư câu lệnh sau mỗi lần đổi số
![Visual](media/de-2-trac-nghiem-arduino-m12/rId56.png)
Câu 26 (Thông hiểu)
Một học sinh lắp mạch điện như sau. Đoạn lập trình sau cho hiệu ứng như thế nào
![Visual](media/de-2-trac-nghiem-arduino-m12/rId57.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId58.png)
- A/ Động cơ quay trong 2 giây, sau đó dừng quay trong 2 giây, lặp lại mãi mãi.
- B/ Động cơ đứng yên mãi mãi.
- C/ Động cơ quay liên tục.
- D/ Động cơ quay theo chiều kim đồng hồ trong 2 giây, sau đó quay ngược chiều kim đồng hồ trong 2 giây, lặp lại mãi mãi.
Câu 27 (Thông hiểu)
Cho mạch điện và đoạn chương trình dưới đây. Điền vào chỗ trống để chương trình có hiệu ứng:
Nếu khoảng cách từ vật cản đến cảm biến nhỏ hơn 20cm thì cả 2 đèn sáng-tắt cùng nhau; Nếu không, thì đèn xanh sáng, đèn đỏ tắt.
![Visual](media/de-2-trac-nghiem-arduino-m12/rId59.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId60.png)
- A/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId61.png)
- B/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId62.png)
- C/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId63.png)
- D/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId64.png)
Câu 28 (Thông hiểu)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId65.png)
Biết mạch điện được nối như sau:

Tên linh kiện | Chân kết nối của linh kiện | Chân kết nối của Arduino
Joystick | VCC | 5V
Joystick | GND | GND
Joystick | VRx | A0
Joystick | VRy | A1
Đèn LED đỏ | Chân dương | D13
Đèn LED xanh | Chân dương | D12
Đèn LED vàng | Chân dương | D11

Đoạn chương trình dưới đây cho hiệu ứng như thế nào?
![Visual](media/de-2-trac-nghiem-arduino-m12/rId66.png)
- A/ Khi kéo joystick theo hướng ngang, qua trái, đèn LED đỏ sẽ sáng.
Khi để joystick ở vị trí cân bằng, đèn LED xanh sẽ sáng.
Khi kéo joystick theo hướng ngang, qua phải, đèn LED vàng sẽ sáng.
- B/ Khi kéo joystick theo hướng ngang, qua trái, đèn LED xanh sẽ sáng.
Khi để joystick ở vị trí cân bằng, đèn LED đỏ sẽ sáng.
Khi kéo joystick theo hướng ngang, qua phải, đèn LED vàng sẽ sáng.
- C/ Khi kéo joystick theo hướng ngang, qua trái, đèn LED vàng sẽ sáng.
Khi để joystick ở vị trí cân bằng, đèn LED xanh sẽ sáng.
Khi kéo joystick theo hướng ngang, qua phải, đèn LED đỏ sẽ sáng.
- D/ Khi kéo joystick theo hướng ngang, qua trái, đèn LED đỏ sẽ sáng.
Khi để joystick ở vị trí cân bằng, đèn LED vàng sẽ sáng.
Khi kéo joystick theo hướng ngang, qua phải, đèn LED xanh sẽ sáng.
Câu 29 (Thông hiểu)
Cho mạch điện Arduino gồm 1 joystick và 1 đèn LED như sau:
![Visual](media/de-2-trac-nghiem-arduino-m12/rId67.png)
Cho yêu cầu lập trình như sau:
- Khi cần gạt joystick nằm ở vị trí trung tâm, không di chuyển, đèn LED sẽ tắt.
- Khi gạt joystick đến vị trí bất kỳ, đèn LED sẽ sáng.
- Chương trình lặp lại mãi mãi.
Một học sinh lập trình như sau:
![Visual](media/de-2-trac-nghiem-arduino-m12/rId68.png)
Hãy chọn đoạn lệnh còn thiếu để điền vào chỗ trống để lập trình được yêu cầu trên.
- A/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId69.png)
- B/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId70.png)
- C/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId71.png)
- D/
![Visual](media/de-2-trac-nghiem-arduino-m12/rId72.png)
Câu 30 (Thông hiểu)
Một học sinh chế tạo một chiếc xe hoạt động bằng Arduino, mạch L298, động cơ vàng và điều khiển bằng remote hồng ngoại như mạch điện như hình dưới.
![Visual](media/de-2-trac-nghiem-arduino-m12/rId73.png)
Biết rằng sau khi học sinh test bằng đoạn lệnh sau và nhấn phím 2 trên remote hồng ngoại, xe đã xoay tròn ngược chiều kim đồng hồ.
![Visual](media/de-2-trac-nghiem-arduino-m12/rId74.png)
![Visual](media/de-2-trac-nghiem-arduino-m12/rId75.png)
Hỏi cũng với chương trình trên, để xe chạy tiến thẳng, ta cần nhấn phím nào trên remote hồng ngoại?
- A/ Phím 6
- B/ Phím 8
- C/ Phím 4
- D/ Phím 5