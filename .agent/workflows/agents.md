# 🚀 Project Agents Registry (Workspace: NoteBookLLM_Br)

> **Mục lục các Agent chuyên trách được kích hoạt cho dự án quản lý tri thức NotebookLM và đồng bộ hóa Gemini.**

## 1. Project Specific Agents
| Agent ID | Tên Agent | Mô tả | Trạng thái |
| :--- | :--- | :--- | :--- |
| `notebooklm-expert` | **NotebookLM Specialist** | Chuyên gia vận hành MCP NotebookLM (tạo audio/slides/audio). | **Active** |
| `context-synthesizer` | **Context Synthesizer** | Phân tích và nén tri thức từ các cuộc hội thoại 10MB thành KIs. | **Active** |
| `steam-k12-coach` | **STEAM K-12 Specialist** | Thiết kế giáo trình và nội dung STEAM theo chuẩn NGSS. | **On-demand** |
| `media-factory` | **Media Factory** | Tự động tạo Audio Overview, Infographic, Video từ Notebook. | **On-demand** |

## 2. Integration Status
*   **Gemini Sync**: Kết nối qua `gemini-sync-server`.
*   **NotebookLM**: Kết nối qua `notebooklm-mcp-server`.
*   **Smart AI Hub**: Kết nối qua Cổng 4000 (Localhost).

---
### 🛠️ Các lệnh thông dụng cho Agent:
- `/setup-notebooklm-mcp`: Cấu hình máy chủ NotebookLM.
- `python tools/pipeline/smart_splitter.py`: Kích hoạt Agent chia nhỏ ngữ cảnh lớn.
- `/cm-dashboard`: Xem bảng Kanban tiến trình làm việc của Agent.

*Lưu ý: Luôn kiểm tra `mcp_config.json` trước khi khởi động các Agent chuyên trách.*
