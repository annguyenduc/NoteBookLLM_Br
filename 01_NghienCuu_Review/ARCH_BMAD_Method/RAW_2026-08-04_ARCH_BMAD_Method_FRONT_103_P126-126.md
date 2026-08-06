# HD SOURCE: ARCH_BMAD_Method_FRONT_103_P126-126
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_103
Part Title: NONE
Chapter Title: NONE
Section Title: Thực hành ngay
Chunk Range: Pages 126 to 126
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 10.7 phối hợp các công cụ review

## Cho code (story hoàn thành)

```
bmad-codereview                   # Review đối nghịch tập trung code bmad-review-edge-case-hunter       # Truy vết đường đi # Kết hợp kết quả → sửa nghiêm trọng trước → triage trung bình/thấp
```

## Cho tài liệu quan trọng (prd, architecture)

```
bmad-review-adversarial-general    # Review hoài nghi toàn diện bmad-editorial-review-structure    # Cải thiện tổ chức # [áp dụng thay đổi cấu trúc] bmad-editorial-reviewprose        # Đánh bóng câu từ # [tùy chọn] bmad-advancedelicitation → pre -mortem
```

## Cho specs và kế hoạch (sau khi soạn thảo)

```
bmad-advanced-elicitation          # Premortem trước  -  tìm rủi roẩn # [cải thiện spec dựa trên pre-mortem] bmad-review-adversarialgeneral    # Sau đó review đối nghịch # [sửa các issues] bmad-review-edge-case-hunter       # Nếu spec có logic điều kiện
```

## Thực hành ngay

## Bài tập  -  Review Liên Tiếp:

Lấy một tài liệu bất kỳ (PRD, spec, story) và chạy theo thứtự :

```
# Bước 1: Tìm vấn đề tổng thể bmad-review-adversarial-general # → phân loại: Vấn đề thật vs false positive # Bước 2: Tìm edge cases (nếu có logic) bmad-review-edge-case-hunter # → review JSON output # Bước 3: Cải thiện cấu trúc bmad-editorial-review-structure # → áp dụng cắt bỏ , gộp, di chuyển # Bước 4: Đánh bóng văn xuôi bmad-editorial-review-prose # Bước 5: Kiểm tra rủi roẩn bmad-advanced-elicitation # → chọn pre-mortem
```

```
-  tìm unhandled cases
```