---
title: Bản sao của Bản sao của Đề kiểm tra Arduino module 1.docx
source: [[Bản sao của Bản sao của Đề kiểm tra Arduino module 1.docx]]
type: RAW_SOURCE
---

Phần 1: Mức độ nhận biết, nhắc lại.

Câu 1: Những cách cấp nguồn cho Arduino Uno R3?

A. Cấp nguồn từ cổng US

B. Cấp nguồn thông qua Adapter.

B. Cấp nguồn từ pin thông qua chân V(in).

C. Cấp nguồn từ pin thông qua chân Digital.

D. Cấp nguồn từ pin thông qua chân Analog.

E. F. Cấp nguồn không dây qua tín hiệu bluetooth.

Câu 2: Vì sao nên hạn chế sử dụng chân digital số 0 (RX) và 1 (TX)?

A.

Hai chân 0 và 1 là hai chân giao tiếp dùng cho Arduino truyền và nhận dữ liệu nên rất dễ bị nhiễu nếu ta dùng hai chân này như các chân digital thông thường.

B.

Trên phần chân digital có tổng cộng 14 chân nên không cần phải sử dụng đến hai chân 0 và

1.

C.

Hai chân 0 và 1 dùng để reset chương trình cho Arduino nên không sử dụng hai chân này.

D.

Hai chân 0 và 1 chỉ dùng cho cảm biến mưa nên phải hạn chế dùng cho các loại cảm biến khác.

Câu 3: Trên Arduino, nên sử dụng nguồn chân nào để cấp nguồn cho cảm biến?

A.

Chân GND của Arduino để nối với cực âm của cảm biến; chân 3,3V hoặc 5V của Arduino để nối với cực dương của cảm biến.

B.

Chân GND của Arduino để nối với cực âm của cảm biến; chân analog từ A0 đến A6 của Arduino để nối với cực dương của cảm biến.

C.

Chân GND của Arduino để nối với cực âm của cảm biến; chân digital từ 2 đến 13 của Arduino để nối với cực dương của cảm biến.

D.

Chọn GND của Arduino để nối với cực âm của cảm biến; chân Vin của Arduino để nối với cực dương của cảm biến.

Câu 4: Nối chân tín hiệu digital, pwm, analog bên cột A với chức năng phù hợp bên cột B

Cột A

Cột B

Digital

Chân tín hiệu số có hai giá trị 0 và

1. PWM

Dùng cho cảm biến hồng ngoại, cảm biến mưa, servo,...

Chân tín hiệu số được điều chế thành các xung có 256 giá trị từ 0 đến 255. Dùng để điều khiển tốc độ quạt, tốc độ động cơ,...

Analog

Chân tín hiệu tương tự có 1024 giá trị từ 0 đến 102

3. Dùng cho biến trở, LCD,..

Câu 5: Sắp xếp các bước theo trình tự thích hợp để kết nối Arduino với phần mềm mblock?

3. Chuyển chế độ “Live” sang “Upload”.

Mở phần mềm mBlock, dùng dây USB kết nối Arduino với máy tính.

2.

Lựa chọn thiết bị cần sử dụng là arduino ở dấu “+” khu vực thiết bị.

1.

4.

Chọn “Connect”, cửa sổ hiện lên chọn cổng kết nối và chọn “connect”.

A.

3-

2-

1-

4.

B.

1-

2-

3-

4.

C.

1-

2-

4-

3.

D.

4-

2-

3-

1.

Câu 6: Một chiếc đèn Led bị gãy chân nên không thể phân biệt các chân của đèn Led bằng chiều dài được. Nếu quan sát bằng cách nhìn bên trong đèn thì phải phân biệt như thế nào?

A. Cả 3 đáp án đều sai.

Phần (bản) cực bên trong nhỏ hơn là chân dương, phần (bản) cực to hơn là chân âm.

B.

Phần (bản) cực bên trong nhỏ hơn là chân âm, phần (bản) cực to hơn là chân dương.

C.

Không thể xác định được chân dương hay chân âm nếu đèn Led bị gãy chân.

D.

Câu 7: Trong breadboard, những hàng cột nào được nối với nhau?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId6.png)

A.

Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng ngang được cách điện với hàng còn lại. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột dọc được cách điện với các cột còn lại.

B.

Khu vực A và D các lỗ được nối theo cột dọc, mỗi cột được cách điện với cột còn lại. Khu vực B và C các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với các hàng còn lại.

C.

Khu vực A và D các lỗ được nối theo hàng ngang và theo từng cặp, 5 cặp theo hàng là cách điện nhau . Khu vực B và C các lỗ được nối theo cột, mỗi cột được cách điện với các cột còn lại.

D.

Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với hàng còn lại và bắt buộc phải nối thiết bị theo cực (+) và cực (-) đã ký hiệu. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột được cách điện với các cột còn lại.

Câu 8:

Chọn phát biểu sai:

A.

Breadboard là thiết bị được thiết kế để ta làm quen với mắc mạch điện mà không cần phải hàn.

B.

Breadboard được thiết kế với nhiều hình dạng và kích thước khác nhau.

C.

Hai hàng màu xanh và đỏ trên breadboard có chức năng cấp nguồn cho các thiết bị khác.

D.

Có thể nhìn ở mặt dưới của breadboard để kiểm tra xem hai lỗ cắm bất kỳ nào đó có được nối với nhau hay không.

Câu 9: Để kết nối các chân của Arduino với các các chân của cảm biến hồng ngoại ta sử dụng dây jumper loại nào?

A. Dây âm (-), âm (-).

B. Dây dương (+), dương (+).

C. Dây âm (-), dương (+).

D.

Nối trực tiếp chân của cảm biến với Arduino mà không cần dây điện trung gian.

Câu 10: Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc nào?

A.

Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc thu và phát ánh sáng hồng ngoại.

B.

Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc thu và phát ánh sáng màu hồng.

C.

Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc phát hiện nhiệt độ của vật cản.

D.

Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc phát hiện ánh sáng màu đỏ do vật cản phát ra.

Câu 11: Điện áp hoạt động của cảm biến hồng ngoại là bao nhiêu?

A. Từ 3,3V đến 5V.

B. 3,3V.

C. 5V.

D. 3V.

Câu 12: Biết điện áp hoạt động của cảm biến mưa là 5V. Nếu nối chân VCC của cảm biến mưa với chân 3,3V của Arduino thì sẽ có hiện tượng gì xảy ra?

A. Cảm biến sẽ bị cháy ngay lập tức.

B. Cảm biến sẽ hoạt động không chính xác.

Không xảy ra hiện tượng gì, cảm biến vẫn hoạt động bình thường.

C.

D.

Nguồn điện sẽ không còn đủ năng lượng để cho đèn led hay động cơ hoạt động.

Câu 13: Đối với cảm biến mưa, để giảm độ nhạy (cần nhiều nước trên bề mặt tấm cảm biến thì cảm biến mới truyền tín hiệu báo trời mưa) thì ta cần làm như thế nào?

A. Dùng băng keo dán lên mặt tấm cảm biến.

Điều chỉnh biến trở (núm vặn màu xanh) trên cảm biến.

B.

C.

Nối chân VCC của cảm biến với chân 3,3V hay vì 5V để giảm điện áp của cảm biến thì độ nhạy của cảm biến sẽ giảm xuống.

D.

Nối chân GND của cảm biến với chân 3,3V hay vì chân GND để giảm mức chênh lệch điện áp so với chân VCC thì độ nhạy của cảm biến sẽ giảm xuống.

Câu 14: Chọn phát biểu đúng:

A.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId7.png)

Câu lệnh chỉ dùng để xuất tín hiệu cho đèn Led

B.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId8.png)

Câu lệnh chỉ dùng để đọc tín hiệu của cảm biến hồng ngoại

C.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId7.png)

Câu lệnh  trả về giá trị với 2 trạng thái cao/thấp.

D.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId8.png)

Câu lệnh trả về giá trị với 2 trạng thái cao/thấp.

Câu 15: Chọn phát biểu đúng khi nói về động cơ Servo?

A. Phần 2: Mức độ thông hiểu.

Động cơ Servo MG90S có thể xoay từ 0 đến 180 độ và ngược lại.

B.

Động cơ Servo có cấu tạo hoàn toàn giống động cơ DC bình thường, chỉ khác là được tích hợp thêm 1 chân tín hiệu để lập trình thay đổi góc.

C.

Động cơ Servo chỉ có thể xoay góc từ 0 đến 180 độ.

D.

Chân tín hiệu của động cơ Servo được nối với chân tín hiệu analog của Arduino.

Câu 16: Cho mạch Arduino và đèn Led như hình bên dưới, hỏi đoạn chương trình nào dùng để điều khiển cho đèn Led sáng nhấp nháy (sáng-tắt) với chu kỳ 1 giây?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId9.png)

A.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId10.png)

