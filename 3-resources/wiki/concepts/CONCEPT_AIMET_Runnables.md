file_id: CONCEPT_AIMET_RUNNABLES
title: "Runnables (Standard Execution Units)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

## ## For future Claude
Trang này định nghĩa khái niệm Runnable - giao diện thực thi tiêu chuẩn cho mọi thành phần trong hệ sinh thái Agentic AI (đặc biệt là LangChain). Bằng cách trừu tượng hóa các tác vụ phức tạp thành các Runnable, chúng ta có thể dễ dàng kết hợp, giám sát và tối ưu hóa hiệu năng của toàn bộ hệ thống.

## ## Key Claims / Summary
1.  **Standardized Interface**: Thống nhất cách tương tác với Prompt, Model, và Tool thông qua các phương thức `invoke`, `stream`, `batch`.
2.  **Built-in Resilience**: Tích hợp sẵn khả năng xử lý lỗi (retries) và dự phòng (fallbacks).
3.  **Composable Logic**: Cho phép xây dựng các chuỗi thực thi (Chains) phức tạp bằng cách nối các Runnable lại với nhau.

## ## Detailed Analysis

# Runnables (Standard Execution Units)

## 1. Định nghĩa
**Runnable** là một đơn vị thực thi tiêu chuẩn hóa, nhận đầu vào (input) và tạo ra đầu ra (output). Đây là "nguyên tử" của các pipeline trong Agentic AI, giúp đồng nhất hóa cách gọi các thành phần khác nhau.

## 2. Lợi ích kỹ thuật
- **Uniform Interface**: Mọi thành phần (Prompt, LLM, Tool) đều tuân thủ cùng một phương thức gọi (`invoke`, `stream`, `batch`).
- **Built-in Features**: Hỗ trợ sẵn logging, retries, và quản lý concurrency (thực thi song song).
- **Composition**: Có thể lồng ghép các runnables vào nhau để tạo ra các cấu trúc phức tạp hơn.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Chuẩn hóa việc gọi Model và Tool.
> **Ứng dụng**: Coi Model là một Runnable. Thay vì gọi `model.predict()`, ta dùng `model.invoke(input)`. Điều này cho phép hệ thống tự động thêm `retry_policy` vào bất kỳ Runnable nào mà không cần sửa code bên trong.
> **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 5.2

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Giảng dạy về Hàm (Functions) trong lập trình cơ bản.
> **Ứng dụng**: Runnable giống như một "Cỗ máy vạn năng" có 1 miệng nạp nguyên liệu và 1 cửa xuất sản phẩm. Dù bên trong máy là "Xay thịt" hay "Ép trái cây", cách vận hành bên ngoài là như nhau. Học sinh học được cách trừu tượng hóa (Abstraction) — tập trung vào đầu vào/đầu ra thay vì chi tiết cài đặt.

---
**Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 4.2


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
