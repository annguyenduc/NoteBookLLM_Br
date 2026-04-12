# LMS KNOWLEDGE BASE (IOT Focus)\n\n


## Source: Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino.md
### 1. FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact] ::** Arduino có thể được cấp nguồn thông qua cổng USB (kết nối máy tính), Jack DC (adapter 9V) hoặc chân Vin. :: [Arduino_Power]*   **[LMS] [Fact] ::** Các chân 3.3V và 5V trên Arduino là các chân cấp nguồn đầu ra cho linh kiện, không dùng để cấp nguồn đầu vào không ổn định. :: [Arduino_Power]*   **[LMS] [Fact] ::** Chế độ Live trong mBlock5 cho phép điều khiển Arduino trực tiếp từ máy tính và chỉ hoạt động khi có kết nối liên tục. :: [mBlock_Modes]*   **[LMS] [Fact] ::** Chế độ Upload trong mBlock5 nạp chương trình vào bộ nhớ của Arduino; chương trình sẽ không bị mất khi ngắt kết nối với máy tính. :: [mBlock_Modes]*   **[LMS] [Fact] ::** Đèn LED siêu sáng có chân dài là chân dương (+), chân ngắn là chân âm (-). :: [LED_Polarity]*   **[LMS] [Fact] ::** Mạch thu phát âm thanh ISD1820 có các chân kết nối cơ bản: VCC (5V), GND (GND), REC (điều khiển ghi âm), PLAYE/PLAYL (điều khiển phát âm thanh). :: [ISD1820]*   **[LMS] [Fact] ::** Động cơ Servo là một thiết bị đầu ra (output), hoạt động ở điện áp 5V, có 3 dây kết nối (Tín hiệu, VCC, GND). :: [Servo_Motor]*   **[LMS] [Fact] ::** Trên Breadboard, các lỗ ở khu vực giữa được kết nối theo hàng dọc (nhóm 5 lỗ), trong khi các dải nguồn ở mép được kết nối theo hàng ngang. :: [Breadboard]*   **[LMS] [Fact] ::** Khối lệnh "Broadcast" và "When I receive message" cho phép truyền nhận thông tin giữa nhân vật (Sprite) và thiết bị (Arduino) khi ở chế độ Live. :: [mBlock_Messaging]*   **[LMS] [Fact] ::** Extension "Cognitive Services" cung cấp các tính năng AI như nhận diện khuôn mặt, giọng nói và có giới hạn số lượt sử dụng mỗi ngày. :: [AI_Extension]*   **[LMS] [Fact] ::** Teachable Machine là công cụ tạo mô hình máy học (Machine Learning) để phân loại hình ảnh, âm thanh hoặc tư thế và tích hợp vào mBlock qua Extension. :: [Teachable_Machine]
---

## Source: Tự_động_hóa_và_IOT_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất tri thức từ tài liệu "Tự động hóa và IOT AI Arduino Đề 3" theo chuẩn LOM v4.1. Dưới đây là kết quả:

---

### 1. FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact] ::** Chế độ Live trong lập trình Arduino có những hạn chế về khối lệnh so với chế độ Upload, đặc biệt là các khối lệnh khởi đầu hệ thống phức tạp. **:: [mBlock_Modes]*   **[LMS] [Fact] ::** Đèn LED siêu sáng có thể phân biệt cực tính: chân dương thường được đánh dấu bằng một lỗ nhỏ hoặc có chiều dài dài hơn chân âm. **:: [LED_Polarity]*   **[LMS] [Fact] ::** Còi Buzzer là thiết bị đầu ra (output), hoạt động ở điện áp 3V - 5V. Cấu tạo gồm 2 chân: chân dài là cực dương (+), chân ngắn là cực âm (-). **:: [Buzzer]*   **[LMS] [Fact] ::** Mạch thu phát âm thanh ISD1820: Chức năng PLAYE (Edge-activated) phát toàn bộ đoạn âm thanh đã ghi khi có tín hiệu kích hoạt, ngay cả khi tín hiệu ngắt giữa chừng. Chức năng PLAYL (Level-activated) chỉ phát âm thanh khi nút nhấn được giữ. **:: [ISD1820]*   **[LMS] [Fact] ::** Động cơ Servo: Dây màu cam là dây tín hiệu, phải được kết nối với các chân Digital có hỗ trợ PWM (ký hiệu dấu ~) trên Arduino như: 3, 5, 6, 9, 10, 11. **:: [Servo_Motor]*   **[LMS] [Fact] ::** Quy tắc dẫn điện trên Breadboard: Các hàng ở khu vực biên (thường đánh số 1 và 4) dẫn điện theo hàng ngang (dùng làm đường nguồn); các lỗ ở khu vực giữa (2 và 3) dẫn điện theo hàng dọc. **:: [Breadboard]*   **[LMS] [Fact] ::** Khối lệnh "Broadcast" (Phát tin) và "When I receive message" (Khi nhận tin) cho phép truyền thông tin giữa các nhân vật (sprites) và mạch Arduino, hoạt động được ở cả chế độ Live và Upload. **:: [mBlock_Messaging]*   **[LMS] [Fact] ::** Quy trình dạy máy tính (Teachable Machine): Thêm extension -> Training model -> Build new model -> Cung cấp dữ liệu hình ảnh -> Learn -> Use the model. **:: [Teachable_Machine]
---

## Source: Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất tri thức từ tài liệu "Tự động hóa và IOT AI Arduino Đề 4" theo đúng quy tắc LOM v4.1.

Dưới đây là kết quả:

---



*   **[LMS] [Fact] ::** Để kết nối Arduino với máy tính, ta sử dụng cáp USB: đầu cắm vào máy tính là USB-A, đầu cắm vào Arduino là USB-B. **:: [Arduino_Power]*   **[LMS] [Fact] ::** Điện áp đầu ra (output) tiêu chuẩn của các cổng Digital trên mạch Arduino Uno là 5V. **:: [Arduino_Power]*   **[LMS] [Fact] ::** Đèn LED đơn có hai cực: chân dài là cực dương (anode), chân ngắn là cực âm (cathode). **:: [LED_Polarity]*   **[LMS] [Fact] ::** Còi Buzzer là thiết bị đầu ra (output), hoạt động ở điện áp từ 3V đến 5V; chân dài là cực dương, chân ngắn là cực âm. **:: [Buzzer]*   **[LMS] [Fact] ::** Cách nối mạch động cơ rung: Dây đỏ nối với cổng Digital (2-13), dây đen nối với cổng GND. **:: [Vibration_Motor]*   **[LMS] [Fact] ::** Sơ đồ dây động cơ Servo: Dây màu cam là dây tín hiệu (nối chân Digital 2-13), dây màu đỏ là dây nguồn (nối chân 5V), dây màu nâu/đen nối chân GND. **:: [Servo_Motor]*   **[LMS] [Fact] ::** Trong mạch ISD1820: Chân PLAYE (Edge-triggered) sẽ phát hết bộ nhớ khi nhận xung cao; chân PLAYL (Level-triggered) chỉ phát khi điện áp ở mức cao và dừng khi điện áp xuống mức thấp hoặc hết bộ nhớ. **:: [ISD1820]*   **[LMS] [Fact] ::** Thứ tự các bước tạo biến trong mBlock: Chọn nhóm lệnh Variable -> Nhấn Make a Variable -> Đặt tên biến -> Nhấn OK. **:: [mBlock_Variable]*   **[LMS] [Fact] ::** Việc truyền (Broadcast) và nhận tin nhắn (When I receive) giữa thiết bị Arduino và nhân vật chỉ có thể thực hiện khi sử dụng chế độ LIVE. **:: [mBlock_Modes]*   **[LMS] [Fact] ::** Teachable Machine là tiện ích mở rộng nằm trong phần Extension của nhân vật (Sprite), cho phép huấn luyện mô hình máy học để phân loại đối tượng. **:: [Teachable_Machine]
---

