---
file_id: "QUESTION_IOT_AI_Arduino_D2_01_De2_Q01"
title: "Câu 1: Cách cấp nguồn cho Arduino"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Hardware", "Power Supply", "Nhận biết"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Nhận biết"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
Khẳng định nào dưới đây là SAI?

## 📝 Đáp án lựa chọn
- **A/ Có thể cấp nguồn cho Arduino thông qua pin với chân 3,3V hoặc 5V. (Đáp án)**
- B/ Có thể cấp nguồn cho Arduino bằng cách kết nối với máy tính thông qua dây cáp.
- C/ Có thể cấp nguồn cho Arduino thông qua dây adapter 9V.
- D/ Có thể cấp nguồn cho Arduino thông qua pin với cổng Vin.

## 💡 Giải thích
Các chân 3.3V và 5V trên Arduino là các chân **đầu ra** (output) để cấp nguồn cho linh kiện ngoại vi, không được dùng để cấp nguồn ngược lại cho board (có thể gây hỏng mạch). Nguồn cấp vào phải thông qua cổng USB, Jack DC hoặc chân Vin.
