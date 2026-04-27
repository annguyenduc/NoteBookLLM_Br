---
file_id: "QUESTION_IOT_AI_Arduino_D3_20_De3_Q20"
title: "Câu 20: Sửa lỗi logic cho hệ thống ghi âm/phát âm"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Programming", "ISD1820", "Debugging", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Một học sinh lập trình để nhấn Space thì ghi âm trong 10 giây, nhấn A thì phát lại bản ghi. Tuy nhiên chương trình dưới đây gặp lỗi. Ta cần sửa như thế nào?

![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId58.png)
![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId59.png)

## 📝 Đáp án lựa chọn
- **A/ Sửa đoạn code II thành: (Đáp án)**
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId60.png)
- B/ Sửa đoạn code II thành:
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId61.png)
- C/ Sửa đoạn code I thành:
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId62.png)
- D/ Sửa đoạn code I thành:
  ![Image](../assets/IMG_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino_rId63.png)

## 💡 Giải thích
Lỗi thường nằm ở việc sử dụng nhầm chân (ví dụ: REC thay vì PLAY) hoặc sai mức logic (High/Low) khi kích hoạt các chức năng của ISD1820.
