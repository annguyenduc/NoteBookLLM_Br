# TEST BANK: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_2_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.md

### Question: Trong sơ đồ mạch điện xe tự hành, khi sử dụng nguồn điện từ đế pin để cấp cho Arduino, dây dương (màu đỏ) của đế pin nên được nối vào chân nào?
A. Chân 5V
B. Chân 3.3V
C. Chân VIN
D. Chân Analog A0
**Correct: C**
**Explanation:** Theo tiêu chí chấm điểm mạch điện, dây dương của nguồn pin phải được kết nối đến chân VIN của Arduino để sử dụng bộ ổn áp tích hợp trên board.

### Question: Để điều khiển động cơ vàng thông qua mạch cầu H L298, các chân IN 1, 2, 3, 4 của mạch L298 nên được ưu tiên kết nối với loại chân nào trên Arduino?
A. Các chân Analog (A0 - A5)
B. Các chân Digital có ký hiệu dấu "~" (PWM)
C. Các chân GND
D. Các chân truyền nhận dữ liệu TX/RX
**Correct: B**
**Explanation:** Các chân Digital PWM (có dấu ~) cho phép điều khiển độ rộng xung, từ đó có thể điều chỉnh được tốc độ của động cơ thay vì chỉ bật/tắt đơn thuần.

### Question: Quan sát hình ảnh minh họa mô hình xe dưới đây:
![image4.jpg](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_2_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.docx_image4.jpg)
**Theo yêu cầu của đề bài, khi cảm biến siêu âm phát hiện vật cản ở khoảng cách gần, xe cần thực hiện chuỗi hành động nào?**
A. Dừng lại và bật đèn LED.
B. Tiếp tục đi thẳng và tăng tốc.
C. Di chuyển lùi lại, xoay hướng khác và sau đó tiếp tục di chuyển.
D. Xoay tròn tại chỗ liên tục.
**Correct: C**
**Explanation:** Theo yêu cầu lập trình số 3 và 4, khi gặp vật cản xe phải lùi lại, xoay hướng khác (sử dụng 1 động cơ đứng yên, 1 động cơ xoay) trước khi tiếp tục hành trình.

### Question: Để lập trình tính năng "Đèn tự động bật khi trời tối", bạn cần sử dụng câu lệnh nào để đọc giá trị từ cảm biến ánh sáng?
A. Read digital pin
B. Read ultrasonic sensor
C. Read analog pin
D. Write digital pin
**Correct: C**
**Explanation:** Cảm biến ánh sáng thường trả về giá trị cường độ ánh sáng dưới dạng tín hiệu tương tự, do đó cần sử dụng câu lệnh "Read analog pin" để xét điều kiện sáng/tối.

### Question: Theo yêu cầu khởi động của đề bài, trạng thái của xe và đèn LED như thế nào là đúng?
A. Xe chạy thẳng ngay lập tức, đèn LED tắt.
B. Xe đứng yên, 2 đèn LED chớp tắt cùng nhau 3 lần.
C. Xe lùi lại, 2 đèn LED sáng liên tục.
D. Xe đứng yên, 2 đèn LED sáng luân phiên.
**Correct: B**
**Explanation:** Yêu cầu lập trình số 1 quy định: Khi khởi động, xe đứng yên và 2 đèn chớp tắt cùng nhau 3 lần trước khi bắt đầu di chuyển.

---
**@scout** đã hoàn thành nhiệm vụ. Các liên kết hình ảnh đã được giữ nguyên theo cấu trúc thư mục assets.