### 2. TEST

## Source: Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất tri thức từ tài liệu "Tự động hóa và IOT AI Arduino - Đề trắc nghiệm 1" theo chuẩn LOM v4.1.

Dưới đây là kết quả:

---



*   **[LMS] [Fact] ::** Để kết nối Arduino với máy tính, sử dụng cáp USB với đầu USB-A cắm vào máy tính và đầu USB-B cắm vào cổng nạp của Arduino. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Chế độ Live trong mBlock5 yêu cầu phần mềm luôn mở và duy trì kết nối với board; mọi thay đổi trong code sẽ tác động trực tiếp đến thiết bị ngay lập tức. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Chế độ Upload cho phép chương trình lưu vĩnh viễn trong bộ nhớ Arduino ngay cả khi ngắt kết nối với máy tính. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Cách phân biệt cực tính LED siêu sáng: Chân dương (Anode) dài hơn chân âm (Cathode), hoặc chân dương được đánh dấu bằng một lỗ nhỏ trên thân đèn. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Mạch thu phát âm thanh ISD1820: Chân REC dùng để ghi âm; chân PLAYE phát toàn bộ đoạn âm thanh đã ghi; chân PLAYL chỉ phát âm thanh khi tín hiệu ở mức cao. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Động cơ Servo sử dụng 3 dây: Cam (Tín hiệu - nối chân Digital PWM), Đỏ (Nguồn 5V), Nâu (GND). **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Cấu tạo Breadboard: Các lỗ ở khu vực giữa (B hoặc C) được kết nối theo hàng dọc, mỗi cột gồm 5 lỗ thông nhau. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Khối lệnh "Broadcast" và "When I receive message" dùng để truyền nhận thông tin giữa thiết bị và nhân vật, chủ yếu hoạt động trong chế độ Live. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Extension "Cognitive Services" (AI) yêu cầu kết nối Internet, có giới hạn số lần sử dụng trong ngày và trả về kết quả nhận diện dưới dạng chuỗi ký tự (string). **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Quy trình dạy máy học với Teachable Machine: Thêm Extension -> Training model -> Build new model -> Cung cấp dữ liệu hình ảnh -> Learn -> Use model. **:: [REVIEW_Uncategorized]
---

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.md
Chào bạn, tôi là @scout. Dưới đây là kết quả chưng cất tri thức từ tài liệu đào tạo Arduino Module 1 & 2 theo chuẩn LOM v4.1.

---

### 1. FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact]** :: Arduino Uno R3 có 3 cách cấp nguồn chính: qua cổng USB, qua Jack Adapter (nguồn ngoài), hoặc qua chân Vin (kết nối với pin/nguồn từ 7-12V). :: [Arduino_Power]*   **[LMS] [Fact]** :: Chân Digital 0 (RX) và 1 (TX) trên Arduino được dành riêng cho giao tiếp Serial (truyền và nhận dữ liệu). Việc sử dụng chúng cho các mục đích Digital thông thường có thể gây nhiễu quá trình nạp code hoặc giao tiếp dữ liệu. :: [Arduino_Communication]*   **[LMS] [Fact]** :: Để cấp nguồn cho cảm biến từ Arduino, chân GND nối với cực âm, chân 3.3V hoặc 5V nối với cực dương tùy theo yêu cầu điện áp của cảm biến. :: [Breadboard]*   **[LMS] [Fact]** :: Cách phân biệt cực đèn LED khi bị gãy chân: Quan sát bản cực bên trong đèn, bản cực nhỏ hơn là chân dương (Anode), bản cực to hơn là chân âm (Cathode). :: [LED_Polarity]*   **[LMS] [Fact]** :: Quy tắc dẫn điện trên Breadboard: Các hàng nguồn (thường ký hiệu xanh/đỏ) nối thông theo hàng ngang; các lỗ ở khu vực giữa nối thông theo cột dọc (thường là cụm 5 lỗ). :: [Breadboard]*   **[LMS] [Fact]** :: Cảm biến hồng ngoại (IR) hoạt động dựa trên nguyên tắc phát và thu ánh sáng hồng ngoại để phát hiện vật cản. Điện áp hoạt động tiêu chuẩn từ 3.3V đến 5V. :: [IR_Sensor]*   **[LMS] [Fact]** :: Độ nhạy của cảm biến (như cảm biến mưa, cảm biến hồng ngoại) có thể được điều chỉnh bằng cách xoay biến trở (núm vặn màu xanh) tích hợp trên module cảm biến. :: [Sensor_General]*   **[LMS] [Fact]** :: Động cơ Servo MG90S có khả năng xoay trong phạm vi từ 0 đến 180 độ. Thứ tự dây chuẩn: Nâu (GND), Đỏ (VCC 5V), Cam (Tín hiệu/PWM). :: [Servo_Motor]*   **[LMS] [Fact]** :: Màn hình LCD I2C sử dụng 4 chân kết nối: VCC (nguồn), GND (đất), SDA (dữ liệu - nối chân A4 trên Uno), SCL (xung nhịp - nối chân A5 trên Uno). :: [I2C_LCD]*   **[LMS] [Fact]** :: Cảm biến siêu âm HC-SR04 đo khoảng cách bằng cách phát sóng siêu âm qua chân Trig và nhận lại qua chân Echo. Khoảng cách đo hiệu quả từ 2cm đến khoảng 400cm. :: [Ultrasonic_Sensor]*   **[LMS] [Fact]** :: Mạch điều khiển động cơ L298N có thể điều chỉnh tốc độ và chiều quay của 2 động cơ DC, điện áp cấp cho động cơ có thể lên đến 12V. :: [Motor_Driver_L298]*   **[LMS] [Fact]** :: Joystick cung cấp giá trị Analog (0-1023). Chân VRx đo trục X, VRy đo trục Y. Ở vị trí trung tâm, giá trị thường xấp xỉ 512. :: [Joystick]
---

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất tri thức từ tài liệu "Arduino Module 1" theo đúng quy tắc LOM v4.1. Dưới đây là kết quả:

