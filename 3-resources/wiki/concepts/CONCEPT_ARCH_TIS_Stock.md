---
file_id: "CONCEPT_ARCH_TIS_Stock"
title: "Kho chứa / Trữ lượng (Stock)"
type: "concept"
status: "DRAFT"
tags:
  - "SYS"
  - "components"
ai-first: true
confidence: 0.95
relationships:
  - type: "part_of"
    target: "[[CONCEPT_ARCH_TIS_System]]"
  - type: "is_affected_by"
    target: "[[CONCEPT_ARCH_TIS_Flow]]"
last_reconciled: "2026-05-18"
source_file: "RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC03_P034-041.md"
source_ref: "[[SOURCE_ARCH_TIS_Thinking_in_Systems]]"
created: "2026-05-18"
last_updated: "2026-05-18"
learning_status: "IN_PROGRESS"
next_review_date: "2026-05-21"
last_reviewed: "2026-05-20 15:33:59"
needs_practice_verification: true
---
## For future Claude (AI Preamble)
> Stock (Kho chứa/Trữ lượng) là các yếu tố có thể đo đếm được tại một thời điểm bất kỳ trong hệ thống. Nó đại diện cho bộ nhớ, trạng thái hiện tại và quán tính của hệ thống, thay đổi từ từ qua thời gian nhờ các Flow (Dòng chảy).

# Kho chứa / Trữ lượng (Stock)

## 1. Định nghĩa
**Kho chứa (Stock)** (còn gọi là trữ lượng, tài sản, trạng thái) là nền tảng của mọi hệ thống. Đó là các yếu tố trong hệ thống mà bạn có thể nhìn thấy, cảm nhận, đếm, hoặc đo lường tại một khoảng thời gian tĩnh bất kỳ. Stock không nhất thiết phải là vật chất; nó có thể là thông tin, sự tự tin, trí nhớ, hoặc uy tín.

## 2. Nguyên lý / Cấu trúc
- **Tích lũy:** Stock đóng vai trò như một bộ nhớ hoặc một sự tích lũy lịch sử của hệ thống. Nó thay đổi khi có sự chênh lệch giữa dòng chảy vào (inflow) và dòng chảy ra (outflow).
- **Quán tính (Inertia):** Kho chứa không thể thay đổi đột ngột. Nó hoạt động như một bộ đệm (buffer) hoặc giảm xóc, tạo ra sự chậm trễ (delay) trong hệ thống, giúp hệ thống ổn định và có thời gian phản ứng.
- **Tách rời luồng:** Stock cho phép dòng vào và dòng ra hoạt động không đồng bộ, tạo ra sự linh hoạt.

## 3. Ví dụ đối chiếu (R18: Double Examples)
### Ví dụ từ sách (Original)
> **Bối cảnh**: Nước trong một bồn tắm.
> **Ứng dụng**: Nước trong bồn là một Stock. Mức nước không thể ngay lập tức đầy hay cạn, nó phải từ từ tăng lên hoặc giảm đi phụ thuộc vào vòi nước (inflow) và lỗ xả (outflow).
> **Nguồn**: [[SOURCE_ARCH_TIS_Thinking_in_Systems]] — Chương 1

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Tích lũy kiến thức học tập.
> **Ứng dụng**: "Kiến thức của học sinh" là một Stock. Học sinh không thể giỏi ngay lập tức chỉ sau một đêm thức trắng (inflow quá nhanh), vì khả năng tiếp thu (inflow rate) và sự quên lãng (outflow rate) quyết định mức độ tích lũy thực sự.

## 4. Phản tư sư phạm (4F)
- **Facts**: Stock tạo ra quán tính và độ trễ.
- **Feelings**: Hiểu về Stock giúp giáo viên kiên nhẫn hơn với tiến độ học tập của học sinh.
- **Findings**: Để tăng Stock, có thể tăng Inflow HOẶC giảm Outflow.
- **Future**: Ứng dụng trong việc thiết kế lộ trình rèn luyện kỹ năng (giảm quên lãng để tăng trữ lượng).

## 5. Trích dẫn nguồn (R3)
- **Nguồn**: [[SOURCE_ARCH_TIS_Thinking_in_Systems]] — (RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC03_P034-041.md)
- **Fact-check**: Định nghĩa cơ bản về Stock.
