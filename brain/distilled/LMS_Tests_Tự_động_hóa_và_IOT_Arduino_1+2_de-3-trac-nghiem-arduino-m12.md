ĐỀ KIỂM TRA TRẮC NGHIỆM - Arduino M1+2
(Đề 3)
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
Những cách cấp nguồn cho Arduino Uno R3?
(Nhiều đáp án)
- A. Cấp nguồn từ cổng USB.
- B. Cấp nguồn thông qua Adapter.
- C. Cấp nguồn từ pin thông qua chân V(in).
- D. Cấp nguồn từ pin thông qua chân Digital.
E. Cấp nguồn từ pin thông qua chân Analog.
F. Cấp nguồn không dây qua tín hiệu bluetooth.
Câu 2 (Nhận biết)
Phát biểu nào sau đây là sai khi nói về đèn LED đơn?
![Visual](media/de-3-trac-nghiem-arduino-m12/rId7.png)
- A/ Phần bản to hơn là cực dương, phần bản nhỏ là cực âm
- B/ Đèn LED là thiết bị output
- C/ Cực âm của đèn LED được cắm vào chân GND của Arduino
- D/ Cực dương của đèn LED được cắm vào chân D2-D13 của Arduino
Câu 3 (Nhận biết)
Phát biểu về còi buzzer nào sau đây là SAI ?
- A/ Còi buzzer có 2 chân kết nối. Chân dài là chân âm; chân ngắn là chân dương.
- B/ Còi buzzer là một thiết bị có thể phát ra âm thanh.
- C/ Còi buzzer có khả năng tiếp nhận điện năng và chuyển chúng thành tín hiệu âm thanh.
- D/ Chân dương của còi buzzer được nối với chân digital từ 2 đến 13 trên Arduino, chân âm được nối với GND.
Câu 4 (Nhận biết)
Dây màu cam của servo cắm với chân nào của Arduino?
- A/ D2-D13
- B/ 5V
- C/ GND
- D/ VIN
Câu 5 (Nhận biết)
Trong breadboard, những hàng cột nào được nối với nhau?
![Visual](media/de-3-trac-nghiem-arduino-m12/rId8.png)
- A/ Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng NGANG (25 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng DỌC (5 lỗ) dẫn điện với nhau.
- B/ Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong từng khu vực A/B/C/D, tất cả các lỗ trong khu vực đó đều dẫn điện với nhau.
- C/ Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng DỌC (2 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng NGANG (30 lỗ) dẫn điện với nhau.
- D/ Tất cả các lỗ ở cả 4 khu vực A, B, C, D đều dẫn điện với nhau.
Câu 6 (Nhận biết)
Để kết nối các chân của Arduino với các các chân của cảm biến hồng ngoại ta sử dụng dây jumper loại nào?
- A. Dây âm (-), âm (-).
- B. Dây dương (+), dương (+).
- C. Dây âm (-), dương (+).
- D. Nối trực tiếp chân của cảm biến với Arduino mà không cần dây điện trung gian.
Câu 7 (Nhận biết)
Cách điều chỉnh độ nhạy của các loại cảm biến là:
- A/ Dùng tua vít điều chỉnh biến trở (núm vặn màu xanh) trên cảm biến.
- B/ Dùng băng keo dán lên mặt tấm cảm biến.
- C/ Nối chân VCC của cảm biến với chân 3,3V để giảm điện áp của cảm biến.
- D/ Nối chân GND của cảm biến với chân 3,3V để giảm mức chênh lệch điện áp so với chân VCC.
Câu 8 (Nhận biết)
Màn hình LCD I2C có mấy chân kết nối và tên gọi của chúng là gì?
- A/ 4 chân (VCC, GND, SCL, SDA)
- B/ 4 chân (VCC, GND, LCD, SDA)
- C/ 4 chân (VCC, GND, LCD, DSA)
- D/ 4 chân (VCC, GND, SCL, DSA)
Câu 9 (Nhận biết)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId9.png)
Khi núm điều khiển trên Joystick được gạt lên trên, giá trị Y sẽ thay đổi vào khoảng bao nhiêu?
- A/ từ 511 về 0
- B/ từ 511 đến 1023
- C/ từ -511 đến 0 
- D/ Từ -511 đến 1023
Câu 10 (Nhận biết)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId10.png)
Nối chân kết nối của cảm biến siêu âm ở cột trái với chức năng ở cột phải sao cho phù hợp
(Dạng ghép nối)
Đáp án