---

### 1. FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact] ::** Arduino Uno R3 có thể được cấp nguồn thông qua 3 cách chính: Cổng USB, Jack Adapter (nguồn ngoài), hoặc qua chân Vin. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Chân Digital 0 (RX) và 1 (TX) trên Arduino là các chân giao tiếp dữ liệu nối tiếp (Serial Communication). Hạn chế sử dụng chúng cho các mục đích Digital I/O thông thường để tránh nhiễu khi nạp code hoặc truyền dữ liệu. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Để cấp nguồn cho cảm biến từ Arduino, chân GND nối với cực âm, chân 3.3V hoặc 5V nối với cực dương tùy theo điện áp hoạt động của cảm biến. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Cách phân biệt cực đèn LED bằng cấu tạo bên trong: Bản cực nhỏ hơn là chân Dương (Anode), bản cực lớn hơn là chân Âm (Cathode). **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Cấu tạo Breadboard: Khu vực cấp nguồn (thường có vạch xanh/đỏ) các lỗ nối thông theo hàng ngang. Khu vực cắm linh kiện các lỗ nối thông theo cột dọc. Các hàng/cột được cách điện với nhau. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Cảm biến hồng ngoại (IR Sensor) hoạt động trên nguyên tắc phát tia hồng ngoại và thu tín hiệu phản xạ để phát hiện vật cản. Điện áp hoạt động phổ biến từ 3.3V đến 5V. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Độ nhạy của cảm biến (như cảm biến mưa, hồng ngoại) thường được điều chỉnh thông qua biến trở (núm vặn màu xanh) tích hợp trên module. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Câu lệnh `read digital pin` trả về 2 trạng thái logic: Cao (High/1) hoặc Thấp (Low/0). **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Động cơ Servo MG90S là loại động cơ điều khiển được góc quay, phổ biến trong khoảng từ 0 đến 180 độ. **:: [Arduino_M1_Facts]
---

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_(CŨ_chưa_sửa_Extension_KDI)_Đề_trắc_nghiệm_1_-_Arduino_M2.md
Đây là bản chưng cất tri thức từ tài liệu "Đề trắc nghiệm 1 - Arduino M2" theo chuẩn LOM v4.1:

---

### 1. Fact Bank (Kiến thức chuẩn)

*   **[LMS] [Fact] ::** Cấu tạo Breadboard (Test board): Các lỗ ở khu vực nguồn (thường ký hiệu A và D) được nối thông với nhau theo hàng NGANG. Các lỗ ở khu vực linh kiện (B và C) được nối thông với nhau theo hàng DỌC (thường là cụm 5 lỗ). **:: [Arduino_M2_Facts]*   **[LMS] [Fact] ::** Kết nối màn hình I2C LCD với Arduino Uno: Chân GND nối GND, chân VCC nối 5V, chân SDA nối chân Analog A4, chân SCL nối chân Analog A5. **:: [Arduino_M2_Facts]*   **[LMS] [Fact] ::** Cảm biến siêu âm HC-SR04: Gồm 2 đầu (phát sóng siêu âm - Trig và thu sóng phản xạ - Echo). Chân VCC nối 5V, chân GND nối GND, chân Trig và Echo nối với các chân Digital. Tầm đo hiệu quả từ 2cm đến khoảng 400cm. **:: [Arduino_M2_Facts]*   **[LMS] [Fact] ::** Mắt thu hồng ngoại VS1838: Thứ tự chân tính từ trái sang phải (khi nhìn vào mặt thu) là: OUT - GND - VCC. **:: [Arduino_M2_Facts]*   **[LMS] [Fact] ::** Mạch điều khiển động cơ L298: Cần 2 chân Digital cho mỗi động cơ để điều khiển chiều quay. Nguồn cấp cho động cơ thường dùng pin rời (như đế 4 pin) nối vào chân 12V và GND của mạch L298. **:: [Arduino_M2_Facts]*   **[LMS] [Fact] ::** Cảm biến DHT11: Dùng để đo đồng thời nhiệt độ và độ ẩm môi trường, trả về dữ liệu số qua 1 chân Digital. **:: [Arduino_M2_Facts]
---

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.md
Đây là bản chưng cất tri thức từ tài liệu "Tự động hóa và IOT Arduino 1+2 - Arduino 2 - Đề 1":

---

### 1. Fact Bank (Kiến thức chuẩn)

*   **[LMS] [Fact]** :: Để cấp nguồn hiệu quả cho hệ thống gồm Arduino và mạch công suất L298, nên sử dụng nguồn pin mắc song song. Dây dương (đỏ) kết nối đồng thời vào chân 12V+ của L298 và chân VIN của Arduino; dây âm (đen) kết nối chung vào chân GND của cả hai thiết bị. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Màn hình LCD 16x2 sử dụng module chuyển đổi I2C yêu cầu kết nối chân SDA vào chân Analog A4 và chân SCL vào chân Analog A5 trên Arduino Uno. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Các chân điều khiển IN1, IN2, IN3, IN4 trên mạch cầu H L298 cần được kết nối với các chân Digital có hỗ trợ PWM (ký hiệu dấu "~" trên board mạch) của Arduino để có thể điều chỉnh tốc độ và hướng quay của động cơ. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Khi lập trình mắt thu hồng ngoại (IR Receiver), sau mỗi lần nhận dữ liệu từ remote, cần sử dụng câu lệnh "IR Receive: Restart" để reset tín hiệu, giúp hệ thống sẵn sàng nhận lệnh tiếp theo. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Cảm biến DHT11 đo nhiệt độ và độ ẩm trả về dữ liệu qua một chân Digital (OUT/DATA). Trong lập trình, cần khai báo đúng chân Digital này để đọc giá trị. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Quy trình điều khiển xe bằng Remote hồng ngoại phổ biến: Phím 2 (Tiến), Phím 8 (Lùi), Phím 4 (Xoay trái), Phím 6 (Xoay phải), Phím 5 (Dừng). :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Để bảo vệ mạch điện và linh kiện khi hoạt động trong môi trường có phun sương (độ ẩm cao), mô hình cần thiết kế mái che hoặc hộp bảo vệ chuyên dụng. :: [Arduino_M2_Facts]
---

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_2_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.md
Chào bạn, tôi là @scout. Dưới đây là kết quả chưng cất tri thức từ tài liệu đào tạo Arduino Module 2 (Đề 2) theo chuẩn LOM v4.1.

