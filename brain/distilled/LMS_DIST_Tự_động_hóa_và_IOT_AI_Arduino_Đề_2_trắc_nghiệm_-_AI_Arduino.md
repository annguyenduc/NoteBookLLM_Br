# DISTILLED KNOWLEDGE: Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino

Source: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino.md]] — [🚀 Xem RAW](file:///d:/NoteBookLLM_Br/brain/raw/LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino.md)

# DISTILLED KNOWLEDGE: TỰ ĐỘNG HÓA VÀ IOT - AI ARDUINO (ĐỀ 2)

## PHẦN 1: FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact] :: Cách cấp nguồn cho Arduino Uno** :: Arduino Uno có thể được cấp nguồn qua cổng USB (kết nối máy tính), Jack DC (adapter 7-12V), hoặc qua chân Vin. Các chân 5V và 3.3V trên board là các chân đầu ra nguồn (output), không dùng để cấp nguồn đầu vào cho board (ngoại trừ các trường hợp kỹ thuật đặc thù nhưng không khuyến khích cho người mới). :: [[Câu 1]]
*   **[LMS] [Fact] :: Chế độ Live và Upload trong mBlock5** :: Chế độ Live cho phép tương tác thời gian thực giữa máy tính và Arduino nhưng yêu cầu kết nối liên tục. Chế độ Upload nạp chương trình trực tiếp vào bộ nhớ Flash của Arduino, giúp board hoạt động độc lập sau khi ngắt kết nối với máy tính. :: [[Câu 3]]
*   **[LMS] [Fact] :: Cấu tạo LED siêu sáng** :: Đèn LED có tính phân cực: Chân dài là chân Dương (+/Anode), chân ngắn là chân Âm (-/Cathode). :: [[Câu 4]]
*   **[LMS] [Fact] :: Điều khiển Động cơ rung 0834** :: Động cơ rung hoạt động dựa trên tín hiệu Digital. Sử dụng khối lệnh `set digital pin [ ] output [high/low]` để bật hoặc tắt động cơ. :: [[Câu 5]]
*   **[LMS] [Fact] :: Mạch thu phát âm thanh ISD1820** :: Chân VCC nối 5V, GND nối GND. Chân REC dùng để điều khiển ghi âm, chân PLAYE/PLAYL dùng để điều khiển phát lại thông qua các chân Digital trên Arduino. :: [[Câu 6, 7]]
*   **[LMS] [Fact] :: Đặc điểm Động cơ Servo** :: Servo là thiết bị đầu ra (Output), có 3 chân kết nối (Tín hiệu - Cam, Nguồn 5V - Đỏ, Đất GND - Nâu). Servo thường được điều khiển theo góc (0 - 180 độ). :: [[Câu 8]]
*   **[LMS] [Fact] :: Quy tắc kết nối Breadboard** :: Trên Breadboard (loại phổ biến), các lỗ ở khu vực giữa (A, B, C, D...) được kết nối với nhau theo hàng dọc (mỗi cột 5 lỗ là một mạch chung). :: [[Câu 9]]
*   **[LMS] [Fact] :: Cơ chế Broadcast trong mBlock** :: Khối lệnh "Broadcast" (Phát tin) và "When I receive" (Khi nhận tin) cho phép truyền tín hiệu qua lại giữa các nhân vật (Sprites) và thiết bị (Devices) khi ở chế độ Live. :: [[Câu 21]]
*   **[LMS] [Fact] :: Extension Cognitive Services** :: Đây là nhóm lệnh AI dùng để nhận diện giọng nói, hình ảnh, văn bản. Các lệnh "Recognize" yêu cầu kết nối Internet và có giới hạn số lần sử dụng trong ngày. :: [[Câu 25]]
*   **[LMS] [Fact] :: Extension Teachable Machine** :: Cho phép người dùng huấn luyện các mô hình máy học (Machine Learning) trực tiếp. Để sử dụng hiệu quả trong mBlock, người dùng cần đăng nhập và có kết nối mạng để tải mô hình. :: [[Câu 28]]

---

## PHẦN 2: TEST BANK (Ngân hàng đề)

### Question 1: Khẳng định nào dưới đây là SAI?
A. Có thể cấp nguồn cho arduino thông qua pin với chân 3,3V hoặc 5V.
B. Có thể cấp nguồn cho arduino bằng cách kết nối với máy tính thông qua dây cáp.
C. Có thể cấp nguồn cho arduino thông qua dây adapter 9V.
D. Có thể cấp nguồn cho arduino thông qua pin với cổng Vin.
**Correct:** A
**Explanation:** Chân 3.3V và 5V trên Arduino là các chân cấp nguồn ra cho linh kiện, không phải chân nhận nguồn vào để nuôi board mạch.

### Question 2: Nối tên với các bộ phận tương ứng trên board Arduino Uno
[![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId7.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId7.png)
A. Nút reset
B. Cổng USB - type B
C. Jack DC
D. Các chân nguồn
E. Các chân pin (chân tín hiệu)
**Correct:** (Theo thứ tự chỉ dẫn trên hình ảnh thực tế của board Arduino)

### Question 3: Phát biểu nào sau đây là đúng khi nói về chế độ Live và chế độ Upload khi lập trình Arduino trên mBlock5?
A. Chế độ Live chỉ hoạt động trong quá trình mở mBlock5 và kết nối với board Arduino.
B. Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta ngắt kết nối giữa hai thiết bị, chương trình được tải lên sẽ bị xóa khỏi bộ nhớ của Arduino.
C. Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta xóa câu lệnh ở khu vực lập trình, chương trình hoạt động của Arduino sẽ bị thay đổi ngay lập tức.
D. Với chế độ Live, ta có thể thấy trực tiếp chương trình đang chạy đến khối lệnh nào khi chọn “Setting - Update firmware - OK”.
**Correct:** A
**Explanation:** Chế độ Live yêu cầu duy trì kết nối với phần mềm. Chế độ Upload lưu chương trình vào bộ nhớ vĩnh viễn của chip cho đến khi có chương trình mới ghi đè lên.

### Question 4: Ta có thể phân biệt được chân dương, chân âm của đèn LED siêu sáng bằng cách nào?
[![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId8.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId8.png)
A. Phần chân âm của đèn led có dấu (-); chân dương của đèn led có dấu (+).
B. Phần chân âm của đèn led dài hơn; chân dương của đèn led ngắn hơn.
C. Phần chân dương của đèn led được đánh dấu bằng một lỗ tròn nhỏ, chân âm không có.
D. Phần chân dương của đèn led dài hơn; chân âm của đèn led ngắn hơn.
**Correct:** D
**Explanation:** Quy ước chuẩn của LED đơn: chân dài là cực Dương (+), chân ngắn là cực Âm (-).

### Question 5: Khối lệnh nào sau đây được sử dụng để điều khiển việc hoạt động/tắt của động cơ rung 0834 3-5V?
A. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId9.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId9.png)
B. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId10.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId10.png)
C. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId11.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId11.png)
D. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId12.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId12.png)
**Correct:** A
**Explanation:** Động cơ rung được điều khiển bằng mức điện áp High/Low tại chân Digital.

