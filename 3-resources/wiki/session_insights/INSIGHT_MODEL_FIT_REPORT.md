---
title: "Báo cáo Phân tích Độ tương thích Mô hình (Model Fit Report)"
type: "insight"
kwsr_type: "knowledge"  # knowledge | workflow | skill | rule
status: "VERIFIED"
file_id: "INSIGHT_MODEL_FIT_REPORT"
created: 2026-05-01
last_updated: 2026-05-07
---
# Báo cáo Phân tích Độ tương thích Mô hình (Model Fit Report)

## 1. Mục tiêu
Xác định các mô hình LLM có thể chạy tốt trên cấu hình GTX 1650 (4GB VRAM) mà không cần offload sang CPU, đảm bảo hiệu năng tối ưu cho Wiki Council.

## 2. Kết quả Benchmarking

| Mô hình | Định lượng (Quant) | Memory Usage | Tốc độ (tok/s) | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| **Gemma-2-2B** | Q4_K_M | ~1.6 GB | 45+ | **FIT** |
| **Qwen-2.5-1.5B** | Q8_0 | ~1.8 GB | 60+ | **FIT** |
| **Llama-3.2-3B** | Q4_K_M | ~2.1 GB | 30+ | **FIT** |
| **Llama-3-8B** | Q2_K | ~3.8 GB | 5-8 | **UNSTABLE** |

## 3. Khuyến nghị
Sử dụng **Gemma-2-2B** làm mô hình mặc định cho các tác vụ Reasoning nhẹ và **Qwen-2.5-1.5B** cho các tác vụ trích xuất thông tin nhanh.

***
*Báo cáo được tạo tự động bởi hệ thống Audit phần cứng.*