---

### 1. FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact]** :: Khi cấp nguồn cho Arduino từ bộ pin ngoài, dây dương (đỏ) phải được kết nối vào chân **VIN** và dây âm (đen) kết nối vào chân **GND**. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Đối với đèn LED đơn, chân âm (chân ngắn) kết nối với chân **GND**, chân dương (chân dài) kết nối với các chân **Digital (D)** của Arduino. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Cảm biến ánh sáng (LDR) kết nối chân **VCC vào 5V**, chân **GND vào GND** và chân tín hiệu **AO (hoặc DO)** vào chân **Analog (hoặc Digital)** tương ứng trên Arduino. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Cảm biến siêu âm sử dụng chân **Trig** và **Echo** kết nối vào các chân **Digital** để đo khoảng cách bằng sóng siêu âm. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Để điều khiển tốc độ và hướng động cơ qua mạch L298, các chân **IN 1, 2, 3, 4** nên được kết nối với các chân **Digital PWM** (các chân có ký hiệu dấu **~**) trên Arduino. :: [Arduino_M2_Facts]*   **[LMS] [Fact]** :: Trong lập trình điều khiển xe, việc sử dụng câu lệnh **"Chờ" (Wait)** sau các hành động như đi lùi hoặc xoay hướng là cần thiết để đảm bảo robot ổn định trạng thái cơ khí trước khi thực hiện lệnh tiếp theo. :: [Arduino_M2_Facts]
---

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_trắc_nghiệm_1_-_Arduino_M2.md
### 1. Fact Bank (Kiến thức chuẩn)

*   [LMS] [Fact] :: Trên breadboard (loại 400 lỗ hoặc 800 lỗ), các lỗ ở khu vực cấp nguồn (thường ký hiệu A và D) được nối thông với nhau theo hàng ngang (dọc theo chiều dài board), trong khi các lỗ ở khu vực linh kiện (B và C) được nối thông theo hàng dọc (thường là cụm 5 lỗ). :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Để điều khiển đèn LED nhấp nháy với chu kỳ 2 giây, chương trình cần thiết lập thời gian sáng 1 giây (1000ms) và thời gian tắt 1 giây (1000ms). :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Màn hình LCD sử dụng giao tiếp I2C kết nối với Arduino Uno qua hai chân tín hiệu cố định: SDA nối với chân A4 và SCL nối với chân A5. :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Cảm biến siêu âm HC-SR04 gồm hai bộ phận chính: một đầu phát sóng siêu âm (Trig) và một đầu thu sóng phản xạ (Echo). :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Cảm biến siêu âm HC-SR04 có chân VCC nối với nguồn 5V, chân GND nối với cực âm (GND) của Arduino, chân Trig và Echo nối với các chân Digital. :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Thứ tự chân của mắt thu hồng ngoại VS1838 khi nhìn từ mặt trước (từ trái sang phải) là: Chân tín hiệu (Out) - Chân âm (GND) - Chân dương (VCC). :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Khi sử dụng mạch cầu H L298 để điều khiển động cơ, cần phải nối chung chân GND của nguồn điện ngoài (pin) với chân GND của Arduino để thống nhất mức điện chiếu. :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Để cấp nguồn hiệu quả cho hệ thống xe Arduino, nguồn pin nên được cấp trực tiếp vào mạch L298 (chân 12V) và cấp vào chân VIN của Arduino. :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Cảm biến DHT11 được sử dụng để đo đồng thời nhiệt độ và độ ẩm của môi trường xung quanh. :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Trong lập trình điều khiển xe, việc đảo ngược trạng thái HIGH/LOW của các chân In1, In2 (hoặc In3, In4) trên mạch L298 sẽ làm động cơ xoay theo chiều ngược lại. :: [Arduino_M2_Facts]
---

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2.md
Dưới đây là kết quả chưng cất tri thức từ tài liệu đào tạo Arduino Module 2 theo quy tắc LOM v4.1:

### 1. Fact Bank (Kiến thức chuẩn)

*   [LMS] [Fact] :: Màn hình LCD I2C sử dụng giao thức truyền thông 2 dây, tổng cộng có 4 chân kết nối: VCC (Nguồn), GND (Đất), SCL (Xung đồng hồ) và SDA (Dữ liệu). :: [Arduino_M2_Facts]*   [LMS] [Fact] :: Module Joystick tiêu chuẩn có 5 chân kết nối, bao gồm các chân cấp nguồn và các chân tín hiệu cho trục X, trục

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Đề_2_Trắc_nghiệm_-_Arduino_M1,2.md
Chào bạn, tôi là @scout. Dưới đây là kết quả chưng cất tri thức từ tài liệu **Tự động hóa và IOT Arduino 1+2 - Đề 2**:

---



*   **[LMS] [Fact] ::** Cổng USB trên mạch Arduino (thường là loại B) là bộ phận dùng để kết nối với máy tính nhằm nạp chương trình và cấp nguồn. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Cách xác định cực tính đèn LED: Chân dài là cực dương (+), chân ngắn là cực âm (-). Về cấu tạo bên trong, bản cực nhỏ hơn là cực dương, bản cực lớn hơn là cực âm. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Còi Buzzer có cực tính: Chân dài nối với cực dương (hoặc chân tín hiệu), chân ngắn nối với cực âm (GND). **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Động cơ Servo MG90S là loại động cơ có thể điều khiển góc quay chính xác trong khoảng từ 0 đến 180 độ. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Cấu tạo Breadboard: Các lỗ ở dải nguồn (khu vực biên) thường được nối thông theo hàng ngang; các lỗ ở khu vực giữa (cắm linh kiện) được nối thông theo cột dọc. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Cảm biến hồng ngoại (IR Sensor) hoạt động dựa trên nguyên lý phát tia hồng ngoại và thu lại tia phản xạ từ vật cản để xác định sự hiện diện của vật thể. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Cảm biến mưa và nhiều module cảm biến Arduino thông dụng hoạt động ổn định ở mức điện áp 5V. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Chân VRx của Joystick dùng để đo mức độ di chuyển theo trục X. Giá trị trả về dạng Analog từ 0 đến 1023 (vị trí cân bằng khoảng 512). **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Cảm biến siêu âm HC-SR04 sử dụng chân Trig để phát sóng và chân Echo để nhận sóng phản hồi. Khoảng cách đo tối ưu trong khoảng từ 2cm đến 400cm. **:: [Arduino_M1_Facts]*   **[LMS] [Fact] ::** Chân 0 (RX) và 1 (TX) trên Arduino được dành riêng cho giao tiếp nối tiếp (Serial). Hạn chế dùng các chân này cho mục đích Digital I/O thông thường để tránh nhiễu tín hiệu khi nạp code hoặc truyền dữ liệu. **:: [Arduino_M1_Facts]
---

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Đề_3_Trắc_nghiệm_-_Arduino_M1,2.md
Chào bạn, tôi là @scout. Dưới đây là kết quả chưng cất tri thức từ tài liệu đào tạo Arduino M1+2 (Đề 3) theo chuẩn LOM v4.1.