### Question 6: Phát biểu nào sau đây là SAI khi nói về các chân kết nối của mạch thu phát âm thanh ISD1820?
A. Chân REC của mạch được gắn với cổng Digital 13 của Arduino. PLAYE, PLAYL của mạch chỉ có thể được bật bằng cách nhấn nút thủ công.
B. Chân PLAYE, PLAYL của mạch chỉ có thể được gắn ở một số chân Digital không có dấu ngã (~): 2, 4, 7, 8, 12, 13.
C. Chân VCC của mạch được gắn với cổng 5V của Arduino.
D. Chân GND của mạch được gắn với cổng GND của Arduino.
**Correct:** A
**Explanation:** Các chân PLAYE, PLAYL hoàn toàn có thể điều khiển bằng lập trình thông qua các chân Digital của Arduino, không bắt buộc phải nhấn thủ công.

### Question 7: Phát biểu nào sau đây là SAI khi nói về các chân kết nối của mạch thu phát âm thanh ISD1820? (Câu hỏi lặp lại với các phương án tương tự)
**Correct:** A

### Question 8: Phát biểu nào sau đây là sai khi nói về động cơ Servo?
A. Servo là thiết bị input.
B. Dây màu cam của động cơ Servo được gọi là dây tín hiệu, kết nối với chân Digital.
C. Servo là thiết bị có 2 chân kết nối.
D. Điện áp hoạt động của servo là 5V.
**Correct:** C (và A cũng sai)
**Explanation:** Servo là thiết bị Output (đầu ra) và có 3 chân kết nối (Tín hiệu, VCC, GND).

### Question 9: Phát biểu nào sau đây là đúng khi nói về cách kết nối các lỗ trên Breadboard?
[![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId13.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId13.png)
A. Các lỗ ở khu vực B hoặc C được kết nối theo hàng dọc, mỗi cột 5 lỗ được kết nối với nhau.
B. Các lỗ ở khu vực A hoặc D được kết nối theo hàng dọc, mỗi cột 2 lỗ được kết nối với nhau.
C. Các lỗ ở khu vực B hoặc C được kết nối theo hàng ngang, mỗi hàng 30 lỗ được kết nối với nhau.
D. Tất cả các lỗ ở khu vực B hoặc C được kết nối với nhau theo hàng ngang và hàng dọc.
**Correct:** A
**Explanation:** Ở khu vực giữa của Breadboard, các lỗ được nối thông với nhau theo từng cột dọc 5 lỗ.

### Question 10: Cách kết nối mạch thu phát âm thanh ISD1820 với Arduino, cách kết nối nào sau đây là sai?
A. ![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_ng