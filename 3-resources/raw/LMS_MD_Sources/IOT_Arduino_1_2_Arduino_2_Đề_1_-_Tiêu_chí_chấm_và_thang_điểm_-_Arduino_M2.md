---
title: Đề 1 - Tiêu chí chấm và thang điểm - Arduino M2.docx
source: [[Đề 1 - Tiêu chí chấm và thang điểm - Arduino M2.docx]]
type: RAW_SOURCE
---

ĐỀ KIỂM TRA THỰC HÀNH - Lập trình Arduino Module 2
(Đề

1) Đề kiểm tra thực hành

Arduino (module

2) Yêu cầu:

1. - Thời gian làm bài: 120 phút

- Đề thực hành gồm: 1 bài tập lập trình và 1 bài tập chế tạo

- Yêu cầu nộp bài tập:

+ Nộp lại file code lập trình
+ Tạo và điền vào “Bảng chân kết nối các linh kiện điện tử” (*), nộp lại file doc hoặc hình ảnh bảng.

+ Chế tạo robot bằng vật dụng Tinkering kết hợp Arduino và các linh kiện cần thiết

+ Nộp lại video, hình ảnh quay lại quá trình robot hoạt động

Đặt tên file theo mẫu: [Chi nhánh]-[Họ và tên giáo viên]-[Tên môn học]-[Tên bài tập]

[Tên môn học]: Arduino 2

Ví dụ: Để nộp bài kiểm tra thực hành 1, giáo viên đặt tên file như sau:  HCM-Nguyễn Văn

A- Arduino

2- Bai kiem tra thuc hanh

2. Vật tư chuẩn bị:

Chuẩn bị: Arduino (x

1) , LED RGB (x3 màu), đế pin 4 (x

2) , breadboard (x

1) , mạch L298 (x

1) , động cơ vàng (x

2) , màn hình I2C LCD 16x2 (x

1) , cảm biến nhiệt độ, độ ẩm DHT11 (x

1) , mắt thu hồng ngoại IR1838 (x

1) , remote hồng ngoại (x

1) , Bình xịt nước phun sương (x

1) .

.

### Table Data

| Tên thiết bị  | Hình ảnh  | Số lượng  |
| Arduino  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId6.png) | 1  |
| Mạch L298  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId7.png) | 1  |
| Đế 4 pin  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId8.png) | *2  |
| Breadboard  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId9.png) | 1  |
| Động cơ vàng, bánh xe  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId10.png) | 2  |
| Màn hình I2C LCD 16x2  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId11.png) | 1  |
| Cảm biến nhiệt độ, độ ẩm DHT11  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId12.png) | 1  |
| Mắt thu hồng ngoại IR1838  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId13.jpg) | 1  |
| LED RGB  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId14.jpg) | 3 (3 màu khác nhau)  |
| Các loại dây jumper  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId15.png) | 1  |
| Bìa carton 40x40  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId16.png) | 1  |
| Bình xịt nước  (phun sương)  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId17.png) | 1  |

3. Đề bài:

Lập trình, gắn mạch điện và chế tạo xe điều khiển từ xa và thu thập dữ liệu nhiệt độ, độ ẩm thỏa các yêu cầu sau:

1/

Sử dụng 2 đế pin 4 làm nguồn điện (mắc song song) cấp nguồn cho Arduino và mạch L298, sao cho nguồn điện được sử dụng hiệu quả nhất.

2/

Sử dụng mạch L298 và động cơ vàng để làm robot di chuyển tới-lùi và có thể xoay trái-phải

3/

Robot được điều khiển bằng mắt thu và remote hồng ngoại:
  + Phím 2: Robot đi tới
  + Phím 4: Robot xoay trái
  + Phím 5: Robot dừng di chuyển
  + Phím 6: Robot xoay phải
  + Phím 8: Robot đi lùi

4/

Sử dụng cảm biến DHT11 để đo nhiệt độ, độ ẩm và gửi thông tin đến màn hình LC

D.

+ Ở dòng 1 của màn hình LCD luôn hiển thị “N.do:  _____  do C”, với “_____” là nhiệt độ hiện tại đo được qua cảm biến DHT1

1.

+ Ở dòng 2 của màn hình LCD luôn hiển thị “Do am:  _____ %”, với “_____” là nhiệt độ hiện tại đo được qua cảm biến DHT1

1.

5/ Sử dụng đèn 3 LED để thể hiện tình trạng của xe điều khiển:
(Lưu ý: Các màu đèn sau đây có thể tự do thay đổi tùy tình trạng vật tư hiện tại, có thể thay đổi màu khác nhưng vẫn giữ nguyên mục đích của đề bài)