---



*   **[LMS] [Fact]** :: Arduino Uno R3 có 3 cách cấp nguồn chính: Cổng USB (5V), Jack nguồn DC (Adapter 7-12V), và chân Vin (7-12V). :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Đèn LED là thiết bị đầu ra (Output). Cực dương (Anode) là chân dài hoặc phần bản kim loại nhỏ bên trong; cực âm (Cathode) là chân ngắn hoặc phần bản kim loại lớn bên trong. :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Còi Buzzer có cực tính: Chân dài là cực dương (+), chân ngắn là cực âm (-). Khi lập trình, chân dương nối với chân Digital (D2-D13), chân âm nối GND. :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Động cơ Servo có 3 dây màu quy ước: Màu cam (Tín hiệu - PWM/Digital), Màu đỏ (Dương nguồn - 5V), Màu nâu (Âm nguồn - GND). :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Cấu tạo Breadboard: Các lỗ ở hàng ngang ngoài cùng (thường ký hiệu +/-) dẫn điện với nhau theo hàng ngang. Các lỗ ở khu vực giữa dẫn điện với nhau theo cột dọc (thường là 5 lỗ). :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Để điều chỉnh độ nhạy của các cảm biến (Hồng ngoại, Ánh sáng, Mưa...), ta sử dụng tua vít để xoay biến trở tối ưu (thường là linh kiện màu xanh dương có núm vặn) trên module cảm biến. :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Màn hình LCD sử dụng giao tiếp I2C chỉ cần 4 chân kết nối: VCC (Nguồn), GND (Đất), SCL (Xung đồng hồ), SDA (Dữ liệu). :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Joystick cung cấp giá trị Analog từ 0 đến 1023. Ở vị trí cân bằng, giá trị xấp xỉ 512. Khi gạt hết cỡ về một phía, giá trị sẽ tiến về 0 hoặc 1023. :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Cảm biến siêu âm HC-SR04 có 4 chân: VCC (5V), Trig (Phát tín hiệu), Echo (Nhận tín hiệu phản hồi), GND (Đất). :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Module Joystick chuẩn có 5 chân kết nối: GND, +5V, VRx (Trục X), VRy (Trục Y), SW (Nút nhấn). :: [REVIEW_Uncategorized]*   **[LMS] [Fact]** :: Khi sử dụng mạch cầu H L298N điều khiển động cơ công suất lớn, cần cấp nguồn ngoài riêng cho mạch L298N và phải nối chung chân GND với Arduino để thống nhất mức điện áp tham chiếu. :: [REVIEW_Uncategorized]
---

## Source: Tự_động_hóa_và_IOT_Arduino_1+2_Đề_4_Trắc_nghiệm_-_Arduino_M1,2.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất tri thức từ tài liệu "Tự động hóa và IOT Arduino 1+2 Đề 4" theo đúng quy tắc LOM v4.1.

Dưới đây là kết quả:

---



*   **[LMS] [Fact] ::** Cấu tạo bên trong đèn LED: Bản cực nhỏ hơn là chân Dương (Anode), bản cực lớn hơn là chân Âm (Cathode). :: [LED_Polarity]*   **[LMS] [Fact] ::** Cực tính còi Buzzer: Chân dài là cực dương, chân ngắn là cực âm (nối với GND). :: [Buzzer]*   **[LMS] [Fact] ::** Thứ tự dây Servo tiêu chuẩn: Dây nâu (GND), dây đỏ (5V), dây cam (Tín hiệu - Digital PWM). :: [Servo_Motor]*   **[LMS] [Fact] ::** Quy tắc kết nối Breadboard: Khu vực đường ray nguồn (ngoài cùng) kết nối theo hàng ngang; khu vực cắm linh kiện (giữa) kết nối theo hàng dọc. :: [Breadboard]*   **[LMS] [Fact] ::** Cảm biến hồng ngoại (IR Proximity) thường được ứng dụng trong: Robot tránh vật cản, đèn thông minh tự sáng, cửa tự động. :: [IR_Sensor]*   **[LMS] [Fact] ::** Điện áp hoạt động: Nếu cấp nguồn 3.3V cho linh kiện yêu cầu 5V (như cảm biến mưa), linh kiện sẽ hoạt động không chính xác hoặc không ổn định. :: [Arduino_Power]*   **[LMS] [Fact] ::** Joystick Arduino: Thường có 5 chân kết nối (VCC, GND, VRx, VRy, SW). :: [Joystick]*   **[LMS] [Fact] ::** Giá trị Joystick: Ở vị trí cân bằng, giá trị analog khoảng 512. Khi gạt sang trái (trục X), giá trị giảm dần từ 512 về 0. :: [Joystick]*   **[LMS] [Fact] ::** Mạch cầu H L298: Có khả năng cung cấp điện áp đầu ra tối đa cho động cơ lên đến 12V (tùy nguồn cấp). :: [Motor_Driver_L298]*   **[LMS] [Fact] ::** Cấp nguồn Arduino: Có thể cấp qua cổng USB Type B, Jack DC (7-12V) hoặc chân VIN. Chân 3.3V và 5V trên board chủ yếu là chân đầu ra (Output), không dùng để cấp nguồn vào (trừ trường hợp nguồn ổn định đặc biệt). :: [Arduino_Power]
---

## Source: Tự_động_hóa_và_IOT_Halocode_Đề_2_trắc_nghiệm_-_Halocode.md
Đây là bản chưng cất tri thức từ tài liệu "Tự động hóa và IOT Halocode Đề 2" theo chuẩn LOM v4.1:

### 1. Fact Bank (Kiến thức chuẩn)

