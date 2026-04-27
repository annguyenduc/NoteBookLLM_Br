# 🧠 Brain Index — NoteBookLLM_Br Wiki Navigation Hub
> **Dành cho LLM Agent:** Đọc file này TRƯỚC TIÊN khi nhận lệnh Query. Không scan toàn bộ `wiki/`.
> **Cập nhật lần cuối:** 2026-04-23 | **Tổng wiki pages:** 2,391 | **Raw sources:** 69

---

## 📍 Cách sử dụng Index này

```
1. Xác định Taxonomy cần tìm (KHMT / IOT / Robot / DESIGN)
2. Đọc section tương ứng để biết file nào liên quan
3. Chỉ đọc file cụ thể đó — KHÔNG đọc toàn bộ folder
4. Cập nhật index.md nếu thêm atom mới (append, không overwrite)
```

---

## 🗺️ Bản đồ Tri thức (Knowledge Map)

### 📚 Taxonomy Chính

| Taxonomy | Prefix | Số wiki | Mô tả |
|---|---|---|---|
| **KHMT** | `QUESTION_KHMT_` | ~241 | Khoa học máy tính — AI cho THCS/Tiểu học |
| **IOT** | `QUESTION_IOT_` | ~1,227 | IoT, Arduino, YoloBit, Halocode, AI Arduino |
| **Robot** | `QUESTION_Robot_` | ~477 | Robotics — Codey, GBot, mBot, Rover, xBot, Unplugged |
| **DESIGN** | `QUESTION_DESIGN_` | ~261 | Thiết kế — 3D Tinkercad, Canva, Maker Empire, Wordpress |
| **CONCEPT** | `ATOMS_` | 12 | Concept nodes — kiến thức nền (không phải câu hỏi) |

---

## 📂 Cấu trúc Thư mục Brain

```
brain/
├── index.md          ← BẠN ĐANG ĐỌC FILE NÀY
├── wip.md            ← Work In Progress (session continuity)
├── log.md            ← Nhật ký tất cả hành động agent
├── lint_report.md    ← Báo cáo kiểm tra sức khỏe wiki
├── WIKI_INDEX.md     ← Index chi tiết (auto-generated)
│
├── raw/              ← 69 files — Nguồn gốc. READ-ONLY. Không sửa!
├── wiki/            ← 2,391 files — Wiki layer chính
│   ├── QUESTION_*    ← Dữ liệu câu hỏi LMS đã atomized
│   └── ATOMS_*       ← Concept knowledge nodes
├── distilled/        ← Knowledge đã verify — Output cuối cùng
├── lessons/          ← 4 files — Bài học đa môn (non-LMS)
├── process/          ← Handoff files giữa agents (sống/chết theo task)
└── archive/          ← 1,272 files — Failed wiki pages (không dùng)
```

---

## 🔍 Hướng dẫn Query nhanh

### Tìm câu hỏi theo Module

| Muốn tìm | Dùng pattern |
|---|---|
| Câu hỏi về YoloBit | `QUESTION_IOT_YoloBit_*` |
| Câu hỏi về AI Arduino Đề 3 | `QUESTION_IOT_AI_Arduino_D3_*` |
| Câu hỏi về mBot Module 1 | `QUESTION_Robot_mBot_*M1*` |
| Câu hỏi về Canva | `QUESTION_DESIGN_Canva_*` |
| Câu hỏi về AI THCS | `QUESTION_KHMT_AI_THCS_*` |
| Khái niệm về Arduino | `ATOMS_Arduino_*` |

### Tìm kiến thức đã distill

- Xem `brain/distilled/` — chứa KB đã verify, test bank chính thức
- Xem `brain/lessons/` — bài học cross-domain (Biology, Math, Physics, AI)

---

## 📚 Thư viện Wiki Chuyên sâu (Advanced Wikis)
*Các file này chứa tri thức đã được tổng hợp và phân loại từ hàng ngàn câu hỏi MCQ.*

| Chủ đề | Phần cứng (Hardware) | Tư duy (Logic) | Trạng thái |
|---|---|---|---|
| **IOT Arduino** | [[WIKI_IOT_Arduino_Hardware]] | [[WIKI_IOT_Arduino_Logic]] | ✅ Hoàn thiện |
| **IOT AI Arduino** | [[WIKI_IOT_AI_Arduino_Hardware]] | [[WIKI_IOT_AI_Arduino_Logic]] | ⚡ Mới tạo |
| **Robotics** | `Pending` | `Pending` | 🔜 Sắp tới |

---

## 📈 Trạng thái Di trú (Migration Status)

| Module | Tình trạng | Ghi chú |
|---|---|---|
| YoloBit (OhStem) D1-D4 | ✅ Hoàn tất | |
| Robotics mBot M1-M2 | ✅ Hoàn tất | |
| AI Arduino D1-D4 | ✅ Hoàn tất | |
| Robotics Rover (5 bộ đề) | ✅ Hoàn tất | |
| GBot / Codey / xBot | 🔜 Pending | Bước tiếp theo |
| Audit Unicode | 🔜 Pending | Rà soát ký tự toàn hệ thống |
| `brain/distilled/` populate | 🔜 Pending | Cần verify wiki → distilled |

---

## 🔗 File cấu hình hệ thống

| File | Vai trò |
|---|---|
| `AGENTS.md` | Swarm Registry, Rules (R1-R13), Manus Commands |
| `CLAUDE.md` | Session context, LOM config |
| `CONTINUITY.md` | Trạng thái qua phiên — đọc khi bắt đầu session |
| `brain/wip.md` | Task đang dở dang — đọc ngay sau index.md |
| `AUDITOR_Protocol.md` | Quy trình Anti-Hallucination |

---

*Index được quản lý bởi @librarian. Mọi thêm/sửa → ghi log vào `brain/log.md`.*
