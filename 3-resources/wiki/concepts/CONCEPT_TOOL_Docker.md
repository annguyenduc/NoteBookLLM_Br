---
file_id: CONCEPT_TOOL_Docker
title: Docker (Containerization for AI Agents)
type: concept
status: VERIFIED
tags:
  - Wiki Page
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-08
last_updated: 2026-05-08
---

# Docker (Containerization for AI Agents)

## Core Principle
Docker cho phép đóng gói toàn bộ môi trường chạy Agent (code, thư viện, biến môi trường) vào một đơn vị duy nhất gọi là Container. Điều này đảm bảo Agent hoạt động nhất quán từ máy phát triển (Dev) lên đến môi trường thực tế (Production).

## Best Practices cho Agentic App
1. **Slim Base Images**: Sử dụng `python:3.11-slim` để giảm dung lượng image và bề mặt tấn công.
2. **Non-root User**: Luôn chạy container với quyền người dùng thông thường để đảm bảo an ninh (Security-first).
3. **Environment Isolation**: Tách biệt API Keys và Database URL thông qua file `.env` hoặc Docker Secrets.

## Ví dụ đối chiếu (R18)
- **Ví dụ thực tế (Original)**: Sử dụng `Docker Compose` để chạy đồng thời Agent API (FastAPI), Vector Database (Qdrant) và UI (Streamlit) chỉ bằng một câu lệnh.
- **Ẩn dụ sư phạm (Pedagogical)**: [Phóng tác] Giống như một **Container vận chuyển tiêu chuẩn**: Dù bên trong là hàng hóa gì (Python code, C++ libs), nó vẫn có thể đặt lên bất kỳ con tàu hay xe tải nào (AWS, Azure, Local Server) và vận hành một cách trơn tru mà không sợ bị hỏng hóc do môi trường khác biệt.

## 4F Reflection
- **Facts**: Docker giúp loại bỏ hoàn toàn câu nói "Chạy tốt trên máy tôi mà!" (It works on my machine).
- **Feelings**: Việc đóng gói thành công một image phức tạp mang lại cảm giác làm chủ hoàn toàn hạ tầng.
- **Findings**: Multi-stage build là kỹ thuật quan trọng nhất để giảm kích thước image cho các thư viện AI nặng.
- **Futures**: Xu hướng chạy Agent trực tiếp trên các WebAssembly (WASM) containers để tăng tốc độ khởi động.

## Nguồn tham khảo
- [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 9.4 (Dockerfile for agentic app).
