---
file_id: "WIKI_IOT_AI_Arduino_Logic"
title: "Tư duy & Logic IOT AI Arduino"
category: "Logic Wiki"
prefix: "WIKI"
tags: ['AI', 'Logic', 'Machine_Learning', 'Teachable_Machine', 'mBlock']
source: "`IOT_AI_Arduino_de_trac_nghiem_1_-_ai_arduino.md`, `IOT_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md`"
status: "verified"
created: "2026-04-24"
---

# 🧠 Tư duy & Logic IOT AI Arduino

Logic trong AI Arduino là sự kết hợp giữa **Quy trình huấn luyện** và **Logic ra quyết định**.

---

## 1. Quy trình Máy học (Machine Learning Workflow)

Quy trình máy học trong mBlock thường gồm 3 bước:
1.  **Học mẫu dữ liệu (Learning)**: Thu thập các mẫu (Hình ảnh, Âm thanh hoặc Tư thế). Cần thu thập nhiều mẫu khác nhau cho mỗi lớp (Class) để tăng độ chính xác.
2.  **Huấn luyện (Training)**: Mô hình học từ dữ liệu. 
    - **Tham số Epochs**: Số lần học lại dữ liệu. Epochs càng cao, máy học càng kỹ nhưng tốn thời gian hơn.
3.  **Nhận diện (Recognition/Testing)**: Sử dụng mô hình đã huấn luyện để nhận diện dữ liệu mới.

## 2. Logic Nhận diện của Cognitive Services

Dịch vụ này cung cấp các khả năng:
- **Thị giác (Vision)**: 
    - Nhận diện khuôn mặt: Trả về **Tuổi**, **Giới tính**, **Cảm xúc** (Hạnh phúc, Buồn, Ngạc nhiên, Tức giận, Sợ hãi, v.v.).
    - Nhận diện chữ viết (**OCR**): Chuyển hình ảnh văn bản thành dữ liệu dạng chuỗi (String).
- **Ngôn ngữ (Speech)**: 
    - **Văn bản thành giọng nói (Text to Speech)**: Có thể tùy chọn ngôn ngữ và giọng đọc.
    - **Giọng nói thành văn bản (Speech to Text)**: Kết quả trả về là một chuỗi văn bản.

## 3. Cấu trúc chương trình AI Arduino

Chương trình thường chia làm 2 phần:
- **Phần AI (Chạy trên Sprite)**: Thực hiện nhận diện và phát tin nhắn (Broadcast).
- **Phần thực thi (Chạy trên Arduino)**: Khi nhận được tin nhắn, Arduino sẽ thực hiện hành động tương ứng.

**Ví dụ:**
- `Nếu <(Kết quả nhận diện khuôn mặt) = [Hạnh phúc]> thì:`
    - `Phát tin nhắn [Mo_Cua]`
- `Khi nhận tin nhắn [Mo_Cua] (Phía Arduino):`
    - `Quay Servo 90 độ.`

---

## 4. Các khái niệm quan trọng
- **Lớp (Class)**: Các nhóm dữ liệu khác nhau trong máy học (VD: Lớp "Chó", Lớp "Mèo").
- **Vòng lặp huấn luyện (Epochs)**: Số lần mô hình học đi học lại dữ liệu để tăng độ chính xác.

---

## 🛡️ Nguồn xác thực (Audit Trail)
- [AUDITOR] **Verified** — Đã đối soát 100% với nguồn RAW (Rule 14).
- 📖 Nguồn: `IOT_AI_Arduino_de_trac_nghiem_1_-_ai_arduino.md` — [Câu 1: Xử lý ngôn ngữ STT/TTS]
- 📖 Nguồn: `IOT_Tự_động_hóa_và_IOT_AI_Arduino_Đề_trắc_nghiệm_1_-_AI_Arduino.md` — [Câu 25: Logic kết nối Arduino]
- 📖 Nguồn: `IOT_AI_Arduino_de_4_trac_nghiem_-_ai_arduino.md` — [Câu 10: Vòng lặp huấn luyện Epochs]
