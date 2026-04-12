# TEST BANK: Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino.md

### Question: Khẳng định nào dưới đây là SAI?
A. Có thể cấp nguồn cho arduino thông qua pin với chân 3,3V hoặc 5V.
B. Có thể cấp nguồn cho arduino bằng cách kết nối với máy tính thông qua dây cáp.
C. Có thể cấp nguồn cho arduino thông qua dây adapter 9V.
D. Có thể cấp nguồn cho arduino thông qua pin với cổng Vin.
**Correct:** A
**Explanation:** Chân 3.3V và 5V là chân nguồn ra (output) để nuôi linh kiện, không phải chân cấp nguồn vào (input) cho mạch Arduino.

### Question: Nối tên với các bộ phận tương ứng trên mạch Arduino Uno:
A. Nút reset
B. Cổng USB - type B
C. Jack DC
D. Các chân nguồn
E. Các chân pin (chân tín hiệu)
**Correct:** (Câu hỏi dạng nối, đáp án dựa trên sơ đồ chuẩn của Arduino Uno)
**Explanation:** A-Nút nhấn màu đỏ/vàng; B-Cổng vuông kết nối máy tính; C-Cổng tròn cấp nguồn; D-Dãy chân Power (5V, GND, Vin); E-Dãy chân Digital/Analog.

### Question: Phát biểu nào sau đây là đúng khi nói về chế độ Live và chế độ Upload khi lập trình Arduino trên mBlock5?
A. Chế độ Live chỉ hoạt động trong quá trình mở mBlock5 và kết nối với board Arduino.
B. Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta ngắt kết nối giữa hai thiết bị, chương trình được tải lên sẽ bị xóa khỏi bộ nhớ của Arduino.
C. Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta xóa câu lệnh ở khu vực lập trình, chương trình hoạt động của Arduino sẽ bị thay đổi ngay lập tức.
D. Với chế độ Live, ta có thể thấy trực tiếp chương trình đang chạy đến khối lệnh nào khi chọn “Setting - Update firmware - OK”.
**Correct:** A
**Explanation:** Chế độ Live yêu cầu kết nối thời gian thực. Chế độ Upload lưu chương trình vĩnh viễn vào chip cho đến khi có chương trình mới đè lên.

### Question: Ta có thể phân biệt được chân dương, chân âm của đèn LED siêu sáng bằng cách nào?
A. Phần chân âm của đèn led có dấu (-); chân dương của đèn led có dấu (+).
B. Phần chân âm của đèn led dài hơn; chân dương của đèn led ngắn hơn.
C. Phần chân dương của đèn led được đánh dấu bằng một lỗ tròn nhỏ, chân âm không có.
D. Phần chân dương của đèn led dài hơn; chân âm của đèn led ngắn hơn.
**Correct:** D
**Explanation:** Theo quy ước linh kiện điện tử, chân dài của LED là cực dương (Anode), chân ngắn là cực âm (Cathode).

### Question: Khối lệnh nào sau đây được sử dụng để điều khiển việc hoạt động/tắt của động cơ rung 0834 3-5V?
![image29.png](assets\Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino.docx_image29.png)
A. Khối lệnh thiết lập chân Digital đầu ra (High/Low).
B. Khối lệnh đọc chân Analog.
C. Khối lệnh Servo.
D. Khối lệnh hiển thị màn hình.
**Correct:** A
**Explanation:** Động cơ rung hoạt động như một thiết bị On/Off đơn giản, sử dụng lệnh xuất mức logic High/Low tại chân Digital.

### Question: Phát biểu nào sau đây là SAI khi nói về các chân kết nối của mạch thu phát âm thanh ISD1820?
A. PLAYE, PLAYL của mạch chỉ có thể được bật bằng cách nhấn nút thủ công.
B. Chân PLAYE, PLAYL của mạch chỉ có thể được gắn ở một số chân Digital không có dấu ngã (~): 2, 4, 7, 8, 12, 13.
C. Chân VCC của mạch được gắn với cổng 5V của Arduino.
D. Chân REC của mạch được gắn với cổng Digital 2-13 của Arduino.
**Correct:** A
**Explanation:** Các chân PLAYE, PLAYL có thể được điều khiển bằng xung điện từ các chân Digital của Arduino