Cột trái | Cột phải
Chân VCC | Chân cấp nguồn dương cho cảm biến
Chân GND | Chân sẽ được nối vào cực âm của nguồn điện hoặc chân GND của arduino
Chân Trig | Chân liên kết đến mắt trái của cảm biến siêu âm, dùng để phát tín hiệu
Chân Echo | Chân liên kết đến mắt phải của cảm biến siêu âm, nhận tín hiệu

Câu 11 (Nhận biết)
Joystick gồm có bao nhiêu chân kết nối?
- A/ 5
- B/ 4
- C/ 3
- D/ 2
Câu 12 (Nhận biết)
Nhận định nào sau đây là đúng khi nói về cách kết nối mạch L298, động cơ với Arduino và nguồn điện?
(Nhiều đáp án)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId11.png)
- A/ Nguồn điện 4 pin trực tiếp cấp điện cho mạch L298; Arduino được cấp điện gián tiếp, thông qua mạch L298.
- B/ Động cơ M1 được kết nối với chân pin D12,D13 của Arduino; Động cơ M2 được kết nối với chân pin D7,D8 của Arduino.
- C/ Cách nối mạch điện như trên sẽ làm động cơ hoạt động yếu.
- D/ Cách nối mạch điện như trên là dư thừa, vì mỗi động cơ chỉ cần kết nối với 1 chân Digital trên Arduino.
E/ Nguồn điện 4 pin cùng lúc trực tiếp cấp điện cho mạch L298 và Arduino.
F/ Động cơ M1 được kết nối với chân pin D7,D8 của Arduino; Động cơ M2 được kết nối với chân pin D12,D13 của Arduino.
Câu 13 (Thông hiểu)
Phương án nào sau đây KHÔNG PHẢI là cách cấp nguồn cho Arduino?
(Nhiều đáp án)
- A/ Gắn cực dương của nguồn điện vào chân 5V của Arduino, gắn cực âm của nguồn điện vào chân GND.
- B/ Gắn cực dương của nguồn điện vào chân 3V của Arduino, gắn cực âm của nguồn điện vào chân GND.
- C/ Gắn cực dương của nguồn điện vào chân VIN của Arduino, gắn cực âm của nguồn điện vào chân GND.
- D/ Sử dụng dây cáp USB type B, kết nối giữa Arduino với máy tính.
Câu 14 (Thông hiểu)
Đoạn chương trình nào dưới đây cho hiệu ứng 2 đèn sáng tắt luân phiên (thời gian sáng, tắt mỗi đèn là 1 giây)?
![Visual](media/de-3-trac-nghiem-arduino-m12/rId12.gif)
- A.    B.
![Visual](media/de-3-trac-nghiem-arduino-m12/rId13.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId14.png)
- C.  D.
![Visual](media/de-3-trac-nghiem-arduino-m12/rId15.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId16.png)
Câu 15 (Thông hiểu)
Quan sát mạch điện dưới đây và điền số thích hợp vào chỗ trống theo thứ tự từ trên xuống dưới trong đoạn chương trình sao cho các đèn led có hiệu ứng giống đèn giao thông (Led xanh sáng trong 7 giây, Led vàng sáng trong 2 giây, Led đỏ sáng trong 5 giây) ?
![Visual](media/de-3-trac-nghiem-arduino-m12/rId17.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId18.png)
- A/ 8 - 9 - 5
- B/ 8 -10 - 5
- C/ 9 -8 - 2
- D/ 9 - 10 - 2
Câu 16 (Thông hiểu)
Chọn đáp án sai: để lập trình cho còi liên tục phát ra tiếng hú, ta dùng đoạn chương trình nào sau đây?
![Visual](media/de-3-trac-nghiem-arduino-m12/rId19.gif)

