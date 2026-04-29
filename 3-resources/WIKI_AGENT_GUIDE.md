---
file_id: "WIKI_AGENT_GUIDE"
title: "Hướng dẫn tạo Wiki Atom cho Agents"
category: "Meta Guide"
prefix: "WIKI"
tags: ["Meta", "Guideline", "Wiki", "Agents"]
status: "verified"
created: "2026-04-25"
---

#  Hướng dẫn tạo Wiki Atom cho Agents

Tài liệu này thay thế `WIKI_TEMPLATE.md` để hướng dẫn các AI Agents cách tạo trang Wiki mới đảm bảo tính nhất quán (Atomic Migration Phase).

## 1. Cấu trúc YAML Frontmatter (Bắt buộc)
Mọi file Wiki phải có phần đầu như sau:
```yaml
---
file_id: "WIKI_[Tên_Viết_Hoa_Rắn]"
title: "[Tiêu đề Tiếng Việt]"
category: "Wiki Page"
prefix: "WIKI"
tags: ["IoT", "Arduino", "Module_X"]
source: "[[Tên_File_Raw_Gốc]]"
status: "draft"
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
---
```

## 2. Các mục nội dung chính
1.  ** Định nghĩa cốt lõi**: Ngắn gọn, súc tích, bám sát thuật ngữ trong sách.
2.  ** Chi tiết kỹ thuật/Phương pháp**: Cấu trúc các bước phải khớp chính xác với tài liệu gốc.
3.  ** Ví dụ đối chiếu (Mandatory)**:
    -   **Ví dụ từ sách (Original)**: Trích dẫn hoặc tóm tắt sát thực tế trong sách.
    -   **Ứng dụng sư phạm (Pedagogical Application)**: Chuyển đổi sang tình huống dạy học/STEAM để giáo viên dễ áp dụng.
4.  ** Liên kết tư duy**: Ít nhất 2 liên kết `[[Wiki_Link]]`.
5.  **4F — Phản tư sư phạm**: Facts, Feelings, Findings, Futures.
6.  ** Nguồn**: Trích dẫn chính xác file và trang/section trong `3-resources/raw/`.

## 3. Quy trình Ingest 2 Bước (Two-Step CoT Ingest) - BẮT BUỘC
Mọi nguồn tài liệu mới phải đi qua 2 bước tư duy trước khi ghi file:

### Bước 1: Phân tích cấu trúc (Analysis)
Agent phải đọc nguồn và trích xuất:
- **Key Entities & Concepts**: Các thực thể và khái niệm cốt lõi.
- **Connections**: Mối liên hệ với kiến thức hiện có trong Wiki (tránh trùng lặp).
- **Contradictions**: Các điểm mâu thuẫn hoặc góc nhìn mới so với những gì đã biết.
- **Recommendations**: Đề xuất cấu trúc các trang Wiki mới sẽ tạo.

### Bước 2: Khởi tạo & Cập nhật (Generation)
Dựa trên phân tích ở Bước 1, thực hiện:
- **Tạo SOURCE_Page**: Sao chép 100% cấu trúc từ `3-resources/SOURCE_TEMPLATE.md`. Cập nhật Frontmatter đầy đủ.
- **Tạo/Cập nhật các trang Entity và Concept**: Theo các mục định nghĩa, ví dụ (Rule 17), 4F và Nguồn.
- **Đồng bộ hóa**: Cập nhật `index.md`, `log.md`, `overview.md`.

## 4. Chiến lược Ingest (10-15 trang/nguồn)
Mỗi khi nạp (Ingest) một nguồn tài liệu mới, Agent phải đảm bảo tạo ra/cập nhật khoảng 10-15 trang Wiki theo cấu trúc phân tầng tri thức:

1.  **Trang Tóm tắt (Source Page - 1 trang)**: `SOURCE_[Tên_Nguồn]`. Chứa phân tích Bước 1 và tổng quan Bước 2 theo `SOURCE_TEMPLATE.md`.
2.  **Trang Thực thể (Entity - 2-3 trang)**: Các trang về công cụ hoặc hệ sinh thái lớn (ví dụ: `ENTITY_Tableau`, `ENTITY_Python`).
3.  **Trang Khái niệm (Concept - 5-8 trang)**: Các trang Atomic về thuật ngữ, kỹ thuật cụ thể (ví dụ: `CONCEPT_STAT_ANOVA`).
4.  **Trang Tổng hợp/Chỉ mục (Index/Synthesis - 1-2 trang)**: Cập nhật `index.md` và các trang Master Topic liên quan.

## 5. Quy tắc vàng (Rule Checklist)
- [ ] **Rule 7 (Flatness)**: Lưu trực tiếp vào `3-resources/wiki/`.
- [ ] **Mật độ tri thức**: Đảm bảo chạm đến 10-15 trang liên quan cho mỗi nguồn.
- [ ] **Rule 14 (Source Integrity)**: Phải mở file raw và trích dẫn trung thực. **CẤM phóng tác tùy ý**.
- [ ] **Rule 17 (Double Examples)**: Xem chi tiết tại [[AGENTS.md]]. Bắt buộc có 1 ví dụ Gốc từ sách và 1 ví dụ Ứng dụng sư phạm.
- [ ] **Rule 18 (Structural Fidelity)**: Xem chi tiết tại [[AGENTS.md]]. Bám sát cấu trúc logic của tác giả.
- [ ] **Encoding**: UTF-8 (không BOM).

---
*Lưu ý: Template mẫu nằm tại `d:/NoteBookLLM_Br/archive/WIKI_TEMPLATE.md`.*
