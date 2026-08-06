# HD SOURCE: ARCH_BMAD_Method_FRONT_69_P091-091
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_69
Part Title: NONE
Chapter Title: NONE
Section Title: Những anti-patterns cần tránh
Chunk Range: Pages 91 to 91
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Chiến lược 1  -  quyết định rõ ràng qua adrs

Document mọi lựa chọn kỹ thuật quan trọng liên quan đến nhiều epic:

Bối cảnh (tại sao quyết định này quan trọCác phươngán đã xem xét

Quyết định (cái gì được chọ Lý do (tạ Hậu quả (đánh đổi được chấp nhậ

```
ng) n) i sao) n)
```

## Chiến lược 2  hướng dẫn cụthể cho fr/nfr

Map các functional requirements đến cách tiếp cận kỹ thuật:

```
c Redis caching
```

```
FR-001: Xác thực người dùng → Dùng NextAuth.js với JWT FR-002: Dashboard realtime → Dùng WebSockets qua Socket.io NFR-001: Hiệu năng → Latency P95 dưới 200ms, bắt buộNFR-002: Bảo mật → Helmet.js, CORS được cấu hình, rate limiting
```

## Chiến lược 3  -  tài liệu tiêu chuẩn và quyước

Tài liệu rõ ràng về :

Cấu trúc thưmục (sơ đồ )

Quyước đặt tên (files, functions, variables, database)

Tổ chức code (feature-based vs layer-based)

Patterns kiểm thử (vịtrítest file, đặt tên, mục tiêu coverage)

## Những anti-patterns cần tránh

| Anti-pattern                                                   | Hậu quả                                                |
|----------------------------------------------------------------|-----------------------------------------------------------|
| **Quyết định ngầm định** - "Chúng ta sẽ xử lý khi gặp" | Mỗi agent ra quyết định độc lập →hỗn loạn         |
| **Over-documentation** - Documentmọi chi tiết nhỏnhặt  | Têliệt phân tích, tài liệu lỗi thời không ai đọc |
| **Kiến trúc cũ** - Viếtmột lần, không cập nhật      | Agents theo các patterns lỗi thời                     |