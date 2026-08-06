# HD SOURCE: ARCH_BMAD_Method_FRONT_120_P147-147
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_120
Part Title: NONE
Chapter Title: NONE
Section Title: 13.1 tại sao dự án hiện cócần cách tiếp cận khác?
Chunk Range: Pages 147 to 147
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Chương 13: Dự án hiện có  -  onboarding BMad vào codebase sẵn có

## Bạn sẽ học được gì?

Sau khi đọc chương này, bạn sẽ hiểu: Tại sao dự án hiện cócần cách tiếp cận khác với dự án mới Ba bước chính thức đểonboard BMad vào codebase có sẵn Vai trò trung tâm của projectcontext.md đối với dự án hiện có Khi nào dùng Quick Flow và khi nào dùng Full Method cho dự án hiện cóCách hướng dẫn agents đọc đúng tài liệu khi bắt đầu workflow Công cụ bmad-document-project đểauto-document legacy codebase Các câu hỏi thường gặp từ tài liệu chính thức

## 13.1 tại sao dự án hiện cócần cách tiếp cận khác?

BMad Method được thiết kế để hoạt động tốt với cả dự án mới lẫn dự án đang chạy, nhưng cách tiếp cận có sự khác biệt căn bản.

## Dự án mới:

Bắt đầu từ tờ giấy trắng BMad dẫn dắt mọi quyết định từ đầu Phases 1-3 xây dựng bối cảnh từng bước

## Dự án hiện có:

Codebase đã tồn tại với patterns và quyước riêng Công nghệ đã được chọn, database schema đã tồn tại Rủi ro: Agents đưa ra quyết định không nhất quán với codebase hiện tại

## Thách thức cốt lõi:

"Trong dự án hiện có, AI agents cần hiểu những gì đã tồn tại trước khi thực hiện bất kỳ thay đổi nào. Không có bối cảnh này, agents đưa ra quyết định xung đột với kiến trúc, quyước đặt tên, và patterns hiện tại của bạn."

## Ví dụthực tế :

Codebase dùng snake\_case cho database columns → Agent không biết → Tạo column mới với camelCase → Inconsistency