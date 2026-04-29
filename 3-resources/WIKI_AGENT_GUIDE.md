---
file_id: "WIKI_AGENT_GUIDE"
title: "Hướng dẫn tạo Wiki Atom cho Agents"
category: "Meta Guide"
prefix: "WIKI"
tags: ["Meta", "Guideline", "Wiki", "Agents"]
status: "verified"
created: "2026-04-25"
---

# 📖 Hướng dẫn tạo Wiki Atom cho Agents

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
1.  **📌 Định nghĩa cốt lõi**: Ngắn gọn, súc tích, bám sát thuật ngữ trong sách.
2.  **🔍 Chi tiết kỹ thuật/Phương pháp**: Cấu trúc các bước phải khớp chính xác với tài liệu gốc.
3.  **💡 Ví dụ đối chiếu (Mandatory)**:
    -   **Ví dụ từ sách (Original)**: Trích dẫn hoặc tóm tắt sát thực tế trong sách.
    -   **Ứng dụng sư phạm (Pedagogical Application)**: Chuyển đổi sang tình huống dạy học/STEAM để giáo viên dễ áp dụng.
4.  **🔗 Liên kết tư duy**: Ít nhất 2 liên kết `[[Wiki_Link]]`.
5.  **4F — Phản tư sư phạm**: Facts, Feelings, Findings, Futures.
6.  **📖 Nguồn**: Trích dẫn chính xác file và trang/section trong `3-resources/raw/`.

## 3. Chiến lược Ingest (10-15 trang/nguồn)
Mỗi khi nạp (Ingest) một nguồn tài liệu mới, Agent phải đảm bảo tạo ra/cập nhật khoảng 10-15 trang Wiki theo cấu trúc:

1.  **Trang Tóm tắt (Summary - 1 trang)**: `WIKI_SOURCE_[Tên_Sách]`. Tóm tắt Key Takeaways, cấu trúc sách và ghi log nạp.
2.  **Trang Chỉ mục (Index - 1-2 trang)**: Cập nhật `WIKI_INDEX.md` và các trang Master Topic (ví dụ: `THINK_Analytical_Thinking.md`).
3.  **Trang Thực thể (Entity - 2-3 trang)**: Các trang về công cụ hoặc hệ thống lớn (ví dụ: `WIKI_ENTITY_SQL`, `WIKI_ENTITY_Python`).
4.  **Trang Khái niệm (Concept - 5-8 trang)**: Các trang Atomic về thuật ngữ, kỹ thuật cụ thể (ví dụ: `WIKI_THINK_Entropy`).

## 4. Quy tắc vàng (Rule Checklist)
- [ ] **Rule 7 (Flatness)**: Lưu trực tiếp vào `3-resources/wiki/`.
- [ ] **Rule 17 (Double Examples)**: Luôn có ví dụ Gốc và ví dụ Sư phạm.
- [ ] **Rule 18 (Structural Fidelity)**: Giữ nguyên cấu trúc logic của tác giả.
- [ ] **Mật độ tri thức**: Đảm bảo chạm đến 10-15 trang liên quan cho mỗi nguồn.
- [ ] **Rule 14 (Source Integrity)**: Phải mở file raw và trích dẫn trung thực. **CẤM phóng tác tùy ý**.
- [ ] **Rule 17 (Double Examples)**: Xem chi tiết tại [[AGENTS.md]]. Bắt buộc có ví dụ đối chiếu.
- [ ] **Rule 18 (Structural Fidelity)**: Xem chi tiết tại [[AGENTS.md]]. Bám sát cấu trúc của tác giả.
- [ ] **Encoding**: UTF-8 (không BOM).

---
*Lưu ý: Template mẫu nằm tại `d:/NoteBookLLM_Br/archive/WIKI_TEMPLATE.md`.*
