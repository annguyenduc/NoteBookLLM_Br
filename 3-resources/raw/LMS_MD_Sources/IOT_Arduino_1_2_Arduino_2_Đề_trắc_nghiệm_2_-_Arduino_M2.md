---
title: Đề trắc nghiệm 2 - Arduino M2.docx
source: [[Đề trắc nghiệm 2 - Arduino M2.docx]]
type: RAW_SOURCE
---

ĐỀ KIỂM TRA TRẮC NGHIỆM - Lập trình Arduino Module 2
(Đề

2) - Thời gian làm bài: 25 phút

- 15 câu: 6 nhận biết (40%) - 9 thông hiểu (60%)
- Câu trắc nghiệm 1 đáp án: 1 điểm
- Câu trắc nghiệm nhiều đáp án: Số điểm = số đáp án đúng, đúng 1 câu được 1 điểm

- Đề kiểm tra thực hành
- Điểm đạt: 75% điểm tối đa

### Table Data

| Các kiến thức cần đạt  | Nhận biết (5 câu)  | Thông hiểu / Vận dụng (10 câu)  |
| Ôn tập kiến thức cũ - Cấu tạo Arduino - Cảm biến hồng ngoại, mưa - Servo - Các câu lệnh lập trình  | 1  | 2,3  |
| Màn hình LCD  | 4  | 5,6  |
| Cảm biến nhiệt độ độ ẩm DHT11  |   | 7  |
| Cảm biến ánh sáng  |   | 8  |
| Cảm biến siêu âm  | 9  |   |
| Joystick  | 10  | 11,12  |
| Remote và mắt thu hồng ngoại  |   |   |
| Mạch L298 và động cơ vàng, động cơ bơm  | 13  | 14,15  |

Câu 1 (Nhận biết)

Hãy cho biết đèn LED nào sáng khi có vật cản ở phía trước?

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId6.png)

A/

B/

C/

D/

Câu 2 (Thông hiểu)

Cho các linh kiện điện tử và sơ đồ mạch điện:

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId7.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId8.png)

Khi nạp đoạn code sau thì đèn LED nào sẽ sáng:

A/ LED xanh

B/ LED xanh và LED vàng

C/ LED vàng

D/ LED đỏ

Câu 3 (Thông hiểu)

Cho sơ đồ mạch điện và bảng kết nối linh kiện như sau:

### Table Data

| Tên linh kiện  | Chân kết nối của linh kiện  | Chân kết nối của Arduino  |
| LED XANH LÁ  | Chân dương  | D4  |
| LED XANH LÁ  | Chân âm  | GND  |
| LED ĐỎ  | Chân dương  | D6  |
| LED ĐỎ  | Chân âm  | GND  |
| LED VÀNG  | Chân dương  | D8  |
|   | Chân âm  | GND  |

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId9.png)

Tìm lỗi sai của mạch trên:

A/ Nối sai cực của LED đỏ

B/ Không cấp nguồn cho LED xanh lá

C/ Cấp sai nguồn cho LED vàng

D/

LED xanh lá và LED đỏ nối chung một chân tín hiệu.

Câu 4 (Nhận biết)

LCD I2C có bao nhiêu chân kết nối và kí hiệu các chân?

A/ 4 chân (VCC, GND, SCL, SD

A) 4 chân (VCC, GND, LCD, SD

B/ 4 chân (VCC, GND, LCD, DS

A) 4 chân (VCC, GND, SCL, DS

C/

A)

D/

A)

Câu 5 (Thông hiểu)

Đoạn lập trình nào phù hợp với hiệu ứng sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId10.gif)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId11.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId12.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId13.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId13.png)

Câu 6 (Thông hiểu)

Đoạn lệnh nào sau đây làm cho màn hình LCD hiện lên dòng chữ như sau?

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId14.gif)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId15.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId16.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId17.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId18.png)

Câu 7 (Thông hiểu)

Sử dụng cảm biến nhiệt độ, độ ẩm DHT11 và màn hình LCD, đoạn lệnh nào sau đây thực hiện yêu cầu sau:

- Ở dòng 1 của màn hình LCD hiện lên “N.Do: ____ do C”; Với “___” là số đo nhiệt độ nhận được từ cảm biến DHT1

1. Với đoạn chương trình sau:

- Ở dòng 2 của màn hình LCD hiện lên “Do am: ____ %”; Với “___” là số đo % độ ẩm nhận được từ cảm biến DHT1

1.

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId19.png)

- Nếu nhiệt độ cao hơn 27 độ thì đèn LED số 13 sáng. Nếu không thì LED số 13 tắt.

