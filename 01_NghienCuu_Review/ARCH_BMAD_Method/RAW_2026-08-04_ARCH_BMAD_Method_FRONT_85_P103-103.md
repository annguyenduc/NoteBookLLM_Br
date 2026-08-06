# HD SOURCE: ARCH_BMAD_Method_FRONT_85_P103-103
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_85
Part Title: NONE
Chapter Title: NONE
Section Title: 8.8 retrospective sau epic
Chunk Range: Pages 103 to 103
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Kiểm tra dependencies của story tiếp theo Quyết định story tiếp theo trong sprint

## 8.7 đúng lộtrình khi scope thay đổi

```
bmad-correct-course # Hoặc: bmad-agentpm  → gọ
```

```
i "CC"
```

## Scope thay đổi là điều thường gặp

Trong thực tế, requirements luôn thay đổi trong quátrình phát triển. Đây không phải thất bại của quy trình đây là bình thường.

Vấn đề là: Khi requirements thay đổi mà không cập nhật tài liệu, các agent đọc thông tin lỗi thời và ra các quyết định không aligned với thực tếmới.

bmad-correct-course giải quyết điều này:

" bmad-correct-course truyền bácác thay đổi phạm vi qua tất cả tài liệu khi requirements thay đổi giữa chừng triển khai. Đảm bảo PRD, kiến trúc, stories, và sprintstatus được cập nhật nhất quán."

## Quy trình

```
Thay đổi scope (người dùng phản hồi, market shift, technical discovery) ↓ bmad-correct-course ↓ PM Agent: Cập nhật PRD (requirements affected) Architect Agent: Cập nhật kiến trúc (quyết định kỹ thuật affected) SM Agent: Cập nhật sprint-status và stories (scope change reflected) ↓ Tiếp tục với thông tin nhất quán
```

Nếu bạn skip bước này và chỉ "biết trong đầu" rằng requirements đã thay đổi  -  các agent tiếp tục đọc tài liệu cũ và triển khai theo scope cũ.

## 8.8 retrospective sau epic

```
bmad-retrospective # Hoặc: bmad-agent-
```

```
dev  → "ER"
```