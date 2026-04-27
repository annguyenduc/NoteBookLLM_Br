---
file_id: "IOT_MCQ_Arduino_De1_Q15"
title: "Câu 15 (Thông hiểu)"
category: "Atomic Question"
prefix: "MCQ"
tags: ['IOT', 'Arduino', 'Thông hiểu']
source: "`(CŨ chưa sửa Extension KDI) Đề trắc nghiệm 1 - Arduino M2.docx`"
level: "Thông hiểu"
answer: "D/"
status: "draft"
created: "2026-04-22"
---

# [MCQ] Câu 15 (Thông hiểu)

## ❓ Câu hỏi
(ĐỀ GẦN GIỐNG CÂU 14)
Một học sinh chế tạo một chiếc xe hoạt động bằng Arduino, mạch L298, động cơ vàng và điều khiển bằng remote hồng ngoại như mạch điện như hình dưới.
![Image](../assets/IMG_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId89.png)
Biết rằng sau khi học sinh test bằng đoạn lệnh sau và nhấn phím 2  trên remote hồng ngoại, xe đã xoay tròn ngược chiều kim đồng hồ .
![Image](../assets/IMG_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId90.png)
![Image](../assets/IMG_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId84.png)
Hỏi cũng với chương trình trên, để xe dừng di chuyển , ta cần nhấn phím nào trên remote hồng ngoại?

