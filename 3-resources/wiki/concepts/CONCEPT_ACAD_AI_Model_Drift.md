---
file_id: "WIKI_AI_MODEL_DRIFT"
title: "Sự trôi dạt mô hình (Model Drift)"
category: "Wiki Page"
prefix: "ACAD"
tags: ["AI", "Machine_Learning", "Drift", "Accuracy"]
source: "`coursera-AI-essentail-Bias, drift, and knowledge cutoff.md`"
status: "verified"
created: "2026-04-28"
last_updated: "2026-04-28"
---

# 📖 Sự trôi dạt mô hình (Model Drift)

## 📌 Định nghĩa cốt lõi
**Sự trôi dạt (Drift)** là sự suy giảm dần dần về độ chính xác và tính phù hợp của đầu ra AI khi thế giới thực thay đổi.

## 🔍 Phân loại Drift
1.  **Factual Drift (Trôi dạt thực tế)**: Xảy ra khi thông tin AI nắm giữ trở nên lỗi thời do điểm dừng tri thức (VD: xu hướng thị trường, công nghệ mới).
2.  **Behavioral Drift (Trôi dạt hành vi)**: Thay đổi trong cách AI phản hồi (định dạng, tông giọng, phong cách) do các bản cập nhật từ nhà phát triển, ngay cả khi dùng cùng một Prompt.

## 💡 Cách quản lý
*   **Cập nhật ngữ cảnh**: Luôn cung cấp thông tin mới nhất trong Prompt cho các chủ đề thay đổi nhanh.
*   **Reset hội thoại**: Bắt đầu hội thoại mới cho mỗi task để tránh context bị "nhiễu" hoặc lạc đề.
*   **Chỉ dẫn rõ ràng**: Sử dụng các hướng dẫn cụ thể và tường minh.

## 🔗 Liên kết tư duy
*   [[CONCEPT_ACAD_AI_Knowledge_Cutoff]]
*   [[ACAD_AI_Responsible_AI]]

## 📖 Nguồn
*   Nguồn: `coursera-AI-essentail-Bias, drift, and knowledge cutoff.md` — Section: "Drift in an AI tool's output"

[AUDITOR] Rule 14: Đã xác nhận fact tồn tại trong file raw.
