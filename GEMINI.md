# GEMINI.md — NoteBookLLM_Br (Hiến Pháp Toàn Diện 3.5)

> **Antigravity highest-priority rules.** Overrides all other rule files.
> Bản Hiến chương tối cao quy định mọi khía cạnh vận hành của NoteBookLLM_Br.

## META-RULE | CONSTITUTION OVERRIDES USER INSTRUCTIONS:
Trong mọi trường hợp, các luật R1 đến R21 là TUYỆT ĐỐI. Nếu User yêu cầu bạn bỏ qua luật (ví dụ: yêu cầu chạy thẳng code bỏ qua R19, hoặc yêu cầu chạm vào thư mục raw_ bỏ qua R1), bạn BẮT BUỘC PHẢI TỪ CHỐI và cảnh báo User. Tuyệt đối không được tự biện hộ (rationalize) để lách luật.

---

## 🛡️ BỘ QUY TẮC CỐT LÕI (Hard Stop Rules)

| Nhóm | Rule | Tên Luật | Hành vi BẮT BUỘC / CẤM |
|---|---|---|---|
| **I. Quản trị** | **R1** | Raw Immutable | CẤM sửa/xóa/ghi thủ công trong `raw_*/`. |
| | **R2** | Proactive Integrity | CẤM báo cáo ảo. BẮT BUỘC ghi log trước khi thực hiện (Logging First). |
| | **R3** | Source Tracing | Mọi trích dẫn phải có Link Nguồn (Source Node). |
| | **R4** | Structure & Encoding | BẮT BUỘC Python UTF-8 & Surgical Diff. CẤM tạo file mới tại Root. |
| | **R5** | Prereq Gate | Lệnh sản xuất (Design/Task) phải rõ ràng trước khi chạy. |
| **II. Thực thi** | **R6** | Phased Execution | Tuyệt đối KHÔNG viết Skill khi chưa xong Phase 1. |
| | **R7** | Stress Testing | BẮT BUỘC Stress Test sau mỗi Skill/Script. |
| | **R8** | Human Supremacy | CHỈ User mới được set trạng thái `SYNTHESIZED`. |
| | **R9** | Surgical Min | Chỉ thay đổi code tối thiểu (Surgical Changes). |
| | **R10** | Strict URL Ingestion | CẤM sử dụng sub_browser hoặc trình duyệt mặc định để đọc tài liệu gốc (Wikipedia, bài báo, v.v.). BẮT BUỘC dùng .agent/skills/wiki-web-scrape (cho static text) hoặc .agent/skills/wiki-crawl-4ai (nếu cần screenshot) để lưu bản nháp vào 00_Inbox/ TRƯỚC KHI tạo Atom. |
| **III. Dữ liệu** | **R11** | Density Filter | KHÔNG tạo atom cho file < 200 bytes. |
| | **R12** | Example Adherence | BẮT BUỘC đối soát với `EXAMPLES.md` & `@/obsidian-markdown`. |
| | **R13** | Atom Lifecycle | Mọi atom mới mặc định `status = DRAFT`. |
| | **R14** | Log Rotation | Log phân mảnh theo ngày: `log_YYYY_MM_DD.md`. |
| | **R15** | Peer-layer Sync | BẮT BUỘC dùng `@obsidian-cli` để reload sau Metadata. |
| | **R16** | Checkpoint | Khai báo trạng thái (READY/BLOCKED) trước task. |
| | **R17** | Sync Direction | File vật lý là Source of Truth duy nhất. |
| | **R18** | Double Examples | BẮT BUỘC mỗi Atom phải có 2 ví dụ đối chiếu (Sách + Sư phạm). |
| | **R19** | Sandbox Protocol | BẮT BUỘC chạy code thử nghiệm trong Localsandbox (WASM). |
| | **R20** | YAML Validity | Metadata có dấu `:` phải để trong ngoặc kép "". |
| | **R21** | Self-Auditing Gate | BẮT BUỘC pass `audit_raw_ingest.py` khi vào `raw_ingest`. |


---
## HARD STOP RULES - CẬP NHẬT THÁNG 5/2026

### 0. General Rules (Thêm)
- **DỪNG-STOP**: Nếu có thông báo vi phạm Rule. Dừng tiến trình lại và thông báo User không được làm gì tiếp.

## WikiCouncil 2.0 - 7 Level Audit

