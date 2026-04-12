# DISTILLED KNOWLEDGE: Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino

Source: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]] — [🚀 Xem RAW](file:///d:/NoteBookLLM_Br/brain/raw/LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md)

---
title: TRI THỨC CHƯNG CẤT - AI ARDUINO ĐỀ 4
source: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]
type: DISTILLED_KNOWLEDGE
---

# PHẦN 1: FACT BANK (KIẾN THỨC CHUẨN)

*   **[LMS] [Fact] :: Kết nối Arduino với máy tính** :: Sử dụng dây cáp USB: Cổng USB-A kết nối với máy tính và cổng USB-B kết nối với mạch Arduino Uno. :: [[Câu 1]]
*   **[LMS] [Fact] :: Điện áp đầu ra Arduino** :: Các cổng Digital của Arduino Uno cung cấp điện áp đầu ra chuẩn là 5V. :: [[Câu 2]]
*   **[LMS] [Fact] :: Cấu tạo LED đơn** :: Đèn LED đơn có hai cực: chân dài là cực dương (+), chân ngắn là cực âm (-). :: [[Câu 3]]
*   **[LMS] [Fact] :: Cấu tạo Còi Buzzer** :: Còi buzzer hoạt động ở điện áp 3V-5V, là thiết bị đầu ra (output). Chân dài là cực dương (+), chân ngắn là cực âm (-). :: [[Câu 5]]
*   **[LMS] [Fact] :: Đấu nối Động cơ rung** :: Dây đỏ (dương) nối với cổng Digital (2-13), dây đen (âm) nối với cổng GND. :: [[Câu 6]]
*   **[LMS] [Fact] :: Đấu nối Động cơ Servo** :: Dây màu cam là dây tín hiệu, kết nối với các chân Digital (2-13). Dây đỏ nối nguồn 5V, dây nâu nối GND. :: [[Câu 7]]
*   **[LMS] [Fact] :: Nguyên lý Breadboard** :: Các lỗ cắm trên cùng một hàng dọc (ở khu vực giữa) hoặc cùng một hàng ngang (ở dải nguồn) được nối thông điện với nhau. :: [[Câu 8]]
*   **[LMS] [Fact] :: Chế độ phát mạch ISD1820** :: Chân PLAYE (Edge trigger) phát hết bản tin dù tín hiệu kích đã tắt; chân PLAYL (Level trigger) chỉ phát khi tín hiệu ở mức cao và dừng khi tín hiệu xuống mức thấp. :: [[Câu 9]]
*   **[LMS] [Fact] :: Quy trình tạo biến trong mBlock** :: Chọn nhóm lệnh Variable -> Nhấn Make a Variable -> Đặt tên biến -> Nhấn OK. :: [[Câu 13]]
*   **[LMS] [Fact] :: Truyền tin (Broadcast) trong mBlock** :: Việc sử dụng khối lệnh Broadcast và Receive để giao tiếp giữa Arduino và nhân vật (Sprite) chỉ thực hiện được ở chế độ LIVE. :: [[Câu 21]]
*   **[LMS] [Fact] :: Dữ liệu nhận diện giọng nói** :: Khối lệnh nhận diện giọng nói (Speech recognition) trong extension Cognitive Services trả về giá trị kiểu Chuỗi (String). :: [[Câu 25]]
*   **[LMS] [Fact] :: Đặc điểm Teachable Machine** :: Là công cụ tạo mô hình máy học (Machine Learning) để phân loại hình ảnh/âm thanh; yêu cầu kết nối Internet và đăng nhập tài khoản mBlock để sử dụng extension. :: [[Câu 28]]

---

# PHẦN 2: TEST BANK (NGÂN HÀNG ĐỀ)

### Question 1: Ta có thể thực hiện cách nào sau đây để kết nối Arduino với máy tính?
A. Kết nối bằng Bluetooth.
B. Kết nối bằng dây điện jumper male-male.
C. Kết nối bằng dây cáp kết nối. Cổng dùng để kết nối với máy tính là cổng USB - A type. Cổng dùng để kết nối với Arduino là cổng USB - B type.
D. Kết nối bằng dây cáp kết nối. Cổng dùng để kết nối với máy tính là cổng USB - B type. Cổng dùng để kết nối với Arduino là cổng USB - C type.
**Correct: C**
**Explanation:** Arduino Uno sử dụng cáp USB chuẩn A-B để giao tiếp với máy tính.

### Question 2: Điện áp đầu ra (output) của các cổng Arduino Uno có thể là bao nhiêu?
A. 5V
B. 4V
C. 7V
D. Tất cả đáp án đều sai
**Correct: A**
**Explanation:** Mức logic HIGH trên các chân Digital của Arduino Uno tương ứng với 5V.