*   **[LMS] [Fact] ::** Halocode kết nối với máy tính thông qua cổng Micro-USB (không phải USB Type C). **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Ở chế độ LIVE, Halocode phải duy trì kết nối liên tục với máy tính để thực thi lệnh từ phần mềm mBlock 5. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Ở chế độ UPLOAD, chương trình được nạp trực tiếp vào bộ nhớ của Halocode, cho phép thiết bị hoạt động độc lập với máy tính. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Điện áp hoạt động tiêu chuẩn của Halocode nằm trong khoảng từ 3V đến 5V. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Halocode tích hợp sẵn các module: Cảm biến ánh sáng, Microphone (cảm biến âm thanh), Cảm biến chạm (4 vị trí 0, 1, 2, 3), Cảm biến chuyển động 6 trục (Gia tốc + Con quay hồi chuyển) và Module Wifi/Bluetooth. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Vòng đèn LED trên Halocode gồm 12 bóng LED RGB, được đánh số thứ tự từ 1 đến 12 tăng dần theo chiều kim đồng hồ. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Màu sắc của mỗi đèn LED RGB có thể được tùy chỉnh bằng cách thay đổi thông số R (Red), G (Green), B (Blue) với giá trị từ 0 đến 255. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Trong lập trình cảm biến gia tốc, thao tác "nghiêng Halocode trái/phải" tương ứng với việc xoay thiết bị quanh trục Y. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Khối lệnh "broadcast - receive message" (phát tin nhắn) ở chế độ LIVE cho phép truyền dữ liệu/tín hiệu hai chiều giữa thiết bị Halocode và các nhân vật (Sprite) trên sân khấu mBlock. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Khối lệnh "When Halocode starts up" (Khi Halocode khởi động) là khối lệnh sự kiện dành riêng cho chế độ UPLOAD. **:: [REVIEW_Uncategorized]*   **[LMS] [Fact] ::** Để kết nối động cơ Servo với Halocode, dây tín hiệu (thường màu cam) phải được nối vào các chân Pin (0, 1, 2, 3), dây nguồn (đỏ) vào 3.3V và dây đất (nâu/đen) vào GND. **:: [REVIEW_Uncategorized]
---

## Source: Tự_động_hóa_và_IOT_Halocode_Đề_3_trắc_nghiệm_-_Halocode.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất tri thức từ tài liệu "Tự động hóa và IOT Halocode Đề 3" theo đúng quy tắc LOM v4.1.

---



*   **[LMS] [Fact] ::** Halocode tích hợp 12 đèn LED RGB có thể lập trình độc lập, các đèn này được đánh số thứ tự từ 0 đến 11. :: [Halocode_Hardware]*   **[LMS] [Fact] ::** Cảm biến chuyển động (gia tốc) trên Halocode cho phép thiết bị nhận biết các tác động vật lý như rung, lắc hoặc độ nghiêng. :: [Halocode_Sensor]*   **[LMS] [Fact] ::** Halocode có 4 cổng cảm biến chạm (touch pins) được đánh số là 0, 1, 2 và 3. :: [Halocode_Hardware]*   **[LMS] [Fact] ::** Quy tắc kết nối Servo với Halocode: Dây nâu nối chân GND (đất), dây đỏ nối chân nguồn 3.3V, và dây cam (tín hiệu) nối vào một trong các chân cảm biến chạm (0, 1, 2, 3). :: [Halocode_Hardware]*   **[LMS] [Fact] ::** Cảm biến hồng ngoại gồm 2 đèn: 1 đèn phát tín hiệu (thường màu trắng/trong suốt) và 1 đèn thu tín hiệu (thường màu đen). :: [Halocode_Sensor]*   **[LMS] [Fact] ::** Ở chế độ LIVE, khối lệnh "Broadcast - Receive message" cho phép truyền thông tin tương tác qua lại giữa thiết bị Halocode và các nhân vật (sprites) trên sân khấu mBlock. :: [Halocode_Programming]*   **[LMS] [Fact] ::** Sơ đồ truyền tin qua Cloud IoT: Sprites <-> mBlock 5 Cloud servers <-> User cloud message <-> Halocode. :: [IoT_Definition]*   **[LMS] [Fact] ::** IoT (Internet of Things) là mạng lưới các thiết bị được kết nối internet để điều khiển từ xa hoặc thu thập dữ liệu (ví dụ: cửa điều khiển qua app, đồng hồ đo chất lượng không khí). :: [IoT_Definition]
---

## Source: Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất tri thức từ tài liệu "Tự động hóa và IOT Halocode Đề 4" theo tiêu chuẩn LOM v4.1. Dưới đây là kết quả:

---



*   **[LMS] [Fact] ::** Halocode được tích hợp sẵn các tính năng: Giao tiếp không dây WiFi, Bluetooth, Microphone thu nhận giọng nói, cảm biến chuyển động (gia tốc kế/con quay hồi chuyển) và các cảm biến chạm. :: [Halocode_Hardware]*   **[LMS] [Fact] ::** Trình tự kết nối Halocode ở chế độ Upload: (1) Mở mBlock & kết nối USB -> (2) Chọn thiết bị Halocode -> (3) Chọn Connect & cổng kết nối -> (4) Chuyển sang chế độ Upload -> (5) Lập trình -> (6) Nhấn Upload. :: [mBlock_Modes]*   **[LMS] [Fact] ::** Vòng đèn LED trên Halocode gồm 12 đèn LED RGB được đánh số thứ tự từ 1 đến 12 theo chiều kim đồng hồ. :: [LED_Matrix]*   **[LMS] [Fact] ::** Chế độ LIVE dùng để điều khiển thiết bị trực tiếp từ máy tính, cho phép tương tác thời gian thực giữa thiết bị và nhân vật (sprite). Chế độ UPLOAD dùng để tải chương trình vào bộ nhớ thiết bị để chạy độc lập không cần máy tính. :: [mBlock_Modes]*   **[LMS] [Fact] ::** Để sử dụng các tính năng liên quan đến WiFi, Cloud Message và nhận diện giọng nói trên mBlock 5, người dùng bắt buộc phải đăng nhập tài khoản. :: [mBlock_Cloud]*   **[LMS] [Fact] ::** Nhóm lệnh "Upload mode broadcast" cho phép truyền dữ liệu không dây giữa Halocode và các thiết bị/nhân vật khác mà không cần duy trì dây cáp kết nối sau khi đã nạp code. :: [Arduino_Communication]*   **[LMS] [Fact] ::** Cảm biến hồng ngoại (IR) cấu tạo gồm: Đèn LED phát tín hiệu (trong suốt), đèn LED thu tín hiệu (màu đen), biến trở điều chỉnh khoảng cách, đèn báo nguồn và đèn báo tín hiệu vật cản. :: [IR_Sensor]*   **[LMS] [Fact] ::** IoT (Internet of Things) là mạng lưới các thiết bị được kết nối internet để thu thập và trao đổi dữ liệu, ví dụ: Hệ thống quan trắc chất lượng không khí, nhà thông minh. :: [IoT_Definition]
---

## Source: Tự_động_hóa_và_IOT_Halocode_Đề_trắc_nghiệm_1_-_Halocode.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất dữ liệu từ tài liệu "Tự động hóa và IOT Halocode - Đề trắc nghiệm 1" sang hai định dạng Fact Bank và Test Bank theo tiêu chuẩn LOM v4.1.

---

### I. FACT BANK (KIẾN THỨC CHUẨN)

