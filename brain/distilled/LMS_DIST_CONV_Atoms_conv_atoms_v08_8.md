---
file_id: CONV_Atoms_conv_atoms_v08_8
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v08 8

# Tài liệu Học Tập: Chuyển Đổi Python sang JSON OhStem

## Thông tin chung

| Thuộc tính | Giá trị |
|------------|---------|
| **Tiêu đề** | Chuyển đổi mã Python sang định dạng JSON tương thích OhStem |
| **Môn học** | Lập trình Nhúng & IoT |
| **Khối lớp** | THPT / Đại học |
| **Thời lượng** | 2 tiết học (90 phút) |
| **Loại tài liệu** | Bài giảng thực hành lập trình |
| **Phiên bản** | LOM v4.4 Supreme |

---

## Mục tiêu học tập

Sau bài học này, học viên sẽ:

- **Hiểu** nguyên lý hoạt động của Google Blockly và cách tạo ID duy nhất chuẩn 20 ký tự
- **Phân tích** cấu trúc JSON của OhStem và mối quan hệ giữa biến và khối lệnh
- **Thực hiện** quá trình chuyển đổi từ mã Python sang định dạng JSON tương thích OhStem
- **Áp dụng** các kỹ thuật ánh xạ biến để đảm bảo tính tham chiếu chính xác

---

## Nội dung bài học

### 1. Giới thiệu về Google Blockly và OhStem

Google Blockly là nền tảng lập trình trực quan sử dụng các khối lệnh kéo thả. Mỗi khối lệnh được nhận diện bởi một **ID duy nhất** có độ dài 20 ký tự.

#### Đặc điểm của ID Blockly:
- **Độ dài**: 20 ký tự
- **Ký tự sử dụng**: 92 ký tự bao gồm:
  - Chữ cái in hoa (A-Z)
  - Chữ cái in thường (a-z)  
  - Chữ số (0-9)
  - 30 ký tự đặc biệt: `!@#$%^&*()_+-={};':"\|,.<>/?~``

> **[CONV]** ID của Google Blockly là một chuỗi cố định 20 ký tự, được chọn ngẫu nhiên từ bộ "soup" gồm 92 ký tự (chữ hoa, chữ thường, số và 30 ký tự đặc biệt). [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 2. Phương pháp tạo ID an toàn

Để đảm bảo tính bảo mật và độ ngẫu nhiên cao, chương trình sử dụng module `secrets` thay vì `random` truyền thống.

```python
import secrets
import string

def generate_blockly_uid():
    """Tạo ID 20 ký tự chuẩn Google Blockly."""
    soup = (
        string.ascii_uppercase + 
        string.ascii_lowercase + 
        string.digits +
        "!@#$%^&*()_+-={};':\"\\|,.<>/?~`"
    )
    return ''.join(secrets.choice(soup) for _ in range(20))
