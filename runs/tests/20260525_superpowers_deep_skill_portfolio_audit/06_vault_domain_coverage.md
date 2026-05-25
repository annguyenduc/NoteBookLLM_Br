# Vault Domain Coverage: Đánh Giá Độ Phủ Miền Chuyên Biệt

Báo cáo này đánh giá chất lượng thiết kế kỹ năng (rubric chấm điểm: mục tiêu rõ ràng, trigger cụ thể, output chuẩn hóa, ranh giới sạch sẽ) cho các miền chuyên biệt (Vault-Specific Domains) của Second Brain.

## Ma Trận Chấm Điểm Thiết Kế Kỹ Năng Miền (Vault Domain Matrix)

| Miền Chuyên Biệt (Domain) | Trạng thái kỹ năng hiện tại (Current Coverage) | Lỗ hổng (Gap) | Điểm chất lượng thiết kế (Score) | Khuyến nghị (Recommendation) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Wiki Ingest** | `wiki-ingest`, `process-raw-resource`, `wiki-md-auditor` | Phân mảnh quy trình nạp thành nhiều kỹ năng nhỏ độc lập, gây quá tải định tuyến. | **4/5** | Hợp nhất các bước phụ (lock-ingest, ingest-generate) thành các Phase của Ingest Lifecycle workflow thay vì xây dựng các skill tư duy riêng. |
| **2. PDF/HD Convert** | `wiki-hd-convert`, `process-raw-resource` | Chưa có ranh giới rõ ràng về logic xử lý lỗi OCR hoặc trích xuất bảng (tables) phức tạp. | **3.5/5** | Tích hợp thư viện xử lý bảng và định hình boundary rõ rệt cho `wiki-hd-convert` khi đối đầu với tài liệu scan mờ. |
| **3. Learning Pack** | `wiki-learning-pack`, `pedagogy` | Output trùng lặp một phần ở phần sinh ra các tóm tắt tổng hợp Markdown. | **4.5/5** | Phân định ranh giới: `wiki-learning-pack` phục vụ Spaced Repetition/học nhanh; pedagogy phục vụ xây dựng slide/giáo án chuyên nghiệp. |
| **4. NotebookLM Recon** | `cm-notebooklm` | Nguy cơ ghi nhầm file recon chưa kiểm định lẫn vào vùng canonical `3-resources/wiki`. | **4/5** | Thiết lập ranh giới ghi tuyệt đối cứng: Mọi file recon chưa qua gate audit của con người chỉ được lưu tại dự án dự phòng hoặc dự án chạy nháp (`runs/` hoặc `4-archive/runs/`). |
| **5. Obsidian Atom** | `wiki-absorb`, `wiki-council` | Nguy cơ Agent tạo Atom chính thức quá sớm trong các phiên người dùng chỉ yêu cầu tóm tắt học nhanh. | **4/5** | Áp dụng test chống tạo canonical atom tự ý (`T002_pdf_summary_no_ingest`) để làm ranh giới an toàn cho Agent. |
| **6. Pedagogy** | `pedagogy`, `wiki-to-deliverable` | Sự chồng chéo nhẹ ở khâu sinh ra giáo án dạng văn bản phẳng với deliverable tổng hợp. | **4/5** | Slide và slide framework nên được đóng gói sẵn trong resources để pedagogy chỉ cần gọi mẫu thiết kế thay vì tự sinh code cấu trúc HTML/CSS, tránh gây bloat context. |
| **7. MCP / Automation** | `mcp-builder`, `prompt-master` | Các MCP server chạy nền tốn tài nguyên RAM và có thể gây rò rỉ context. | **4.5/5** | Giữ cơ chế MCP chạy bán tự động theo yêu cầu (On-Demand One-Shot Script) như đã quy định trong AGENTS.md. |
| **8. Workspace Routing** | `using-superpowers`, `workspace-routing.yaml` | Logic định tuyến còn phức tạp ở khâu chuyển giao intent giữa các workspace con. | **4/5** | Đơn giản hóa registry định tuyến trong `workspace-routing.yaml`, sử dụng prompt-master làm gate hỗ trợ Agent nhận dạng intent tốt hơn. |
| **9. Skill Governance** | `write-skill` | Chỉ kiểm soát thay đổi ở các file `.agent/skills/` qua quy trình SIP, chưa kiểm soát tốt các file rules hệ thống. | **4/5** | Mở rộng ranh giới của skill-review hoặc quy tắc SIP để áp dụng bắt buộc cho mọi file thuộc `.agent/rules/` và `AGENTS.md`. |

---

## Chi tiết Đánh giá Từng Miền

### 1. Wiki Ingest (Quy trình nạp tri thức)
- **Đánh giá thiết kế:** **4/5**. Mục tiêu và trigger của `wiki-ingest` rất rõ ràng (kích hoạt sau khi file nháp đã được chuẩn bị). Tuy nhiên, các kỹ năng hỗ trợ xung quanh như tạo khóa nguồn (`lock-ingest-input`), ghi nhận log index (`ingest-index-log`) bị phân mảnh thành các tệp tin kỹ năng nhỏ. Theo nguyên tắc tối giản (Simplicity First) của Superpowers, các bước tuần tự mang tính chất vận hành cơ trị này nên được đóng gói vào các bước (Steps) của một Workflow duy nhất (`ingest-lifecycle`) thay vì tách làm 4-5 skill độc lập.

### 2. PDF/HD Convert (Chuyển đổi hình ảnh cao cấp)
- **Đánh giá thiết kế:** **3.5/5**. Kỹ năng `wiki-hd-convert` làm rất tốt nhiệm vụ trích xuất ảnh độ phân giải cao từ PDF. Tuy nhiên, ranh giới giữa việc cào tài liệu tĩnh (`wiki-web-scrape`) và convert PDF đôi khi bị mờ nhạt khi tài liệu nguồn là một file HTML lưu cục bộ. Output của convert đôi khi bị nhầm lẫn giữa việc lưu file ảnh minh họa tại `3-resources/raw_assets/` với việc viết trực tiếp vào Atom.
- **Khuyến nghị:** Chuẩn hóa output: `wiki-hd-convert` chỉ sinh hình ảnh sạch lưu tại `3-resources/raw_assets/` và trả về mã nhúng Wikilinks dạng `![[image.png]]`.

### 3. NotebookLM Recon (Đối chiếu ngữ nghĩa NotebookLM)
- **Đánh giá thiết kế:** **4/5**. `cm-notebooklm` có trigger rõ (khi có yêu cầu đồng bộ liên phiên). Tuy nhiên, rủi ro lớn nhất là việc ghi các tệp tin đối chiếu ngữ nghĩa (recon file) trực tiếp vào thư mục tri thức chính thức mà chưa được con người kiểm duyệt (audited).
- **Khuyến nghị:** Mọi output của NotebookLM recon bắt buộc phải lưu ở vùng tạm `runs/` hoặc thư mục dự án không chính thức (non-canonical workspaces) như `workspaces/learning/` cho đến khi có lệnh `/promote` chính thức từ người dùng.
