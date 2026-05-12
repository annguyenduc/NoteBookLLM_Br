---
file_id: "INSIGHT_2026_05_11_AI_Ollama_Gap_Check"
title: "Ollama Gap-Check Integration (Phase 2 & Final Choice)"
type: "insight"
tags:
  - "Session_Log"
  - "AI_Integration"
  - "Gemma3"
  - "Gap_Check"
status: "VERIFIED"
created: "2026-05-11"
last_updated: "2026-05-11"
---

# Nhật ký & Bài học hệ thống (Session Insight)

## 1. Mục tiêu phiên làm việc (Session Objectives)
- Lựa chọn Model Layer tối ưu cho tác vụ Gap-check.
- Khắc phục lỗi Encoding và Escaping khi tích hợp Ollama vào pipeline.

## 2. Kết quả đạt được (Outcomes)
- Chốt hạ **Gemma3:4b** làm model mặc định cho Atom Drafting nhờ khả năng Recall vượt trội.
- Sửa lỗi JSON Decode Error do PowerShell escaping.
- Tối ưu hóa hiệu năng nạp file lớn bằng cách điều chỉnh chunk preview và timeout.

## 3. Vấn đề phát sinh & Khắc phục (Issues & Resolutions)
- **Vấn đề 1:** PowerShell JSON Escaping làm hỏng tham số JSON.
    - **Nguyên nhân (Root Cause):** PowerShell xử lý dấu ngoặc kép không đồng nhất khi truyền tham số.
    - **Cách khắc phục:** Chuyển sang dùng Python `subprocess.run` với danh sách arguments thay vì shell command string.
- **Vấn đề 2:** Lỗi Encoding UTF-8 trên Windows terminal.
    - **Nguyên nhân (Root Cause):** Terminal mặc định dùng cp1252.
    - **Cách khắc phục:** Cấu hình `sys.stdout` reconfigure encoding sang UTF-8 và set `$env:PYTHONIOENCODING`.

## 4. Bài học hệ thống (System Learnings / Instincts)
- **Bài học 1:** Ưu tiên chất lượng tri thức (Recall) hơn tốc độ nạp. Gemma3:4b (15s) đáng giá hơn Qwen2.5:3b (8s) vì độ chi tiết.
- **Bài học 2:** Luôn xử lý arguments dưới dạng list trong Python để tránh các vấn đề về shell escaping đặc thù của hệ điều hành.

## 5. Đề xuất cho phiên sau (Next Steps)
- [ ] Tích hợp chính thức Gap-check vào quy trình Ingest tự động.
- [ ] Theo dõi tải VRAM khi chạy batch lớn 10+ chunks.
