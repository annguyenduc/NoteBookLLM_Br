---
file_id: "QUESTION_IOT_AI_Arduino_D2_16_De2_Q16"
title: "Câu 16: Điều khiển LED bằng phím mũi tên"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Programming", "Events", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Khi nhấn phím mũi tên lên, sau đó 10 giây thì nhấn phím mũi tên xuống, đèn LED sẽ hoạt động như thế nào dựa trên đoạn code dưới đây?

![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId31.png)
![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId32.png)

## 📝 Đáp án lựa chọn
- **A/ Khi nhấn phím mũi tên lên, đèn LED chớp tắt liên tục mỗi 0,5 giây. Khi nhấn phím mũi tên xuống, đèn LED tắt trong thời gian ngắn, sau đó tiếp tục chớp tắt liên tục. (Đáp án)**
- B/ Khi nhấn phím mũi tên lên, đèn LED chớp tắt liên tục mỗi 0,5 giây. Khi nhấn phím mũi tên xuống, đèn LED tắt hẳn.
- C/ Khi nhấn phím mũi tên lên, đèn LED tắt. Khi nhấn phím mũi tên xuống, đèn LED sáng lên.
- D/ Khi nhấn phím mũi tên lên, đèn LED sáng. Khi nhấn phím mũi tên xuống, đèn LED tắt đi.

## 💡 Giải thích
Phân tích logic sự kiện: Phím lên kích hoạt vòng lặp vĩnh viễn (hoặc lặp lại). Phím xuống chỉ thực hiện lệnh tắt một lần rồi dừng, nhưng nếu phím lên vẫn đang chạy trong một luồng khác, LED có thể bị tác động ngược lại.
