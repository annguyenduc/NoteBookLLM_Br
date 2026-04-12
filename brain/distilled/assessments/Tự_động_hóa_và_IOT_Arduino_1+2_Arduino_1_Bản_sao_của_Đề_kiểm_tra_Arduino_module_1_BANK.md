# TEST BANK: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.md

### Question: Những cách cấp nguồn cho Arduino Uno R3?
A. Cấp nguồn từ cổng USB.
B. Cấp nguồn thông qua Adapter.
C. Cấp nguồn từ pin thông qua chân V(in).
D. Cấp nguồn từ pin thông qua chân Digital.
E. Cấp nguồn từ pin thông qua chân Analog.
F. Cấp nguồn không dây qua tín hiệu bluetooth.
Correct: A, B, C
Explanation: Arduino hỗ trợ cấp nguồn qua USB (5V), Jack DC (7-12V) và chân Vin. Các chân Digital/Analog không dùng để cấp nguồn đầu vào cho board.

### Question: Vì sao nên hạn chế sử dụng chân digital số 0 (RX) và 1 (TX)?
A. Hai chân 0 và 1 là hai chân giao tiếp dùng cho Arduino truyền và nhận dữ liệu nên rất dễ bị nhiễu nếu ta dùng hai chân này như các chân digital thông thường.
B. Trên phần chân digital có tổng cộng 14 chân nên không cần phải sử dụng đến hai chân 0 và 1.
C. Hai chân 0 và 1 dùng để reset chương trình cho Arduino nên không sử dụng hai chân này.
D. Hai chân 0 và 1 chỉ dùng cho cảm biến mưa nên phải hạn chế dùng cho các loại cảm biến khác.
Correct: A
Explanation: Chân 0 (RX) và 1 (TX) phục vụ nạp chương trình và giao tiếp Serial với máy tính.

### Question: Trên Arduino, nên sử dụng nguồn chân nào để cấp nguồn cho cảm biến?
A. Chân GND của Arduino để nối với cực âm của cảm biến; chân 3,3V hoặc 5V của Arduino để nối với cực dương của cảm biến.
B. Chân GND của Arduino để nối với cực âm của cảm biến; chân analog từ A0 đến A6 của Arduino để nối với cực dương của cảm biến.
C. Chân GND của Arduino để nối với cực âm của cảm biến; chân digital từ 2 đến 13 của Arduino để nối với cực dương của cảm biến.
D. Chọn GND của Arduino để nối với cực âm của cảm biến; chân Vin của Arduino để nối với cực dương của cảm biến.
Correct: A
Explanation: Cảm biến cần nguồn ổn định 3.3V hoặc 5V và chân mass (GND).

### Question: Sắp xếp các bước theo trình tự thích hợp để kết nối Arduino với phần mềm mblock?
1. Chuyển chế độ “Live” sang “Upload”.
2. Lựa chọn thiết bị cần sử dụng là arduino ở dấu “+” khu vực thiết bị.
3. Mở phần mềm mBlock, dùng dây USB kết nối Arduino với máy tính.
4. Chọn “Connect”, cửa sổ hiện lên chọn cổng kết nối và chọn “connect”.
A. 3-2-1-4.
B. 1-2-3-4.
C. 1-2-4-3.
D. 4-2-3-1.
Correct: A
Explanation: Quy trình chuẩn: Kết nối phần cứng -> Chọn thiết bị trên app -> Chuyển chế độ lập trình -> Kết nối cổng COM.

### Question: Một chiếc đèn Led bị gãy chân nên không thể phân biệt các chân của đèn Led bằng chiều dài được. Nếu quan sát bằng cách nhìn bên trong đèn thì phải phân biệt như thế nào?
A. Phần (bản) cực bên trong nhỏ hơn là chân dương, phần (bản) cực to hơn là chân âm.
B. Phần (bản) cực bên trong nhỏ hơn là chân âm, phần (bản) cực to hơn là chân dương.
C. Không thể xác định được chân dương hay chân âm nếu đèn Led bị gãy chân.
D. Cả 3 đáp án đều sai.
Correct: A
Explanation: Cấu tạo trong của LED: Bản cực to là Cathode (-), bản cực nhỏ là Anode (+).

