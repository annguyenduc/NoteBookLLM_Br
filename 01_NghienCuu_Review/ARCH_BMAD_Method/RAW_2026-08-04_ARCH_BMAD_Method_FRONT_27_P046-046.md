# HD SOURCE: ARCH_BMAD_Method_FRONT_27_P046-046
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 1
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_27
Part Title: NONE
Chapter Title: NONE
Section Title: 3.4 cấu trúc files được tạo ra
Chunk Range: Pages 46 to 46
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Một số ví dụthực tế

```
# Cài đặt cơbản nhất  -  chỉ core + BMM, dùng với Claude code npx bmad-method install --directory ./ --modules bmm --tools claude-code --yes # Cài với module kiểm thử -  phù hợp choứng dụng web vàmobile npx bmad-method install --directory ./ --modules bmm,tea --tools cursor --yes # Cài full stack cho nhóm phát triển game npx bmad-method install --directory ./ --modules bmm,gds --tools claude-code --yes # Cài cho nhóm product cần sáng tạo và xây dựng custom tools npx bmad-method install --directory ./ --modules bmm,cis,bmb --tools claude-code --yes # Cài tất cảmodules npx bmad-method install --directory ./ --modules bmm,bmb,tea,gds,cis --tools claude-code -yes
```

## Dùng phiên bản thửnghiệm

```
npx bmad-method@next install --directory ./ --modules bmm --tools claude-code --yes
```

Phiên bản @next chứa các tính năng mới nhất nhưng cóthể có bug. Dùng cho môi trường development để tiếp cận tính năng mới sớm, không dùng cho production.

## 3.4 cấu trúc files được tạo ra

Sau khi cài đặt thành công, đây lànhững gì xuất hiện trong dự án của bạn:


![[ARCH_BMAD_Method_FRONT_27_fig_00.png]]
