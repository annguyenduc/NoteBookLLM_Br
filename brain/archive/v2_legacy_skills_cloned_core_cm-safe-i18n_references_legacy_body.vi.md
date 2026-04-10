# 🌐 Safe i18n Translation (LITE)

> **Goal:** Chuyển đổi ngôn ngữ an toàn tuyệt đối cho hệ thống (i18n), ngăn chặn các lỗi vỡ giao diện (UI crash), lỗi logic hoặc sai lệch định dạng mã nguồn.

## 🚧 The Iron Rules (BẮT BUỘC)
- **Batch Limit:** Tối đa **30 strings** mỗi đợt. Không làm nhiều hơn.
- **No Autoplay:** Không bao giờ tự động thay đổi nếu chưa qua kiểm tra.
- **HTML Protection:** Chỉ dịch nội dung văn bản (Text content), KHÔNG chạm vào thẻ HTML/Attributes.
- **Key Parity:** Tất cả các file ngôn ngữ phải có số lượng Key bằng nhau tuyệt đối.

## 🚀 8-Gate Audit Lifecycle
| Gate | Check | Command | Pass Criteria |
|---|---|---|---|
| **1-2** | Syntax (JS/All) | `node -c app.js` | No syntax errors. |
| **3** | Corruption | `grep` pattern check | 0 matches for broken strings. |
| **4** | Delimiters | Mismatched quotes | 0 matches (Mixed delims). |
| **5** | HTML Integrity| Broken tags space | 0 matches (< div, </ div). |
| **6** | Shadowing | `t` variable check | 0 matches in map/filter. |
| **7** | JSON Valid | `JSON.parse` | Valid JSON structure. |
| **8** | Full Test | `npm run test:gate`| 0 failures. |

## 📐 Translation Sync Rules
- **Placeholders:** Giữ nguyên `{{param}}` tuyệt đối, không dịch bên trong dấu ngoặc.
- **Tech Terms:** KHÔNG dịch các thuật ngữ kỹ thuật (KPI, PPH, CSV).
- **Parallel Sync:** Sau khi file chính (vi.json) chuẩn, dịch các file khác song song.

## 🚨 Quality Gate (Red Flags)
- ❌ Dùng Regex để sửa lỗi Regex (Bắt buộc dùng Lexical Scanner).
- ❌ Thiếu kiểm tra Key Parity sau khi dịch xong.
- ❌ Placeholder bị thay đổi hoặc dịch sang ngôn ngữ đích (Gây lỗi runtime).
- ❌ Bỏ qua bất kỳ Gate nào trong bộ 8 cổng kiểm soát.

## 💡 Example Triggers
- "Dịch toàn bộ file blog sang tiếng Anh và Thái Lan."
- "Extract các string cứng trong app.js sang i18n."
- "Kiểm duyệt (Audit) lại file vi.json và en.json."
