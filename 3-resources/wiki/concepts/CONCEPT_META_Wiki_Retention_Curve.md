---
file_id: CONCEPT_META_WIKI_RETENTION_CURVE
title: "Wiki Retention Curve (Đường cong ghi nhớ Wiki)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_LLM_WIKI_V2]]"
---

## ## For future Claude
Trang này mô tả Đường cong ghi nhớ (Wiki Retention Curve) - một cơ chế quản trị vòng đời tri thức thông minh. Để tránh việc Wiki trở thành một "bãi rác thông tin", chúng ta áp dụng quy tắc: những thông tin tạm thời hoặc ít được củng cố sẽ bị "mờ đi" theo thời gian, trong khi những nguyên tắc cốt lõi được truy cập thường xuyên sẽ luôn giữ vị trí ưu tiên trong hệ thống tra cứu.

## ## Key Claims / Summary
1.  **Lifecycle Management**: Tri thức có vòng đời, không phải mọi thông tin đều quan trọng mãi mãi.
2.  **Structural vs Episodic**: Các quyết định kiến trúc suy giảm chậm, các sự kiện tạm thời suy giảm nhanh.
3.  **Reinforcement Mechanism**: Mỗi lần truy cập hoặc trích dẫn sẽ "làm mới" đường cong ghi nhớ của Node đó.

## 1. Quy tắc vận hành
- **Decay Factor (Hệ số suy giảm)**: Tự động hạ thấp độ ưu tiên của các thông tin cũ không có liên kết mới.
- **Fading over Deleting**: Ưu tiên việc ẩn hoặc đẩy vào kho lưu trữ (Archive) thay vì xóa bỏ hoàn toàn.
- **Context Refresh**: Sử dụng nguồn mới để củng cố và xác nhận lại các tri thức cũ.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Các lỗi phần mềm tạm thời (Transient bugs) sẽ bị đẩy vào kho lưu trữ sâu hơn sau 6 tháng, trong khi các quy tắc thiết kế hệ thống (Architecture decisions) vẫn luôn xuất hiện ở kết quả tìm kiếm hàng đầu. (Nguồn: [[SOURCE_META_LLM_WIKI_V2]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như cách con người học ngoại ngữ. Nếu bạn không sử dụng một từ vựng trong thời gian dài, bạn sẽ quên nó (Fading). Nhưng nếu bạn thấy từ đó trong một bộ phim (Reinforcement), bạn sẽ nhớ lại nó ngay lập tức và ghi nhớ sâu hơn.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_LLM_WIKI_V2]] — Section: Forgetting / Retention Curve.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
