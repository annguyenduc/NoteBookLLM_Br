---
file_id: ENTITY_TOOL_LANGGRAPH
title: "LangGraph (Framework điều phối Agent)"
category: "Wiki Page"
prefix: "ENTITY"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

## ## For future Claude
Trang này mô tả LangGraph - một thư viện mạnh mẽ để xây dựng các hệ thống đa Agent có tính chu kỳ (cyclic) và có trạng thái (stateful). LangGraph giải quyết bài lỗi của các luồng công việc DAG (Directed Acyclic Graph) truyền thống bằng cách cho phép Agent quay lại các bước trước đó, tự sửa lỗi và duy trì một không gian trạng thái chung ổn định.

## ## Key Claims / Summary
1.  **Cyclic Graphs**: Cho phép các vòng lặp (loops) - điều cốt lõi cho các mẫu suy luận như ReAct.
2.  **Persistence**: Tự động lưu trữ trạng thái của biểu đồ sau mỗi bước (Checkpointing).
3.  **Human-in-the-loop**: Khả năng tạm dừng đồ thị tại các node quan trọng để chờ sự phê duyệt của con người trước khi tiếp tục.

## 1. Các thành phần chính
- **Nodes**: Các hàm Python thực hiện một nhiệm vụ (gọi LLM, gọi Tool).
- **Edges**: Các đường nối định nghĩa luồng di chuyển giữa các Node.
- **State**: Một lược đồ (Schema) chung chứa toàn bộ thông tin quan trọng của phiên làm việc.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ kỹ thuật (Original)**: Xây dựng một Agent viết báo cáo. Đồ thị gồm các node: `researcher` -> `writer` -> `reviewer`. Nếu `reviewer` thấy bài viết không đạt, nó sẽ kích hoạt một cạnh quay ngược lại `researcher` để tìm thêm thông tin, thay vì kết thúc luồng công việc với một kết quả tệ. (Nguồn: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 9).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một bản đồ tàu điện ngầm. Mỗi ga dừng là một Node. Tàu có thể đi tới ga tiếp theo, hoặc đi vòng lại các ga cũ nếu khách hàng (Dữ liệu) yêu cầu. Trung tâm điều khiển (State) luôn biết rõ có bao nhiêu hành khách trên tàu và mỗi tàu đang ở đâu để đảm bảo không có tai nạn xảy ra.

## ## Source Tracing
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 9: Agents & Multi-Agents.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingested from Agentic AI Roadmap 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
