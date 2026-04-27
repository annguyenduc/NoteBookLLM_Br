---
file_id: "KB_IOT_Arduino_Master"
title: "Bản đồ Tri thức IOT Arduino (Final)"
category: "Knowledge Base"
prefix: "KB"
tags: ["Arduino", "IoT", "AI", "Master_Data"]
source_pages: ["WIKI_IOT_Arduino_Hardware", "WIKI_IOT_Arduino_Logic", "WIKI_IOT_Arduino_Advanced"]
distilled_by: "/distill workflow v4.3 (Karpathy)"
status: "verified"
created: "2026-04-25"
last_updated: "2026-04-25"
---

# 🎓 Bản đồ Tri thức IOT Arduino (Final Distilled)

Đây là tệp tin chưng cất cuối cùng, tổng hợp toàn bộ tri thức từ hơn 120 câu hỏi LMS và 200+ câu hỏi AI Arduino. Tệp này đóng vai trò là "Ground Truth" cho toàn bộ hệ thống.

## 📊 Thống kê Khai thác (Mining Stats)
| Chỉ số | Số lượng | Trạng thái |
|:---|:---|:---|
| Tổng số câu hỏi đã trích xuất | 120 (LMS) + 238 (AI) | 100% |
| Tệp Wiki thành phần | 3 (Hardware, Logic, Advanced) | 100% |
| Fact xác thực (Audit Trail) | ~45 facts | Verified |
| Độ phủ kiến thức | Toàn diện (Board, Sensor, Logic, AI) | 100% |

---

## 🏗️ 1. Trụ cột Phần cứng (Hardware Pillars)
- **Board:** Arduino Uno R3 (Atmega328P).
- **Kết nối:** Jack DC (nguồn ngoài), USB (nạp code).
- **Linh kiện:** 
    - **Input:** Nút nhấn (Pullup), Joystick (Analog), Siêu âm (Trig/Echo), DHT11, Cảm biến Analog (G-V-S).
    - **Output:** LED (220Ω), RGB (Common Cathode), Buzzer (3-5V), Servo (PWM), LCD (I2C: A4/A5), L298 (Motor Driver).

## 🧠 2. Trụ cột Logic (Logic Pillars)
- **Cấu trúc:** Setup (khởi tạo) và Forever (vòng lặp).
- **Vận hành:** 
    - Tuần tự (Sequential) dùng `Wait`.
    - Đa nhiệm (Multitasking) dùng `Timer` và `My Blocks`.
- **Robot:** Điều khiển 2 bánh qua 4 chân Digital (L298).

## 🚀 3. Trụ cột AI & Nâng cao (AI & Advanced)
- **Quy trình ML:** Lấy mẫu ➔ Huấn luyện (Epochs) ➔ Nhận diện (Confidence).
- **Dịch vụ Đám mây:** OCR (nhận diện chữ), TTS (đọc văn bản), STT (nghe giọng nói).
- **Nâng cao:** Hiệu chuẩn L298, Ngưỡng Joystick (400-600), Logic đảo trạng thái (1 - x).

---

## 🔗 Liên kết hệ thống
- [[WIKI_IOT_Arduino_Hardware]] — Chi tiết từng linh kiện.
- [[WIKI_IOT_Arduino_Logic]] — Chi tiết các mô thức lập trình.
- [[WIKI_IOT_Arduino_Advanced]] — Các kỹ thuật chuyên sâu và xử lý lỗi.

## 📖 Nguồn xác thực (Audit Trail)
Mọi tri thức trong bộ này đều có thể truy xuất ngược (Reverse Tracing) về các tệp tin trong `brain/raw/` theo **Rule 14**.
- `📖 Nguồn chính: 120_Cau_Hoi_IOT_Arduino_LMS.md`
- `📖 Nguồn phụ: IOT_AI_Arduino_Deep_Mining.md`

---
**Xác nhận bởi @pm & @librarian: 2026-04-25**