B.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId11.png)

C.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId12.png)

D.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId13.png)

Câu 17: Chọn đáp án sai: để lập trình cho còi liên tục phát ra tiếng hú, ta dùng đoạn chương trình nào sau đây?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId14.gif)

A

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId15.png)

C

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId16.png)

B

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId17.png)

D

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId18.png)

Câu 18: Đoạn chương trình nào dưới đây cho hiệu ứng 2 đèn sáng tắt luân phiên (thời gian sáng, tắt mỗi đèn là 1 giây)?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId19.gif)

B.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId20.png)

A.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId21.png)

C.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId22.png)

D.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId23.png)

Câu 19: Một bạn học sinh mắc mạch gồm Arduino, đèn Led và breadboard, (quy ước các chân đèn Led được minh họa như hình. Hỏi khi bạn thực hiện chương trình sau thì có những đèn nào phát sáng?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId24.png)

Đây là đoạn chương trình của học sinh đã thực hiện. Hỏi những đèn nào phát sáng với đoạn chương trình trên?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId25.png)

A. Cả 5 đèn đều sáng.

B. Chỉ có đèn đỏ và đèn xanh dương sáng.

C. Chỉ có đèn xanh dương sáng.

D. Chỉ có đèn đỏ sáng.

E. Chỉ có đèn vàng không sáng.

F. Đèn đỏ, đèn xanh lá và đèn xanh dương sáng.

Câu 20: Cho mạch điện ba đèn sáng luân phiên, hãy chọn số thích hợp vào ô số 01 và 02 để được đoạn chương trình cho kết quả ba đèn sáng luân phiên như ảnh động.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId26.gif)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId27.png)

Đáp án:

Chân pin ở câu lệnh thứ nhất là 10.

Chân pin ở câu lệnh thứ hai là 1

1.

Câu 21: Cho mạch điện gồm Arduino, còi, đèn Led và breadboard được thiết lập để mô phỏng đèn xe cảnh sát đang hoạt động như hình minh hoạ. Hãy kéo và thả các câu lệnh thích hợp vào đoạn chương trình đang khuyết để được kết quả như yêu cầu.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId28.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId29.gif)

Đáp án:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId30.png)

Câu 22:  Ứng dụng nào sau đây không phải của cảm biến hồng ngoại?

A. Robot tránh vật cản.

Đo thân nhiệt con người thông qua ánh sáng hồng ngoại.

B. Đèn thông minh tự phát sáng khi có người đến.

C. Cửa tự động mở khi có người đến.

D.

Câu 23: Giáo viên đưa ra yêu cầu lập trình cho cảm biến hồng ngoại như sau: Khi phát hiện vật cản thì cho đèn Led được nối với chân D8 sáng, còn không có vật cản thì cho đèn Led đó tắt. Hỏi đoạn chương trình nào dưới đây cho kết quả đúng với yêu cầu của giáo viên, biết chân DO của cảm biến được nối với chân D7.

A.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId31.png)

B.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId32.png)

C.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId33.png)

D.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId34.png)

Câu 24: Yêu cầu lập trình cho cảm biến hồng ngoại, đèn Led và còi hoạt động như sau: khi không có vật cản, đèn xanh sáng, đèn đỏ tắt, còi tắt; khi có vật cản đèn xanh sáng thêm 2 giây rồi tắt, còi hú báo động, đèn đỏ sáng.

Quan sát sơ đồ nối mạch dưới đây, hỏi người mắc đã nối sai linh kiện gì và sai như thế nào?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId35.png)

A.

Chân VCC của cảm biến chưa được nối với chân 3,3V của Arduino.

B.

Nối sai chân dương của đèn Led đỏ. Chân dương của đèn Led đỏ nối với chân tín hiệu digital của Arduino để có thể lập trình.

C.

Chân GND của cảm biến chưa được nối với chân GND của Arduino.

D.

Nối sai chân dương của đèn Led xanh. Chân dương của đèn Led xanh phải nối với chân D5 của Arduino.

E.

Nối sai chân âm của đèn Led xanh. Chân âm của đèn cần nói với chân GND của Arduino.

F. Nối sai chân âm của đèn Led đỏ. Chân âm của đèn cần nói với chân GND của Arduino.

Câu 25: Yêu cầu lập trình cho cảm biến hồng ngoại, đèn Led và còi hoạt động như sau: khi không có vật cản, đèn xanh sáng, đèn đỏ tắt, còi tắt;  khi có vật cản đèn xanh sáng 2 giây rồi tắt, còi hú báo động, đèn đỏ sáng.

Quan sát đoạn chương trình dưới đây, hãy tìm điểm sai trong đoạn chương trình.

Biết các chân tín hiệu được nối như bảng bên dưới.

### Table Data

| Linh kiện điện tử  | Arduino  |
| Chân D0 của cảm biến hồng ngoại  | D7  |
| Chân dương của còi  | D12  |
| Chân dương của đèn xanh  | D8  |
| Chân dương của đèn đỏ  | D9  |

Chương trình:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId36.png)

A. Thiếu câu lệnh cho đèn led xanh tắt.

B. Đặt sai điều kiện của câu lệnh if...then.

Sai chân tín hiệu của đèn led đỏ, đèn Led xanh và còi.

C.

Phải sử dụng câu lệnh if...then...else thay cho câu lệnh if...then.

D.

E.

Thiếu thời gian cho đèn xanh sáng khi không có vật cản.

F. Thiếu câu lệnh cho đèn đỏ tắt sau khi đã sáng khi có vật cản.

Câu 26: Yêu cầu lập trình cho cảm biến mưa và các đèn Led hoạt động như sau: khi trời không mưa, đèn đỏ sáng, đèn xanh tắt; khi trời mưa, đèn đỏ tắt, đèn xanh sáng.

Một học sinh đã lập trình như sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId37.png)

Hỏi học sinh đó đã nối chân tín hiệu của cảm biến mưa và đèn Led với các chân nào của Arduino?

A. Chân dương của đèn Led đỏ nối với chân D5.

Chân tín hiệu của cảm biến mưa được nối với chân D6. Chân dương của đèn Led xanh nối với chân D

4. Chân dương của đèn Led đỏ nối với chân D5.

B.

Chân tín hiệu của cảm biến mưa được nối với chân D6. Chân dương của đèn Led xanh nối với chân D5. Chân dương của đèn Led đỏ nối với chân D

4.

C.

Chân tín hiệu của cảm biến mưa được nối với chân A6. Chân dương của đèn Led xanh nối với chân D5. Chân dương của đèn Led đỏ nối với chân D

4.

D.

Chân tín hiệu của cảm biến mưa được nối với chân A6. Chân dương của đèn Led xanh nối với chân D

4.

Câu 27: Cho các linh kiện điện tử và các chân kết nối như bảng dưới đây:

### Table Data

| Tên linh kiện  | Chân kết nối của linh kiện  | Chân kết nối của Arduino  |
| Cảm biến mưa  | VCC  | 5V  |
| Cảm biến mưa  | GND  | GND  |
| Cảm biến mưa  | D0  | D8  |
| Đèn Led xanh  | Chân dương  | D7  |
| Đèn Led xanh  | Chân âm  | GND  |
| Đèn Led đỏ  | Chân dương  | D6  |
| Đèn Led đỏ  | Chân âm  | GND  |
| Còi buzzer  | Chân dương  | D5  |
| Còi buzzer  | Chân âm  | GND  |

Cho đoạn chương trình sau, mô tả nào dưới đây đúng với kết quả của chương trình nhất:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId38.png)

A.

Khi trời không mưa thì đèn xanh sáng, đèn đỏ và còi tắt. Khi trời mưa thì đèn xanh sáng tiếp trong 3 giây sau đó tắt;  đèn đỏ sáng lên; còi buzzer báo động hú tắt liên tục (thời gian hú tắt đứt quãng là 1 giây) cho đến khi hết mưa.

B.

Khi trời không có mưa thì đèn đỏ sáng, đèn xanh và còi tắt. Khi trời mưa thì đèn đỏ sáng tiếp trong 3 giây sau đó tắt;  đèn xanh sáng lên và còi buzzer báo động hú tắt liên tục (thời gian hú ngắt quãng là 1 giây) cho đến khi hết mưa.

C.

Khi trời không mưa thì đèn xanh sáng, đèn đỏ tắt, còi tắt. Khi trời mưa thì đèn xanh sáng trong 3 giây sau đó tắt; đèn đỏ sáng lên, sau đó tắt và còi buzzer báo động hú tắt liên tục (thời gian hú ngắt quãng là 1 giây) cho đến khi hết mưa.

D.

