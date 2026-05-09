---
file_id: WIKI_V3_AI_FIRST_STANDARD
title: "Tiêu chuẩn Wiki V3.0: Master Schema & Metadata Philosophy"
type: synthesis
status: VERIFIED
tags: 
ai-first: true
confidence: 1.0
last_reconciled: 2026-05-08
created: 2026-05-08
last_updated: 2026-05-08
sources:
  - "[[SOURCE_GOV_WIKI_V3_MASTER_CONSTITUTION]]"
---

## For future Claude (AI Preamble)
> Tài liệu này là "Hiến chương Metadata" của Wiki 2.0. Nó quy hoạch lại toàn bộ cấu trúc Frontmatter để đảm bảo tính đồng nhất tuyệt đối giữa Template và Thực tế. Agent BẮT BUỘC phải tuân thủ Master Schema 3 lớp để xóa bỏ nợ kỹ thuật và phục vụ các script Audit định lượng.

# Master Schema & Metadata Philosophy V3.0

## 1. Phân tích Nợ kỹ thuật (Architectural Debt)
Hệ thống cũ đang gánh chịu sự "Phân kỳ Template" (Template Drift):
- **Sự hỗn loạn**: Mỗi loại Atom có bộ metadata khác nhau không theo quy luật, gây khó khăn cho việc lập chỉ mục (Indexing).
- **Sự bó hẹp**: `SOURCE` chỉ hỗ trợ sách, thiếu hụt các nguồn hiện đại (Video, Web, Podcast).
- **Sự dư thừa**: Trường `domain` gây chồng chéo với hệ thống `tags`.

---

## 2. Giải pháp: Master Schema 3 Lớp

Triết lý của chúng ta là: **Chassis chung - Functional riêng - Tối giản hóa**.

### Lớp 1: Khung gầm chung (Mandatory Chassis) - BẮT BUỘC 100%
Dùng cho mọi file để phục vụ Governance Engine (Audit/Risk/Rebuild):
- **Lớp 0 (Governance Integration)**: Các file phải pass qua `audit_raw_ingest.py` (Rule R21) để đảm bảo Metadata đúng chuẩn trước khi được đưa vào Index.
- **Lưu ý 0 (file_id Format)**: Bắt buộc theo định dạng `TYPE_[PREFIX]_[Name]` (vd: `SOURCE_AI_ThinkDataScience`, `CONCEPT_ARCH_System_Resilience`).
- **Prefixes Hệ thống**: `THINK` (Critical Thinking), `ARCH` (Infrastructure/System Design), `AIMET` (AI Orchestration), `ENTITY` (Tools/People).
- **Lưu ý 1**: `domain` chính thức bị loại bỏ, thay thế bằng hệ thống `tags`.
- **Lưu ý 2 (Title Convention)**: Title phải là tên định danh tự nhiên, không chứa ID. Riêng `SYNTHESIS` bắt buộc có tiền tố "TỔNG HỢP: " để phân biệt trong danh mục.
- **Lưu ý 3 (Original Language Preservation)**: BẮT BUỘC giữ nguyên ngôn ngữ gốc của tiêu đề (Title). CẤM dịch tên riêng (Tools, Orgs, People) và tên tác phẩm (Books, Videos) sang Tiếng Việt.
- **Lưu ý 4 (Language Protocol)**: Toàn bộ Keys và Giá trị hệ thống (System Values) BẮT BUỘC là **Tiếng Anh**. Chỉ có nội dung diễn giải (Preamble/Body) mới dùng Tiếng Việt. Tiêu đề (Title) được phép chứa Tiếng Việt **CHỈ KHI** đối tượng gốc vốn dĩ là Tiếng Việt.

### Lớp 2: Metadata Chức năng (Functional Extension) - Tùy biến theo Type
Chỉ thêm các trường này nếu nó phục vụ mục đích tính toán hoặc truy vết cụ thể:

| Loại Atom | Các trường mở rộng (Lớp 2) | Mục đích |
|---|---|---|
| **CONCEPT** | `relationships` (`is_a`, `part_of`, `prerequisite_of`) | Xây dựng Graph tri thức. |
| **ENTITY** | `entity_type`, `ecosystem`, `version`, `affiliation` | Quản lý công cụ & nhân vật. |
| **SOURCE** | `source_type` (book/video/web/pdf), `author`, `url` | Truy vết nguồn gốc (R3). |
| **SYNTHESIS**| `summary_of`, `target_audience` | Định hướng nội dung tổng hợp. |

### Lớp 3: Nội dung chuẩn (Standard Body)
Nội dung bên dưới Frontmatter được thiết kế dựa trên vai trò của Atom:

#### A. Nhóm Tri thức (CONCEPT & ENTITY)
*Mục tiêu: Chuyên sâu & Sư phạm*
1. **AI Preamble**: Tóm tắt ngữ cảnh cho Agent.
2. **Standard Headers**: Định nghĩa & Nguyên lý.
3. **Double Examples (R18)**: Ví dụ gốc & Ví dụ sư phạm (STEAM/EdTech).
4. **4F Reflection**: Fact, Feeling, Finding, Future.

#### B. Nhóm Nguồn (SOURCE)
*Mục tiêu: Truy vết & Bằng chứng*
1. **AI Preamble**: Tóm tắt xuất xứ.
2. **Executive Summary**: Nội dung cốt lõi của tài liệu.
3. **Key Topics**: Danh sách các Concept liên quan.
4. **Source Audit**: Đánh giá độ tin cậy & Tính cập nhật.

#### C. Nhóm Tổng hợp (SYNTHESIS & INSIGHT)
*Mục tiêu: Kết nối & Chiến lược*
1. **AI Preamble**: Tóm tắt mục đích tổng hợp.
2. **Narrative Content**: Luận điểm tổng hợp từ nhiều Atom.
3. **Strategic Insight**: Bài học rút ra cho hệ thống.
4. **Action Items**: Đề xuất hành động thực tế.

---

## 3. Bảng đối soát Master Schema (Quick Reference)

| Key | Chassis | Concept | Entity | Source | Synthesis |
|---|:---:|:---:|:---:|:---:|:---:|
| `ai-first` / `confidence` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `relationships` | ❌ | ✅ | ✅ | ❌ | ❌ |
| `entity_type` / `ecosystem`| ❌ | ❌ | ✅ | ❌ | ❌ |
| `source_type` / `author` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `summary_of` | ❌ | ❌ | ❌ | ❌ | ✅ |

---
*Phê duyệt bởi: @pm (Antigravity)*
