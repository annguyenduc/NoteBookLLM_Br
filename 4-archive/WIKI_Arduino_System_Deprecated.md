---
file_id: "WIKI_Arduino_System"
title: "Hệ thống lập trình Arduino"
category: "Wiki Page"
prefix: "WIKI"
tags: ["IOT", "Arduino", "System"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Hệ thống lập trình Arduino

## 📌 Định nghĩa cốt lõi
Arduino là một nền tảng mã nguồn mở (Open-source) được sử dụng để xây dựng các ứng dụng điện tử tương tác. Hệ thống bao gồm phần cứng (bo mạch vi điều khiển) và phần mềm (IDE hoặc các ứng dụng lập trình kéo thả như mBlock) giúp người dùng dễ dàng giao tiếp với các linh kiện điện tử.

## 🔍 Đặc tả kỹ thuật (Technical Specifications)

### 2.1. Cấu trúc chân Pin (Arduino Uno R3)
- **Digital Pins**: 14 chân (0-13).
- **Analog Pins**: 6 chân (A0-A5), đọc giá trị từ 0-1023.
- **PWM Pins (Điều chế xung)**: Các chân có ký hiệu `~` (**3, 5, 6, 9, 10, 11**), dùng để điều khiển tốc độ động cơ hoặc độ sáng LED. (Nguồn: Đề M2-1 - Câu 2).
- **Chân 13**: Tích hợp sẵn đèn LED trên board mạch. (Nguồn: Đề M1-2 - Câu 5).

### 2.2. Giao tiếp & Ngoại vi
- **Giao thức I2C**: Sử dụng 2 chân chuyên dụng: **SDA (A4)** và **SCL (A5)**. Thường dùng kết nối LCD 1602 (I2C). (Nguồn: Đề M1-2 - Câu 15).
- **Baudrate**: Tốc độ truyền dữ liệu chuẩn thường dùng là **9600** cho các dự án cơ bản và **115200** cho các tác vụ AI. (Nguồn: Đề M1-2 - Câu 20).
- **Linh kiện Input (Cảm biến)**: 
    - **PIR**: Có 3 chân (VCC, GND, OUT). Tầm xa phát hiện ~3-7m.
    - **Siêu âm**: Có 4 chân (VCC, Trig, Echo, GND).

**Đặc điểm nổi bật:**
- **Tính linh hoạt**: Có thể kết hợp với vô số loại linh kiện điện tử khác nhau.
- **Dễ học**: Hỗ trợ lập trình kéo thả cho người mới và lập trình ngôn ngữ C/C++ cho người nâng cao.
- **Cộng đồng lớn**: Rất nhiều thư viện và hướng dẫn có sẵn.

## 💡 Ví dụ thực tế
Một hệ thống "Vườn thông minh" sử dụng Arduino để đọc độ ẩm đất từ cảm biến, nếu đất khô sẽ điều khiển rơ-le bật máy bơm nước và hiển thị trạng thái lên màn hình LCD.

## 🔗 Liên kết tư duy
- Khái niệm con: `WIKI_Arduino_Board_and_Pins`, `WIKI_Arduino_Electronic_Components`, `WIKI_Arduino_Sensors`
- Công cụ bổ trợ: `WIKI_Breadboard_Usage`, `WIKI_mBlock_5_Software`
- Ứng dụng vào: `WIKI_IOT_Smart_Home_Project`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Nền tảng mã nguồn mở, đa dạng linh kiện, hỗ trợ lập trình đa cấp độ. |
| **Feelings** | Người học thường cảm thấy "choáng ngợp" ban đầu vì có quá nhiều dây cắm, nhưng sẽ rất hào hứng khi tự tay điều khiển được một chiếc đèn nhấp nháy. |
| **Findings** | Arduino là công cụ tốt nhất để học sinh hiểu về bản chất của phần cứng và dòng điện thay vì chỉ lập trình phần mềm thuần túy. |
| **Futures** | Là nền tảng cốt lõi cho các kỹ sư điện tử và chuyên gia IOT tương lai. |

## 📖 Nguồn
`📖 Nguồn: IOT_Arduino_de_2_trac_nghiem_-_arduino_m1_2.md — Câu 1, 14, 30`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về 3-resources/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại (Câu 1: Kết nối Arduino với máy tính; Câu 14: Lập trình LED; Câu 30: Ứng dụng xe Arduino).
