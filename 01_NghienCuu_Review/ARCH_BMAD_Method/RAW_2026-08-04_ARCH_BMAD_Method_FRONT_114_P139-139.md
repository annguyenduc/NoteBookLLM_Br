# HD SOURCE: ARCH_BMAD_Method_FRONT_114_P139-139
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_114
Part Title: NONE
Chapter Title: NONE
Section Title: Điểm cốt lõi: Lossless không phải summary
Chunk Range: Pages 139 to 139
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
c architecture/)
```

```
Bạn muốn làm gì với architecture.md gốc? 1. Xóa (sections đã được đặt trong thưmụ 2. Archive (đổi tên thành architecture.md.archive) 3. Giữnguyên (duy trì cả hai)
```

## Khuyến nghịtừ kinh nghiệm thực tế :

Chọn Xóa nếu bạn tựtin vào việc chia nhỏ Chọn Archive nếu muốn cótham chiếu nhanh trong vài tuần đầ

```
u
```

Tránh Giữnguyên -  hai nguồn thông tin gây nhầm lẫn khi cập nhật

## Sau khi chia  -  cập nhật references

Nếu các tài liệu khác tham chiếu đến file gốc (ví dụ : stories tham chiếu architecture.md ), cần cập nhật sang tham chiếu mới. Kiểm tra bằng:

```
grep -r "architecture.md" _bmad-output/
```

## 12.3 công cụ 2: Bmad-distillator  -  nén lossless

bmad-distillator Đã được giới thiệu trong Chương 4. Phần này đi sâu vàoứng dụng thực tếtrong quản lýtài liệu.

## Hai trường hợp sử dụng chính

## Trường hợp 1  -  Tài liệu lớn cần load vào context:

Khi bạn cần feed một tài liệu lớn vào một workflow nhưng nó vượt quácontext window, distillator tạo ra phiên bản nén để load thay thế .

## Trường hợp 2  -  Nhiều tài liệu cần feed cùng lúc:

Trước khi bắt đầu bmad-create-prd , bạn cónăm tài liệu nghiên cứu. Distillator nén tất cả chúng vào một distillate cóthể load vào context cùng lúc.

## Điểm cốt lõi: Lossless không phải summary

Sự khác biệt được nhắc đến trong Chương 4 nhưng quan trọng đến mức cần nhấn mạnh lại: