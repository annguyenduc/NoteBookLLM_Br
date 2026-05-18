# Bảng Chỉ Mục Skills (Wiki 2.0 Skill Index)

Bảng chỉ mục này là lookup reference cho skills, không phải startup file bắt buộc và không override `AGENTS.md`.

Bảng chỉ mục này phân loại và tóm tắt chức năng của các Skills cốt lõi đang hoạt động trong hệ thống NoteBookLLM_Br, giúp định hướng luồng công việc (Workflow).

## 1. 📥 Nạp Dữ Liệu & Tiền Xử Lý (Ingestion)
Nhóm kỹ năng dùng để cào dữ liệu, xử lý file thô và tạo Atom nháp (DRAFT).
- **`source-preview` / `process-raw-resource`**: Đọc nhanh nguồn, tạo learning map, và đề xuất có ingest chính thức không. Preview-only, non-canonical, `CHAT_ONLY` by default at runtime.
- **`wiki-ingest`**: Stage deterministic của ingest lifecycle. Đăng ký file đã được chuẩn bị vào Review Queue bằng hash + score; không phải full user-facing `/ingest` entrypoint.
- **`wiki-web-scrape`**: Cào dữ liệu web an toàn bằng Lightpanda. Chuyển đổi bài báo, Wikipedia thành Markdown sạch (Bắt buộc dùng thay cho Browser mặc định).
- **`wiki-crawl-4ai`**: Thu thập web động với khả năng chụp screenshot (R10 evidence), lưu trữ an toàn vào `00_Inbox/`.
- **`wiki-hd-convert`**: Trích xuất hình ảnh/biểu đồ độ phân giải cao từ PDF để giữ nguyên minh họa trực quan.
- **`defuddle`**: Lọc bỏ rác web (quảng cáo, menu bar) để lấy nội dung Markdown lõi, giúp tiết kiệm Token.

## 2. 🧹 Quản Trị Hệ Thống & Bảo Trì (Maintenance)
Nhóm kỹ năng giữ cho Database và Filesystem sạch sẽ, đồng bộ.
- **`wiki-rebuild`**: Đồng bộ Database với thư mục vật lý (Filesystem). Chạy khi có lỗi lệch Index hoặc rác dữ liệu.
- **`wiki-cleanup`**: Quét định kỳ để tìm Link gãy (Broken Links), file rác hoặc kiến thức đã quá hạn (STALE).
- **`wiki-md-auditor`**: Kiểm định chuẩn Markdown, sửa lỗi font chữ (Mojibake, ligatures) trước khi file được duyệt.
- **`wiki-learning-audit`**: Đẩy các Atom kiến thức (được học nhưng chưa thực hành) vào Review Queue để chờ con người kiểm chứng.

## 3. 🔍 Truy Vấn & Đánh Giá (Retrieval & Discovery)
Nhóm kỹ năng giúp moi móc kiến thức từ Second Brain.
- **`wiki-query`**: Tìm kiếm chính xác (Keyword / Graph traversal) để truy vết nguồn gốc và kết nối tri thức.
- **`wiki-semantic-search`**: Tìm kiếm theo ngữ nghĩa (Ý định), dùng khi không nhớ từ khóa chính xác.
- **`wiki-breakdown`**: Phân tích Atom để tìm ra "Lỗ hổng kiến thức" (Các thuật ngữ được nhắc đến nhưng chưa có Atom giải thích).
- **`wiki-status`**: Báo cáo sức khỏe toàn Wiki (số lượng Atom, tỷ lệ Verified, mật độ liên kết).

## 4. ⚖️ Xác Thực & Giải Quyết Xung Đột (Governance)
Nhóm kỹ năng duy trì tính toàn vẹn sự thật (The Iron Triangle).
- **`wiki-absorb`**: Hấp thụ Atom nháp vào hệ thống. Tự gộp nếu trùng lặp, hoặc chuyển sang Council nếu có mâu thuẫn.
- **`wiki-council`**: Hội đồng Agent phân xử các xung đột kiến thức (CONTRADICTS). Đưa ra quyết định file nào được giữ, file nào bị giáng cấp (DEPRECATED).

## 5. 📤 Tổng Hợp & Đầu Ra (Synthesis & Delivery)
Nhóm kỹ năng biến mảnh ghép (Atom) thành thành phẩm.
- **`wiki-to-deliverable`**: Ghép nhiều Atom nhỏ lại thành một bài báo cáo, tóm tắt hoặc Markdown note hoàn chỉnh.
- **`pedagogy`**: Chuyển kiến thức thô thành giáo án (Lesson Plan) hoặc Slide (PPTX) dựa trên mô hình sư phạm.

