# Đề Kiểm Tra Arduino 1 – Kiến Thức Nền Tảng IoT  
**Thời lượng:** 45 phút  
**Số câu hỏi:** 10  
**Cấu trúc Bloom:** 4 (Nhớ) – 4 (Hiểu) – 2 (Vận dụng)

---

## I. Cấp độ **Nhớ** (Mỗi câu 1 điểm)

### Câu 1:  
Liệt kê các chân **Digital Pin**, **Analog Pin**, **Power Pin** và **Ground Pin** chính trên **Arduino Uno** và nêu chức năng cơ bản của từng loại.

---

### Câu 2:  
Trình bày các bước cơ bản để **kết nối LED** với **Arduino Uno** thông qua **breadboard** và **điện trở hạn dòng**.

---

### Câu 3:  
Viết cú pháp đúng cho hai hàm sau trong **lập trình Arduino IDE**:  
- `pinMode()`  
- `digitalWrite()`

---

### Câu 4:  
Nêu tên các chân của **Servo MG90S** và mô tả cách kết nối từng chân với **Arduino Uno**.

---

## II. Cấp độ **Hiểu** (Mỗi câu 1.5 điểm)

### Câu 5:  
Giải thích sự khác biệt giữa **chân Digital** và **chân Analog** trên **Arduino Uno** về chức năng và ứng dụng.

---

### Câu 6:  
Phân tích vai trò của **điện trở hạn dòng** khi kết nối **LED** với **Arduino Uno**. Nếu không có điện trở, điều gì sẽ xảy ra?

---

### Câu 7:  
Giải thích chức năng của hàm `loop()` trong chương trình **Arduino IDE** và so sánh với hàm `setup()`.

---

### Câu 8:  
So sánh **Servo MG90S** với **servo thông thường** về:  
- Góc quay tối đa  
- Momen xoắn  
- Ứng dụng phổ biến

---

## III. Cấp độ **Vận dụng** (Mỗi câu 2 điểm)

### Câu 9:  
Viết đoạn mã **Arduino IDE** để điều khiển **Servo MG90S** quay từ **0° đến 180°** với tốc độ **1° mỗi giây**, sau đó quay ngược lại về 0° và lặp lại quá trình này.

---

### Câu 10:  
Thiết kế mạch và viết mã điều khiển **2 LED** (một **LED đỏ**, một **LED xanh**) sao cho:  
- **LED đỏ** sáng trong **2 giây**,  
- Sau đó **LED xanh** sáng trong **1 giây**,  
- Quá trình này **lặp lại liên tục**.

---

## Gợi Ý & Tài Liệu Tham Khảo:
- Sử dụng tài liệu: **LMS_KB_IOT_DEEP.md**
- Kiến thức về: **Arduino Uno**, **Servo MG90S**, **LED**, **breadboard**, **hàm pinMode**, **digitalWrite**, **analogRead**, **Servo.h**

---

## Đáp Án Gợi Ý (Không bắt buộc phải có trong đề thi):
> (Phần này dành riêng cho giáo viên hoặc người chấm thi)

---

**Lưu ý:**  
- Học sinh có thể sử dụng **simulator mạch** như **Tinkercad** để kiểm tra code trước khi nộp bài (nếu được phép).  
- Các thuật ngữ như **digital pin**, **analog pin**, **breadboard**, **Servo MG90S**, **Arduino IDE**, **loop()**, **setup()**, **Servo.h library** cần được sử dụng đúng theo **terminology trong KB**.