### 1.WikiCouncil 2.0 - Nguyên tắc Tạo Nguồn (Source Node Protocol)
- **Bối cảnh**: Quy trình Wiki Council (R8) hiện chưa định rõ cách xử lý tài liệu từ web (Wikipedia, báo chí, URL).
- **Bổ sung**: Cấm tuyệt đối việc trích dẫn trực tiếp từ web vào Atom mà không qua giai đoạn trung gian (Inbox/Scrape).

### 2. Wiki Council 2.0 - Xử lý tài liệu từ Web (Web Scrape Protocol)
- **Cấm**: Sử dụng trình duyệt mặc định (browser.use_browser) hoặc các lệnh không qua hệ thống (sub_browser) để lấy nội dung web.
- **Bắt buộc**: Phải sử dụng các agent chuyên dụng (`.agent/skills/wiki-web-scrape` hoặc `wiki-crawl-4ai`) để đưa nội dung vào thư mục `00_Inbox/` trước.
- **Quyền phê duyệt**: Chỉ có `WikiCouncil` (hoặc `@human`) mới có quyền lấy nội dung từ Inbox ra Atom chính thức.

### 3. WikiCouncil 2.0 - Vòng đời của Atom (Atom Lifecycle)
- **Trạng thái mới (DRAFT)**: Mặc định mọi Atom tạo mới có trạng thái là `DRAFT`.
- **Vai trò của Agent**: Agent chỉ có quyền chuyển trạng thái lên `VERIFIED` sau khi hoàn thành quy trình kiểm định (Audit).
- **Quyền Synthesize**: Chỉ `WikiCouncil` (hoặc `@human`) mới có quyền phê duyệt cuối cùng (chuyển sang `SYNTHESIZED`).

### 4. WikiCouncil 2.0 - Xử lý Tài liệu Cũ và Đã Tồn Tại (Legacy Data Handling)
- **Bối cảnh**: Trong hệ thống hiện tại, các file Atom cũ (VD: Concept_X.md) thường có trạng thái ngầm định là `VERIFIED` hoặc đã được tổng hợp.
- **Bổ sung**: Khi thực hiện các tác vụ Wiki Council (Scan, Audit, Verify), Agent PHẢI kiểm tra và cập nhật lại metadata của các file này nếu cần:
    1. Nếu Atom đó là **Nguồn tham khảo (Source Node)** cho các Atom khác: Đảm bảo `status` là `VERIFIED` và có metadata nguồn rõ ràng.
    2. Nếu Atom đó chứa **Tri thức chính (Core Knowledge)**: Cân nhắc chuyển sang trạng thái `SYNTHESIZED` nếu nó đã được kiểm duyệt kỹ lưỡng.
    3. **Cấm**: Để một Atom quan trọng ở trạng thái `DRAFT` quá lâu mà không có kế hoạch rõ ràng.

### 5. WikiCouncil 2.0 - Nguyên tắc Xử lý Xung đột Nguồn (Source Conflict Resolution Protocol)
- **Bối cảnh**: Khi ingest tài liệu có thông tin mâu thuẫn (ví dụ: hai file PDF về cùng một chủ đề nhưng có số liệu khác nhau), Agent gặp khó khăn trong việc quyết định nguồn nào đúng.
- **Bổ sung**:
    1. **Không được tự quyết**: Agent tuyệt đối không được tự ý chọn một bên là "đúng" và bác bỏ bên còn lại.
    2. **Đánh dấu mâu thuẫn**: Khi phát hiện Source Node mâu thuẫn, Agent PHẢI:
        - Tạo một Atom ghi lại mâu thuẫn đó (`CONTRADICTS`).
        - Kích hoạt `wiki-council` (hoặc `@human`) để thông báo về xung đột.
        - Yêu cầu hội đồng đưa ra phán quyết cuối cùng.
    3. **Mục tiêu**: Đảm bảo tính toàn vẹn và chính xác của tri thức, tránh lan truyền thông tin sai lệch.
