---
file_id: INSIGHT_20260508_Wiki_2_0_Governance_Architecture
title: "Đúc kết Kiến trúc Quản trị Wiki 2.0: Quy trình và Cấu trúc"
type: session_insight
category: Architecture
tags:
  - Governance
  - Wiki_2.0
  - Workflow
  - Refactoring
status: DRAFT
created: 2026-05-08
---
# 🧠 Đúc kết Kiến trúc Quản trị Wiki 2.0

Phiên làm việc ngày 08/05/2026 đã chuẩn hóa toàn bộ luồng vận hành của Second Brain, giải quyết các xung đột giữa tự động hóa và kiểm soát con người.

## 1. Phân định Bản chất (Folder) vs Trạng thái (Status)
Hệ thống sử dụng cơ chế quản lý song song để đảm bảo tính chặt chẽ:
- **Thư mục (Ontology)**: Trả lời câu hỏi "Nó là cái gì?". Cố định theo bản chất tri thức (`concepts`, `entities`, `sources`, `comparisons`, `synthesis`).
- **Trạng thái (Lifecycle)**: Trả lời câu hỏi "Nó đã chín chưa?". Fluid (biến đổi) theo tiến trình học tập (`DRAFT` ➔ `VERIFIED` ➔ `SYNTHESIZED`).
- **Trạng thái đặc biệt**: `STUB` (quá mỏng), `DEPRECATED` (lỗi thời), `STALE` (gãy link nguồn).

## 2. Hệ thống Thư mục & Chức năng (Folder Functions)

Hệ thống được tổ chức theo chức năng chuyên biệt để tối ưu hóa việc truy xuất và quản trị:

- **`sources/` (Nguồn)**: "Điểm neo" chứng minh. Đại diện cho 1 cuốn sách, bài báo, URL. Giúp kiến thức không bị bịa đặt.
- **`concepts/` (Khái niệm)**: "Viên gạch" cơ bản. Chứa tri thức nguyên tử (Ví dụ: Định nghĩa Machine Learning).
- **`entities/` (Thực thể)**: Thông tin về Con người, Tổ chức, Công cụ (Ví dụ: OpenAI, Sam Altman).
- **`comparisons/` (Đối chiếu)**: "Thuốc giải" mâu thuẫn. Chứa các bảng đánh giá, so sánh để hỗ trợ ra quyết định.
- **`synthesis/` (Tổng hợp)**: Sản phẩm cuối cùng. Các bài viết dài, giáo trình được lắp ghép từ nhiều Atom.
- **`review_queue/`**: "Bàn làm việc" (Inbox). Nơi giữ chân các Atom lỗi, mâu thuẫn hoặc chưa được User kiểm duyệt.
- **`decisions/`**: Nhật ký phân xử. Ghi lại các phán quyết của Hội đồng Wiki khi có xung đột tri thức.
- **`queries/`**: Thư viện kết quả. Lưu trữ các truy vấn phức tạp để tái sử dụng, giúp tiết kiệm Token.
- **`session_insights/`**: Nhật ký trưởng thành. Ghi lại các bài học về quy trình và quản trị sau mỗi phiên.

## 3. Ma trận Quyền hạn & Luân chuyển (Technical Matrix)

Bảng này định nghĩa các Skill/Agent nào có quyền "chạm" vào các thư mục tương ứng:

