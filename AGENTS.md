# 🚀 AGENTS.md — NoteBookLLM_Br (Swarm 4.0 Supreme)

> **Cảnh báo cho AI Agent**: Đọc tệp này VÀ **[[CLAUDE.md]]** TRƯỚC KHI thực hiện bất kỳ tác vụ nào. Sử dụng ký hiệu `@` để triệu hồi cá tính phù hợp.

## 🏁 GLOBAL STARTUP PROTOCOL (Bắt buộc)
1. **READ FIRST**: Luôn đọc `AGENTS.md` và `CLAUDE.md` ngay khi bắt đầu phiên làm việc hoặc trước khi thực hiện tác vụ quan trọng.
2. **CHECKPOINT**: Luôn khai báo block `CHECKPOINT` (mục ✋ bên dưới) trước khi thực hiện task.
3. **LOG**: Luôn ghi nhật ký vào `3-resources/log.md` sau khi hoàn thành.

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
| **AG-SWARM-007** | **@designer** | **Instructional Designer** | Thiết kế learning sequence, scaffolding, lesson plan theo 5E/UDL/Backward Design. | 25k / 6k | < 50s |
| **AG-SWARM-008** | **@evaluator** | **Learning Evaluator** | Phân tích kết quả đào tạo theo Kirkpatrick, xác định knowledge gap, đề xuất remediation path. | 15k / 3k | < 45s |
| **AG-SWARM-009** | **@profiler** | **Learner Profiler** | Xây dựng và cập nhật Trainer Profile (entry/intermediate/advanced), feed context cho @designer và @engineer. | 20k / 4k | < 40s |
| **AG-SWARM-010** | **@creative** | **Creative Specialist** | Tạo case study, roleplay scenario, lesson plan mẫu cho giáo viên (Creative content). | 25k / 5k | < 60s |
| **AG-SWARM-011** | **@healer** | **Maintenance** | Hàn gắn tri thức, sửa lỗi liên kết và phục hồi tính toàn vẹn hệ thống. | 10k / 2k | < 20s |
## 🗂️ Cấu trúc Resources (Resources Architecture v4.1)
 
```
3-resources/
├── raw/          ← Dữ liệu thô gốc. KHÔNG ai được sửa, chỉ được đọc.
├── wiki/         ← Wiki Pages có [[wikilinks]]. 1 file = 1 khái niệm.
│                    Guide: 3-resources/WIKI_AGENT_GUIDE.md
└── distilled/    ← Output cuối: Test bank (ELN_Test_*.md) và KB đã verify.
                     CHỈ @librarian và @auditor được ghi vào đây sau khi verify.
```
**Quy tắc vàng:**
- `raw/` → không ai sửa (Immutable Source)
- `wiki/` → Atomic Records (Lịch sử trích xuất, hỗ trợ Rule 14)
- `distilled/` → **The Wiki** (Nơi bồi đắp tri thức nén, đa chiều)
- `process/` → [DEPRECATED] Chuyển sang `1-projects/` hoặc `2-areas/`.
- `archive/` → Snapshot Storage (Lưu trữ vĩnh viễn, Wikilinks đã trung hòa)

