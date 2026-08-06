# HD SOURCE: ARCH_BMAD_Method_FRONT_127_P154-154
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_127
Part Title: NONE
Chapter Title: NONE
Section Title: Thực hành ngay
Chunk Range: Pages 154 to 154
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

"Quick Flow phát hiện quyước của bạn và hỏi: 'Tôi cónên theo quyước hiện cónày không?' Bạn quyết định: Có → Duy trìnhất quán với codebase hiện tại; Không → Thiết lập tiêu chuẩn mới (document lý do trong spec). BMM tôn trọng lựa chọn của bạn  -  nó sẽ không force modernization, nhưng nó sẽoffer nó."

## 13.7 ongoing maintenance: Thói quen sau onboarding

Sau khi đã setup, BMad dành cho dự án hiện cótrở thành continuous improvement loop:

```
New feature request ↓ Cónhỏ và rõ ràng không? Có → bmad -quick-dev Không → bmad -createprd → [chọn phases phù hợp] ↓ Sau khi implement: → Cập nhật project-context.md nếu cópatterns mới nổi lên → bmad -retrospective nếu làepic đáng kể
```

## Bốn thói quen quan trọng nhất

## Thói quen 1  -  Cập nhật project-context.md sau mỗi quyết định đáng kể :

File này là tài liệu sống. Mỗi khi team quyết định một convention mới, pattern mới, hay rule mới  -  thêm vào ngay.

## Thói quen 2  Archive completed artifacts thường xuyên:

Không để stale docs chất đống. Archive định kỳ để giữworkspace sạch sẽ .

## Thói quen 3  -  Chạy bmad-help khi không chắc:

Sau khi dọn dẹp hoặc thêm module mới, bmad-help sẽ quét lại và đề xuất bước phù hợp nhất.

## Thói quen 4  -  Fresh chat per workflow:

Đặc biệt quan trọng cho dự án hiện có  -  "baggage" từ previous context gây nhầm lẫn nhiều hơn trong môi trường complex.

## Thực hành ngay

## Bài tập: Onboard Dự Án Hiện Cócủa Bạn

Chọn một dự án đang chạy và thực hiện ba bước: