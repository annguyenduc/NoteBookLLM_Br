# DISTILLED KNOWLEDGE: Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino

Source: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]] — [🚀 Xem RAW](file:///d:/NoteBookLLM_Br/brain/raw/LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md)

# DISTILLED KNOWLEDGE: TỰ ĐỘNG HÓA VÀ IOT AI ARDUINO - ĐỀ 1

---

## PHẦN 1: FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact] :: Kết nối vật lý Arduino** :: Để kết nối Arduino với máy tính, sử dụng cáp USB với đầu USB-A cắm vào máy tính và đầu USB-B cắm vào board Arduino. :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Chế độ Live (Trực tiếp)** :: Chế độ Live trong mBlock5 chỉ hoạt động khi phần mềm đang mở và duy trì kết nối liên tục với board Arduino. :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Chế độ Upload (Tải lên)** :: Sau khi tải chương trình ở chế độ Upload, chương trình được lưu vào bộ nhớ Arduino và vẫn hoạt động ngay cả khi ngắt kết nối với máy tính (chỉ cần cấp nguồn). :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Phân cực LED siêu sáng** :: Chân dương (+) của đèn LED siêu sáng thường được đánh dấu bằng một lỗ nhỏ trên thân đèn, chân âm (-) không có. :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Mạch ISD1820 - Chân REC** :: Chân REC (Record) của mạch thu phát âm thanh ISD1820 được kết nối với các cổng Digital (từ 2 đến 13) trên Arduino để điều khiển ghi âm. :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Mạch ISD1820 - Chế độ PLAYE** :: Chức năng PLAYE (Play Edge) sẽ phát toàn bộ đoạn âm thanh đã ghi cho đến khi kết thúc, ngay cả khi tín hiệu kích hoạt bị ngắt giữa chừng. :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Động cơ Servo - Sơ đồ dây** :: Dây màu cam là dây tín hiệu (nối chân Digital PWM có dấu ~), dây màu đỏ là dây nguồn (nối 5V), dây màu nâu là dây mass (nối GND). :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Cấu tạo Breadboard** :: Các lỗ ở khu vực giữa (B hoặc C) được kết nối theo hàng dọc (mỗi cột 5 lỗ thông nhau). :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Khối lệnh Broadcast** :: Việc truyền (Broadcast) và nhận tin nhắn (Receive) giữa thiết bị Arduino và nhân vật chỉ thực hiện được trong chế độ Live. :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Extension Cognitive Services** :: Các lệnh "Recognize" (nhận diện giọng nói/hình ảnh) có giới hạn số lần sử dụng trong ngày và yêu cầu kết nối Internet. :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]
*   **[LMS] [Fact] :: Quy trình Teachable Machine** :: Thứ tự sử dụng: Thêm Extension -> Training model -> Build a new model -> Cung cấp hình ảnh/dữ liệu -> Learn -> Use the model. :: [[LMS_RAW_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]

---

## PHẦN 2: TEST BANK (Ngân hàng đề)

### Question 1: Ta có thể thực hiện cách nào sau đây để kết nối Arduino với máy tính?
A. Kết nối bằng dây cáp kết nối. Cổng dùng để kết nối với máy tính là cổng USB - A type. Cổng dùng để kết nối với Arduino là cổng USB - B type.
B. Kết nối bằng Bluetooth.
C. Kết nối bằng dây điện jumper male-male.
D. Kết nối bằng dây cáp kết nối. Cổng dùng để kết nối với máy tính là cổng USB - B type. Cổng dùng để kết nối với Arduino là cổng USB - C type.
**Correct:** A
**Explanation:** Arduino Uno sử dụng cáp USB chuẩn A-B để giao tiếp với máy tính.

### Question 2: Phát biểu nào sau đây là đúng khi nói về chế độ Live và chế độ Upload khi lập trình Arduino trên mBlock5?
A. Chế độ Live chỉ hoạt động trong quá trình mở mBlock5 và kết nối với board Arduino.
B. Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta ngắt kết nối giữa hai thiết bị, chương trình được tải lên sẽ bị xóa khỏi bộ nhớ của Arduino.
C. Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta xóa câu lệnh ở khu vực lập trình, chương trình hoạt động của Arduino sẽ bị thay đổi ngay lập tức.
D. Với chế độ Live, ta có thể thấy trực tiếp chương trình đang chạy đến khối lệnh nào khi chọn “Setting - Update firmware - OK”.
**Correct:** A
**Explanation:** Chế độ Live yêu cầu sự tương tác thời gian thực giữa phần mềm và phần cứng.

### Question 3: Khối lệnh nào sau đây không thể sử dụng được trong việc lập trình Arduino bằng chế độ Live?
A. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId7.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId7.png)
B. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId8.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId8.png)
C. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId9.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId9.png)
D. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId10.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId10.png)
**Correct:** A
**Explanation:** Khối lệnh "When Arduino starts up" chỉ dành cho chế độ Upload.

### Question 4: Ta có thể phân biệt được chân dương, chân âm của đèn LED siêu sáng bằng cách nào?
A. Phần chân âm của đèn LED siêu sáng được đánh dấu bằng một lỗ nhỏ, chân dương không có.
B. Phần chân âm của đèn LED siêu sáng dài hơn chân dương.
C. Phần chân dương của đèn LED siêu sáng có màu sáng hơn chân âm.
D. Phần chân dương của đèn LED siêu sáng được đánh dấu bằng một lỗ nhỏ, chân âm không có.
**Correct:** D
**Explanation:** Đây là đặc điểm nhận dạng vật lý của LED siêu sáng trong bộ kit.

### Question 5: Khối lệnh nào sau đây được sử dụng để điều khiển việc hoạt động/tắt của động cơ rung 0834 3-5V?
A. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId11.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId11.png)
B. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId12.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId12.png)
C. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId13.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId13.png)
D. [![Image](../assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId14.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino_rId14.png)
**Correct:** A
**Explanation:** Động cơ rung được điều khiển như một thiết bị đầu ra kỹ thuật số (Digital Output) bằng lệnh set digital pin.

### Question 6: Phát biểu nào sau đây là đúng nói về các chân kết nối của mạch thu phát âm thanh ISD1820?
A. Chân REC của mạch được gắn với cổng Digital 2-13 của Arduino.
B. Chân VCC của mạch được gắn với cổng GND của Arduino.
C. Chân GND của mạch được gắn với cổng 5V của Arduino.
D. Chân PLAYE, PLAYL của mạch chỉ có thể được gắn ở một số chân Digital không có dấu ngã (~): 2, 4, 7, 8, 12, 13.
**Correct:** A
**Explanation:** Chân REC nhận tín hiệu mức cao để bắt đầu ghi âm.

### Question 7: Phát biểu nào sau đây là đúng khi nói về chức năng PLAYE và PLAYL của mạch thu phát âm thanh ISD1820?
A. Cả 3 đáp án còn lại đều đúng.
B. Khi nhấn và giữ nút nhấn, điện áp ở chân kết nối đang ở mức cao. Khi không nhấn nút, điện áp ở chân kết nối ở mức thấp.
C. Chức năng PLAYE sẽ phát đoạn âm thanh được ghi lại