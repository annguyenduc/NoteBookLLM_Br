# HD SOURCE: ARCH_BMAD_Method_FRONT_72_P090-090
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_72
Part Title: NONE
Chapter Title: NONE
Section Title: 7.5 ba chiến lược ngăn ngừa xung đột agent
Chunk Range: Pages 90 to 90
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
## Adr-001: Chiến lược thiết kếAPI **Bối cảnh:** Người dùng cần cập nhật real-time cho dữ liệu analytics. Đội có kinh nghiệm cả REST và GraphQL. Nhiều loại client (web, mobile) cần dùng API. **Các phươngán đã xem xét:** 1. REST API -Ưu: Đơn giản, được hiểu rõ, caching dễ -Nhược: Overfetching, nhiều roundtrips cho queries phức tạp 2. GraphQL -Ưu: Queries linh hoạt, single endpoint, strong typing -Nhược: Caching phức tạp, học tập tốn thời gian, N+1 cần xử lýcẩn thận 3. Kết hợp (REST cho đơn giản, GraphQL cho phức tạp) -Ưu: Tốt nhất từ cả hai -Nhược: Phức tạp thêm, patterns không nhất quán **Quyết định:** Dùng GraphQL cho tất cả giao tiếp client-server **Lý do:** Mobile clients cần queries tốiưu để giảm data transfer. PRD yêu cầu real-time subscriptions (GraphQL native). Đội có kinh nghiệm GraphQL từ dự án trước. **Hậu quả :** - Tất cảagents PHẢI dùng GraphQL mutations/queries (không có REST endpoints cho client) - Cần Apollo Serverở backend, Apollo Clientởfrontend - Phải implement DataLoader để tránh vấn đềN+1 - Hỗ trợ Subscription cần thiết cho tính năng real -time
```

## Các chủ đềADR quan trọng nhất Đây là danh sách những quyết định nên được document lại đểngăn ngừa xung đột:

| Chủ đềADR                  | Xung đột nóngăn ngừa                              |
|------------------------------|-----------------------------------------------------|
| Kiểu API (REST vs GraphQL) | Agent A dùng REST, Agent B dùng GraphQL             |
| Quyước đặt tên database    | snake_case vs camelCase vs PascalCase               |
| Quản lý state              | Redux vs Zustand vs React Context                   |
| Pattern xử lý lỗi         | try/catch vs handler tập trung                    |
| Cách tiếp cận xác thực | JWT vs Session vs OAuth                             |
| Cấu trúc thưmục           | Components trong /components vs /features vs /pages |
| Patterns kiểmthử          | Tỷ lệUnit vs Integration vs E2E                  |
| Cách import                  | Named imports vs default imports                    |

## 7.5 ba chiến lược ngăn ngừa xung đột agent