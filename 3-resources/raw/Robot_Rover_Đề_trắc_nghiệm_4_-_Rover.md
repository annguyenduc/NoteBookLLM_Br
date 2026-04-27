---
title: Đề trắc nghiệm 4 - Rover.docx
source: [[Đề trắc nghiệm 4 - Rover.docx]]
type: RAW_SOURCE
---

ĐỀ KIỂM TRA TRẮC NGHIỆM - Robot Rover (Không nâng cao)
(Đề

4) - Thời gian làm bài: 45 phút (30 câu)

- 30 câu: 12 nhận biết (40%) - 18 thông hiểu (60%)
- Câu trắc nghiệm 1 đáp án: 1 điểm
- Câu trắc nghiệm nhiều đáp án: Số điểm = số đáp án đúng, đúng 1 câu được 1 điểm
- Điểm đạt: 70% điểm tối đa

### Table Data

|   Các kiến thức cần đạt  |   |   |
|   Các kiến thức cần đạt  | Nhận biết (12 câu)  | Thông hiểu /  Vận dụng (18 câu)  |
| Sử dụng mạch Yolobit và robot Rover - Các bộ phận, phần cứng trên mạch Yolobit - Các bước kết nối, lập trình Yolobit - Chế độ Live và Upload - Cách reset bộ nhớ trên Yolobit - Lưu trữ và chia sẻ dự án - Sử dụng pin Rover - Các bộ phận, phần cứng trên robot Rover  |   1,4      2  3  5  6,7  |   |
| Lập trình Rover sáng đèn LED  | 8  | 9,10,11  |
| Lập trình Rover di chuyển  | 12  | 13,14,15,16  |
| Lập trình Rover điều khiển tay gắp với Servo  |   | 17,18  |
| Lập trình hiển thị các thông số của cảm biến - Vị trí các loại cảm biến (CB nhiệt độ, ánh sáng, gia tốc)  - Hiển thị thông tin với "Cửa sổ thông tin" và "Cửa sổ nhập lệnh" - Lập trình với nút nhấn A,B - Biến số  |   19            |       21,23    20,22    |
| Lập trình Rover dò đường - Cảm biến dò đường trên robot - Câu lệnh cảm biến dò đường  |   24  |   25,26    |
| Lập trình Rover né vật cản - Cảm biến siêu âm trên robot - Câu lệnh cảm biến siêu âm  |   27  |   28  29,30  |

Câu 1 (Nhận biết)

Phần cứng nào sau đây KHÔNG được gắn trên mạch Yolobit?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId7.png)

A/ Cảm biến dò đường

B/ Cảm biến nhiệt độ

C/ Anten wifi và Bluetooth

D/ Cảm biến gia tốc, cảm biến nghiêng

Câu 2 (Nhận biết)

Làm thế nào để nạp lại chương trình mặc định cho Rover?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId8.png)

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId9.png)

A/

Tải và cài đặt thư viện Rover vào Yolo:Bit, nhấn vào nút A trên Yolo:Bit.

B/

Tải và cài đặt thư viện Rover vào Yolo:Bit, RESET lại robot bằng cách nhấn vào nút RESET trên mạch Yolo:Bit.

C/

Tải và cài đặt thư viện Rover vào Yolo:Bit, nhấn vào nút B trên Yolo:Bit.

D/

Chỉ cần tải và cài đặt thư viện Rover vào Yolo:Bit.

Câu 3 (Nhận biết)

Khi muốn import file lập trình app.ohstem.vn, file sẽ có định dạng đuôi là gì?

A/ .ino

B/ .sb3

C/ .json

D/ .mblock

Câu 4 (Nhận biết)

Màn hình LED nhiều màu trên mạch Yolobit có bao nhiêu đèn LED?

A/ 25

B/ 6

C/ 20

D/ 36

Câu 5 (Nhận biết)

Quan sát hình ảnh dưới đây, Robot Rover đang ở trạng thái nào?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId10.png)

A/ Rover đang được sạc pin

B/ Kết nối Rover với máy tính

C/ Nạp chương trình cho Rover

D/ Kiểm tra pin của Rover

Câu 6 (Nhận biết)

Nối các bộ phận của robot Rover với tên tương ứng.

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId11.png)

