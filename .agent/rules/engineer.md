# engineer.md — Rules for @engineer

> Áp dụng khi: @engineer được gọi để viết code, tạo Atom, thực thi task kỹ thuật.
> Luôn đọc CORE.md trước. Tra cứu thêm: [[GEMINI.md]]

---

## R4 — STRUCTURE & ENCODING
**CẤM** tạo file code (`.py`, `.js`, `.json`) tại thư mục gốc.
- Code production → `scripts/`
- Code nháp/test → `scratch/`
- Mọi thao tác ghi/sửa file: dùng Python UTF-8. **CẤM PowerShell** cho file operations.
- Khi tạo file mới: tạo file mồi (empty) trước, sau đó mới điền nội dung (để User thấy Diff).

## R9 — SURGICAL MINIMALISM
Chỉ thay đổi **tối thiểu** những gì cần thiết.
**CẤM** tự ý "làm đẹp" code, format lại indentation của cả file, hay refactor ngoài phạm vi task.

## R12 — EXAMPLE ADHERENCE
**BẮT BUỘC** đối soát với `EXAMPLES.md` và `.agent/skills/obsidian-markdown` trước khi tạo Atom.
Dùng `[[Wikilinks]]` cho liên kết nội bộ. Không tự sáng tạo format mới nếu đã có mẫu.

## R18 — DOUBLE EXAMPLES
Mỗi Atom Concept **BẮT BUỘC** có section `## Ví dụ đối chiếu (R18: Double Examples)` với:
1. **Ví dụ từ nguồn (Original)**: trích dẫn trực tiếp từ tài liệu gốc.
2. **Ứng dụng sư phạm (Pedagogical)**: áp dụng vào bối cảnh K-12 hoặc dự án thực tế.

## R19 — SANDBOX PROTOCOL
Code AI sinh ra **BẮT BUỘC** chạy trong Localsandbox (WASM) trước.
Chỉ sau khi chạy an toàn trong Sandbox mới được thực thi trên file thật.

## R8-ENFORCEMENT — PRE-WRITE GATE
Trước khi ghi BẤT KỲ file Atom nào vào wiki/,
BẮT BUỘC chạy synthesis_guard.py check trước:

```bash
python scripts/maintenance/synthesis_guard.py check \
  "<file_path>" --content "<proposed_content>"
```

Nếu output KHÔNG phải "[SYNTHESIS GUARD] OK" → DỪNG NGAY.
Không được ghi file. Báo cáo vi phạm cho User.
Không có exception. Không có workaround.

---
*engineer.md — 7 rules cho @engineer. Nguồn: [[GEMINI.md#R4]], [[GEMINI.md#R8]], [[GEMINI.md#R9]], [[GEMINI.md#R12]], [[GEMINI.md#R18]], [[GEMINI.md#R19]], [[GEMINI.md#R26]]*
