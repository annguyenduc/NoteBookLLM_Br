# [SOP] PROJECT BRAIN: NOTEBOOKLLM_BR (v3.5)
<!-- LAST UPDATED: 2026-04-08 -->
<!-- STATUS: LOM v3.0 INTEGRATED (KARPATHY/SPISAK MODE) -->

Tài liệu này là **Chỉ mục Tri thức Chiến lược** (The Kernel) của dự án. Mọi Agent khi bắt đầu nhiệm vụ đều phải nạp file này để nắm bắt kiến trúc "LLM OS" và quy chuẩn vận hành bầy đàn.

> **Cập nhật v3.5**:
> - **Refactoring**: `SyncManager` di chuyển về `libs/core` để tách biệt Logic và Giao thức.
> - **Standard**: Cấu hình cứng `UTF-8` cho hệ thống Pipeline trên Windows, triệt tiêu lỗi Unicode.
> - **Memory**: Đồ thị kiến thức đạt trạng thái tối ưu (154 nodes sạch).


---

## 1. KIẾN TRÚC BỘ NHỚ VẬN HÀNH (LOM v3.0)

Hệ thống tuân thủ triết lý **"Accumulation over Retrieval"**:

| Layer | Tên gọi | Lưu trữ | Vai trò |
| :--- | :--- | :--- | :--- |
| **L1** | **Working Memory** | `CONTINUITY.md` | RAM: Trạng thái tức thời, checklist hiện hành. |
| **L2** | **Episodic Memory** | `3-resources/raw/` | I/O Logs: Dấu vết thực thi thô (Input cho chưng cất). |
| **L3** | **Semantic Local** | `3-resources/distilled/` | **LLM Wiki**: Tri thức chưng cất, liên kết bằng ``Wikilinks``. |
| **L4** | **Semantic Cloud** | **NotebookLM** | Deep Research: Thư viện tài liệu khổng lồ và Podcast tri thức. |

---

## 2. HIẾN PHÁP & ĐIỀU PHỐI AGENT

### 🛡️ Hiến pháp Agent (`CLAUDE.md`)
Quy định tối cao về cách Agent tương tác với Vault:
1. **Wiki Merge**: Luôn cập nhật vào bài viết Wiki hiện có thay vì tạo file mới.
2. **Graph Weaving**: Tự động tạo link chéo để duy trì Graph View.
3. **Reconciliation**: Xử lý mâu thuẫn tri thức bằng tag `#deprecated`.

### 👥 Swarm Registry (`AGENTS.md`)
Hệ thống vận hành với 8 Persona chuyên trách (v3.0):
- **@pm**: Lập kế hoạch & Hòa giải (`/reconcile`).
- **@researcher**: Chưng cất & Duy trì Wiki (`/heartbeat`).
- **@engineer**: Phát triển code & Tối ưu hóa pipeline.
- **@qa**: Kiểm định link & Sức khỏe dự án (`/visualize`).
- **@devops / @gateway**: Duy trì hạ tầng Port 4000.

---

## 3. TRI THỨC CHIẾN LƯỢC (STRATEGIC KNOWLEDGE)

### 📠 Chế tác & In 3D (Neptune 4)
- **Kỹ thuật bù trừ**: Sử dụng "Horizontal Expansion" để khớp các chi tiết lắp ghép cơ khí.
- **Workflow**: Nạp G-Code qua Moonraker (Port 7125) với SSH `mks:makerbase`.

### 🤖 Robotcon & STEAM (Mars Rover)
- **Cơ cấu Servo**: Giới hạn tối đa 2 servo cho học sinh khối 6.
- **Ý tưởng chủ đạo**: Đào mẫu đất (Excavation), Nâng hạ mẫu, và Hướng anten liên lạc.
- **Mô phỏng**: Gắn cảm biến siêu âm lên servo xoay để quét radar địa hình sa bàn giấy.

### 🧩 Tích hợp AI & IoT
- **Yolo Uno (ESP32-S3)**: Tích hợp mô hình YOLO nhận diện vật thể qua Bridge API.
- **Communication**: UART (115200) là kênh giao tiếp vật lý ưu tiên.

---

## 4. DANH MỤC THƯ MỤC CHUẨN (DIRECTORY MAP)

```text
d:\NoteBookLLM_Br\
├── .agent/              # Rules, Workflows, Skills
├── brain/               # BỘ NÃO DỰ ÁN (LOM)
│   ├── distilled/       # LLM Wiki (Tất cả hạt nhân tri thức nằm ở đây)
│   ├── raw/             # Toàn bộ Logs thô
│   └── optimized_context.md # FILE NÀY (Kernel tri thức)
├── res/                 # Tài liệu nghiên cứu & Docs
└── CONTINUITY.md        # RAM (Trạng thái xuyên phiên)
```
---
*Cập nhật bởi @pm | Framework: Antigravity v3.0 | Tiêu chuẩn: Karpathy/Spisak*
