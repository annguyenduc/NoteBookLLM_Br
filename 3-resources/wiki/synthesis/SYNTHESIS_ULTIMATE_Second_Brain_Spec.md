---
file_id: SYNTHESIS_ULTIMATE_Second_Brain_Spec
title: "SYNTHESIS: The Ultimate Second Brain Specification (V3.0)"
type: synthesis
status: VERIFIED
tags: 
ai-first: true
confidence: 1.0
last_reconciled: 2026-05-08
created: 2026-05-02
last_updated: 2026-05-08
---

## For future Claude (AI Preamble)
> [Bản đặc tả tối thượng quy định mọi khía cạnh vận hành của Second Brain V3.0. Tập trung vào kiến trúc AI-First, hệ thống 7 lệnh vận hành, và quy trình hòa giải tri thức chủ động. Đây là Source of Truth cho việc thiết lập Agent và xây dựng Wiki Atoms.]

# Đại bản đặc tả Second Brain (The Ultimate Specification)

Tài liệu này là sự hợp nhất của 3 thế hệ phương pháp luận LLM Wiki, tạo ra một hệ thống tri thức không chỉ để lưu trữ mà còn để **tự học và tự tiến hóa**.

## 1. Triết lý thiết kế: AI-First Vault
Thay vì viết note cho "bản thân trong tương lai" đọc trong 30 phút, chúng ta viết note để **"Claude trong tương lai" có thể đọc và hiểu trong 10 giây**.

- **Nguyên tắc Rewrite (Thay vì Append)**: Khi có thông tin mới về một thực thể đã tồn tại, hệ thống phải **viết lại (Rewrite)** trang đó để phản ánh trạng thái chính xác nhất hiện tại. Các thông tin cũ được đẩy xuống phần "Archive/History" bên dưới.
- **Tính đảo ngược (Reversibility)**: Mọi thay đổi tự động phải được ghi vào `daily_diff.md` và có thời gian chờ 24h trước khi trở thành vĩnh viễn.

## 2. Cấu trúc Schema chuẩn (The High-Fidelity Schema)

Hệ thống sử dụng một Schema chặt chẽ để biến các tệp Markdown thành các "Database-like Objects" mà AI có thể truy vấn chính xác.

### A. Metadata (Frontmatter) nâng cao
Mọi tệp trong `wiki/` bắt buộc phải có các trường sau:
```yaml
file_id: CONCEPT_META_AI_FIRST_TEMPLATE         # Ví dụ: CONCEPT_META_AI_FIRST
title: [Tên_trang_đầy_đủ]
type: "concept | entity | source | synthesis | query"
ai-first: true                   # Đánh dấu trang đã được tối ưu cho AI
confidence: "low | mid | high"   # Độ tin cậy của thông tin
status: "DRAFT | VERIFIED | DEPRECATED | superseded
source"
relationships:                   # Danh sách liên kết có định dạng (Typed Links)
  - type: "is_a | relates_to | governs | supersedes | fixed_by"
    target: "[[index]]"
last_reconciled: "YYYY-MM-DD"    # Ngày cuối cùng thực hiện hòa giải tri thức
```

### B. Cấu trúc nội dung (Body Structure)
Một trang Wiki lý tưởng phải tuân thủ thứ tự sau:
1.  **## For future Claude**: (Preamble) Tóm tắt 3-5 câu về trang này để Agent nắm bắt nhanh mà không cần đọc hết file.
2.  **## Key Claims / Summary**: Các khẳng định cốt lõi hoặc tóm tắt nội dung.
3.  **## Detailed Analysis**: Nội dung chi tiết, sử dụng **Recency Markers** (ví dụ: `[Fact_A] (Updated: 2026-04)`).
4.  **## Relationships**: Liệt kê trực quan các liên kết quan trọng.
5.  **## Source Tracing**: Danh sách các trích dẫn nguồn thực tế (R3).
6.  **## History / Revisions**: Nhật ký thay đổi (Archive các thông tin cũ đã bị Rewrite).

### C. Danh mục các loại liên kết (Relationship Types)
Để AI có thể thực hiện **Graph Traversal**, chúng ta định nghĩa các quan hệ sau:
- `is_a`: Phân loại (Ví dụ: Python *is_a* Programming Language).
- `part_of`: Thành phần (Ví dụ: Engine *part_of* Car).
- `governs`: Quy định/Quản lý (Ví dụ: Rule_A *governs* Ingest_Process).
- `supersedes`: Thay thế (Thông tin mới thay thế thông tin cũ).
- `contradicts`: Mâu thuẫn (Dùng để Flag các điểm cần hòa giải).
- `caused_by / fixed_by`: Nguyên nhân và Giải pháp (Dùng cho Debugging/History).

