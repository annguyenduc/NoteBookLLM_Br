# HD SOURCE: ARCH_BMAD_Method_FRONT_46_P065-065
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_46
Part Title: NONE
Chapter Title: NONE
Section Title: Pattern 4 - pipeline phát triểnýtưởng
Chunk Range: Pages 65 to 65
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Tài liệu chính thức:

"Tạo hoặc cập nhật chỉmục của tất cả tài liệu trong một thưmục. Quét một thưmục, đọc từng file để hiểu mục đích, và tạo ra file index.md được tổ chức với liên kết vàmôtả ."

## Cơchế hoạt động

```
1. Quét thưmục mục tiêu → tất cảfiles khôngẩn 2. Đọc từng file → hiểu mục đích thực sự 3. Nhóm files → theo loại, mục đích, hoặc thưmục con 4. Tạo môtả → ba đến mười từmỗi file 5. Xuất index.md → được tổ chức với liên kết tương đố
```

```
i
```

Điểm quan trọng: Tool đọc nội dung file để hiểu mục đích thực sự , không chỉ dựa vào tên file.

## 4.13 các pattern kết hợp công cụ

## Pattern 1  -  bộ đảm bảo chất lượng kép

```
# Chạy cả hai để coverage trực giao: bmad-review-adversarialgeneral   # Review hoài nghi định hướng thái độ bmad-review-edge-case-hunter      # Truy vết cơhọc định hướng phương pháp # Kết hợp findings → coverage toàn diện
```

## Pattern 2  pipeline đánh bóng tài liệu

```
# Sau khi soạn thảo xong tài liệu: bmad-editorial-review-structure   # Sửa tổ chức trước # [áp dụng thay đổi cấu trúc] bmad-editorial-reviewprose       # Sau đó đánh bóng câu từ
```

## Pattern 3  -  quản lýtài liệu lớn

```
# Khi tài liệu vượt quánăm trăm dòng: bmad-shard-doc document-lon.md    # Chia nhỏ bmad-index-docs ./document-lon/   # Tạo chỉmục (cóthể đã được tạo tự động) # Sau đónếu cần cho LLM tiêu thụ : bmad-distillator                  # Nén từng section
```

## Pattern 4  -  pipeline phát triểnýtưởng

```
# Từ ýtưởng thô đến đầu ra cócấu trúc: bmad-brainstorming                   # Tạo hơn một trămýtưởng
```