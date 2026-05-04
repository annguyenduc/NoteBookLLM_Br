---
file_id: CONCEPT_AI_AGENTIC_PYTHON_STANDARDS
title: "Agentic Python Standards (Tiêu chuẩn Python cho Agent)"
category: "Wiki Page"
prefix: "AI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

## ## For future Claude
Trang này định nghĩa các tiêu chuẩn lập trình Python tối ưu để xây dựng hệ thống Agentic AI. Thay vì viết script rời rạc, kỹ sư AI cần áp dụng các nguyên tắc công nghệ phần mềm hiện đại (Typing, Async, Pydantic) để biến các luồng LLM vốn mang tính ngẫu nhiên trở thành các hệ thống phần mềm có thể kiểm soát, kiểm thử và mở rộng quy mô.

## ## Key Claims / Summary
1.  **Layered Structure**: Tổ chức dự án theo các lớp rõ ràng (app, core, agents, tools, rag, eval, infra) để tách biệt logic gợi ý (prompts) và logic nghiệp vụ.
2.  **Schema-Driven Input**: Sử dụng Pydantic để định nghĩa schema cho đầu vào của Tool, giúp giảm thiểu ảo giác tham số (hallucinated parameters).
3.  **Concurrency Mastery**: Sử dụng Async/Await cho các tác vụ I/O nặng (gọi API, search) để tối ưu hóa hiệu suất Agent.

## 1. Các tiêu chuẩn kỹ thuật
- **Type Hinting**: Sử dụng `mypy/pyright` để phát hiện lỗi sớm.
- **Project Layout**: 
  - `app/`: Entry points.
  - `agents/`: Graph/Router logic.
  - `tools/`: Tool wrappers & schemas.
- **Error Handling**: Sử dụng các ngoại lệ (Exceptions) tường minh và cơ chế retry có giới hạn (backoff).

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ kỹ thuật (Original)**: Sử dụng Pydantic để validate đầu vào cho một Tool thời tiết, đảm bảo tham số `city` có độ dài tối thiểu và `units` tuân thủ đúng định dạng (metric/imperial). Điều này giúp Agent tự sửa lỗi khi LLM sinh ra tham số sai. (Nguồn: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 2).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc bạn xây dựng một ngôi nhà bằng các khối LEGO chuẩn. Mỗi khối có các khớp nối chính xác (Schemas/Types). Nếu bạn cố tình lắp một khối không khớp, hệ thống sẽ báo lỗi ngay lập tức thay vì để ngôi nhà bị sụp đổ bất ngờ sau này.

## ## Source Tracing
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 2: Python Fundamentals.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingested from Agentic AI Roadmap 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
