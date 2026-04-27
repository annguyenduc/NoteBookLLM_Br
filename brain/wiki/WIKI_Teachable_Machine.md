---
file_id: "ATOMS_Teachable_Machine"
title: "Teachable Machine — Công cụ Học máy No-Code"
category: "Atomic Note"
prefix: "ATOMS"
tags: ["AI", "ML", "mBlock", "Extension", "Image Classification"]
source: "[[IOT_AI_Arduino_de_trac_nghiem_1_-_ai_arduino]]"
status: "verified"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Teachable Machine — Công cụ Học máy No-Code

## 📌 Định nghĩa cốt lõi
Teachable Machine là tiện ích mở rộng (Extension) trong mBlock, cho phép **huấn luyện mô hình máy học (Machine Learning)** để phân loại hình ảnh, âm thanh hoặc tư thế — không cần viết code phức tạp — và tích hợp trực tiếp vào dự án mBlock.

## 🔍 Chi tiết kỹ thuật
<!-- COPY NGUYÊN VĂN từ nguồn — KHÔNG paraphrase -->
- **Fact 1:** Teachable Machine là công cụ phù hợp để dạy máy tính nhận biết (hình ảnh) một số vật bất kỳ. *(Câu 1, IOT_AI_Arduino_de_trac_nghiem_1)*
- **Fact 2:** Để sử dụng Teachable Machine trong mBlock, phải thêm tiện ích mở rộng (Extension) "Teachable Machine". *(Câu 2)*
- **Fact 3:** Quy trình huấn luyện (Training): **Thêm extension → Training model → Build new model → Cung cấp dữ liệu hình ảnh → Learn → Use the model**.
- **Fact 4 (điểm sai thường gặp):** Teachable Machine **không sử dụng** extension "Cognitive Services" — đây là 2 extension riêng biệt trong mBlock. *(Câu sai — IOT_AI_Arduino_de_2)*
- **Fact 5:** Teachable Machine nằm trong nhóm lệnh Extension của **nhân vật (Sprite)**, không phải của Stage.

## 💡 Ví dụ thực tế
Học sinh dùng Teachable Machine để dạy máy tính phân biệt **3 loại rác** (hữu cơ, vô cơ, tái chế) qua hình ảnh camera. Sau khi huấn luyện, mBlock tự động phân loại và điều khiển servo quay thùng rác đúng ngăn — ứng dụng trong dự án "Thùng rác thông minh AI".

## 🔗 Liên kết tư duy
- Được tích hợp vào: [[WIKI_Servo_Motor]] (điều khiển actuator sau phân loại)
- Cùng nhóm AI Tools trong mBlock: [[WIKI_Prompt_Engineering_Hoc_Tap]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Extension trong mBlock. Quy trình: Add Extension → Train → Build → Learn → Use. Phân loại: hình ảnh, âm thanh, tư thế. |
| **Feelings** | Học sinh hay nhầm lẫn giữa "Training model" (thu thập dữ liệu) và "Build new model" (biên dịch model) — hay bỏ qua bước Build. |
| **Findings** | Điểm mạnh của Teachable Machine: lowcode/nocode, chạy offline sau khi train, dễ tích hợp với phần cứng Arduino qua mBlock. |
| **Futures** | Ứng dụng trong các dự án STEM: nhận diện cử chỉ tay điều khiển robot, phân loại vật thể, nhận diện khuôn mặt cơ bản. |

## 📖 Nguồn
`📖 Nguồn: brain/raw/IOT_AI_Arduino_de_trac_nghiem_1_-_ai_arduino.md (Câu 1-2) + brain/raw/IOT_AI_Arduino_de_2_trac_nghiem_-_ai_arduino.md`
<!-- [AUDITOR] Rule 14: File nguồn đã được mở và xác nhận fact tồn tại tại Câu 1, 2, 3 — 2026-04-23 -->

---
<!-- ATOM CHECKLIST — @librarian verify trước khi đổi status: verified -->
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] Facts là copy nguyên văn, không paraphrase
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 1-2 AI Arduino Đề 1 + Đề 2)
<!-- @librarian verified: 2026-04-23 -->
