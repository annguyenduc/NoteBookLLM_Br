---
file_id: "CONCEPT_ARCH_TIS_Oscillation"
title: "Dao động (Oscillation)"
type: "concept"
status: "DRAFT"
tags:
  - "SYS"
  - "behavior"
ai-first: true
confidence: 0.95
relationships:
  - type: "emerges_from"
    target: "[[CONCEPT_ARCH_TIS_Delay]]"
  - type: "emerges_from"
    target: "[[CONCEPT_ARCH_TIS_Balancing_Feedback]]"
last_reconciled: "2026-05-18"
source_file: "RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074.md"
source_ref: "[[SOURCE_ARCH_TIS_Thinking_in_Systems]]"
created: "2026-05-18"
last_updated: "2026-05-18"
---

## For future Claude (AI Preamble)
> Dao động là hành vi hệ thống lúc lên lúc xuống vượt qua mục tiêu cân bằng. Nó là kết quả trực tiếp của các vòng lặp phản hồi cân bằng (Balancing loops) có chứa độ trễ (Delays) đáng kể.

# Dao động (Oscillation)

## 1. Định nghĩa
**Dao động (Oscillation)** là một mẫu hành vi hệ thống trong đó trạng thái của Kho chứa (Stock) liên tục di chuyển lên trên rồi lại xuống dưới điểm cân bằng mục tiêu. Đây là dấu hiệu của việc hệ thống liên tục "sửa sai quá đà" (overshoot) do thiếu thông tin kịp thời.

## 2. Nguyên lý / Cấu trúc
- Dao động không phải do một tác nhân ngẫu nhiên giật hệ thống lên xuống, mà sinh ra từ chính cấu trúc bên trong: một vòng lặp cân bằng cố gắng kéo hệ thống về đích, nhưng vì **độ trễ** (thông tin hoặc hành động đến chậm), nó tiếp tục dùng lực kéo ngay cả khi đã vượt qua đích.
- Chu kỳ dao động phụ thuộc vào độ dài của độ trễ. Trễ càng lâu, biên độ dao động càng lớn và có thể dẫn đến sự sụp đổ nếu vượt quá giới hạn chịu đựng.
- Việc cố gắng phản ứng nhanh hơn (rút ngắn thời gian phản ứng) trong một hệ thống có độ trễ giao hàng cố định thường sẽ làm cho sự dao động trở nên tồi tệ hơn (khuếch đại dao động).

## 3. Ví dụ đối chiếu (R18: Double Examples)
### Ví dụ từ sách (Original)
> **Bối cảnh**: Chu kỳ sản xuất ô tô (hàng tồn kho).
> **Ứng dụng**: Do độ trễ từ lúc đặt hàng đến lúc xe về, đại lý thấy thiếu xe nên đặt liên tục (hành động quá mức). Khi lô xe đầu tiên về, kho bắt đầu đầy nhưng các lô xe sau vẫn tiếp tục về, gây thừa ứ. Đại lý hoảng sợ ngừng đặt hàng hoàn toàn cho đến khi bán hết sạch, lại quay về trạng thái thiếu xe nghiêm trọng.
> **Nguồn**: [[SOURCE_ARCH_TIS_Thinking_in_Systems]] — Chương 2

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Sự dao động trong việc ép học sinh học bài.
> **Ứng dụng**: Giáo viên thấy lớp điểm thấp -> Ép học cực mạnh, giao nhiều bài (Trễ nhận thức/phản ứng). Điểm tăng cao nhưng học sinh kiệt sức (Overshoot). Giáo viên thấy học sinh quá mệt -> Cho chơi thả ga không kiểm soát. Hệ quả là học sinh lại buông thả, điểm lại rớt thảm hại, và chu kỳ ép uổng - buông lỏng tiếp tục lặp lại.

## 4. Phản tư sư phạm (4F)
- **Facts**: Dao động xảy ra khi có trễ trong vòng lặp cân bằng.
- **Feelings**: Việc sửa sai liên tục nhưng luôn trễ nhịp gây ra sự mệt mỏi và ức chế (burnout).
- **Findings**: Không thể chống lại dao động bằng cách phản ứng mạnh hơn. Cách tốt nhất là dự báo dựa trên hàng đợi (những gì đang trên đường đến) hoặc làm chậm lại tốc độ phản ứng.
- **Future**: Thay vì "sốc điện" vào phương pháp dạy, nên điều chỉnh nhẹ nhàng và chờ đợi kết quả tích lũy.

## 5. Trích dẫn nguồn (R3)
- **Nguồn**: [[SOURCE_ARCH_TIS_Thinking_in_Systems]] — (RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074.md)
- **Fact-check**: Các phân tích về dao động của vòng lặp hàng tồn kho.
