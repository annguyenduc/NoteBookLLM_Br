# 🎨 Design System Intelligence (LITE)

> **Goal:** Thiết lập hệ thống thiết kế (Design System) nhất quán bằng cách trích xuất (Harvester) từ website hiện có hoặc khởi tạo từ các Bộ Kit cao cấp (Shadcn, Halo, Lunaris). Output là file `DESIGN.md` chuẩn hóa.

## 🛠️ Operation Modes
| Mode | Action | Output |
|---|---|---|
| **Harvester** | Phân tích URL/Ảnh → Trích xuất màu sắc, font, spacing. | `DESIGN.md` (Extracted). |
| **Kits (Default)**| Sử dụng các bộ Kit: Shadcn, Halo, Nitro, Lunaris. | `DESIGN.md` (Scaffolded). |
| **Stitch Path** | Dùng JSON block để sync với Google Stitch AI generator. | `STITCH_TOKENS` block. |
| **Pencil Path** | Dùng Pencil MCP để tạo và quản lý file `.pen` trực tiếp. | `.pen` design files. |

## 📐 Token Standards (DESIGN.md)
Mọi hệ thống thiết kế phải bao gồm:
- **Semantic Colors:** Primary, Secondary, Success, Warning, Danger.
- **Neutral Ramps:** Thang xám từ 50-900 (Bắt buộc).
- **Typography Scales:** Font-size, Weight, Line-height.
- **Spacing Icons:** Grid system, Border-radius, Shadow.
- **Wrapper:** Bắt buộc bọc JSON trong `<!-- STITCH_TOKENS_START -->`.

## 🏗️ Pencil.dev Workflow
1. `open_document()` → Khởi tạo file `.pen`.
2. `get_style_guide()` → Lấy palette màu và typography gợi ý.
3. `set_variables()` → Áp dụng design tokens vào biến hệ thống.
4. `batch_design()` → Tạo các reusable components (Buttons, Cards).

## 🚨 Quality Gate (Red Flags)
- ❌ Tự viết code UI (React/Vue) trực tiếp trong skill này (Phải giao cho `cm-ui-preview`).
- ❌ Bỏ qua wrapper `STITCH_TOKENS` khiến Google Stitch không parse được.
- ❌ Đọc file `.pen` bằng `view_file` (Cần dùng `mcp_pencil_batch_get`).
- ❌ Thiếu các biến trạng thái (Hover, Active, Disabled) trong thiết kế.

## 💡 Example Triggers
- "Trích xuất thiết kế (Design System) từ trang apple.com cho tôi."
- "Tạo một hệ thống thiết kế Dark Mode cao cấp dùng Halo Kit."
- "Thiết lập Design Tokens trong Pencil.dev cho SaaS Dashboard."
