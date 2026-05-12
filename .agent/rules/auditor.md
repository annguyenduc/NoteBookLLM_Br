# auditor.md — Rules for @auditor

> Áp dụng khi: @auditor được gọi cho /cleanup, kiểm định nguồn, reverse tracing, lint.
> Luôn đọc CORE.md trước. Tra cứu thêm: [[GEMINI.md]]

---

## R3 — SOURCE TRACING
**CẤM tạo nguồn ảo.**
Mọi thông tin trong Atom phải có Link dẫn về Source Node trong `3-resources/wiki/sources/`.
Source Node phải xuất phát từ tài liệu vật lý/URL có thật trong `3-resources/raw_sources/`.
Nếu không tìm được nguồn → đánh dấu `status: UNVERIFIED`, không được tự bịa.

## R21 — SELF-AUDITING GATE
Mọi file vào `3-resources/raw_ingest/` **BẮT BUỘC** pass `audit_raw_ingest.py`.
Nếu status = `FAILED` → đánh dấu Atom `status: REJECTED` hoặc `DRAFT` kèm cảnh báo.
**Tuyệt đối không** tiến hành `breakdown` hay `absorb` nếu chưa pass audit.

## R27 — SCOPE ISOLATION
Gap-Check **CHỈ** dùng cho `DRAFT` atoms.
**Tuyệt đối không** dùng gap_check.py cho `synthesis/` hoặc `verified` content.

## R20 — YAML VALIDITY
Mọi giá trị Metadata có chứa dấu `:` **BẮT BUỘC** để trong ngoặc kép `""`.
Vi phạm → Ghost Atoms và hỏng liên kết Graph.

---
*auditor.md — 4 rules cho @auditor. Nguồn: [[GEMINI.md#R3]], [[GEMINI.md#R21]], [[GEMINI.md#R27]], [[GEMINI.md#R20]]*
