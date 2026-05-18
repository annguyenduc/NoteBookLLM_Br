---
file_id: "CONCEPT_ARCH_TIS_Stock_Flow_Diagram"
title: "Sơ đồ Kho chứa-Dòng chảy (Stock-Flow Diagram)"
type: "concept"
status: "DRAFT"
tags:
  - "SYS"
  - "model"
  - "visualization"
ai-first: true
confidence: 0.95
relationships:
  - type: "represents"
    target: "[[CONCEPT_ARCH_TIS_Stock]]"
  - type: "represents"
    target: "[[CONCEPT_ARCH_TIS_Flow]]"
  - type: "represents"
    target: "[[CONCEPT_ARCH_TIS_Feedback_Loop]]"
last_reconciled: "2026-05-18"
source_file: "RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC03_P034-041.md"
source_ref: "[[SOURCE_ARCH_TIS_Thinking_in_Systems]]"
created: "2026-05-18"
last_updated: "2026-05-18"
---

## For future Claude (AI Preamble)
> Stock-Flow Diagram (SFD) là ngôn ngữ trực quan chuẩn của System Dynamics dùng để biểu diễn hệ thống. Khác với sơ đồ luồng (flowchart) thông thường, SFD đặc biệt ở chỗ phân biệt rõ ràng giữa các "bồn chứa" (Stocks) và các "vòi nước" (Flows), đồng thời hiển thị các vòng lặp phản hồi.

# Sơ đồ Kho chứa-Dòng chảy (Stock-Flow Diagram)

## 1. Định nghĩa
**Sơ đồ Kho chứa-Dòng chảy (Stock-Flow Diagram - SFD)** là công cụ biểu diễn trực quan chuẩn mực của System Dynamics, dùng để vẽ bản đồ cấu trúc của một hệ thống. Nó sử dụng một bộ ký hiệu đặc trưng để biểu diễn Stock, Flow, Feedback Loop, và các biến phụ.

## 2. Nguyên lý / Cấu trúc (Ký hiệu chuẩn)
- **Hình chữ nhật (Rectangle):** Biểu diễn **Stock** (Kho chứa/Trữ lượng) — những thứ có thể tích lũy.
- **Mũi tên đôi (Double arrow / Valve):** Biểu diễn **Flow** (Dòng chảy) — tốc độ thay đổi của Stock. Các "van" điều chỉnh tốc độ của Flow.
- **Mũi tên thông tin (Information arrow):** Biểu diễn liên kết thông tin phản hồi (Feedback link). Thường là mũi tên thường.
- **Hình mây (Cloud):** Biểu diễn Nguồn (Source) hoặc Đích (Sink) của Flow nằm bên ngoài ranh giới hệ thống được mô hình hóa.
- **Chữ C hoặc R trên vòng lặp:** Biểu diễn Balancing (Cân bằng) hoặc Reinforcing (Tăng cường) loop.

## 3. Ví dụ đối chiếu (R18: Double Examples)
### Ví dụ từ sách (Original)
> **Bối cảnh**: Mô hình hóa hệ thống bồn nước của Meadows.
> **Ứng dụng**: Vẽ SFD cho bồn nước: **[Mực nước]** (Stock/Rectangle) được điều chỉnh bởi **→[Vòi vào]→** (Flow vào) và **→[Vòi ra]→** (Flow ra). Nhiệt kế báo mực nước (Information arrow) trở về van để điều chỉnh vòi ra. Vòng phản hồi này là Balancing loop (B) — hệ thống tự ổn định.
> **Nguồn**: [[SOURCE_ARCH_TIS_Thinking_in_Systems]] — Chương 1 (hệ thống bồn tắm)

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Mô hình hóa kiến thức học sinh.
> **Ứng dụng**: **[Kiến thức trong đầu]** (Stock) ← **→[Học mới]→** (Inflow: đọc sách, nghe giảng) và **→[Quên]→** (Outflow: theo thời gian). Giáo viên giỏi thiết kế Inflow đủ mạnh (ôn tập lặp lại - Spaced Repetition) để bù đắp Outflow (quên). SFD giúp trực quan hóa lý do vì sao ôn tập định kỳ quan trọng hơn học nhồi nhét.

## 4. Phản tư sư phạm (4F)
- **Facts**: SFD là ngôn ngữ trực quan; cùng một hệ thống có thể được diễn đạt bằng SFD hoặc bằng phương trình.
- **Feelings**: Lần đầu nhìn vào SFD có thể bối rối, nhưng khi quen rồi nó trở thành một "kính hiển vi" để nhìn vào cấu trúc hệ thống.
- **Findings**: SFD đặc biệt hữu ích khi cần giải thích tại sao một chính sách can thiệp không mang lại kết quả mong đợi — vẽ ra, bạn sẽ thấy vòng lặp đang đẩy ngược.
- **Future**: Thử vẽ SFD cho một vấn đề giáo dục thực tế bằng phần mềm Vensim hoặc Stella.

## 5. Trích dẫn nguồn (R3)
- **Nguồn**: [[SOURCE_ARCH_TIS_Thinking_in_Systems]] — Chương 1 (`CH01_SEC03_P034-041`)
- **Công cụ thực hành**: Vensim PLE (miễn phí), Insightmaker (web-based)