Số 1: Cảm biến siêu âm

Số 2: Mắt nhận tia hồng ngoại

Số 3: Cảm biến dò đường

Số 4: Cổng mở rộng

Số 5: Động cơ

Số 6: Đèn LED nhiều màu

Câu 7 (Nhận biết)

Đèn LED RGB nào gần với nút nguồn của Rover?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId12.png)

A/ LED RGB số 4,5,6

B/ LED RGB số 1,2,3

C/ LED RGB số 1,3,5

D/ LED RGB số 2,4,6

Câu 8 (Nhận biết)

Đèn LED của Rover có tổng cộng bao nhiêu màu phát sáng?

A/ 6

B/ 7

C/ 8

D/ 9

Câu 9 (Thông hiểu)

Đoạn chương trình nào chỉ làm LED số 1 sáng tắt 2 lần sau đó tắt hẳn?

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId13.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId14.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId15.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId16.png)

Câu 10 (Thông hiểu)

Đoạn chương trình nào sau đây phù hợp để lập trình robot sáng đèn LED như hình sau đây khi nhấn nút A trên mạch Yolobit?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId17.gif)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId18.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId19.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId20.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId21.png)

Câu 11 (Thông hiểu)

Đoạn chương trình nào làm tất cả đèn LED trên Rover đổi 3 màu liên tục?
(Nhiều đáp án)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId22.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId23.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId24.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId25.png)

Câu 12 (Nhận biết)

Phát biểu nào sau đây là đúng khi nói về khối lệnh di chuyển dưới đây?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId26.png)

A/

Khi tốc độ của bánh trái và bánh phải bằng nhau và đều nhỏ hơn 0, robot sẽ di chuyển lùi ngược về sau.

B/

Khi tốc độ của bánh trái và bánh phải đều nhỏ hơn 0, robot đứng yên vì tốc độ của động cơ phải lớn hơn 0.

C/

Khi tốc độ của bánh trái lớn hơn 0 và bánh phải nhỏ hơn 0, robot xoay vòng tròn tại chỗ theo chiều ngược chiều kim đồng hồ.

D/

Khi tốc độ của bánh trái nhỏ hơn 0 và bánh phải lớn hơn 0, robot xoay vòng tròn tại chỗ cùng chiều kim đồng hồ.

Câu 13 (Thông hiểu)

Hãy lựa chọn quỹ đạo di chuyển phù hợp của robot khi thực hiện chương trình sau.

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId27.png)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId28.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId29.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId30.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId31.png)

Câu 14 (Thông hiểu)

Điền vào dấu … các dấu <, >, = trong đoạn lệnh để robot chạy được quỹ đạo dưới đây.
(Dạng ghép nối)

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId32.png)

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId33.png)

Đáp án

A … 0

>

B … 0

>

C … 0

>

D …0

< hoặc =

Câu 15 (Thông hiểu)

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId34.gif)

Đoạn lệnh nào còn thiếu trong chương trình dưới đây để lập trình robot có hiệu ứng di chuyển và đèn LED lặp lại mãi mãi như hình trên?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId35.png)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId36.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId37.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId38.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId39.png)

Câu 16 (Thông hiểu)

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId40.png)

Robot sẽ thực hiện những hành động gì khi chạy chương trình trên?

A/

Robot đi tới trong 1 giây sau đó đi lùi mãi mãi; Khi đi tới, đèn LED sáng đèn màu xanh lá, khi đi lùi, đèn LED sáng màu đỏ.

B/

Robot đi tới-lùi sau mỗi 1 giây, lặp lại mãi mãi; Khi đi tới, đèn LED sáng đèn màu xanh lá, khi đi lùi, đèn LED sáng màu đỏ.

C/

Robot đi tới trong 1 giây sau đó đi lùi mãi mãi; Khi đi tới, đèn LED sáng đèn màu đỏ, khi đi lùi, đèn LED sáng màu xanh lá.

D/

Robot đi tới-lùi sau mỗi 1 giây, lặp lại mãi mãi; Khi đi tới, đèn LED sáng đèn màu đỏ, khi đi lùi, đèn LED sáng màu xanh lá.

