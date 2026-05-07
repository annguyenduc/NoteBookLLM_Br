---
file_id: CONCEPT_META_ATOMIC_METHODOLOGY
title: "Atomic Methodology (Phương pháp luận Wiki Hạt nhân)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_LLM_WIKI]]"
  - "SOURCE_META_KARPATHY_LLM_WIKI"
---

## ## For future Claude
Trang này định nghĩa triết lý cốt lõi của NoteBookLLM_Br: Tính hạt nhân (Atomicity). Bằng cách chia nhỏ tri thức thành các đơn vị độc lập và tự giải thích, chúng ta tối ưu hóa khả năng truy xuất của RAG và giảm thiểu sự nhiễu loạn thông tin cho Agent. Đây là điều kiện tiên quyết để xây dựng một "Bộ não thứ hai" thực sự hiệu quả.

## ## Key Claims / Summary
1.  **Granular Knowledge**: Mỗi trang chỉ giải quyết một khái niệm duy nhất để tránh loãng context.
2.  **Autonomous Nodes**: Các node tri thức phải có khả năng tự giải thích mà không phụ thuộc quá nhiều vào ngữ cảnh của trang mẹ.
3.  **High Reuse**: Tính hạt nhân cho phép tái sử dụng tri thức trong nhiều ngữ cảnh khác nhau (Synthesis/Case Studies).

## ## Detailed Analysis

# Phương pháp luận Wiki Hạt nhân (Atomic)

## 1. Định nghĩa & Triết lý Cốt lõi
Wiki Hạt nhân là cách tiếp cận quản trị tri thức trong đó mỗi trang Wiki chỉ chứa một khái niệm duy nhất, độc lập và có ý nghĩa hoàn chỉnh.

**Ẩn dụ "Second Brain 3.0" (Karpathy Pattern):**
> "Obsidian là **IDE**; LLM là **lập trình viên**; Wiki là **mã nguồn (codebase)**."
- Tri thức không còn là văn bản tĩnh, mà là các "module code" có thể được biên dịch, kiểm tra và liên kết chéo.

## 2. Kiến trúc 3 Tầng (Three-Layer Architecture)
Để duy trì tính hạt nhân bền vững, hệ thống được cấu trúc thành 3 lớp riêng biệt:
1.  **Raw Sources (Lớp Thô)**: Bất biến (Immutable). Chứa PDF, bài báo, repository. LLM chỉ đọc, không ghi.
2.  **Wiki (Lớp Biên dịch)**: Do LLM sở hữu hoàn toàn. Chứa các bản tóm tắt, concept nguyên tử và liên kết chéo.
3.  **Schema (Lớp Quy tắc)**: Định nghĩa "luật chơi" (ví dụ: `AGENTS.md`). Đây là bộ nhớ ổn định giúp Agent duy trì kỷ luật wiki qua nhiều phiên làm việc.

## 3. Nguyên lý vận hành
- **Single Responsibility**: Một trang, một nhiệm vụ.
- **Decontextualization**: Thông tin được viết sao cho có thể hiểu được mà không cần đọc trang trước đó.
- **Granularity**: Độ chi tiết vừa đủ để LLM có thể xử lý trong một cửa sổ ngữ cảnh nhỏ.
- **Compounding Knowledge**: Tri thức được "biên dịch" một lần và tích lũy theo thời gian, thay vì phải khám phá lại từ đầu như mô hình RAG truyền thống.

## 4. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ Công nghệ (Original)
> **Bối cảnh**: Quản lý một repository mã nguồn lớn.
> **Ứng dụng**: Thay vì viết một file `utils.py` dài 5000 dòng, chúng ta chia nhỏ thành các module hạt nhân: `date_utils.py`, `string_utils.py`, `auth_utils.py`. Khi cần sửa logic ngày tháng, chúng ta chỉ tác động vào một "atom" duy nhất mà không làm hỏng toàn bộ hệ thống.
> **Nguồn**: SOURCE_META_KARPATHY_LLM_WIKI — Section: Idea Files.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Thiết kế bài giảng STEAM về Robotics.
> **Ứng dụng**: Thay vì tạo một file dài về "Lập trình mBot", hãy chia nhỏ thành các Wiki Atoms: "Khối lệnh di chuyển", "Cảm biến siêu âm", "Vòng lặp vô hạn". Điều này giúp giáo viên dễ dàng lấy từng module để lắp ghép vào các giáo án khác nhau, giống như việc tái sử dụng các thư viện code trong lập trình.


## ## Source Tracing
- **Nguồn**: [[SOURCE_META_LLM_WIKI]] — Section: Atomicity 1.2.
- **Nguồn**: SOURCE_META_KARPATHY_LLM_WIKI — Concept: Expert Persona & Low Friction.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
