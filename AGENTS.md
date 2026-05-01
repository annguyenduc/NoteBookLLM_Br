#  AGENTS.md — NoteBookLLM_Br (Swarm 4.0 Supreme)

> **Cảnh báo cho AI Agent**: Đọc tệp này VÀ **[[CLAUDE.md]]** TRƯỚC KHI thực hiện bất kỳ tác vụ nào. Sử dụng ký hiệu `@` để triệu hồi cá tính phù hợp.

## GLOBAL STARTUP PROTOCOL (Bắt buộc)
1. **READ FIRST**: Luôn đọc `AGENTS.md`, `CLAUDE.md` và `WORKSPACE_OVERVIEW.md` ngay khi bắt đầu phiên làm việc hoặc trước khi thực hiện tác vụ quan trọng.
2. **CHECKPOINT**: Luôn khai báo block `CHECKPOINT` (mục bên dưới) trước khi thực hiện task.
3. **LOG**: Luôn ghi nhật ký vào `3-resources/wiki/log.md` sau khi hoàn thành.
4. **GEMINI BRIDGE**: Global behavior rules nằm tại `~/.gemini/GEMINI.md` — các rule đó có hiệu lực song song với AGENTS.md. Nếu có conflict → **AGENTS.md được ưu tiên** (project-specific wins over global). Agent không cần tự đọc lại GEMINI.md trong mỗi phiên — Antigravity đã load nó tự động khi khởi động.
5. **PURPOSE SCOPE**: Workspace có 2 file purpose: `purpose.md` (root) định hướng toàn bộ workspace; `3-resources/purpose.md` định hướng riêng cho wiki/knowledge base. Khi thực hiện tác vụ wiki → đọc `3-resources/purpose.md`. Khi thực hiện tác vụ project → đọc `purpose.md` ở root.

---

## Danh mục Biệt đội Agent (Swarm Registry v4.0 Supreme)
Dự án vận hành theo mô hình Swarm với hệ thống Phân loại thông minh (Taxonomy):

| Audit-ID | Agent | Vai trò ECC | Trọng tâm v4.0 | Budget (In/Out) | Latency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AG-SWARM-001** | **@pm** | **Planner** | Lập kế hoạch theo ECC, Audit ID. | 15k / 3k | < 45s |
| **AG-SWARM-002** | **@engineer** | **Executioner** | Viết mã nguồn, thực thi TDD. | 30k / 8k | < 60s |
| **AG-SWARM-003** | **@scout** | **Researcher** | Nghiên cứu tri thức, Audit CLT. | 40k / 6k | < 30s |
| **AG-SWARM-004** | **@devops** | **Orchestrator** | Quản lý MCP, Terminal & Git. | 10k / 1k | < 20s |
| **AG-SWARM-005** | **@librarian** | **Reviewer** | Rà soát chất lượng, quản lý Wiki. | 20k / 4k | < 50s |
| **AG-SWARM-006** | **@auditor** | **Integrity** | Kiểm định tính xác thực theo AUDITOR_Protocol.md. | 20k / 4k | < 40s |
| **AG-SWARM-007** | **@designer** | **Instructional Designer** | Thiết kế learning sequence, scaffolding, lesson plan theo 5E/UDL/Backward Design. | 25k / 6k | < 50s |
| **AG-SWARM-008** | **@evaluator** | **Learning Evaluator** | Phân tích kết quả đào tạo theo Kirkpatrick, xác định knowledge gap, đề xuất remediation path. | 15k / 3k | < 45s |
| **AG-SWARM-009** | **@profiler** | **Learner Profiler** | Xây dựng và cập nhật Trainer Profile (entry/intermediate/advanced), feed context cho @designer và @engineer. | 20k / 4k | < 40s |
| **AG-SWARM-010** | **@creative** | **Creative Specialist** | Tạo case study, roleplay scenario, lesson plan mẫu cho giáo viên (Creative content). | 25k / 5k | < 60s |
| **AG-SWARM-011** | **@healer** | **Maintenance** | Hàn gắn tri thức, sửa lỗi liên kết và phục hồi tính toàn vẹn hệ thống. | 10k / 2k | < 20s |

