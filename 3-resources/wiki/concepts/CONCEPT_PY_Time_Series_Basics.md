---
file_id: CONCEPT_PY_TIME_SERIES_BASICS
title: "Time Series Basics (Cơ bản về chuỗi thời gian)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "SOURCE_TOOL_PYTHON_FOR_DATA_ANALYSIS"
  - "SOURCE_STAT_STATISTICS_IN_A_NUTSHELL"
---

## ## For future Claude
Trang này cung cấp các nguyên tử tri thức về xử lý dữ liệu chuỗi thời gian (Time Series) bằng Python, đặc biệt là sử dụng thư viện Pandas. Trong lĩnh vực EdTech, kỹ thuật này được ứng dụng để phân tích tiến độ học tập theo thời gian, dự báo xu hướng đăng ký khóa học và phát hiện các điểm bất thường trong hành vi của học viên.

## ## Key Claims / Summary
1.  **Datetime Objects**: Nền tảng của Time Series là việc sử dụng kiểu dữ liệu `datetime64` trong Pandas để quản lý thời gian một cách chính xác.
2.  **Resampling**: Khả năng chuyển đổi tần suất dữ liệu (ví dụ: từ dữ liệu theo giờ sang dữ liệu theo ngày) là kỹ thuật quan trọng nhất trong phân tích xu hướng.
3.  **Indexing & Slicing**: Sử dụng thời gian làm chỉ mục (Index) cho phép truy xuất dữ liệu cực kỳ linh hoạt (ví dụ: `df['2026-05']`).

## ## Ví dụ đối chiếu (Rule 17)
-   **Ví dụ thực tế (Original)**: `df.resample('M').mean()` - Lệnh này chuyển đổi dữ liệu thô (ví dụ: số lượt đăng nhập mỗi ngày) thành dữ liệu trung bình theo tháng để quan sát sự tăng trưởng dài hạn.
-   **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc bạn quay một bộ phim "Time-lapse" về sự phát triển của một cái cây. Bạn chụp ảnh mỗi phút (Dữ liệu gốc), sau đó bạn chỉ chọn lọc các bức ảnh theo từng tuần để ghép lại thành một đoạn phim ngắn (Resampling), giúp bạn nhìn rõ sự thay đổi mà không bị rối bởi quá nhiều chi tiết nhỏ nhặt hàng ngày.

## ## Detailed Analysis
Các khái niệm quan trọng trong Time Series với Pandas:
- **Timestamp**: Một thời điểm cụ thể (Tương đương với `datetime` của Python).
- **Period**: Một khoảng thời gian (Ví dụ: Tháng 5 năm 2026).
- **Date Range**: Tạo một chuỗi thời gian đều đặn với `pd.date_range()`.
- **Shifting**: Di chuyển dữ liệu tiến hoặc lùi theo thời gian (`df.shift()`) để tính toán sự thay đổi giữa các kỳ.
- **Window Functions**: Tính toán trung bình trượt (`rolling()`) để làm mịn dữ liệu và loại bỏ nhiễu.

## ## Relationships
- `part_of` -> ENTITY_Python
- `uses` -> [[ENTITY_PANDAS]]
- `supports` -> [[CONCEPT_DSML_Model_Evaluation_Metrics]]

## ## Source Tracing
- **Nguồn**: SOURCE_TOOL_PYTHON_FOR_DATA_ANALYSIS — Chapter 11: Time Series.
- **Nguồn**: SOURCE_STAT_STATISTICS_IN_A_NUTSHELL — Section: Seasonal Decomposition.

## ## History / Revisions
- **2026-05-03**: [@engineer] Chuyển đổi từ stub sang verified, bổ sung Rule 17 và Rule 20.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
