---
file_id: "QUESTION_IOT_AI_Arduino_D3_21_De3_Q21"
title: "Câu 21: Hạn chế của Broadcast trong chế độ Upload"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "mBlock5", "Broadcast", "Upload Mode", "Nhận biết"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_3_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Nhận biết"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Phát biểu nào sau đây là SAI khi nói về khối lệnh "Broadcast" và "When I receive message"?

## 📝 Đáp án lựa chọn
- **A/ Việc truyền và nhận tin nhắn khi lập trình Arduino có thể sử dụng cả khi dùng chế độ UPLOAD và LIVE. (Đáp án)**
- B/ Việc truyền và nhận tin nhắn có thể sử dụng khi lập trình các nhân vật.
- C/ Các tin nhắn có thể được truyền qua lại giữa nhân vật và Arduino.
- D/ Thông tin có thể truyền và nhận từ nhiều sprite trong cùng 1 chương trình.

## 💡 Giải thích
Cơ chế Broadcast (truyền tin) để tương tác giữa nhân vật (Sprite) và thiết bị (Arduino) chỉ hoạt động ở chế độ LIVE. Ở chế độ UPLOAD, mã nguồn được nạp trực tiếp vào chip Arduino nên không thể giao tiếp thời gian thực với các nhân vật trên máy tính qua Broadcast thông thường.
