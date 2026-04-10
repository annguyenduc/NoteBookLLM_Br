# Schemas for Skills 2.0

Tài liệu này định nghĩa cấu trúc dữ liệu cho các file cấu hình và kết quả trong hệ thống Skill Creator.

## 1. Test Cases (`eval_cases.json`)
```json
[
  {
    "id": "test_01",
    "prompt": "Câu lệnh gửi tới agent...",
    "expected_outcome": "Kết quả mong đợi hoặc các điểm cần có...",
    "assertions": [
      "Có chứa ít nhất 3 dấu gạch ngang",
      "Văn phong chuyên nghiệp",
      "Độ dài từ 500-800 từ"
    ]
  }
]
```

## 2. Evaluation Results (`eval_results.json`)
```json
{
  "skillName": "Tên kỹ năng",
  "version": "A (Gốc) hoặc B (Tối ưu)",
  "metrics": {
    "passRate": "80%",
    "avgTokens": "12,450",
    "avgTime": "14.2s"
  },
  "results": [
    {
      "id": "test_01",
      "prompt": "...",
      "output": "...",
      "grade": "Pass/Fail",
      "feedback": "Phân tích từ Grader agent..."
    }
  ]
}
```
