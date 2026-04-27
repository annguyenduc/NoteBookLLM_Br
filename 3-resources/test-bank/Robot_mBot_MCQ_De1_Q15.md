---
file_id: "ROBOT_mBot_MCQ_De1_Q15"
title: "Câu 15 (Thông hiểu)"
category: "Atomic Question"
prefix: "MCQ"
tags: ['Robot', 'mBot', 'Thông hiểu']
source: "`Đề trắc nghiệm 1 - mBot M2.docx`"
level: "Thông hiểu"
answer: "D/"
status: "draft"
created: "2026-04-22"
---

# [MCQ] Câu 15 (Thông hiểu)

## ❓ Câu hỏi
Đoạn lệnh nào sau đây giúp robot thực hiện yêu cầu sau:
Robot di chuyển liên tục trên sa bàn có vạch kẻ đen
![Image](../assets/ASSET_IOT_AI_Arduino_De2_rId38.png)

## 📝 Đáp án lựa chọn
- **A/**
  ![Image](../assets/ASSET_IOT_AI_Arduino_De2_rId21.gif)
- **B/**
  ![Image](../assets/ASSET_IOT_AI_Arduino_De2_rId39.gif)
- **C/**
  ![Image](../assets/ASSET_IOT_AI_Arduino_De2_rId40.gif)
- **D/ (Đáp án)**
  ![Image](../assets/ASSET_IOT_AI_Arduino_De2_rId41.gif)
  ĐỀ THỰC HÀNH
  Đề kiểm tra thực hành
  Robot mBot (module 2)
  1. Yêu cầu:
  - Đề thực hành gồm: 2 bài tập lập trình
  - Thời gian làm bài: 120 phút
  - Yêu cầu nộp bài tập: Nộp file lập trình .mBlock và hình ảnh/video quay lại quá trình robot hoạt động.
  Đặt tên file theo mẫu: [Chi nhánh]-[Họ và tên giáo viên]-[Tên môn học]-Bai kiem tra thuc hanh-[Số thứ tự bài tập]
  [Tên môn học]: mbot 2
  Ví dụ: Để nộp bài kiểm tra thực hành 1, giáo viên đặt tên file như sau:  HCM-Nguyễn Văn A-mbot 2-Bai kiem tra thuc hanh-1
  2. Vật tư chuẩn bị:
  3. Đề bài:
  Bài 1: Hãy lập trình mBot phát hiện vực thẳm
  - Robot bắt đầu thực hiện chương trình khi nhấn nút trên bo mạch trung tâm mCore
  - Khi bắt đầu, mBot luôn di chuyển thẳng tới.
  - Sử dụng cảm biến dò đường, nếu gặp vực thẳm, mBot chạy lùi và rẽ sang hướng khác
  - Chương trình lặp lại mãi mãi và kết thúc khi nhấn nút trên mạch trung tâm mCore lần thứ 2, khi đó mBot dừng lại không di chuyển nữa
  ![Image](../assets/ASSET_IOT_AI_Arduino_De2_rId63.png)
  Bài 2: Hãy lập trình mBot di chuyển trên line kết hợp tránh vật cản:
  - Chuẩn bị: Một sa bàn trắng đen có hình dạng bất kỳ, một chai nước đặt trên vạch đen để làm vật cản
  - Robot bắt đầu thực hiện chương trình khi nhấn nút trên bo mạch trung tâm mCore.
  - Khi bắt đầu, mBot luôn di chuyển trên vạch kẻ đen của sa bàn.
  - Khi gặp vật cản trên sa bàn, mBot sẽ tự động rẽ sang hướng khác và quay trở lại sa bàn.
  - Chương trình lặp lại mãi mãi và kết thúc khi nhấn nút trên mạch trung tâm mCore lần thứ 2, khi đó mBot dừng lại không di chuyển nữa.
  ![Image](../assets/ASSET_IOT_AI_Arduino_De4_rId47.png)
  4. Đáp án:
  Code lập trình Bài 1,2:
  5. Tiêu chí chấm điểm:
  Bài 1
  ![Image](../assets/ASSET_IOT_AI_Arduino_De3_rId78.png)
  1/ Chương trình có tổng cộng ít nhất 3 câu lệnh điều kiện nằm trong vòng lặp If, Wait until, repeat until, được sắp xếp như sau:
  <1> - Wait until “When on-board button pressed”
  <2> - Repeat until “When on-board button pressed”
  <3> ---- If "Line follower… ALL detects" = black (Có vực thẳm)
  ---- If "Line follower… ALL detects" = white (Trên mặt bàn)
  (0.25x4 = 1đ)
  2/ Sử dụng được câu lệnh “Wait until” + “When on-board button pressed” <1> để lập trình được robot bắt đầu chương trình khi nhấn nút trên board.  (0.5đ)
  ![Image](../assets/ASSET_IOT_AI_Arduino_De3_rId79.png)
  3/ Sử dụng được câu lệnh “Repeat until” + “When on-board button pressed” <2> và “stop moving” để lập trình được robot kết thúc chương trình khi nhấn nút trên board lần 2. (0.5đ)
  ![Image](../assets/ASSET_IOT_AI_Arduino_De3_rId80.png)
  4/ Bên trong vòng lặp “Repeat until”, có sử dụng câu lệnh If hoặc If-else <3> để chia hai trường hợp có/không phát hiện vực thẳm. (0.5đ)
  5/ Sử dụng câu lệnh điều kiện của cảm biến dò đường để chia trường hợp của chương trình
  - Gặp vách đá = Cả hai bên cảm biến KHÔNG nhận tín hiệu = Cả hai bên cảm biến phát hiện “màu đen” (0.25đ)
  ![Image](../assets/ASSET_IOT_AI_Arduino_De3_rId81.png)
  - Trên mặt bàn = Cả hai bên cảm biến CÓ nhận tín hiệu = Cả hai bên cảm biến phát hiện “màu trắng” (0.25đ)
  6/ Các câu lệnh điều kiện “cảm biến dò đường” sử dụng đúng “cổng” của cảm biến trong thực tế. (0.5đ)
  7/ Lập trình đúng hành động được yêu cầu trong mỗi trường hợp có/không phát hiện vực thẳm
  - Trên mặt bàn: Chạy thẳng liên tục (0.25đ)
  - Phát hiện vực thẳm: Đi lùi, xoay hướng khác (0.25đ)
  Bài 2
  ![Image](../assets/ASSET_IOT_AI_Arduino_De3_rId82.png)
  1/ Chương trình có tổng cộng ít nhất 4 câu lệnh điều kiện nằm trong vòng lặp If, Wait until, Repeat until, được sắp xếp 2 cách như sau:
  CÁCH 1
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
  2/ Sử dụng được câu lệnh “Wait until” + “When on-board button pressed” <1> để lập trình được robot bắt đầu chương trình khi nhấn nút trên board. (0.5đ)
  3/ Sử dụng được câu lệnh “Repeat until” + “When on-board button pressed” <2> và “stop moving” để lập trình được robot kết thúc chương trình khi nhấn nút trên board lần 2. (0.5đ)
  4/ Bên trong vòng lặp “Repeat until”, có sử dụng câu lệnh If hoặc If-else <3> để chia các trường hợp ngược nhau của cảm biến siêu âm, cảm biến dò đường theo 2 cách trên. (0.5đ)
  ![Image](../assets/ASSET_IOT_AI_Arduino_De3_rId80.png)
  5/ Sử dụng câu lệnh điều kiện của cảm biến siêu âm và phép so sánh để chia trường hợp CÓ/KHÔNG gặp vật cản <3> của chương trình. Trường hợp “=” có thể được lược bỏ. (0.5đ)
  ![Image](../assets/ASSET_IOT_AI_Arduino_De3_rId83.png)
  6/ Sử dụng câu lệnh điều kiện của cảm biến dò đường để chia 4 trường hợp di chuyển trên line <4> của chương trình.  (0.5đ)
  ![Image](../assets/ASSET_IOT_AI_Arduino_De2_rId64.png)
  ![Image](../assets/ASSET_IOT_AI_Arduino_De2_rId65.png)
  7/ Các câu lệnh điều kiện “cảm biến siêu âm” và “cảm biến dò đường” phải sử dụng khác “cổng” nhau. (0.5đ)
  8/ Lập trình đúng hành động được yêu cầu trong mỗi trường hợp có/không phát hiện vật cản
  - Có vật cản: Chạy vòng qua vật cản (0.25đ)
  - Không có vật cản: Chạy trên line (0.25đ)
  9/ Lập trình đúng hành động được yêu cầu trong mỗi trường hợp di chuyển trên line
  - Cả 2 cảm biến trên vạch đen: Chạy thẳng (0.125đ)
  - Cảm biến phải bị lệch khỏi vạch đen: Xoay trái (0.125đ)
  - Cảm biến trái bị lệch khỏi vạch đen: Xoay phải (0.125đ)
  - Cả 2 cảm biến ngoài vạch đen: tự do (0.125đ)

## 🔗 Liên kết tư duy
- Kiến thức liên quan: `WIKI_Robot`
- Module: `Robot_mBot`

## 📖 Nguồn
`📖 Nguồn: [Đề trắc nghiệm 1 - mBot M2.docx] — 15`
