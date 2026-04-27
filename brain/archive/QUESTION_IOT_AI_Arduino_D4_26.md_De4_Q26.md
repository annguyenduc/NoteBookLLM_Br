---
file_id: "QUESTION_IOT_AI_Arduino_D4_26_De4_Q26"
title: "Câu 26: Lập trình Voice Control cho Servo (Phần nhân vật)"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "AI", "Speech Recognition", "Servo", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Điều khiển Servo xoay 0/180 độ bằng giọng nói "left/right". Với code Arduino có sẵn, đáp án nào thể hiện câu lệnh của nhân vật Sprite để thực hiện yêu cầu?

![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId74.png)

## 📝 Đáp án lựa chọn
- **A/ (Đáp án)**
  ![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId73.png)
- B/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId71.png)
- C/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId72.png)
- D/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId73.png)

## 💡 Giải thích
Nhân vật cần sử dụng khối `recognize [English] for [x] seconds` của extension Cognitive Services để thu âm và xử lý giọng nói thành văn bản cho Arduino so khớp.