## 🛠️ Lệnh điều khiển (Manus Commands)
- `/scout` — Kích hoạt `@scout` nghiên cứu & Đánh giá độ khó (Difficulty Audit).
- `/file-back` — Tự động lưu kết quả phân tích có giá trị thành Wiki page mới (Query Compounding).
- `/ingest` — Kích hoạt quy trình chuẩn nạp nguồn dữ liệu mới vào Wiki (5 bước cố định).
- `/lint` — Kiểm tra sức khỏe Wiki: orphan pages, mâu thuẫn, stale claims, concept gaps.
- `/assess-difficulty` — Lệnh chuyên biệt để đánh giá tải nhận thức của tri thức.
- `/heal` — Kích hoạt `@healer` sửa lỗi dựa trên log hoặc báo cáo lỗi.
- `/heartbeat` — Kích hoạt `@librarian` tổng hợp `3-resources/raw/` và cập nhật đồ thị kiến thức.
- `/graphify` — Cập nhật hoặc truy vấn đồ thị kiến thức dự án (Structural Memory).
- `/lint` — Kích hoạt `@librarian` chạy `scripts/brain_lint.py` để kiểm tra sức khỏe tri thức.
- `/audit-tokens` — Kiểm tra ngân sách token của từng phiên làm việc (Warning mode).
- `/scout-exam [module] [bloom_levels]` — Kích hoạt `@scout` nghiên cứu chuyên biệt cho ra đề kiểm tra. Output bắt buộc ghi vào `1-projects/[Project_Name]/EXAM_Context_[module].md` trước khi `@engineer` tiếp nhận.
- `/audit-exam [file_đề]` — Kích hoạt `@auditor` đối soát ngược từng câu hỏi. Thứ tự ưu tiên: (1) `1-projects/[Project_Name]/EXAM_Context_*.md` → (2) `3-resources/distilled/` các file khác → (3) `3-resources/raw/` chỉ khi distilled không đủ. KHÔNG dùng general knowledge. Nếu không tìm thấy nguồn ở cả 3 tầng → ghi rõ `[KHÔNG TÌM THẤY NGUỒN]`, tuyệt đối không reconstruct.
- `/profile [trainer_id] [level]` — Kích hoạt `@profiler` tạo hoặc cập nhật Trainer Profile. Output ghi vào `2-areas/Profiles/Trainer_Profile_[id].md`. Level: `entry` / `intermediate` / `advanced`.
- `/design [module] [trainer_level]` — Kích hoạt `@designer` thiết kế learning sequence cho module và level trainer cụ thể. Output ghi vào `1-projects/[Project_Name]/Learning_Design_[module].md`. Bắt buộc đọc Trainer Profile tương ứng trước.
- `/evaluate [module] [kết_quả_file]` — Kích hoạt `@evaluator` phân tích kết quả đào tạo theo Kirkpatrick Level 1-4. Output ghi vào `2-areas/Assessment/Eval_Report_[module].md` và `3-resources/log.md`.
- `/ingest-inbox` — @librarian đọc toàn bộ `00_Inbox/`, phân loại từng file, propose action trước khi execute.

## 📂 Phân quyền truy cập (Manus Scoped Access)

| Agent | Đọc | Ghi | Cấm tuyệt đối |
|:---|:---|:---|:---|
| **@pm** | Tất cả | `3-resources/log.md`, `CONTINUITY.md`, `1-projects/` (task plans) | Ghi `3-resources/raw/` |
| **@scout** | `3-resources/raw/`, `1-projects/` | `3-resources/wiki/` (draft), `1-projects/[Project]/EXAM_Context_*.md` | Ghi `3-resources/distilled/` trực tiếp |
| **@engineer** | `1-projects/`, `3-resources/distilled/` | `1-projects/[Project]/` (output task) | Ghi `3-resources/wiki/`, `3-resources/raw/` |
| **@librarian** | Tất cả | `3-resources/distilled/` (sau verify), `3-resources/log.md` | Overwrite `3-resources/log.md` |
| **@auditor** | Tất cả (read-only) | `3-resources/log.md` (append only) | Ghi bất kỳ file nội dung nào |
| **@designer** | `3-resources/raw/`, `3-resources/distilled/`, `2-areas/Profiles/Trainer_Profile_*.md` | `1-projects/[Project]/Learning_Design_*.md` | Bỏ qua Trainer_Profile |
| **@evaluator** | `1-projects/`, `3-resources/distilled/` | `2-areas/Assessment/Eval_Report_*.md`, `3-resources/log.md` | — |
| **@profiler** | `3-resources/raw/`, `3-resources/distilled/` | `2-areas/Profiles/Trainer_Profile_*.md` | — |
| **@creative** | `3-resources/distilled/`, `3-resources/wiki/` | `docs/`, `res/`, `templates/` | Ghi `3-resources/` trực tiếp |
| **@healer** | Tất cả | `3-resources/wiki/` (sửa links), `scripts/` | Xóa file không có backup |
| **@devops** | Tất cả | `scripts/`, `tools/`, `libs/` | Ghi `3-resources/distilled/` |
 
