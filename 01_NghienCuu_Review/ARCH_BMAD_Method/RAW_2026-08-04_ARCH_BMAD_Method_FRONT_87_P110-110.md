# HD SOURCE: ARCH_BMAD_Method_FRONT_87_P110-110
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_87
Part Title: NONE
Chapter Title: NONE
Section Title: Kịch bản 3 - phân tích sau sựcốChunk Range: Pages 110 to 110
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Ai sẽ tham gia: Architect (technical feasibility), PM (business constraints), Developer (implementation complexity), Tech Writer (documentation impact).

Kết quả điển hình: Winston (Architect) đề xuất event streaming với Kafka. James (Developer) chỉ ra learning curve và đề xuất Redis Streams đơn giản hơn. Amelia (PM) nhắc nhở về timeline sáu tháng và hỏi phươngán nào đạt được trong thời hạn. Từ cuộc thảo luận này, quyết định được đưa ra cónhiều yếu tố được cân nhắc hơn bất kỳagent đơn nào cóthể làm.

## Kịch bản 2  -  tổng kết sprint / lập kế hoạch

Tình huống: Sau khi hoàn thành một epic, toàn đội cần nhìn lại và lập kế hoạch tiếp.

## Cách chạy:

```
bmad-party-mode "Sprint 2 vừa hoàn thành. Dashboard cơbản đã hoạt động. Kết quả : -Hoàn thành chín trong mười một stories - Hai stories bị delay: export PDF (kỹ thuật phức tạp hơn dự kiến) và phân quyền nâng cao (requirements không rõ ràng) Hãy retrospective và lập kế hoạch Sprint 3."
```

## Ai sẽ tham gia:

Amelia sẽ tập trung vào yêu cầu chưa rõ ràng và customer value Winston sẽ phân tích tại sao PDF export phức tạp hơn dự kiến James sẽước tính lại effort

Sage (Tech Writer) sẽnhắc về docs pending

Lợiích: Tất cả "stakeholders" aligned trong một phiên thay vìnhiều phiên riêng lẻ .

## Kịch bản 3  -  phân tích sau sựcốTình huống: Production bug hoặc sựcố xảy ra, cần tìm nguyên nhân gốc rễmà không đổ lỗi.

## Cách chạy:

```
bmad-party-mode "Hệthống xác thực bị gián đoạn tám giờ sáng qua suốt hai giờ . Timeline: - 08:00: Deploy v2.3.1 (chỉ cóinfrastructure changes) - 08:15: Bắt đầu nhận error reports từ customers - 08:45: Rollback về v2.3.0 - 08:47: Hệthống phục hồi
```