---

## Cấu trúc Resources (Resources Architecture v4.1)

```
3-resources/
├── purpose.md              ← Định hướng wiki/knowledge base (đọc khi làm wiki task)
├── schema.md               ← Quy định cấu trúc Wiki
├── raw/
│   ├── sources/            ← Dữ liệu thô gốc dạng PDF/Docx. KHÔNG ai được sửa.
│   └── assets/             ← Local images.
└── wiki/                   ← Kho tri thức hệ thống.
    ├── index.md            ← Mục lục (Tự động tạo)
    ├── log.md              ← Nhật ký hệ thống
    ├── entities/           ← Thực thể (công cụ, hệ thống, ngôn ngữ)
    ├── concepts/           ← Khái niệm, kỹ thuật, phương pháp (THINK_*, STAT_*)
    ├── sources/            ← Tóm tắt nguồn sách đã Ingest
    ├── queries/            ← Kết quả research đã file-back
    ├── comparisons/        ← Bảng so sánh
    └── synthesis/          ← (Thay thế distilled/) Nơi bồi đắp tri thức, bài kiểm tra
```

**Quy tắc vàng:**
- `raw/sources/` → không ai sửa (Immutable Source)
- `wiki/concepts/` & `wiki/entities/` → Atomic Records (Lịch sử trích xuất, hỗ trợ Rule 14)
- `wiki/synthesis/` → **The Wiki Master** (Nơi bồi đắp tri thức nén, đa chiều)
- `distilled/` → [DEPRECATED] Đã gộp vào `wiki/synthesis/`
- `archive/` → Snapshot Storage (Lưu trữ vĩnh viễn, Wikilinks đã trung hòa)

---

## Lệnh điều khiển (Manus Commands)

| Lệnh | Agent | Mô tả |
| :--- | :--- | :--- |
| `/scout` | `@scout` | Nghiên cứu & Đánh giá độ khó (Difficulty Audit). |
| `/file-back` | `@pm` | Lưu kết quả phân tích có giá trị thành Wiki page mới (Query Compounding). |
| `/ingest` | `@scout` → `@engineer` | Quy trình 2 bước: (1) @scout phân tích raw file → tạo Analysis file; (2) User duyệt → @engineer tạo Wiki Atoms & cập nhật synthesis. |
| `/lint` | `@auditor` → `@librarian` | @auditor chạy full lint pass (broken links, orphans, frontmatter, dead sources) theo AUDITOR_Protocol.md. Sau đó @librarian nhận Lint Report và fix theo độ ưu tiên. |
| `/assess-difficulty` | `@scout` | Đánh giá tải nhận thức của tri thức. |
| `/heal` | `@healer` | Sửa lỗi dựa trên log hoặc báo cáo lỗi. |
| `/heartbeat` | `@librarian` | Tổng hợp `3-resources/raw/` và cập nhật đồ thị kiến thức. |
| `/graphify` | `@librarian` | Cập nhật hoặc truy vấn đồ thị kiến thức dự án (Structural Memory). |
| `/audit-tokens` | `@pm` | Kiểm tra ngân sách token của từng phiên làm việc (Warning mode). |
| `/scout-exam [module] [bloom_levels]` | `@scout` | Nghiên cứu chuyên biệt cho ra đề kiểm tra. Output ghi vào `1-projects/[Project]/EXAM_Context_[module].md` trước khi @engineer tiếp nhận. |
| `/audit-exam [file_đề]` | `@auditor` | Đối soát ngược từng câu hỏi. Thứ tự: (1) EXAM_Context → (2) wiki/synthesis → (3) raw/ nếu cần. KHÔNG dùng general knowledge. Nếu không tìm thấy → ghi `[KHÔNG TÌM THẤY NGUỒN]`. |
| `/profile [trainer_id] [level]` | `@profiler` | Tạo hoặc cập nhật Trainer Profile. Output ghi vào `2-areas/Profiles/Trainer_Profile_[id].md`. Level: `entry / intermediate / advanced`. |
| `/design [module] [trainer_level]` | `@designer` | Thiết kế learning sequence. Output ghi vào `1-projects/[Project]/Learning_Design_[module].md`. Bắt buộc đọc Trainer Profile trước. |
| `/evaluate [module] [kết_quả_file]` | `@evaluator` | Phân tích kết quả đào tạo theo Kirkpatrick Level 1-4. Output ghi vào `2-areas/Assessment/Eval_Report_[module].md`. |
| `/ingest-inbox` | `@librarian` | Đọc toàn bộ `00_Inbox/`, phân loại từng file, propose action trước khi execute. |