### D. Cấu trúc thư mục (Taxonomy)
- `concepts/`: Các khái niệm trừu tượng, phương pháp luận.
- `entities/`: Người, Công cụ, Tổ chức, Hệ thống cụ thể.
- `sources/`: Tóm tắt các nguồn dữ liệu từ `raw/`.
- `synthesis/`: Các trang tổng hợp tri thức đa nguồn, bài kiểm tra.
- `queries/`: Kết quả của các phiên nghiên cứu chuyên sâu (QUERY_).
- `logs/`: Nhật ký hệ thống và `daily_diff.md`.


## 3. Hệ thống 7 Lệnh & 5 Tiện ích mở rộng (Skills & Extensions)

### A. 7 Lệnh vận hành (The Wiki-Gen Protocol)
1.  **`/wiki ingest`**: Nạp dữ liệu thô, tự động phân loại Taxonomy.
2.  **`/wiki absorb`**: Vòng lặp hấp thụ tri thức, thực hiện Rewrite và tích hợp mạch truyện.
3.  **`/wiki query`**: Truy vấn đồ thị, tổng hợp câu trả lời đa nguồn.
4.  **`/wiki cleanup`**: Audit chất lượng (Steve Jobs Test), chuẩn hóa Tone Wikipedia.
5.  **`/wiki breakdown`**: Đào bới lỗ hổng tri thức (Concrete Noun Test).
6.  **`/wiki status`**: Báo cáo sức khỏe, mật độ liên kết và độ tin cậy.
7.  **`/wiki rebuild`**: Đồng bộ hóa Index, Backlinks và Đồ thị tri thức.

### B. 5 Tiện ích mở rộng nâng cao (The V3 Extensions)
1.  **Write-back (Tự động cập nhật)**: Hệ thống tự động cập nhật lại các trang cũ khi phát hiện thông tin mới trong quá trình Chat.
2.  **Automatic Reconciliation (Tự động hòa giải)**: Tự động giải quyết mâu thuẫn tri thức dựa trên **Recency** (độ mới) và **Authority** (độ uy tín của nguồn).
3.  **Unsolicited Synthesis (Tổng hợp chủ động)**: AI tự phát hiện các Pattern ẩn (ví dụ: "Bạn đã nhắc đến X 7 lần trong 5 trang khác nhau") và tự tạo trang Synthesis mới.
4.  **Scheduled Agents (Agent lịch trình)**: Chạy ngầm (Nightly/Weekly) để dọn dẹp, bảo trì và Audit hệ thống.
5.  **AI-First Preamble**: Mọi trang đều bắt đầu bằng đoạn `## For future Claude` tóm tắt ngữ cảnh cho Agent.

## 4. Phân cấp bộ nhớ (Consolidation Tiers)
- **Working Memory**: Các quan sát gần đây (00_Inbox).
- **Episodic Memory**: Tóm tắt các phiên làm việc (Queries/Logs).
- **Semantic Memory**: Các sự thật phi bối cảnh (Concepts/Entities).
- **Procedural Memory**: Các quy trình và Pattern đã được kiểm chứng (Skills/Workflows).

## 5. Phản tư sư phạm (4F)
- **Facts**: Chúng ta đã đi từ một kho lưu trữ tĩnh (V1) sang một thực thể có khả năng tự hòa giải và tự tổng hợp (V3).
- **Feelings**: Cảm thấy choáng ngợp trước tiềm năng của "AI-First Vault" — nơi Agent thực sự là một người đồng nghiệp (Collaborator) chứ không chỉ là công cụ.
- **Findings**: Điểm mấu chốt là **Tính đảo ngược**. Nếu không có `daily_diff`, người dùng sẽ sợ hãi khi để AI tự ý Rewrite dữ liệu.
- **Futures**: Ưu tiên xây dựng `daily_diff.py` và `reconciler.py` để hiện thực hóa V3 Extensions.

## 6. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Lệnh & Taxonomy.
- **Nguồn**: SOURCE_META_KARPATHY_LLM_WIKI — AI-First Principle & Extensions.
- **Nguồn**: [[SOURCE_META_LLM_WIKI_V2]] — Consolidation Tiers.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
