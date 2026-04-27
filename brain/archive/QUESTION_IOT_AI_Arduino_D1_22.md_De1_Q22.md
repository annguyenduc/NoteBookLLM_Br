---
file_id: "QUESTION_IOT_AI_Arduino_D1_22_De1_Q22"
title: "Câu 22: Điều khiển đa thiết bị qua nút nhấn ảo"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Programming", "Events", "Broadcast", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Hãy lập trình thiết bị Arduino và các nhân vật nút nhấn thỏa các yêu cầu: Nút 1 bật LED, Nút 2 bật Laser, Nút 3 bật Động cơ rung. Đáp án nào sau đây thể hiện câu lệnh của 3 nhân vật nút nhấn?

![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId38.png)
![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId79.png)

## 📝 Đáp án lựa chọn
- **A/ (Đáp án)**
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId80.png)
- B/
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId81.png)
- C/
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId82.png)
- D/
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId83.png)

## 💡 Giải thích
Mỗi nhân vật nút nhấn khi được click (`when this sprite clicked`) cần gửi một thông điệp (message) riêng biệt. Arduino sẽ lắng nghe các thông điệp này để thực hiện lệnh tương ứng.