### Question: Trong breadboard, những hàng cột nào được nối với nhau?
A. Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng ngang được cách điện với hàng còn lại. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột dọc được cách điện với các cột còn lại.
B. Khu vực A và D các lỗ được nối theo cột dọc, mỗi cột được cách điện với cột còn lại. Khu vực B và C các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với các hàng còn lại.
C. Khu vực A và D các lỗ được nối theo hàng ngang và theo từng cặp, 5 cặp theo hàng là cách điện nhau . Khu vực B và C các lỗ được nối theo cột, mỗi cột được cách điện với các cột còn lại.
D. Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với hàng còn lại và bắt buộc phải nối thiết bị theo cực (+) và cực (-) đã ký hiệu. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột được cách điện với các cột còn lại.
Correct: A
Explanation: Breadboard thông thường có 2 dải nguồn biên nối ngang và các dải linh kiện ở giữa nối dọc.

### Question: Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc nào?
A. Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc thu và phát ánh sáng hồng ngoại.
B. Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc thu và phát ánh sáng màu hồng.
C. Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc phát hiện nhiệt độ của vật cản.
D. Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc phát hiện ánh sáng màu đỏ do vật cản phát ra.
Correct: A
Explanation: Cảm biến IR phát tia hồng ngoại, nếu gặp vật cản tia sẽ phản xạ lại đầu thu.

### Question: Đối với cảm biến mưa, để giảm độ nhạy (cần nhiều nước trên bề mặt tấm cảm biến thì cảm biến mới truyền tín hiệu báo trời mưa) thì ta cần làm như thế nào?
A. Điều chỉnh biến trở (núm vặn màu xanh) trên cảm biến.
B. Dùng băng keo dán lên mặt tấm cảm biến.
C. Nối chân VCC của cảm biến với chân 3,3V hay vì 5V để giảm điện áp của cảm biến thì độ nhạy của cảm biến sẽ giảm xuống.
D. Nối chân GND của cảm biến với chân 3,3V hay vì chân GND để giảm mức chênh lệch điện áp so với chân VCC thì độ nhạy của cảm biến sẽ giảm xuống.
Correct: A
Explanation: Biến trở trên module cảm biến dùng để điều chỉnh ngưỡng so sánh điện áp (độ nhạy).

### Question: Chọn phát biểu đúng khi nói về động cơ Servo?
A. Động cơ Servo MG90S có thể xoay từ 0 đến 180 độ và ngược lại.
B. Động cơ Servo có cấu tạo hoàn toàn giống động cơ DC bình thường, chỉ khác là được tích hợp thêm 1 chân tín hiệu để lập trình thay đổi góc.
C. Động cơ Servo chỉ có thể xoay góc từ 0 đến 180 độ.
D. Chân tín hiệu của động cơ Servo được nối với chân tín hiệu analog của Arduino.
Correct: A
Explanation: Servo MG90S là servo góc quay 180 độ, nhận tín hiệu PWM từ chân Digital.

### Question: Cho mạch Arduino và đèn Led như hình bên dưới, hỏi đoạn chương trình nào dùng để điều khiển cho đèn Led sáng nhấp nháy (sáng-tắt) với chu kỳ 1 giây?
![image24.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image24.png)
A. ![image3.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image3.png)
B. ![image32.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image32.png)
C. ![image33.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image33.png)
D. ![image4.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image4.png)
Correct: A
Explanation: Để nhấp nháy chu kỳ 1s, cần bật LED -> đợi 1s -> tắt LED -> đợi 1s.

### Question: Giáo viên đưa ra yêu cầu lập trình cho cảm biến hồng ngoại như sau: Khi phát hiện vật cản thì cho đèn Led được nối với chân D8 sáng, còn không có vật cản thì cho đèn Led đó tắt. Hỏi đoạn chương trình nào dưới đây cho kết quả đúng với yêu cầu của giáo viên, biết chân DO của cảm biến được nối với chân D7.
A. ![image17.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image17.png)
B. ![image20.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1.docx_image20.png)
C. ![image