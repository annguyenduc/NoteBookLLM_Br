---
file_id: "QUESTION_IOT_AI_Arduino_D4_21_De4_Q21"
title: "Câu 21: Chế độ hoạt động của Broadcast"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["mBlock5", "Broadcast", "Live Mode", "Nhận biết"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Nhận biết"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Phát biểu nào sau đây là đúng khi nói về khối lệnh "Broadcast" và "When I receive message"?

## 📝 Đáp án lựa chọn
- **A/ Việc truyền và nhận tin nhắn khi lập trình Arduino chỉ có thể sử dụng khi dùng chế độ LIVE. (Đáp án)**
- B/ Việc truyền và nhận tin nhắn chỉ có thể sử dụng khi lập trình các nhân vật.
- C/ Arduino chỉ có thể nhận tin nhắn từ nhân vật, chứ không thể gửi tin nhắn đến nhân vật.
- D/ Mỗi nhân vật, thiết bị chỉ có thể truyền, nhận 1 tin nhắn khi lập trình.

## 💡 Giải thích
Tin nhắn (Broadcast) là cơ chế giao tiếp thời gian thực giữa máy tính (mBlock Sprite) và thiết bị (Arduino). Vì vậy, nó yêu cầu kết nối duy trì ở chế độ LIVE. Trong chế độ UPLOAD, thiết bị chạy độc lập nên không thể sử dụng Broadcast để tương tác với Sprite trên màn hình.
