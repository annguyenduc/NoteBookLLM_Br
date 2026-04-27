---
file_id: "QUESTION_IOT_AI_Arduino_D4_17_De4_Q17"
title: "Câu 17: Phân tích trạng thái LED trên Breadboard"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Hardware", "LED", "Breadboard", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Với sơ đồ đấu nối 5 đèn LED trên Breadboard và đoạn code dưới đây, khi nhấn lá cờ xanh, những đèn LED nào sẽ phát sáng?

![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId27.png)
![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId38.png)

## 📝 Đáp án lựa chọn
- **A/ Chỉ có đèn đỏ sáng. (Đáp án)**
- B/ Chỉ có đèn xanh lá, xanh dương, xám, vàng sáng; Đèn đỏ không sáng.
- C/ Chỉ có đèn đỏ, xanh lá, xanh dương, xám sáng; Đèn vàng không sáng.
- D/ Cả 5 đèn đều sáng.

## 💡 Giải thích
Dựa vào sơ đồ mạch để biết chân LED nào được nối với chân Digital nào trên Arduino, sau đó đối chiếu với lệnh `set digital pin... to HIGH` trong code.
