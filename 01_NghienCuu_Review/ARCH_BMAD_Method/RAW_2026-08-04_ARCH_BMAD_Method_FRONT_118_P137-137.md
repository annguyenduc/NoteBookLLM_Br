# HD SOURCE: ARCH_BMAD_Method_FRONT_118_P137-137
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_118
Part Title: NONE
Chapter Title: NONE
Section Title: 12.2 công cụ 1: Bmad-shard-doc - chia nhỏ tài liệu
Chunk Range: Pages 137 to 137
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Chương 12: Quản lýtài liệu  -  sharding, distillation, vàindexing

## Bạn sẽ học được gì?

Sau khi đọc chương này, bạn sẽ hiểu: Vấn đề "tài liệu ngày càng lớn" và tại sao nócản trởAI Ba công cụ quản lýtài liệu lớn: Sharding, Distillation, Indexing Khi nào chia nhỏ, khi nào nén, khi nào đánh chỉmục Quy trình tốiưu hóa tài liệu lớn từ đầu đến cuối Chiến lược duy trì tài liệu chất lượng theo thời gian

## 12.1 tại sao tài liệu lớn là thách thức?

Dự án phát triển theo thời gian. Tài liệu cũng phát triển: PRD ban đầu hai mươi dòng → Sau ba tháng: ba trăm dòng Architecture document ban đầu năm mươi dòng → Sau sáu tháng: tám trăm dòng Research folder: mười file nhỏ → Sau một năm: năm mươi file Điều này tạo ra hai vấn đềnghiêm trọng:

## Vấn đề 1  -  Giới hạn context window của LLM:

Môhình AI có giới hạn về lượng text cóthể xử lýtrong một lần. Khi tài liệu vượt quá giới hạn đó, agent không thể load toàn bộ và phải chọn phần nào đọc  thường dẫn đến quyết định không đầy đủ .

## Vấn đề 2  -  Khảnăng điều hướng của con người:

Khi ai đócần tìm một quyết định kiến trúc cụthể trong file tám trăm dòng, họphải cuộtìm kiếm. Review trởnên chậm chạp và dễ bỏ sót.

BMad có ba công cụ để giải quyết hai vấn đềnày.

## 12.2 công cụ 1: Bmad-shard-doc  -  chia nhỏ tài liệu

bmad-shard-doc n và