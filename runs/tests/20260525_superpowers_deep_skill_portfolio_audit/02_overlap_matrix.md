# Overlap Matrix: Đánh Giá Sự Chồng Chéo Kỹ Năng

Báo cáo này phân tích chi tiết các nhóm kỹ năng có chức năng gần nhau, phân loại mức độ chồng chéo, chỉ ra rủi ro vận hành và khuyến nghị giải pháp xử lý cụ thể cho từng nhóm.

| Nhóm chồng chéo (Group) | Kỹ năng liên quan (Skills) | Loại chồng chéo (Overlap Type) | Rủi ro (Risk) | Khuyến nghị hành động (Recommended Action) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Planning / Brainstorming** | `brainstorming`, `cm-planning`, `writing-plans`, `executing-plans` | **Trigger & Responsibility overlap** (Chồng chéo điều kiện kích hoạt và trách nhiệm ở Phase 0) | **High** (Dễ làm Agent bối rối không biết nên kích hoạt brainstorming hay cm-planning khi bắt đầu phiên nháp) | **Merge** brainstorming vào `cm-planning` làm Phase 0 thống nhất. Giữ `writing-plans` làm Phase 1 và `executing-plans` làm Phase 2. |
| **2. TDD / Verification** | `cm-tdd`, `verification-before-completion`, `cm-quality-gate` | **Output & Process overlap** (Chồng chéo ở khâu xác minh chất lượng cuối cùng) | **High** (Agent viết code lặp lại việc kiểm chứng nhiều lần, gây phí token và kéo dài phiên không cần thiết) | **Merge** `cm-tdd` vào `verification-before-completion` làm quy chuẩn xác minh chung. **Chuyển đổi** `cm-quality-gate` thành rule vận hành tĩnh. |
| **3. Wiki Ingest & Process** | `wiki-ingest`, `process-raw-resource`, `wiki-hd-convert`, `wiki-rebuild`, `wiki-query` | **Responsibility overlap** (Quy trình nạp dữ liệu bị phân mảnh thành quá nhiều skill nhỏ) | **Medium** (Rối loạn ranh giới giữa Ingestion và Retrieval; rebuild không nên là skill tự động kích hoạt) | Giữ `wiki-ingest` và `process-raw-resource` với ranh giới rõ (Preview vs Ingest). **Chuyển đổi** `wiki-rebuild` thành workflow bán tự động. |
| **4. Learning Pack & Pedagogy** | `wiki-learning-pack`, `pedagogy`, `wiki-to-deliverable` | **Output overlap** (Cùng sinh ra các gói tài liệu học tập, giáo án từ Atom) | **Medium** (Gây phình ngữ cảnh do nạp cả 3 skill khi người dùng muốn học một tài liệu) | Giữ `wiki-learning-pack` cho Spaced Repetition/học nhanh. Giữ `pedagogy` phục vụ chuyên sâu tạo Giáo án/Slide. Gom đầu ra tổng hợp Markdown của deliverable vào `wiki-to-deliverable`. |
| **5. Agent Tooling** | `mcp-builder`, `prompt-master`, `write-skill` | **Adjacent but clean** | **Low** (Không có chồng chéo lớn, phân nhiệm rõ ràng) | Giữ nguyên cả 3 kỹ năng hỗ trợ phát triển này. |
| **6. Scout / Search** | `references`, `wiki-query`, `wiki-semantic-search` | **Trigger overlap** (Cùng mục tiêu tìm kiếm tri thức) | **Medium** (Agent dễ chạy song song cả keyword search và semantic search khi gặp câu hỏi trừu tượng) | Thiết lập ranh giới rõ ràng: Ưu tiên `wiki-query` cho tìm kiếm từ khóa chính xác/đồ thị; tự động chuyển đổi sang `wiki-semantic-search` nếu kết quả trả về rỗng. Thư mục `references` đổi tên/cách ly. |
| **7. Governance** | `wiki-absorb`, `wiki-council`, `wiki-learning-audit` | **Process overlap** | **Medium** (Đôi khi Council bị kích hoạt sớm khi chưa cần weighted consensus) | Giữ nguyên. Thiết lập trigger tự động của `wiki-council` chỉ khi `wiki-absorb` báo cáo mâu thuẫn tri thức (`CONTRADICTS` edge) không thể tự gộp. |
| **8. Workspace Isolation** | `using-superpowers`, `subagent-driven-development` | **Boundary overlap** | **Low** (using-superpowers là bootstrap đầu phiên; subagent điều phối chạy song song) | Giữ nguyên. Tích hợp định tuyến workspace vào bootstrap. |
| **9. Context & Token** | `cm-context-budget`, `cm-continuity` | **Responsibility overlap** (Cùng quản lý ngữ cảnh phiên làm việc) | **High** (Hao tốn token khi duy trì cả hai skill chạy ngầm liên tục) | Giữ `cm-context-budget` làm core skill quản lý Token. **Chuyển đổi** `cm-continuity` thành rule vận hành tĩnh (ghi nhận CONTINUITY.md ở Session End). |

