---
file_id: "QUESTION_IOT_AI_Arduino_D2_20_De2_Q20"
title: "Câu 20: Hệ thống phối hợp Buzzer, LED và ISD1820"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Programming", "ISD1820", "Buzzer", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Dựa vào đoạn chương trình dưới đây, các thiết bị trên mạch Arduino sẽ thực hiện hành động như thế nào?

![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId47.png)
![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId48.png)

## 📝 Đáp án lựa chọn
- **A/ Khi nhấn phím Space, sau 3 tiếng kêu ngắt quãng của cái Buzzer, đèn LED sẽ sáng và mạch ISD1820 sẽ phát ra đoạn ghi âm đã được thu. (Đáp án)**
- B/ Khi nhấn phím Space, đèn LED sẽ sáng đồng thời thu âm giọng của người dùng trong 10 giây rồi tắt.
- C/ Khi nhấn phím Space, sau 3 tiếng kêu ngắt quãng của cái Buzzer, đèn LED sẽ sáng đồng thời thu âm giọng của người dùng trong 10 giây rồi tắt.
- D/ Khi nhấn phím Space, đèn LED tắt đồng thời mạch ISD1820 sẽ phát ra đoạn ghi âm đã được thu.

## 💡 Giải thích
Phân tích trình tự code: Vòng lặp kêu 3 lần -> Bật LED -> Kích hoạt chân PLAY của ISD1820. Đây là một quy trình báo động hoặc thông báo tự động.