## 6. 🛠️ Obsidian Ecosystem (Tương tác Vault)
Nhóm kỹ năng làm việc trực tiếp với UI/UX của Obsidian.
- **`obsidian-cli`**: Điều khiển Obsidian từ dòng lệnh (đọc file, tìm kiếm, reload UI).
- **`obsidian-markdown`**: Viết chuẩn Markdown dành riêng cho Obsidian (Wikilinks `[[ ]]`, Callouts, Frontmatter).
- **`obsidian-bases`**: Quản lý các view cơ sở dữ liệu nội bộ Obsidian (Tables, Filters).
- **`json-canvas`**: Tạo sơ đồ tư duy dạng bảng vô cực (`.canvas`).

## 7. ⚙️ Agent Tooling (Phát triển nội bộ)
Nhóm kỹ năng để "Agent tự tiến hóa".
- **`skill-creator` / `write-skill`**: Tạo mới hoặc nâng cấp các Skill khác theo chuẩn.
- **`mcp-builder`**: Xây dựng máy chủ giao thức MCP kết nối API bên ngoài.
- **`karpathy-core`**: Bộ nguyên tắc cốt lõi (Surgical Min, Simplicity First) áp dụng cho mọi thao tác code.

## 8. 🧠 Phương Pháp Luận Lõi (Core Methods - CM)
Nhóm kỹ năng nền tảng chuẩn hóa quy trình kỹ thuật.
- **`cm-code-review`**: Quy trình review mã nguồn toàn vòng đời (Lite & Core).
- **`cm-context-budget`**: Quản lý và tối ưu hóa ngân sách Token (Context Window).
- **`cm-continuity`**: Khôi phục và duy trì ngữ cảnh qua các phiên làm việc tiếp theo (CONTINUITY.md).
- **`cm-core-edit-pro`**: Chỉnh sửa file code quy mô lớn an toàn, tích hợp Dry-run và Validation.
- **`cm-core-grep`**: Tìm kiếm cấp hệ thống tốc độ cao kèm Insight Analysis.
- **`cm-debugging`**: Deep Root Cause Analysis (RCA) phân tích và sửa lỗi đệ quy.
- **`cm-dockit`**: Tự động phân tích nguồn và tạo tài liệu SOP/Tech Docs dạng Markdown/VitePress.
- **`cm-gateway-pro`**: Tối ưu hóa và bảo trì kiến trúc SmartProxyHub Gateway.
- **`cm-git-flow`**: Xử lý, đồng bộ hóa phiên bản và resolve conflict Git.
- **`cm-instinct-learning`**: Hệ thống học liên tục lưu trữ các "Instinct" để tái sử dụng.
- **`cm-notebooklm`**: Lưu kiến thức sang Google NotebookLM để truy xuất đa nền tảng (podcast, flashcard).
- **`cm-quality-gate`**: Bước kiểm tra chất lượng bắt buộc trước khi kết thúc task hoặc xuất bản.
- **`cm-tdd`**: Quy trình phát triển hướng kiểm thử (Test-Driven Development) và sửa lỗi tự động.
- **`cm-terminal`**: Điều phối Terminal (PowerShell) linh hoạt với khả năng ghi log và tự phục hồi.

## 9. 📝 Lập Kế Hoạch & Thực Thi (Planning & Execution)
Nhóm kỹ năng quản trị vòng đời Task từ thiết kế đến báo cáo kết quả.
- **`using-superpowers`**: Đọc hướng dẫn chọn và gọi đúng các skill ở đầu phiên.
- **`brainstorming`**: Khám phá ý định, định hình giải pháp trước khi viết code.
- **`writing-plans`**: Thiết kế kế hoạch triển khai đa bước chi tiết cho các chức năng mới.
- **`executing-plans`**: Thực thi tuần tự kế hoạch đã lập và checkpoint sau mỗi bước.
- **`subagent-driven-development`**: Phân bổ tác vụ cho các Subagent chạy song song trong phiên hiện tại.
- **`systematic-debugging`**: Hệ thống hóa phương pháp phân tích và khoanh vùng lỗi.
- **`verification-before-completion`**: Ràng buộc xác minh (Evidence) thực tế qua script/test trước khi báo cáo hoàn thành.