| Tầng vận hành | Nguồn đầu vào (From) | Skill / Agent | Đích đến (To) | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| **1. NẠP (Ingest)** | `raw_sources/` | `Converter` (Tool) | `00_Inbox/` | `SCRAPED` |
| **1. NẠP (Audit)** | `00_Inbox/` | `wiki-md-auditor` | `raw_ingest/` | `AUDITED` |
| **1. NẠP (Atomize)** | `raw_ingest/`, `raw_sources/` | `wiki-ingest` | `sources/`, `concepts/`, `entities/` | `DRAFT` |
| **2. XÁC THỰC** | `concepts/`, `entities/` | `wiki-absorb` | `review_queue/` | `DRAFT` |
| **3. PHÂN TÍCH** | Toàn bộ Wiki | `wiki-query`, `wiki-semantic-search` | `queries/` | `verified` |
| **3. PHÂN TÍCH** | `queries/` | `wiki-council` | `decisions/` | `verified` |
| **4. HUMAN (Duyệt)** | `review_queue/` + `decisions/` | **User (Approval)** | `concepts/`, `entities/` | `VERIFIED` |
| **4. HUMAN (Đúc kết)** | `concepts/`, `entities/`, `decisions/` | `/file-back` (User) | `comparisons/`, `synthesis/` | `DRAFT` |
| **4. HUMAN (Duyệt)** | `comparisons/`, `synthesis/` | **User (Approval)** | `comparisons/`, `synthesis/` | `SYNTHESIZED` |
| **5. BẢO TRÌ** | Filesystem (.md) | `wiki-rebuild` | `wiki_brain.db` (Sync) | `verified` |
| **5. BẢO TRÌ** | Toàn bộ Wiki | `wiki-cleanup` | `review_queue/` (Broken links) | `DRAFT` |
| **5. BẢO TRÌ** | Toàn bộ Wiki | `wiki-status` | `Console / Dashboard` | `verified` |
| **6. SIÊU TRI THỨC** | Chat Session | `/file-back` | `session_insights/` | `verified` |
| **6. SIÊU TRI THỨC** | `session_insights/` | **Promotion Workflow** | `GEMINI.md` / `SOP` | `FINAL` |

> [!IMPORTANT]
> Thư mục **`review_queue/`** là nơi bận rộn nhất, tất cả các Agent/Skill đều có quyền vào đây để thực hiện Audit, sửa lỗi Markdown, hoặc cung cấp thêm chứng cứ trước khi trình User duyệt.

## 4. Ví dụ minh họa: Vòng đời tri thức "Full-Stack"

Dưới đây là cách một mẩu kiến thức về **"Lịch sử Rule R8 (Human Supremacy)"** đi xuyên qua hệ thống:

| Bước | Hành động của Hệ thống | Skill / Workflow thực thi | Kết quả (File sinh ra) |
| :--- | :--- | :--- | :--- |
| **1. Cào tin** | Bạn đưa link bài blog về quản trị AI. | `wiki-web-scrape` | `00_Inbox/RAW_R8_Blog.md` |
| **2. Ingest** | Hệ thống bóc tách bài blog thành các Atom. | `wiki-ingest` | `concepts/CONCEPT_Rule_R8.md` (DRAFT) |
| **3. Xung đột** | Nguồn mới nói "R8 từ 2025" mâu thuẫn với Nguồn cũ "2024". | `wiki-absorb` | **Cả 2 file (Cũ & Mới)** ➔ `review_queue/` (Cách ly để phân xử) |
| **4. Truy vấn** | Bạn tìm xem ai đã viết Rule này. | `wiki-query` | `queries/QUERY_R8_Author.md` |
| **5. Phân xử** | Council Agent họp để xác minh tác giả. | `wiki-council` | `decisions/DECISION_R8_Origin.md` |
| **6. Đúc kết** | Bạn tổng hợp quy tắc vào SOP. | `/file-back` | `synthesis/WIKI_GOVERNANCE_SOP.md` |
| **7. Về đích** | Bạn lệnh: "Hợp nhất mốc 2024". | `User` | **File Merge** ➔ `concepts/` (SYNTHESIZED)<br>(Giữ lại kiến thức đúng từ cả 2 nguồn) |



### Giải thích sự phối hợp:
*   **`wiki-ingest`**: Là người "quản gia" bóc tem hàng mới.
*   **`wiki-absorb`**: Là "cảnh sát giao thông" điều hướng file vào khu cách ly nếu có đụng xe tri thức.
*   **`wiki-query` & `wiki-council`**: Là "thám tử" và "quan tòa ảo" cung cấp bằng chứng cho bạn.
*   **`/file-back`**: Là "thư ký" ghi lại những đúc kết quý giá sau khi bạn đã hiểu vấn đề.
*   **`User`**: Là "vua", người duy nhất có quyền đóng dấu `SYNTHESIZED` để đưa tri thức vào sử dụng chính thức.

