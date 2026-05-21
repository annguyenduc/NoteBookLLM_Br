---
file_id: "INSIGHT_ARCH_TIS_Ollama_Gap_Check_Hardening"
title: "Session Insight: Ollama Gap-Check Hardening and Vault Dedup Cross-Type Match"
type: "insight"
tags:
  - "Session_Log"
  - "System_Audit"
  - "Gap_Check"
status: "DRAFT"
source_file: ""
source_ref: "[[SOURCE_ARCH_TIS_Thinking_in_Systems]]"
created: "2026-05-21"
last_updated: "2026-05-21"
---

## For future Claude (AI Preamble)
> Phiên làm việc tập trung vào kiểm tra chất lượng kết quả batch gap-check gồm 77 chunks của tài liệu Thinking in Systems. Phát hiện và xử lý lỗi lọt bộ lọc trùng do AI phân loại sai loại Atom (ví dụ: gemma3 gắn nhãn "Stock" là Entity thay vì Concept dẫn đến bypass filter). Sửa đổi script `gap_check.py` để hỗ trợ quét chéo loại (cross-type scan), chuẩn hóa số nhiều/số ít, đồng thời bổ sung 4 quy tắc nghiêm ngặt vào Prompt để ép gemma3 bỏ qua các ví dụ minh họa cơ bản của sách (chloroplasts, furnace...).

# Nhật ký & Bài học hệ thống (Session Insight)

## 1. Mục tiêu phiên làm việc (Session Objectives)
- Đánh giá chất lượng của 77 tệp gap candidates tạo ra từ batch runner.
- Xác định tỷ lệ trùng lặp với kho dữ liệu (vault) hiện tại của tài liệu `arch_thinking_in_systems`.
- Khắc phục triệt để tình trạng lọt trùng (false negatives) và giảm nhiễu (noise) do AI sinh ra.

## 2. Kết quả đạt được (Outcomes)
- Hoàn thành audit chất lượng 493 candidates của 77 chunks.
- Chỉ ra 127 candidates (25.8%) bị lọt trùng do phân loại sai type hoặc biến thể số nhiều/ít.
- Chỉnh sửa thành công `gap_check.py` trong worktree `agent/gap-check-tis`:
  - Chuyển `check_vault_duplicate()` thành quét chéo (cross-type scan) trên cả 7 thư mục lưu trữ Atom.
  - Bổ sung cơ chế chuẩn hóa biến thể số nhiều (`loops` ↔ `loop`).
  - Thêm 4 luật mới trong `PROMPT_TEMPLATE` để siết chặt tiêu chuẩn trích xuất của gemma3.
- Chạy thử nghiệm thành công trên chunk 001: loại bỏ hoàn toàn các thực thể minh họa (`chloroplasts`, `enzymes`) và chỉ giữ lại các concept thực thụ.
- Đạt 13/13 unit tests pass cho cơ chế kiểm tra trùng lặp mới.

## 3. Vấn đề phát sinh & Khắc phục (Issues & Resolutions)
- **Vấn đề 1:** Khoảng 25.8% gap candidates bị trùng lặp với các Atom đã tồn tại trong vault (ví dụ: `Feedback Loop` xuất hiện 9 lần, `Stock` và `Flow` xuất hiện nhiều lần).
  - **Root Cause:** 
    1. Hàm `check_vault_duplicate()` cũ chỉ tìm kiếm trong thư mục tương ứng với loại Atom mà AI phân loại (nếu AI nhầm `Stock` là Entity thì script chỉ quét thư mục `entities/` trong khi tệp thực sự nằm ở `concepts/`).
    2. AI sinh ra các biến thể số nhiều như `Feedback Loops` trong khi vault chỉ lưu `Feedback Loop`.
  - **Cách khắc phục:** Cập nhật logic `check_vault_duplicate()` sang quét toàn bộ 7 thư mục con của wiki và tự động bóc tách tiền tố/hậu tố số nhiều `s`.
- **Vấn đề 2:** Tồn tại nhiều từ khóa mang tính minh họa thuộc vật lý/sinh học/đời sống (`bloodstream`, `furnace`, `insulation`, `lumber`) được trích xuất thành Entity.
  - **Root Cause:** Prompt cũ hướng dẫn lọc ví dụ minh họa chung chung (`digestive system`, `city`...) nhưng không chỉ rõ các ví dụ đặc thù về công cụ vật lý hoặc thực thể sinh học trong sách.
  - **Cách khắc phục:** Siết prompt bằng cách bổ sung luật cấm chi tiết (Rules 9, 10, 11, 12) cùng các từ khóa cấm cụ thể.

## 4. Bài học hệ thống (System Learnings / Instincts)
- **Instinct #1:** Khi làm việc với local model nhỏ (gemma3:4b), luật cấm trong prompt phải mang tính đại diện trực quan cao kèm ví dụ cụ thể thay vì viết abstract (ví dụ: liệt kê rõ "furnace, chloroplasts" thay vì chỉ viết "illustrative systems").
- **Instinct #2:** Không được tin tưởng hoàn toàn vào loại Atom do AI gắn nhãn khi thực hiện đối soát trùng lặp. Kiểm tra trùng lặp bắt buộc phải thực hiện quét chéo (cross-type) trên toàn bộ danh mục wiki.
- **Instinct #3:** Sau khi promote tài liệu thô thành công, cần dọn dẹp hoặc đóng gói thư mục gốc tương ứng trong `00_Inbox/Converted_Sources/` sang `_archive/` để tránh agent nhầm lẫn dữ liệu giữa Inbox và raw_ingest.

## 5. Đề xuất cho phiên sau (Next Steps)
- [ ] Merge nhánh `agent/gap-check-tis` vào `main`.
- [ ] Chạy lại toàn bộ batch gap-check cho 77 chunks bằng script và prompt mới đã được siết chặt để làm sạch triệt để `00_Inbox/gap_candidates/`.

**Source PDF:** [Thinking in Systems.pdf]
