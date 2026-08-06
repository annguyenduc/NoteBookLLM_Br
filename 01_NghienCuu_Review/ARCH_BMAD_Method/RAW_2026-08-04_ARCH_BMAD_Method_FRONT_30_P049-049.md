# HD SOURCE: ARCH_BMAD_Method_FRONT_30_P049-049
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_30
Part Title: NONE
Chapter Title: NONE
Section Title: Lỗi cúpháp YAML khi tùy chỉnh
Chunk Range: Pages 49 to 49
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
ls _bmad/ # 2. thưmục _bmad-output/ tồn tại (trống làok) ls _bmad-output/ # 3. files tích hợp IDE tồn tại ls .claude/commands/ | grep bmad  # hoặc ls .cursor/rules/ # 4. bmad-help hoạt động # Gõ trong IDE: Bmad-help
```

Nếu bmad-help không được nhận diện, kiểm tra:

Bạn đang mở đúng thưmục dự án trong IDE chưa?

```
Files .claude/commands/ (hoặc .cursor/rules/ ) cótồn tại không?
```

Thử restart IDE

## 3.9 xử lýcác lỗi phổ biến

## Lỗi: "command not found: bmad-help"

Nguyên nhân: IDE chưa nhận diện được skill files.

## Cách sửa:

Restart IDE

```
Kiểm tra skill files: Gõ lệnh ls .claude/commands/ | grep bmad trong terminal Nếu files không có, chạy lại: npx bmad-method install → chọn Quick Update
```

## Lỗi: "phiên bản Node.js quácũ"

## Cách sửa:

```
# Dùng nvm để cài Node.js phiên bản 20 nvm install 20 nvm use 20 node --version  # Phải hiển thị v20.x.x hoặc cao hơn
```

Nếu chưa cónvm, tải Node.js trực tiếp từ trang chủnodejs.org.

## Cài xong nhưng skills không hoạt động Đảm bảo bạn mở đúng thưmục dự án trong IDE, không phải thưmục cha

```
Thưmục .claude/ hoặc .cursor/ phải nằm trong cùng thưmục với _bmad/ Chạy lại: npx bmad-method install → Quick Update
```

## Lỗi cúpháp YAML khi tùy chỉnh