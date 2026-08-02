# 🎓 EduResearch & Instructional Design Hub (v2.0)

> **Bộ công cụ & Trợ lý AI Chuyên biệt dành cho Nhà Giáo Dục K-12 (Toán & STEM)**  
> Tích hợp quy trình nghiên cứu tổng quan tài liệu (PRISMA 2020), thiết kế giáo án phân hóa 3 mức năng lực, và sáng tác bài tập Toán theo phương pháp Singapore Math CPA.

---

## 🎯 Mục Tiêu Workspace

 Workspace này giúp giáo viên & nhà nghiên cứu giáo dục:
1. **Nghiên cứu & Đánh giá Bằng chứng (Evidence-Based Research)**: Tổng quan tài liệu edtech/AI theo chuẩn PRISMA 2020 từ các cơ sở dữ liệu lớn (ERIC, OpenAIRE, DOAJ, Zenodo).
2. **Thiết kế Bài giảng Phân hóa 3 Mức (Tiered Instruction)**: Soạn giáo án & bài học STEM phân hóa năng lực (Dưới chuẩn / Đạt chuẩn / Vượt chuẩn) theo chuẩn Anthropic K-12 & Bloom Taxonomy.
3. **Thiết kế Bài tập Toán Chuyên sâu (Singapore Math CPA)**: Xây dựng chuỗi bài tập Toán theo các giai đoạn Cụ thể (Concrete) $\rightarrow$ Trực quan (Pictorial / Bar Model) $\rightarrow$ Trừu tượng (Abstract).

---

## 🏗️ Kiến Trúc Thư Mục Chuyên Môn (Domain-Driven Edu Architecture)

```text
EduResearch_Hub/
│
├── 📁 01_NghienCuu_Review/     ← RESEARCH & EVIDENCE (PRISMA 2020, Tổng quan tài liệu, Bằng chứng edtech)
├── 📁 02_Khung_ChuyenMon/      ← STANDARDS & CURRICULUM (Chuẩn Toán K-12, Khung STEM, Bloom Alignment)
├── 📁 03_ThietKe_BaiDay/       ← INSTRUCTIONAL LAB (Giáo án 3 mức, Dự án STEM, Kịch bản giảng dạy)
├── 📁 04_DanhGia_KiemTra/      ← ASSESSMENT & RUBRICS (Ma trận đề thi, Rubrics STEM, AI Feedback Prompts)
├── 📁 05_Kho_NguyenLieu/       ← MEDIA & ASSETS (Tài liệu thô PDF, Sơ đồ minh họa Toán/STEM)
├── 📁 06_LuuTru_Archive/       ← ARCHIVE (Lưu trữ an toàn tài liệu cũ & thiết chế cũ)
├── 📁 workspaces/              ← Xưởng làm việc phụ (learning, dev-lab...)
└── 📁 .agent/skills/           ← Bộ kỹ năng AI chuyên biệt cho Giáo dục
```

---

## 🧰 Bộ Skills Sư Phạm Cốt Lõi (Edu AI Skills)

| Skill | Đường dẫn | Công dụng chính |
|---|---|---|
| **`edu-math-problem-designer`** | [SKILL.md](file:///.agent/skills/edu-math-problem-designer/SKILL.md) | Sáng tác bài tập Toán theo mô hình CPA (Concrete-Pictorial-Abstract) & Singapore Bar Model cho Số học, Đại số, Hình học. |
| **`edu-lesson-designer`** | [SKILL.md](file:///.agent/skills/edu-lesson-designer/SKILL.md) | Soạn giáo án & bài học STEM phân hóa 3 mức năng lực (Dưới/Đạt/Vượt chuẩn) chuẩn K-12. |
| **`edu-prisma-reviewer`** | [SKILL.md](file:///.agent/skills/edu-prisma-reviewer/SKILL.md) | Tổng quan tài liệu nghiên cứu giáo dục theo chuẩn PRISMA 2020 (ERIC, OpenAIRE, DOAJ, Zenodo). |
| **`spec-writer`** | [SKILL.md](file:///.agent/skills/spec-writer/SKILL.md) | Quy trình thiết kế bài học/dự án chuẩn Spec-First (`SPEC.md` $\rightarrow$ `PLAN` $\rightarrow$ `TASKS`). |
| **`course-writer`** | [SKILL.md](file:///.agent/skills/course-writer/SKILL.md) | Tòa soạn biên tập bài viết tiếng Việt chuyên nghiệp. |

---

## 🔒 Quy Tắc Bảo Mật & An Toàn Dữ Liệu

- **Bảo mật đề thi & Tài liệu nội bộ**: Toàn bộ dữ liệu đề thi thật hoặc tài liệu bàn giao đối tác được cách ly tại thư mục `_Delete/` hoặc cấu hình `.gitignore` không commit lên GitHub public.
- **Vệ sinh Repository**: Tự động loại bỏ `node_modules`, các file debug tạm (`*_probe_out`, `*_test.png`), giữ repository siêu nhẹ và sạch sẽ.