[LMS] [Fact] :: Trình tự kết nối Halocode ở chế độ Upload: 1. Kết nối USB -> 2. Chọn thiết bị Halocode -> 3. Kết nối cổng (Connect) -> 4. Chuyển sang chế độ Upload -> 5. Lập trình -> 6. Nhấn Upload. :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Halocode được trang bị 12 đèn LED RGB có khả năng lập trình riêng biệt, được đánh số thứ tự từ 0 đến 11. :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Cảm biến chuyển động (Motion sensor) trên Halocode cho phép nhận biết các tác động vật lý như rung lắc hoặc nghiêng thiết bị. :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Halocode có 4 vị trí cảm biến chạm (Touch sensors) được phân bố trên bo mạch, thường được đánh số để lập trình tương tác. :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Halocode tích hợp chip điều khiển có khả năng thu phát tín hiệu không dây qua giao thức Bluetooth và Wifi. :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Động cơ Servo MG90S có góc quay giới hạn từ 0 đến 180 độ. :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Quy định màu dây của động cơ Servo: Dây màu Cam (Signal - tín hiệu điều khiển), dây màu Đỏ (VCC - nguồn dương 3.3V), dây màu Nâu (GND - cực âm). :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Trong lập trình Halocode, thao tác nghiêng thiết bị sang Trái hoặc Phải tương ứng với sự thay đổi giá trị trên trục Y. :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Chế độ LIVE trong mBlock 5 cho phép điều khiển thiết bị và nhân vật (Sprite) tương tác thời gian thực, nhưng không hỗ trợ khối lệnh "When Halocode starts up" (chỉ dùng cho Upload mode). :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Để truyền tin nhắn giữa Halocode và Sprite trong mBlock, ta sử dụng khối lệnh Broadcast (Phát tin) và When I receive (Khi nhận tin). :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Cảm biến hồng ngoại (IR) gồm 2 bộ phận: Đèn trắng (phát tín hiệu) và Đèn đen (thu tín hiệu). :: [REVIEW_Uncategorized]
[LMS] [Fact] :: Sơ đồ kết nối Cloud mBlock: Halocode -> User cloud message -> mBlock 5 Cloud servers -> Sprites. :: [REVIEW_Uncategorized]
---

## Source: Tự_động_hóa_và_IOT_YoloBit_Đề_2._TRẮC_NGHIỆM_YOLOBIT_.md
Đây là kết quả chưng cất tri thức từ tài liệu LMS: **Tự động hóa và IOT YoloBit - Đề 2**.

---

### 1. FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact] ::** Ma trận LED của Yolo:Bit bao gồm 25 đèn LED RGB được sắp xếp theo cấu trúc 5 hàng và 5 cột. **:: [YoloBit_Hardware]*   **[LMS] [Fact] ::** Yolo:Bit không hỗ trợ hiển thị tiếng Việt có dấu trên ma trận LED. **:: [YoloBit_Display]*   **[LMS] [Fact] ::** Khối lệnh "Hiện chữ" có khả năng hiển thị cả ký tự chữ và số, trong khi khối lệnh "Hiện số" chỉ chuyên dụng cho dữ liệu số. **:: [YoloBit_Programming]*   **[LMS] [Fact] ::** Nhóm lệnh "Nâng cao" trong giao diện lập trình Yolo:Bit mặc định có 8 nhóm lệnh con. **:: [YoloBit_Programming]*   **[LMS] [Fact] ::** Các phương thức chia sẻ dự án Yolo:Bit bao gồm: Xuất file dự án (.py hoặc .xml), chia sẻ đường dẫn (link) trực tuyến, hoặc sử dụng mã QR. **:: [YoloBit_Software]*   **[LMS] [Fact] ::** Chân cắm tiêu chuẩn Grove cho các module mở rộng (như LED) thường bao gồm 3 chân: GND (Đất), VCC (Nguồn), và SIG (Tín hiệu). **:: [Breadboard]*   **[LMS] [Fact] ::** Cảm biến ánh sáng hoạt động dựa trên nguyên lý của hiệu ứng quang điện; điện trở của cảm biến sẽ thay đổi nghịch biến với cường độ ánh sáng (ánh sáng càng mạnh, điện trở càng giảm). **:: [Sensor_General]*   **[LMS] [Fact] ::** Động cơ Servo tiêu chuẩn có 3 dây màu quy ước: Đỏ (Nguồn VCC), Nâu/Xám/Đen (Cực âm GND), và Vàng/Cam (Tín hiệu điều khiển). **:: [Servo_Motor]*   **[LMS] [Fact] ::** Độ chính xác của cảm biến siêu âm chịu ảnh hưởng bởi chất liệu vật thể, bề mặt phản xạ, góc phát sóng và nhiệt độ môi trường. **:: [Sensor_General]*   **[LMS] [Fact] ::** Việc cập nhật Firmware cho Yolo:Bit được thực hiện thông qua mục Quản lý dự án (biểu tượng bánh răng hoặc danh sách dự án). **:: [YoloBit_Software]*   **[LMS] [Fact] ::** Cảm biến chuyển động PIR (Passive Infrared) chỉ kích hoạt tín hiệu khi phát hiện sự thay đổi bức xạ hồng ngoại từ vật thể chuyển động; nếu vật thể đứng yên, cảm biến sẽ không phát hiện. **:: [Sensor_General]
---

## Source: Tự_động_hóa_và_IOT_YoloBit_Đề_3._TRẮC_NGHIỆM_YOLOBIT_.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất tri thức từ tài liệu "Tự động hóa và IOT YoloBit Đề 3" theo đúng quy tắc LOM v4.1.

---



*   **[LMS] [Fact]** :: Ngoài 5 chân cắm lỗ to (P0, P1, P2, 3V, GND), mạch Yolo:Bit còn có 20 chân cắm mở rộng khác để kết nối ngoại vi. :: [YoloBit_Hardware]*   **[LMS] [Fact]** :: Trong lập trình Yolo:Bit, khối lệnh đặt trong phần "Bắt đầu" chỉ thực thi một lần duy nhất khi khởi động; khối lệnh trong "Lặp lại mãi" sẽ thực hiện lặp đi lặp lại liên tục cho đến khi tắt nguồn hoặc reset. :: [YoloBit_Programming]*   **[LMS] [Fact]** :: Động cơ Servo là động cơ điện có độ chính xác cao, trục quay di chuyển đến góc chỉ định qua lập trình. Đặc điểm: tốc độ thấp, lực (mô-men xoắn) mạnh, sử dụng hộp số giảm tốc có tỉ số truyền lớn, góc xoay phổ biến từ 0 đến 180 độ. :: [Servo_Motor]*   **[LMS] [Fact]** :: Cảm biến nhiệt độ và độ ẩm DHT20 sử dụng giao tiếp I2C, có thể kết nối vào cả hai cổng I2C1 và I2C2 trên mạch mở rộng. :: [YoloBit_Sensor]*   **[LMS] [Fact]** :: Yolo:Bit tích hợp sẵn hai phương thức kết nối không dây là WiFi và Bluetooth. :: [Arduino_Communication]*   **[LMS] [Fact]** :: Trình duyệt web tự động lưu dự án lập trình Yolo:Bit; khi mở lại app, quá trình làm việc trước đó sẽ được giữ nguyên. :: [YoloBit_Software]*   **[LMS] [Fact]** :: Cảm biến ánh sáng trên Yolo:Bit có thể đọc giá trị từ các chân analog như P0, P1, P2. :: [YoloBit_Sensor]*   **[LMS] [Fact]** :: Cảm biến siêu âm (cảm biến khoảng cách) có phạm vi đo hiệu quả từ 3cm đến 200cm. :: [YoloBit_Sensor]*   **[LMS] [Fact]** :: Giá trị điều xung (PWM/Analog Write) trên Yolo:Bit có độ phân giải 12-bit, tương ứng với dải giá trị từ 0 (0%) đến 4095 (100%). :: [YoloBit_Sensor]
---

