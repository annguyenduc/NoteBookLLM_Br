# HD SOURCE: ARCH_BMAD_Method_FRONT_59_P080-080
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_59
Part Title: NONE
Chapter Title: NONE
Section Title: Tạo PRD với PM agent
Chunk Range: Pages 80 to 80
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 6.2 PRD  -  tài liệu yêu cầu sản phẩm

## Tại sao PRD quan trọng?

PRD là hợp đồng giữa bạn và toàn bộ đội dự án  -  cả con người lẫn AI. Nó định nghĩa:

Ai làngười dùng và họcần gì Tính năng nào phải có (MVP), nên có (nice-to-have), vànhững gìnằm ngoài phạThành công của dự án trông nhưthếnào (chỉ sốcụthể Các giả định và ràng buộc

## Hậu quả của việc không cóPRD:

Architect thiết kế hệthống không biết phải tốiưu cho use case nào

Developer implement tính năng không biết thứtự Stories được tạo thiếu bối cảnh về giátrịPhạm vi dự án bịcreep không kiểưu tiên kinh doanh m soát

## Tạo PRD với PM agent

```
bmad-create-prd # Hoặc: bmad-agentpm    → gõ "CP" từ
```

```
menu
```

PM Agent (Amelia) sẽ dẫn dắt bạn qua một cuộc phỏng vấn cócấu trúc gồm năm giai đoạn:

## Giai đoạn A  -  Tải bối cảnh:

Agent tải các tài liệu phân tích nếu có (product-brief, market-research, v.v.). Nếu không có, agent hỏi từ đầu về bối cảnh dự án.

## Giai đoạn B  -  Nghiên cứu người dùng:

"Ai làngười dùng chính của sản phẩ

"Pain points cụthể của họ

"Họ đang giải quyết vấn đềnày bằng cách nào hiện tạ

"Điều gì sẽ khiến người dùng từ bỏ sản phẩm của bạ

```
m?" là gì?" i?" n?"
```

## Giai đoạn C Định nghĩa tính năng:

- "Tính năng nào là bắt buộc phải cócho MVP?"
- "Tính năng nào lànice -to-have cho phiên bản 1?"

"Tính năng nào chúng ta KHÔNG build và tại sao?"

m vi )