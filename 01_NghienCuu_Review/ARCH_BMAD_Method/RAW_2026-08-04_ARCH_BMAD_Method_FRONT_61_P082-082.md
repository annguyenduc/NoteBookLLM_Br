# HD SOURCE: ARCH_BMAD_Method_FRONT_61_P082-082
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_61
Part Title: NONE
Chapter Title: NONE
Section Title: Review chéo chức năng (góc nhìn kiến trúc)
Chunk Range: Pages 82 to 82
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Khi bắt đầu bmad-create-prd , agent hỏi về tài liệu hiện có. Load product-brief.md vàmarket-research.md ngay lập tức.

Với tài liệu phân tích, phiên tạo PRD nhanh hơn và sâu hơn -  PM Agent không cần hỏi lại những gì đãnghiên cứu.

## 6.3 advanced elicitation trong quátrình tạo PRD

Tại các checkpoint trong quátrình phỏng vấn, PM Agent sẽ hỏi:

```
"Bạn cómuốn chạy Advanced Elicitation để làm sâu thêm phân tích không? (Có/Không)"
```

Nếu chọn Có, agent đề xuất năm phương pháp phù hợp nhất:

Pre-mortem: "Giả sử PRD này dẫn đến thất bại dự án. Tại sao?"

Bản đồ stakeholder: "Đánh giá lại từ góc nhìn của từng bên liên quan"

v.v.

Đây là cách tốt nhất để phát hiện lỗ hổng trong requirements trước khi cam kết vào kiến trúc .

## 6.4 xác nhận PRD  review đối nghịch

Sau khi PRD được tạo, bước tiếp theo được khuyến nghị là review nótừ hai góc độ khác nhau.

## Review tựthẩm định (của PM agent)

```
bmad-agentpm  → gõ "VP" (Validate PRD)
```

PM Agent đóng vai người review hoài nghi. Bắt buộc phải tìm ra vấn đề -  không thểapprove ngay. Tập trung vào: tính đầy đủ , nhất quán, rõ ràng.

## Review chéo chức năng (góc nhìn kiến trúc)

Mời Architect Agent vào Party Mode hoặc phiên riêng:

```
bmad-party-mode # Topic: "review PRD này từ góc độ kỹ thuậ # Tìm những gì sẽ gây khó khăn khi triể
```

```
t  n khai"
```