### Question 3: Phát biểu nào sau đây là đúng khi nói về đèn LED đơn?
[![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId6.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId6.png)
A. Đèn LED đơn gồm hai cực âm, dương. Chân dài hơn là chân dương.
B. Đèn LED đơn gồm hai cực âm, dương. Chân ngắn hơn là cực dương.
C. Đèn LED đơn gồm hai cực âm, dương. Chân dài hơn là chân âm.
D. Tất cả các câu trên đều sai.
**Correct: A**
**Explanation:** Theo quy ước linh kiện điện tử, chân dài của LED là cực dương (Anode).

### Question 4: Khối lệnh nào dưới đây dùng để điều khiển đèn led siêu sáng?
A. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId7.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId7.png)
B. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId8.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId8.png)
C. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId9.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId9.png)
D. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId10.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId10.png)
**Correct: A**
**Explanation:** Đèn LED được điều khiển bằng lệnh xuất mức logic (Digital Write) ra chân pin tương ứng.

### Question 5: Khẳng định nào sau đây là SAI?
A. Còi buzzer có điện áp hoạt động từ 3V đến 5V.
B. Còi buzzer là thiết bị output.
C. Còi buzzer có cấu tạo gồm 2 chân; chân dài là chân âm; chân ngắn là chân dương.
D. Còi buzzer là một thiết bị có thể phát ra âm thanh, có khả năng tiếp nhận các loại tín hiệu và chuyển chúng thành tín hiệu âm thanh.
**Correct: C**
**Explanation:** Khẳng định C sai vì chân dài của còi buzzer là chân dương (+).

### Question 6: Để điều khiển động cơ rung qua mạch Arduino ta cần nối mạch điện như thế nào?
A. Dây đỏ của động cơ rung nối với cổng pin digital 2-13; dây đen nối với cổng GND.
B. Dây đỏ của động cơ rung nối với cổng GND; dây đen nối với cổng pin digital 2-13.
C. Dây đỏ của động cơ rung nối với cổng 3,3V hoặc 5V; dây đen nối với cổng GND.
D. Dây đỏ của động cơ rung nối với cổng GND; dây đen nối với cổng 3,3V hoặc 5V.
**Correct: A**
**Explanation:** Dây đỏ là cực dương cần nối vào chân điều khiển (Digital Pin), dây đen là cực âm nối vào GND.

### Question 7: Phát biểu nào sau đây là đúng khi nói về động cơ Servo?
A. Dây màu cam của động cơ Servo được gọi là dây tín hiệu, kết nối với chân Digital 2-13 của Arduino.
B. Dây màu đỏ của động cơ Servo được gọi là dây tín hiệu, kết nối với chân Digital 2-13 của Arduino.
C. Dây màu cam của động cơ Servo được gọi là dây tín hiệu, chỉ có thể kết nối với chân Digital có dấu (~): 3, 5, 6, 9, 10, 11 của Arduino.
D. Dây màu đỏ của động cơ Servo được gọi là dây nguồn, kết nối với chân 5V hoặc GND bất kỳ của Arduino.
**Correct: A**
**Explanation:** Dây cam là dây Signal, có thể kết nối với bất kỳ chân Digital nào từ 2-13 để nhận lệnh PWM.

### Question 8: Nếu nối nguồn điện 5V vào điểm A thì điểm nào trong 4 điểm B,C,D,E cũng có điện?
[![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId11.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId11.png)
A. E
B. D
C. C
D. B
**Correct: D**
**Explanation:** Trên breadboard, các lỗ trong cùng một cột dọc (như A và B) được nối thông với nhau.

### Question 9: Phân biệt sự khác nhau giữa 2 chân PLAYE và PLAYL trong mạch ISD1820:
A. Khi điện áp ở mức cao, PLAYE và PLAYL đều phát nhạc. Tuy nhiên, PLAYE chỉ tắt sau khi phát hết bộ nhớ còn PLAYL tắt khi điện áp ở mức thấp hoặc hết bộ nhớ.
B. Khi điện áp ở mức cao, PLAYE phát nhạc còn PLAYL tắt.
C. Khi điện áp ở mức cao, PLAYE và PLAYL đều phát nhạc. Nếu điện áp ở mức thấp, âm thanh ngừng phát.
D. Khi điện áp ở mức cao, PLAYE và PLAYL đều phát nhạc. Tuy nhiên, PLAYL chỉ tắt sau khi phát hết bộ nhớ còn PLAYE tắt khi điện áp ở mức thấp hoặc hết bộ nhớ.
**Correct: A**
**Explanation:** PLAYE là kích cạnh (phát hết), PLAYL là kích mức (phát khi có điện).

### Question 10: Cho mạch điện Arduino gồm 5 đèn LED và chương trình như hình. Khi chạy chương trình, các đèn LED hoạt động như thế nào?
[![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId12.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId12.png)
[![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId13.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId13.png)
A. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId14.gif)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId14.gif)
B. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId15.gif)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId15.gif)
C. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId16.gif)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId16.gif)
D. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId17.gif)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId17.gif)
**Correct: B**
**Explanation:** Chương trình điều khiển các chân Digital lần lượt sáng rồi tắt tạo hiệu ứng chạy đuổi.

### Question 11: Cho mạch điện Arduino gồm 4 đèn LED. Các cặp đèn LED nào sẽ hoạt động giống nhau khi được lập trình?
[![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId18.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId18.png)
A. Đỏ - xanh lá, vàng - xanh dương
B. Đỏ - xanh dương, vàng - xanh lá
C. Đỏ - vàng, xanh lá - xanh dương
D. Đỏ