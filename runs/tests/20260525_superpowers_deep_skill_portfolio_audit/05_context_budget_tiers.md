# Context Budget Tiers: Phân Tầng Ngân Sách Ngữ Cảnh Kỹ Năng

Báo cáo này thiết lập cơ chế phân tầng nạp kỹ năng động (Dynamic Skill Loading) để ngăn ngừa tình trạng phình ngữ cảnh (Context Bloat) và tối ưu hóa việc sử dụng Token Window của AI Agent.

## Phân Phối Tầng Ngữ Cảnh (Tiers)

- **Tier 0 — Always loaded (Luôn nạp mặc định):** Chỉ gồm các quy tắc rules cốt lõi tối thiểu và ranh giới an toàn của vault (`AGENTS.md`, `karpathy-core`). Dung lượng: **< 1,000 tokens**.
- **Tier 1 — Router only (Chỉ nạp để định tuyến):** Kỹ năng hướng dẫn Agent cách chọn lựa và kích hoạt các kỹ năng khác (`using-superpowers`, `workspace-routing.yaml`). Dung lượng: **~ 1,500 tokens**.
- **Tier 2 — Task-specific (Nạp động theo loại task):** Chỉ nạp khi prompt hoặc intent của người dùng khớp hoàn toàn với một nhóm công việc cụ thể. Dung lượng: **~ 3,000 - 5,000 tokens** tùy nhóm.
- **Tier 3 — Deep reference / audit only (Chỉ nạp khi audit/debug sâu):** Các tài liệu kỹ thuật, SOP hoặc hướng dẫn phát triển mở rộng. Chỉ nạp khi Agent cần tự nâng cấp kỹ năng hoặc sửa lỗi hệ thống phức tạp. Dung lượng: **> 8,000 tokens**.

---

## Bảng Phân Tầng Kỹ Năng Đề Xuất

Dưới đây là bảng định tầng tối ưu hóa cho danh mục kỹ năng của vault:

| Kỹ năng (Skill) | Vai trò hiện tại (Current Role) | Tầng đề xuất (Proposed Tier) | Lý do đề xuất (Reason) | Rủi ro phình ngữ cảnh (Token Risk) |
| :--- | :--- | :--- | :--- | :--- |
| **AGENTS.md** | Core law | **Tier 0** | Luật chơi và ranh giới an toàn tối cao bắt buộc phải có ở đầu mọi phiên. | **Low** (~300 tokens, tĩnh) |
| **karpathy-core** | Behavior guide | **Tier 0** | Đảm bảo tính kỷ luật Surgical Change được duy trì ngầm trong mọi lượt viết code. | **Low** (~200 tokens, tĩnh) |
| **using-superpowers** | Bootstrap | **Tier 1** | Chỉ cần dùng ở lượt đầu tiên để định hướng routing. | **Low** (Chỉ nạp 1 lần ở startup) |
| **cm-planning** | Core skill | **Tier 2** | Chỉ nạp khi bắt đầu task phát triển mới (Phase 0). | **Medium** (~1,200 tokens) |
| **writing-plans** | Core skill | **Tier 2** | Chỉ nạp khi bắt đầu thiết kế kỹ thuật (Phase 1). | **Medium** (~1,500 tokens) |
| **verification-before-completion** | Core skill | **Tier 2** | Chỉ nạp khi chuẩn bị hoàn tất và kiểm chứng code. | **Medium** (~1,000 tokens) |
| **wiki-ingest** | Domain skill | **Tier 2** | Chỉ nạp khi bắt đầu Ingest Lifecycle. | **Medium** (~1,200 tokens) |
| **process-raw-resource** | Domain skill | **Tier 2** | Chỉ nạp ở Preview Lane. | **Medium** (~1,000 tokens) |
| **pedagogy** | Domain skill | **Tier 2** | Chỉ nạp khi người dùng yêu cầu lộ trình học tập, slide. | **High** (~2,500 tokens do chứa slide framework) |
| **cm-notebooklm** | Support skill | **Tier 2** | Chỉ nạp khi đồng bộ lên NotebookLM. | **Low** (~800 tokens) |
| **wiki-rebuild** | Maintenance | **Tier 3** | Chỉ nạp khi có yêu cầu fix DB/Index gãy bán tự động. | **High** (~2,000 tokens) |
| **wiki-cleanup** | Maintenance | **Tier 3** | Chỉ nạp khi audit/dọn dẹp link gãy định kỳ tuần. | **High** (~2,500 tokens) |
| **wiki-status** | Audit | **Tier 3** | Chỉ nạp khi người dùng yêu cầu xem tình trạng sức khỏe vault. | **Medium** (~1,200 tokens) |
| **write-skill** | Internal tool | **Tier 3** | Chỉ nạp khi cần sửa đổi kỹ năng (SIP). | **High** (~3,000 tokens) |

---

## Phân Tích Rủi Ro Phình Ngữ Cảnh & Giải Pháp Tinh Gọn

### 1. Phình Ngữ Cảnh do Nạp Kỹ Năng Tĩnh (Static Loading Bloat)
- **Vấn đề:** Nếu Agent nạp đồng thời toàn bộ 44 kỹ năng ở startup, dung lượng ngữ cảnh riêng cho định hướng skill sẽ chiếm tới **~35,000 - 45,000 tokens**, chiếm mất 40% - 60% Context Window của các model lớn và gây cạn kiệt hoàn toàn đối với các model nhỏ. Việc này dẫn đến Agent phản hồi cực kỳ chậm và mất trí nhớ liên phiên.
- **Giải pháp:** Áp dụng **Dynamic Skill Loading Strategy** (Chiến lược nạp kỹ năng động):
  - Startup: Chỉ nạp **Tier 0** và **Tier 1** để định tuyến.
  - Sau lượt đầu tiên (Startup Phase): Agent sử dụng `using-superpowers` để phân tích prompt của người dùng, xác định đúng intent và **chỉ nạp các kỹ năng Tier 2 tương ứng**.
  - Tier 3 hoàn toàn bị cô lập: Chỉ được nạp khi có chỉ thị hoặc command cụ thể từ người dùng (ví dụ: `/rebuild` hay `/cleanup`).
  - Tích hợp chặt chẽ việc kiểm soát ngữ cảnh thông qua `cm-context-budget` để tự động giải phóng các kỹ năng Tier 2 đã hoàn thành vai trò ở các lượt trước.