```

> **[CONV]** Sử dụng `secrets.choice` là phương pháp tạo ID an toàn và chuẩn xác hơn so với `random.choice` khi mô phỏng trình tạo ID của Blockly. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 3. Cấu trúc JSON của OhStem

Cấu trúc JSON của OhStem bao gồm hai phần chính:

#### 3.1. Phần biến (Variables)
```json
{
  "variables": [
    {
      "name": "STATE_WAITING",
      "id": "abc123..."
    }
  ]
}
```

#### 3.2. Phần khối lệnh (Blocks)
```json
{
  "blocks": {
    "languageVersion": 0,
    "blocks": [
      {
        "type": "variables_set",
        "id": "xyz789...",
        "fields": {
          "VAR": {"id": "abc123..."}
        },
        "inputs": {
          "VALUE": {
            "shadow": {
              "type": "math_number",
              "fields": {"NUM": "0"}
            }
          }
        }
      }
    ]
  }
}
```

> **[CONV]** Trong cấu trúc JSON của OhStem, sự khác biệt giữa biến và khối lệnh được xác định bằng vị trí ngữ nghĩa trong file, không phải bằng định dạng ID (ID là phổ quát cho mọi thực thể). [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài tập thực hành

### Worksheet 1: Phân tích mã nguồn chuyển đổi

**Họ và tên:** _________________________  
**Lớp:** _________________________  
**Ngày:** _________________________

#### Câu 1: Phân tích hàm `generate_blockly_uid()`
a) Module nào được sử dụng để tạo ID an toàn?  
**Trả lời:** _________________________

b) Bộ ký tự "soup" chứa bao nhiêu ký tự tổng cộng?  
**Trả lời:** _________________________

c) Tại sao không sử dụng `random.choice` mà dùng `secrets.choice`?  
**Trả lời:** _________________________

#### Câu 2: Hiểu về ánh xạ biến
a) Biến `var_mapping` trong chương trình dùng để làm gì?  
**Trả lời:** _________________________

b) Tại sao cần duy trì sơ đồ ánh xá giữa tên biến Python và ID Blockly?  
**Trả lời:** _________________________

> **[CONV]** Việc duy trì một sơ đồ ánh xạ (Mapping) giữa tên biến trong Python và ID Blockly là bắt buộc để đảm bảo tính tham chiếu chính xác khi tạo các khối lệnh. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Quiz kiểm tra kiến thức

### Câu hỏi trắc nghiệm

**Câu 1:** ID của Google Blockly có độ dài bao nhiêu ký tự?
- A. 16 ký tự
- B. 20 ký tự  
- C. 24 ký tự
- D. 32 ký tự

**Câu 2:** Module nào nên sử dụng để tạo ID an toàn cho Blockly?
- A. `random`
- B. `uuid`
- C. `secrets`  
- D. `hashlib`

**Câu 3:** Trong JSON OhStem, sự khác biệt giữa biến và khối lệnh được xác định bởi:
- A. Định dạng ID
- B. Vị trí ngữ nghĩa trong file  
- C. Loại dữ liệu
- D. Độ dài chuỗi

### Câu hỏi tự luận

**Câu 4:** Giải thích tại sao việc duy trì ánh xá giữa tên biến Python và ID Blockly lại quan trọng trong quá trình chuyển đổi?

---

## Scenario thực tiễn

### Tình huống: Chuyển đổi dự án Rover từ Python sang OhStem

**Bối cảnh:** Bạn là kỹ sư phần mềm đang phát triển hệ thống điều khiển robot Rover. Dự án hiện tại viết bằng Python sử dụng mô hình máy trạng thái (state machine) với các hằng số như `STATE_WAITING`, `STATE_MOVING`, `STATE_STOPPED`. Bây giờ bạn cần chuyển đổi sang môi trường OhStem để học sinh có thể học và thử nghiệm dễ dàng hơn.

**Yêu cầu:**
1. Phân tích cấu trúc Python hiện tại
2. Thiết kế sơ đồ ánh xạ biến
3. Tạo mã chuyển đổi phù hợp
4. Kiểm thử với môi trường OhStem

**Gợi ý:** Sử dụng mã nguồn mẫu đã cung cấp, điều chỉnh các kiểu khối (`type`) để phù hợp với thư viện cảm biến/động cơ của Rover trên OhStem.

---

## Tài nguyên hỗ trợ

- ![Minh họa cấu trúc JSON](../../brain/raw/lms_multi_media_dump/assets/volume_v08_image1.png)
- ![Sơ đồ chuyển đổi Python sang JSON](../../brain/raw/lms_multi_media_dump/assets/volume_v08_image2.png)
- [Tài liệu API OhStem](https://app.ohstem.vn/api-docs)
- [Thư viện khối lệnh OhStem](https://app.ohstem.vn/library)

---

## Đánh giá và phản hồi

| Tiêu chí | Mức độ đạt được | Ghi chú |
|----------|----------------|---------|
| Hiểu nguyên lý ID Blockly | □ Tốt □ Khá □ Trung bình | |
| Viết được hàm tạo ID | □ Có □ Không | |
| Phân tích cấu trúc JSON | □ Có □ Không | |
| Thực hiện chuyển đổi | □ Có □ Không | |

**Ghi chú của giáo viên:**  
_________________________________________________________________
_________________________________________________________________

---

## Ghi chú bản quyền

Tài liệu này thuộc về chương trình đào tạo LOM v4.4 Supreme.  
Tất cả nội dung đều có dẫn nguồn đầy đủ theo quy chuẩn [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).