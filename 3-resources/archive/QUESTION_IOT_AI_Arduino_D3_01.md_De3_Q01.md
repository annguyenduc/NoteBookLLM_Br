---
file_id: "QUESTION_IOT_AI_Arduino_D3_01_De3_Q01"
title: "Câu 1: Khối lệnh không dùng được trong chế độ Live"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "mBlock5", "Programming", "Live Mode", "Nhận biết"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Nhận biết"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Khối lệnh nào sau đây không thể sử dụng được trong việc lập trình Arduino bằng chế độ Live?

## 📝 Đáp án lựa chọn
- **A/ (Đáp án)**
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId7.png)
- B/
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId8.png)
- C/
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId9.png)
- D/
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId10.png)

## 💡 Giải thích
Các khối lệnh sự kiện dành riêng cho chế độ Upload (như `when Arduino Uno starts up`) sẽ không hoạt động ở chế độ Live. Ở chế độ Live, ta thường bắt đầu bằng các sự kiện của mBlock như `when green flag clicked`.