> **Lệnh đã deprecated**: `/distill`, `/consolidate` — Không còn dùng trong Schema v5+. Thay thế bằng `/ingest`.

---

## Phân quyền truy cập (Manus Scoped Access)

| Agent | Đọc | Ghi | Cấm tuyệt đối |
|:---|:---|:---|:---|
| **@pm** | Tất cả | `3-resources/wiki/log.md`, `CONTINUITY.md`, `1-projects/` (task plans) | Ghi `3-resources/raw/` |
| **@scout** | `3-resources/raw/`, `1-projects/` | `3-resources/wiki/` (draft), `1-projects/[Project]/EXAM_Context_*.md` | Ghi `3-resources/wiki/synthesis/` trực tiếp |
| **@engineer** | `1-projects/`, `3-resources/wiki/synthesis/` | `1-projects/[Project]/` (output task) | Ghi `3-resources/wiki/`, `3-resources/raw/` |
| **@librarian** | Tất cả | `3-resources/wiki/synthesis/` (sau verify), `3-resources/wiki/log.md` | Overwrite `3-resources/wiki/log.md` |
| **@auditor** | Tất cả (read-only) | `3-resources/wiki/log.md` (append only) | Ghi bất kỳ file nội dung nào |
| **@designer** | `3-resources/raw/`, `3-resources/wiki/synthesis/`, `2-areas/Profiles/Trainer_Profile_*.md` | `1-projects/[Project]/Learning_Design_*.md` | Bỏ qua Trainer_Profile |
| **@evaluator** | `1-projects/`, `3-resources/wiki/synthesis/` | `2-areas/Assessment/Eval_Report_*.md`, `3-resources/wiki/log.md` | — |
| **@profiler** | `3-resources/raw/`, `3-resources/wiki/synthesis/` | `2-areas/Profiles/Trainer_Profile_*.md` | — |
| **@creative** | `3-resources/wiki/synthesis/`, `3-resources/wiki/` | `docs/`, `res/`, `templates/` | Ghi `3-resources/` trực tiếp |
| **@healer** | Tất cả | `3-resources/wiki/` (sửa links), `scripts/` | Xóa file không có backup |
| **@devops** | Tất cả | `scripts/`, `tools/`, `libs/` | Ghi `3-resources/wiki/synthesis/` |

**Quy tắc ghi log bắt buộc:**
Mọi hành động ghi file → append vào `3-resources/wiki/log.md` theo format:
```
## [YYYY-MM-DD HH:MM] <type> | <agent> | <mô tả ngắn>
- File tạo/sửa: [đường dẫn]
- Lý do: [1 câu]
```

---

## Quy tắc Swarm v4.0 Supreme (Manus Standard)

1. **Manus First**: Ưu tiên đọc `task_plan.md` trước khi thực hiện bất kỳ hành động nào.
2. **Double Link**: Mọi note mới trong Wiki phải có ít nhất 2 liên kết `[[Wikilinks]]`.
3. **Knowledge Compounding (Rule 3)**: Mọi giải pháp, Insight hoặc tri thức mới từ Raw phải được bồi đắp (Compounded) trực tiếp vào các file Master trong `3-resources/wiki/synthesis/` ngay trong phiên làm việc. Không đợi đến cuối Pipeline.
4. **Log-First Ingest (Rule 4 - Absolute Encoding)**: Mọi thay đổi về tri thức hệ thống phải được ghi nhận vào `3-resources/wiki/log.md`.
    - **BẮT BUỘC** dùng append, không overwrite.
    - **BẮT BUỘC** sử dụng bảng mã UTF-8 (không BOM) khi ghi file.
    - **CẢNH BÁO ĐỎ:** Khi dùng PowerShell (`Add-Content`, `Out-File`), **PHẢI** thêm `-Encoding UTF8`. Nếu không, PowerShell 5.1 sẽ phá hủy ký tự Tiếng Việt (Mojibake).
    - **Ưu tiên:** Dùng Python hoặc `replace_file_content` để ghi log nếu có thể.
