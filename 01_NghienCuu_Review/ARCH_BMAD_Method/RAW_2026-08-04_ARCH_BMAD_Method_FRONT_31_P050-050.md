# HD SOURCE: ARCH_BMAD_Method_FRONT_31_P050-050
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_31
Part Title: NONE
Chapter Title: NONE
Section Title: Tóm tắt chương 3
Chunk Range: Pages 50 to 50
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Sau khi sửa file .customize.yaml và chạy lại install thì báo lỗi:

Dùng công cụ validate YAML trực tuyến nhưyaml.me hoặc các công cụtương tựYAML rất nhạy cảm với indentation (khoảng trắng thụt đầu dòng)  -  dùng spaces, không dùng tabs

Mọi key phải có dấu cách sau dấu hai chấm: name: 'Giátrị ' không phải name:'Giátrị '

## Thực hành ngay

Bài tập thực hành  Cài đặt và thửnghiệm đầu tiên:

```
# 1. điều hướng đến dự án cd /đường/dẫn/đến/dự -án-của-bạn # 2. cài đặt npx bmad-method install # 3. chọn: Module BMM + IDE bạn đang dùng # 4. verify trong IDE bmad-help # 5. thử hỏi bằng ngôn ngữ tựnhiên bmadhelp Tôi có ýtưởng về ứng dụng quản lýchi tiêu. Bắt đầu từ đâu?
```

## Tóm tắt chương 3

```
Yêu cầu: Node.js v20 trở lên, một AI Code IDE (Claude Code hoặc Cursor đượ dùng) Cài đặt tương tác: Chạy npx bmad-method install và làm theo hướng dẫn Cài đặt tự động: npx bmad-method install --directory ./ --modules bmm -tools claude-code --yes Mã code modules: bmm (bắt buộc), bmb , tea , gds , cis Mã code IDE: claude-code , cursor , copilot , codex Phiên bản thửnghiệm: npx bmad-method@next install Xác nhận: Gõ bmad-help trong IDE  -  thấy recommendations là thành công Tùy chỉnh: Luôn dùng file .customize.yaml , không bao giờ sửa trực tiếp _bmad/ Khi gặp lỗi: Restart IDE → Kiểm tra files → Chạy Quick Update
```

```
c khuyên
```