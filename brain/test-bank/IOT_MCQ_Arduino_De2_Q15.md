---
file_id: "IOT_MCQ_Arduino_De2_Q15"
title: "Câu 15 (Thông hiểu)"
category: "Atomic Question"
prefix: "MCQ"
tags: ['IOT', 'Arduino', 'Thông hiểu']
source: "`Đề trắc nghiệm 2 - Arduino M2.docx`"
level: "Thông hiểu"
answer: "A/"
status: "draft"
created: "2026-04-22"
---

# [MCQ] Câu 15 (Thông hiểu)

## ❓ Câu hỏi
Cho mạch điều khiển động cơ bằng joystick như sau:
![Image](../assets/IMG_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId42.png)
![Image](../assets/IMG_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId43.png)
![Image](../assets/IMG_Arduino_1_2_Arduino_2_Đề_trắc_nghiệm_2_-_Arduino_M2_rId44.png)
Hãy cho biết đoạn code A làm cho động cơ thực hiện hành động nào?

## 📝 Đáp án lựa chọn
- **A/ (Đáp án)**
  Dừng lại
- **B/**
  Đi tới
- **C/**
  Rẽ trái
- **D/**
  Rẽ phải
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
  Chuẩn bị: Arduino (x1), đèn LED đơn (x2), đế pin 4 (x2), breadboard (x1), mạch L298 (x1), động cơ vàng và bánh xe (x2), cảm biến ánh sáng (x1), cảm biến siêu âm (x1), dây điện jumper các loại, bìa carton và các dụng cụ Tinkering khác.
  .
  3. Đề bài:
  Lập trình, gắn mạch điện và chế tạo xe tự né vật cản thỏa các yêu cầu sau:
  Mô hình xe gồm các linh kiện điện tử như sau:
  Sử dụng 2 đế pin 4 (mắc song song) làm nguồn điện cấp nguồn cho Arduino và mạch L298, sao cho nguồn điện được sử dụng hiệu quả nhất.
  Sử dụng mạch L298 và động cơ vàng để làm robot di chuyển tới-lùi, xoay trái-phải.
  Sử dụng cảm biến siêu âm để xe tự động né vật cản.
  Sử dụng 2 đèn LED để làm đèn soi sáng cho xe.
  Sử dụng cảm biến ánh sáng để đo cường độ ánh sáng môi trường xung quanh.
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2_Đề_2_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId16.png)
  (Hình minh họa trên chưa có đế pin, breadboard và các dây kết nối)
  Yêu cầu lập trình:
  1/ Khi khởi động, xe đứng yên, 2 đèn chớp tắt cùng nhau 3 lần.
  2/ Sau đó, xe bắt đầu tự di chuyển thẳng.
  3/ Mỗi khi gặp vật cản, xe di chuyển lùi lại và xoay, di chuyển hướng khác.
  4/ Nếu môi trường xung quanh đang sáng đèn, 2 đèn LED sẽ tắt. Ngược lại, nếu môi trường xung quanh đang tối, 2 đèn LED sẽ tự động bật lên.
  Yêu cầu chế tạo:
  5/ Hãy sử dụng các vật dụng cần thiết để chế tạo mô hình xe thỏa các yêu cầu sau:
  Xe có trục bánh sau chạy bằng động cơ vàng, trục bánh trước xoay được.
  Xe có thân xe có thể chứa các linh kiện điện tử cần thiết.
  Lắp đặt động cơ vàng theo vị trí, chiều phù hợp để xe có thể di chuyển theo hướng mong muốn.
  Lắp đặt cảm biến ánh sáng ở vị trí phù hợp để dễ dàng đo cường độ ánh sáng xung quanh.
  Xe có tính thẩm mỹ: Các linh kiện và breadboard được đặt ở vị trí phù hợp, các dây jumper được kết nối gọn gàng, được cố định chặt chẽ…
  Hình dáng xe có sự sáng tạo (hình dáng, màu sắc, trang trí…).
  8/ Điền các thông tin các chân kết nối của các linh kiện điện tử vào “Bảng chân kết nối các linh kiện điện tử” sau:
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_rId61.png)
  4. Đáp án:
  Mô hình, mạch điện
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2_Đề_2_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId18.png)
  “Bảng chân kết nối các linh kiện điện tử” sau:
  Code lập trình
  5. Tiêu chí chấm điểm:
  Tinkering  (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)
  1/ Xe có đầy đủ các bộ phận sau: bánh xe sau (động cơ vàng), trục bánh xe trước, thân xe. (0,7đ)
  2/ Thân xe có kích thước, hình dáng phù hợp, có thể chứa các LKĐT. (0,7đ)
  3/ Trục bánh xe trước chế tạo bằng các dụng cụ Tinkering và xoay được. (0,7đ)
  4/ Lắp đặt động cơ vàng theo vị trí, chiều phù hợp để xe có thể di chuyển theo hướng mong muốn. (0,7đ)
  5/ Lắp đặt cảm biến ánh sáng ở vị trí phù hợp để dễ dàng đo cường độ ánh sáng xung quanh.  (0,7đ)
  6/ Xe có tính thẩm mỹ: Các linh kiện được đặt ở vị trí phù hợp, các dây jumper được kết nối gọn gàng, được cố định chặt chẽ… (0,7đ)
  7/ Hình dáng xe có sự sáng tạo (hình dáng, màu sắc, trang trí…). (0,7đ)
  Mạch điện  (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)
  Dựa vào mạch điện trên xe điều khiển và “Bảng chân kết nối các linh kiện điện tử” được nộp, xét các tiêu chí sau:
  1/ Ở nguồn điện 4 pin, dây âm (đen) được kết nối đến chân GND bất kỳ của Arduino. (1đ)
  2/ Ở nguồn điện 4 pin, dây dương (đỏ) được kết nối kết nối đến chân VIN của Arduino. (1đ)
  3/ Ở 2 đèn LED RGB, chân âm (ngắn) được gắn vào chân GND bất kỳ. (1đ)
  4/ Ở 2 đèn LED RGB, chân dương (dài) được gắn vào 1 hoặc 2 chân Digital bất kỳ (D__) của Arduino. (1đ)
  5/ Ở cảm biến ánh sáng, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (1đ)
  6/ Ở cảm biến ánh sáng, chân AO (hoặc DO) được gắn vào chân Analog (A__)  (hoặc Digital (D__) ) bất kỳ của Arduino. (1đ)
  7/ Ở cảm biến siêu âm, chân GND được gắn vào chân GND bất kỳ và chân VCC được gắn vào chân 5V của Arduino. (1đ)
  8/ Ở cảm biến siêu âm, chân Trig và Echo được gắn vào 2 chân Digital bất kỳ (D__)  của Arduino. (1đ)
  9/ Ở mỗi động cơ vàng, nối 2 đầu cực của động cơ đến 2 chân OUT1, OUT2 hoặc OUT3, OUT4 của mạch L298. (1đ)
  10/ Ở mạch L298, nối các chân IN 1, 2, 3, 4 đến các chân Digital PWM bất kỳ của Arduino (Chân pin digital có dấu “~”, ví dụ D5~). (1đ)
  Code lập trình  (Mỗi tiêu chí có số điểm riêng; Tổng điểm = 10đ)
  Đáp án mẫu
  Dựa vào code lập trình và “Bảng chân kết nối các linh kiện điện tử” được nộp, xét các tiêu chí sau:
  1/ Khi khởi động, lập trình được 2 đèn chớp tắt cùng nhau 3 lần. (1đ)
  2/ Chương trình có tổng cộng ít nhất 4 câu lệnh If nằm trong vòng lặp forever, được sắp xếp như sau:
  <1> - If  "độ sáng" < … (Sáng LED)
  <2> - If  "độ sáng" > … (Tắt LED)
  <3> - If  "khoảng cách đến vật cản" > … (Xe đi thẳng)
  <4> - If  "khoảng cách đến vật cản" < … (Xe đi lùi và xoay hướng khác)
  (0.25x4 = 1đ)
  3/ Trong phần điều kiện <1,2>, sử dụng được câu lệnh “Read analog pin < …” để xét điều kiện và đo độ sáng môi trường. (1đ)
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2_Đề_2_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId21.png)
  4/ Trong phần điều kiện <3,4>, sử dụng được câu lệnh “Read ultrasonic sensor… < …” để xét điều kiện và đo khoảng cách đến vật cản. (1đ)
  ![Image](../assets/IMG_Arduino_1_2_Arduino_2_Đề_2_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_rId22.png)
  5/ Trong phần điều kiện <1>, lập trình được 2 đèn LED sáng cùng nhau. (1đ)
  6/ Trong phần điều kiện <2>, lập trình được 2 đèn LED tắt cùng nhau. (1đ)
  7/ Trong phần điều kiện <3>, lập trình được 2 động cơ xoay cùng lúc về phía trước để đi thẳng. (1đ)
  8/ Trong phần điều kiện <4>, lập trình được 2 động cơ xoay cùng lúc về phía sau để đi lùi. (1đ)
  9/ Trong phần điều kiện <4>, sau khi đi lùi, lập trình được 1 động cơ đứng yên, 1 động cơ còn lại xoay để xe xoay hướng khác. (1đ)
  10/ Trong phần điều kiện <4>, có sử dụng câu lệnh “Chờ” ở sau hai hành động đi lùi và xoay hướng khác. (1đ)

## 🔗 Liên kết tư duy
- Kiến thức liên quan: `WIKI_IOT`
- Module: `IOT_Arduino`

## 📖 Nguồn
`📖 Nguồn: [Đề trắc nghiệm 2 - Arduino M2.docx] — 15`