+ Khi khởi động và di chuyển, đèn LED (

1) màu xanh dương sáng lên.

luôn sáng màu xanh lá, thể hiện chương trình đã khởi động thành công.
  + Khi xe di chuyển trong điều kiện nhiệt độ, độ ẩm bình thường (độ ẩm trong khoảng 40-70%, nhiệt độ trong khoảng 25-35 độ

C)

, 2 đèn còn lại đều tắt.
  + Khi xe gặp điều kiện nhiệt độ ngoài khoảng bình thường, một đèn LED (

2)

màu đỏ sáng lên. Khi xe gặp điều kiện độ ẩm ngoài khoảng bình thường, một đèn LED (

3)

6/ Sử dụng bình xịt nước (phun sương) để tạo nên điều kiện thời tiết ẩm ướt và cho xe thu thập dữ liệu và báo hiệu.
7/ Hãy sử dụng các vật dụng cần thiết để chế tạo mô hình xe thỏa các yêu cầu sau:
  + Xe có trục bánh sau chạy bằng động cơ vàng, trục bánh trước xoay được.
  + Xe có thân xe có thể chứa các linh kiện điện tử cần thiết.
  + Lắp đặt động cơ vàng theo vị trí, chiều phù hợp để xe có thể di chuyển theo hướng mong muốn.
  + Lắp đặt mắt thu hồng ngoại ở vị trí phù hợp để dễ dàng nhận tín hiệu từ remote hồng ngoại.
  + Lắp đặt cảm biến độ ẩm DHT11 ở vị trí phù hợp để dễ dàng lấy dữ liệu không khí xung quanh. 
  + Xe có mái che hoặc bộ phận bất kỳ bảo vệ mạch điện, tất cả linh kiện khi phun sương.
  + Xe có tính thẩm mỹ: Các linh kiện được đặt ở vị trí phù hợp, các dây jumper được kết nối gọn gàng, được cố định chặt chẽ…
  + Hình dáng xe có sự sáng tạo (hình dáng, màu sắc, trang trí…).
8/ Điền các thông tin các chân kết nối của các linh kiện điện tử vào “Bảng chân kết nối các linh kiện điện tử” sau:

### Table Data

| Tên linh kiện điện tử  | Các chân kết nối của linh kiện  | Kết nối đến chân của Arduino  |
| LED xanh lá (  1) | Chân dương  |   |
| LED xanh lá (  1) | Chân âm  |   |
| LED đỏ (  2) | Chân dương  |   |
| LED đỏ (  2) | Chân âm  |   |
| LED xanh dương (  3) | Chân dương  |   |
| LED xanh dương (  3) | Chân âm  |   |
| Màn hình LCD I2C  | VCC  |   |
| Màn hình LCD I2C  | GND  |   |
| Màn hình LCD I2C  | SDA  |   |
| Màn hình LCD I2C  | SCL  |   |
| Mắt thu hồng ngoại IR1838  | VCC  |   |
| Mắt thu hồng ngoại IR1838  | GND  |   |
| Mắt thu hồng ngoại IR1838  | SIG  |   |
| Cảm biến nhiệt độ, độ ẩm DHT11  | VCC  |   |
| Cảm biến nhiệt độ, độ ẩm DHT11  | GND  |   |
| Cảm biến nhiệt độ, độ ẩm DHT11  | OUT / DATA  |   |
| Động cơ trái  | x  |   (=> L298) OUT 1,2 hay 3,4  |
| Động cơ phải  | x  |   (=> L298) OUT 1,2 hay 3,4  |
| Mạch L298  | IN 1  |   |
| Mạch L298  | IN 2  |   |
| Mạch L298  | IN 3  |   |
| Mạch L298  | IN 4  |   |

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId18.png)

4. Đáp án:

Mô hình, mạch điện (Chưa có đế pin 4, breadboard)

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId19.png)

Code lập trình

https://planet.mblock.cc/project/2823246

5. Tiêu chí chấm điểm:

### Table Data

