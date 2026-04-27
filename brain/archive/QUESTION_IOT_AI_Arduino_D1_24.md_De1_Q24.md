---
file_id: "QUESTION_IOT_AI_Arduino_D1_24_De1_Q24"
title: "Câu 24: Điều khiển Servo xoay liên tục bằng nút nhấn"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Programming", "Servo", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Lập trình để khi nhấn "On", Servo xoay 0-180 liên tục; khi nhấn "Off", Servo dừng ở 90 độ. Đáp án nào sau đây thể hiện câu lệnh của Arduino?

![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId57.png)
![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId59.png)

## 📝 Đáp án lựa chọn
- **A/ (Đáp án)**
  ![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId58.png)
- B/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId58.png)
- C/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId59.png)
- D/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId60.png)

## 💡 Giải thích
Để tạo hiệu ứng xoay liên tục sau khi nhấn một nút, ta cần sử dụng vòng lặp `repeat until` cho đến khi nhận được tín hiệu dừng từ phím còn lại.
