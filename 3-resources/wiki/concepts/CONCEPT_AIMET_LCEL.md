file_id: CONCEPT_AIMET_LCEL
title: "LCEL (LangChain Expression Language)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_Agentic_AI_Roadmap_2026]]"
---

## ## For future Claude
Trang này giải thích về LCEL (LangChain Expression Language) - một ngôn ngữ đặc tả giúp lập trình viên xây dựng các pipeline AI một cách có cấu trúc và dễ bảo trì. LCEL biến các thành phần rời rạc thành một "dòng chảy" tri thức thống nhất, hỗ trợ đắc lực cho việc xây dựng các Agent phức tạp.

## ## Key Claims / Summary
1.  **Declarative Chains**: Chuyển từ cách viết code tuần tự sang cách khai báo luồng dữ liệu (Data Flow).
2.  **Streaming & Async**: Hỗ trợ mặc định việc truyền dữ liệu từng phần (streaming) và thực thi bất đồng bộ.
3.  **Unified Interface**: Mọi thành phần LCEL đều tuân thủ interface `Runnable`.

## ## Detailed Analysis

# LCEL (LangChain Expression Language)

## 1. Định nghĩa
**LCEL** là một ngôn ngữ đặc tả (DSL) giúp kết hợp các thành phần của [[ENTITY_TOOL_LangChain|LangChain]] (prompts, models, parsers, tools) thành các chuỗi (chains) hoặc pipeline xử lý một cách linh hoạt và có tính khai báo (declarative).

## 2. Đặc điểm cốt lõi
- **Tính Module (Modularity)**: Cho phép tráo đổi model hoặc parser mà không cần viết lại toàn bộ logic.
- **Tính Quan sát (Observability)**: Tự động hỗ trợ logging và tracing cho từng bước trong chain.
- **Tính Song song**: Tối ưu hóa việc thực thi các bước độc lập cùng một lúc.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Xây dựng một RAG chain cơ bản.
> **Ứng dụng**: Sử dụng cú pháp `|` (pipe) để nối: `Prompt | Model | StrOutputParser`. Đây là cách viết sạch và dễ bảo trì hơn so với việc gọi hàm lồng nhau.
> **Nguồn**: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 5.1

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Dạy học sinh về "Luồng dữ liệu" (Data Flow) trong STEAM.
> **Ứng dụng**: Ví LCEL như các khối Lego có các đầu nối tiêu chuẩn. Học sinh chỉ cần lắp ráp: "Khối Lắng nghe | Khối Suy nghĩ | Khối Hành động". Việc thay đổi "Khối Suy nghĩ" (từ GPT-4 sang Claude) không làm hỏng các khối còn lại. Đây là tư duy thiết kế hệ thống (Systems Thinking).

---
**Nguồn**: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 4.1


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