Câu 17 (Thông hiểu)

Sử dụng động cơ Servo, đoạn chương trình nào sau đây phù hợp để lập trình robot đóng, mở tay gắp, lặp lại mãi mãi như hình sau đây?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId41.gif)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId42.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId43.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId44.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId45.png)

Câu 18 (Thông hiểu)

Sử dụng động cơ Servo, đoạn chương trình nào sau đây phù hợp để lập trình robot thực hiện yêu cầu sau:
- Mỗi khi nhấn nút A trên mạch Yolobit, tất cả đèn LED trên robot sáng màu xanh lá và tay gắp sẽ mở ra (Servo xoay góc 90 độ).
- Mỗi khi nhấn nút B trên mạch Yolobit, tất cả đèn LED trên robot sáng màu đỏ và tay gắp sẽ đóng lại (Servo xoay góc 0 độ).

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId46.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId47.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId48.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId49.png)

Câu 19 (Nhận biết)

Phần cứng số 4 trên mạch Yolobit được gọi là gì?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId50.png)

A/ Cảm biến ánh sáng

B/ Cảm biến gia tốc

C/ Cảm biến nhiệt độ, độ ẩm

D/ Vi xử lý

Câu 20 (Thông hiểu)

Cho yêu cầu sau:
- Khi khởi động, robot sáng tất cả đèn LED màu đỏ.
- Mỗi lần nhấn nút A, một đèn sẽ tắt, lần lượt từ đèn 1 đến đèn 6.
- Khi tất cả đèn đã tắt, khi nhấn nút A, tất cả đèn LED lại sáng màu đỏ.

Đoạn lệnh nào còn thiếu trong chương trình sau đây để robot thực hiện yêu cầu trên?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId51.png)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId52.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId53.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId54.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId55.png)

Câu 21 (Thông hiểu)

Hãy lựa chọn chương trình phù hợp để điều khiển robot thỏa yêu cầu sau:
Sử dụng cảm biến nhiệt độ và đưa robot đến các vị trí có nhiệt độ khác nhau, lập trình để robot sáng đèn LED các màu khác nhau khi nhận đo được các giá trị nhiệt độ khác nhau.
- Nếu nhiệt độ nhỏ hơn 25 độ C, đèn LED sáng màu xanh dương.
- Nếu nhiệt độ trong khoảng 25-27 độ C, đèn LED sáng màu xanh lá.
- Nếu nhiệt độ lớn hơn 27 độ C, đèn LED sáng màu đỏ.

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId56.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId57.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId58.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId59.png)

Câu 22 (Thông hiểu)

Cho yêu cầu sau:
- Khi khởi động, robot tắt tất cả đèn LE

D.

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId60.png)

- Khi nhấn nút A, một đèn sẽ sáng màu đỏ, lần lượt từ đèn 1 đến đèn 6.

- Sau khi tất cả đèn đã sáng, mỗi lần nhấn nút A, tất cả đèn LED lại chớp tắt 3 lần màu trắng.

Đoạn lệnh còn thiếu trong chương trình sau đây để robot thực hiện yêu cầu trên là gì?

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId61.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId62.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId63.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId64.png)

Câu 23 (Thông hiểu)

Hãy lựa chọn chương trình phù hợp để điều khiển robot liên tục  hiển thị số đo khoảng cách lên màn hình lập trình và màn hình LED trên mạch Yolobit khi đặt vật cản ở các khoảng cách khác nhau trước robot.

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId65.gif)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId66.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId67.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId68.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId69.png)

Câu 24 (Nhận biết)

(Những) Phát biểu nào sau đây là đúng khi nói về cảm biến dò đường trên robot Rover?
(Nhiều đáp án)

A/

Cảm biến dò đường của robot Rover có 4 mắt cảm biến.

B/

Cảm biến dò đường sử dụng sóng siêu âm để nhận biết màu trắng, đen.

C/

Mỗi mắt cảm biến dò đường gồm một đầu phát và một đầu thu tín hiệu hồng ngoại.

D/

Mắt cảm biến dò đường sẽ phát ra và thu về hồng ngoại. Tùy theo mức độ hồng ngoại nhận lại mà xác định được bên dưới là vạch đen hay nền trắng.

