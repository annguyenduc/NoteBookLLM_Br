# Analysis: ARCH_Operating_Systems_Three_Easy_Pieces.pdf
**Nguồn**: `00_Inbox/ARCH_Operating_Systems_Three_Easy_Pieces.pdf`
**Phân tích bởi**: @scout | **Ngày**: 2026-05-11

## Mining Stats
| Chỉ số | Số lượng |
|:---|:---:|
| Key Concepts phát hiện | ~50 (Dự kiến) |
| Entities phát hiện | ~20 (Dự kiến) |
| Connections với wiki hiện tại | Đang phân tích... |
| Atoms đề xuất tạo mới | ~30 (Dự kiến) |

## Tóm tắt cốt lõi
Cuốn sách "Operating Systems: Three Easy Pieces" (OSTEP) tập trung vào ba khái niệm cốt lõi của hệ điều hành:
1. **Virtualization**: Cách hệ điều hành tạo ra ảo giác về các tài nguyên riêng biệt cho từng chương trình (CPU, Memory).
2. **Concurrency**: Cách xử lý nhiều tác vụ đồng thời và các vấn đề liên quan (Locks, Semaphores, Condition Variables).
3. **Persistence**: Cách lưu trữ dữ liệu lâu dài và đáng tin cậy (File Systems, I/O Devices, RAID).

## Atoms đề xuất

### Concepts (wiki/concepts/)
- [ ] `ARCH_Process_Abstraction.md` — Khái niệm tiến trình và cách OS quản lý nó.
- [ ] `ARCH_Address_Space.md` — Mô hình không gian địa chỉ và ảo hóa bộ nhớ.
- [ ] `ARCH_Scheduling_Policies.md` — Các thuật toán điều phối CPU (FIFO, SJF, RR, MLFQ).
- [ ] `ARCH_Paging_Segmentation.md` — Các kỹ thuật quản lý bộ nhớ phân trang và phân đoạn.
- [ ] `ARCH_Locking_Mechanisms.md` — Các cơ chế khóa và đồng bộ hóa.

### Entities (wiki/entities/)
- [ ] `ENTITY_Remzi_Arpaci_Dusseau.md` — Tác giả chính của cuốn sách.
- [ ] `ENTITY_Andrea_Arpaci_Dusseau.md` — Đồng tác giả.
- [ ] `ENTITY_UNIX_Operating_System.md` — Hệ điều hành tham chiếu chính trong sách.

### Source Summary (wiki/sources/)
- [ ] `SOURCE_ARCH_OSTEP.md` — Tóm tắt toàn bộ cuốn sách và cấu trúc 3 phần.

## Connections với Wiki hiện tại
- `[[CONCEPT_ARCH_Kernel_Abstraction]]` — OSTEP cung cấp chi tiết sâu hơn về cách Kernel thực hiện các abstraction này.
- `[[CONCEPT_ARCH_Privileged_Instructions]]` — Giải thích cơ chế chuyển đổi mode (Trap, Return-from-trap).

## Mâu thuẫn (Contradictions & Tensions)
- Đang chờ kết quả HD Conversion để so sánh chi tiết với các Atoms hiện tại về "Kernel Abstraction".

## Master Files cần bồi đắp (Rule 3)
- `wiki/synthesis/ARCH_OS_Fundamentals.md` — Section về Virtualization và Concurrency.

## ⏸️ CHỜ USER DUYỆT (Giai đoạn HD Conversion)
- Hiện tại hệ thống đang thực hiện chuyển đổi PDF sang Markdown HD (Docling).
- Sau khi có kết quả chunking, mình sẽ cập nhật chi tiết mining stats.