Thêm đoạn lệnh nào thì chương trình thực hiện như yêu cầu đề bài?

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId20.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId21.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId22.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId23.png)

Câu 8 (Thông hiểu)

Cho các linh kiện điện tử và các chân kết nối như bảng dưới đây:

### Table Data

| Tên linh kiện  | Chân kết nối của linh kiện  | Chân kết nối của Arduino  |
| Cảm biến ánh sáng  | VCC  | 5V  |
| Cảm biến ánh sáng  | GND  | GND  |
| Cảm biến ánh sáng  | D0  | D8  |
| Đèn Led  | Chân dương  | D7  |
| Đèn Led  | Chân âm  | GND  |

Chọn chương trình thực hiện đúng yêu cầu nếu trời sáng thì đèn tắt, nếu trời tối thì đèn sáng.

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId24.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId25.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId26.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId27.png)

Câu 9 (Nhận biết)

Câu lệnh nào phù hợp với cách lắp mạch dưới đây?

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId28.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId29.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId30.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId31.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId32.png)

Câu 10 (Nhận biết)

Joystick có bao nhiêu chân kết nối?

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId33.png)

A/ 5

B/ 4

C/ 6

D/ 3

Câu 11 (Thông hiểu)

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId34.png)

Khi núm điều khiển trên Joystick được gạt qua trái, giá trị X hay Y sẽ thay đổi và thay đổi trong khoảng bao nhiêu?

A/ X : từ 511 về 0

B/ X : từ 511 đến 1023

C/ Y: từ 511 đến 0

D/ Y : từ 511 đến 1023

Câu 12 (Thông hiểu)

Cho mạch điện gồm 1 joystick, 1 servo với chương trình có hiệu ứng: Nếu giá trị VRx > 300  xoay qua trá và VRx < 600 thì servo xoay qua phải. Mỗi lần quay 5 độ. Servo sẽ dừng quay khi đạt đến giới hạn. Giới hạn của servo là 0 đến 180 độ.

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId35.png)

Điền vào các giá trị A và B để chương trình thực hiện yêu cầu?

Các chân linh kiện được nối như thế nào?

A/ A: 181

B: 0

B/ A: 90

B: 90

C/ A: 0

B: 180

D/ A: 90

B: 0

Câu 13 (Nhận biết)

Phát biểu nào sau đây là đúng?

A/ Điện áp hoạt động tối đa của mạch L298 là 12V

B/ Số thiết bị điều khiển tối đa là 4

C/ Mạch L298 không điều khiển được động cơ giảm tốc

D/ Điện áp mạch L298 cấp cho thiết bị tối đa là 12V

Câu 14 (Thông hiểu)

Một học sinh lắp mạch hoạt động bằng Arduino, mạch L298 và động cơ vàng như mạch điện như hình dưới.

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId36.png)

Học sinh nạp đoạn chương trình như sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId37.png)

Chương trình nào hoạt động giống đoạn chương trình học sinh đã nạp?

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId38.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId39.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId40.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId41.png)

Câu 15 (Thông hiểu)

Cho mạch điều khiển động cơ bằng joystick như sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId42.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId43.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId44.png)

Hãy cho biết đoạn code A làm cho động cơ thực hiện hành động nào?

A/ Dừng lại

B/ Đi tới

C/ Rẽ trái

D/ Rẽ phải

ĐỀ THỰC HÀNH

Đề kiểm tra thực hành

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

1) , đèn LED đơn (x

2) , đế pin 4 (x

2) , breadboard (x

1) , mạch L298 (x

1) , động cơ vàng và bánh xe (x

2) , cảm biến ánh sáng (x

1) , cảm biến siêu âm (x

1) .

, dây điện jumper các loại, bìa carton và các dụng cụ Tinkering khác.

### Table Data

| Tên thiết bị  | Hình ảnh  | Số lượng  |
| Arduino  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId45.png) | 1  |
| Mạch L298  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId46.png) | 1  |
| Đế 4 pin  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId47.png) | 2  |
| Breadboard  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId48.png) | 1  |
| Động cơ vàng, bánh xe  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId49.png) | 2  |
| Cảm biến siêu âm  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId50.png) | 1  |
| Cảm biến ánh sáng  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId51.png) | 1  |
| LED đơn  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId52.jpg) | 2  |
| Các loại dây jumper  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId53.png) | 1  |
| Bìa carton 40x40cm  |  ![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId54.png) | 1  |

3. Đề bài:

Lập trình, gắn mạch điện và chế tạo xe tự né vật cản thỏa các yêu cầu sau:

Mô hình xe gồm các linh kiện điện tử như sau:

Sử dụng 2 đế pin 4 (mắc song song) làm nguồn điện cấp nguồn cho Arduino và mạch L298, sao cho nguồn điện được sử dụng hiệu quả nhất.

Sử dụng mạch L298 và động cơ vàng để làm robot di chuyển tới-lùi, xoay trái-phải.

Sử dụng cảm biến siêu âm để xe tự động né vật cản.

Sử dụng 2 đèn LED để làm đèn soi sáng cho xe.

Sử dụng cảm biến ánh sáng để đo cường độ ánh sáng môi trường xung quanh.

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId55.png)

(Hình minh họa trên chưa có đế pin, breadboard và các dây kết nối)

Yêu cầu lập trình:

1/ Sau đó, xe bắt đầu tự di chuyển thẳng.

Khi khởi động, xe đứng yên, 2 đèn chớp tắt cùng nhau 3 lần.

2/ Yêu cầu chế tạo:

3/

Mỗi khi gặp vật cản, xe di chuyển lùi lại và xoay, di chuyển hướng khác.

4/

Nếu môi trường xung quanh đang sáng đèn, 2 đèn LED sẽ tắt. Ngược lại, nếu môi trường xung quanh đang tối, 2 đèn LED sẽ tự động bật lên.

5/ Hãy sử dụng các vật dụng cần thiết để chế tạo mô hình xe thỏa các yêu cầu sau:

Xe có trục bánh sau chạy bằng động cơ vàng, trục bánh trước xoay được.

Xe có thân xe có thể chứa các linh kiện điện tử cần thiết.

Lắp đặt động cơ vàng theo vị trí, chiều phù hợp để xe có thể di chuyển theo hướng mong muốn.

Lắp đặt cảm biến ánh sáng ở vị trí phù hợp để dễ dàng đo cường độ ánh sáng xung quanh.

Xe có tính thẩm mỹ: Các linh kiện và breadboard được đặt ở vị trí phù hợp, các dây jumper được kết nối gọn gàng, được cố định chặt chẽ…

Hình dáng xe có sự sáng tạo (hình dáng, màu sắc, trang trí…).

8/ Điền các thông tin các chân kết nối của các linh kiện điện tử vào “Bảng chân kết nối các linh kiện điện tử” sau:

### Table Data

| Tên linh kiện điện tử  | Các chân kết nối của linh kiện  | Kết nối đến chân của Arduino  |
| LED (  1) | Chân dương  |   |
| LED (  1) | Chân âm  |   |
| LED (  2) | Chân dương  |   |
| LED (  2) | Chân âm  |   |
| Cảm biến siêu âm  | VCC  |   |
| Cảm biến siêu âm  | Trig  |   |
| Cảm biến siêu âm  | Echo  |   |
| Cảm biến siêu âm  | GND  |   |
| Cảm biến ánh sáng  | VCC  |   |
| Cảm biến ánh sáng  | GND  |   |
| Cảm biến ánh sáng  | OUT / DO  |   |
| Động cơ trái  | x  |   (=> L298) OUT 1,2 hay 3,4  |
| Động cơ phải  | x  |   (=> L298) OUT 1,2 hay 3,4  |
| Mạch L298  | IN 1  |   |
| Mạch L298  | IN 2  |   |
| Mạch L298  | IN 3  |   |
| Mạch L298  | IN 4  |   |

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId56.png)

4. Đáp án:

Mô hình, mạch điện

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId57.png)

“Bảng chân kết nối các linh kiện điện tử” sau:

### Table Data

| Tên linh kiện điện tử  | Các chân kết nối của linh kiện  | Kết nối đến chân của Arduino  |
| LED (  1) | Chân dương  |   |
| LED (  1) | Chân âm  |   |
| LED (  2) | Chân dương  |   |
| LED (  2) | Chân âm  |   |
| Cảm biến siêu âm  | VCC  |   |
| Cảm biến siêu âm  | Trig  |   |
| Cảm biến siêu âm  | Echo  |   |
| Cảm biến siêu âm  | GND  |   |
| Cảm biến ánh sáng  | VCC  |   |
| Cảm biến ánh sáng  | GND  |   |
| Cảm biến ánh sáng  | OUT / DO  |   |
| Động cơ trái  | x  |   (=> L298) OUT 1,2 hay 3,4  |
| Động cơ phải  | x  |   (=> L298) OUT 1,2 hay 3,4  |
| Mạch L298  | IN 1  |   |
| Mạch L298  | IN 2  |   |
| Mạch L298  | IN 3  |   |
| Mạch L298  | IN 4  |   |

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

1/ Đáp án mẫu

Xe có đầy đủ các bộ phận sau: bánh xe sau (động cơ vàng), trục bánh xe trước, thân xe. (0,7đ)