5. **Automated Self-Healing (Rule 5)**: Agent phải **tự động** triệu hồi `@healer` khi gặp lỗi hệ thống hoặc logic lặp lại.
6. **Budget Awareness (Rule 6)**: Thông báo cho người dùng khi phiên làm việc tiêu tốn >80% Budget đã định nghĩa.
7. **Hierarchy Limit (Rule 7 - Semantic Structure)**:
    - Cấp 1 (Root Buckets): `00_Inbox/`, `1-projects/`, `2-areas/`, `3-resources/`, `4-archive/`, `scripts/`, `tools/`.
    - `00_Inbox/`: Files flat, không subfolder, prefix YYYYMMDD_, xử lý hàng tuần.
    - Cấp 2 (Buckets):
      - `1-projects/`: Mỗi dự án là 1 folder (vd: `2026_TOT_STEAM/`, `2026_Data_Analyst/`)
      - `2-areas/`: `Curriculum/`, `Assessment/`, `Profiles/`
      - `3-resources/`: `raw/`, `wiki/`
      - `scripts/`: `maintenance/`, `pipelines/`, `tests/`
    - Cấp 3 — **Ngoại lệ `wiki/`**: Thư mục `3-resources/wiki/` được phép có các thư mục con ngữ nghĩa:
      - `wiki/concepts/` ← Trang khái niệm, kỹ thuật (THINK_*, ACAD_*, STAT_*...)
      - `wiki/entities/` ← Trang thực thể (công cụ, hệ thống, tổ chức)
      - `wiki/sources/` ← Trang tóm tắt nguồn sách đã Ingest
      - `wiki/queries/` ← Kết quả chat/research đã file-back
      - `wiki/synthesis/` ← Nơi bồi đắp tri thức, so sánh, bài kiểm tra
      - `wiki/comparisons/` ← Bảng so sánh song song
      - `wiki/assets/` ← Hình ảnh, sơ đồ minh họa
    - Cấp 3 (Files, áp dụng cho tất cả trừ `wiki/`): Phải là tệp tin trực tiếp. **KHÔNG CÓ THƯ MỤC CON**.
    - **Quy tắc Lưu trữ (Archiving)**: Khi hoàn thành task, các file từ `1-projects/` hoặc tài liệu cũ phải được chuyển vào `4-archive/` với prefix `YYYYMMDD_`.
    - **Quy tắc Trung hòa (Neutralization)**: Khi di chuyển file vào `4-archive/`, PHẢI chuyển đổi Wikilinks `[[...]]` thành văn bản thuần (bọc trong backticks) để không làm loãng đồ thị tri thức.
    - **Quy tắc Prefix 2 cấp**: Bắt buộc đặt tên file theo cấu trúc `[CẤP_1]_[CẤP_2]_[TÊN_FILE].md`.
        - **KHMT**: AI_THCS, AI_Tieu_hoc, Python, Scratch, Scratch_Jr, Tynker.
        - **Robot**: Codey, GBot, mBot, Rover, Unplugged, xBot.
        - **DESIGN**: 3D_Tinkercad, Canva, Maker_Empire, Wordpress.
        - **PROMPT**: K10_Toan, K10_Van, K10_Anh.
        - **ACAD**: Biology, Math, Physics.
