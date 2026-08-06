# HD SOURCE: ARCH_BMAD_Method_FRONT_20_P036-036
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_20
Part Title: NONE
Chapter Title: NONE
Section Title: 2.6 project context - "điều lệ" của mọi dự án
Chunk Range: Pages 36 to 36
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Bạn chỉ cần nhớ và gõ skill name . Tất cả phần còn lại xảy ra tự động.

## 2.5 nguyên tắc fresh chat  -  quy tắc quan trọng nhất

Nếu bạn chỉnhớmột điều từ chương này, hãy nhớ điều này:

Mỗi workflow hoặc agent session phải được chạy trong một cuộc hội thoại mới, riêng biệt với cửa sổ context sạch.

## Tại sao fresh chat quan trọng?

AI có giới hạn về context window  lượng thông tin cóthể xử lýtrong một lần. Khi một cuộc hội thoại kéo dài qua nhiều workflow, hai vấn đề xảy ra:

Vấn đề 1  -  Ônhiễm context: Thông tin từworkflow nàyảnh hưởng đến quyết định của workflow tiếp theo theo những cách không mong muốn. Ví dụ: Khi agent đang tạo PRD vẫn còn "nhớ " rằng bạn muốn dùng React vì đã đề cập trong brainstorming session, nócóthể ảnh hưởng đến PRD theo cách không được kiểm soát.

Vấn đề 2  -  Context window bịthu lại: Khi context quá dài, model bắt đầu "quên" những gì ở đầu cuộc hội thoại  thường lànhững gì quan trọng nhất nhưyêu cầu và ràng buộc cốt lõi.

## Áp dụng nguyên tắc fresh chat

| Tình huống                             | Làm gì                                         |
|------------------------------------------|------------------------------------------------|
| Chạy `bmad-create-prd`                 | Mở cuộc hội thoại mới                 |
| Xong PRD, bắt đầu architecture         | Mở cuộc hội thoại mới                 |
| Xong architecture, bắt đầu mỗi story | Mở cuộc hội thoại mới                 |
| `bmad-code-review` sau khi dev story     | Mở cuộc hội thoại mới                 |
| Party Mode cho một chủ đề cụthể    | Dùng CÙNG cuộc hội thoại trong session đó |
| Tiếp tục thảo luận cùng chủ đề  | Dùng CÙNG cuộc hội thoại                 |

## 2.6 project context  "điều lệ " của mọi dự án

project-context.md làfile đặc biệt nhất trong BMad. Tài liệu chính thức gọi nó là "constitution"  điều lệcủa dự án.