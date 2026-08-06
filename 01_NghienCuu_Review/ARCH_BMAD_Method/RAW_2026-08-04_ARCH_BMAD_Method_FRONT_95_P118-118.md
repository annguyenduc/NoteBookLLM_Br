# HD SOURCE: ARCH_BMAD_Method_FRONT_95_P118-118
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_95
Part Title: NONE
Chapter Title: NONE
Section Title: Chạy hai lần cho nội dung quan trọng
Chunk Range: Pages 118 to 118
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Dấu hiệu của false positive:

"Cóthể tốiưu hơn" nhưng không có vấn đề về correctness Gợiýpattern khác nhưng pattern hiện tại nhất quán với code base Hiểu nhầmý định business của feature

## Dấu hiệu của vấn đề thật:

Logic cóthể trả về kết quả sai trong một số điều kiện Security vulnerability cóthể bị khai thác Performance issue cóthể ảnh hưởng đến SLAs đã cam kế

## Áp dụng cho nhiều loại artifact

Review Đối nghịch không chỉ cho code  -  áp dụng được cho:

## PRD:

"Requirements cómâu thuẫn nội bộ

"User stories có representative cho tất cả

"Success metrics cóthực sự đo lường đượ

## Architecture Document:

"Có single point of failure nào không được document không?" "ADRs cóthực sự giải quyết được vấn đề xung đột agent không?" "CóNFRs nào trong PRD không được địa chỉ trong kiế

## User Story:

"Tiêu chíchấp nhận có đủ để kiểm thử

"Có điều kiện biên nào bị bỏ

"Developer cóthể triển khai mà không cần hỏi thêm câu hỏ không?" personas không?" c không?"

n trúc không?"

không?" qua không?" i không?"

## Chạy hai lần cho nội dung quan trọng

Sau khi sửa các vấn đề từ lần đầu, chạy review lần hai. Hiệu suất giảm dần nhưng vẫn có giátrị :

Lần 1: Bắt được phần lớn vấn đề lớn

Lần 2: Bắt thêm vấn đề xuất hiện do thay đổi từ lần 1, vàmột số vấn đề bị bỏ sót

Lần 3+: Chỉ còn soi mói nhỏ, false positives cao hơn -  cóthể dừng

t