8. **Machine-Readability**: Đặt tên File/Folder theo chuẩn `Snake_Case`, prefix bằng số (`01_`, `02_`) và sử dụng YAML Frontmatter cho ngữ cảnh.
9. **Exam Handoff Protocol (Rule 9)**: Khi tạo đề kiểm tra, `@scout` PHẢI hoàn thành và ghi `1-projects/[Project]/EXAM_Context_[module].md` chứa:
    - Danh sách concept chính xác cần kiểm tra (trích từ tài liệu gốc).
    - Terminology chuẩn (không paraphrase).
    - Phạm vi KHÔNG kiểm tra (negative scope).
    - `@engineer` chỉ được bắt đầu viết sau khi file này tồn tại.
10. **Anti-Hallucination Reverse Tracing (Rule 10 - Absolute)**:
    Khi thực hiện bất kỳ tác vụ truy xuất ngược nào, agent BẮT BUỘC phải:
    a. Tuân thủ nghiêm ngặt `AUDITOR_Protocol.md`.
    b. Chỉ trích dẫn từ file có trong `3-resources/raw/` hoặc `3-resources/wiki/synthesis/` — KHÔNG dùng general knowledge.
    c. Với mỗi claim, ghi rõ: `Nguồn: [tên file] — [dòng/section cụ thể]`
    d. Nếu không tìm thấy nguồn: → Ghi `[KHÔNG TÌM THẤY NGUỒN]` → Báo cáo cho `@auditor` → KHÔNG tự điền nội dung thay thế.
    e. **@auditor** là agent duy nhất được phép thực hiện reverse tracing.
11. **Pedagogical Pipeline (Rule 11 - Absolute Sequence + Guard)**:

    | Bước | Agent | Prerequisite file phải tồn tại |
    |---|---|---|
    | 1 | @profiler | Không cần |
    | 2 | @designer | `2-areas/Profiles/Trainer_Profile_[id].md` |
    | 3 | @engineer | `1-projects/[Project]/Learning_Design_[module].md` |
    | 4 | @evaluator | `2-areas/Assessment/Eval_Report_[module].md` |

    Nếu file prerequisite KHÔNG tồn tại → agent DỪNG ngay, báo @pm, KHÔNG tự tiếp tục.

12. **RAW IS IMMUTABLE (Rule 12)**:
    - `3-resources/raw/` là READ-ONLY với TẤT CẢ agents.
    - Vi phạm → @healer rollback ngay, ghi incident vào `3-resources/wiki/log.md`.
    - CHỈ người dùng mới được thêm file mới vào `3-resources/raw/`.

13. **WIKI CATALOGING (Rule 13)**:
    - Mọi tệp tin kiến thức khi tạo/sửa đều PHẢI được cập nhật vào `3-resources/wiki/index.md`.
    - **BẮT BUỘC**: Trước khi tạo/sửa Wiki, Agent phải đọc `3-resources/WIKI_AGENT_GUIDE.md`.
    - Khi tạo file `SOURCE_`: BẮT BUỘC sao chép cấu trúc từ `3-resources/SOURCE_TEMPLATE.md`.
    - Khi tạo file `QUERY_`: BẮT BUỘC sử dụng cấu trúc từ `3-resources/QUERY_template.md`.

14. **SOURCE INTEGRITY (Rule 14)**:
    - Khi viết trường `Nguồn`, agent phải **thực sự mở file đó** trong `3-resources/raw/` trước khi viết.
    - Chỉ ghi tên file raw gốc hiện tồn tại — không ghi file tổng hợp trung gian đã deprecated.
    - Checklist ATOMS bắt buộc có mục: `- [ ] [Rule 14] Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại`.
    - Vi phạm: ATOMS không được phép đổi status thành `verified`.

15. **EXECUTION INTEGRITY (Rule 15)**:
    - Tuyệt đối KHÔNG báo cáo "Đã tạo/sửa file" nếu chưa thực hiện tool call thành công.
    - Vi phạm: Phải tự phê bình và ghi lỗi vào `CONTINUITY.md`.

16. **EXTRACTION_MANDATORY_STATS (Rule 16)**:
    - Mọi tệp tin trung gian trong `1-projects/[Project]/` PHẢI dùng cấu trúc từ `3-resources/PROCESS_TEMPLATE.md`.
    - Bắt buộc có **Bảng thống kê hiệu suất Khai thác (Mining Stats)** ở đầu file.
    - Phải liệt kê danh sách Master Files đã được bồi đắp tri thức từ nguồn này.

