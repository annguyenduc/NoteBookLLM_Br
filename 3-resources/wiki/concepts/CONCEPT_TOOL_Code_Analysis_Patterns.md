---
file_id: CONCEPT_TOOL_CODE_ANALYSIS_PATTERNS
title: "Code Analysis Patterns (Mẫu phân tích logic mã nguồn)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]]"
  - "[[SOURCE_META_KARPATHY_CLAUDE_SKILLS]]"
---

## ## For future Claude
Trang này định nghĩa các mẫu (patterns) để Agent thực hiện phân tích mã nguồn một cách hệ thống. Thay vì chỉ đọc code từ trên xuống dưới, việc áp dụng các pattern này giúp Agent phát hiện nhanh các lỗ hổng logic, nợ kỹ thuật (technical debt) và các điểm cần tối ưu hóa hiệu năng.

## ## Key Claims / Summary
1.  **Decomposition First**: Chia nhỏ module phức tạp thành các đơn vị chức năng trước khi phân tích.
2.  **Flow Tracing**: Theo dõi dòng chảy của dữ liệu (Data Flow) và luồng điều khiển (Control Flow) để tìm điểm nghẽn.
3.  **Cross-Reference Audit**: Luôn đối chiếu code hiện tại với các quy tắc hệ thống (ví dụ: Rule 17, Rule 20) để đảm bảo tính nhất quán.

## ## Ví dụ đối chiếu (Rule 17)
-   **Ví dụ thực tế (Original)**: Sử dụng kỹ thuật "Inverted Reasoning" - Giả định một bug cụ thể đang xảy ra (ví dụ: memory leak) và tìm kiếm các dấu hiệu trong code xác nhận giả định đó, thay vì quét code một cách mù quáng.
-   **Ẩn dụ sư phạm (Pedagogical)**: Giống như một bác sĩ giải phẫu đang xem phim X-quang. Bác sĩ không chỉ nhìn vào tấm phim, họ tìm kiếm các "mẫu hình" (patterns) của sự bất thường mà họ đã học được qua hàng nghìn ca bệnh khác nhau để đưa ra chẩn đoán chính xác và nhanh chóng.

## ## Detailed Analysis
Các mẫu phân tích phổ biến cho AI Agent:
- **Dependency Map Analysis**: Xây dựng bản đồ các file liên quan để hiểu tầm ảnh hưởng của một thay đổi.
- **Edge Case Stress Test**: Yêu cầu AI liệt kê 5 kịch bản input "cực đoan" nhất để kiểm tra tính bền bỉ của hàm.
- **Complexity Audit**: Đánh giá độ phức tạp Cyclomatic và đề xuất refactor nếu vượt quá ngưỡng cho phép.
- **Surgical Edit Identification**: Xác định số dòng code tối thiểu cần thay đổi để giải quyết vấn đề (Surgical Changes Principle).

## ## Relationships
- `uses` -> [[CONCEPT_TOOL_Gemini_Role_Prompting]]
- `part_of` -> [[ENTITY_Python]]
- `governed_by` -> [[AGENTS.md]]

## ## Source Tracing
- **Nguồn**: [[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]] — Section 5: Advanced Debugging.
- **Nguồn**: [[SOURCE_META_KARPATHY_CLAUDE_SKILLS]] — Pattern: Surgical Refactoring.

## ## History / Revisions
- **2026-05-03**: [@engineer] Chuyển đổi từ stub sang verified, bổ sung Rule 17 và Rule 20.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
