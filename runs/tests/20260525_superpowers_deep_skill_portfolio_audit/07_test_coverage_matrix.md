# Test Coverage Matrix: Đánh Giá Độ Phủ Kiểm Thử Kỹ Năng

Báo cáo này phân tích tình trạng phủ kiểm thử (test coverage) của các kỹ năng hoặc nhóm kỹ năng trong vault, đối chiếu trực tiếp với bộ test skeleton tại `.agent/tests/` và đề xuất các bài kiểm tra hồi quy còn thiếu.

| Kỹ năng / Nhóm kỹ năng (Skill / Group) | Đã có test case (Has Test) | Các test case hiện có (Existing Tests) | Các test case còn thiếu (Missing Tests) | Độ ưu tiên của test thiếu (Priority) |
| :--- | :--- | :--- | :--- | :--- |
| **Wiki Learning Pack** | Yes | `T001_pdf_summary_learning_pack`, `T002_pdf_summary_no_ingest` | - Kiểm định learning summary với yêu cầu xuất file artifact cụ thể.<br>- Yêu cầu ingest canonical tường minh từ chat để xem có tuân thủ workflow không. | **Medium** |
| **Skill Governance (`write-skill`)** | Yes | `T003_skill_edit_requires_sip` | - Sửa đổi rules cốt lõi (như `AGENTS.md`) có bắt tạo đề xuất SIP hay Rule-Review không. | **High** |
| **Engineering / Code Change** | Yes | `T004_code_change_requires_plan` | - Xác thực self-healing đệ quy của TDD khi test crash.<br>- Thay đổi nhiều khối không liên tục trong file lớn bằng cm-core-edit-pro. | **Medium** |
| **Canonical Ingest** | Yes | `T005_ingest_requires_source_lock` | - Quét nguồn từ thư mục inbox có bị bỏ qua gate audit hay không.<br>- Kiểm chứng ghi đè Atom trùng lặp khi chạy absorb. | **High** |
| **Workflow / Source Prep** | Yes | `T001_prepare_source_vs_ingest` | - Chuyển giao intent tự động từ Preview Lane sang Ingest Lifecycle khi có chỉ thị rõ. | **Medium** |
| **NotebookLM Recon** | Yes | `T002_notebooklm_recon_storage` | - Đồng bộ thất bại liên phiên (lỗi API) và cơ chế rollback recon file.<br>- Tách biệt ghi dữ liệu non-canonical ở workspace `source-lab`. | **High** |
| **Workspace child routing** | Yes | `T003_workspace_child_vs_vault_root` | - Cô lập dữ liệu: Kiểm thử Agent chạy ngầm trong workspace con có bị rò rỉ token hoặc rò rỉ đường dẫn sang vault chính không. | **High** |
| **Pedagogy / Sư phạm** | No | None | - Kích hoạt pedagogy tạo slide PPTX từ Atom và kiểm tra xem có bị gọi nhầm deliverable phẳng không. | **High** |
| **Context Budget & Token** | No | None | - Kiểm thử vượt ngưỡng token: Tự động kích hoạt `cm-context-budget` khi context đạt 80% để giải phóng dữ liệu. | **High** |
| **Wiki absorb & Council** | No | None | - Phân xử mâu thuẫn tri thức: Kích hoạt `wiki-council` bằng fake mâu thuẫn tri thức và xem weighted consensus phân xử thế nào. | **Medium** |

---

## Chi tiết các Test Case Cần Bổ Sung (Gaps Analysis)

### 1. Test cho miền Sư phạm (`pedagogy` và `wiki-learning-pack`)
- **Tình trạng:** Hiện tại miền Spaced Repetition/học nhanh đã có test `T001` và `T002` trong `.agent/tests/skill-triggering/`. Tuy nhiên, miền sư phạm tạo slide/giáo án chuyên nghiệp (`pedagogy`) hoàn toàn chưa có test case nào.
- **Rủi ro:** Agent khi nhận yêu cầu *"hãy thiết kế giáo án sư phạm cho Atom này"* dễ bị nhầm lẫn và gọi `wiki-to-deliverable` sinh ra một file Markdown tổng hợp phẳng thay vì một lộ trình giáo án phân rã khoa học.
- **Đề xuất test:** Tạo `T006_pedagogy_creates_lesson_plan.md` kiểm tra Agent kích hoạt đúng pedagogy skill và Trainer Profile khi có yêu cầu giáo án/slide.

### 2. Test cho Quản lý Ngân sách Token (`cm-context-budget`)
- **Tình trạng:** Chưa có test case xác thực khả năng tự phòng vệ của Agent khi gặp hiện tượng phình ngữ cảnh (Context Bloat).
- **Rủi ro:** Khi người dùng yêu cầu đọc hàng loạt file tri thức thô trong `00_Inbox/`, Agent cố gắng đọc hết, làm tràn Context Window dẫn tới crash phiên hoặc mất trí nhớ cục bộ.
- **Đề xuất test:** Tạo `T007_context_budget_enforcement.md` giả lập context bùng nổ và kiểm chứng Agent tự động kích hoạt `cm-context-budget` để cắt giảm hoặc chia nhỏ file đọc.
