# Executive Summary: Tóm Tắt Tinh Gọn Cho AN

Báo cáo này tóm tắt kết quả kiểm định chuyên sâu danh mục kỹ năng (Skill Portfolio Rationalization Audit) của vault `NoteBookLLM_Br`, sử dụng Superpowers làm metodologia grader để chấm thiết kế và ranh giới hoạt động của kỹ năng.

- **Số lượng kỹ năng thực tế kiểm đếm tại thời điểm audit:** **44 kỹ năng** (hoạt động) và **1 thư mục tham chiếu** (`references`).

---

## 5 Kỹ năng nên giữ làm CORE (Core Skills)
Đây là các kỹ năng xương sống có thiết kế mục tiêu, ranh giới và output hoàn hảo nhất, cần duy trì để đảm bảo kỷ luật:
1. **`cm-planning` (Phase 0):** Quản lý spec nháp, làm rõ ý định và phân tích rủi ro RCA.
2. **`writing-plans` (Phase 1):** Lập kế hoạch chi tiết `implementation_plan.md` cho các task phát triển.
3. **`verification-before-completion`:** Chốt chặn kiểm thử thực tế (evidence before assertion) trước khi hoàn tất.
4. **`cm-context-budget`:** Kỹ năng sinh tồn kiểm soát và tiết kiệm Token Window.
5. **`karpathy-core`:** Nguyên tắc vàng về Surgical Change (chỉ sửa những gì bắt buộc).

---

## 5 Kỹ năng nên Rút gọn / Gom lại (Consolidation Candidates)
Các kỹ năng có sự chồng chéo cao về mặt chức năng và trigger cần được tinh giản để giải phóng context:
1. **`brainstorming`:** Gom hoàn toàn vào Phase 0 của `cm-planning`.
2. **`cm-tdd`:** Gom vào vòng lặp self-healing đệ quy của `verification-before-completion`.
3. **`systematic-debugging`:** Gom vào logic RCA của `cm-debugging`.
4. **`wiki-rebuild` & `wiki-cleanup`:** Chuyển đổi thành workflow/script vận hành tĩnh (gọi qua slash command hoặc shell lệnh).
5. **`cm-continuity` & `cm-quality-gate`:** Chuyển đổi thành Quy tắc (Rules) tĩnh bắt buộc thực thi ngầm ở Session End thay vì skill active.

---

## 5 Trigger dễ gây nhầm lẫn nhất (Trigger Conflicts)
Các mẫu prompt dễ làm Agent định tuyến sai kỹ năng và giải pháp khắc phục:
1. **"Tóm tắt PDF này để tôi học nhanh"** (Nhầm giữa Preview và Canonical Ingest) $\rightarrow$ *Khắc phục:* Định tuyến cứng qua workspace `learning` và workflow `learning-first`.
2. **"Sửa script convert PDF để chạy ổn định hơn"** (Nhầm giữa Code ngay và Lập Kế Hoạch) $\rightarrow$ *Khắc phục:* Cưỡng chế chạy `cm-planning` (Phase 0) trước.
3. **"Tôi muốn đưa tài liệu này vào vault chính"** (Nhầm bypass chốt chặn chuẩn hóa) $\rightarrow$ *Khắc phục:* Kích hoạt trực tiếp `ingest-lifecycle` và yêu cầu AN GO.
4. **"Tìm định nghĩa của thuật ngữ X"** (Nhầm giữa Keyword và Semantic Search) $\rightarrow$ *Khắc phục:* Chạy `wiki-query` trước, nếu rỗng mới kích hoạt `wiki-semantic-search`.
5. **"Tạo sơ đồ giáo án hoặc slide cho bài học X"** (Nhầm giữa pedagogy và deliverable phẳng) $\rightarrow$ *Khắc phục:* Giới hạn boundary bằng slide framework chỉ load khi gọi pedagogy.

---

## 5 Bài Test nên thêm vào `.agent/tests/` (Missing Tests)
Các test case hồi quy cần bổ sung gấp để tăng độ tin cậy vận hành:
1. **`T006_pedagogy_creates_lesson_plan`:** Đảm bảo gọi đúng pedagogy khi có yêu cầu giáo án thay vì deliverable phẳng.
2. **`T007_context_budget_enforcement`:** Kiểm chứng khả năng tự phòng vệ của Agent khi dung lượng context đạt 80%.
3. **`T008_system_rules_modification_block`:** Đảm bảo Agent từ chối tự ý sửa đổi `AGENTS.md` khi chưa được phê duyệt.
4. **`T009_notebooklm_recon_api_failure`:** Kiểm định cơ chế tự phục hồi và rollback file recon khi kết nối NotebookLM API thất bại.
5. **`T010_workspace_cross_pollution_prevention`:** Đảm bảo Agent chạy trong workspace con không bị rò rỉ token hoặc ghi nhầm sang vault chính.

---

## 3 Việc nên làm tiếp theo (Next Actions)
1. **Thực thi Phase 1 của Consolidation Plan:** Di chuyển thư mục tham chiếu `references` ra khỏi `skills/` sang `docs/` và chuyển đổi các skill maintenance tĩnh (`wiki-rebuild`, `wiki-cleanup`) thành kịch bản workflow.
2. **Xây dựng bổ sung 5 Test Cases khuyến nghị:** Tạo các file test skeleton tương tự nhóm T001-T005 tại `.agent/tests/` để chuẩn hóa các chốt chặn tự động cho Agent.
3. **Tích hợp Dynamic Skill Loading:** Cập nhật logic bootstrap trong `using-superpowers` để nạp skill theo phân tầng ngữ cảnh (Tiers), giải phóng vĩnh viễn không gian token cho vault.
