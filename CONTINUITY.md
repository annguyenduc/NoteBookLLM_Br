# CONTINUITY.md

## Current Objective

Hoàn thiện và kiểm nghiệm tính năng xuất bản sách tự động đa định dạng (HTML & EPUB Reader) cho nguồn ARCH_TIS theo lộ trình học tập cá nhân hóa, đồng thời tinh giản mục lục và làm nhỏ tiêu đề phù hợp với thiết bị di động.

## Current State

- **Trạng thái**: Đã hoàn thành 100% việc lập trình, tối ưu CSS, tinh giản mục lục, biên dịch thành công và đóng gói tính năng thành Skill mới.
- **Nhánh làm việc**: `agent/20260522-export-reader` tại Git worktree `D:\_agent_worktrees\20260522_export_reader`.
- **Thay đổi chính**:
  1. Xây dựng script `export_epub.py` điều phối xuất bản đồng thời HTML và EPUB.
  2. Sắp xếp các Atom theo đúng thứ tự logic trong lộ trình học tập cá nhân hóa tại `5-learning/paths/`.
  3. Làm sạch mục lục (TOC) chỉ giữ tên Atom tiếng Việt tinh gọn, loại bỏ ID và chú thích tiếng Anh rườm rà.
  4. Đổi `toc_depth` thành `1` cho EPUB để loại bỏ toàn bộ các H2 phụ (như `For future Claude (AI Preamble)`) ra khỏi mục lục của EPUB khi đọc trên Apple Books.
  5. Khắc phục lỗi lặp tiêu đề H1 bằng cách loại bỏ tiêu đề H1 trong thân bài Atom nguồn.
  6. Giảm kích thước font chữ tiêu đề (H1, H2, H3) trong CSS của cả EPUB và HTML (bổ sung `.reader-content` cho thân bài HTML Reader) để tối ưu hiển thị trên màn hình iPad/iPhone.
  7. Nhúng trực tiếp toàn bộ CSS và JS vào HTML Reader giúp nó trở thành một file độc lập chạy offline mượt mà.
  8. Đóng gói toàn bộ tính năng và quy trình biên dịch này thành một Skill chính thức: `wiki-export-reader` tại `.agent/skills/wiki-export-reader/`.

## Next Step For AN

1. **Nghiệm thu thủ công**:
   - Mở file [LEARNING_PACK_SOURCE_ARCH_TIS_Thinking_in_Systems.html](file:///D:/_agent_worktrees/20260522_export_reader/5-learning/packs/html/LEARNING_PACK_SOURCE_ARCH_TIS_Thinking_in_Systems.html) bằng Safari/Chrome di động để xác nhận giao diện premium và mục lục tinh giản.
   - Chuyển file [LEARNING_PACK_SOURCE_ARCH_TIS_Thinking_in_Systems.epub](file:///D:/_agent_worktrees/20260522_export_reader/5-learning/packs/epub/LEARNING_PACK_SOURCE_ARCH_TIS_Thinking_in_Systems.epub) sang ứng dụng Apple Books trên iPad/iPhone để kiểm tra giao diện đọc sách.
2. **Merge nhánh vào main**: AN kiểm tra lại và merge nhánh `agent/20260522-export-reader` vào `main`.
3. **Dọn dẹp worktree (Tùy chọn)**:
   ```bash
   git worktree remove D:\_agent_worktrees\20260522_export_reader --force
   git branch -D agent/20260522-export-reader
   ```

## Blockers

- Không có blockers.
