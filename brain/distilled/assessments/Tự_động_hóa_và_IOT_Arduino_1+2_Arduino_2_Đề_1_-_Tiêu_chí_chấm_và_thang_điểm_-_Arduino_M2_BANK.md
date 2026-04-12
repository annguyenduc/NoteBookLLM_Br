# TEST BANK: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.md

### Question: 
Lập trình, gắn mạch điện và chế tạo xe điều khiển từ xa kết hợp thu thập dữ liệu nhiệt độ, độ ẩm với các yêu cầu sau:
1. Sử dụng mạch L298 điều khiển 2 động cơ vàng di chuyển: Tiến (phím 2), Lùi (phím 8), Xoay trái (phím 4), Xoay phải (phím 6), Dừng (phím 5) qua Remote hồng ngoại.
2. Hiển thị dữ liệu DHT11 lên LCD 16x2 I2C: Dòng 1 hiển thị "N.do: [giá trị] do C", Dòng 2 hiển thị "Do am: [giá trị] %".
3. Hệ thống cảnh báo bằng 3 LED:
   - LED 1: Sáng khi khởi động thành công.
   - LED 2 (Đỏ): Sáng khi nhiệt độ ngoài khoảng 25-35°C.
   - LED 3 (Xanh dương): Sáng khi độ ẩm ngoài khoảng 40-70%.
4. Yêu cầu phần cứng: Nguồn 2 đế pin 4 mắc song song, có mái che bảo vệ linh kiện khi phun sương.

![image1.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.docx_image1.png)

A. Kết nối LCD SDA-A5, SCL-A4; LED 2 sáng khi nhiệt độ 30°C.
B. Kết nối LCD SDA-A4, SCL-A5; LED 3 sáng khi độ ẩm 50%.
C. Kết nối LCD SDA-A4, SCL-A5; LED 2 sáng khi nhiệt độ 38°C; LED 3 sáng khi độ ẩm 80%.
D. Kết nối LCD SDA-A5, SCL-A4; Sử dụng nguồn nối tiếp cho L298.

**Correct:** C
**Explanation:** 
- Theo chuẩn I2C trên Arduino Uno, SDA nối A4 và SCL nối A5.
- Theo yêu cầu đề bài: LED 2 (Đỏ) sáng khi nhiệt độ ngoài khoảng 25-35°C (38°C là ngoài khoảng).
- LED 3 (Xanh dương) sáng khi độ ẩm ngoài khoảng 40-70% (80% là ngoài khoảng).
- Phương án A và D sai sơ đồ chân I2C. Phương án B sai logic cảnh báo (50% là bình thường nên LED phải tắt).

---

### 3. Hình ảnh minh họa (Assets)

Hệ thống sơ đồ mạch điện và mô hình tham khảo:

![image3.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.docx_image3.png)
*(Sơ đồ kết nối các linh kiện chính)*

![image15.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.docx_image15.png)
*(Giao diện lập trình khối điều khiển IR)*

![image18.jpg](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.docx_image18.jpg)
*(Mô hình xe thực tế với mái che bảo vệ)*

![image6.png](assets\Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2.docx_image6.png)
*(Cấu trúc vòng lặp kiểm tra điều kiện cảm biến)*