## Source: Tự_động_hóa_và_IOT_YoloBit_Đề_4._TRẮC_NGHIỆM_YOLOBIT_.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất dữ liệu từ tài liệu "Tự động hóa và IOT YoloBit Đề 4" theo đúng quy tắc LOM v4.1.

Dưới đây là kết quả:

---

### 1. FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact] ::** Ma trận LED của Yolo:Bit bao gồm 5 hàng, 5 cột với tổng cộng 25 đèn LED RGB có khả năng hiển thị nhiều màu sắc, hình ảnh, chữ và số. **:: [YoloBit_Hardware]*   **[LMS] [Fact] ::** Để chia sẻ dự án trên môi trường lập trình Yolo:Bit, người dùng có thể: Xuất dự án thành file (.xml), chia sẻ đường link liên kết hoặc sử dụng mã QR. **:: [YoloBit_Software]*   **[LMS] [Fact] ::** Động cơ Servo có 3 dây tín hiệu đặc trưng: dây đỏ (nguồn VCC), dây nâu/xám/đen (đất GND) và dây vàng/cam (tín hiệu Signal). **:: [Servo_Motor]*   **[LMS] [Fact] ::** Động cơ Servo được kết nối với mạch mở rộng Yolo:Bit thông qua các dãy cổng GVS (Ground - Voltage - Signal). **:: [Breadboard]*   **[LMS] [Fact] ::** Module LED tiêu chuẩn sử dụng chuẩn cắm Grove gồm 3 chân: GND (Đất), VCC (Nguồn) và SIG (Tín hiệu). **:: [LED_Polarity]*   **[LMS] [Fact] ::** Cảm biến siêu âm (Ultrasonic Sensor) dùng để đo khoảng cách vật cản trong phạm vi hoạt động hiệu quả từ 3cm đến 200cm. **:: [Sensor_General]*   **[LMS] [Fact] ::** Cảm biến PIR (Passive Infrared) hoạt động dựa trên việc phát hiện bức xạ hồng ngoại từ các vật thể chuyển động (như người hoặc động vật). **:: [PIR_Sensor]*   **[LMS] [Fact] ::** Cảm biến ánh sáng trên Yolo:Bit là một quang trở; khi cường độ ánh sáng chiếu vào tăng lên, trở kháng của cảm biến sẽ giảm xuống. **:: [Sensor_General]*   **[LMS] [Fact] ::** Cảm biến PIR chỉ kích hoạt trạng thái "có người" khi phát hiện sự chuyển động; nếu đối tượng đứng yên hoàn toàn, cảm biến sẽ trả về trạng thái không có người. **:: [PIR_Sensor]*   **[LMS] [Fact] ::** Việc cập nhật Firmware cho mạch Yolo:Bit được thực hiện thông qua menu Quản lý dự án (biểu tượng bánh răng hoặc danh sách dự án). **:: [YoloBit_Software]
---

## Source: Tự_động_hóa_và_IOT_YoloBit_Đề_trắc_nghiệm_1_-_Yolo_Bit.md
Chào bạn, tôi là @scout. Tôi đã thực hiện chưng cất tri thức từ tài liệu "Tự động hóa và IOT YoloBit - Đề trắc nghiệm 1" theo đúng quy tắc LOM v4.1.

Dưới đây là kết quả:

### 1. Fact Bank (Kiến thức chuẩn)

- [LMS] [Fact] :: Yolo:Bit tích hợp các bộ phận phần cứng bao gồm: Màn hình LED ma trận, cảm biến nhiệt độ, cảm biến ánh sáng, nút nhấn (A và B), cảm biến gia tốc, loa, nút reset và cổng kết nối USB. :: [YoloBit_Hardware]- [LMS] [Fact] :: Yolo:Bit hỗ trợ kết nối với máy tính thông qua hai phương thức chính là dây cáp USB hoặc kết nối không dây Bluetooth. :: [Arduino_Power]- [LMS] [Fact] :: Ma trận LED trên Yolo:Bit bao gồm 25 đèn LED RGB được sắp xếp theo cấu trúc 5 hàng và 5 cột. :: [LED_Matrix]- [LMS] [Fact] :: Các phương thức lưu trữ dự án lập trình Yolo:Bit bao gồm: Lưu trên bộ nhớ trình duyệt, xuất file offline định dạng .json hoặc .ohs, và chia sẻ qua đường dẫn (link) hoặc mã QR. :: [YoloBit_Software]- [LMS] [Fact] :: Module đèn LED RGB và các cảm biến cơ bản thường sử dụng dây kết nối chuẩn Grove để kết nối với mạch mở rộng. :: [Breadboard]- [LMS] [Fact] :: Động cơ Servo có quy định màu dây chuẩn: chân nguồn (màu đỏ), chân đất (màu nâu/đen) và chân tín hiệu (màu vàng/cam). :: [Servo_Motor]- [LMS] [Fact] :: Module màn hình LCD và cảm biến DHT20 thường sử dụng giao tiếp I2C để kết nối với mạch mở rộng Yolo:Bit. :: [I2C_LCD]- [LMS] [Fact] :: Cảm biến hồng ngoại PIR (Passive Infrared) có chức năng phát hiện chuyển động của các vật thể phát ra bức xạ hồng ngoại. :: [PIR_Sensor]- [LMS] [Fact] :: Cảm biến siêu âm được sử dụng để phát hiện vật cản và đo khoảng cách đến vật thể phía trước. :: [Ultrasonic_Sensor]- [LMS] [Fact] :: Cảm biến DHT20 là thiết bị chuyên dụng để đo đồng thời nhiệt độ và độ ẩm của môi trường không khí. :: [DHT20_Sensor]
---