2/ <1> - If  "độ sáng" < … (Sáng LE

Thân xe có kích thước, hình dáng phù hợp, có thể chứa các LKĐT. (0,7đ)

3/ <2> - If  "độ sáng" > … (Tắt LE

Trục bánh xe trước chế tạo bằng các dụng cụ Tinkering và xoay được. (0,7đ)

4/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId60.png)

Lắp đặt động cơ vàng theo vị trí, chiều phù hợp để xe có thể di chuyển theo hướng mong muốn. (0,7đ)

5/ Lắp đặt cảm biến ánh sáng ở vị trí phù hợp để dễ dàng đo cường độ ánh sáng xung quanh.  (0,7đ)

6/ Xe có tính thẩm mỹ: Các linh kiện được đặt ở vị trí phù hợp, các dây jumper được kết nối gọn gàng, được cố định chặt chẽ… (0,7đ)

7/ Hình dáng xe có sự sáng tạo (hình dáng, màu sắc, trang trí…). (0,7đ)

Mạch điện (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)

Dựa vào mạch điện trên xe điều khiển và “Bảng chân kết nối các linh kiện điện tử” được nộp, xét các tiêu chí sau:

1/

![Image](../assets/IOT_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId61.png)

Ở nguồn điện 4 pin, dây âm (đen) được kết nối đến chân GND bất kỳ của Arduino. (1đ)

2/

Ở nguồn điện 4 pin, dây dương (đỏ) được kết nối kết nối đến chân VIN của Arduino. (1đ)

3/

Ở 2 đèn LED RGB, chân âm (ngắn) được gắn vào chân GND bất kỳ. (1đ)

4/

Ở 2 đèn LED RGB, chân dương (dài) được gắn vào 1 hoặc 2 chân Digital bất kỳ (D__) của Arduino. (1đ)

5/ Ở cảm biến ánh sáng, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (1đ)

6/ Ở cảm biến ánh sáng, chân AO (hoặc DO) được gắn vào chân Analog (A__)  (hoặc Digital (D__) ) bất kỳ của Arduino. (1đ)

7/ Ở cảm biến siêu âm, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (1đ)

8/ Ở cảm biến siêu âm, chân Trig và Echo được gắn vào 2 chân Digital bất kỳ (D__)  của Arduino. (1đ)

9/ Ở mỗi động cơ vàng, nối 2 đầu cực của động cơ đến 2 chân OUT1, OUT2 hoặc OUT3, OUT4 của mạch L298. (1đ)

10/ Ở mạch L298, nối các chân IN 1, 2, 3, 4 đến các chân Digital PWM bất kỳ của Arduino (Chân pin digital có dấu “~”, ví dụ D5~). (1đ)

Code lập trình (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)

https://drive.google.com/file/d/1iqENn7v9afO6MUR_6KB_tzHsOfDgu38N/view?usp=drive_link

Dựa vào code lập trình và “Bảng chân kết nối các linh kiện điện tử” được nộp, xét các tiêu chí sau:

1/

Khi khởi động, lập trình được 2 đèn chớp tắt cùng nhau 3 lần. (1đ)

2/

Chương trình có tổng cộng ít nhất 4 câu lệnh If nằm trong vòng lặp forever, được sắp xếp như sau:

D)

D)

<3> - If  "khoảng cách đến vật cản" > … (Xe đi thẳng)

<4> - If  "khoảng cách đến vật cản" < … (Xe đi lùi và xoay hướng khác)
(0.25x4 = 1đ)

3/

Trong phần điều kiện <1,2>, sử dụng được câu lệnh “Read analog pin < …” để xét điều kiện và đo độ sáng môi trường. (1đ)

4/

Trong phần điều kiện <3,4>, sử dụng được câu lệnh “Read ultrasonic sensor… < …” để xét điều kiện và đo khoảng cách đến vật cản. (1đ)

5/ Trong phần điều kiện <1>, lập trình được 2 đèn LED sáng cùng nhau. (1đ)

6/ Trong phần điều kiện <2>, lập trình được 2 đèn LED tắt cùng nhau. (1đ)

7/ Trong phần điều kiện <3>, lập trình được 2 động cơ xoay cùng lúc về phía trước để đi thẳng. (1đ)

8/ Trong phần điều kiện <4>, lập trình được 2 động cơ xoay cùng lúc về phía sau để đi lùi. (1đ)

9/ Trong phần điều kiện <4>, sau khi đi lùi, lập trình được 1 động cơ đứng yên, 1 động cơ còn lại xoay để xe xoay hướng khác. (1đ)

10/ Trong phần điều kiện <4>, có sử dụng câu lệnh “Chờ” ở sau hai hành động đi lùi và xoay hướng khác. (1đ)