Khi trời mưa thì đèn Led màu xanh sáng, đèn đỏ và còi tắt. Khi trời không mưa mưa thì đèn xanh sáng trong 3 giây sau đó tắt;  đèn đỏ sáng lên và còi buzzer báo động hú tắt liên tục (thời gian mỗi lần hú, tắt là 1 giây) cho đến khi trời mưa.

Câu 28: Tìm đoạn chương trình cho kết quả quan sát được động cơ servo MG90S quay theo góc tăng dần từ góc 0 đến góc 90 độ

A.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId39.png)

B.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId40.png)

C.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId41.png)

D.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId42.png)

Câu 29: Tìm đoạn chương trình cho kết quả quan sát được động cơ servo MG90S quay theo góc từ góc 0 độ đến góc 150 độ, sau đó, quay ngược lại từ góc 150 độ về góc 0 độ (thời gian ngắt quãng là 1 giây)

A.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId43.png)

B.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId44.png)

C.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId45.png)

D.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId46.png)

Câu 30: Yêu cầu lập trình cho cảm biến mưa, động cơ servo và các đèn Led như sau:

khi trời không mưa đèn xanh và đèn vàng sáng, đèn đỏ tắt, servo được đặt ở góc 0 độ;

khi trời mưa, đèn xanh và đèn vàng sáng nhấp nháy luân phiên trong 3 giây (chu kỳ sáng-tắt là 0.5 giây, khi đèn này sáng thì đèn kia tắt),.

sau đó servo quay từ góc 0 độ sang 180 độ, đèn đỏ sáng nhấp nháy (chu kỳ là 1 giây) cho đến khi trời hết mưa.

Đoạn chương trình dưới đây bị thiếu một số câu lệnh, hãy bổ sung các câu lệnh phù hợp vào đoạn chương trình để cho kết quả hoạt động đúng như mô tả.

### Table Data

| Tên linh kiện  | Chân kết nối của linh kiện  | Chân kết nối của Arduino  |
| Cảm biến mưa  | VCC  | 5V  |
| Cảm biến mưa  | GND  | GND  |
| Cảm biến mưa  | D0  | D8  |
| Đèn Led xanh  | Chân dương  | D7  |
| Đèn Led xanh  | Chân âm  | GND  |
| Đèn Led đỏ  | Chân dương  | D6  |
| Đèn Led đỏ  | Chân âm  | GND  |
| Đèn Led vàng  | Chân dương  | D3  |
| Đèn Led vàng  | Chân âm  | GND  |
| Động cơ Servo  | Chân dương  | 5V  |
| Động cơ Servo  | Chân âm  | GND  |
| Động cơ Servo  | Chân tín hiệu  | D9  |

Chương trình:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId47.png)

Bổ sung câu lệnh cho đèn vàng sáng khi trời không có mưa.

Bổ sung câu lệnh lặp lại để đảm bảo đèn xanh, đèn vàng nhấp nháy đủ 3 giây.

Bổ sung câu lệnh cho servo quay tới góc 180 độ khi trời mưa.

Bổ sung câu lệnh cho servo quay từ góc 180 về 0 độ khi trời không có mưa.

Bổ sung câu lệnh cho đèn đỏ sáng khi trời mưa.

Bổ sung câu lệnh cho đèn xanh, đèn vàng tắt khi trời mưa.

ĐỀ KIỂM TRA TRẮC NGHIỆM - Lập trình Arduino Module 2
(Đề

1) - Thời gian làm bài: 25 phút

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
| Remote và mắt thu hồng ngoại  | 10  | 11  |
| Mạch L298 và động cơ vàng, động cơ bơm  | 12  | 13,14,15  |

Câu 1 (Nhận biết)

Trong breadboard, những hàng cột nào được nối với nhau?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId48.png)

A/

Tất cả các lỗ ở cả 4 khu vực A, B, C, D đều dẫn điện với nhau.

B/

Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong từng khu vực

A/

B/

C/

D, tất cả các lỗ trong khu vực đó đều dẫn điện với nhau.

C/

Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng DỌC (2 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng NGANG (30 lỗ) dẫn điện với nhau.

D/

Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng NGANG (25 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng DỌC (5 lỗ) dẫn điện với nhau.

Câu 2 (Thông hiểu)

Cho mạch Arduino và đèn Led như hình bên dưới, hỏi đoạn chương trình nào dùng để điều khiển cho đèn Led sáng nhấp nháy (sáng-tắt) với chu kỳ 2 giây?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId49.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId50.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId51.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId52.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId53.png)

Câu 3 (Thông hiểu)

Yêu cầu lập trình cho cảm biến mưa và các đèn Led hoạt động như sau: khi trời không mưa, đèn đỏ sáng, đèn xanh tắt; khi trời mưa, đèn đỏ tắt, đèn xanh sáng.

Một học sinh đã lập trình như sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId54.png)

Hỏi học sinh đó đã nối chân tín hiệu của cảm biến mưa và đèn Led với các chân nào của Arduino?

A/ Chân dương của đèn Led đỏ nối với chân D5.

Chân tín hiệu của cảm biến mưa được nối với chân A6. Chân dương của đèn Led xanh nối với chân D

4. Chân dương của đèn Led đỏ nối với chân D5.

B/

Chân tín hiệu của cảm biến mưa được nối với chân A6. Chân dương của đèn Led xanh nối với chân D5. Chân dương của đèn Led đỏ nối với chân D

4.

C/

Chân tín hiệu của cảm biến mưa được nối với chân D6. Chân dương của đèn Led xanh nối với chân D

4.

D/

Chân tín hiệu của cảm biến mưa được nối với chân D6. Chân dương của đèn Led xanh nối với chân D5. Chân dương của đèn Led đỏ nối với chân D

4.

Câu 4 (Nhận biết)

Đáp án nào sau đây là đúng khi nói về cách kết nối màn hình LCD với Arduino?

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId55.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId56.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId57.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId58.png)

Câu 5 (Thông hiểu)

Đoạn lệnh nào sau đây làm cho màn hình LCD hiện lên dòng chữ như sau?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId59.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId60.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId61.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId62.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId63.png)

Câu 6 (Thông hiểu)

Đoạn lệnh nào sau đây làm cho màn hình LCD hiện lên dòng chữ như sau?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId64.gif)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId65.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId66.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId67.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId68.png)

Câu 7 (Thông hiểu)

Cho đoạn lệnh và yêu cầu như sau:

Yêu cầu

- Sử dụng cảm biến ánh sáng và Arduino để liên tục nhận biết ánh sáng mỗi 1 giây.

- Có 2 đèn LED đỏ, xanh: 
  + Đèn xanh luôn bật cho thấy chương trình có hoạt động.

+ Khi trời đủ sáng, đèn đỏ tắt. Khi trời tối, đèn đỏ tự động bật.
- Có 1 màn hình LCD:
  + Khi trời tối, màn hình hiển thị “Anh sang YEU”
  + Khi trời sáng, màn hình hiển thị “Anh sang TOT”

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId69.png)

Với đoạn lệnh như trên, hãy lựa chọn đáp án thể hiện đúng các chân thiết bị so với yêu cầu như trên.

A/ Chân dương đèn LED đỏ: D12

Chân dương đèn LED xanh: D13

Chân DO/OUT của cảm biến ánh sáng: D9

Chân SDA của màn hình LCD: A4

Chân SCL của màn hình LCD: A5

B/ Chân dương đèn LED đỏ: D13

Chân dương đèn LED xanh: D12

Chân DO/OUT của cảm biến ánh sáng: D9

Chân SDA của màn hình LCD: A5

Chân SCL của màn hình LCD: A4

C/ Chân dương đèn LED đỏ: D13

Chân dương đèn LED xanh: D12

Chân DO/OUT của cảm biến ánh sáng: D9

Chân SDA của màn hình LCD: A1

Chân SCL của màn hình LCD: A2

D/ Chân dương đèn LED đỏ: D13

Chân dương đèn LED xanh: D12

Chân DO/OUT của cảm biến ánh sáng: D9

Chân SDA của màn hình LCD: A4

Chân SCL của màn hình LCD: A5

Câu 8 (Thông hiểu)

Sử dụng cảm biến nhiệt độ, độ ẩm DHT11 và màn hình LCD, đoạn lệnh nào sau đây thực hiện yêu cầu sau:

- Ở dòng 1 của màn hình LCD hiện lên “N.Do: ____ do C”; Với “___” là số đo nhiệt độ nhận được từ cảm biến DHT1

1.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId70.png)

- Ở dòng 2 của màn hình LCD hiện lên “Do am: ____ %”; Với “___” là số đo % độ ẩm nhận được từ cảm biến DHT1

1.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId71.png)

- Mỗi 2 giây, màn hình LCD sẽ cập nhật chỉ số nhiệt độ và độ ẩm.

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId72.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId73.png)

C/

D/

Câu 9 (Nhận biết)

Nhận định nào sau đây là đúng khi nói về cảm biến siêu âm H

C- SR04?

(Nhiều đáp án)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId74.png)

A/ Chân Trig của cảm biến được gắn với chân Digital

Cảm biến gồm 2 đầu trái, phải dùng để phát và thu âm thanh.

B/ 13 ở Arduino.

Đầu bên trái dùng để phát ra sóng siêu âm, đầu bên phải dùng để thu sóng siêu âm.

C/ G/ Cảm biến siêu âm H

Chân GND của cảm biến được gắn với chân GND ở Arduino.

D/

Chân VCC của cảm biến được gắn với chân GND ở Arduino.

E/

2-

F/ Chân Echo của cảm biến được gắn với chân Analog 0-5 ở Arduino.

C-

SR04 có thể đo khoảng cách đến vật cản từ  2cm đến vô hạn.

Câu 10 (Nhận biết)

Hãy gọi tên và sắp xếp thứ tự các chân của mắt thu hồng ngoại VS1838 từ trái sang phải?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId75.png)

A/ VCC - GND - Out

B/ VCC - Out - GND

C/ GND - VCC - Out

D/ Out - GND - VCC

Câu 11 (Thông hiểu)

Cho mạch điện gồm mắt thu hồng ngoại và 2 đèn LED đỏ, xanh như hình sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId76.png)

Hãy lựa chọn chương trình phù hợp để điều khiển đèn LED bằng remote hồng ngoại:

- Phím 1: Đèn đỏ sáng, đèn xanh tắt.

- Phím 2: Đèn xanh sáng, đèn đỏ tắt.

- Phím 3: Cả 2 đèn đều tắt.

- Phím 4: Cả 2 đèn đều sáng.

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId77.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId78.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId79.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId80.png)

Câu 12 (Nhận biết)

Nhận định nào sau đây là đúng khi nói về cách kết nối mạch L298, động cơ với Arduino và nguồn điện?

(Nhiều đáp án)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId81.png)

A/

Nguồn điện 4 pin cùng lúc trực tiếp cấp điện cho mạch L298 và Arduino.

B/

Nguồn điện 4 pin trực tiếp cấp điện cho mạch L298; Arduino được cấp điện gián tiếp, thông qua mạch L298.

C/

Động cơ M1 được kết nối với chân pin D12,D13 của Arduino; Động cơ M2 được kết nối với chân pin D7,D8 của Arduino.

D/

Động cơ M1 được kết nối với chân pin D7,D8 của Arduino; Động cơ M2 được kết nối với chân pin D12,D13 của Arduino.

E/

Cách nối mạch điện như trên sẽ làm động cơ hoạt động yếu.

F/ Cách nối mạch điện như trên là dư thừa, vì mỗi động cơ chỉ cần kết nối với 1 chân Digital trên Arduino.

Câu 13 (Thông hiểu)

Một học sinh chế tạo một chiếc xe hoạt động bằng Arduino, mạch L298 và động cơ vàng như mạch điện như hình dưới.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId82.png)

Biết rằng sau khi học sinh thử nghiệm chiều xoay của 2 động cơ bằng đoạn lệnh sau, xe đã xoay tròn ngược chiều kim đồng hồ.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId83.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId84.png)

Hỏi để điều chỉnh cho xe chạy thẳng khi khởi động, ta có thể sử dụng đoạn lệnh nào sau đây?

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId85.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId86.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId87.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId88.png)

Câu 14 (Thông hiểu)

Một học sinh chế tạo một chiếc xe hoạt động bằng Arduino, mạch L298, động cơ vàng và điều khiển bằng remote hồng ngoại như mạch điện như hình dưới.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId89.png)

Biết rằng sau khi học sinh test bằng đoạn lệnh sau và nhấn phím 2 trên remote hồng ngoại, xe đã xoay tròn ngược chiều kim đồng hồ.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId90.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId84.png)

Hỏi cũng với chương trình trên, để xe chạy tiến thẳng, ta cần nhấn phím nào trên remote hồng ngoại?

A/ Phím 6

B/ Phím 8

C/ Phím 4

D/ Phím 5

Câu 15 (Thông hiểu)
(ĐỀ GẦN GIỐNG CÂU 1

4)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId89.png)

Một học sinh chế tạo một chiếc xe hoạt động bằng Arduino, mạch L298, động cơ vàng và điều khiển bằng remote hồng ngoại như mạch điện như hình dưới.

Biết rằng sau khi học sinh test bằng đoạn lệnh sau và nhấn phím 2 trên remote hồng ngoại, xe đã xoay tròn ngược chiều kim đồng hồ.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId90.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId84.png)

Hỏi cũng với chương trình trên, để xe dừng di chuyển, ta cần nhấn phím nào trên remote hồng ngoại?

A/ Phím 6

B/ Phím 8

C/ Phím 4

D/ Phím 5

Bộ câu hỏi trắc nghiệm, tự luận - Arduino Module 1,2

- 60 câu: 24 nhận biết (40%) - 36 thông hiểu (60%)
- Câu trắc nghiệm 1 đáp án: 1 điểm
- Câu trắc nghiệm nhiều đáp án: Số điểm = số đáp án đúng, đúng 1 câu được 1 điểm
- Điểm đạt: 75% điểm tối đa

- Thời gian làm bài: 45-60 phút (30 câu)

### Table Data

|   Các kiến thức cần đạt  60% M1 = 12 câu 40% M2 = 18 câu  | Giáo viên 1  | Giáo viên 1  | Giáo viên 2  | Giáo viên 2  |
|   Các kiến thức cần đạt  60% M1 = 12 câu 40% M2 = 18 câu  | Nhận biết (12 câu)  | Thông hiểu / Vận dụng (18 câu)  | Nhận biết (12 câu)  | Thông hiểu / Vận dụng (18 câu)  |
| Cấu tạo Arduino  | 1  | 13  | 31  | 43  |
| Cấu tạo, cách sử dụng và lập trình các thiết bị output - Đèn LED - Còi Buzzer - Động cơ Servo (Lập trình: Câu lệnh thực thi + Hiệu ứng  vòng lặp)  |     2  3  4  |     14, 15  16  17  |     32  33  34  |     44, 45  46  47  |
| Cấu tạo, cách sử dụng Breadboard để lắp mạch Arduino  | 5  | 18, 19  | 35  | 48, 49  |
| Cấu tạo và lập trình thiết bị Input - Cảm biến hồng ngoại - Cảm biến ánh sáng - Cảm biến mưa  |     6    7  |     20, 21  22  23  |       36  37  |     50, 51  52  53  |
| Cấu tạo, cách sử dụng và lập trình màn hình LCD  | 8  | 24, 25  | 38  | 54, 55  |
| Cấu tạo, cách sử dụng và lập trình cảm biến nhiệt độ độ ẩm DHT11  | 9  | 26  | 39  | 56  |
| Cảm biến siêu âm  | 10  | 27  | 40  | 57  |
| Remote và mắt thu hồng ngoại  |   |   |   |   |
| Joystick  | 9,11  | 28, 29  | 39,41  | 58, 59  |
| Mạch L298 và động cơ vàng, động cơ bơm  | 12  | 26,30  | 42  | 56,60  |
| Bài thực hành  | Bài 1  | Bài 2  | Bài 3  | Bài 4  |

Câu 1 (Nhận biết)

Bộ phận nào dùng để gắn dây kết nối với máy tính?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId91.png)

A/ A

B/ B

C/ C

D/ D

Câu 2 (Nhận biết)

Phát biểu nào sau đây là sai khi nói về đèn LED đơn?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId92.png)

A/ Đèn LED là thiết bị output

Phần bản to hơn là cực dương, phần bản nhỏ là cực âm

B/ Cực dương của đèn LED được cắm vào chân D

C/ D13 của Arduino

Cực âm của đèn LED được cắm vào chân GND của Arduino

D/

2-

Câu 3 (Nhận biết)

Phát biểu nào sau đây là đúng khi nói về còi Buzzer?

A/ Chân dài của còi buzzer gắn với cực âm của pin

Chân ngắn của còi buzzer gắn với chân GND của arduino

B/

Chân dài của còi buzzer gắn với chân GND  của arduino

C/

Chân ngắn của còi buzzer gắn với cực dương của pin

D/

Câu 4 (Nhận biết)

Dây màu cam của servo cắm với chân nào của Arduino?

A/ D

2- D13

B/ 5V

C/ GND

D/ VIN

Câu 5 (Nhận biết)

Breadboard kết nối với nhau theo quy tắc nào?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId93.png)

A/ Khu vực 1 và 4 dòng điện đi theo hàng dọc.

B/ Khu vực 1 và 4 dòng điện đi theo hàng ngang.

C/ Khu vực 2 và 3 dòng điện đi theo hàng dọc.

D/ Khu vực 1 và 3 dòng điện đi theo hàng ngang.

Câu 6 (Nhận biết)

Cách lắp servo với mạch Arduino theo thứ tự chân VC

C/ GN

D/ OUT nào dưới đây là đúng?

A/ 5V/GN

D/ D

2- D13

B/ D

2- D1

3/ GN

D/ 5V.

C/ GN

D/ D

2- D1

3/ 5V

D/ 5V/D

2- D1

3/ GND

Câu 7 (Nhận biết)

Để cảm biến mưa có thể hoạt động được thì cần phải cung cấp lượng điện áp bao nhiêu?

A/ 5V

B/ 3V

C/ 3,3V

D/ 1,5V

Câu 8 (Nhận biết)

Màn hình LCD I2C có mấy chân kết nối và tên gọi của chúng là gì?

A/ 4 chân (VCC, GND, SCL, SD

A) 4 chân (VCC, GND, LCD, SD

B/ 4 chân (VCC, GND, LCD, DS

A) 4 chân (VCC, GND, SCL, DS

C/

A)

D/

A)

Câu 9 (Nhận biết)

Chân VRx của joystick có tác dụng gì?

A/

Đo mức độ di chuyển của joystick theo trục X (trục song song với phương của các chân kết nối trên joystick)

B/

Đo mức độ di chuyển của joystick theo trục X (trục vuông góc với phương của các chân kết nối trên joystick)

C/

Đo mức độ di chuyển của joystick theo trục Y (trục vuông góc với phương của các chân kết nối trên joystick)

D/

Đo mức độ di chuyển của joystick theo trục Y (trục song song với phương của các chân kết nối trên joystick)

Câu 10 (Nhận biết)

Câu lệnh nào phù hợp với cách lắp mạch dưới đây?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId94.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId95.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId96.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId97.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId98.png)

Câu 11 (Nhận biết)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId99.png)

Khi núm điều khiển trên Joystick được gạt lên trên, giá trị Y sẽ thay đổi vào khoảng bao nhiêu?

A/ từ 511 về 0

B/ từ 511 đến 1023

C/ từ -511 đến 0

D/ Từ -511 đến 1023

Câu 12 (Nhận biết)

Phát biểu nào sau đây là đúng?

A/ Tổng số chân kết nối của mạch L298 là 11 chân

B/ Điện áp hoạt động tối đa của mạch L298 là 5V

C/ Mạch L298 chỉ điều khiển được 1 thiết bị

D/ Điện áp mạch L298 cấp cho thiết bị tối đa là 12V

Câu 13 (Hiểu)

Phương án nào sau đây KHÔNG PHẢI là cách cấp nguồn cho Arduino?
(Nhiều đáp án)

A/

Gắn cực dương của nguồn điện vào chân 5V của Arduino, gắn cực âm của nguồn điện vào chân GN

D.

B/

Gắn cực dương của nguồn điện vào chân 3V của Arduino, gắn cực âm của nguồn điện vào chân GN

D.

C/

Gắn cực dương của nguồn điện vào chân VIN của Arduino, gắn cực âm của nguồn điện vào chân GN

D.

D/

Sử dụng dây cáp USB type B, kết nối giữa Arduino với máy tính.

Câu 14 (Hiểu)

Với đoạn chương trình dưới đây, đèn LED sẽ có hiệu ứng như thế nào? Biết các chân tín hiệu được nối như bảng bên dưới.

Linh kiện điện tử

Arduino

Chân dương của đèn 1

D13

Chân dương của đèn 2

D12

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId100.png)

A/ 2 đèn sáng tắt luân phiên

B/ 2 đèn sáng tắt cùng lúc

C/

2 đèn sáng tắt luân phiên 5 lần, sau đó cả 2 tất hẳn

D/

2 đèn sáng tắt cùng lúc 5 lần, sau đó cả 2 tất hẳn

Câu 15 (Hiểu)

Đoạn chương trình nào dưới đây thực hiện yêu cầu sau:

Mạch điện gồm 2 đèn LED xanh, đỏ
Khi khởi động, 2 đèn LED sáng tắt luân phiên nhau mỗi 1 giây. Sau 10 lần sáng tắt luân phiên, đèn LED xanh sáng còn đèn LED đỏ tắt mãi mãi.

Biết các chân tín hiệu được nối như bảng bên dưới.

Linh kiện điện tử

Arduino

Chân dương của LED xanh

D9

Chân dương của LED đỏ

D10

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId101.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId102.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId103.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId104.png)

Câu 16 (Vận dụng)

Điền đoạn lập trình còn thiếu để chương trình có hiệu ứng:

Khi khởi động, servo xoay qua lại từ 0 đến 90 độ. Khi servo xoay ngược chiều kim đồng hồ, đèn LED sẽ sáng, khi servo xoay cùng chiều kim đồng hồ, đèn LED sẽ tắt.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId105.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId106.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId107.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId108.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId109.png)

Câu 17 (Vận dụng)

Điền từ thích hợp để chương trình có hiệu ứng 3 đèn nhấp nháy luân phiên.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId110.png)

A/ High - high - low

B/ High - low - high

C/ Low - high - low

D/ Low - low - high

Câu 18 (Hiểu)

Với mạch điện và chương trình dưới đây, đèn LED nào hoạt động?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId111.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId112.png)

A/ Chỉ đèn vàng sáng

B/ Chỉ đèn đỏ sáng

C/ Chỉ đèn xanh lá sáng

D/ Đèn đỏ và xanh lá đều sáng

E/ Cả 3 đèn đều sáng

Câu 19 (Vận dụng)

Cách lắp mạch điện nào sau đây cho hiệu ứng đèn đỏ và xanh sáng cùng lúc

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId113.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId114.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId115.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId116.png)

Câu 20 (Hiểu)

Với mạch điện và đoạn chương trình sau sẽ có hiệu ứng như thế nào?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId117.png)

A/ Khi không có và có vật cản, đèn LED đều tắt.

Khi không có vật cản, đèn LED tắt. Khi có vật cản, đèn LED sáng - tắt mỗi 0,5s và lặp lại mãi mãi

B/ Khi không có và có vật cản, đèn LED đều sáng.

C/

Khi không có vật cản: đèn LED tắt. Khi có vật cản: đèn LED sáng.

D/

Câu 21 (Hiểu)

Cho các linh kiện điện tử sau

### Table Data

| Tên linh kiện  | Chân kết nối của linh kiện  | Chân kết nối của Arduino  |
| Cảm biến mưa  | VCC  | 5V  |
| Cảm biến mưa  | GND  | GND  |
| Cảm biến mưa  | D0  | D8  |
| Còi buzzer  | Chân dương  | D7  |
| Còi buzzer  | Chân âm  | GND  |

Chọn chương trình thực hiện đúng yêu cầu: Nếu trời không mưa, còi buzzer tắt, nếu trời mưa thì còi kêu tắt mỗi 3s, lặp lại liên tục.

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId118.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId119.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId120.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId121.png)

Câu 22 (Vận dụng)

Cho các linh kiện điện tử sau

### Table Data

| Tên linh kiện  | Chân kết nối của linh kiện  | Chân kết nối của Arduino  |
| Cảm biến mưa  | VCC  | 5V  |
| Cảm biến mưa  | GND  | GND  |
| Cảm biến mưa  | D0  | D8  |
| Đèn LED  | Chân dương  | D13  |
| Đèn LED  | Chân âm  | GND  |

Điền vào chỗ trống để chương trình có hiệu ứng: Khi có mưa, đèn led nhấp nháy 0.5s. Khi không mưa, đèn LED nhấp nháy 5s.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId122.png)

A/ 1 - 13 - 8 - 0

B/ 1 - 8 - 13 - 0

C/ 0 - 13 - 8 - 1

D/ 0 - 8 - 13 - 1

Câu 23 (Vận dụng)

Cho mạch điện gồm 1 cảm biến hồng ngoại, 2 đèn led có chương trình có hiệu ứng sau: nếu phát hiện vật cản 2 đèn led sẽ nhấp nháy luân phiên, nếu không có vật cản, 2 đèn led tắt. Hãy cho biết các chân kết nối thiết bị với arduino

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId123.png)

### Table Data

| Tên linh kiện  | Chân kết nối của linh kiện  | Chân kết nối của Arduino  |
| Cảm hồng ngoại  | VCC  | 5V  |
| Cảm hồng ngoại  | GND  | GND  |
| Cảm hồng ngoại  | D0  |   |
| Đèn LED 1  | Chân dương  |   |
| Đèn LED 1  | Chân âm  | GND  |
| Đèn LED 2  | Chân dương  | 12  |
| Đèn LED 2  | Chân âm  |   |

A/ D7 - D13 - GND

B/ D7 - D12 - GND

C/ D13 - D7 - GND

