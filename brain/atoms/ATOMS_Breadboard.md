---
file_id: "ATOMS_Breadboard"
title: "Breadboard — Quy tắc kết nối"
category: "Atomic Note"
prefix: "ATOMS"
tags: ["Hardware", "Arduino", "Circuit"]
source: "[[LMS_KB_IOT_NORMALIZED.md]]"
status: "draft"
created: "2026-04-13"
last_updated: "2026-04-13"
---

# Breadboard — Quy tắc kết nối

## 📌 Định nghĩa cốt lõi
Breadboard (bo mạch thử nghiệm) và mạch mở rộng là các công cụ hỗ trợ kết nối, phân phối nguồn điện và tín hiệu giữa mạch điều khiển chính với các linh kiện ngoại vi mà không cần hàn mạch.

## 🔍 Chi tiết kỹ thuật
<!-- COPY NGUYÊN VĂN từ nguồn — KHÔNG paraphrase -->
- **Fact 1:** Trên Breadboard, các lỗ ở khu vực giữa được kết nối theo hàng dọc (nhóm 5 lỗ), trong khi các dải nguồn ở mép được kết nối theo hàng ngang.
- **Fact 2:** Quy tắc dẫn điện trên Breadboard: Các hàng ở khu vực biên (thường đánh số 1 và 4) dẫn điện theo hàng ngang (dùng làm đường nguồn); các lỗ ở khu vực giữa (2 và 3) dẫn điện theo hàng dọc.
- **Fact 3:** Quy tắc kết nối Breadboard: Khu vực đường ray nguồn (ngoài cùng) kết nối theo hàng ngang; khu vực cắm linh kiện (giữa) kết nối theo hàng dọc.
- **Fact 4:** Chân cắm tiêu chuẩn Grove cho các module mở rộng (như LED) thường bao gồm 3 chân: GND (Đất), VCC (Nguồn), và SIG (Tín hiệu).
- **Fact 5:** Động cơ Servo được kết nối với mạch mở rộng Yolo:Bit thông qua các dãy cổng GVS (Ground - Voltage - Signal).
- **Fact 6:** Module đèn LED RGB và các cảm biến cơ bản thường sử dụng dây kết nối chuẩn Grove để kết nối với mạch mở rộng.

## 💡 Ví dụ thực tế
Khi thiết kế mạch đèn giao thông, học sinh cắm Arduino và 3 đèn LED lên Breadboard. Học sinh sử dụng dải nguồn biên để cấp chung cực âm (GND) cho cả 3 đèn, giúp mạch gọn gàng và dễ dàng thay thế linh kiện nếu cần.

## 🔗 Liên kết tư duy
- Phối hợp cấp nguồn: [[ATOMS_Arduino_Power]]
- Chỉ báo âm thanh: [[ATOMS_Buzzer]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Biên: Dẫn điện ngang (nguồn). Giữa: Dẫn điện dọc. Chuẩn cắm: Grove (3 chân) / GVS. |
| **Feelings** | Học sinh mới thường bị rối bởi quy tắc "dọc giữa - ngang biên" và hay cắm linh kiện bị ngắn mạch (short circuit) do cắm cả hai chân vào cùng một hàng dọc. |
| **Findings** | Nắm vững quy tắc dẫn điện trên Breadboard và chuẩn cắm Grove/GVS giúp việc lắp ráp phần cứng trở nên khoa học, dễ debug và giảm thiểu sai sót vật lý. |
| **Futures** | Làm nền tảng để lắp ráp nhanh các loại mạch tiền-vạn-năng (prototype) cho các dự án IoT, robot và thiết bị tự động hóa. |

## 📖 Nguồn
`📖 Nguồn: brain/raw/LMS_KB_IOT_NORMALIZED.md — tag [Breadboard]`

---
<!-- ATOM CHECKLIST — @librarian verify trước khi đổi status: verified -->
- [ ] Chỉ có 1 khái niệm duy nhất trong file này
- [ ] Có ít nhất 2 [[wikilinks]]
- [ ] Phần Futures không để trống
- [ ] Nguồn có thể trace về brain/raw/
- [ ] Facts là copy nguyên văn, không paraphrase
