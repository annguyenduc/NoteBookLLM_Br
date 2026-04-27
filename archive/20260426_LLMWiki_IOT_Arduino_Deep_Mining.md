# ⛏️ Báo cáo Khai thác sâu tri thức IOT Arduino (Pure)

### 📊 Thống kê hiệu suất Khai thác (Mining Stats)
| Chỉ số | Giá trị | Ghi chú |
| :--- | :--- | :--- |
| **Số tệp nguồn đã quét** | 4 tệp | Đề M2 (1,2) và Đề M1-2 (2,3) |
| **Tổng số câu hỏi** | 120 câu | Trung bình 30 câu/đề |
| **Nguyên tử tri thức (Atoms)** | 18 | Các khái niệm phần cứng & logic độc lập |
| **Tỷ lệ tri thức/câu hỏi** | **1 : 6.6** | Mật độ tri thức trung bình |

---

## 📂 NHÓM KIẾN THỨC PHẦN CỨNG (Hardware)
- **Board Arduino Uno R3**:
    - Có **14 chân Digital** (0-13) và **6 chân Analog** (A0-A5). (Nguồn: Đề M2-1 - Câu 1).
    - Các chân **PWM** (Điều chế độ rộng xung) ký hiệu dấu `~`: 3, 5, 6, 9, 10, 11. (Nguồn: Đề M2-1 - Câu 2).
    - Chân số 13 tích hợp sẵn đèn LED trên board. (Nguồn: Đề M1-2 - Câu 5).

- **Cảm biến & Kết nối**:
    - **PIR (Hồng ngoại)**: Có 3 chân (VCC, GND, OUT). Tầm xa phát hiện ~3-7m. (Nguồn: Đề M2-1 - Câu 10).
    - **Siêu âm (HC-SR04)**: Có 4 chân (VCC, Trig, Echo, GND). Chân Trig phát sóng, Echo nhận sóng. (Nguồn: Đề M1-2 - Câu 5).
    - **LCD 1602 (I2C)**: Chỉ dùng 4 dây kết nối. SDA kết nối A4, SCL kết nối A5 trên Arduino Uno. (Nguồn: Đề M1-2 - Câu 15).

## 📂 NHÓM KIẾN THỨC LẬP TRÌNH (Logic)
- **Cấu trúc code**: 
    - `void setup()`: Chạy 1 lần duy nhất khi khởi động.
    - `void loop()`: Chạy lặp lại vô hạn.
- **Lệnh cơ bản**:
    - `pinMode(pin, OUTPUT/INPUT)`: Thiết lập chế độ chân.
    - `digitalWrite(pin, HIGH/LOW)`: Xuất tín hiệu Digital.
    - `analogRead(pin)`: Đọc giá trị Analog (0 - 1023).

## 📂 GIAO TIẾP & GỠ LỖI
- **Serial Monitor**: Công cụ để xem dữ liệu truyền từ Arduino lên máy tính.
- **Baudrate**: Tốc độ truyền chuẩn thường dùng là **9600**. (Nguồn: Đề M1-2 - Câu 20).

---
*Báo cáo đang được hoàn thiện để đối soát với Wiki chính.*
