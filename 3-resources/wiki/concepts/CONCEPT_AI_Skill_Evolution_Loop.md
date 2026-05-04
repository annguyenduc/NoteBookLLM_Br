---
file_id: "CONCEPT_AI_Skill_Evolution_Loop"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
---

# CONCEPT: AI Skill Evolution Loop

## Core Principle
**AI Skill Evolution Loop** là một quy trình tự động hóa việc bảo trì, tối ưu hóa và mở rộng năng lực của AI thông qua việc phân tích dữ liệu thực thi (telemetry) và phản hồi lỗi. Thay vì để skill ở trạng thái tĩnh, hệ thống sẽ liên tục "tiến hóa" skill để phù hợp với sự thay đổi của codebase và yêu cầu người dùng.

## Kiến trúc (Theo CodyMaster)
Quy trình gồm 3 chế độ (Modes):
1.  **FIX**: Sửa lỗi trực tiếp khi phát hiện drift (lệch) giữa tài liệu và thực thi.
2.  **DERIVED**: Tạo ra một phiên bản skill mới (clone) dựa trên một skill gốc nhưng tối ưu cho ngữ cảnh cụ thể.
3.  **CAPTURED**: Tự động "đóng gói" các chuỗi hành động thành công (thường xuyên lặp lại) thành một skill vĩnh viễn.

## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Khi một Agent liên tục gặp lỗi khi deploy lên môi trường Staging vì thiếu bước check VPN. Thay vì để user nhắc mỗi lần, hệ thống tự động cập nhật skill `safe-deploy` thêm bước `check-vpn`.
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như hệ miễn dịch của cơ thể. Lần đầu gặp vi khuẩn (lỗi), cơ thể sẽ học cách tạo kháng thể. Lần sau gặp lại, hệ thống sẽ tự tiêu diệt vi khuẩn đó mà không cần hỏi ý thức.

## 4F Reflection
- **Facts**: CodyMaster sử dụng `cm-skill-evolution` và `cm-learning-promoter` để thực hiện vòng lặp này.
- **Feelings**: Cảm giác an tâm khi biết hệ thống có khả năng tự sửa lỗi và tự học từ những lần "vấp ngã" (failures).
- **Findings**: Chìa khóa là "Telemetry" - phải ghi lại mọi bước đi và kết quả để có dữ liệu phân tích.
- **Futures**: Tích hợp vòng lặp này vào `wiki-lint` và `write-skill` của chúng ta để tự động đề xuất sửa đổi khi phát hiện link hỏng hoặc pattern lỗi thời.

Nguồn: [SOURCE_CODYMASTER_README](file:///d:/NoteBookLLM_Br/3-resources/wiki/sources/SOURCE_CODYMASTER_README.md) — Section: Self-Healing Skills
