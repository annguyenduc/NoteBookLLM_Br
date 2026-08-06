# HD SOURCE: ARCH_BMAD_Method_FRONT_130_P157-157
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_130
Part Title: NONE
Chapter Title: NONE
Section Title: Khi nào cần BMad builder
Chunk Range: Pages 157 to 157
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 14.1 hệthống module: Kiến trúc mở rộng

BMad có kiến trúc module cho phép mở rộng theo nhu cầu:

```
BMad Core + BMM (Cài mặc định) │ ├── BMad Builder (bmb) -  Tạo custom agents vàworkflows ├── Creative Intelligence Suite (cis) -Đổi mới và sáng tạo ├── Game Dev Studio (gds) -  Phát triển game └── Test Architect TEA (tea) -  Kiểm thửenterprise
```

## Triết lýthiết kếThay vìmột framework nguyên khối cồng kềnh, BMad được thiết kếtheo nguyên tắc:

Bắt đầu nhỏ với Core + BMM đủ cho hầu hết dự án

Cài thêm chỉ khi thực sựcần

Mỗi module giải quyết một lĩnh vực cụthể , không overlap

## Cài đặt modules

```
# Từ đầu  -  chọn qua menu tương tác npx bmad-method install # Hoặc thêm module sau khi đã cài npx bmad-method install --modules tea --directory ./ --yes # Cài nhiều modules cùng lúc npx bmad-method install --modules bmm,tea,cis --tools claude-code --yes
```

## 14.2 BMad builder  -  tạo custom agents, workflows, vàmodules

Mã code cài đặt: bmb

## Môtả chính thức

"Tạo custom agents, workflows, và domain-specific modules với hỗ trợcó hướng dẫn. BMad Builder làmetamodule đểmở rộng framework."

Nói cách khác: BMad Builder cho phép bạn mở rộng BMad theo cách riêng -  tạo agents với persona tùy chỉnh hoàn toàn, thiết kếworkflows mới, đóng gói chúng thành module cóthể chia sẻ .

## Khi nào cần BMad builder