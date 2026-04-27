---
file_id: "QUESTION_IOT_AI_Arduino_D2_07_De2_Q07"
title: "Câu 7: Sai sót khi kết nối mạch ISD1820 (2)"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Hardware", "ISD1820", "Nhận biết"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Nhận biết"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Phát biểu nào sau đây là SAI khi nói về các chân kết nối của mạch thu phát âm thanh ISD1820?

## 📝 Đáp án lựa chọn
- **A/ Chân PLAYE, PLAYL của mạch chỉ có thể được gắn ở một số chân Digital không có dấu ngã (~) như: 2, 4, 7, 8, 12, 13. (Đáp án)**
- B/ Chân GND của mạch được gắn với cổng GND của Arduino.
- C/ Chân VCC của mạch được gắn với cổng 5V của Arduino.
- D/ Chân REC của mạch được gắn với cổng Digital 2-13 của Arduino.

## 💡 Giải thích
Các chân Digital của Arduino (từ 2-13) đều có thể xuất tín hiệu HIGH/LOW để kích hoạt các chức năng của ISD1820, không phân biệt chân đó có hỗ trợ PWM (dấu ~) hay không.