E/

Phía trên Rover có các đèn báo hiệu tương ứng với từng mắt đọc: đọc được nền đen = đèn sáng, đọc được nền trắng = đèn tắt.

Câu 25 (Thông hiểu)

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId70.gif)

Để lập trình Rover đi trên line mãi mãi như trên, hãy chọn hành động lập trình phù hợp khi cảm biến dò line ở các trường hợp sau?

(Dạng ghép nối)

Đáp án

### Table Data

| Cột trái  | Cột phải  |
|  ![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId71.png) | Chạy thẳng  |
|  ![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId72.png) | Rẽ phải  |
|  ![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId73.png) | Rẽ trái  |
|  ![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId74.png) | Rẽ phải  |
|  ![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId75.png) | Rẽ trái  |
|  ![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId76.png) | Chạy thẳng  |
|   | Chạy lùi  |

Câu 26 (Thông hiểu)

Hãy lựa chọn chương trình phù hợp nhất để điều khiển robot di chuyển mãi mãi bên trong vòng tròn đen đến khi tìm được lối ra.

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId77.png)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId78.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId79.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId80.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId81.png)

Câu 27 (Nhận biết)

Phát biểu nào sau đây là đúng khi nói về cảm biến siêu âm trên robot Rover?
(Nhiều đáp án)

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId82.png)

A/

Cảm biến siêu âm dùng để đo khoảng cách từ cảm biến đến vật cản phía trước.

B/

Mắt PHẢI của cảm biến siêu âm dùng để PHÁT sóng siêu âm. Khi gặp vật cản, sóng siêu âm bị phản xạ lại và mắt TRÁI của cảm biến sẽ THU được tín hiệu.

C/

Mắt TRÁI của cảm biến siêu âm dùng để PHÁT sóng siêu âm. Khi gặp vật cản, sóng siêu âm bị phản xạ lại và mắt PHẢI của cảm biến sẽ THU được tín hiệu.

D/

Cảm biến siêu âm của Rover có thể đo khoảng cách tới vật cản trong phạm vi từ 0 đến 3m.

Câu 28 (Thông hiểu)

Đâu là ứng dụng của cảm biến dò đường trên Rover?
(Nhiều đáp án)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId65.gif)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId83.gif)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId84.png)

https://drive.google.com/file/d/1yQJT-aOCp8VwyT59W6a5Er7q12BqyeO

1/ view?usp=drive_link

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId86.png)

https://drive.google.com/file/d/1lmbcyK3qXMiyOjxF9JwRuyJKWETTMW6p/view?usp=drive_link

Câu 29 (Thông hiểu)

Đoạn lệnh nào sau đây KHÔNG giúp robot thực hiện yêu cầu sau?
Yêu cầu: Robot đi thẳng nếu gặp vật cản (khoảng cách từ robot đến vật cản nhỏ hơn 20cm) thì xoay đi hướng khác, sau đó tiếp tục đi thẳng.

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId83.gif)

Link gif:

https://drive.google.com/file/d/1Yzhle93xDBC5r0eENHJzALc58zDTIKCR/view?usp=drive_link

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId89.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId90.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId91.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId92.png)

Câu 30 (Thông hiểu)

Đặt robot Rover trong một vòng tròn có vạch kẻ đen, cùng các chướng ngại vật như hình sau:

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId93.png)

Hãy lựa chọn chương trình phù hợp để điều khiển robot di chuyển mãi mãi bên trong vòng tròn và báo hiệu tín hiệu khi gặp chướng ngại vật. 
Khi gặp chướng ngại vật, robot dừng di chuyển và phát âm thanh. Đợi đến khi người dùng lấy chướng ngại vật ra ngoài và nhấn nút A, robot mới tiếp tục công việc di chuyển trong vòng tròn và tìm vật cản.

Đoạn lệnh nào còn thiếu trong chương trình sau đây để robot thực hiện yêu cầu trên?

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId94.png)

A/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId95.png)

B/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId96.png)

C/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId97.png)

D/

![Image](../assets/DESIGN_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover_rId98.png)