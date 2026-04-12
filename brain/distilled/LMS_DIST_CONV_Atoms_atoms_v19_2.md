---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v19_2
  title: atoms_v19_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu RAW (Volume v19) liên quan đến kỹ thuật lập trình Google Apps Script và quy trình quản lý hệ thống học tập:

- **Fact:** Trong Google Apps Script, đối tượng `sourceSlide` không có phương thức `duplicate()` trực tiếp để sao chép một trang slide đơn lẻ.
- **Source:** Đoạn "Lỗi 'TypeError: sourceSlide.duplicate is not a function' xảy ra khi đối tượng sourceSlide không có phương thức duplicate."
- **Tag:** [vv19]

- **Fact:** Để sao chép slide giữa các bản trình diễn khác nhau, cần sử dụng phương thức `appendSlide()` kết hợp với `getLayout()` của