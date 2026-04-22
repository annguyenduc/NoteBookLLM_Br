---
file_id: "ATOMS_Arduino_Power"
title: "Nguồn điện Arduino"
category: "Atomic Note"
prefix: "ATOMS"
tags: ["Hardware", "Arduino", "Power"]
source: "[[LMS_KB_IOT_NORMALIZED.md]]"
status: "draft"
created: "2026-04-13"
last_updated: "2026-04-13"
---

# Nguồn điện Arduino

## 📌 Định nghĩa cốt lõi
Cấp nguồn cho Arduino là việc cung cấp điện năng (điện áp và dòng điện) thông qua các cổng USB, Jack DC hoặc chân Vin để mạch vi điều khiển hoạt động ổn định và an toàn.

## 🔍 Chi tiết kỹ thuật
<!-- COPY NGUYÊN VĂN từ nguồn — KHÔNG paraphrase -->
- **Fact 1:** Arduino có thể được cấp nguồn thông qua cổng USB (kết nối máy tính), Jack DC (adapter 9V) hoặc chân Vin.
- **Fact 2:** Các chân 3.3V và 5V trên Arduino là các chân cấp nguồn đầu ra cho linh kiện, không dùng để cấp nguồn đầu vào không ổn định.
- **Fact 3:** Để kết nối Arduino với máy tính, ta sử dụng cáp USB: đầu cắm vào máy tính là USB-A, đầu cắm vào Arduino là USB-B.
- **Fact 4:** Điện áp đầu ra (output) tiêu chuẩn của các cổng Digital trên mạch Arduino Uno là 5V.
- **Fact 5:** Điện áp hoạt động: Nếu cấp nguồn 3.3V cho linh kiện yêu cầu 5V (như cảm biến mưa), linh kiện sẽ hoạt động không chính xác hoặc không ổn định.
- **Fact 6:** Cấp nguồn Arduino: Có thể cấp qua cổng USB Type B, Jack DC (7-12V) hoặc chân VIN. Chân 3.3V và 5V trên board chủ yếu là chân đầu ra (Output), không dùng để cấp nguồn vào (trừ trường hợp nguồn ổn định đặc biệt).
- **Fact 7:** Yolo:Bit hỗ trợ kết nối với máy tính thông qua hai phương thức chính là dây cáp USB hoặc kết nối không dây Bluetooth.

## 💡 Ví dụ thực tế
Khi chế tạo Xe robot tránh vật cản, học sinh sử dụng bộ pin sạc 11.1V nối vào Jack DC của Arduino. Việc này giúp xe di chuyển linh hoạt (không vướng cáp USB) và cung cấp đủ dòng điện cho động cơ hoạt động mạnh mẽ.

## 🔗 Liên kết tư duy
- Phân phối nguồn qua: [[ATOMS_Breadboard]]
- Linh kiện tiêu thụ nguồn lớn: [[ATOMS_Servo_Motor]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Cấp nguồn qua USB (5V), Jack DC (7-12V) hoặc Vin. Chân 5V/3.3V là chân Output. |
| **Feelings** | Học sinh thường lo lắng khi cắm nguồn 12V (sợ cháy mạch) hoặc hay nhầm lẫn chân 5V (Out) là chân dùng để sạc pin. |
| **Findings** | Điện áp ổn định là "xương sống" của hệ thống; nguồn yếu sẽ khiến cảm biến sai số hoặc Arduino bị reset liên tục khi động cơ khởi động. |
| **Futures** | Thiết kế giải pháp quản lý năng lượng cho các thiết bị IoT tầm xa (Smart Farmland) sử dụng pin Lithium và sạc mặt trời. |

## 📖 Nguồn
`📖 Nguồn: brain/raw/LMS_KB_IOT_NORMALIZED.md — tag [Arduino_Power]`

---
<!-- ATOM CHECKLIST — @librarian verify trước khi đổi status: verified -->
- [ ] Chỉ có 1 khái niệm duy nhất trong file này
- [ ] Có ít nhất 2 [[wikilinks]]
- [ ] Phần Futures không để trống
- [ ] Nguồn có thể trace về brain/raw/
- [ ] Facts là copy nguyên văn, không paraphrase