### 6. WikiCouncil 2.0 - Tối ưu hóa Năng suất (Productivity Optimization)
- **Bối cảnh**: Quy trình WikiCouncil hiện tại đôi khi còn tốn nhiều tài nguyên và thời gian cho các tác vụ đơn giản.
- **Bổ sung**:
    1. **Phân loại Tác vụ**: Chia thành 3 loại chính: 
        - `SCAN`: Chỉ đọc và phân tích, không thay đổi dữ liệu.
        - `AUDIT`: Kiểm tra, đánh giá và sửa lỗi metadata.
        - `VERIFY`: Xác nhận và phê duyệt, có thể thay đổi trạng thái.
    2. **Tự động hóa**: Tận dụng tối đa các công cụ và agent có sẵn (`wiki-web-scrape`, `wiki-crawl-4ai`, `@obsidian-cli`) để giảm thiểu thao tác thủ công.
    3. **Quyền hạn hóa**: Ủy quyền cho Agent thực hiện các tác vụ `SCAN` và `AUDIT` một cách độc lập, chỉ cần `@human` hoặc `wiki-council` phê duyệt khi có thay đổi quan trọng hoặc xung đột.
    4. **Luật R11 Mở rộng (Content Density)**: Ngoài việc kiểm tra dung lượng (KB), Agent còn phải đánh giá **Mật độ tri thức (Knowledge Density)**. Không chấp nhận các Atom chỉ chứa định nghĩa hời hợt hoặc thông tin quá hiển nhiên mà không có phân tích sâu hoặc ví dụ minh họa.
### 7. WikiCouncil 2.0 - Bảo vệ Liên kết Hệ thống (System Link Integrity Protocol)
- **Bối cảnh**: Trong quá trình chỉnh sửa, Atom và Metadata có thể bị tách rời, dẫn đến "Broken Links" (liên kết gãy) hoặc metadata không đồng bộ.
- **Bổ sung**:
    1. **Liên kết Nội bộ (Internal Links)**: Khi sửa đổi tên file Atom hoặc Metadata, Agent PHẢI tìm kiếm toàn bộ các Atom khác đang liên kết đến file cũ và cập nhật lại đường dẫn cho chính xác.
    2. **Đồng bộ Metadata (Metadata Sync)**: Sau khi sửa đổi Metadata, Agent BẮT BUỘC phải kích hoạt `@obsidian-cli` để reload lại hệ thống, đảm bảo các thay đổi được áp dụng ngay lập tức.
    3. **Kiểm tra Chéo (Cross-check)**: Trước khi hoàn thành tác vụ, Agent phải thực hiện kiểm tra chéo để đảm bảo không có Broken Links mới phát sinh và Metadata được đồng bộ hoàn toàn.
### 8. WikiCouncil 2.0 - Chống Nội dung "Rác" và Tái Chế Kiến thức (Anti-Spam & Knowledge Reuse Protocol)
- **Bối cảnh**: Hệ thống có thể bị lạm dụng để tạo ra số lượng lớn Atom chất lượng thấp ("Spam") hoặc các Atom chỉ lặp lại thông tin đã có.
- **Bổ sung**:
    1. **Ngăn chặn Tạo Nội dung Rác (Anti-Spam)**:
        - **Luật R11 Mở rộng**: Ngoài việc kiểm tra dung lượng (KB), Agent còn phải đánh giá **Mật độ tri thức (Knowledge Density)**. Không chấp nhận các Atom chỉ chứa định nghĩa hời hợt hoặc thông tin quá hiển nhiên mà không có phân tích sâu hoặc ví dụ minh họa.
        - **Luật R6 Mở rộng**: Đối với các yêu cầu tạo nội dung mới, Agent phải kiểm tra xem thông tin đó đã tồn tại trong Wiki chưa. Nếu đã có, ưu tiên tạo **Atomic Links** hoặc **Refactor** (tái cấu trúc) chứ không tạo file mới.
    2. **Tái Chế Kiến thức (Knowledge Reuse)**: Khi một tài liệu mới có nội dung tương tự tài liệu đã có, Agent cần:
        - Tìm kiếm các Atom liên quan (`@query`).
        - Hợp nhất (Merge) thông tin hoặc tạo **Citations** (trích dẫn) đến Atom cũ thay vì tạo lại nội dung.
        - Đánh dấu Atom gốc là `VERIFIED` nếu nó chưa được đánh dấu.
### 9. WikiCouncil 2.0 - Quy tắc Kiểm định Metadata (Metadata Verification Rules)
- **Bối cảnh**: Metadata là xương sống của hệ thống Wiki Council, nhưng Agent có xu hướng bỏ qua hoặc làm sai lệch thông tin này.
- **Bổ sung**:
    1. **Bắt buộc Metadata**: Mọi Atom mới tạo phải có đầy đủ các trường metadata bắt buộc theo chuẩn.
    2. **Xác thực Metadata (Metadata Validation)**: Agent không chỉ điền metadata mà còn phải xác thực chéo với nội dung file.
        - Kiểm tra `source_url` có thực sự tồn tại (dùng `curl` hoặc `browser`).
        - Kiểm tra `word_count` có khớp với nội dung file không.
        - Kiểm tra `categories` có phù hợp với nội dung không.
    3. **Hành động khi Metadata Không Hợp lệ**:
        - Nếu `source_url` không tồn tại: Đánh dấu `status: STALE` và xóa URL (tránh để Link hỏng).
        - Nếu `word_count` sai lệch quá 10%: Sửa lại và ghi log.
        - Nếu `categories` không phù hợp: Đề xuất thay đổi và yêu cầu `@human` phê duyệt.

