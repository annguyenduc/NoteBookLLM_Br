---
file_id: "QUESTION_IOT_Arduino_D4_16"
title: "Câu hỏi: Câu 16 (Thông hiểu)"
category: "Atomic Question"
prefix: "QUESTION"
tags: ["AI", "THCS", "Thông hiểu"]
source: "[[LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md]]"
level: "Thông hiểu"
answer: "A/"
status: "verified"
created: "2026-04-22"
---

# [QUESTION] Câu 16 (Thông hiểu)

## ❓ Câu hỏi
Cho một hệ thống có yêu cầu như sau:

- Mạch Arduino gồm 2 đèn LED đỏ và xanh, 1 động cơ servo, 1 mạch thu phát âm thanh ISD1820.
- Khi nhấn lá cờ, cả 2 đèn LED đều tắt và servo xoay ở góc 90 độ.
- Khi nhấn nút mũi tên trái, đèn LED đỏ sáng, LED xanh tắt, động cơ servo gạt tay sang trái (giả sử servo gạt sang trái ở góc 0 độ) và mạch ISD1820 sẽ bắt đầu quá trình ghi âm trong 10 giây.
- Sau 10 giây ghi âm, các thiết bị sẽ tự động quay về trạng thái ban đầu giống như khi nhấn lá cờ xanh.
- Khi nhấn nút mũi tên phải, đèn LED xanh sáng, LED đỏ tắt, động cơ servo gạt tay sang phải (giả sử servo gạt sang trái ở góc 180 độ) và mạch ISD1820 sẽ phát ra âm thanh được ghi.
- Sau khi phát âm thanh được ghi, các thiết bị sẽ tự động quay về trạng thái ban đầu giống như khi nhấn lá cờ xanh.

Cho bảng kết nối các linh kiện điện tử với chân Digital trên Arduino như sau:

### Table Data

| Linh kiện điện tử  | Chân kết nối của linh kiện  | Chân Digital trên Arduino  |
| LED đỏ  | Chân dương  | Digital 13  |
| LED xanh  | Chân dương  | Digital 12  |
| Động cơ Servo  | Dây tín hiệu (Cam)  | Digital 11  |
| Mạch thu phát âm thanh ISD1820  | Chân PLAYL  | Digital 6  |
| Mạch thu phát âm thanh ISD1820  | Chân PLAYE  | Digital 5  |
| Mạch thu phát âm thanh ISD1820  | Chân REC  | Digital 4  |

Một học sinh lập trình chương trình của Arduino như sau:

![Image](../assets/IMG_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId32.png)

Hỏi đoạn chương trình còn thiếu ở chỗ trống là gì?

## 📝 Đáp án lựa chọn
- **A/ (Đáp án) (Đáp án)**
- B/

![Image](../assets/IMG_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId34.png)
- C/

![Image](../assets/IMG_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId35.png)
- D/

![Image](../assets/IMG_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino_rId36.png)

## 🔗 Liên kết tư duy
- Kiến thức liên quan: [[AI_THCS]]
- Module: [[Khoa_học_máy_tính]]

## 📖 Nguồn
`📖 Nguồn: [LMS_MASTER_Tự_động_hóa_và_IOT_AI_Arduino_Đề_4_trắc_nghiệm_-_AI_Arduino.md] — Câu 16`
