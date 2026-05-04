---
file_id: ENTITY_TOOL_GEMINI_PROMPTS_CODEX
title: "Gemini Prompts Codex (Selected Templates)"
category: "Entity"
prefix: "ENTITY"
agent_id: "@engineer"
status: "verified"
tags: ["Gemini", "Prompts", "Templates", "Coding", "Debug"]
source: "[[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]]"
---

# Gemini Prompts Codex (Selected Templates)

Ngân hàng các mẫu prompt tối ưu cho Gemini trích xuất từ Codex 850 Prompts.

## 1. Coding & Development
### Mẫu Tối ưu hóa Code
```markdown
[Role: Senior Python Performance Expert]
[Task: Optimize the following function for time complexity]
[Constraints:
- Maintain readability
- Do not use external libraries
- Provide Big O analysis before and after]
[Input: <paste_code_here>]
```

### Mẫu Debugging chuyên sâu
```markdown
[Role: Senior Debugger]
[Task: Identify the root cause of the following error]
[Context: The error occurs only in production environment under high load]
[Input: <paste_traceback_and_logs_here>]
```

## 2. System Architecture
### Mẫu Thiết kế Microservices
```markdown
[Role: Cloud Solutions Architect]
[Task: Design a scalable microservice architecture for <system_name>]
[Requirement: Must handle 10k requests per second using AWS services]
[Output: Provide a Mermaid diagram and component descriptions]
```

## 3. Documentation & Testing
### Mẫu Viết Unit Test (Pytest)
```markdown
[Role: QA Engineer]
[Task: Write comprehensive Pytest cases for the following class]
[Requirement: Include edge cases, invalid inputs, and 100% branch coverage]
[Input: <paste_class_here>]
```

## 4. Data Transformation
### Mẫu Chuyển đổi định dạng dữ liệu phức tạp
```markdown
[Role: Data Engineering Specialist]
[Task: Convert the following unstructured JSON into a normalized CSV schema]
[Requirement: Handle nested arrays by flattening them and ensure date formats are ISO-8601]
[Input: <paste_json_here>]
```

## 5. Web Scraping & Extraction
### Mẫu Trích xuất tri thức từ HTML
```markdown
[Role: Web Scraping Expert]
[Task: Extract all product names, prices, and ratings from the provided HTML]
[Constraint: Return the data as a clean Markdown table. Ignore ads and navigation links.]
[Input: <paste_html_here>]
```

## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Sử dụng cấu trúc `[Role] [Task] [Constraint] [Input]` để ép Gemini vào trạng thái "Deep Thinking".
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc bạn cấp một "Bộ khuôn đúc" (Templates) cho một nghệ nhân: Nghệ nhân có thể rất giỏi, nhưng bộ khuôn giúp mọi tác phẩm họ tạo ra đều có hình khối chuẩn xác và đồng nhất về chất lượng.

## Nguồn tham khảo
- [[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]] — Phân đoạn Prompts cho Developer.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
