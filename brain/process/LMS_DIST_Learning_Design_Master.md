# 🧭 Learning Design Master (v4.4 Supreme)

Bản thiết kế này là kim chỉ nam cho `@engineer` thực hiện việc tinh cất tri thức hàng loạt.

## 📐 Cấu trúc tệp tiêu chuẩn (Standard Template)

Mọi tệp trong `brain/distilled/` BẮT BUỘC tuân theo cấu trúc sau:

```markdown
---
file_id: [PHẢI KHỚP VỚI TÊN FILE]
title: [Tên bài học/Khái niệm]
category: [Atomic Note | Assessment | Guide]
trainer_level: [Entry | Intermediate | Advanced]
bloom_level: [1-6]
source: [[Tên_File_Raw.md]]
status: standardized
---

# [Tiêu đề]

> [!NOTE]
> Phân nhóm: [[Trainer_Profile_Standard]] > [Module tương ứng]

[Nội dung bài học/sự kiện]

## 🔗 Nguồn xác thực (Provenance)
- 📖 Tài liệu gốc: [[Tên_File_Raw.md]]
- 🖋️ Trích đoạn: [Section/Dòng cụ thể]
```

## 🔗 Quy tắc Đan lưới Tri thức (Knowledge Weaving)
1. **Source Linking**: Tuyệt đối không để nguồn ở dạng text. Phải dùng `[[filename.md]]` để linter có thể verify.
2. **Contextual Linking**: Nếu trong nội dung nhắc tới linh kiện (ví dụ: `ESP32`, `Yolo:Bit`), phải link tới tệp Master tương ứng (ví dụ: `[[LMS_KB_IOT]]`).
3. **Double Link Rule**: Mỗi tệp mới tạo ra phải có ít nhất 2 liên kết tới các tệp khác trong hệ thống.

## 🏗️ Phân bổ Module (Knowledge Map)
- **Module M1 (Căn bản)**: Tập trung cho Entry Level (CONV_Atoms_v01 đến v05).
- **Module M2 (Kỹ thuật)**: Tập trung cho Intermediate Level (Volume v06 đến v20).
- **Module M3 (Sư phạm/Hệ thống)**: Tập trung cho Advanced Level (Master files và Volume v21+).

---
*Thiết kế bởi: @designer | Phụ trách Pipeline: Swarm Orchestrator*
