---
file_id: "ATOMS_Prompt_Engineering_Hoc_Tap"
title: "Kỹ thuật Prompt trong học tập"
category: "Atomic Note"
prefix: "ATOMS"
tags: ["AI", "Prompt", "Pedagogy", "M2.1"]
source: "[[AI24-AItool-M2_1-BG]]"
status: "verified"
created: "2026-04-13"
last_updated: "2026-04-13"
---

# Kỹ thuật Prompt trong học tập

## 📌 Định nghĩa cốt lõi
Prompt kỹ thuật không phải là "hỏi đúng câu" — mà là **cung cấp đủ ngữ cảnh để AI trả lời đúng ngay lần đầu**, thay vì phải hỏi thêm nhiềưu vòng.

## 🔍 Khái niệm cốt lõi

**Cấu trúc prompt hiệu quả gồm 3 thành phần:**
- **Vai trò**: LLM đóng vai gì? (ví dụ: gia sư Tiếng Anh, chuyên gia tâm lý)
- **Nhiệm vụ**: Cần làm gì cụ thể?
- **Ngữ cảnh**: Người hỏi là ai, hoàn cảnh thế nào, cần output dạng gì?
  - [cite_start]*Mẹo:* Có thể chụp ảnh phần giải bài tập trên giấy gửi vào khung chat để yêu cầu AI kiểm tra, phát hiện lỗi sai và hướng dẫn chỉnh sửa[cite: 89].


**2 nguyên tắc viết prompt:**
- **Cụ thể**: Nêu rõ nội dung, phạm vi, tránh mơ hồ
- **Rõ ràng**: Diễn đạt mạch lạc, không gộp quá nhiều ý

**Vòng phản hồi (Feedback loop):**
Prompt → Đánh giá kết quả → Prompt chỉnh sửa → Lặp lại cho đến khi đạt yêu cầu

**Kích hoạt tính năng Học có hướng dẫn (Guided Learning) của AI:**
[cite_start]Tính năng Học có hướng dẫn giúp AI đưa ra gợi ý học tập từng bước và giải thích chi tiết thay vì chỉ trả lời ngắn gọn[cite: 41]. Để tận dụng tính năng này, cần giao các nhiệm vụ (Task) đặc thù theo từng môn học:

- [cite_start]**Khoa học Tự nhiên / Toán:** Hướng dẫn từng bước, Giải thích cách làm, Gợi ý bài tập rèn luyện[cite: 60].
- [cite_start]**Ngữ văn:** Phân tích đề, Gợi ý dàn bài (bằng câu hỏi gợi mở), Nhận xét và sửa ý cho đoạn văn[cite: 92].
- [cite_start]**Ngoại ngữ:** Giải bài tập, Học từ vựng/ngữ pháp (qua flashcard hoặc ngữ cảnh), Ôn luyện kĩ năng[cite: 102].


## 💡 Insight từ lớp học
> *"Không cần kỹ thuật cũng được — hỏi thêm nhiều câu là xong."*

Học sinh nói đúng một phần. Sự khác biệt thật sự là:

| | Không có kỹ thuật | Có kỹ thuật |
|---|---|---|
| Số vòng hỏi | 5-10 vòng | 1-2 vòng |
| Chất lượng câu trả lời | Chung chung | Sát nhu cầu |
| Khả năng kiểm soát | Thụ động — AI dẫn | Chủ động — người học dẫn |
| Khi thi/deadline gấp | Mất nhiều thời gian | Tiết kiệm thời gian |

**Điểm mấu chốt cần nhấn mạnh với học sinh:**
Kỹ thuật prompt không phải để AI "thông minh hơn" — mà để **người học chủ động hơn** trong việc định hướng cuộc hội thoại.

## 🎯 Mục tiêu sau bài học
Học sinh phân biệt được các khái niệm và kỹ thuật prompt để:
- Không phụ thuộc vào may mắn khi hỏi AI
- Biết tại sao kết quả tốt/xấu và cách điều chỉnh
- Ứng dụng vào các môn học khác nhau

## 🔗 Liên kết tư duy
- [[WIKI_AI_vs_LLM]] — AI là gì, LLM là gì
- [[WIKI_Trach_Nhiem_Nguoi_Hoc_AI]] — Trách nhiệm khi dùng AI học tập
- [[WIKI_Gemini_Guided_Learning]] — Tính năng Guided Learning của Gemini
- Thực hành: [[WIKI_Mau_Prompt_Hoc_Tap_K10]], [[WIKI_Demo_Prompt_Comparison_K10]]


## 4F — Phản tư của tôi
| | Nội dung |
|---|---|
| **Facts** | Cấu trúc prompt: Vai trò + Nhiệm vụ + Ngữ cảnh. Nguyên tắc: Cụ thể + Rõ ràng. |
| **Feelings** | Học sinh phản biện hợp lý — "hỏi thêm cũng được". Cần có ví dụ so sánh thời gian thực tế để thuyết phục. |
| **Findings** | Kỹ thuật prompt = kiểm soát cuộc hội thoại, không phải làm AI thông minh hơn. Đây là framing quan trọng. |
| **Futures** | Dùng bảng so sánh trên khi học sinh hỏi "tại sao cần học prompt?". Thêm ví dụ thi deadline gấp vào slide. |

## 📖 Nguồn
`📖 Nguồn: AI24-AItool-M2_1-BG-Giải_bài_tập_cùng_AI-2025.txt`
`📖 Kinh nghiệm dạy: buổi dạy M2.1 tại KDI`

---
<!-- Ghi chú cá nhân — không cần agent verify -->
- Câu 3 (ví dụ giải thích hay nhất) còn trống — điền sau khi dạy xong buổi đầu
- Cần tạo thêm: ATOMS_Trach_Nhiem_Nguoi_Hoc_AI.md sau khi đọc phần còn lại của bài
