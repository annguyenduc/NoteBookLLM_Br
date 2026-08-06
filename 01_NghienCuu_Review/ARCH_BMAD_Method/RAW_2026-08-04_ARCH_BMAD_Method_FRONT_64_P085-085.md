# HD SOURCE: ARCH_BMAD_Method_FRONT_64_P085-085
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_64
Part Title: NONE
Chapter Title: NONE
Section Title: Thực hành ngay
Chunk Range: Pages 85 to 85
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Giữa các phần của quátrình tạTrước khi chuyển từ PRD sang kiếTrong quátrình tạo story trước khi chuyển sang triểo PRD n trúc n khai

## 6.7 lập kế hoạch feed vào thiết kế giải pháp

Sau khi hoàn thành Giai đoạn Lập kế hoạch:

```
PRD.md          → Architect Agent đọc để hiểu "cần build gì" uxspec.md      → Architect Agent xem xét khi thiết kế kiến trúc frontend projectcontext.md → Nếu đã có (dự án hiện có), architect tôn trọng các tùy chọ
```

## Quyết định tiếp theo:

```
Nếu dự án cónhiều epics: → Giai đoạn 3 Thiết kế giải pháp (bắt buộc) Nếu dự án nhỏ với một đến hai epics: → Cóthể cân nhắc bỏ qua kiến trúc chi tiết (thận trọng) Nếu là Quick Flow: → bmad-quick-dev ngay
```

## Thực hành ngay

## Bài tập 1  -  Tạo PRD Cho Dự Án Thực:

Chuẩn bịtrả lời bốn câu hỏi này trước khi chạy workflow:

Ai làngười dùng chính? (Cụthểnhất cóthể -  không phải "mọi người") Ba pain points hàng đầu của họ là gì? Ba tính năng bắt buộc phải cócho MVP là gì? Chỉ sốnào sẽ đo lường thành công sau ba tháng? Sau khi cócâu trả lời:

```
bmad-create-prd
```

Và đểagent dẫn dắt từ đó.

## Bài tập 2  -  Self-Review PRD:

Sau khi PRD được tạo, đọc lại toàn bộ với câu hỏi: "Nếu tôi làArchitect và chỉ đọc tài liệu này, tôi có đủ thông tin để bắt đầu thiết kế hệthống không?" Xác định các lỗ hổng còn tồn tại.

```
n
```