D/ D12 - D7 - GND

Câu 24 (Hiểu)

Đoạn lập trình nào phù hợp với hiệu ứng sau

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId124.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId125.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId126.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId127.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId128.png)

Câu 25 (Vận dụng)

TÌm lỗi sai của đoạn chương trình sau sao cho có hiệu ứng màn hình hiển thị thời gian đếm ngược từ 3 -

1.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId129.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId130.png)

Thiếu câu lệnh  trước mỗi lần đổi số.

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId131.png)

Thiếu câu lệnh cho toàn bộ đoạn chương trình

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId132.png)

Thiếu câu lệnh  sau mỗi lần đổi số

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId133.png)

Dư câu lệnh sau mỗi lần đổi số

Câu 26 (Hiểu)

Một học sinh lắp mạch điện như sau. Đoạn lập trình sau cho hiệu ứng như thế nào

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId134.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId135.png)

A/ Động cơ đứng yên mãi mãi.

Động cơ quay trong 2 giây, sau đó dừng quay trong 2 giây, lặp lại mãi mãi.

B/ Động cơ quay liên tục.

C/

D/

Động cơ quay theo chiều kim đồng hồ trong 2 giây, sau đó quay ngược chiều kim đồng hồ trong 2 giây, lặp lại mãi mãi.

Câu 27 (Vận dụng)

Cho mạch điện và đoạn chương trình dưới đây. Điền vào chỗ trống để chương trình có hiệu ứng:

Nếu khoảng cách từ vật cản đến cảm biến nhỏ hơn 20cm thì cả 2 đèn sáng-tắt cùng nhau; Nếu không, thì đèn xanh sáng, đèn đỏ tắt.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId136.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId137.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId138.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId139.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId140.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId141.png)

Câu 28 (Vận dụng)

Cho mạch điện gồm 1 joystick, 1 servo với chương trình có hiệu ứng: Nếu giá trị VRx > 700 thì xoay servo góc 120 độ. Nếu giá trị VRx < 300 thì xoay servo góc 45 độ.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId142.png)

Các chân linh kiện được nối như thế nào?

A/ Chân VRX: A1

Dây cam: D11

B/ Chân VRX: D1

Dây cam: D11

C/ Chân VRX: A1

Dây cam: D1

D/ Chân VRX: A11

Dây cam: D1

Câu 29 (Hiểu)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId99.png)

Biết mạch điện được nối như sau:

### Table Data

| Tên linh kiện  | Chân kết nối của linh kiện  | Chân kết nối của Arduino  |
| Joystick  | VCC  | 5V  |
| Joystick  | GND  | GND  |
| Joystick  | VRx  | A0  |
| Joystick  | VRy  | A1  |
| Đèn LED đỏ  | Chân dương  | D13  |
| Đèn LED xanh  | Chân dương  | D12  |
| Đèn LED vàng  | Chân dương  | D11  |

Đoạn chương trình dưới đây cho hiệu ứng như thế nào?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId143.png)

A/

Khi kéo joystick theo hướng ngang, qua trái, đèn LED đỏ sẽ sáng.

Khi để joystick ở vị trí cân bằng, đèn LED xanh sẽ sáng.

Khi kéo joystick theo hướng ngang, qua phải, đèn LED vàng sẽ sáng.

B/

Khi kéo joystick theo hướng ngang, qua trái, đèn LED xanh sẽ sáng.

Khi để joystick ở vị trí cân bằng, đèn LED đỏ sẽ sáng.

Khi kéo joystick theo hướng ngang, qua phải, đèn LED vàng sẽ sáng.

C/

Khi kéo joystick theo hướng ngang, qua trái, đèn LED vàng sẽ sáng.

Khi để joystick ở vị trí cân bằng, đèn LED xanh sẽ sáng.

Khi kéo joystick theo hướng ngang, qua phải, đèn LED đỏ sẽ sáng.

D/

Khi kéo joystick theo hướng ngang, qua trái, đèn LED đỏ sẽ sáng.

Khi để joystick ở vị trí cân bằng, đèn LED vàng sẽ sáng.

Khi kéo joystick theo hướng ngang, qua phải, đèn LED xanh sẽ sáng.

Câu 30 (Vận dụng)

Cho mạch 1 mạch được lắp như hình.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId82.png)

Biết rằng sau khi học sinh thử nghiệm chiều xoay của 2 động cơ bằng đoạn lệnh sau, xe đã đi tới.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId144.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId145.png)

Hỏi để điều chỉnh cho xe chạy thẳng khi khởi động, ta có thể sử dụng đoạn lệnh nào sau đây?

(Dạng ghép nối)

Đáp án

Cột trái

Cột phải

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId146.png)

Chạy lùi

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId147.png)

Xoay ngược chiều kim đồng hồ

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId148.png)

Xoay cùng chiều kim đồng hồ

Câu 31 (Nhận biết)

Nối tên với các bộ phận tương ứng

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId149.png)

A/ Nút reset

B/ Cổng USB - type B

C/ Jack DC

D/ Các chân nguồn

E/ Các chân pin (chân tín hiệu)

Câu 32  (Nhận biết)

Trong trường hợp chân đèn led bị gãy làm không biết được chân âm - dương qua độ dài của chân đèn thì ta còn có thể dựa vào đặc điểm nào dưới đây ?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId92.png)

A/ Cả 3 đáp án đều sai.

Nhìn vào phần (bản) cực bên trong đèn nhỏ hơn là chân dương, phần (bản) cực to hơn là chân âm.

B/

Nhìn vào phần (bản) cực bên trong đèn nhỏ hơn là chân âm, phần (bản) cực to hơn là chân dương.

C/

Không thể xác định được chân dương hay chân âm nếu đèn Led bị gãy chân.

D/

Câu 33 (Nhận biết)

Phát biểu về còi buzzer nào sau đây là SAI ?

A/

Còi buzzer có 2 chân kết nối. Chân dài là chân âm; chân ngắn là chân dương.

B/

Còi buzzer là một thiết bị có thể phát ra âm thanh.

C/

Còi buzzer có khả năng tiếp nhận điện năng và chuyển chúng thành tín hiệu âm thanh.

D/

Chân dương của còi buzzer được nối với chân digital từ 2 đến 13 trên Arduino, chân âm được nối với GN

D.

Câu 34 (Nhận biết)

Cách mắc servo với mạch Arduino theo thứ tự dây nâu/dây đỏ/dây cam nào dưới đây là đúng ?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId150.png)

A/ GN

D/ 5V/D2 → D13

B/ 5V/GN

D/ D2→D13

C/ D2→D1

3/ GN

D/ 5V

D/ D2→D1

3/ 5V/GND

Câu 35 (Nhận biết)

Trong breadboard, các dây điện được nối với nhau như thế nào?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId151.png)

A/

Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng ngang được cách điện với hàng còn lại. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột dọc được cách điện với các cột còn lại.

B/

Khu vực A và D các lỗ được nối theo cột dọc, mỗi cột được cách điện với cột còn lại. Khu vực B và C các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với các hàng còn lại.

C/

Khu vực A và D các lỗ được nối theo hàng ngang và theo từng cặp, 5 cặp theo hàng là cách điện nhau . Khu vực B và C các lỗ được nối theo cột, mỗi cột được cách điện với các cột còn lại.

D/

Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với hàng còn lại và bắt buộc phải nối thiết bị theo cực (+) và cực (-) đã ký hiệu. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột được cách điện với các cột còn lại.

Câu 36 (Nhận biết)

Để cảm biến hồng ngoại có thể hoạt động được thì cần phải cung cấp điện áp bao nhiêu V?

A/ Từ 3,3V đến 5V.

B/ 3,3V.

C/ 5V.

D/ 3V.

Câu 37 (Nhận biết)

Cách điều chỉnh độ nhạy của các loại cảm biến là:

A/ Dùng băng keo dán lên mặt tấm cảm biến.

Dùng tua vít điều chỉnh biến trở (núm vặn màu xanh) trên cảm biến.

B/

C/

Nối chân VCC của cảm biến với chân 3,3V để giảm điện áp của cảm biến.

D/

Nối chân GND của cảm biến với chân 3,3V để giảm mức chênh lệch điện áp so với chân VC

C.

Câu 38 (Nhận biết)

Cách lắp mạch nào dưới đây là đúng?

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId152.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId153.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId154.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId155.png)

Câu 39 (Nhận biết)

Joystick gồm có bao nhiêu chân kết nối?

A/ 5

B/ 4

C/ 3

D/ 2

Câu 40 (Nhận biết)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId156.png)

Nối chân kết nối của cảm biến siêu âm ở cột trái với chức năng ở cột phải sao cho phù hợp

(Dạng ghép nối)

Đáp án

### Table Data

| Cột trái  | Cột phải  |
| Chân VCC  | Chân cấp nguồn dương cho cảm biến  |
| Chân GND  | Chân GND sẽ được nối vào cực âm của nguồn điện hoặc chân GND của arduino  |
| Chân Trig  | Chân liên kết đến mắt trái của cảm biến siêu âm, dùng để phát tín hiệu  |
| Chân Echo  | Chân liên kết đến mắt phải của cảm biến siêu âm, nhận tín hiệu  |

Câu 41 (Nhận biết)

Khi núm điều khiển trên Joystick được gạt sang trái, giá trị X sẽ thay đổi vào khoảng bao nhiêu?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId157.png)

A/ từ 512 về 0

B/ từ 512 đến 1023

C/ từ -512 đến 0

D/ Từ -512 đến

Câu 42 (Nhận biết)

Điện áp đầu ra tối đa của mạch L298 là bao nhiêu?

A/ 5V

B/ 3,3V

C/ 3V

D/ 12V

Câu 43 (Hiểu)

Vì sao người ta thường hạn chế sử dụng hai chân số 0 (RX) và 1 (TX) để lấy tín hiệu Digital?

A/

Hai chân 0 và 1 là hai chân giao tiếp dùng cho Arduino truyền và nhận dữ liệu nên rất dễ bị nhiễu nếu ta dùng hai chân này như các chân digital thông thường.

B/

Trên phần chân digital có tổng cộng 14 chân nên không cần phải sử dụng đến hai chân 0 và

1.

C/

Hai chân 0 và 1 dùng để reset chương trình cho Arduino nên không sử dụng hai chân này.

D/

Hai chân 0 và 1 chỉ dùng cho cảm biến mưa nên phải hạn chế dùng cho các loại cảm biến khác.

Câu 44 (Hiểu)

Đoạn chương trình nào dưới đây lập trình tạo hiệu ứng 2 đèn sáng tắt luân phiên liên tục như đoạn gif dưới đây (thời gian sáng, tắt mỗi đèn là 0.5 giây)?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId19.gif)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId158.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId159.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId160.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId161.png)

Câu 45 (Vận dụng)

Quan sát mạch điện dưới đây và điền số thích hợp vào chỗ trống theo thứ tự từ trên xuống dưới trong đoạn chương trình sao cho các đèn led có hiệu ứng giống đèn giao thông (Led xanh sáng trong 7 giây, Led vàng sáng trong 2 giây, Led đỏ sáng trong 5 giây) ?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId162.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId163.png)

A/ 8 - 9 - 5

B/ 8 -10 - 5

C/ 9 -8 - 2

D/ 9 - 10 - 2

Câu 46 (Hiểu)

Cho mạch điện gồm 2 đèn LED xanh, đỏ và yêu cầu lập trình như sau:

Khi khởi động, 2 đèn LED xanh, đỏ lặp lại 5 lần hành động 2 đèn LED sáng tắt luân phiên mỗi 1 giây. (Khi đèn xanh sáng thì đèn đỏ tắt và ngược lại). Sau 5 lần sáng tắt luân phiên, đèn xanh sáng mãi mãi, trong khi đèn đỏ tắt.

Cho đoạn chương trình như sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId164.png)

Biết rằng các chân tín hiệu được nối như bảng bên dưới.

Linh kiện điện tử

Arduino

Chân dương của đèn LED xanh

D9

Chân dương của đèn LED đỏ

D10

Phần chương trình 1, 2 còn thiếu lần lượt là gì để có thể thực hiện yêu cầu trên.

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId165.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId166.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId167.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId168.png)

Câu 47 (Vận dụng)

Chọn chương trình đúng với mô tả sau: Khi Arduino khởi động, động cơ Servo ở góc 0 độ, đèn LED sáng. Sau 2 giây, động cơ Servo ở góc 180 độ, đèn LED tắt. Sau 2 giây, trở lại trạng thái như khi Arduino khởi động.

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId169.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId170.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId171.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId172.png)

Câu 48 (Hiểu)

Một bạn học sinh mắc mạch gồm Arduino, 5 đèn Led và Breadboard, (quy ước các chân đèn Led được minh họa như hình dưới đây)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId24.png)

Biết rằng các chân tín hiệu được nối như bảng bên dưới.

### Table Data

| Linh kiện điện tử  | Arduino  |
| Chân dương của đèn LED đỏ  | D12  |
| Chân dương của đèn LED xanh lá  | D11  |
| Chân dương của đèn LED xanh dương  | D10  |
| Chân dương của đèn LED xám  | D9  |
| Chân dương của đèn LED vàng  | D8  |

Hỏi khi bạn thực hiện chương trình sau thì có những đèn nào phát sáng ?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId25.png)

A/ Chỉ đèn xanh dương sáng

B/ Chỉ có đèn xanh dương và đèn đỏ sáng

C/ Chỉ có đèn đỏ, đèn xanh lá cây và đèn xám sáng

D/ Chỉ có đèn vàng không sáng.

Câu 49 (Vận dụng)

Giáo viên cho đoạn chương trình sau và yêu cầu học sinh lắp mạch gồm 1 cảm biến hồng ngoại, 1 breadboard, 1 đèn led hoạt động như sau:

Khi có vật cản thì đèn led sáng

Khi không có vật cản thì đèn led tắt

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId173.png)

Một học sinh thực hiện lắp mạch như sau và mạch không hoạt động theo yêu cầu của giáo viên. Hỏi học sinh đã lắp mạch sai ở đâu ?  (Nhiều đáp án)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId174.png)

A/ Chân dương của đèn Led

B/ Chân GND của cảm biến

C/ Chân OUT của cảm biến

D/ Chân VCC của cảm biến

Câu 50 (Hiểu)

Yêu cầu lập trình cho cảm biến hồng ngoại, đèn Led và còi hoạt động như sau:
- Khi không có vật cản, đèn xanh sáng, đèn đỏ tắt, còi tắt.
- Khi có vật cản, còi kêu, đèn đỏ sáng và đèn xanh sáng tắt luân phiên với nhau.

Biết các chân tín hiệu được nối như bảng bên dưới.

### Table Data

| Linh kiện điện tử  | Arduino  |
| Chân DO của cảm biến hồng ngoại  | D7  |
| Chân dương của còi buzzer  | D12  |
| Chân dương của đèn xanh  | D8  |
| Chân dương của đèn đỏ  | D9  |

Phát biểu nào sau đây là đúng khi nói về đoạn chương trình sau đây.

(Nhiều đáp án)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId175.png)

A/ Câu lệnh điều kiện ở dòng (

Câu lệnh điều kiện ở dòng (5) dùng sai chân pin DO của cảm biến hồng ngoại

B/ và (5) với nhau.

1)

và (5) xét sai điều kiện có/không có người của cảm biến siêu âm, cần đảo 2 giá trị 1, 0 ở 2 phần (

1)

C/

Khi có vật cản, thiếu câu lệnh cho đèn Led xanh sáng khi làm hiệu ứng 2 đèn sáng tắt luân phiên, cần thêm một câu lệnh làm đèn xanh sáng ở giữa dòng (9) và (10).

D/

Câu lệnh (6), (8), (10) dùng sai chân pin của còi buzzer và đèn LED đỏ. Chân pin ở câu lệnh (6) có chân pin là 9, câu lệnh (8), (10) có chân pin là 1

2.

E/

Chương trình không hoạt động được, phải sử dụng câu lệnh if...then...else thay cho câu lệnh if...then.

Câu 51 (Vận dụng)

Yêu cầu lập trình cho cảm biến hồng ngoại như sau:

Khi phát hiện vật cản thì cho đèn Led được nối với chân D8 sáng.

Không có vật cản thì cho đèn Led đó tắt.

Hỏi đoạn chương trình nào dưới đây cho kết quả đúng với yêu cầu của giáo viên, biết chân DO của cảm biến được nối với chân D7.

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId31.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId32.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId33.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId34.png)

Câu 52 (Vận dụng)

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

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId176.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId177.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId178.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId179.png)

Câu 53 (Hiểu)

Mạch điện gồm cảm biến mưa, đèn led và còi buzzer được nối như sau:

### Table Data

| Tên linh kiện  | Chân kết nối của linh kiện  | Chân kết nối của Arduino  |
| Cảm biến mưa  | VCC  | 5V  |
| Cảm biến mưa  | GND  | GND  |
| Cảm biến mưa  | D0  | D8  |
| Đèn Led xanh  | Chân dương  | D7  |
| Đèn Led xanh  | Chân âm  | GND  |
| Đèn Led đỏ  | Chân dương  | D6  |
| Đèn Led đỏ  | Chân âm  | GND  |
| Còi buzzer  | Chân dương  | D5  |
| Còi buzzer  | Chân âm  | GND  |

Chọn đáp án mô tả đúng nhất của đoạn chương trình sau

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId38.png)

Khi  ___ thì đèn xanh sáng, đèn đỏ và còi tắt. Khi  ___ thì đèn đỏ sáng lên, trong khi đèn xanh ___ , sau đó còi buzzer báo động hú tắt liên tục (thời gian hú tắt đứt quãng là 1 giây) cho đến khi  ___ thì dừng lại.

A/ trời không mưa - trời mưa - tắt - trời không mưa

trời không mưa - trời mưa - sáng trong 3 giây rồi tắt - trời không mưa

B/ trời mưa - trời không mưa - tắt - trời không mưa

trời mưa - trời không mưa - sáng trong 3 giây rồi tắt - trời mưa

C/

D/

Câu 54 (Hiểu)

Đoạn lệnh nào sau đây làm cho màn hình LCD hiện lên dòng chữ như sau?

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId59.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId180.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId181.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId182.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId183.png)

Câu 55 (Hiểu)

Cho đoạn lệnh và yêu cầu như sau:

Yêu cầu

- Mạch điện Arduino gồm 1 cảm biến mưa, 2 đèn LED đỏ, xanh và 1 cảm biến mưa.

- 2 đèn LED đỏ, xanh: 
  + Đèn xanh luôn bật cho thấy chương trình có hoạt động.

+ Khi có mưa, đèn đỏ sáng. Khi không có mưa, đèn đỏ tắt.
- Màn hình LCD:
  + Khi có mưa, màn hình hiển thị “CO MUA”
  + Khi không có mưa, màn hình hiển thị “KHONG CO MUA”

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId184.png)

Với đoạn lệnh như trên, hãy lựa chọn đáp án thể hiện đúng các chân thiết bị so với yêu cầu như trên.
(Dạng ghép nối)

Đáp án

### Table Data

| Cột trái  | Cột phải  |
| Chân dương đèn LED đỏ  | D13  |
| Chân dương đèn LED xanh  | D12  |
| Chân DO/OUT của cảm biến mưa  | D9  |
| Chân SDA của màn hình LCD      | A4  |
| Chân SCL của màn hình LCD    | A5  |
|   | A0  |
|   | A1  |
|   | A2  |
|   | A3  |
|   | Chân Analog bất kỳ  |
|   | Chân Digital bất kỳ  |

Câu 56 (Hiểu)

Quan sát mạch điện dưới đây và chọn đoạn chương trình khi thực hiện thì động cơ dừng lại ? Nhiều đáp án

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId185.png)

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId186.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId187.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId188.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId189.png)

Câu 57 (Hiểu)

Cho sơ đồ nối mạch dưới đây, đoạn chương trình nào cho kết quả quan sát được khi khoảng cách của cảm biến siêu âm nhỏ hơn 30cm, đèn LED sáng nhấp nháy, ngược lại thì đèn LED tắt.

### Table Data

| Thiết bị/linh kiện  | Chân kết nối của thiết bị/linh kiện  | Chân kết nối của Arduino  |
| Cảm biến siêu âm  | VCC  | 5V  |
| Cảm biến siêu âm  | GND  | GND  |
| Cảm biến siêu âm  | Trig  | 10  |
| Cảm biến siêu âm  | Echo  | 9  |
| LED  | Chân dương  | 8  |
| LED  | Chân âm  | GND  |

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId190.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId191.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId192.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId193.png)

Câu 58 (Hiểu)

Cho mạch điện Arduino gồm 1 joystick và 1 đèn LED như sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId194.png)

Cho yêu cầu lập trình như sau:

- Khi cần gạt joystick nằm ở vị trí trung tâm, không di chuyển, đèn LED sẽ tắt.
- Khi gạt joystick đến vị trí bất kỳ, đèn LED sẽ sáng.
- Chương trình lặp lại mãi mãi.

Một học sinh lập trình như sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId195.png)

Hãy chọn đoạn lệnh còn thiếu để điền vào chỗ trống để lập trình được yêu cầu trên.

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId196.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId197.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId198.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId199.png)

Câu 59 (Vận dụng)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId99.png)

Điều khiển 3 đèn LED bằng joystick theo yêu cầu sau:

- Khi kéo joystick theo hướng ngang, qua trái, đèn LED đỏ sẽ sáng, đèn vàng, cam tắt.

- Khi để joystick ở vị trí cân bằng, đèn LED cam sẽ sáng, đèn đỏ, vàng tắt.

- Khi kéo joystick theo hướng ngang, qua phải, đèn LED vàng sẽ sáng, đèn đỏ, cam tắt.

### Table Data

| Thiết bị/linh kiện  | Chân kết nối của thiết bị/linh kiện  | Chân kết nối của Arduino  |
| Joystick  | VCC  | 5V  |
| Joystick  | GND  | GND  |
| Joystick  | VRx  | A0  |
| Joystick  | VRy  | A1  |
| LED vàng  | Chân dương  | D11  |
| LED vàng  | Chân âm  | GND  |
| LED cam  | Chân dương  | D12  |
| LED cam  | Chân âm  | GND  |
| LED đỏ  | Chân dương  | D13  |
| LED đỏ  | Chân âm  | GND  |

Cho đoạn chương trình như sau:

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId200.png)

Hãy điền vào các vị trí trống nội dung thích hợp

(Dạng ghép nối)

Đáp án

### Table Data

| Cột trái  | Cột phải  |
| 1  | 0 (A0)  |
| 2  | OR  |
| 3  | Q > 600  |
| 4  | low  |
| 5  | high  |
| 6  | low  |
|   | AND  |
|   | Q < 300  |
|   | 1 (A  1) |

Câu 60 (Hiểu)

Một học sinh chế tạo một chiếc xe hoạt động bằng Arduino, mạch L298 và động cơ vàng như mạch điện như hình dưới.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId82.png)

Biết rằng sau khi học sinh thử nghiệm chiều xoay của 2 động cơ bằng đoạn lệnh sau, xe đã xoay tròn thuận chiều kim đồng hồ.

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId201.png)

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId202.png)

Hỏi để điều chỉnh cho xe chạy thẳng khi khởi động, ta có thể sử dụng đoạn lệnh nào sau đây?

A/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId86.png)

B/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId88.png)

C/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId87.png)

D/

![Image](../assets/IOT_Arduino_1_2_Arduino_1_Bản_sao_của_Bản_sao_của_Đề_kiểm_tra_Arduino_module_1_rId85.png)

ĐỀ THỰC HÀNH

Yêu cầu:

Thời lượng

1- 2 bài: 120-180 phút

Dự án chứa các kiến thức ở cả module 1 và module 2
Module 1: Có sử dụng 1 trong các loại cảm biến sau: CB hồng ngoại hoặc CB mưa
Module 2: Có sử dụng 2 trong 3 thiết bị sau: LCD hoặc Joystick hoặc động cơ vàng (+L298)

Dự án có ít nhất 2 phần: mạch điện và lập trình

Có thể thêm phần 3: Tinkering nếu muốn

Bài 1:

1. Đề bài:

Lập trình hệ thống gồm 1 cảm biến mưa, 1 còi buzzer và 1 đèn led hoạt động như sau:

Khi phát hiện trời mưa, đèn led nhấp nháy và còi kêu.

Khi không có mưa, đèn và còi không hoạt động.

2. Link file đáp án/ video:

- Tải file offline lên folder Material - Bộ câu hỏi TN, TL

- Đổi tên Môn - Video/Code - Bài n

Bài 2:

1. Đề bài:

Lập trình hệ thống xe điều khiển bằng joystick gồm 2 động cơ vàng (+L298), 1 joystick hoạt động như sau:

Y > 600 → Robot đi lùi, Y < 400 → Robot đi tới

X > 600 → Robot xoay phải, X < 400 → Robot xoay trái

2. Link file đáp án/ video:

Bài 3:

1. Đề bài:

Lập trình, gắn mạch điện gồm 1 cảm biến hồng ngoại, 1 đèn led và 1 còi hoạt động như sau:

Khi phát hiện có người, đèn led sáng nhấp nháy 5 lần và còi kêu báo động.

Khi không phát hiện có người, đèn led tắt và còi tắt.

2. Link file đáp án/ video:

Môn Arduino-Video/code-Bài 3

Bài 4:

1. Đề bài:

Lập trình hệ thống đèn báo hiệu của bãi đỗ xe, gắn mạch điện gồm 1 joystick, 3 đèn led và 1 LCD hoạt động như sau:

- Khi kéo joystick lên trên, đèn LED đỏ sẽ sáng và LCD hiện chữ HẾT CHỖ.

- Khi kéo joystick xuống dưới, đèn LED xanh dương sẽ sáng và LCD hiện CÒN CHỖ .

2. Link file đáp án/ video:

Môn Arduino-Video/code-Bài 4