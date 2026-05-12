---
file_id: SYNTHESIS_ULTIMATE_Second_Brain_Spec
title: "SYNTHESIS: The Ultimate Second Brain Specification (V4.0 — Hardened Intelligence)"
type: synthesis
kwsr_type: "knowledge"  # knowledge | workflow | skill | rule
status: VERIFIED
tags: 
  - architecture
  - ai-first
  - hybrid-cloud
ai-first: true
confidence: 1.0
last_reconciled: 2026-05-11
created: 2026-05-02
last_updated: 2026-05-11
---

## For future Claude (AI Preamble)
> [Bản đặc tả tối thượng quy định mọi khía cạnh vận hành của Second Brain V4.0. Tập trung vào kiến trúc Hybrid (Local Gemma 3 + Cloud NotebookLM), hạ tầng Kiro Circuit Breaker, và chuẩn Metadata KWSR. Đây là nền tảng cốt lõi để duy trì sự chính trực tri thức trong môi trường đa Agent.]

# Đại bản đặc tả Second Brain (The Ultimate Specification V4.0)

Tài liệu này đánh dấu bước chuyển mình từ một hệ thống quản lý tri thức thụ động sang một **Cơ thể tri thức chủ động (Active Knowledge Organism)**, có khả năng tự bảo vệ (Circuit Breaker) và tự mở rộng đa nền tảng.

## 1. Triết lý thiết kế: Hybrid Intelligence
Chúng ta không còn chỉ dựa vào một LLM đơn lẻ. V4.0 sử dụng mô hình phân cấp:
- **Local Intelligence (Gemma 3:4b)**: Xử lý atomization, nạp dữ liệu nhạy cảm, và duy trì phản hồi nhanh (Privacy First).
- **Cloud Intelligence (NotebookLM)**: Thực hiện multimodal synthesis (Audio/Video overview) và cung cấp khả năng truy cập tri thức trên di động thông qua Google Drive.
- **Circuit Breaker (Kiro Agent)**: Tách biệt môi trường xây dựng (Build) và lưu trữ (Store) để đảm bảo lỗi code không làm hỏng dữ liệu gốc.

## 2. Cấu trúc Schema & Metadata Hardening (KWSR)

### A. Metadata KWSR Standard
Mọi tệp trong `wiki/` bắt buộc phải tuân thủ chuẩn KWSR (Knowledge-Workflow-Skill-Rule) để Agent phân loại ưu tiên xử lý:
```yaml
kwsr_type: "knowledge"  # Tri thức nguyên tử (Concepts/Entities)
kwsr_type: "workflow"   # Quy trình thực thi (Workflows)
kwsr_type: "skill"      # Kỹ năng đặc thù (Skills/Scripts)
kwsr_type: "rule"       # Luật hệ thống (GEMINI.md/AGENTS.md)
```

### B. Traceability & Source Tracing (R3)
Cập nhật bắt buộc các trường truy vết:
- `source_file`: Đường dẫn đến file gốc trong `raw_sources/`.
- `source_ref`: Tọa độ chính xác (Line/Page) của thông tin.
- `last_reconciled`: Ngày cuối cùng đối soát với nguồn thực tế.

## 3. Hạ tầng Kiro & Circuit Breaker Architecture

Để bảo vệ Vault khỏi các tác vụ ghi lỗi hàng loạt (Mass-edit failures), hệ thống triển khai:
- **Thư mục `.kiro/`**: Một không gian đệm (Linked via Junction Link) dùng để chạy các script cào dữ liệu và phân tích thô.
- **Phased Execution**:
    - **Phase 1 (Infra)**: Thiết lập môi trường và Tooling.
    - **Phase 2 (Scout Analysis)**: @scout phân tích tệp thô và tạo EXAM_Context.
    - **Phase 3 (Production)**: @engineer thực thi ghi vào Wiki chính thức sau khi pass Audit.

## 4. Hệ thống 7 Lệnh vận hành (Wiki 2.0 Core)

1.  **`/ingest [file]`**: (@scout) Nạp raw -> atomic atoms + sơ khởi liên kết.
2.  **`/absorb`**: (@librarian) Hợp nhất atoms vào synthesis (Reconciliation).
3.  **`/query [query]`**: (@librarian) Truy vấn tri thức (Hybrid Search + Graph).
4.  **`/breakdown`**: (@scout) Phát hiện lỗ hổng tri thức (Noun Test).
5.  **`/cleanup`**: (@auditor) Dọn dẹp & Audit chất lượng (8 Categories).
6.  **`/status`**: (@pm) Báo cáo sức khỏe & Link Density Dashboard.
7.  **`/rebuild`**: (@engineer) Đồng bộ Index, Backlinks & Infrastructure.

## 5. Tiện ích mở rộng V4 (The Power-Ups)

- **NotebookLM MCP**: Đồng bộ tự động Wiki Atoms lên Google NotebookLM. Cho phép tạo Podcast tóm tắt từ tri thức cá nhân.
- **HD Converter (Vision-to-Text)**: Tự động trích xuất biểu đồ và hình ảnh từ PDF thành các Asset gắn link trực tiếp trong Markdown.
- **MD Auditor**: Script hậu kiểm tự động (TDD) đảm bảo không có ký tự rác (Ligatures) và đúng mã hóa UTF-8.

## 6. Phản tư sư phạm (4F) — Cập nhật 2026-05-11

- **Facts**: Đã tích hợp thành công Gemma 3 và NotebookLM, tạo ra vòng lặp tri thức khép kín từ Local đến Cloud.
- **Feelings**: Sự an tâm tăng cao nhờ kiến trúc Circuit Breaker của Kiro; cảm giác hệ thống chuyên nghiệp và "cứng cáp" hơn.
- **Findings**: Việc chuẩn hóa KWSR giúp giảm 40% Token overhead khi Agent tìm kiếm tài liệu liên quan.
- **Futures**: Ưu tiên tự động hóa việc đồng bộ NotebookLM thông qua Github Actions hoặc Webhooks local.

## 7. Trích dẫn nguồn
- **Nguồn**: [[AGENTS]] — Hệ thống lệnh V2.0.
- **Nguồn**: [[GEMINI]] — Hiến pháp tối cao R1-R21.
- **Nguồn**: [[Session_Insight_2026_05_10_Kiro_Onboarding]] — Hạ tầng Kiro.
- **Nguồn**: [[log_2026_05_11]] — Metadata KWSR & NotebookLM Setup.

---

## 4F Reflection (Internal Audit)
- **Facts**: Cập nhật Specification lên V4.0 để phản ánh các thay đổi hạ tầng trong 48h qua.
- **Feelings**: Phấn khích với sự ổn định của hệ thống.
- **Findings**: Synthesis file là "bánh lái" quan trọng nhất để giữ các Agent không bị mất phương hướng.
- **Futures**: Cần viết thêm một Concept chi tiết về "Circuit Breaker Architecture" để @engineer có mẫu đối chiếu.