A |  | C | 
B |  | D | 

Câu 17 (Thông hiểu)
Chọn chương trình đúng với mô tả sau: Khi Arduino khởi động, động cơ Servo ở góc 0 độ, đèn LED sáng. Sau 2 giây, động cơ Servo ở góc 180 độ, đèn LED tắt. Sau 2 giây, trở lại trạng thái như khi Arduino khởi động.
- A/           B/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId24.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId25.png)
- C/  D/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId26.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId27.png)
Câu 18 (Thông hiểu)
Cách lắp mạch điện nào sau đây cho hiệu ứng đèn đỏ và xanh sáng cùng lúc
- A/   B/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId28.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId29.png)
- C/  D/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId30.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId31.png)
Câu 19 (Thông hiểu)
Một bạn học sinh mắc mạch gồm Arduino, 5 đèn Led và Breadboard, (quy ước các chân đèn Led được minh họa như hình dưới đây)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId32.png)
Biết rằng các chân tín hiệu được nối như bảng bên dưới.

Linh kiện điện tử | Arduino
Chân dương của đèn LED đỏ | D12
Chân dương của đèn LED xanh lá | D11
Chân dương của đèn LED xanh dương | D10
Chân dương của đèn LED xám | D9
Chân dương của đèn LED vàng | D8

Hỏi khi bạn thực hiện chương trình sau thì có những đèn nào phát sáng ?
![Visual](media/de-3-trac-nghiem-arduino-m12/rId33.png)
- A/ Chỉ đèn xanh dương sáng
- B/ Chỉ có đèn xanh dương và đèn đỏ sáng
- C/ Chỉ có đèn đỏ, đèn xanh lá cây và đèn xám sáng 
- D/ Chỉ có đèn vàng không sáng.
Câu 20 (Thông hiểu)
Yêu cầu lập trình cho cảm biến hồng ngoại, đèn Led và còi hoạt động như sau:
- Khi không có vật cản, đèn xanh sáng, đèn đỏ tắt, còi tắt.
- Khi có vật cản, còi kêu, đèn đỏ sáng và đèn xanh sáng tắt luân phiên với nhau.
Biết các chân tín hiệu được nối như bảng bên dưới.

Linh kiện điện tử | Arduino
Chân DO của cảm biến hồng ngoại | D7
Chân dương của còi buzzer | D12
Chân dương của đèn xanh | D8
Chân dương của đèn đỏ | D9

Phát biểu nào sau đây là đúng khi nói về đoạn chương trình sau đây.
(Nhiều đáp án)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId34.png)
- A/ Câu lệnh điều kiện ở dòng (5) dùng sai chân pin DO của cảm biến hồng ngoại
- B/ Khi có vật cản, thiếu câu lệnh cho đèn Led xanh sáng khi làm hiệu ứng 2 đèn sáng tắt luân phiên, cần thêm một câu lệnh làm đèn xanh sáng ở giữa dòng (9) và (10).
- C/ Câu lệnh điều kiện ở dòng (1) và (5) xét sai điều kiện có/không có người của cảm biến siêu âm, cần đảo 2 giá trị 1, 0 ở 2 phần (1) và (5) với nhau.
- D/ Câu lệnh (6), (8), (10) dùng sai chân pin của còi buzzer và đèn LED đỏ. Chân pin ở câu lệnh (6) có chân pin là 9, câu lệnh (8), (10) có chân pin là 12.
E/ Chương trình không hoạt động được, phải sử dụng câu lệnh if...then...else thay cho câu lệnh if...then.
Câu 21 (Thông hiểu)
Giáo viên đưa ra yêu cầu lập trình cho cảm biến hồng ngoại như sau: Khi phát hiện vật cản thì cho đèn Led được nối với chân D8 sáng, còn không có vật cản thì cho đèn Led đó tắt. Hỏi đoạn chương trình nào dưới đây cho kết quả đúng với yêu cầu của giáo viên, biết chân DO của cảm biến được nối với chân D7.
- A.  B.
![Visual](media/de-3-trac-nghiem-arduino-m12/rId35.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId36.png)
- C.  D.
![Visual](media/de-3-trac-nghiem-arduino-m12/rId37.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId38.png)
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
![Visual](media/de-3-trac-nghiem-arduino-m12/rId39.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId40.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId41.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId42.png)
Câu 23 (Thông hiểu)
Mạch điện gồm cảm biến mưa, đèn led và còi buzzer được nối như sau:

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

