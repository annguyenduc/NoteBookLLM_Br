# HD SOURCE: ARCH_BMAD_Method_FRONT_71_P093-093
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_71
Part Title: NONE
Chapter Title: NONE
Section Title: Đầu ra
Chunk Range: Pages 93 to 93
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Hướng dẫn kích thước

| Quy môdự án     | Gợiý                                                               |
|-------------------|-----------------------------------------------------------------------|
| Nhỏ (Quick Flow) | Năm đến mười lăm stories tổng cộng, không cần epics chính thức |
| BMad Method       | Hai đến sáu epics, tám đến hai mươi stories mỗi epic                 |
| Enterprise        | Sáu epics trở lên, theo dõi epic/story chính thức bắt buộc     |

## 7.7 kiểm tra sẵn sàng triển khai

```
bmad-check-implementation-readiness
```

```
# Hoặc: bmad-agentpm  → "IR" bmad-agentarchitect  → "IR"
```

Từ tài liệu chính thức, đây là bước Được Khuyến NghịCao.

Đây là review chéo tài liệu cótính đối nghịch -  kiểm tra tính coherent giữa tất cả tài liệu lập kế hoạch trước khi bắt đầu triển khai.

## Nó kiểm tra gì?

## Coherent PRD ↔ Kiến trúc:

- "PRD yêu cầu real-time updates, kiến trúc có kế hoạ

"NFRs về bảo mật có được giải quyế

## Coherent Kiến trúc ↔ Stories:

- "Stories cótham chiếu đúng các quyết định kiến trúc không?"

"Technical notes trong stories cónhất quán với ADRs không?"

## Coherent phạm vi:

- "Stories có bao phủ tất cảfunctional requirements trong PRD không?"
- "Có requirements nào trong PRD chưa được map vào bất kỳ story nào không?"

## Đầu ra

Báo cáo xác nhận liệt kê:

ch cho WebSockets không?" t trong security architecture không?"