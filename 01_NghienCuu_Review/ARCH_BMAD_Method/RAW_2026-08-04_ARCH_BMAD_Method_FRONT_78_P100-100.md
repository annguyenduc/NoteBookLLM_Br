# HD SOURCE: ARCH_BMAD_Method_FRONT_78_P100-100
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 1
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_78
Part Title: NONE
Chapter Title: NONE
Section Title: Những gì developer agent làm
Chunk Range: Pages 100 to 100
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Có sự khác biệt quan trọng cần hiểu:

Story trong file epic = Tên vàmôtảngắn gọn đủ để lập kế hoạch vàước tính, không đủ để triển khai.

Story sau `bmad-create-story` = Tài liệu đầy đủ với đủ bối cảnh để Developer Agent triển khai trong một session mà không cần hỏi thêm câu hỏi.

Đây làmục đích của bmad-create-story :

"Mở rộng epic story thành file story đầy đủ với đủ bối cảnh để triển khai trong một session."

## Tiêu chuẩn "sẵn sàng phát triển"

Trước khi bmad-dev-story , story phải đápứng tiêu chuẩn này:


![[ARCH_BMAD_Method_FRONT_78_fig_00.png]]


```
User story rõ ràng: "Với tưcách là [ai], tôi muốn [gì], để [tại sao]" Tiêu chíchấp nhận cụthể và cóthể kiểm chứng Ghi chú kỹ thuật tham chiếu đúng các quyết định kiến trúc Phụthuộc stories được liệt kêvà đã hoàn thành Định nghĩa hoàn thành rõ ràng Story đủnhỏ để tập trung trong một session
```

## Developer agent đọc gì?

Khi bmad-dev-story chạy, Developer Agent (James) đọc:

```
story[tên].md          ── Nhiệm vụngay trước mắt: làm gì cụthểarchitecture.md          ── Quyết định kỹ thuật đã được thống nhấprojectcontext.md       ── Quyước và patterns của dự án [Codebase hiện có]       ── Code thực tế đểfollow patterns
```

```
t
```

Đây là lý do tại sao bối cảnh tích lũy từ ba giai đoạn trước quan trọng đến vậy: Developer không cần hỏi lại, không cần mòmẫm, chỉ cần đọc và triển khai nhất quán.

## 8.4 dev story  -  triển khai

```
bmad-dev-story # Hoặc: bmad-agentdev  → gõ "DS"
```

Đây là bước triển khai thực sự -Developer Agent đọc story và triển khai code.

## Những gì developer agent làm