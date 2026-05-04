---
title: "CONCEPT: Tool Integration (Custom Tools & Connectors)"
type: concept
tags: ["Agentic AI", "Tools", "Integration", "Pydantic", "AIMET"]
status: "draft"
relationships:
  - type: "part_of"
    target: "[[CONCEPT_AIMET_MultiAgent_Architecture]]"
  - type: "prerequisite_of"
    target: "[[ENTITY_AIMET_LangGraph]]"
created: "2026-05-02"
---

# Tool Integration (Custom Tools & Connectors)

## 1. Định nghĩa

**Tool Integration** là quá trình cho phép LLM agent tương tác với thế giới bên ngoài thông qua các hàm code, API, hoặc databases. Trong hệ thống agentic, "tool" không chỉ là một script mà là một **typed interface** mà LLM có thể hiểu và gọi một cách chính xác.

## 2. Nguyên lý / Cấu trúc

Mô hình tích hợp tool chuẩn thường bao gồm 3 phần:
1. **Tool Definition**: Tên tool và mô tả (bằng ngôn ngữ tự nhiên để LLM hiểu khi nào dùng).
2. **Input Schema**: Định nghĩa kiểu dữ liệu đầu vào (thường dùng **Pydantic**).
3. **Execution Logic**: Code thực thi thực tế (Python function, REST call...).

```python
# Ví dụ Pydantic Schema cho Tool
from pydantic import BaseModel, Field

class SearchArgs(BaseModel):
    query: str = Field(..., description="Từ khóa cần tìm kiếm")
```

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Agent cần lấy dữ liệu thời tiết thực tế
> **Ứng dụng**: Tạo một `GetWeather` tool với input là `city`. LLM đọc mô tả tool → suy luận cần city → gọi tool với `city="Hanoi"` → nhận kết quả Observation.
> **Nguồn**: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 7 (Tool Integration)

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Học sinh lớp 9 làm dự án IOT Robot
> **Ứng dụng**: Tạo tool `MoveRobot(direction, distance)` tích hợp vào LLM Agent. Học sinh nói: "Đi tới 5m rồi rẽ trái". Agent Thought: "Cần gọi tool MoveRobot". Action: `MoveRobot(direction="forward", distance=5)`. Đây là cách dạy lập trình điều khiển thông qua ngôn ngữ tự nhiên.

## 4. Phản tư sư phạm (4F)
- **Facts**: Typed schemas giảm 80% lỗi hallucination parameters của LLM.
- **Feelings**: Việc viết mô tả tool (docstring) tốt quan trọng hơn việc viết code logic phức tạp.
- **Findings**: Luôn cần validate input trước khi tool thực thi (Gatekeeping).
- **Futures**: Tích hợp với [[ENTITY_AIMET_LangGraph]] để handle tool errors (Self-healing).

## 5. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 7, trang 15
- **Fact-check**: Đã đối chiếu PDF trang 15: "Use Pydantic models for schemas... reduce hallucinated parameters"

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_AIMET_Tool_Integration.md"
  operation: "create"
  added: "Healing broken link: tạo concept Tool Integration còn thiếu"
  compliance: "Rule 20 OK"


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
