---
file_id: CONCEPT_META_SKILL_MODULARITY
title: "Skill Modularity (Tính Module của Skill)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_KARPATHY_CLAUDE_SKILLS]]"
---

## ## For future Claude
Trang này mô tả nguyên tắc Thiết kế Skill theo dạng Module (Skill Modularity) - chìa khóa để xây dựng các Agent có khả năng mở rộng. Bằng cách đóng gói các khả năng thành những đơn vị độc lập, chúng ta cho phép Agent tự học hỏi và tích hợp các kỹ năng mới mà không làm xáo trộn cấu trúc hệ thống hiện có.

## ## Key Claims / Summary
1.  **Encapsulation**: Mỗi Skill (ví dụ: Ingest, Query) là một thực thể độc lập với hướng dẫn (SKILL.md) và mã thực thi riêng.
2.  **Scalability**: Dễ dàng thêm mới hoặc nâng cấp từng Skill mà không ảnh hưởng đến toàn bộ hệ thống.
3.  **Standardization**: Tuân thủ cấu trúc thư mục chuẩn (Karpathy Pattern) để mọi Agent đều có thể hiểu và sử dụng.

## 1. Cấu trúc tiêu chuẩn
- **`SKILL.md`**: Bản mô tả và hướng dẫn cho Agent.
- **`scripts/`**: Chứa mã nguồn thực thi (Python, Bash).
- **`resources/`**: Chứa các templates và dữ liệu mẫu.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Triển khai Skill `wiki-ingest` cho Antigravity. Thay vì viết code trực tiếp vào system prompt, ta tạo folder chứa script xử lý. Agent chỉ cần đọc `SKILL.md` để biết cách gọi và thực thi kỹ năng đó. (Nguồn: [[SOURCE_META_KARPATHY_CLAUDE_SKILLS]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như kho học liệu STEAM. Mỗi chủ đề bài giảng (ví dụ: "Cảm biến siêu âm") được đóng gói thành một "Module". Giáo viên có thể "import" module này vào giáo án của mình một cách linh hoạt tùy theo nhu cầu của buổi học.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_KARPATHY_CLAUDE_SKILLS]] — Section: Skill Modularity and Agentic Infrastructure.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
