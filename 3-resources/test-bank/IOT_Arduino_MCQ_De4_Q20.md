---
file_id: "IOT_Arduino_MCQ_De4_Q20"
title: "Câu 20 (Thông hiểu)"
category: "Atomic Question"
prefix: "MCQ"
tags: ['IOT', 'Arduino', 'Thông hiểu']
source: "`Đề 4 Trắc nghiệm - Arduino M1,2.docx`"
level: "Thông hiểu"
answer: "B/"
status: "draft"
created: "2026-04-27"
---

# [MCQ] Câu 20 (Thông hiểu)

## ❓ Câu hỏi
Yêu cầu lập trình cho cảm biến hồng ngoại, đèn Led và còi hoạt động như sau:
- Khi không có vật cản, đèn xanh sáng, đèn đỏ tắt, còi tắt.
- Khi có vật cản, còi kêu, đèn đỏ sáng và đèn xanh sáng tắt luân phiên với nhau.
Biết các chân tín hiệu được nối như bảng bên dưới.
Phát biểu nào sau đây là đúng khi nói về đoạn chương trình sau đây.
(Nhiều đáp án)
![Image](../assets/ASSET_IOT_AI_Arduino_De4_rId34.png)

## 📝 Đáp án lựa chọn
- **A/ (Đáp án)** Câu lệnh điều kiện ở dòng (5) dùng sai chân pin DO của cảm biến hồng ngoại
- **B/ (Đáp án)** Khi có vật cản, thiếu câu lệnh cho đèn Led xanh sáng khi làm hiệu ứng 2 đèn sáng tắt luân phiên, cần thêm một câu lệnh làm đèn xanh sáng ở giữa dòng (9) và (10).
- **C/** Câu lệnh điều kiện ở dòng (1) và (5) xét sai điều kiện có/không có người của cảm biến siêu âm, cần đảo 2 giá trị 1, 0 ở 2 phần (1) và (5) với nhau.
- **D/** Câu lệnh (6), (8), (10) dùng sai chân pin của còi buzzer và đèn LED đỏ. Chân pin ở câu lệnh (6) có chân pin là 9, câu lệnh (8), (10) có chân pin là 12.
- **E/** Chương trình không hoạt động được, phải sử dụng câu lệnh if...then...else thay cho câu lệnh if...then.

## 🔗 Liên kết tư duy
- [Rule 14] Đã mở file nguồn `3-resources/raw/Tổng hợp đề kiểm tra LMS/Tự động hóa và IOT/.../Đề 4 Trắc nghiệm - Arduino M1,2.docx` và xác nhận fact.