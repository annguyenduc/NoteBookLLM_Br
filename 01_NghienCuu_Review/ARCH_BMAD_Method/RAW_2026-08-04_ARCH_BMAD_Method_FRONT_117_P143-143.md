# HD SOURCE: ARCH_BMAD_Method_FRONT_117_P143-143
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_117
Part Title: NONE
Chapter Title: NONE
Section Title: Thói quen vệ sinh tài liệu
Chunk Range: Pages 143 to 143
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Bước 4: Verify

```
# Đọc index để đảm bảo all files được map cat _bmad-output/planning-artifacts/index.md # Kiểm tra không còn dangling references grep -r "architecture.md" _bmad-output/ | grep -v "architecture/"
```

## 12.6 chiến lược phòng ngừa: Duy trì tài liệu chất lượng

Tốt hơn là xử lýtài liệu lớn theo phảnứng. Dưới đây là thói quen duy trì chủ động:

## Tần suất đánh giá

| Thời điểm                  | Hành động                                                                      |
|------------------------------|---------------------------------------------------------------------------------|
| Cuối mỗi sprint          | Kiểm tra kích thước sprint-status.yaml và stories - archive completed stories |
| Saumỗi epic                | Retrospective→Cập nhật project- context.md→ Archive planning artifacts cũ    |
| Khi document đạt 300 dòng   | Cân nhắc cấu trúc lại trước khi reach 500                                 |
| Khi onboard team membermới | Chạy `bmad-index- docs` để đảm bảo navigation clear                        |

## Thói quen vệ sinh tài liệu

## Archive completed artifacts:

```
mkdir _bmad-output/archive/ mv _bmad-output/planning-artifacts/sprint-1-stories/* _bmad-output/archive/
```

## Không xóa  Archive để có lịch sử :

Completed stories chứa bài học quý giá. Archive, không xóa.

## Update index sau khi thêm documents:

Mỗi khi thêm tài liệu mới vào thưmục, chạy bmad-index-docs để cập nhật.