## 📝 Đáp án lựa chọn
- **A/**
  Phím 6
- **B/**
  Phím 8
- **C/**
  Phím 4
- **D/ (Đáp án)**
  Phím 5
  ĐỀ THỰC HÀNH
  Đề kiểm tra thực hành
  Arduino (module 2)
  1. Yêu cầu:
  - Đề thực hành gồm: 1 bài tập lập trình và 1 bài tập chế tạo
  - Thời gian làm bài: 120 phút
  - Yêu cầu nộp bài tập:
  + Nộp lại file code lập trình
  + Tạo và điền vào “Bảng chân kết nối các linh kiện điện tử” (*), nộp lại file doc hoặc hình ảnh bảng.
  + Chế tạo robot bằng vật dụng Tinkering kết hợp Arduino và các linh kiện cần thiết
  + Nộp lại video, hình ảnh quay lại quá trình robot hoạt động
  Đặt tên file theo mẫu: [Chi nhánh]-[Họ và tên giáo viên]-[Tên môn học]-[Tên bài tập]
  [Tên môn học]: Arduino 2
  Ví dụ: Để nộp bài kiểm tra thực hành 1, giáo viên đặt tên file như sau:  HCM-Nguyễn Văn A-Arduino 2-Bai kiem tra thuc hanh
  2. Vật tư chuẩn bị:
  Chuẩn bị: Arduino (x1), LED RGB (x3 màu), đế pin 4 (x2), breadboard (x1), mạch L298 (x1), động cơ vàng (x2), màn hình I2C LCD 16x2 (x1), cảm biến nhiệt độ, độ ẩm DHT11 (x1), mắt thu hồng ngoại IR1838 (x1), remote hồng ngoại (x1), Bình xịt nước phun sương (x1).
  .
  3. Đề bài:
  Lập trình, gắn mạch điện và chế tạo xe điều khiển từ xa và thu thập dữ liệu nhiệt độ, độ ẩm thỏa các yêu cầu sau:
  1/ Sử dụng đế 2 pin 4 (mắc song song) làm nguồn điện cấp nguồn cho Arduino và mạch L298, sao cho nguồn điện được sử dụng hiệu quả nhất.
  2/ Sử dụng mạch L298 và động cơ vàng để làm robot di chuyển tới-lùi và có thể xoay trái-phải
  3/ Robot được điều khiển bằng mắt thu và remote hồng ngoại:
  + Phím 2: Robot đi tới
  + Phím 4: Robot xoay trái
  + Phím 5: Robot dừng di chuyển
  + Phím 6: Robot xoay phải
  + Phím 8: Robot đi lùi
  4/ Sử dụng cảm biến DHT11 để đo nhiệt độ, độ ẩm và gửi thông tin đến màn hình LCD.
  + Ở dòng 1 của màn hình LCD luôn hiển thị “N.do:  _____  do C”, với “_____” là nhiệt độ hiện tại đo được qua cảm biến DHT11.
  + Ở dòng 2 của màn hình LCD luôn hiển thị “Do am:  _____ %”, với “_____” là nhiệt độ hiện tại đo được qua cảm biến DHT11.
  5/ Sử dụng đèn 3 LED để thể hiện tình trạng của xe điều khiển:
  (Lưu ý: Các màu đèn sau đây có thể tự do thay đổi tùy tình trạng vật tư hiện tại, có thể thay đổi màu khác nhưng vẫn giữ nguyên mục đích của đề bài)
  + Khi khởi động và di chuyển, đèn LED (1) luôn sáng màu xanh lá, thể hiện chương trình đã khởi động thành công.
  + Khi xe di chuyển trong điều kiện nhiệt độ, độ ẩm bình thường (độ ẩm trong khoảng 40-70%, nhiệt độ trong khoảng 25-35 độ C), 2 đèn còn lại đều tắt.
  + Khi xe gặp điều kiện nhiệt độ ngoài khoảng bình thường, một đèn LED (2) màu đỏ sáng lên. Khi xe gặp điều kiện độ ẩm ngoài khoảng bình thường, một đèn LED (3) màu xanh dương sáng lên.
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
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_rId61.png)
  4. Đáp án:
  Mô hình, mạch điện (Chưa có đế pin 4, breadboard)
  ![Image](../assets/IMG_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId89.png)
  Code lập trình
  5. Tiêu chí chấm điểm:
  Tinkering  (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)
  1/ Xe có đầy đủ các bộ phận sau: bánh xe sau (động cơ vàng), trục bánh xe trước, thân xe, thiết bị bảo vệ các LKĐT (linh kiện điện tử). (1đ)
  2/ Thân xe có kích thước, hình dáng phù hợp, có thể chứa các LKĐT. (1đ)
  3/ Trục bánh xe trước chế tạo bằng các dụng cụ Tinkering và xoay được. (1đ)
  4/ Lắp đặt động cơ vàng theo vị trí, chiều phù hợp để xe có thể di chuyển theo hướng mong muốn. (1đ)
  5/ Lắp đặt mắt thu hồng ngoại ở vị trí phù hợp để dễ dàng nhận tín hiệu từ remote hồng ngoại. (1đ)
  6/ Lắp đặt cảm biến độ ẩm DHT11 ở vị trí phù hợp để dễ dàng lấy dữ liệu không khí xung quanh.  (1đ)
  7/ Lắp đặt màn hình LCD và đèn LED ở vị trí phù hợp để dễ dàng xem thông tin và cảnh báo. (1đ)
  8/ Xe có thiết kế mái che hoặc bộ phận bất kỳ bảo vệ mạch điện, tất cả linh kiện khi phun sương. (1đ)
  9/ Xe có tính thẩm mỹ: Các linh kiện được đặt ở vị trí phù hợp, các dây jumper được kết nối gọn gàng, được cố định chặt chẽ… (1đ)
  10/ Hình dáng xe có sự sáng tạo (hình dáng, màu sắc, trang trí…). (1đ)
  Mạch điện  (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)
  Dựa vào mạch điện trên xe điều khiển và “Bảng chân kết nối các linh kiện điện tử” được nộp, xét các tiêu chí sau:
  1/ Có sử dụng Breadboard để tạo các chân cắm bổ sung cho mạch điện. (0.5đ)
  2/ Ở nguồn điện 4 pin, dây âm (đen) được kết nối đến chân GND của L298 và chân GND bất kỳ của Arduino. (0.5đ)
  3/ Ở nguồn điện 4 pin, dây dương (đỏ) được kết nối SONG SONG đến chân 12V+ của L298 và chân VIN của Arduino. (1đ)
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_rId63.png)
  4/ Ở 3 đèn LED RGB, chân âm (ngắn) được gắn vào chân GND bất kỳ. (0.5đ)
  5/ Ở 3 đèn LED RGB, chân dương (dài) được gắn vào 3 chân Digital bất kỳ (D__) của Arduino. (0.5đ)
  6/ Ở màn hình LCD, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (0.5đ)
  7/ Ở màn hình LCD, chân SDA được gắn chính xác vào chân analog A4 của Arduino. (1đ)
  8/ Ở màn hình LCD, chân SCL được gắn chính xác vào chân analog A5 của Arduino. (1đ)
  9/ Ở mắt thu hồng ngoại, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (0.5đ)
  10/ Ở mắt thu hồng ngoại, chân SIG được gắn vào chân Digital bất kỳ (D__)  của Arduino. (1đ)
  11/ Ở cảm biến nhiệt độ, độ ẩm, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (0.5đ)
  12/ Ở cảm biến nhiệt độ, độ ẩm, chân OUT / DATA được gắn vào chân Digital bất kỳ (D__)  của Arduino. (1đ)
  13/ Ở mỗi động cơ vàng, nối 2 đầu cực của động cơ đến 2 chân OUT1, OUT2 hoặc OUT3, OUT4 của mạch L298. (0.5đ)
  14/ Ở mạch L298, nối các chân IN 1, 2, 3, 4 đến các chân Digital PWM bất kỳ của Arduino (Chân pin digital có dấu “~”, ví dụ D5~). (1đ)
  Code lập trình  (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)
  Đáp án mẫu
  Dựa vào code lập trình và “Bảng chân kết nối các linh kiện điện tử” được nộp, xét các tiêu chí sau:
  1/ Khi khởi động, lập trình được 1 đèn LED (1) sáng, thể hiện chương trình đã khởi động thành công. (0.5đ)
  2/ Khi khởi động, có sử dụng câu lệnh “Set address LCD” để kết nối LCD với Arduino. (0.5đ)
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_rId65.png)
  3/ Khi khởi động, có sử dụng câu lệnh “IR ReceiveNo.1: Set digital pin” để kết nối mắt thu hồng ngoại với Arduino. (0.5đ)
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_rId66.png)
  4/ Ở MỌI câu lệnh mắt thu hồng ngoại, số chân digital pin phải khớp với thông tin được nhập ở “Bảng chân kết nối các linh kiện điện tử” (0.5đ)
  5/ Khi khởi động, có sử dụng câu lệnh “Temper&humidity 1: Set digital pin” để kết nối mắt thu hồng ngoại với Arduino. (0.5đ)
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_rId67.png)
  6/ Ở MỌI câu lệnh cảm biến nhiệt độ, độ ẩm, số chân digital pin phải khớp với thông tin được nhập ở “Bảng chân kết nối các linh kiện điện tử”. (0.5đ)
  7/ Khi khởi động, trong vòng lặp forever lập trình được màn hình LCD luôn hiển thị “N.do:  _____  do C”, với “_____” là nhiệt độ hiện tại đo được qua cảm biến DHT11 ở dòng 1. (0.5đ)
  8/ Khi khởi động, trong vòng lặp forever lập trình được màn hình LCD luôn hiển thị “Do am:  _____ %”, với “_____” là độ ẩm hiện tại đo được qua cảm biến DHT11 ở dòng 2. (0.5đ)
  9/ Chương trình có tổng cộng ít nhất 8 câu lệnh If nằm trong vòng lặp forever, được sắp xếp như sau:
  <1> - If  "humidity (độ ẩm)" > 40 hoặc "humidity (độ ẩm)" < 70 (Tắt LED)
  - If  "humidity (độ ẩm)" < 40 hoặc "humidity (độ ẩm)" < 40 (Sáng LED)
  <2> - If  "temperature (nhiệt độ)" > 40 hoặc "humidity (độ ẩm)" < 70 (Tắt LED)
  - If  "humidity (độ ẩm)" < 40 hoặc "humidity (độ ẩm)" < 40 (Sáng LED)
  <3> - If "Data IR was receive?"
  <4> ---- If "IR read data" = 2 (Di chuyển)
  <5> ---- If "IR read data" = 4 (Di chuyển)
  <6> ---- If "IR read data" = 6 (Di chuyển)
  <7> ---- If "IR read data" = 8 (Di chuyển)
  <8> ---- If "IR read data" = 5 (Di chuyển)
  (0.25x8 = 2đ)
  10/ Trong phần điều kiện <1>, lập trình được một đèn LED (2) TẮT khi độ ẩm trong khoảng 40-70% và SÁNG khi không trong khoảng đó. (0.5đ)
  11/ Trong phần điều kiện <2>, lập trình được một đèn LED (3) TẮT khi nhiệt độ trong khoảng 25-35 độ C và SÁNG khi không trong khoảng đó. (0.5đ)
  12/ Trong phần điều kiện <3>, có sử dụng câu lệnh “IR ReceiveNo.1: Restart” để reset tín hiệu mỗi lần nhấn nút từ remote hồng ngoại. (0.5đ)
  13/ Trong phần điều kiện <4-8>, các câu lệnh điều khiển động cơ có chân digital PIN PWM khớp với thông tin được nhập ở “Bảng chân kết nối các linh kiện điện tử”. (0.5đ)
  14/ So sánh với mô hình thực tế và lựa chọn các công suất phù hợp, lập trình được mô hình di chuyển tới / lùi / xoay trái / xoay phải / dừng lại (0.2x5 = 1đ)
  15/ So sánh với mô hình thực tế, mô hình di chuyển đúng với các nút nhấn từ remote hồng ngoại được yêu cầu.
  + Phím 2: Robot đi tới
  + Phím 4: Robot xoay trái
  + Phím 5: Robot dừng di chuyển
  + Phím 6: Robot xoay phải
  + Phím 8: Robot đi lùi
  (0.2x5 = 1đ)

## 🔗 Liên kết tư duy
- Kiến thức liên quan: `WIKI_IOT`
- Module: `IOT_Arduino`

## 📖 Nguồn
`📖 Nguồn: [(CŨ chưa sửa Extension KDI) Đề trắc nghiệm 1 - Arduino M2.docx] — 15`
