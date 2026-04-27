# Project Continuity - NoteBookLLM_Br (Swarm Supreme v8.0 - PARA Transition)

## 🏛️ Status: LMS Project Finished & Graph Stabilized (2026-04-27)
- **Current Goal**: Hoàn tất giai đoạn Mining LMS, ổn định hóa Đồ thị tri thức Obsidian và chuẩn bị chuyển đổi sang kiến trúc PARA (Tiago Forte).
- **Architecture**: Hệ thống đã tách biệt rõ rệt giữa **Wiki (Trí tuệ)** và **Test-Bank (Dữ liệu)**. Toàn bộ 2000+ Atoms đã được "trung hòa" để không làm nhiễu Đồ thị.

## ✅ Accomplishments (Session 27/04 - The Great Purification)
- [x] **Graph Purification**: Di chuyển 2010 file trắc nghiệm vào `brain/test-bank/` và trung hòa toàn bộ Wikilinks bên trong.
- [x] **Source Integrity (Rule 14)**: Cập nhật 31 trang Wiki liên kết trực tiếp đến tài liệu `brain/raw/`.
- [x] **Root Clean-up**: Xóa bỏ các tệp tin ma tự sinh (`WIKI_IOT.md`, `Robot_Rover.md`).
- [x] **Encoding Fix**: Sửa lỗi font chữ Tiếng Việt cho `WIKI_INDEX.md`.
- [x] **PARA Implementation Plan**: Đã lập kế hoạch tái cấu trúc thư mục theo PARA (Projects/Areas/Resources/Archives).

## 🔜 Next Steps (Giai đoạn Tái cấu trúc)
- [ ] **Thực thi PARA**: Di chuyển các thành phần Root vào cấu trúc 1-4 của PARA.
- [ ] **Cập nhật AGENTS.md**: Sửa đổi Rule 7 (Depth <= 2) để tương thích với cấu trúc phân cấp mới.
- [ ] **LMS Archiving**: Đưa toàn bộ các scripts Mining cũ vào `4-archive/scripts/` vì dự án LMS đã kết thúc.

## ⚠️ Incidents & Lessons Learned
### [2026-04-27] Bài học về "Chaos Graph" trong Obsidian
- **Vấn đề:** Đồ thị bị rối loạn (hàng ngàn node) dù đã loại trừ thư mục.
- **Nguyên nhân:** Obsidian vẫn render "Unresolved Links" (liên kết đến file chưa tồn tại) và "Orphan Nodes" (file mồ côi) nếu không được tắt trong bộ lọc (Filters).
- **Khắc phục:** Sử dụng script `purge_test_bank_links.py` để trung hòa `[[ ]]` thành ` `` ` (backticks). Hướng dẫn người dùng tắt "Orphans" và bật "Existing files only".
- **Bài học:** Để quản lý Knowledge Graph lớn (>2000 nodes), việc "Trung hòa liên kết" quan trọng hơn việc "Loại trừ thư mục".
