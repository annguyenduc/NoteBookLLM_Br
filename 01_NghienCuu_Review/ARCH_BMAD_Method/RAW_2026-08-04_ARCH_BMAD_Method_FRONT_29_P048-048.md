# HD SOURCE: ARCH_BMAD_Method_FRONT_29_P048-048
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 1
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_29
Part Title: NONE
Chapter Title: NONE
Section Title: 3.8 xác nhận cài đặt đầy đủ Chunk Range: Pages 48 to 48
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
# Trong Copilot chat:
```

```
bmad-help
```

## Với codex cli

```
# Trong terminal: codex "bmad-help"
```

## 3.7 nâng cấp từ phiên bản cũ lên phiên bản 6

Nếu bạn đang dùng BMad phiên bản 5 hoặc cũ hơn:

## Bước 1: Sao lưu dữ liệu

```
# Sao lưu tất cả tài liệu đầu ra
```

```
cp -r _bmad-output/ _bmad-output-backup/
```

## Bước 2: Chạy nâng cấp

```
npx bmad-method install # Chọn "nâng cấp lên v6" khi được hỏ
```

```
i
```

## Những thay đổi quan trọng nhất trong phiên bản 6

| Điều thay đổi             | Phiên bản cũ                   | Phiên bản 6               |
|----------------------------|---------------------------------|-----------------------------|
| Tên file đặc tảUX       | `ux-design.md`                  | `ux-spec.md`                |
| Hệthống tùy chỉnh    | Sửa trực tiếp agent files | Chỉ dùng `.customize.yaml` |
| Module code cho game       | (tên cũ khác nhau)              | `gds`                       |
| Cấu trúc `_bmad-output/` | Khác                            | Được tái tổ chức        |

## 3.8 xác nhận cài đặt đầy đủ Chạy checklist kiểm tra này sau khi cài đặt:


![[ARCH_BMAD_Method_FRONT_29_fig_00.png]]


1. thưmục \_bmad/ tồn tại