## 5. Tư duy về Meta-knowledge (Siêu tri thức)

Insight không chỉ là tóm tắt chat, mà là "Hệ điều hành" của bộ não:
- **Insight kỹ thuật**: Lưu tại `session_insights/` để tra cứu về cấu trúc/vận hành.
- **Insight quy trình (SOP)**: Nếu insight tạo ra một quy trình lặp lại có giá trị, cần được **Thăng cấp (Promotion)** thành một bản `SOP` (Standard Operating Procedure) hoặc cập nhật vào `GEMINI.md`.
- **Mục tiêu**: Biến "kinh nghiệm nhất thời" thành "quy trình vĩnh viễn".

## 6. Cải cách Workflow `/file-back`

Chuyển đổi từ mô hình Tự động sang mô hình **Thăng cấp chủ động (Explicit Promotion)**:
- **Trigger**: Chỉ kích hoạt khi User ra lệnh cụ thể hoặc khi thực hiện Promotion từ kết quả phân tích có giá trị.
- **An toàn**: Mọi file sinh ra từ chat phải ở trạng thái `DRAFT` và nằm trong `review_queue/` để chờ duyệt.
- **Ghi log**: Bắt buộc ghi nhận vào `3-resources/wiki/logs/log_YYYY_MM_DD.md` theo Luật R14.

---
*Bản đúc kết kiến trúc Quản trị Wiki 2.0 (Phiên bản v2.1).*

- **Pre-flight Check**: Agent phải kiểm tra trùng lặp và cảnh báo độ dày nội dung (R11) trước khi ghi file.

## 7. Quy trình Phê duyệt & Hợp nhất (Approval & Merge)
- **Xung đột bộ phận**: Nếu một Atom chỉ sai một phần nhỏ, User sẽ ra lệnh **Merge/Refactor**.
- **Vị trí sau Merge (Placement Rules)**:
    - **Cùng thư mục**: Hợp nhất và đặt tại thư mục gốc tương ứng (VD: `concepts/`).
    - **Khác thư mục**: Agent phải phân loại lại theo bản chất (Ontology). Tri thức định nghĩa ➔ `concepts/`, Hồ sơ thực thể ➔ `entities/`. Thực hiện `move_file` về đúng "nhà" của nó.
    - **Bảo tồn liên kết**: File mới phải bao hàm Metadata `aliases` hoặc cập nhật tất cả Backlinks để không làm gãy Graph.



## 8. Tái cấu trúc Hub Template (Shared Resources)
- Di dời toàn bộ `_TEMPLATE.md` và `WIKI_AGENT_GUIDE.md` ra khỏi skill `wiki-ingest` để làm tài sản chung tại `.agent/skills/references/`.
- Bổ sung `SYNTHESIS_TEMPLATE.md` và `COMPARISON_TEMPLATE.md` để chuẩn hóa các bài viết tổng hợp.

## 9. Chiến lược Chống "Bãi rác tri thức" (Anti-Spam Strategy)
- **Vấn đề**: Các Node giả (STUB rỗng) như `CONCEPT_index` làm loãng Graph.
- **Giải pháp @pm**: Nâng cấp Skill **`wiki-breakdown`** thay vì chỉ dùng Auditor.
- **Cơ chế Gác cổng**: Áp dụng "Noun-Test" (Kiểm tra thuật ngữ) và "Blocklist" cho từ khóa phổ thông trước khi cho phép tạo Stub.

---
**Kết luận:** Hệ thống đã chuyển đổi từ một công cụ lưu trữ thụ động sang một cỗ máy tri thức có khả năng tự sàng lọc (Audit), tự phát hiện mâu thuẫn (Conflict Detection) và thăng cấp kiến thức (Knowledge Promotion) dưới sự kiểm soát tuyệt đối của con người.