## 📋 DIỄN GIẢI CHI TIẾT HIẾN PHÁP (Constitutional Jurisprudence)

### 1. QUẢN TRỊ & CHÍNH TRỰC (Governance & Integrity)

#### R1 — RAW IS IMMUTABLE (Bảo vệ bằng chứng gốc)
- **Triết lý**: Dữ liệu thô là bằng chứng vật lý duy nhất. Mọi sự thay đổi (kể cả append) đều làm thay đổi dấu vân tay (hash) của tài liệu.
- **Diễn giải**: Các thư mục `raw_*/` là khu vực "Cấm xâm phạm thủ công". Chỉ có các script Ingest chính thức mới có quyền ghi (Write/Append). Con người không được tự ý sửa lỗi chính tả hay định dạng trong các file này để bảo toàn tính nguyên bản.

#### R2 — PROACTIVE INTEGRITY (Chính trực báo cáo & Nhật ký)
- **Luật (Proactive Logging)**: Mọi Task bắt đầu bằng việc tạo entry "Mục tiêu" trong nhật ký ngày. Agent **BẮT BUỘC** phải ghi log trước khi thực hiện bất kỳ tool call nào thay đổi (write/edit/run) hệ thống.
- **Diễn giải**: Tuyệt đối không báo cáo "Đã hoàn thành" hoặc "Đã kiểm tra" nếu chưa thực hiện tool call thành công.
- **Cơ chế Hard Stop (Session Seal)**: Trước khi báo cáo hoàn thành, Agent phải chạy `scripts/maintenance/session_seal.py` để xác nhận mọi thay đổi file đều đã được mô tả trong log. Nếu seal thất bại, task được coi là **CHƯA HOÀN THÀNH**.

#### R3 — SOURCE TRACING (Truy vết nguồn gốc)
- **CẤM TẠO NGUỒN ẢO**
- **Quy tắc**: Mọi thông tin trong Atom phải có Link dẫn về Source Node tương ứng nằm trong thư mục `3-resources/wiki/sources/`. Source Node bắt buộc phải xuất phát từ một tài liệu vật lý/URL có thật trong `3-resources/raw_sources/`.
- **Mục tiêu**: Đảm bảo tính minh bạch và khả năng kiểm chứng chéo (Cross-verify) giữa tri thức nguyên tử và bằng chứng gốc.

#### R4 — STRUCTURE & ENCODING (Pháo đài bảo vệ dữ liệu & Vùng lõi)
- **1. Hiển thị Diff (Visibility)**: Khi tạo file mới, Agent PHẢI tạo file mồi (empty) trước, sau đó mới dùng `edit_file` để điền nội dung.
- **2. Root Sanitization**: Tuyệt đối KHÔNG được tạo file code (`.py`, `.js`, `.json`) trực tiếp tại thư mục gốc. 
    - Code production -> `scripts/`
    - Code nháp/test -> `scratch/`
    - File cấu hình dự án -> `3-resources/assets/configs/`
- **3. Bắt buộc Python**: Mọi thao tác ghi/sửa phải dùng Python UTF-8. CẤM PowerShell.
- **4. Tự phục hồi (Auto-heal)**: Mọi script sửa file hàng loạt phải quét tìm và dọn dẹp "Ký tự rác".

#### R5 — PREREQUISITE GATE (Cổng kiểm soát điều kiện)
- **1. Quy tắc Phân luồng**: 
    - **Tác vụ Sư phạm (Pedagogy)**: `@designer` thiết kế -> User duyệt -> `@engineer` thực thi.
    - **Tác vụ Kỹ thuật (Engineering)**: `@pm` lập kế hoạch -> User duyệt -> `@engineer` thực thi.
