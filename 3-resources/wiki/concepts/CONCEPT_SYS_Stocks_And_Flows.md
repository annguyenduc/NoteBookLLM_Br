---
file_id: "CONCEPT_SYS_Stocks_And_Flows"
title: "Stocks and Flows (Kho chứa và Dòng chảy)"
type: "concept"
status: "DRAFT"
tags:
  - "Systems_Thinking"
  - "Modeling"
  - "Architecture"
ai-first: true
confidence: 0.9
learning_source: true
source_file: "ARCH_Thinking_in_Systems.pdf"
source_ref: "Chapter 1: The Basics"
last_reconciled: "2026-05-10"
created: "2026-05-10"
last_updated: "2026-05-10"
---

## For future Claude (AI Preamble)
> Trong kỹ thuật phần mềm, Stocks tương đương với "State" (Trạng thái) hoặc "Database", còn Flows tương đương với "Events" hoặc "APIs". Hiểu được sự khác biệt này giúp thiết kế các hệ thống xử lý dữ liệu (Data-Intensive) một cách mạch lạc.

# Stocks and Flows (Kho chứa và Dòng chảy)

## 1. Định nghĩa (Definition)
- **Stock (Kho chứa)**: Là các yếu tố định lượng có thể nhìn thấy, cảm nhận hoặc đếm được của hệ thống tại một thời điểm. Nó tích lũy theo thời gian.
- **Flow (Dòng chảy)**: Là các hành động làm tăng hoặc giảm lượng hàng trong kho chứa (Inflow/Outflow).

## 2. Đặc tính quan trọng (Dynamics)
- **Sự trễ (Delays)**: Stocks thay đổi chậm hơn so với Flows. Điều này tạo ra sự ổn định nhưng cũng gây ra khó khăn trong việc điều chỉnh hệ thống ngay lập tức.
- **Decoupling**: Stocks cho phép Flows vào và Flows ra độc lập với nhau (ví dụ: bộ đệm/buffer).

## 3. Liên hệ kiến trúc (R18: Pedagogical Application)
| Khái niệm hệ thống | Ứng dụng vào Phần mềm/AI |
|---|---|
| **Stock** | **Memory/Context Window** (Thông tin được tích lũy qua các lượt chat). |
| **Inflow** | **User Input/RAG Content** (Dòng thông tin nạp vào). |
| **Outflow** | **Token Decay/Forgetfulness** (Thông tin bị loại bỏ khỏi context). |

## 4. Ví dụ đối chiếu (R18: Double Examples)
### Ví dụ từ nguồn (Original)
> "Stocks are the foundation of any system. They are the accumulations of material or information that has built up over time... Flows are the filling and draining of those stocks." (Meadows, Thinking in Systems).

### Ứng dụng sư phạm (Pedagogical)
Trong một ứng dụng xử lý ảnh hàng loạt:
- **Stock**: Hàng đợi (Queue) các ảnh đang chờ xử lý.
- **Inflow**: User upload ảnh mới.
- **Outflow**: Worker xử lý xong một ảnh.
Nếu Inflow > Outflow, Stock (hàng đợi) sẽ tăng lên, dẫn đến latency cao. Để tối ưu, ta phải tác động vào Flow (tăng số lượng Worker).

## 5. Các khái niệm liên quan (Related Atoms)
- [[CONCEPT_SYS_Feedback_Loops]]: Điều khiển tốc độ của Flows dựa trên trạng thái của Stocks.
- [[CONCEPT_SYS_Leverage_Points]]: Tác động vào Flows thường hiệu quả hơn tác động trực tiếp vào Stocks.

---
*Phiên bản Template V3.0 (Language Aligned).*
