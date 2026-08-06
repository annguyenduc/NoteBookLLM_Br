# HD SOURCE: ARCH_BMAD_Method_FRONT_72_P094-094
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 2
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_72
Part Title: NONE
Chapter Title: NONE
Section Title: Hai sections chính
Chunk Range: Pages 94 to 94
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---


![[ARCH_BMAD_Method_FRONT_72_fig_00.png]]



![[ARCH_BMAD_Method_FRONT_72_fig_01.png]]


- Các khu vực coherent và được document tốt
- Lỗ hổng hoặc không nhất quán cần giải quyết
- Các vấn đềnghiêm trọng phải sửa trước khi triển khai

Quan trọng: Sửa tất cả vấn đềnghiêm trọng trước khi bắt đầu Giai đoạn 4.

## 7.8 project context  "điều lệ " của dự án

bmad-generate-project-context

Phần này đã được giới thiệuở Chương 2, nhưng trong bối cảnh Giai đoạn 3, đây là thời điểm tựnhiên nhất để tạo hoặc cập nhật nó  -  vì kiến trúc đã được xây dựng.

## Hai sections chính

## Section 1  -  Tech Stack và Phiên Bản:

```
## Tech stack và phiên bản - Node.js 20.x (LTS) - TypeScript 5.3 (strict mode bật) - React 18.2 - Quản lý state: Zustand (KHÔNG phải Redux  -  xem ADR-003) - Testing: Vitest (unit), Playwright (E2E), MSW (mock API) - Database: PostgreSQL 16 qua Prisma ORM
```

## Section 2  -  Quy Tắc Triển Khai Quan Trọng:

```
## Quy tắc triển khai quan trọng **Cấu hình TypeScript:** - Strict mode bật  -  không có kiểu `any` không có lý do rõ ràng - Dùng `interface` cho public APIs, `type` cho unions/intersections **Tổ chức code:** - Cấu trúc theo feature: /src/features/{tên-feature}/ - Components: Co-locate với test files .test.tsx **Gọi API:** - Dùng apiClient singleton  -  KHÔNG BAO GIỜ gọi fetch() trực tiếp - Tất cảasync operations PHẢI dùng handleError wrapper từ @/lib/errors **Cụthể vềframework:** - Route mới: theo file-based routing trong /src/app/ - Feature flags: dùng featureFlag() từ @/lib/flags - Database queries: LUÔN dùng Prisma, không bao giờ raw SQL
```