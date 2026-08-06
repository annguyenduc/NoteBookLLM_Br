# HD SOURCE: ARCH_BMAD_Method_FRONT_19_P038-038
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_19
Part Title: NONE
Chapter Title: NONE
Section Title: 2.7 tại sao không được sửa `_bmad/` trực tiếp
Chunk Range: Pages 38 to 38
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
## Tech stack và phiên bản - Node.js 20.x (LTS) - TypeScript 5.3 (strict mode bật) - React 18.2 - State Management: Zustand (KHÔNG dùng Redux  -  xem ADR-003) - Testing: Vitest (unit), Playwright (E2E), MSW (API mocking) - Database: PostgreSQL 16 qua Prisma ORM
```

## Phần 2  -  Quy Tắc Triển Khai Quan Trọng:

```
## Quy tắc triển khai quan trọng **TypeScript:** - Strict mode bật  -  không dùng kiểu `any` không có lý do - Dùng `interface` cho public APIs, `type` cho union/intersection types **Cấu trúc code:** - Feature-based: /src/features/{tên-feature}/ - Co-locate test files với source: ComponentName.test.tsx **VềAPI:** - Gọi API: LUÔN dùng apiClient singleton  -  không bao giờ gọi fetch() trực tiếp - Xử lý lỗi: dùng handleError wrapper từ @/lib/errors **Database:** - LUÔN dùng Prisma  -  không bao giờ viết raw SQL - Column names: snake_case
```

## 2.7 tại sao không được sửa `\_bmad/` trực tiếp Đây là quy tắc vàng được nhắc đến nhiều lần trong tài liệu chính thức vì đây là lỗi phổ biến nhất:

"Luôn dùng các file \_.customize.yaml\_ thay vì sửa agent files trực tiếp. Installer ghi đèagent files khi cập nhật, nhưng bảo toàn các thay đổi \_.customize.yaml\_ của bạn."

Khi bạn chạy npx bmad-method install đểnâng cấp lên phiên bản mới:

```
Bị ghi đè: Toàn bộnội dung trong _bmad/agents/*.md Được bảo toàn: Tất cảfiles trong _bmad/_config/agents/*.customize.yaml
```

Vì vậy:

## Sai  -  sẽmất sau khi nâng cấp:

```
nano _bmad/agents/bmmpm.md  # Không làm điề
```

```
u này!
```

## Đúng -được bảo toàn qua mọi lần nâng cấp: