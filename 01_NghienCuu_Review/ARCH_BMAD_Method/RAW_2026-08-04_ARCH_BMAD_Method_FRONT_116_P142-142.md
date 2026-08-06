# HD SOURCE: ARCH_BMAD_Method_FRONT_116_P142-142
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_116
Part Title: NONE
Chapter Title: NONE
Section Title: Bước 3: Thực hiện
Chunk Range: Pages 142 to 142
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Khi nào chạy

Sau khi tạo thưmục mới với nhiều tài liệu

Sau khi chia nhỏmột document lớn bằng bmad-shard-doc

Khi thêm tài liệu mới vào thưmục cóindex cũ (để cập nhật index)

Định kỳ khi thưmục phát triển đáng kể

## 12.5 quy trình tốiưu hóa tài liệu toàn diện

Dưới đây làworkflow hoàn chỉnh khi tài liệu dự án trởnên khó quản lý:

## Bước 1: Đánh giá

```
# Kiểm tra kích thước files wc -l _bmad-output/**/*.md | sort -rn | head -20 # Tìm files lớn nhất (ngưỡng 500 dòng) find _bmad-output -name "*.md" -exec wc -l {} + | sort -rn | head -10
```

## Bước 2: Phân loại

Với mỗi file lớn, quyết định:

```
File quá lớn (> 500 dòng)? Cónhiều sections độc lập? → Dùng bmad -shard-doc File lớn nhưng làmột document thống nhất? Cần load vào LLM context? → Dùng bmad -distillator Thưmục cónhiều files khónavigate? → Dùng bmad -index-docs
```

## Bước 3: Thực hiện

```
# Cho tài liệu cần chia nhỏ bmad-shard-doc _bmad-output/planning-artifacts/architecture.md # Cho thưmục research (nhiều files cần nén đểfeed vào prd) bmad-distillator \ source_documents="./research/" \ downstream_consumer="Architect cần biết tech constraints vàmarket gaps" \ token_budget="Giảm còn 40% gốc" \ --validate # Sau khi chia, tạo index bmad-index-docs _bmad-output/planning-artifacts/
```