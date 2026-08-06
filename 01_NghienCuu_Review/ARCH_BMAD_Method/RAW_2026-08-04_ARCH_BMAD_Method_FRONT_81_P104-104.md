# HD SOURCE: ARCH_BMAD_Method_FRONT_81_P104-104
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_81
Part Title: NONE
Chapter Title: NONE
Section Title: Năm nguyên tắc thiết kếChunk Range: Pages 104 to 104
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Mục đích kép

Học hỏi team: Ghi lại bài học kinh nghiệm, điều gì hoạt động tốt, điều gì cần cải thiện. Cập nhật "điều lệ ": project-context.md được cập nhật với patterns và quyước mới được khám phátrong quátrình triển khai.

## Tại sao cập nhật project context quan trọng?

Trong quátrình triển khai, bạn phát hiện ra: Pattern tốt hơn cho error handling Quyước đặt tên hợp lý hơn trong context cụthểAnti-pattern cần tránh Performance tricks cho dataset kích thước thực tếNhững patterns này cần được đưa vào project-context.md để các agent trong epic tiếtheo tự động biết và áp dụng .

Không có retrospective → Mỗi epic bắt đầu lại từ đầu → Không bao giờ cócải tiến tích lũy.

## 8.9 quick dev  -  sáng kiến triển khai nhẹ

```
bmad-quick-dev # Hoặc: bmad-agentdev  → "QD"
```

## Triết lýTài liệu chính thức môtả Quick Dev: "Quick Dev: Intent in, code out, minimal human-in-the-loop. Compress your intentions into the smallest, clearest, most contradiction-free spec possible, route once to the right approach, then let it run." a con

Dịch nghĩa thực tế: "Đưa vàoý định, nhận được code ra, giảm tối thiểu sự giám sát củngười."

## Năm nguyên tắc thiết kế

## Nguyên tắc 1  Néný định trước:

Không phải "viết code cho tính năng X". Mà là: spec ngắn, rõ ràng, không mâu thuẫn. AI hiểu được ngay lập tức.

p