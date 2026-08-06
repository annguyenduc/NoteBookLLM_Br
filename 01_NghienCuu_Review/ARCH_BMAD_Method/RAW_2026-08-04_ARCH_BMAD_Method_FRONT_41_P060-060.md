# HD SOURCE: ARCH_BMAD_Method_FRONT_41_P060-060
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_41
Part Title: NONE
Chapter Title: NONE
Section Title: Điểm mấu chốt: Trực giao
Chunk Range: Pages 60 to 60
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

"VìAI được hướng dẫn tìm vấn đề , nó SẼ tìm ra vấn đề -  kể cả khi không tồn tại. Hãy kỳ vọng false positives: những soi mói nhỏnhặt được ngụy trang thành vấn đề hiểu lầm về ý định, hoặc lo lắng hoàn toàn do AI tưởng tượng ra. Bạn quyết đị gì là thật."

Đây không phải lỗi đây là đánh đổi cóchủ đích. Tốt hơn là có ba false positive mà bạ lọc, còn hơn bỏ sót một lỗ hổng bảo mật thật.

## Lặp lại review

Sau khi khắc phục các vấn đề , hãy chạy review lần hai. Lần hai thường bắt được thêm. Lần ba cũng không vôích. Nhưng theo thời gian, lợi nhuận giảm dần  -  chỉ còn những soi mói nhỏnhặt vàfalse findings.

## 4.8 bmad-review-edge-case-hunter  -  truy tìm edge cases Môtả Tài liệu chính thức:

"Đi qua mọi đường rẽ và điều kiện biên, báo cáo chỉnhững trường hợp chưa được xử lý. Phương pháp truy vết đường đi thuần túy, cơhọc phân loại các edge class. Trực giao với review đối nghịch  theo phương pháp, không theo thái độ ."

## Điểm mấu chốt: Trực giao

Tài liệu chính thức nhấn mạnh:

"Chạy cả bmad-review-adversarial-general và bmad-review-edge-case-hunter cùng nhau để cócoverage trực giao. Review đối nghịch bắt các vấn đề chất lượng và tính đầy đủ ; edge case hunter bắt các đường đi chưa được xử lý."

| Review Đối Nghịch    | Edge Case Hunter                           |                                          |
|-------------------------|--------------------------------------------|------------------------------------------|
| **Cách tiếp cận**   | Theo thái độ (hoài nghi cay đắng)         | Theo phương pháp (truy vết cơhọc)     |
| **Tìm thấy**          | Vấn đề chất lượng, tính năng còn thiếu | Edge cases, điều kiện biên chưa xử lý |
| **Định dạng đầu ra** | Danh sách findings dạng văn xuôi          | Mảng JSON                              |
| **Trùng lặp?**        | Rấtít                                   | Rấtít                                 |

, nh cái n