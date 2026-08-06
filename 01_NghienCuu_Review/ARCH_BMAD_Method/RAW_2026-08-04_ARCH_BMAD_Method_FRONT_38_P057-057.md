# HD SOURCE: ARCH_BMAD_Method_FRONT_38_P057-057
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_38
Part Title: NONE
Chapter Title: NONE
Section Title: Thưviện phương pháp
Chunk Range: Pages 57 to 57
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

| `--validate`   | Không (flag)   | -   | Chạy kiểmtra vòng tròn   |
|----------------|----------------|-----|------------------------------|

## Khi nào dùng

Tài liệu quá lớn để load toàn bộ vào context window của LLM Cần phiên bản tiết kiệm token của research, specs, planning artifacts Muốn xác minh không cóthông tin bịmất trong quátrình nén Chuẩn bịnhiều tài liệu nghiên cứu đểfeed vào phiên tạo PRD

## 4.6 bmad-advanced-elicitation  -  lần xem lại cócấu trúc

## Vấn đề với "hãy làm lại, tốt hơn"

Khi bạn nói với AI "Hãy cải thiện nội dung này" hoặc "Làm tốt hơn đi", AI không biết cần cải thiện theo chiều nào  nên thường tạo ra bản sửa đổi generic không khác gì bản gốc.

Tài liệu chính thức giải thích tại sao advanced elicitation hiệu quả hơn:

"Một phương pháp được đặt tên buộc AI tấn công từmột góc cạnh cụthể , khám phánhững insights màmột lần thử lại generic sẽ bỏ lỡ ."

## Cách hoạt động

```
[Workflow tạo ra đầu ra  -  phần PRD, quyết định kiến trúc, user story] ↓ AI đề xuất: "Bạn cómuốn chạy Advanced Elicitation không?" ↓ AI đề xuất năm phương pháp phù hợp nhất dựa trên loại nội dung ↓ Bạn chọn một phương pháp (hoặc xem thêm lựa chọn khác) ↓ AIáp dụng phương pháp đó -  hiện kết quả cải thiện ↓ Bạn: Chấp nhận, bỏ qua, hoặc chạy phương pháp khác
```

## Thưviện phương pháp

| Phương pháp                    | Môtả                                                       | Phù hợp nhất với                |
|--------------------------------|--------------------------------------------------------------|---------------------------------------|
| **Phân tích Pre-mortem**       | Giả sử dự án đã thất bại, làm ngược lại nguyên nhân | Specs, kế hoạch - tìm rủi roẩn |
| **Tưduy nguyên lý đầu tiên** | Bỏ hết giả định, xây lại từ sựthật căn bản       | Quyết định kiến trúc              |