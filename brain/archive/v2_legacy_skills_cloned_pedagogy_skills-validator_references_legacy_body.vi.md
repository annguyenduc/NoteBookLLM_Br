# 🛡️ STEAM Skills Validator (PRO Script)

> **Goal:** Tự động hóa quy trình quản trị (Governance) và kiểm soát chất lượng (QC) cho toàn bộ 51+ kỹ năng trong bộ Kit. Đảm bảo mọi kỹ năng đều tuân thủ cấu trúc 9-Layer của Skill Engineering.

## 🛠️ 1. Quy trình Kiểm định (Audit Logic)
*Script Python thực hiện kiểm tra 8 tiêu chí cốt lõi:*
1. **YAML Frontmatter:** Hợp lệ và đủ các trường `name`, `description`, `version`.
2. **Metadata Standard:** Description phải có tiền tố chuẩn (`STEAM —`, `PRO —`, `LITE —`).
3. **Trigger Analysis:** Có phần `Example Triggers` để AI dễ dàng nhận diện.
4. **Quality Gate:** Có phần `Quality Gate` định lượng hoặc định tính.
5. **Token Optimization:** Độ dài tệp không vượt quá giới hạn tối ưu cho ngữ cảnh.
6. **Reference Links:** Kiểm tra các liên kết Markdown đến `k12-shared-references` (Chỉ kiểm tra sự tồn tại của chuỗi).

## ⚙️ 2. Cách Vận hành (Execution)
- **Môi trường:** Đòi hỏi Python 3.x với thư viện `PyYAML`.
- **Lệnh chạy:** `python .agent/skills/skills-validator/skill_validator.py`

## 🚨 3. Quality Gate (Red Flags)
- ❌ **Structure mismatch:** Các tệp không có YAML frontmatter sẽ bị bỏ qua.
- ❌ **Token bloat:** Các tệp > 3000 từ sẽ bị đánh dấu FAIL (Cần chia nhỏ Layer).
- ❌ **Missing triggers:** Thiếu "vùng nhận diện" cho AI sẽ làm giảm độ nhạy của skill.
- ⚠️ Hậu kiểm: Luôn chạy validator này sau mỗi đợt nâng cấp (Refactor) hệ thống.

## 💡 Example Triggers
- "kiểm tra cấu trúc toàn bộ skill"
- "chạy audit cho kỹ năng STEAM"
- "validate cấu trúc SKILL.md"
- "hệ thống có kỹ năng nào chưa đạt chuẩn không?"