---

## High-risk overlaps

### Nhóm 1: Planning & Brainstorming
- **Bằng chứng chồng chéo:** Cả `brainstorming` và `cm-planning` đều tự nhận vai trò làm rõ ý định của người dùng và thiết kế spec nháp ở đầu phiên. Cả hai đều có trigger nhạy bén với prompt dạng: *"Tôi muốn xây dựng tính năng X..."* hay *"Hãy lên ý tưởng cho Y..."*.
- **Rủi ro:** Agent sẽ kích hoạt đồng thời cả hai skill, dẫn đến sinh ra hai bản kế hoạch spec nháp chồng chéo nhau trong Context, gây lãng phí khoảng 1,500 - 3,000 token ngay đầu phiên.
- **Giải pháp đề xuất:** Gom hoàn toàn `brainstorming` vào `cm-planning`. Bản kế hoạch Phase 0 của `cm-planning` sẽ bao gồm luôn bước khám phá ý định và brainstorming giải pháp.

### Nhóm 2: TDD & Verification Discipline
- **Bằng chứng chồng chéo:** `cm-tdd` tự nhận quy trình viết test tự động và sửa lỗi đệ quy, trong khi `verification-before-completion` bắt buộc chạy test kiểm chứng trước khi hoàn tất. Cả hai cùng yêu cầu Agent viết kịch bản test và chạy kiểm định local.
- **Rủi ro:** Khi sửa một script nhỏ, Agent sẽ bị cuốn vào vòng lặp của TDD trước, sau đó lại tiếp tục chạy thêm một vòng xác minh của verification-before-completion. Việc này gây lặp quy trình và lãng phí cực lớn Token Window (bloat context).
- **Giải pháp đề xuất:** Merge `cm-tdd` vào `verification-before-completion`. Quy trình kiểm chứng trước khi hoàn thành sẽ tích hợp sẵn cơ chế tự sửa lỗi đệ quy (self-healing loop) nếu phát hiện lỗi kiểm thử.

---

## Medium-risk overlaps

### Nhóm 3: Retrieval & Search (`wiki-query` vs `wiki-semantic-search`)
- **Bằng chứng chồng chéo:** Khi người dùng đặt câu hỏi tra cứu kiến thức, cả hai skill tìm kiếm này đều có trigger kích hoạt rất nhạy.
- **Rủi ro:** Agent sẽ gọi song song cả hai công cụ tìm kiếm keyword và semantic search, sinh ra lượng kết quả trùng lặp lớn trong Context.
- **Giải pháp đề xuất:** Tạo ranh giới cứng: Agent luôn chạy `wiki-query` trước để tìm kiếm chính xác và duyệt đồ thị Wiki Graph. Chỉ khi không tìm thấy hoặc kết quả nghèo nàn mới kích hoạt `wiki-semantic-search` để quét ngữ nghĩa diện rộng.

### Nhóm 4: Context & Continuity (`cm-context-budget` vs `cm-continuity`)
- **Bằng chứng chồng chéo:** Cả hai đều hướng tới việc bảo toàn và ghi nhận trạng thái ngữ cảnh phiên làm việc.
- **Rủi ro:** Việc kích hoạt liên tục hai kỹ năng này chạy ngầm gây tốn tài nguyên. Thực tế, `cm-continuity` chỉ cần chạy một lần duy nhất ở Session End, do đó không nên cấu hình nó như một skill active thường trực.
- **Giải pháp đề xuất:** Gom `cm-continuity` thành một Quy tắc vận hành tĩnh (Rule) được kích hoạt bắt buộc tại Session End thay vì một skill chủ động. Giữ `cm-context-budget` làm skill chạy ngầm duy nhất để liên tục kiểm soát ngân sách token trong phiên.

---

## Low-risk overlaps

### Nhóm 5: Agent Tooling (`mcp-builder`, `prompt-master`, `write-skill`)
- **Bằng chứng & Phân tích:** Các kỹ năng này có phạm vi hoạt động cực kỳ chuyên biệt và độc lập (MCP builder làm việc với server, prompt-master tinh chỉnh prompt, write-skill để viết/edit skill). Ranh giới giữa chúng rất sạch sẽ và không có chồng chéo đáng kể.

---

## Non-overlap but adjacent skills
- **`references` (Thư mục) và các skill tìm kiếm:** Thư mục `.agent/skills/references` thực chất không chứa tệp `SKILL.md` hay logic kỹ năng nào, mà chỉ là thư mục chứa các tài liệu tham chiếu (tài liệu Gemini, SOP, v.v.). Việc đặt nó trong `skills/` dễ làm Agent hiểu nhầm đây là một kỹ năng có thể kích hoạt. Cần di chuyển thư mục này ra khỏi `skills/` để làm sạch danh mục kỹ năng của vault.