| Điểm thực hành = Điểm Tinkering x 0.3 + Điểm Mạch điện x 0.4 + Điểm Code x 0.3 Các thông số điểm được tính theo thang điểm 10.  | Điểm thực hành = Điểm Tinkering x 0.3 + Điểm Mạch điện x 0.4 + Điểm Code x 0.3 Các thông số điểm được tính theo thang điểm 10.  | Điểm thực hành = Điểm Tinkering x 0.3 + Điểm Mạch điện x 0.4 + Điểm Code x 0.3 Các thông số điểm được tính theo thang điểm 10.  | Điểm thực hành = Điểm Tinkering x 0.3 + Điểm Mạch điện x 0.4 + Điểm Code x 0.3 Các thông số điểm được tính theo thang điểm 10.  | Điểm thực hành = Điểm Tinkering x 0.3 + Điểm Mạch điện x 0.4 + Điểm Code x 0.3 Các thông số điểm được tính theo thang điểm 10.  | Điểm thực hành = Điểm Tinkering x 0.3 + Điểm Mạch điện x 0.4 + Điểm Code x 0.3 Các thông số điểm được tính theo thang điểm 10.  |
| Tên học viên  | Nộp file  | Điểm  | Điểm  | Điểm  | Điểm  |
| Tên học viên  | Nộp file  | Tinkering  | Mạch điện  | Code  | Điểm thực hành  |
|   |   |   |   |   |   |
|   |   |   |   |   |   |

Tinkering (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)

1/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId21.png)

Xe có đầy đủ các bộ phận sau: bánh xe sau (động cơ vàng), trục bánh xe trước, thân xe, thiết bị bảo vệ các LKĐT (linh kiện điện tử). (1đ)

2/ 1

Thân xe có kích thước, hình dáng phù hợp, có thể chứa các LKĐT. (1đ)

3/ 1

Trục bánh xe trước chế tạo bằng các dụng cụ Tinkering và xoay được. (1đ)

4/ 1

Lắp đặt động cơ vàng theo vị trí, chiều phù hợp để xe có thể di chuyển theo hướng mong muốn. (1đ)

5/ Lắp đặt mắt thu hồng ngoại ở vị trí phù hợp để dễ dàng nhận tín hiệu từ remote hồng ngoại. (1đ)

6/ Lắp đặt cảm biến độ ẩm DHT11 ở vị trí phù hợp để dễ dàng lấy dữ liệu không khí xung quanh.  (1đ)

7/ Lắp đặt màn hình LCD và đèn LED ở vị trí phù hợp để dễ dàng xem thông tin và cảnh báo. (1đ)

8/ Xe có thiết kế mái che hoặc bộ phận bất kỳ bảo vệ mạch điện, tất cả linh kiện khi phun sương. (1đ)

9/ Xe có tính thẩm mỹ: Các linh kiện được đặt ở vị trí phù hợp, các dây jumper được kết nối gọn gàng, được cố định chặt chẽ… (1đ)

10/ Hình dáng xe có sự sáng tạo (hình dáng, màu sắc, trang trí…). (1đ)

Mạch điện (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)

Dựa vào mạch điện trên xe điều khiển và “Bảng chân kết nối các linh kiện điện tử” được nộp, xét các tiêu chí sau:

1/ 1

Có sử dụng Breadboard để tạo các chân cắm bổ sung cho mạch điện. (0.5đ)

2/ Đáp án mẫu

Ở nguồn điện 4 pin, dây âm (đen) được kết nối đến chân GND của L298 và chân GND bất kỳ của Arduino. (0.5đ)

3/ https://planet.mblock.cc/project/2823246

Ở nguồn điện 4 pin, sau khi kết nối dây dương (đỏ) được kết nối SONG SONG đến chân 12V+ của L298 và chân VIN của Arduino. (1đ)

4/ Khi khởi động, lập trình được 1 đèn LED (

Ở 3 đèn LED RGB, chân âm (ngắn) được gắn vào chân GND bất kỳ. (0.5đ)

5/ Ở 3 đèn LED RGB, chân dương (dài) được gắn vào 3 chân Digital bất kỳ (D__) của Arduino. (0.5đ)

6/ Ở màn hình LCD, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (0.5đ)

7/ Ở màn hình LCD, chân SDA được gắn chính xác vào chân analog A4 của Arduino. (1đ)

8/ Ở màn hình LCD, chân SCL được gắn chính xác vào chân analog A5 của Arduino. (1đ)

9/ Ở mắt thu hồng ngoại, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (0.5đ)

10/ Ở mắt thu hồng ngoại, chân SIG được gắn vào chân Digital bất kỳ (D__)  của Arduino. (1đ)

1/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId23.png)

Ở cảm biến nhiệt độ, độ ẩm, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (0.5đ)

2/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId24.png)

Ở cảm biến nhiệt độ, độ ẩm, chân OUT / DATA được gắn vào chân Digital bất kỳ (D__)  của Arduino. (1đ)

3/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId25.png)

Ở mỗi động cơ vàng, nối 2 đầu cực của động cơ đến 2 chân OUT1, OUT2 hoặc OUT3, OUT4 của mạch L298. (0.5đ)

4/ (0.5đ)

Ở mạch L298, nối các chân IN 1, 2, 3, 4 đến các chân Digital PWM bất kỳ của Arduino (Chân pin digital có dấu “~”, ví dụ D5~). (1đ)

Code lập trình (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)

Dựa vào code lập trình và “Bảng chân kết nối các linh kiện điện tử” được nộp, xét các tiêu chí sau:

1/ (0.5đ)

1) <3> - If "Data IR was receive?"

sáng, thể hiện chương trình đã khởi động thành công. (0.5đ)

2/ <4> ---- If "IR read data" = 2 (Di chuyển)

Khi khởi động, có sử dụng câu lệnh “Set address LCD” để kết nối LCD với Arduino. (0.5đ)

3/ <5> ---- If "IR read data" = 4 (Di chuyển)

Khi khởi động, có sử dụng câu lệnh “IR ReceiveNo.1: Set digital pin” để kết nối mắt thu hồng ngoại với Arduino. (0.5đ)

4/ <6> ---- If "IR read data" = 6 (Di chuyển)

Ở MỌI câu lệnh mắt thu hồng ngoại, số chân digital pin phải khớp với thông tin được nhập ở “Bảng chân kết nối các linh kiện điện tử” (0.5đ)

5/ Khi khởi động, có sử dụng câu lệnh “Temper&humidity 1: Set digital pin” để kết nối mắt thu hồng ngoại với Arduino. (0.5đ)

6/ Ở MỌI câu lệnh cảm biến nhiệt độ, độ ẩm, số chân digital pin phải khớp với thông tin được nhập ở “Bảng chân kết nối các linh kiện điện tử”. (0.5đ)

7/ Khi khởi động, trong vòng lặp forever lập trình được màn hình LCD luôn hiển thị “N.do:  _____  do C”, với “_____” là nhiệt độ hiện tại đo được qua cảm biến DHT11 ở dòng

1. <7> ---- If "IR read data" = 8 (Di chuyển)

8/ Khi khởi động, trong vòng lặp forever lập trình được màn hình LCD luôn hiển thị “Do am:  _____ %”, với “_____” là độ ẩm hiện tại đo được qua cảm biến DHT11 ở dòng

2. 1

9/ Chương trình có tổng cộng ít nhất 8 câu lệnh If nằm trong vòng lặp forever, được sắp xếp như sau:

<1> - If  "humidity (độ ẩm)" > 40 hoặc "humidity (độ ẩm)" < 70 (Tắt LE

D) 1

- If  "humidity (độ ẩm)" < 40 hoặc "humidity (độ ẩm)" < 40 (Sáng LE

D) 1

<2> - If  "temperature (nhiệt độ)" > 40 hoặc "humidity (độ ẩm)" < 70 (Tắt LE

D) Trong phần điều kiện <

- If  "humidity (độ ẩm)" < 40 hoặc "humidity (độ ẩm)" < 40 (Sáng LE

D) 1

<8> ---- If "IR read data" = 5 (Di chuyển)
(0.25x8 = 2đ)

10/ Trong phần điều kiện <1>, lập trình được một đèn LED (

2) (0.2x5 = 1đ)

TẮT khi độ ẩm trong khoảng 40-70% và SÁNG khi không trong khoảng đó. (0.5đ)

1/

Trong phần điều kiện <2>, lập trình được một đèn LED (

3)

TẮT khi nhiệt độ trong khoảng 25-35 độ C và SÁNG khi không trong khoảng đó. (0.5đ)

2/

Trong phần điều kiện <3>, có sử dụng câu lệnh “IR ReceiveNo.1: Restart” để reset tín hiệu mỗi lần nhấn nút từ remote hồng ngoại. (0.5đ)

3/

4-

8>, các câu lệnh điều khiển động cơ có chân digital PIN PWM khớp với thông tin được nhập ở “Bảng chân kết nối các linh kiện điện tử”. (0.5đ)

4/

So sánh với mô hình thực tế và lựa chọn các công suất phù hợp, lập trình được mô hình di chuyển tới / lùi / xoay trái / xoay phải / dừng lại (0.2x5 = 1đ)

15/ So sánh với mô hình thực tế, mô hình di chuyển đúng với các nút nhấn từ remote hồng ngoại được yêu cầu.

+ Phím 2: Robot đi tới
  + Phím 4: Robot xoay trái
  + Phím 5: Robot dừng di chuyển
  + Phím 6: Robot xoay phải
  + Phím 8: Robot đi lùi