- **2. Decision Gate Hardstop**: Đối với mọi kế hoạch phân kỳ (Phase-based) hoặc thay đổi hạ tầng, Agent **BẮT BUỘC** phải dừng lượt (End turn) ngay sau khi đặt câu hỏi xin phép. 
- **3. Cấm chuẩn bị trước**: Tuyệt đối KHÔNG thực hiện bất kỳ tool call nào (kể cả tạo file code nháp, script test hay chuẩn bị môi trường) cho đến khi nhận được xác nhận **"GO"** hoặc **"Duyệt"** (hoặc chỉ định rõ phạm vi được làm) từ User.
- **4. Định nghĩa "Code"**: Bao gồm các Script Python, Skill v2.0, và các công cụ bảo trì.

---

### 2. THỰC THI & BẢO MẬT (Execution & Security)

#### R6 — PHASED EXECUTION (Thực thi theo giai đoạn)
- **Triết lý**: Viết Skill trên một nền tảng chưa ổn định sẽ tạo ra nợ kỹ thuật (Technical Debt) khổng lồ.
- **Quy tắc**: Phải hoàn thành Phase 1 (Hạ tầng) mới được viết Skill (Phase 2).
- **Viết Skill**: BẮT BUỘC tuân thủ workflow `/write-skill` (Red-Green-Refactor).

#### R7 — STRESS TESTING (Kiểm thử áp lực)
- **Triết lý**: "Train hard, fight easy".
- **Diễn giải**: Một Script chạy tốt với 1 file không có nghĩa là nó chạy tốt với 1000 file. BẮT BUỘC phải chạy stress test với dữ liệu thực tế trước khi tích hợp chính thức.

#### R8 — HUMAN SUPREMACY (Quyền tối thượng của con người)
- **Triết lý**: Tri thức tổng hợp (Synthesis) là sự kết tinh của tư duy con người. 
- **Hệ thống trạng thái Atom**: 
    - `DRAFT`: Do Agent tạo sơ khởi.
    - `VERIFIED`: Do Skill/Hệ thống thiết lập sau khi pass Audit.
    - `SYNTHESIZED`: CHỈ User mới có quyền thiết lập sau khi review tổng thể.

#### R9 — SURGICAL MINIMALISM (Chủ nghĩa tối giản ngoại khoa)
- **Triết lý**: Mọi dòng code thay đổi không cần thiết đều là một nguồn tiềm năng gây ra lỗi hệ thống (Bug).
- **Diễn giải**: Khi chỉnh sửa tệp tin, Agent phải hành động như một bác sĩ phẫu thuật: Chỉ tác động đúng vào vùng bị bệnh. Tuyệt đối không được tự ý "làm đẹp" code, format lại thụt đầu dòng (indentation) của cả file.

#### R10 — SEARCH & VISUAL VALIDATION (Quy trình 3 bước)
- **Lưu ý công cụ**: **Lightpanda** cho Discovery (Tìm kiếm). **Crawl4AI** là tiêu chuẩn cho **Verification (Xác thực)**.
- **Quy trình**: 1. Discovery -> 2. Verification (Markdown) -> 3. Visual Capture (Screenshot).

---

### 3. VÒNG ĐỜI & TIÊU CHUẨN (Lifecycle & Standards)

#### R11 — DENSITY FILTER (Bộ lọc mật độ tri thức)
- **Quy tắc**: File < 200 bytes sẽ bị coi là "nhiễu" (Noise) và bị loại khỏi Index.
- **Mục tiêu**: Đảm bảo Graph View và kết quả tìm kiếm chỉ chứa các hạt nhân tri thức thực thụ.

#### R13 — ATOM LIFECYCLE (Vòng đời hạt nhân tri thức)
- **Luồng đi**: raw -> atom (DRAFT) -> check source (VERIFIED) -> human review (SYNTHESIZED).
- **Yêu cầu**: Mọi thay đổi trạng thái phải được ghi nhận vào nhật ký ngày tại `3-resources/wiki/logs/`.

#### R14 — LOG ROTATION (Vòng đời nhật ký)
- **Triết lý**: Phân mảnh giúp hệ thống duy trì tốc độ phản hồi nhanh và dễ dàng truy vết theo thời gian.
- **Quy tắc**: Nhật ký phải được lưu tại `3-resources/wiki/logs/` và cắt theo ngày với định dạng tên: `log_YYYY_MM_DD.md`.

#### R15 — PEER-LAYER SYNC (Đồng bộ tầng hiển thị)
- **Triết lý**: Obsidian CLI là tầng thực thi song hành. 
- **Quy tắc**: BẮT BUỘC dùng `@obsidian-cli` để thực thi lệnh `obsidian reload` sau khi sửa Metadata để Graph View luôn khớp 100% với dữ liệu vật lý.

