---
title: "PROPOSAL: Reorganizing 3-resources/raw for Wiki 2.0"
type: synthesis
tags: ["Optimization", "Taxonomy", "Raw_Resources"]
status: "draft"
sources:
  - "[[SYNTHESIS_ULTIMATE_Second_Brain_Spec]]"
  - "d:\\NoteBookLLM_Br\\3-resources\\raw\\sources\\"
relationships:
  - type: "governs"
    target: "d:\\NoteBookLLM_Br\\3-resources\\raw\\"
created: "2026-05-02"
---

# Đề xuất tái cấu trúc thư mục Raw (3-resources/raw)

## Hiện trạng
Thư mục `3-resources/raw/sources` hiện chứa 114 tệp tin nằm phẳng (flat list), gây khó khăn cho việc:
- Phân loại nguồn gốc (Provenance).
- Quản lý trạng thái xử lý (Ingest Status).
- Tránh trùng lặp nội dung.

## Giải pháp đề xuất: "The Pipeline-PARA Model"

Tôi đề xuất cấu trúc lai (Hybrid) để tối ưu hóa cho cả Con người (Dễ tìm) và AI (Dễ xử lý).

### 1. Phương án mới: "Prefix-based Flattening" (Tuân thủ Rule 7)
Để đảm bảo không vi phạm Rule 7 (Cấm thư mục con ở cấp 3), chúng ta sẽ không tạo folder mới mà thực hiện **Chuẩn hóa tiền tố tên file**.

- **Vị trí**: Giữ nguyên toàn bộ file tại `3-resources/raw/sources/`.
- **Hệ thống mã Prefix**:
    - `AIMET_`: (AI Methodology) Karpathy, Nashsu, Wiki Gen...
    - `DSML_`: (Data Science) Pandas, Python, Analytics...
    - `STAT_`: (Statistics) Probability, Regression...
    - `SQLDB_`: (SQL & Databases) Snowflake, SQL Cookbook...
    - `VIZ_`: (Visualization) Tableau, Power BI, Storytelling...
    - `METAS_`: (Meta System) METAS_AGENTS.md, Rules, Guides...

### 2. Quy trình Ingest & Quản lý
1. **User** quăng file vào `00_Inbox/`.
2. **Agent** thực hiện lệnh `/wiki ingest`.
3. Sau khi xử lý, **Agent** đổi tên file gốc theo chuẩn Prefix và di chuyển vào `raw/sources/`.

### 3. Ưu điểm
- **Tuân thủ tuyệt đối Rule 7**: Không phát sinh thư mục con.
- **Tốc độ AI**: Agent chỉ cần liệt kê 1 folder là thấy toàn bộ nguồn, dễ dàng grep/search.
- **Thẩm mỹ**: Khi xem trong Obsidian, các file cùng chủ đề sẽ tự động nhóm lại với nhau.

## Kế hoạch thực hiện
1. [ ] Khởi tạo cấu trúc thư mục mới.
2. [ ] Di chuyển các file có prefix rõ ràng (`STAT_`, `VIZ_`, `TOOL_`, `THINK_`, `DE_`, `DSML_`, `PY_`) vào đúng folder.
3. [ ] Phân loại các file PDF chưa có prefix dựa trên nội dung.
4. [ ] Cập nhật `METAS_AGENTS.md` để Agent biết cấu trúc mới.

## User Review Required
> [!IMPORTANT]
> Việc di chuyển file sẽ làm thay đổi đường dẫn vật lý. Tuy nhiên, các trang Wiki hiện tại sử dụng Wikilink (ví dụ: `[[index]]`), nên nếu chúng ta cập nhật metadata trong các trang Source, hệ thống sẽ không bị gãy liên kết.

Bạn có đồng ý với cấu trúc phân loại theo **Chủ đề (Domain)** như trên không?


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