17. **DOUBLE EXAMPLES MANDATORY (Rule 17)**:
    - Mọi trang Concept/Entity BẮT BUỘC có khối `## Ví dụ đối chiếu (Rule 17: Double Examples)` trước phần trích dẫn Nguồn.
    - Khối này PHẢI có chính xác 2 ví dụ:
      1. **Ví dụ từ sách (Original)**: Trích dẫn sát thực tế tài liệu gốc.
      2. **Ứng dụng sư phạm (Pedagogical Application)**: Chuyển đổi sang tình huống dạy học/STEAM/EdTech.
    - Vi phạm: @librarian/@auditor block trang đó khỏi danh mục "verified".

18. **FILE OPERATION STANDARD (Rule 18)**:
    - Agent KHÔNG được tự generate lệnh PowerShell/bash tùy ý để ghi file.
    - Mọi thao tác tạo/sửa file BẮT BUỘC đi qua MCP Filesystem tool.
    - Sửa file đã tồn tại: `edit_file` / `replace_file_content` (patch mode). NGHIÊM CẤM `write_file` cho file đã có.
    - Tạo file mới: `create_file` / `write_file`.
    - Append log.md: `edit_file` (chỉ thêm cuối, không xóa dòng nào).
    - **Báo cáo sau mỗi lần ghi (bắt buộc)**:
      ```
      WRITE REPORT:
        file: "[đường dẫn]"
        operation: "append | patch | create"
        added: "[tóm tắt 1 câu]"
        removed: "[tóm tắt 1 câu — hoặc NONE]"
      ```
    - Vi phạm → @healer rollback ngay lập tức.

19. **QUERY_STANDARDIZATION (Rule 19)**:
    - Mọi kết quả research khi lưu vào `3-resources/wiki/queries/` PHẢI dùng prefix `QUERY_` và tuân thủ `3-resources/QUERY_template.md`.
    - Trường bắt buộc: `type: query`, `title`, `tags`, `related`, `source_tool`.

20. **TRIPLE-VIEW PROTOCOL (Rule 20 - Absolute)**:
    Trước khi tạo hoặc chỉnh sửa bất kỳ tệp tin nào trong `3-resources/wiki/`, agent BẮT BUỘC thực hiện:
    a. `view_file` Template tương ứng (vd: `SOURCE_TEMPLATE.md`, `CONCEPT_TEMPLATE.md`).
    b. `view_file` Nguồn thô trong `3-resources/raw/sources/` (đảm bảo Rule 14).
    c. Chỉ sau khi có 2 tool call trên, mới thực hiện lệnh ghi/sửa file.
    d. Trong nội dung file, mục `WRITE REPORT` phải có dòng: `compliance: "[Rule 20] Đã đối soát Template và Raw thành công."`

21. **SELF-AUDIT INTEGRITY LOOP (Rule 21)**:
    a. Ngay sau khi thực hiện lệnh ghi file, agent (đóng vai `@auditor`) phải thực hiện 1 lệnh `view_file` ngược lại chính file vừa tạo để đối soát với Template.
    b. Nếu phát hiện sai sót về cấu trúc, agent phải tự động sửa lỗi ngay lập tức TRƯỚC KHI kết thúc phiên làm việc.
    c. Vi phạm trình tự này sẽ bị `@healer` rollback và ghi incident vào `log.md`.

---

## CHECKPOINT Protocol (Bắt buộc mọi agent)

Trước khi thực hiện BẤT KỲ task nào, agent PHẢI trả lời chính xác block sau:

```yaml
CHECKPOINT:
  agent: "@[tên agent]"
  task: "[tên task cụ thể — không được viết chung chung]"
  step: "[bước X / tổng Y bước trong pipeline]"
  output_file: "[đường dẫn file sẽ tạo]"
  stop_condition: "[điều kiện dừng cụ thể]"
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
