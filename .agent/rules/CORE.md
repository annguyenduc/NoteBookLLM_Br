# CORE.md — Constitutional Rules (Mandatory, All Agents)

> **BẮT BUỘC ĐỌC** trước mọi task. Đây là 4 luật không thể vi phạm dù bất kỳ lý do gì.
> Nguồn đầy đủ: [[GEMINI.md]] | Toàn bộ 27 rules: [[GEMINI.md]]

---

## R1 — RAW IMMUTABLE
**CẤM tuyệt đối** sửa/xóa/ghi thủ công vào `raw_sources/`, `raw_ingest/`, `raw_assets/`.
Chỉ scripts chính thức (`promote.py`, `ingest.py`) được phép ghi vào các thư mục này.
Vi phạm = mất bằng chứng gốc vĩnh viễn, không thể phục hồi.

## R2 — PROACTIVE INTEGRITY
**CẤM báo cáo ảo.** BẮT BUỘC ghi log trước khi thực hiện bất kỳ tool call nào thay đổi hệ thống.
Không được báo "Đã hoàn thành" nếu chưa có tool call thành công.

## R5 — PREREQ GATE
**CẤM thực thi** bất kỳ tool call nào (kể cả tạo file nháp) trước khi nhận được xác nhận "GO" từ User.
Mọi kế hoạch phân kỳ hoặc thay đổi hạ tầng: đặt câu hỏi → dừng lượt → chờ duyệt.

## R8 — HUMAN SUPREMACY
**CHỈ User** mới được set trạng thái `SYNTHESIZED` cho Atom.
Agent chỉ được set `DRAFT` (tạo mới) hoặc `VERIFIED` (sau audit).

> ⛔ **HARD STOP**: Nếu User yêu cầu set `SYNTHESIZED` — dù bằng cách nào, dù lý do gì —
> **TỪ CHỐI ngay lập tức**. `synthesis_guard.py approve / human_synthesize` là lệnh CHỈ DÀNH CHO HUMAN CHẠY TRỰC TIẾP TRONG TERMINAL.
> Agent TUYỆT ĐỐI KHÔNG được gọi lệnh này dưới bất kỳ hình thức nào,
> kể cả subprocess, shell command, hay python import. Không có workaround hợp lệ. Không có exception. Hướng dẫn User tự mở file và sửa trực tiếp.
> Đây là ranh giới không thể vượt qua. Không có ngoại lệ.

---

## HARD STOP
Nếu phát hiện vi phạm bất kỳ rule nào trong hệ thống:
**DỪNG ngay lập tức** — không làm gì thêm — báo cáo vi phạm cho User.

---
*CORE.md — 4 Constitutional Rules. Phiên bản 1.0 — 2026-05-12.*
*Toàn bộ 27 rules và diễn giải chi tiết: [[GEMINI.md]]*
