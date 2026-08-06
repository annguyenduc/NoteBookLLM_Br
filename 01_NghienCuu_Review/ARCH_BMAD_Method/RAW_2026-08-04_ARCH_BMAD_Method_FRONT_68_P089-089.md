# HD SOURCE: ARCH_BMAD_Method_FRONT_68_P089-089
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_68
Part Title: NONE
Chapter Title: NONE
Section Title: Cấu trúc một ADR
Chunk Range: Pages 89 to 89
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Phỏng vấn bạn về các tùy chọn kỹ thuật Ra và document các quyết định kiến trúc

Tạo architecture.md

## Cấu trúc architecture document chuẩn

```
# Tài liệu kiến trúc  -  [tên dự án] ## 1. tổng quan hệthống -Sơ đồ kiến trúc cấp cao - Các components chính vàmối quan hệ ## 2. tech stack - Frontend: React 18 + TypeScript 5.3 - Backend: Node.js 20, Express.js - Database: PostgreSQL 16 - ... ## 3. records quyết định kiến trúc (adrs) - ADR-001: Chiến lược thiết kếAPI - ADR-002: Cách tiếp cận database schema - ADR-003: Quản lý state - ADR-004: Chiến lược xác thực - ... ## 4. kiến trúc hệthống - Cấu trúc thưmục - Ranh giới module -Sơ đồ luồng dữ liệu ## 5. kiến trúc dữ liệu - Tổng quan database schema - Quan hệ giữa các entities ## 6. thiết kếAPI -Phong cách và quyước API - Patterns endpoint ## 7. kiến trúc bảo mật - Cách tiếp cận xác thực - Bảo vệ dữ liệu ## 8. hạtầng và deployment - Cách tiếp cận hosting - Chiến lược CI/CD ## 9. chiến lược kiểm thử - Cách tiếp cận theo tháp kiểm thử - Mục tiêu test coverage
```

## 7.4 adrs  -  records quyết định kiến trúc

ADR là cốt lõi của Architecture Document  -  mỗi quyết định kỹ thuật quan trọng được document hóa.

## Cấu trúc một ADR