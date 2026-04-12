# TEST BANK: Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.md

### Question: Tính năng nào sau đây KHÔNG được tích hợp trên Halocode?
A. Giao tiếp không dây Bluetooth
B. Giao tiếp không dây WiFi
C. Bộ cảm biến đa năng
D. Tích hợp microphone thu nhận giọng nói
**Correct:** C
**Explanation:** Halocode tích hợp sẵn WiFi, Bluetooth, Mic và một số cảm biến cụ thể (chuyển động, chạm), nhưng không gọi là một "bộ cảm biến đa năng" (thường dùng để chỉ các module rời tích hợp nhiều loại cảm biến môi trường như nhiệt độ, độ ẩm, áp suất cùng lúc).

### Question: Sắp xếp các bước theo trình tự thích hợp để điều khiển Halocode bằng chế độ Upload mode với phần mềm mblock.
1. Chuyển chế độ “Live” sang “Upload”.
2. Lựa chọn thiết bị cần sử dụng là Halocode ở dấu “+” khu vực thiết bị.
3. Mở phần mềm mBlock, dùng dây USB kết nối Halocode với máy tính.
4. Chọn “Connect”, cửa sổ hiện lên chọn cổng kết nối và chọn “connect”.
5. Lập trình câu lệnh
6. Nhấn Upload để tải câu lệnh từ máy tính sang Halocode
A. 3-2-4-1-5-6
B. 2-3-4-5-1-6
C. 4-2-3-5-6-1
D. 3-4-2-6-5-1
**Correct:** A
**Explanation:** Quy trình chuẩn: Kết nối vật lý -> Chọn thiết bị trên phần mềm -> Kết nối cổng COM -> Chuyển chế độ nạp code -> Viết code -> Nạp code.

### Question: Đèn LED RGB số 8 của Halocode nằm ở vị trí nào sau đây?
![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image29.png)
A. D
B. B
C. A
D. C
**Correct:** D
**Explanation:** Đèn LED trên Halocode được đánh số từ 1-12 theo chiều kim đồng hồ, bắt đầu từ vị trí gần cổng USB hoặc dấu chỉ định. Vị trí C tương ứng với đèn số 8.

### Question: Nhóm lệnh nào sau đây có chức năng thay đổi màu đèn của vòng đèn LED?
A. ![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image37.png)
B. ![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image108.png)
C. ![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image71.png)
D. ![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image45.png)
**Correct:** A
**Explanation:** Nhóm lệnh Lighting (Chiếu sáng) chứa các khối lệnh điều khiển màu sắc LED.

### Question: Nhóm lệnh nào sau đây có chức năng điều khiển góc quay của động cơ Servo?
A. ![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image63.png)
B. ![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image8.png)
C. ![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image55.png)
D. ![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image47.png)
**Correct:** B
**Explanation:** Lệnh điều khiển Servo nằm trong nhóm mở rộng hoặc nhóm Pins, có tham số góc quay (degree).

### Question: Chọn các bộ phận với vị trí tương ứng của nó trên cảm biến hồng ngoại. (Dạng ghép nối)
![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_nghiệm_-_Halocode.docx_image20.png)
1- Đèn LED hồng ngoại để phát tín hiệu
2- Đèn báo có vật cản
3- Các chân kết nối với Halocode
4- Đèn báo có nguồn điện
5- Biến trở điều chỉnh khoảng cách đo của cảm biến hồng ngoại tới vật cản
6- Đèn LED dùng để thu tín hiệu hồng ngoại
**Correct:** (Thực hiện ghép nối theo cấu tạo cảm biến IR)
**Explanation:** 1-LED phát (trong suốt), 6-LED thu (đen), 5-Biến trở (núm xoay), 2&4-Đèn báo nhỏ trên mạch, 3-Chân cắm (VCC, GND, OUT).

### Question: Khối lệnh nào sau đây sử dụng chức năng của cảm biến nghiêng trên Halocode?
A. ![image](assets/Tự_động_hóa_và_IOT_Halocode_Đề_4_trắc_