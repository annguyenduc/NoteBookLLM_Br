---
file_id: "QUESTION_IOT_AI_Arduino_D4_20_De4_Q20"
title: "Câu 20: Tương tác giữa các sự kiện phím nhấn (Blink vs Stop)"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Programming", "LED", "Events", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Khi nhấn phím 'a' (LED chớp tắt mỗi 0.5s), sau đó 10 giây nhấn phím 'b', đèn LED sẽ hoạt động như thế nào dựa trên code mBlock?

![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId63.png)
![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId47.png)

## 📝 Đáp án lựa chọn
- **A/ Khi nhấn phím 'a', đèn LED chớp tắt liên tục mỗi 0,5 giây. Khi nhấn phím 'b', đèn LED tắt trong thời gian ngắn, sau đó tiếp tục chớp tắt liên tục. (Đáp án)**
- B/ Khi nhấn phím 'a', đèn LED tắt. Khi nhấn phím 'b', đèn LED sáng lên.
- C/ Khi nhấn phím 'a', đèn LED sáng. Khi nhấn phím 'b', đèn LED tắt đi.
- D/ (Trống)

## 💡 Giải thích
Trong mBlock, các khối lệnh sự kiện chạy song song. Nếu phím 'a' kích hoạt vòng lặp `forever` để chớp tắt, thì việc nhấn phím 'b' chỉ thực hiện lệnh tắt LED tức thời rồi vòng lặp `forever` của phím 'a' sẽ ngay lập tức ghi đè trạng thái ở chu kỳ tiếp theo.
