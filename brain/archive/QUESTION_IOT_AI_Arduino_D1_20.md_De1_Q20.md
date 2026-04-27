---
file_id: "QUESTION_IOT_AI_Arduino_D1_20_De1_Q20"
title: "Câu 20: Tương tác phím bấm và LED"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Programming", "Events", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Hỏi khi nhấn phím a, sau đó 10 giây thì nhấn phím b, đèn LED sẽ hoạt động như thế nào?

![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId63.png)
![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId47.png)

## 📝 Đáp án lựa chọn
- **A/ Khi nhấn phím a, đèn LED chớp tắt liên tục mỗi 0,5 giây. Khi nhấn phím b, đèn LED tắt trong thời gian ngắn, sau đó tiếp tục chớp tắt liên tục. (Đáp án)**
- B/ Khi nhấn phím a, đèn LED tắt. Khi nhấn phím b, đèn LED sáng lên.
- C/ Khi nhấn phím a, đèn LED sáng. Khi nhấn phím b, đèn LED tắt đi.
- D/ (Không có nội dung)

## 💡 Giải thích
Vì phím a kích hoạt vòng lặp "forever", nên dù phím b có lệnh tắt LED, nhưng ngay sau đó vòng lặp của phím a sẽ lại tiếp tục thực thi lệnh bật/tắt tiếp theo.
