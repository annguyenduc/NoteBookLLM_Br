---
file_id: "QUESTION_IOT_AI_Arduino_D4_29_De4_Q29"
title: "Câu 29: Hệ thống an ninh nhận diện Chủ nhà (Owner)"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "AI", "Teachable Machine", "Security", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Sử dụng Teachable Machine để phân biệt Chủ nhà (owner) và Người lạ (stranger). Với code dưới đây, hệ thống hoạt động như thế nào?

![Image](../assets/IMG_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId77.png)
![Image](../assets/IMG_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_rId84.png)

## 📝 Đáp án lựa chọn
- **A/ Khi nhận diện được chủ nhà (owner), đèn LED sẽ sáng. Ngược lại nếu nhận diện người lạ (stranger), đèn LED sẽ tắt. (Đáp án)**
- B/ Nếu nhận diện người lạ, đèn LED sáng. Ngược lại chủ nhà thì tắt.
- C/ Nếu nhận diện người lạ, đèn LED nhấp nháy. Ngược lại chủ nhà thì tắt.
- D/ Nếu nhận diện người lạ, đèn LED tắt. Ngược lại chủ nhà thì nhấp nháy.

## 💡 Giải thích
Dựa vào khối lệnh `if [result is owner] then [set pin ... to High] else [set pin ... to Low]` để mô tả kịch bản thực tế của hệ thống an ninh.