Chọn đáp án mô tả đúng nhất của đoạn chương trình sau
![Visual](media/de-3-trac-nghiem-arduino-m12/rId43.png)
Khi  ___ thì đèn xanh sáng, đèn đỏ và còi tắt. Khi  ___ thì đèn đỏ sáng lên, trong khi đèn xanh ___ , sau đó còi buzzer báo động hú tắt liên tục (thời gian hú tắt đứt quãng là 1 giây) cho đến khi  ___ thì dừng lại.
- A/ trời không mưa - trời mưa - sáng trong 3 giây rồi tắt - trời không mưa
- B/ trời mưa - trời không mưa - sáng trong 3 giây rồi tắt - trời mưa
- C/ trời không mưa - trời mưa - tắt - trời không mưa
- D/ trời mưa - trời không mưa - tắt - trời không mưa
Câu 24 (Thông hiểu)
Cho đoạn lệnh và yêu cầu như sau:
Yêu cầu:
- Mạch điện Arduino gồm 1 cảm biến mưa, 2 đèn LED đỏ, xanh và 1 cảm biến mưa.
- 2 đèn LED đỏ, xanh: 
  + Đèn xanh luôn bật cho thấy chương trình có hoạt động.
+ Khi có mưa, đèn đỏ sáng. Khi không có mưa, đèn đỏ tắt.
- Màn hình LCD:
  + Khi có mưa, màn hình hiển thị “CO MUA”
  + Khi không có mưa, màn hình hiển thị “KHONG CO MUA”
Đoạn lệnh:
![Visual](media/de-3-trac-nghiem-arduino-m12/rId44.png)
Hãy chọn số chân tương ứng với thiết bị so với yêu cầu và đoạn lệnh như trên.
(Dạng ghép nối)
Đáp án

Cột trái | Cột phải
Chân dương đèn LED đỏ | D13
Chân dương đèn LED xanh | D12
Chân DO/OUT của cảm biến mưa | D9
Chân SDA của màn hình LCD | A4
Chân SCL của màn hình LCD | A5
 | A0
 | A1
 | A2
 | A3
 | Chân Analog bất kỳ
 | Chân Digital bất kỳ

Câu 25 (Thông hiểu)
Đoạn lệnh nào sau đây làm cho màn hình LCD hiện lên dòng chữ như sau?
![Visual](media/de-3-trac-nghiem-arduino-m12/rId45.gif)
- A/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId46.png)
- B/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId47.png)
- C/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId48.png)
- D/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId49.png)
Câu 26 (Thông hiểu)
Cho mạch 1 mạch được lắp như hình.
![Visual](media/de-3-trac-nghiem-arduino-m12/rId50.png)
Biết rằng sau khi học sinh thử nghiệm chiều xoay của 2 động cơ bằng đoạn lệnh sau, xe đã đi tới.
![Visual](media/de-3-trac-nghiem-arduino-m12/rId51.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId52.png)
Chọn hướng chuyển động của xe tương ứng với chương trình.
(Dạng ghép nối)
Đáp án

