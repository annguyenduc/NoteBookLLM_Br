---
file_id: "CONCEPT_ARCH_TIS_Feedback_Loop"
title: "Vòng lặp phản hồi (Feedback Loop)"
type: "concept"
status: "DRAFT"
tags:
  - "SYS"
  - "mechanism"
ai-first: true
confidence: 0.95
relationships:
  - type: "is_a"
    target: "[[CONCEPT_ARCH_TIS_Balancing_Feedback]]"
  - type: "is_a"
    target: "[[CONCEPT_ARCH_TIS_Reinforcing_Feedback]]"
last_reconciled: "2026-05-18"
source_file: "RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC04_P042-043.md"
source_ref: "[[SOURCE_ARCH_TIS_Thinking_in_Systems]]"
created: "2026-05-18"
last_updated: "2026-05-18"
---

## For future Claude (AI Preamble)
> Vòng lặp phản hồi là cơ chế mà thông tin về mức độ của Stock phản hồi lại để kiểm soát Inflow hoặc Outflow của chính Stock đó. Đây là cách các hệ thống tự điều chỉnh và tạo ra các hành vi phức tạp qua thời gian.

# Vòng lặp phản hồi (Feedback Loop)

## 1. Định nghĩa
**Vòng lặp phản hồi (Feedback Loop)** là một chuỗi khép kín các mối liên kết nhân quả, trong đó một sự thay đổi ở trạng thái của Kho chứa (Stock) sẽ truyền thông tin qua hệ thống để tác động lên Dòng chảy (Flow), từ đó tiếp tục làm thay đổi trạng thái của chính Kho chứa đó.

## 2. Nguyên lý / Cấu trúc
Hệ thống không chỉ vận hành theo chuỗi nguyên nhân - kết quả tuyến tính (A -> B -> C), mà thông qua các vòng lặp (A -> B -> C -> A). 
- Thông tin về trạng thái hiện tại luôn là đầu vào cho quyết định về dòng chảy trong tương lai.
- Vòng lặp phản hồi có thể duy trì sự cân bằng của hệ thống (Balancing) hoặc khuếch đại sự phát triển/suy thoái (Reinforcing).
- Vòng lặp phản hồi giải thích tại sao một hệ thống có khả năng tự vận hành, tự duy trì hoặc tự phá hủy từ bên trong mà không cần tác nhân can thiệp từ bên ngoài.

## 3. Ví dụ đối chiếu (R18: Double Examples)
### Ví dụ từ sách (Original)
> **Bối cảnh**: Bộ điều nhiệt (Thermostat) điều khiển máy sưởi.
> **Ứng dụng**: Nhiệt độ phòng (Stock) giảm xuống -> Bộ điều nhiệt nhận thông tin -> Bật máy sưởi (Inflow) -> Nhiệt độ tăng lên -> Bộ điều nhiệt ngắt máy sưởi.
> **Nguồn**: [[SOURCE_ARCH_TIS_Thinking_in_Systems]] — Chương 1

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Vòng lặp nhận xét và làm bài.
> **Ứng dụng**: Học sinh nộp bài tập (Flow) -> Điểm số và nhận xét (Thông tin về Stock) được gửi lại cho học sinh -> Dựa vào điểm số, học sinh điều chỉnh cách học và nỗ lực (Flow mới). Quá trình này tạo ra một vòng lặp giúp năng lực của học sinh tự điều chỉnh.

## 4. Phản tư sư phạm (4F)
- **Facts**: Mọi hệ thống phức tạp đều tồn tại nhờ các vòng lặp phản hồi.
- **Feelings**: Việc nhận diện được các vòng lặp ẩn giấu mang lại cảm giác làm chủ hệ thống sâu sắc.
- **Findings**: Thiết kế một vòng lặp phản hồi thông tin (ví dụ: dashboard tiến độ học tập minh bạch) hiệu quả hơn việc ra lệnh.
- **Future**: Xây dựng cơ chế phản hồi nhanh (rapid feedback loops) trong các sản phẩm công nghệ giáo dục.

## 5. Trích dẫn nguồn (R3)
- **Nguồn**: [[SOURCE_ARCH_TIS_Thinking_in_Systems]] — (RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC04_P042-043.md)
- **Fact-check**: Cơ chế vòng lặp phản hồi cốt lõi của System Dynamics.
