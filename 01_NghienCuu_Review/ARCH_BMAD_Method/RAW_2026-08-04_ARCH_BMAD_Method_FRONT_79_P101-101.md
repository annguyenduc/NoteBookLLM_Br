# HD SOURCE: ARCH_BMAD_Method_FRONT_79_P101-101
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_79
Part Title: NONE
Chapter Title: NONE
Section Title: Cơchế review
Chunk Range: Pages 101 to 101
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

n follow Đọc story file để hiểu yêu cầu và tiêu chíchấp nhận Đọc architecture.md để biết patterns kỹ thuật cầ Đọc projectcontext.md để biết quyước code cụthể Quét code hiện có để hiểu patterns đang được dùng Implement theo tiêu chíchấp nhận từng cái một Viết tests theo chiến lược testing trong kiến trúc Cập nhật sprint-status.yaml khi hoàn thành

## Hướng dẫn phiên dev story

## Bắt đầu phiên với context cụthể :

```
"Đây là dự án [tên]. Tôi đang triển khai Story 1.2. Kiến trúc có sẵn tại architecture.md. Project context tại project-context.md. Hãy đọc story-1-2-lam-moi-jwt-token.md và bắt đầu."
```

## Không bao giờ :

Bắt đầu với "Hãy code feature X" mà không có story Triển khai nhiều stories trong một session (mỗi story = một fresh chat) Cho phép agent bắt đầu mà không đọc project-context

## 8.5 code review đối nghịch

```
bmad-code-review # Hoặc: bmad-agent-
```

```
dev  → gõ "CR"
```

## Tại sao code review sau mỗi story?

Tài liệu chính thức:

"Follow-up review sau khi triển khai Story 2.3 hoàn thành. Hành động nhưmột reviewer hoài nghi."

Developer Agent triển khai code  Code Review Agent review code đótừ góc độ hoài nghi. Có sựtách biệt hoàn toàn về vai trò và quan điểm.

## Cơchế review

Giống nhưbmad-review-adversarial-general (xem Chương 4), nhưng tập trung vào code: