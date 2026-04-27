---
title: Tiêu chí và thang điểm - mBot M2.docx
source: [[Tiêu chí và thang điểm - mBot M2.docx]]
type: RAW_SOURCE
---

ĐỀ KIỂM TRA TRẮC NGHIỆM - Lập trình robot mbot Module 2
(Đề

1) Đề kiểm tra thực hành

Robot mBot (module

2) Yêu cầu:

1. - Đề thực hành gồm: 2 bài tập lập trình

- Thời gian làm bài: 120 phút

- Yêu cầu nộp bài tập: Nộp file lập trình .mBlock và hình ảnh/video quay lại quá trình robot hoạt động.

Đặt tên file theo mẫu: [Chi nhánh]-[Họ và tên giáo viên]-[Tên môn học]-Bai kiem tra thuc hanh-[Số thứ tự bài tập]

[Tên môn học]: mbot 2

Ví dụ: Để nộp bài kiểm tra thực hành 1, giáo viên đặt tên file như sau:  HCM-Nguyễn Văn

A- mbot

2- Bai kiem tra thuc hanh-1

2. Vật tư chuẩn bị:

Vật tư chuẩn bị

Số lượng

Ghi chú

Robot mBot, dây kết nối

1

Sa bàn

1

Sa bàn có hình dạng là một vòng tròn kín, liên tục, được tạo nên từ băng keo đen và dán trên mặt sàn để robot di chuyển.

Chướng ngại vật

1

Có thể thay thể bằng vật bất kỳ. VD: Chai nước, hộp bút,...

3. Đề bài:

Bài 1: Hãy lập trình mBot phát hiện vực thẳm
- Robot bắt đầu thực hiện chương trình khi nhấn nút trên bo mạch trung tâm mCore

- Khi bắt đầu, mBot luôn di chuyển thẳng tới.
- Sử dụng cảm biến dò đường, nếu gặp vực thẳm, mBot chạy lùi và rẽ sang hướng khác

- Chương trình lặp lại mãi mãi và kết thúc khi nhấn nút trên mạch trung tâm mCore lần thứ 2, khi đó mBot dừng lại không di chuyển nữa

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId6.gif)

Bài 2: Hãy lập trình mBot di chuyển trên line kết hợp tránh vật cản:

- Chuẩn bị: Một sa bàn trắng đen có hình dạng bất kỳ, một chai nước đặt trên vạch đen để làm vật cản

- Robot bắt đầu thực hiện chương trình khi nhấn nút trên bo mạch trung tâm mCore.

- Khi bắt đầu, mBot luôn di chuyển trên vạch kẻ đen của sa bàn.

- Khi gặp vật cản trên sa bàn, mBot sẽ tự động rẽ sang hướng khác và quay trở lại sa bàn.

- Chương trình lặp lại mãi mãi và kết thúc khi nhấn nút trên mạch trung tâm mCore lần thứ 2, khi đó mBot dừng lại không di chuyển nữa.

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId7.gif)

4. Đáp án:

Code lập trình Bài 1,2:

https://planet.mblock.cc/project/2826361

5. Tiêu chí chấm điểm:

### Table Data

| Điểm thực hành = Điểm Bài 1 + Điểm Bài 2 Mỗi bài có tiêu chí và số điểm riêng cho từng tiêu chí. Tổng điểm tiêu chí ở cả hai bài bằng 10 điểm.  | Điểm thực hành = Điểm Bài 1 + Điểm Bài 2 Mỗi bài có tiêu chí và số điểm riêng cho từng tiêu chí. Tổng điểm tiêu chí ở cả hai bài bằng 10 điểm.  | Điểm thực hành = Điểm Bài 1 + Điểm Bài 2 Mỗi bài có tiêu chí và số điểm riêng cho từng tiêu chí. Tổng điểm tiêu chí ở cả hai bài bằng 10 điểm.  | Điểm thực hành = Điểm Bài 1 + Điểm Bài 2 Mỗi bài có tiêu chí và số điểm riêng cho từng tiêu chí. Tổng điểm tiêu chí ở cả hai bài bằng 10 điểm.  | Điểm thực hành = Điểm Bài 1 + Điểm Bài 2 Mỗi bài có tiêu chí và số điểm riêng cho từng tiêu chí. Tổng điểm tiêu chí ở cả hai bài bằng 10 điểm.  | Điểm thực hành = Điểm Bài 1 + Điểm Bài 2 Mỗi bài có tiêu chí và số điểm riêng cho từng tiêu chí. Tổng điểm tiêu chí ở cả hai bài bằng 10 điểm.  |
| Tên học viên  | Nộp file  | Nộp file  | Điểm  | Điểm  | Điểm  |
| Tên học viên  | Bài 1  | Bài 2  | Bài 1  | Bài 2  | Điểm thực hành  |
|   |   |   |   |   |   |
|   |   |   |   |   |   |

Bài 1

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId9.png)

1/ <1> - Wait until “When on-board button pressed”

Chương trình có tổng cộng ít nhất 3 câu lệnh điều kiện nằm trong vòng lặp If, Wait until, repeat until, được sắp xếp như sau:

<2> - Repeat until “When on-board button pressed”

<3> ---- If "Line follower… ALL detects" = black (Có vực thẳm)

---- If "Line follower… ALL detects" = white (Trên mặt bàn)
(0.25x4 = 1đ)

2/

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId10.png)

Sử dụng được câu lệnh “Wait until” + “When on-board button pressed” <1> để lập trình được robot bắt đầu chương trình khi nhấn nút trên board.  (0.5đ)

3/ (0.5đ)

Sử dụng được câu lệnh “Repeat until” + “When on-board button pressed” <2> và “stop moving” để lập trình được robot kết thúc chương trình khi nhấn nút trên board lần

2.

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId11.png)

4/ - Gặp vách đá = Cả hai bên cảm biến KHÔNG nhận tín hiệu = Cả hai bên cảm biến phát hiện “màu đen” (0.25đ)

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId12.png)

Bên trong vòng lặp “Repeat until”, có sử dụng câu lệnh If hoặc If-else <3> để chia hai trường hợp có/không phát hiện vực thẳm. (0.5đ)

5/ Sử dụng câu lệnh điều kiện của cảm biến dò đường để chia trường hợp của chương trình

- Trên mặt bàn = Cả hai bên cảm biến CÓ nhận tín hiệu = Cả hai bên cảm biến phát hiện “màu trắng” (0.25đ)

6/ Các câu lệnh điều kiện “cảm biến dò đường” sử dụng đúng “cổng” của cảm biến trong thực tế. (0.5đ)

7/ Lập trình đúng hành động được yêu cầu trong mỗi trường hợp có/không phát hiện vực thẳm

- Trên mặt bàn: Chạy thẳng liên tục (0.25đ)
- Phát hiện vực thẳm: Đi lùi, xoay hướng khác (0.25đ)

Bài 2

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId13.png)

1/ CÁCH 1

Chương trình có tổng cộng ít nhất 4 câu lệnh điều kiện nằm trong vòng lặp If, Wait until, Repeat until, được sắp xếp 2 cách như sau:

<1> - Wait until “When on-board button pressed”

<2> - Repeat until “When on-board button pressed”
 <3> ---- If "Ultrasonic sensor" < … (Có vật cản)

---- If "Ultrasonic sensor" >= …  (Ngược lại, không có vật cản)
 <4> -------- If "Line follower value" = 0 (hoặc LEFT = black, RIGHT = black)

-------- If "Line follower value" = 1 (hoặc LEFT = black, RIGHT = white)

-------- If "Line follower value" = 2 (hoặc LEFT = white, RIGHT = black)
        -------- If "Line follower value" = 3 (hoặc LEFT = white, RIGHT = white)

CÁCH 2

<1> - Wait until “When on-board button pressed”

<2> - Repeat until “When on-board button pressed”
 <3> ---- If "Ultrasonic sensor" < … (Có vật cản)

---- If "Ultrasonic sensor" >= …  (Ngược lại, không có vật cản)
 <4> ---- If "Line follower value" = 0 (hoặc LEFT = black, RIGHT = black)

---- If "Line follower value" = 1 (hoặc LEFT = black, RIGHT = white)

---- If "Line follower value" = 2 (hoặc LEFT = white, RIGHT = black)
        ---- If "Line follower value" = 3 (hoặc LEFT = white, RIGHT = white)
(0.25x8 = 2đ)

2/ (0.5đ)

Sử dụng được câu lệnh “Wait until” + “When on-board button pressed” <1> để lập trình được robot bắt đầu chương trình khi nhấn nút trên board. (0.5đ)

3/

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId11.png)

Sử dụng được câu lệnh “Repeat until” + “When on-board button pressed” <2> và “stop moving” để lập trình được robot kết thúc chương trình khi nhấn nút trên board lần

2.

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId14.png)

4/

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId15.png)

Bên trong vòng lặp “Repeat until”, có sử dụng câu lệnh If hoặc If-else <3> để chia các trường hợp ngược nhau của cảm biến siêu âm, cảm biến dò đường theo 2 cách trên. (0.5đ)

5/ Sử dụng câu lệnh điều kiện của cảm biến siêu âm và phép so sánh để chia trường hợp CÓ/KHÔNG gặp vật cản <3> của chương trình. Trường hợp “=” có thể được lược bỏ. (0.5đ)

6/ Sử dụng câu lệnh điều kiện của cảm biến dò đường để chia 4 trường hợp di chuyển trên line <4> của chương trình.  (0.5đ)

![Image](../assets/DESIGN_RAW_Robotics_mBot_1_2_mBot_2_Tiêu_chí_và_thang_điểm_-_mBot_M2_rId16.png)

7/ Các câu lệnh điều kiện “cảm biến siêu âm” và “cảm biến dò đường” phải sử dụng khác “cổng” nhau. (0.5đ)

8/ Lập trình đúng hành động được yêu cầu trong mỗi trường hợp có/không phát hiện vật cản

- Có vật cản: Chạy vòng qua vật cản (0.25đ)
- Không có vật cản: Chạy trên line (0.25đ)

9/ Lập trình đúng hành động được yêu cầu trong mỗi trường hợp di chuyển trên line

- Cả 2 cảm biến trên vạch đen: Chạy thẳng (0.125đ)
- Cảm biến phải bị lệch khỏi vạch đen: Xoay trái (0.125đ)
- Cảm biến trái bị lệch khỏi vạch đen: Xoay phải (0.125đ)
- Cả 2 cảm biến ngoài vạch đen: tự do (0.125đ)