**Quy tắc ghi log bắt buộc:**
Mọi hành động ghi file → append vào `3-resources/log.md` theo format:
```
## [YYYY-MM-DD HH:MM] <type> | <agent> | <mô tả ngắn>
- File tạo/sửa: [đường dẫn]
- Lý do: [1 câu]
```
 

## ⚖️ Quy tắc Swarm v4.0 Supreme (Manus Standard)
1. **Manus First**: Ưu tiên đọc `task_plan.md` trước khi thực hiện bất kỳ hành động nào.
2. **Double Link**: Mọi note mới trong Wiki phải có ít nhất 2 liên kết `[[Wikilinks]]`.
3. **Knowledge Compounding (Rule 3)**: Mọi giải pháp, Insight hoặc tri thức mới từ Raw phải được bồi đắp (Compounded) trực tiếp vào các file Master trong `3-resources/distilled/` ngay trong phiên làm việc. Không đợi đến cuối Pipeline.
4. **Log-First Ingest (Rule 4)**: Mọi thay đổi về tri thức hệ thống (Brain/Wiki) phải được ghi nhận vào `3-resources/log.md`, phải dùng append không được overwrite, phải viết đúng định dạng được ghi trong log. **BẮT BUỘC sử dụng bảng mã UTF-8 (không BOM) khi ghi file.** Khi dùng PowerShell, luôn thêm `-Encoding UTF8`.
5. **Automated Self-Healing (Rule 5)**: Agent phải **tự động** triệu hồi `@healer` khi gặp lỗi hệ thống hoặc logic lặp lại.
6. **Budget Awareness (Rule 6)**: Thông báo cho người dùng khi phiên làm việc tiêu tốn >80% Budget đã định nghĩa.
7. **Hierarchy Limit (Rule 7 - Absolute Flatness)**: 
    - Cấp 1 (Root Buckets): `00_Inbox/`, `1-projects/`, `2-areas/`, `3-resources/`, `4-archive/`, `scripts/`, `tools/`.
    - `00_Inbox/`: Files flat, không subfolder, prefix YYYYMMDD_, xử lý hàng tuần.
    - Cấp 2 (Buckets): 
      - `1-projects/`: Mỗi dự án là 1 folder (vd: `2026_TOT_STEAM/`, `2026_K10_Prompt/`)
      - `2-areas/`: `Curriculum/`, `Assessment/`, `Profiles/`
      - `3-resources/`: `raw/`, `wiki/`, `distilled/`
      - `scripts/`: `maintenance/`, `pipelines/`, `tests/`
    - Cấp 3 (Files): Phải là tệp tin trực tiếp. **KHÔNG CÓ THƯ MỤC CON Ở CẤP 3**.
    - **Quy tắc Lưu trữ (Archiving)**: Khi hoàn thành task, các file từ `1-projects/` hoặc tài liệu cũ phải được chuyển vào `4-archive/` với prefix `YYYYMMDD_` (KHÔNG có subfolder ở cấp 2 của archive).
    - **Quy tắc Trung hòa (Neutralization)**: Khi di chuyển file vào `4-archive/`, PHẢI chuyển đổi Wikilinks `[[...]]` thành văn bản thuần (ví dụ: bọc trong backticks `` `...` ``) để không làm loãng đồ thị tri thức.
    - **Quy tắc Prefix 2 cấp**: Bắt buộc đặt tên file theo cấu trúc `[CẤP_1]_[CẤP_2]_[TÊN_FILE].md` để duy trì tính phẳng nhưng vẫn phân loại được.
        - **KHMT**: AI_THCS, AI_Tieu_hoc, Python, Scratch, Scratch_Jr, Tynker.
        - **Robot**: Codey, GBot, mBot, Rover, Unplugged, xBot.
        - **DESIGN**: 3D_Tinkercad, Canva, Maker_Empire, Wordpress.
        - **IOT**: AI_Arduino, Arduino, Halocode, YoloBit.
        - **PROMPT**: K10_Toan, K10_Van, K10_Anh (Dành cho Prompt Engineering).
        - **ACAD**: Biology, Math, Physics (Dành cho Giáo án/Academic).
