---
file_id: "QUESTION_IOT_AI_Arduino_D4_24_De4_Q24"
title: "Câu 24: Đồng bộ trạng thái Bulb (Sprite) sang Arduino LED"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Programming", "Sync", "LED", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Khi nhấn vào nhân vật Bulb, nếu trang phục là 'off' thì đổi sang 'on' và ngược lại. Đèn LED trên Arduino phải sáng/tắt tương ứng. Với code Arduino có sẵn, đáp án nào thể hiện chương trình của nhân vật Bulb?

![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId64.png)
![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId66.png)

## 📝 Đáp án lựa chọn
- **A/ (Đáp án)**
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId64.png)
- B/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId65.png)
- C/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId66.png)
- D/
  ![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId67.png)

## 💡 Giải thích
Nhân vật Sprite đóng vai trò giao diện điều khiển (UI). Việc thay đổi trang phục của Sprite cần được Arduino theo dõi (thông qua lệnh `costume name`) để phản ánh trạng thái đó ra phần cứng LED.
