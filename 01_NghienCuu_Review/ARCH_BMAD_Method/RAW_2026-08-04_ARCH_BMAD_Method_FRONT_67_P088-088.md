# HD SOURCE: ARCH_BMAD_Method_FRONT_67_P088-088
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_67
Part Title: NONE
Chapter Title: NONE
Section Title: Quy trình khi chạy `bmad-create-architecture`
Chunk Range: Pages 88 to 88
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Và:

"Nếu bạn cónhiều epics cóthể được triển khai bởi các agents khác nhau, bạn cần giai đoạn thiết kế giải pháp."

Bảng so sánh chi phí sửa lỗi theo thời điểm:

| Thời điểmphát hiện                   | Chi phítương đối                                      |
|------------------------------------------|---------------------------------------------------------|
| Trong giai đoạn thiết kế giải pháp | 1x (chỉ cần sửa tài liệu)                        |
| Trong quátrình triển khai             | 10x (viết lại code qua nhiều session)             |
| Trong production                         | 50x trở lên (refactor lớn + tác động đến khách hàng) |

## 7.3 tài liệu kiến trúc  -  nền tảng bối cảnh chung

```
bmad-create-architecture # Hoặc: bmad-agent-
```

```
architect  → gõ "CA"
```

Architecture Document là "bối cảnh chung" mà tất cảagents đọc trước khi triển khai bất kỳ thứ gì.

```
PRD: "Cần build gì" ↓ Kiến trúc: "Build nhưthếnào" ↓ Agent A đọc kiến trúc → triển khai Epic 1 Agent B đọc kiến trúc → triển khai Epic 2 Agent C đọc kiến trúc → triển khai Epic 3 ↓ Kết quả : Triển khai nhất quán
```

## Quy trình khi chạy `bmad-create-architecture`

Architect Agent (Winston) sẽ :

```
Tải PRD.md vàux-spec.md (nếu có) Tải project-context.md nếu tồn tạ
```

```
i
```

Quét codebase hiện cónếu là dự án đã tồn tại

"Bắt gặp vấn đềalignment trong giai đoạn thiết kế giải pháp nhanh hơn mười lần so với phát hiện chúng trong quátrình triển khai."