# 🧠 Code Intelligence (PRO)

> **Goal:** Biến việc đọc code thủ công thành truy vấn cấu trúc (Querying). Sử dụng Skeleton Index (<4s) + AST graph + Mermaid diagrams để hiểu thấu đáo mọi codebase từ nhỏ đến siêu lớn.

## 🏗️ The 5-Layer Intelligence Model
| Layer | Name | Tech | Output / Benefit |
|---|---|---|---|
| **L0** | **Topology** | Analysis | Nhận diện ranh giới module & Luồng dữ liệu chính. |
| **L1** | **Skeleton** | Grep/POSIX | `.cm/skeleton.md` (Instant signatures). |
| **L2** | **Graph** | Tree-sitter AST | SQLite DB (Callers/Callees/Impact). |
| **L3** | **Diagram** | Mermaid.js | `.cm/architecture.mmd` (Big picture). |
| **L4** | **Context** | Synthesis | Focused context packet cho LLM. |

## 🚀 Phase 0: Topology & Permission Gate
Trước khi thực hiện bất kỳ truy vấn nào, AI Agent phải:
1. **Permission Gate (cm-identity-guard):**
   - Xác thực danh tính nếu Topology quét qua các thư mục nhạy cảm (`.ssh`, `vault/`, `secrets/`).
2. **Identify Entry Points:** Tìm các file khởi chạy chính (main, index, app).
3. **Map Dependencies:** Đọc `package.json`, `requirements.txt` hoặc tương đương.

## 🛠️ Advanced Intelligence Tools
- `codegraph_search(symbol)`: Tìm symbol theo tên hoặc ý nghĩa.
- `codegraph_callers(func)`: Truy vết ngược những ai gọi hàm này.
- `codegraph_impact(symbol)`: Dự báo những gì sẽ break nếu thay đổi symbol.
- **Recursive Indexing:** Tự động chạy lại `index-codebase.sh` khi phát hiện cấu trúc thư mục thay đổi > 10%.

## 📐 Integration Protocol
1. **cm-start:** Tự động phát hiện quy mô dự án và thiết lập Layer phù hợp.
2. **cm-planning:** Sử dụng `impact_analysis` để cảnh báo rủi ro cao trong plan.
3. **cm-debugging:** Truy vết Root cause thông qua call chain (Callers/Callees).

## 🚨 Quality Gate (Red Flags)
- ❌ Duy trì Index cũ (Stale) → Dẫn đến ảo tưởng về cấu trúc code hiện tại.
- ❌ Quét toàn bộ codebase (>200 files) bằng `list_dir` mà không có Skeleton.
- ❌ Để sót các "Silent dependencies" (phụ thuộc ngầm qua chuỗi string hoặc config).

## 💡 Example Triggers
- "Giải thích cấu trúc project này (Topology)."
- "Kiểm tra Impact Analysis cho việc refactor hàm login."
- "Cập nhật lại Skeleton Index của dự án."