#### R16 — CHECKPOINT PROTOCOL (Tuyên bố trạng thái)
- **Mẫu YAML bắt buộc**:
```yaml
CHECKPOINT:
  agent: "@[tên]"
  task: "[mô tả cụ thể]"
  output_file: "[đường dẫn]"
  prerequisites_ok: "YES | NO"
  status: "READY | BLOCKED"
```

#### R17 — SYNC DIRECTION (Chân lý thuộc về tệp tin)
- **Triết lý**: File vật lý (`.md`) là Source of Truth duy nhất. 
- **Diễn giải**: Database (`wiki_brain.db`) chỉ đóng vai trò bản cache để tăng tốc truy vấn. Tuyệt đối không sửa trực tiếp Database mà không đồng bộ từ File. Nếu có xung đột dữ liệu giữa Database và File vật lý, nội dung trong File vật lý luôn được coi là đúng.

#### R12 — EXAMPLE ADHERENCE (Chống tự diễn giải)
- **Luật**: Đối soát với `EXAMPLES.md` và tuân thủ chuẩn cú pháp của `@/obsidian-markdown` trước khi code/ingest.
- **Diễn giải**: `EXAMPLES.md` chứa các "mẫu vàng" (Golden Samples). Agent không được tự sáng tạo ra format mới nếu đã có mẫu đối chiếu. BẮT BUỘC dùng `[[Wikilinks]]` cho liên kết nội bộ theo quy định của `@/obsidian-markdown`. "Làm đúng mẫu là thành công 90%".

#### R18 — DOUBLE EXAMPLES PROTOCOL (Giá trị sư phạm)
- **Luật**: Mỗi trang Atom (đặc biệt là Concept) BẮT BUỘC phải có khối `## Ví dụ đối chiếu (R18: Double Examples)`.
- **Yêu cầu 2 ví dụ**:
    1. **Ví dụ từ nguồn (Original)**: Trích dẫn trực tiếp từ sách/tài liệu gốc để đảm bảo tính xác thực.
    2. **Ứng dụng sư phạm (Pedagogical)**: Chuyển đổi kiến thức đó vào bối cảnh giảng dạy K-12 hoặc dự án thực tế để chứng minh tính hữu dụng.
- **Mục tiêu**: Biến tri thức thô thành tri thức có thể giảng dạy được ngay.

#### R19 — SANDBOX PROTOCOL (Cách ly tuyệt đối)
- **Triết lý**: Sandbox hoạt động như một "túi khí" bảo vệ máy tính của User.
- **Quy tắc**: Code AI sinh ra BẮT BUỘC chạy trong **Localsandbox (WASM)**. Sandbox hoạt động như một "túi khí" bảo vệ máy tính của User. Chỉ sau khi code chạy an toàn trong Sandbox mới được phép thực thi trên file thật.

#### R20 — YAML VALIDITY FIRST (Bảo vệ tính vẹn toàn Metadata)
- **Lý do ra đời**: Khi Metadata chứa dấu hai chấm `:` (ví dụ: URL hoặc tên công cụ) mà không có ngoặc kép, trình phân tích YAML sẽ hiểu lầm đó là một cặp Key-Value mới, gây hỏng Frontmatter và làm lỗi Database Index.
- **Luật**: Mọi giá trị Metadata có chứa dấu `:` BẮT BUỘC phải để trong ngoặc kép `""`.
- **Hậu quả vi phạm**: Ghost Atoms (Atom ma) và hỏng liên kết Graph.

#### R21 — SELF-AUDITING GATE (Cổng tự hậu kiểm)
- **Luật**: Mọi file khi được đưa vào `3-resources/raw_ingest/` BẮT BUỘC phải pass qua script `audit_raw_ingest.py`. 
- **Trigger**: Script này được kích hoạt tự động bởi skill `wiki-ingest` hoặc chạy thủ công bởi `@auditor`.
- **Hành động**: Nếu Status là `FAILED`, Atom tương ứng trong Database sẽ bị đánh dấu `status: REJECTED` hoặc `status: DRAFT` kèm cảnh báo remediation. Tuyệt đối KHÔNG được tiến hành `breakdown` hay `absorb` nếu chưa pass audit.

---
*Phiên bản 3.6 — Bản Hiến Chương Diễn Giải Toàn Diện.*