8. **Machine-Readability**: Đặt tên File/Folder theo chuẩn `Snake_Case`, prefix bằng số (`01_`, `02_`) và sử dụng YAML Frontmatter cho ngữ cảnh.
9. **Exam Handoff Protocol**: Khi tạo đề kiểm tra, `@scout` PHẢI hoàn thành và ghi `1-projects/[Project]/EXAM_Context_[module].md` chứa:
    - Danh sách concept chính xác cần kiểm tra (trích từ tài liệu gốc).
    - Terminology chuẩn (không paraphrase).
    - Phạm vi KHÔNG kiểm tra (negative scope).
    `@engineer` chỉ được bắt đầu viết sau khi file này tồn tại.
10. **Anti-Hallucination Reverse Tracing (Rule 10 - Absolute)**:
    Khi thực hiện bất kỳ tác vụ truy xuất ngược nào (reverse knowledge extraction), agent BẮT BUỘC phải:

    a. Tuân thủ nghiêm ngặt [AUDITOR_Protocol.md](file:///d:/NoteBookLLM_Br/AUDITOR_Protocol.md) đặt tại Root level để tất cả agent (bao gồm `@engineer`) đều có thể tham chiếu.

    b. Chỉ trích dẫn từ file có trong `3-resources/raw/` hoặc `3-resources/distilled/` — KHÔNG dùng general knowledge.

    c. Với mỗi claim, ghi rõ: `📖 Nguồn: [tên file] — [dòng/section cụ thể]`

    d. Nếu không tìm thấy nguồn trong hệ thống: → Ghi `[KHÔNG TÌM THẤY NGUỒN]` → Báo cáo cho `@auditor` → KHÔNG tự điền nội dung thay thế.

    e. **@auditor** là agent duy nhất được phép thực hiện reverse tracing. `@scout`, `@engineer`, `@librarian` bị cấm tự ý thực hiện tác vụ này.
11. **Pedagogical Pipeline (Rule 11 - Absolute Sequence + Guard)**:
    
    TRƯỚC KHI chạy mỗi bước, agent PHẢI verify file prerequisite:
    
    | Bước | Agent | Prerequisite file phải tồn tại |
    |---|---|---|
    | 1 | @profiler | Không cần |
    | 2 | @designer | 2-areas/Profiles/Trainer_Profile_[id].md |
    | 3 | @engineer | 1-projects/[Project]/Learning_Design_[module].md |
    | 4 | @evaluator | 2-areas/Assessment/Eval_Report_[module].md |
    
    Nếu file prerequisite KHÔNG tồn tại → agent DỪNG ngay,
    báo @pm, KHÔNG tự tiếp tục.
## 🔒 WRITE-PROTECT Rule (Bổ sung vào Rules)
Rule 12 — RAW IS IMMUTABLE:
- 3-resources/raw/ là READ-ONLY với TẤT CẢ agents
- Không agent nào được ghi, sửa, hoặc overwrite file trong 3-resources/raw/
- Vi phạm Rule này → @healer rollback ngay, ghi incident vào 3-resources/log.md
- CHỈ người dùng mới được thêm file mới vào 3-resources/raw/

## 📚 WIKI CATALOGING (Quy tắc Mục lục Kiến thức)
Rule 13 — WIKI_INDEX & AGENT_GUIDE IS MANDATORY:
- Mọi tệp tin kiến thức (Atoms, Distilled) khi được tạo ra hoặc chỉnh sửa đều PHẢI được cập nhật vào `3-resources/WIKI_INDEX.md`.
- **BẮT BUỘC**: Trước khi tạo/sửa Wiki, Agent phải đọc hướng dẫn tại `3-resources/WIKI_AGENT_GUIDE.md`.
- Agent có thể dùng script `scripts/update_wiki_index.py` để tự động hóa việc này.
- `3-resources/WIKI_INDEX.md` đóng vai trò là "Bản đồ" (Catalog) để LLM quét nhanh thay vì lục lọi toàn bộ files.

Rule 15 — EXECUTION INTEGRITY (Chống "Nói mà không làm"):
- Tuyệt đối KHÔNG báo cáo "Đã tạo/sửa file" nếu chưa thực hiện cuộc gọi tool (write_file, replace_file, v.v.) thành công trong cùng lượt phản hồi.
- Mọi báo cáo hoàn thành phải dựa trên Output thực tế của Tool, không dựa trên dự định của Agent.
- Vi phạm: Phải tự phê bình và ghi lỗi vào `CONTINUITY.md`.
## 🔐 SOURCE INTEGRITY (Bắt buộc khi tạo ATOMS)
Rule 14 — SOURCE_INTEGRITY:
- Khi viết trường `📖 Nguồn`, agent phải **thực sự mở file đó** trong `3-resources/raw/` trước khi viết.
- Chỉ ghi **tên file raw gốc hiện tồn tại** trong `3-resources/raw/` — không ghi file tổng hợp trung gian đã deprecated.
- Phải xác nhận fact xuất hiện ở section / câu hỏi nào cụ thể — ghi rõ vào comment `[AUDITOR] Rule 14`.
- Checklist ATOMS bắt buộc có mục: `- [ ] [Rule 14] Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại`.
- Vi phạm: ATOMS không được phép đổi status thành `verified` nếu thiếu mục này.

Rule 16 — EXTRACTION_MANDATORY_STATS:
- Mọi tệp tin trung gian trong `1-projects/[Project]/` PHẢI sử dụng cấu trúc từ `3-resources/PROCESS_TEMPLATE.md`.
- Bắt buộc phải có **Bảng thống kê hiệu suất Khai thác (Mining Stats)** ở đầu tệp tin để theo dõi độ phủ tri thức.
- **BẮT BUỘC**: Phải liệt kê danh sách các Master Files (`3-resources/distilled/`) đã được bồi đắp tri thức từ nguồn này.
- Bất kỳ Agent nào khi thực hiện trích xuất tri thức (Extraction/Mining) đều phải cập nhật bảng này trước khi nạp vào Wiki.

## ✋ CHECKPOINT Protocol (Bắt buộc mọi agent)

Trước khi thực hiện BẤT KỲ task nào, agent PHẢI trả lời chính xác các block sau:
```yaml
CHECKPOINT:
  agent: "@[tên agent]"
  task: "[tên task cụ thể — không được viết chung chung]"
  step: "[bước X / tổng Y bước trong pipeline]"
  output_file: "[đường dẫn file sẽ tạo — VD: 3-resources/distilled/EXAM_Context_M2.md]"
  stop_condition: "[điều kiện dừng cụ thể — VD: sau khi tạo xong 5 Wiki Pages]"
  prerequisites:
    - file: "[tên file prerequisite 1]"
      exists: "YES | NO"
    - file: "[tên file prerequisite 2]"
      exists: "YES | NO"
  status: "READY | BLOCKED"
  blocked_reason: "[để trống nếu READY — ghi lý do nếu BLOCKED]"
```
---
**Build**: Antigravity v4.0 | **Taxonomy**: AG-CORE-Series | **Status**: Operational | **Pattern**: LLM Wiki Supreme
