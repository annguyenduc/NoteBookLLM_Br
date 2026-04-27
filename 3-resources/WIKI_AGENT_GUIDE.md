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
1.  **📌 Định nghĩa cốt lõi**: Ngắn gọn, súc tích.
2.  **🔍 Chi tiết kỹ thuật**: Thông số, bảng chân (Pinout).
3.  **💡 Ví dụ thực tế**: Ứng dụng trong KDI/Arduino.
4.  **🔗 Liên kết tư duy**: Ít nhất 2 liên kết `[[Wiki_Link]]`.
5.  **4F — Phản tư sư phạm**: Facts, Feelings, Findings, Futures.
6.  **📖 Nguồn**: Trích dẫn chính xác file trong `3-resources/raw/`.

## 3. Quy tắc vàng (Rule Checklist)
- [ ] **Rule 7 (Flatness)**: Lưu trực tiếp vào `3-resources/wiki/`, không tạo thư mục con. Tên file: `WIKI_[NHÓM]_[TÊN].md`.
- [ ] **Rule 14 (Source Integrity)**: Phải mở file raw trong `3-resources/raw/` trước khi trích dẫn.
- [ ] **Rule 16 (Stats)**: Nếu là file tổng hợp (Distilled), phải có bảng thống kê mining.
- [ ] **Encoding**: Luôn sử dụng UTF-8 (không BOM).

---
*Lưu ý: Template mẫu nằm tại `d:/NoteBookLLM_Br/archive/WIKI_TEMPLATE.md`.*
