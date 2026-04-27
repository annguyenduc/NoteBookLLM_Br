---
file_id: "QUESTION_IOT_AI_Arduino_D4_27_De4_Q27"
title: "Câu 27: Phân tích logic điều khiển 3 LED qua giọng nói"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "AI", "Speech Recognition", "LED", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Khi người dùng nói "Light number three!", dựa trên sơ đồ và mã nguồn, đèn LED nào trên mạch Arduino sẽ sáng?

![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId78.png)
![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId91.png)
![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId92.png)

## 📝 Đáp án lựa chọn
- **A/ Cả ba đèn LED đều sáng. (Đáp án)**
- B/ Đèn LED đỏ và xanh dương sáng, đèn LED xanh lá tắt.
- C/ Đèn LED xanh dương sáng, đèn LED đỏ, xanh lá tắt.
- D/ Đèn LED đỏ và xanh lá sáng, đèn LED xanh dương tắt.

## 💡 Giải thích
Cần kiểm tra kỹ các câu lệnh `if` lồng nhau. Trong trường hợp từ khóa "three" được nhận diện, code thực hiện lệnh bật tất cả các chân Digital nối với 3 đèn LED.