Cột trái | Cột phải
 | Chạy lùi
 | Xoay ngược chiều kim đồng hồ
 | Xoay cùng chiều kim đồng hồ

Câu 27 (Thông hiểu)
Cho sơ đồ nối mạch dưới đây, đoạn chương trình nào cho kết quả quan sát được khi khoảng cách của cảm biến siêu âm nhỏ hơn 30 cm, đèn LED sáng nhấp nháy, ngược lại thì đèn LED tắt.

Thiết bị/linh kiện | Chân kết nối của thiết bị/linh kiện | Chân kết nối của Arduino
Cảm biến siêu âm | VCC | 5V
Cảm biến siêu âm | GND | GND
Cảm biến siêu âm | Trig | 10
Cảm biến siêu âm | Echo | 9
LED | Chân dương | 8
LED | Chân âm | GND

- A/ B/ 
- C/ D/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId56.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId57.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId58.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId59.png)
Câu 28 (Thông hiểu)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId9.png)
Điều khiển 3 đèn LED bằng joystick theo yêu cầu sau:
- Khi kéo joystick theo hướng ngang, qua trái, đèn LED đỏ sẽ sáng, đèn vàng, cam tắt.
- Khi để joystick ở vị trí cân bằng, đèn LED cam sẽ sáng, đèn đỏ, vàng tắt.
- Khi kéo joystick theo hướng ngang, qua phải, đèn LED vàng sẽ sáng, đèn đỏ, cam tắt.

Thiết bị/linh kiện | Chân kết nối của thiết bị/linh kiện | Chân kết nối của Arduino
Joystick | VCC | 5V
Joystick | GND | GND
Joystick | VRx | A0
Joystick | VRy | A1
LED vàng | Chân dương | D11
LED vàng | Chân âm | GND
LED cam | Chân dương | D12
LED cam | Chân âm | GND
LED đỏ | Chân dương | D13
LED đỏ | Chân âm | GND

Cho đoạn chương trình như sau:
![Visual](media/de-3-trac-nghiem-arduino-m12/rId60.png)
Hãy điền vào các vị trí trống nội dung thích hợp
(Dạng ghép nối)
Đáp án

Cột trái | Cột phải
1 | 0 (A0)
2 | OR
3 | Q > 600
4 | low
5 | high
6 | low
 | AND
 | Q < 300
 | 1 (A1)

Câu 29 (Thông hiểu)
Cho mạch điện gồm 1 joystick, 1 servo với chương trình có hiệu ứng: Nếu giá trị VRx > 700 thì xoay servo góc 120 độ. Nếu giá trị VRx < 300 thì xoay servo góc 45 độ.
![Visual](media/de-3-trac-nghiem-arduino-m12/rId61.png)
Các chân linh kiện được nối như thế nào?
- A/ Chân VRX: A1
Dây cam: D11
- B/ Chân VRX: D1
Dây cam: D11
- C/ Chân VRX: A1
Dây cam: D1
- D/ Chân VRX: A11
Dây cam: D1
Câu 30 (Thông hiểu)
Một học sinh chế tạo một chiếc xe hoạt động bằng Arduino, mạch L298 và động cơ vàng như mạch điện như hình dưới.
![Visual](media/de-3-trac-nghiem-arduino-m12/rId50.png)
Biết rằng sau khi học sinh thử nghiệm chiều xoay của 2 động cơ bằng đoạn lệnh sau, xe đã xoay tròn ngược chiều kim đồng hồ.
![Visual](media/de-3-trac-nghiem-arduino-m12/rId62.png)
![Visual](media/de-3-trac-nghiem-arduino-m12/rId63.png)
Hỏi để điều chỉnh cho xe chạy thẳng khi khởi động, ta có thể sử dụng đoạn lệnh nào sau đây?
- A/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId64.png)
- B/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId65.png)
- C/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId66.png)
- D/
![Visual](media/de-3-trac-nghiem-arduino-m12/rId67.png)