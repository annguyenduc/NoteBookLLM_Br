# Superpowers Test Inventory

Báo cáo này liệt kê toàn bộ các nhóm test thực tế của Superpowers kiểm đếm được, so sánh với hệ thống kiểm thử hiện có của vault và đưa ra quyết định thích nghi hoặc giữ tham chiếu.

## Summary

- Total Superpowers test groups inspected: **7**
- Test groups useful for vault: **3** (Chứa các kịch bản hành động kích hoạt skill, subagent và yêu cầu tường minh)
- Test groups not relevant yet: **4** (Các nhóm test đặc thù cho các nền tảng IDE hoặc CLI bên thứ ba)

## Test Group Table

| Superpowers test group | Purpose | Vault equivalent | Decision |
| :--- | :--- | :--- | :--- |
| **skill-triggering** | Kiểm tra việc tự động kích hoạt kỹ năng đầu phiên. | `.agent/tests/skill-triggering` | adapt_as_test |
| **explicit-skill-requests** | Kiểm tra hành vi Agent khi người dùng yêu cầu gọi đích danh một skill. | None / Partial | adapt_as_test |
| **subagent-driven-dev** | Kiểm tra tính kỷ luật cô lập và phân bổ tác vụ khi gọi subagent. | None / Partial | adapt_as_test |
| **claude-code** | Các test case chuyên biệt cho môi trường chạy Claude Code. | None | reference_only |
| **opencode** | Các test case dành riêng cho môi trường OpenCode. | None | reference_only |
| **codex-plugin-sync** | Kiểm tra quy trình đồng bộ hóa plugin đóng gói của Codex. | None | reference_only |
| **brainstorm-server** | Kiểm thử API server hỗ trợ brainstorming local. | None | reference_only |
