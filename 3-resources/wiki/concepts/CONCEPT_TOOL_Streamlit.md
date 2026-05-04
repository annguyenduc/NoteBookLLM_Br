---
file_id: CONCEPT_TOOL_STREAMLIT
title: "Streamlit (Agentic UI Framework)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@scout"
status: "verified"
source: "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

# Streamlit (Agentic UI Framework)

## Core Principle
Streamlit là một thư viện Python mã nguồn mở giúp tạo các ứng dụng web cho Machine Learning và Data Science chỉ trong vài phút. Trong Agentic AI, Streamlit là công cụ hàng đầu để xây dựng giao diện chat và bảng điều khiển (Dashboard) nhờ khả năng phản ứng (Reactivity) mạnh mẽ.

## Tại sao chọn Streamlit cho Agent?
1. **Python-Only**: Không cần kiến thức về HTML/CSS/JS, toàn bộ UI được viết bằng Python.
2. **Chat Elements**: Cung cấp sẵn các thành phần như `st.chat_message` và `st.chat_input` để xây dựng giao diện hội thoại chuyên nghiệp.
3. **Session State**: Quản lý lịch sử hội thoại và trạng thái của Agent một cách dễ dàng qua `st.session_state`.

## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Xây dựng một thanh Side-bar để hiển thị "Thought process" của Agent (vd: Log từ LangGraph) giúp người dùng hiểu tại sao Agent đưa ra câu trả lời đó.
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một **Kịch bản sân khấu tự viết (Instant Stage)**: Bạn chỉ cần tập trung vào lời thoại và diễn xuất (Logic), còn sân khấu, ánh sáng và đạo cụ (UI) sẽ tự động xuất hiện theo ý muốn mà không cần thuê đội ngũ kỹ thuật phức tạp.

## 4F Reflection
- **Facts**: Streamlit thực thi lại toàn bộ script mỗi khi có tương tác, điều này đòi hỏi kỹ thuật Caching (`@st.cache_resource`) để tối ưu hiệu suất.
- **Feelings**: Cảm giác cực kỳ phấn khích khi biến một đoạn script CLI khô khan thành một web app lung linh chỉ sau 10 dòng code.
- **Findings**: Việc tích hợp bảng "Debug" để hiển thị Tool Calls là yếu tố then chốt để xây dựng niềm tin của người dùng vào Agent.
- **Futures**: Xu hướng tích hợp các thành phần React tùy chỉnh (Custom Components) để mở rộng khả năng hiển thị dữ liệu phức tạp.

## Nguồn tham khảo
- [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 9.3 (Simple chat layout in Streamlit).
