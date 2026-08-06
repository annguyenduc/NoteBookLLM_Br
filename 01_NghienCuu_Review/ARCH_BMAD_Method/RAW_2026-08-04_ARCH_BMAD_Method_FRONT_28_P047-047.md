# HD SOURCE: ARCH_BMAD_Method_FRONT_28_P047-047
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_28
Part Title: NONE
Chapter Title: NONE
Section Title: Với GitHub Copilot
Chunk Range: Pages 47 to 47
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 3.5 cài thêm module sau khi đã cài ban đầu

Bạn không cần quyết định ngay từ đầu tất cả các modules. Cóthể thêm bất cứ lúc nào:

```
# Thêm module kiểm thửnpx bmad-method install --modules tea --directory ./ --yes # Hoặc chạy installer tương tác để xem options npx bmad-method install
```

Khi chạy lại installer trên project đã có BMad, bạn sẽ thấy options:

Cập nhật nhanh (Quick Update): Chỉ áp dụng những thay đổi mới  -  nhanh nhất, dùng khi cài thêm module hoặcáp dụng customization

Cài đặt lại toàn bộ ộ -  dùng khi gặp vấn đề Thêm module (Add Modules): Chỉ cài thêm modules mớ

(Full Reinstall): Tái cài toàn b i

## 3.6 cấu hình IDE sau khi cài

## Với Claude code

Sau khi cài, các BMad skills xuất hiện dưới dạng slash commands trong Claude Code:

```
# Gõ dấu / để thấy danh sách commands /bmad-help /bmad-create-prd /bmad-agent-pm
```

Hoặc gõ tên skill trực tiếp (không cần dấu gạch chéo):

```
bmad-help bmad-create-prd
```

## Với cursor IDE

Trong Cursor, các BMad rules được tự động inject vào system prompt. Gọi skills trong cửa sổ chat:

```
@bmad-help @bmad-create-prd
```

## Với GitHub Copilot