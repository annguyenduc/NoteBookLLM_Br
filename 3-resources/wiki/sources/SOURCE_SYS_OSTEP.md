---
file_id: "SOURCE_SYS_OSTEP"
title: "Operating Systems: Three Easy Pieces"
type: "source"
status: "VERIFIED"
tags:
  - "OS"
  - "Kernel"
  - "Architecture"
ai-first: true
confidence: 1.0
source_type: "pdf"
author: "Remzi Arpaci-Dusseau, Andrea Arpaci-Dusseau"
url: "https://ostep.org"
publisher: "Arpaci-Dusseau Books"
last_reconciled: "2026-05-11"
created: "2026-05-11"
last_updated: "2026-05-11"
---

## For future Claude (AI Preamble)
> Đây là một trong những giáo trình kinh điển và phổ biến nhất về Hệ điều hành hiện nay. Tài liệu này cung cấp cái nhìn sâu sắc về các cơ chế cơ bản của OS thông qua ba khái niệm chính: Ảo hóa (Virtualization), Đồng thời (Concurrency) và Lưu trữ (Persistence). Giá trị cốt lõi của nó nằm ở cách giải thích đơn giản nhưng kỹ thuật, đi kèm với các ví dụ code thực tế.

# Operating Systems: Three Easy Pieces

## 1. Executive Summary
Cuốn sách "Operating Systems: Three Easy Pieces" (OSTEP) giới thiệu các nguyên lý cơ bản của hệ điều hành hiện đại. Cách tiếp cận của tác giả tập trung vào việc giải quyết các vấn đề thiết kế thông qua ba "mảnh ghép" đơn giản:
- **Virtualization**: Biến một tài nguyên vật lý (như CPU hoặc bộ nhớ) thành một dạng ảo, cho phép nhiều chương trình chạy như thể chúng có toàn quyền truy cập vào tài nguyên đó.
- **Concurrency**: Giải quyết các thách thức khi nhiều dòng lệnh thực thi cùng lúc và chia sẻ dữ liệu (Race conditions, Deadlocks).
- **Persistence**: Đảm bảo dữ liệu được lưu trữ an toàn trên các thiết bị lưu trữ không bay hơi (I/O, File Systems, RAID).

## 2. Các chủ đề chính (Key Topics Indexed)
- [[CONCEPT_ARCH_Process_Abstraction]]: Cách OS quản lý các chương trình đang chạy.
- [[CONCEPT_ARCH_Address_Space]]: Cơ chế ảo hóa bộ nhớ.
- [[CONCEPT_ARCH_Scheduling]]: Các thuật toán điều phối tài nguyên.
- [[CONCEPT_ARCH_Locking]]: Đồng bộ hóa tiến trình và luồng.
- [[CONCEPT_ARCH_File_Systems]]: Cấu trúc và quản lý dữ liệu trên đĩa.

## 3. Đánh giá chất lượng (Source Audit)
- **Tính cập nhật**: Tài liệu liên tục được cập nhật bởi tác giả (bản online miễn phí).
- **Độ tin cậy**: Rất cao, được sử dụng làm giáo trình tại nhiều đại học hàng đầu thế giới (Wisconsin-Madison).
- **Mức độ bao phủ**: Toàn diện về các nguyên lý cơ bản của OS, đặc biệt mạnh về cơ chế thực thi.

## 4. Ghi chú bổ sung
- Tài liệu đã được HD-Converted sang Markdown và chia thành 4 chunks để dễ dàng atomization.
- Chứa nhiều sơ đồ và ví dụ code C/UNIX quan trọng.
