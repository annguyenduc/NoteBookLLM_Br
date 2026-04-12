---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v22_4
  title: CONV_atoms_v22_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật trích xuất từ nguồn dữ liệu về nhiệm vụ khám phá sao Hỏa (Robotics & AI) và giải pháp Google Apps Script cho yêu cầu của bạn.

### I. TRÍCH XUẤT THÔNG TIN KỸ THUẬT (FACTS)

- **Fact:** [CONV] Robot tự hành (Rover) thực hiện lấy mẫu lõi đá (rock core sample) bằng mũi khoan và lưu trữ trong ống mẫu để gửi về Trái Đất trong tương lai.
- **Source:** (v22 - Đoạn: 1:00 - 1:06)
- **Tag:** [vv22]

- **Fact:** [CONV] Trực thăng Ingenuity là thiết bị bay có động cơ đầu tiên thực hiện chuyến bay trên một hành tinh khác ngoài Trái Đất.
- **Source:** (v22 - Đoạn: 1:30 - 1:39)
- **Tag:** [vv22]

- **Fact:** [CONV] Hệ thống điều khiển trực thăng phải có khả năng thích nghi (adapt) với các thay đổi của môi trường trên sao Hỏa để duy trì hoạt động bay.
- **Source:** (v22 - Đoạn: 1:43 - 1:46)
- **Tag:** [vv22]

- **Fact:** [CONV] Robot sử dụng các cảm biến và hệ thống lấy mẫu để phân tích dấu hiệu của sự sống cổ đại (ancient life) tại khu vực Jezero Crater.
- **Source:** (v22 - Đoạn: 1:25 - 2:13)
- **Tag:** [vv22]

- **Fact:** [CONV] Việc vận hành xe tự hành (Rover) trên địa hình mới (vùng Delta) đòi hỏi khả năng điều hướng và vượt qua các thách thức địa hình phức tạp.
- **Source:** (v22 - Đoạn: 2:16 - 2:34)
- **Tag:** [vv22]

---

### II. GIẢI PHÁP GOOGLE APPS SCRIPT (NÂNG CAO)

Để thêm dấu ` - ` trước nhiều từ khác nhau cùng một lúc, cách tối ưu nhất là sử dụng **Biểu thức chính quy (Regular Expression - Regex)** với toán tử `|` (nghĩa là "hoặc").

Dưới đây là mã nguồn đã được tối ưu:

```javascript
function addHyphenBeforeMultipleWords() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var range = sheet.getRange("A1"); // Bạn có thể đổi thành vùng chọn khác
  var cellValue = range.getValue();
  
  // Danh sách các từ bạn muốn thêm dấu gạch ngang phía trước
  // Các từ cách nhau bởi dấu gạch đứng |
  // Ví dụ: [Nêu], [Giải thích], [Phân tích]
  var wordsToMatch = /\[Nêu\]|\[Giải thích\]|\[Phân tích\]/g;

  // Sử dụng hàm replace với Regex
  // match là từ tìm thấy, sẽ được thay bằng " - " + chính nó
  var newValue = cellValue.replace(wordsToMatch, function(match) {
    return " - " + match;
  });

  range.setValue(newValue);
}
```

**Giải thích kỹ thuật:**
1.  **`/ ... /g`**: Đây là ký hiệu của Regex. Chữ `g` (global) cực kỳ quan trọng, nó giúp tìm và thay thế **tất cả** các vị trí khớp trong ô, thay vì chỉ vị trí đầu tiên.
2.  **`|`**: Đây là toán tử "HOẶC". Bạn có thể thêm bao nhiêu từ tùy thích vào giữa các dấu `|`.
3.  **`\[` và `\]`**: Vì dấu ngoặc vuông là ký tự đặc biệt trong lập trình, ta cần thêm dấu gạch chéo ngược `\` phía trước để máy hiểu bạn đang tìm chính xác ký tự `[` đó.
4.  **Hàm Callback `function(match)`**: Giúp giữ nguyên từ gốc (dù là "Nêu" hay "Giải thích") và chỉ chèn thêm chuỗi `" - "` vào phía trước.

**Cách sử dụng:**
- Bạn chỉ cần sửa dòng `var wordsToMatch = /từ_1|từ_2|từ_3/g;` theo đúng các từ bạn cần.
- Nếu muốn không phân biệt chữ hoa chữ thường, hãy dùng `/.../gi` (thêm chữ `i`).