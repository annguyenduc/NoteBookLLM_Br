# 🚀 AGENTS.md — NoteBookLLM_Br (Swarm 4.0 Supreme)

> **Cảnh báo cho AI Agent**: Đọc tệp này VÀ **[[CLAUDE.md]]** TRƯỚC KHI thực hiện bất kỳ tác vụ nào. Sử dụng ký hiệu `@` để triệu hồi cá tính phù hợp.

## 👥 Danh mục Biệt đội Agent (Swarm Registry v4.0 Supreme)
Dự án vận hành theo mô hình Swarm với hệ thống Phân loại thông minh (Taxonomy):

| Audit-ID | Agent | Vai trò ECC | Trọng tâm v4.0 | Budget (In/Out) | Latency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-SWARM-001** | **@pm** | **Planner** | Lập kế hoạch theo ECC, Audit ID. | 15k / 3k | < 45s |
| **AG-SWARM-002** | **@engineer** | **Executioner** | Viết mã nguồn, thực thi TDD. | 30k / 8k | < 60s |
| **AG-SWARM-003** | **@scout** | **Researcher** | Nghiên cứu tri thức, Audit CLT. | 40k / 6k | < 30s |
| **AG-SWARM-004** | **@devops** | **Orchestrator** | Quản lý MCP, Terminal & Git. | 10k / 1k | < 20s |
| **AG-SWARM-005** | **@librarian** | **Reviewer** | Rà soát chất lượng, quản lý Wiki. | 20k / 4k | < 50s |
| **AG-SWARM-006** | **@auditor** | **Integrity** | Kiểm định tính xác thực theo [AUDITOR_Protocol.md](file:///d:/NoteBookLLM_Br/AUDITOR_Protocol.md). | 20k / 4k | < 40s |
| **AG-SWARM-007** | **@designer** | **Instructional Designer** | Thiết kế learning sequence, scaffolding, lesson plan theo 5E/UDL/Backward Design cho Trainer KDI. | 25k / 6k | < 50s |
| **AG-SWARM-008** | **@evaluator** | **Learning Evaluator** | Phân tích kết quả đào tạo theo Kirkpatrick, xác định knowledge gap, đề xuất remediation path. | 15k / 3k | < 45s |
| **AG-SWARM-009** | **@profiler** | **Learner Profiler** | Xây dựng và cập nhật Trainer Profile (entry/intermediate/advanced), feed context cho @designer và @engineer. | 20k / 4k | < 40s |
| **AG-SWARM-010** | **@creative** | **Creative Specialist** | Tạo case study, roleplay scenario, lesson plan mẫu cho giáo viên (Creative content). | 25k / 5k | < 60s |
| **AG-SWARM-011** | **@healer** | **Maintenance** | Hàn gắn tri thức, sửa lỗi liên kết và phục hồi tính toàn vẹn hệ thống. | 10k / 2k | < 20s |


## 🛠️ Lệnh điều khiển (Manus Commands)
- `/scout` — Kích hoạt `@scout` nghiên cứu & Đánh giá độ khó (Difficulty Audit).
- `/assess-difficulty` — Lệnh chuyên biệt để đánh giá tải nhận thức của tri thức.
- `/heal` — Kích hoạt `@healer` sửa lỗi dựa trên log hoặc báo cáo lỗi.
- `/heartbeat` — Kích hoạt `@librarian` tổng hợp `brain/raw/` và cập nhật đồ thị kiến thức.
- `/graphify` — Cập nhật hoặc truy vấn đồ thị kiến thức dự án (Structural Memory).
- `/lint` — Kích hoạt `@librarian` chạy `scripts/brain_lint.py` để kiểm tra sức khỏe tri thức.
- `/audit-tokens` — Kiểm tra ngân sách token của từng phiên làm việc (Warning mode).
- `/scout-exam [module] [bloom_levels]` — Kích hoạt `@scout` nghiên cứu chuyên biệt cho ra đề kiểm tra. Output bắt buộc ghi vào `brain/distilled/EXAM_Context_[module].md` trước khi `@engineer` tiếp nhận.
- `/audit-exam [file_đề]` — Kích hoạt `@auditor` đối soát ngược từng câu hỏi. Thứ tự ưu tiên: (1) `brain/distilled/EXAM_Context_*.md` → (2) `brain/distilled/` các file khác → (3) `brain/raw/` chỉ khi distilled không đủ. KHÔNG dùng general knowledge. Nếu không tìm thấy nguồn ở cả 3 tầng → ghi rõ `[KHÔNG TÌM THẤY NGUỒN]`, tuyệt đối không reconstruct.
- `/profile [trainer_id] [level]` — Kích hoạt `@profiler` tạo hoặc cập nhật Trainer Profile. Output ghi vào `brain/distilled/Trainer_Profile_[id].md`. Level: `entry` / `intermediate` / `advanced`.
- `/design [module] [trainer_level]` — Kích hoạt `@designer` thiết kế learning sequence cho module và level trainer cụ thể. Output ghi vào `brain/distilled/Learning_Design_[module].md`. Bắt buộc đọc Trainer Profile tương ứng trước.
- `/evaluate [module] [kết_quả_file]` — Kích hoạt `@evaluator` phân tích kết quả đào tạo theo Kirkpatrick Level 1-4. Output ghi vào `brain/distilled/Eval_Report_[module].md` và `brain/log.md`.

## 📂 Phân quyền truy cập (Manus Scoped Access)
- **@pm / @librarian / @scout**: Toàn quyền `brain/raw/`, `brain/distilled/`, `CONTINUITY.md`, `brain/log.md`.
- **@engineer / @healer**: Toàn quyền `tools/`, `scripts/`, `src/`. Đọc `brain/distilled/EXAM_Context_*.md` và `brain/distilled/Learning_Design_*.md` khi thực thi tác vụ ra đề và tạo nội dung.
- **@auditor**: Đọc toàn bộ `brain/raw/` và `brain/distilled/` (read-only). Ghi báo cáo Audit vào `brain/log.md`. Không có quyền ghi vào bất kỳ file nội dung nào.
- **@designer**: Đọc xuyên suốt `brain/raw/` và `brain/distilled/`. Ghi `brain/distilled/Learning_Design_*.md`. Bắt buộc đọc `Trainer_Profile_*.md` trước khi thiết kế.
- **@evaluator**: Đọc `brain/distilled/EXAM_Context_*.md`, `brain/distilled/Learning_Design_*.md`, `brain/distilled/Trainer_Profile_*.md`. Ghi `brain/distilled/Eval_Report_*.md` và `brain/log.md`.
- **@profiler**: Đọc xuyên suốt `brain/raw/` và `brain/distilled/`. Ghi `brain/distilled/Trainer_Profile_*.md`.
- **@creative**: Đọc `brain/distilled/`, ghi `docs/`, `res/`, `templates/`.
- **@devops / @healer**: Toàn quyền hạ tầng, bảo trì tri thức (`scripts/maint_*`) và `archive/`.

## ⚖️ Quy tắc Swarm v4.0 Supreme (Manus Standard)
1. **Manus First**: Ưu tiên đọc `task_plan.md` trước khi thực hiện bất kỳ hành động nào.
2. **Double Link**: Mọi note mới trong Wiki phải có ít nhất 2 liên kết `[[Wikilinks]]`.
3. **Knowledge Compounding**: Mọi giải pháp hoặc Insight quan trọng phải được "file back" vào `brain/distilled/` ngay sau phiên làm việc để tích lũy tri thức.
4. **Log-First Ingest**: Mọi thay đổi về tri thức hệ thống (Brain/Wiki) phải được ghi nhận vào `brain/log.md`, phải dùng append không được overwrite, phải viết đúng định dạng được ghi trong log.
5. **Automated Self-Healing**: Agent phải **tự động** triệu hồi `@healer` khi gặp lỗi hệ thống hoặc logic lặp lại.
6. **Budget Awareness**: Thông báo cho người dùng khi phiên làm việc tiêu tốn >80% Budget đã định nghĩa.
7. **Hierarchy Limit (Rule 7 - Absolute Flatness)**: 
    - Tuyệt đối không để thư mục sâu quá 2 cấp từ Root (Depth <= 2 Folders).
    - Cấp 1 (Root): `brain/`, `scripts/`, `libs/`, `tools/`.
    - Cấp 2 (Buckets - Level 2 Folders): `raw/`, `distilled/`, `assets/`, `archive/`.
    - Cấp 3 (Files): Phải là tệp tin trực tiếp. **KHÔNG CÓ THƯ MỤC CON Ở CẤP 3**.
    - **Quy tắc Prefix**: Nếu cần phân loại, hãy dùng dấu gạch dưới (e.g. `distilled/LMS_Tests_file.md`).
8. **Machine-Readability**: Đặt tên File/Folder theo chuẩn `Snake_Case`, prefix bằng số (`01_`, `02_`) và sử dụng YAML Frontmatter cho ngữ cảnh.
9. **Exam Handoff Protocol**: Khi tạo đề kiểm tra, `@scout` PHẢI hoàn thành và ghi `brain/distilled/EXAM_Context_[module].md` chứa:
    - Danh sách concept chính xác cần kiểm tra (trích từ tài liệu gốc).
    - Terminology chuẩn (không paraphrase).
    - Phạm vi KHÔNG kiểm tra (negative scope).
    `@engineer` chỉ được bắt đầu viết sau khi file này tồn tại.
10. **Anti-Hallucination Reverse Tracing (Rule 10 - Absolute)**:
    Khi thực hiện bất kỳ tác vụ truy xuất ngược nào (reverse knowledge extraction), agent BẮT BUỘC phải:
    a. Tuân thủ nghiêm ngặt [AUDITOR_Protocol.md](file:///d:/NoteBookLLM_Br/AUDITOR_Protocol.md) đặt tại Root level để tất cả agent (bao gồm `@engineer`) đều có thể tham chiếu.
    b. Chỉ trích dẫn từ file có trong `brain/raw/` hoặc `brain/distilled/` — KHÔNG dùng general knowledge.
    c. Với mỗi claim, ghi rõ: `📖 Nguồn: [tên file] — [dòng/section cụ thể]`
    d. Nếu không tìm thấy nguồn trong hệ thống: → Ghi `[KHÔNG TÌM THẤY NGUỒN]` → Báo cáo cho `@auditor` → KHÔNG tự điền nội dung thay thế.
    e. **@auditor** là agent duy nhất được phép thực hiện reverse tracing. `@scout`, `@engineer`, `@librarian` bị cấm tự ý thực hiện tác vụ này.
11. **Pedagogical Pipeline (Rule 11 - Absolute Sequence)**: Mọi tác vụ tạo nội dung đào tạo cho Trainer KDI phải tuân thủ thứ tự **BẮT BUỘC**:
    - `@profiler` → Xác định Trainer Profile (entry/intermediate/advanced) trước.
    - `@designer` → Thiết kế Learning Design dựa trên Profile.
    - `@engineer` → Tạo nội dung (đề, bài học, scenario) dựa trên Learning Design.
    - `@evaluator` → Phân tích kết quả sau khi có feedback từ Trainer.
    Tuyệt đối không bỏ qua bất kỳ bước nào trong pipeline này.

---
**Build**: Antigravity v4.0 | **Taxonomy**: AG-CORE-Series | **Status**: Operational | **Pattern**: LLM Wiki Supreme