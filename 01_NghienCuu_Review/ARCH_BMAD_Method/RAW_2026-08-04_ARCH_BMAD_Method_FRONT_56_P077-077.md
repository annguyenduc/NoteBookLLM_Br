# HD SOURCE: ARCH_BMAD_Method_FRONT_56_P077-077
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_56
Part Title: NONE
Chapter Title: NONE
Section Title: 5.11 ma trận quyết định: Chọn workflow nào?
Chunk Range: Pages 77 to 77
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Quy tắc thực tế :

Đã biết rõ build gì và cho ai → Product Brief

Cần validateýtưởng trước khi đầu tưthời gian → PRFAQ

## 5.10 đầu ra phân tích feed vào lập kế hoạch

Sau khi hoàn thành Giai đoạn Phân tích, các tài liệu này trở thành bối cảnh cho Giai đoạn Lập Kế Hoạch :

```
brainstorming-session{ngày}.md  ─┐ marketresearch.md               ─┤→ PM Agent đọc khi tạo PRD domainresearch.md               ─┤ technicalresearch.md            ─┤→ Architect Agent đọc khi tạo kiến trúc productbrief.md                 ─┘→ Foundation cho PRD prfaq-{tên-dự -án}.md             ──→ Foundation cho PRD
```

Lợiích cụthể : Khi PM Agent chạy bmad-create-prd , nó sẽyêu cầu bạn load những tài liệu nghiên cứu này. Với bối cảnh đó, PRD được tạo ra:

Không hỏi lại những gì đã được nghiên cứu

Personas phảnánh cảm nhận thịtrường thực tế Requirements aligned với ràng buộc lĩnh vực Được inform bởi tính khả thi kỹ thuật

Nếu nhiều tài liệu nghiên cứu lớn, hãy dùng bmad-distillator đểnén trước khi feed vào PRD creation, tiết kiệm context window mà không mất thông tin.

## 5.11 ma trận quyết định: Chọn workflow nào?

```
Bạn có ýtưởng sản phẩm mới chưa được xác nhận? → PRFAQ (kiểm tra căng thẳng trước khi đầu tưnguồn lực) Bạn đã có ýtưởng rõnhưng chưa document? → Product Brief (nhanh hơn PRFAQ) Bạn cần hiểu bức tranh thịtrường? → Market Research Bạn build cho lĩnh vực phức tạp (y tế , pháp lý, tài chính)? → Domain Research bắt buộc Bạn không chắc tech stack nào phù hợp? → Technical Research trước khi kiến trúc Bạn bịtắc về ýtưởng hoặc hướng đi tính năng? → Brainstorming
```