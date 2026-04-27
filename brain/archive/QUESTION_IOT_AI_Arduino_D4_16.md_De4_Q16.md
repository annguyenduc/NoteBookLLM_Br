---
file_id: "QUESTION_IOT_AI_Arduino_D4_16_De4_Q16"
title: "Câu 16: Lập trình hệ thống đa thiết bị (LED, Servo, ISD1820)"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Programming", "LED", "Servo", "ISD1820", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Với yêu cầu hệ thống: Nhấn mũi tên Trái để Ghi âm + Bật LED Đỏ + Gạt Servo sang 0 độ; Nhấn mũi tên Phải để Phát âm + Bật LED Xanh + Gạt Servo sang 180 độ. Hãy xác định đoạn chương trình còn thiếu?

### Bảng chân kết nối
| Thiết bị | Chân Arduino |
| :--- | :--- |
| LED Đỏ | 13 |
| LED Xanh | 12 |
| Servo | 11 |
| PLAYL | 6 |
| PLAYE | 5 |
| REC | 4 |

## 📝 Đáp án lựa chọn
- **A/ (Đáp án)**
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId33.png)
- B/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId34.png)
- C/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId35.png)
- D/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId36.png)

## 💡 Giải thích
Cần đối chiếu chính xác các chân Digital đã khai báo trong bảng với lệnh `set digital pin` và `set servo pin` trong code để đảm bảo đúng kịch bản điều khiển.
