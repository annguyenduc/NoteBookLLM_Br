---
title: "ENTITY: Lightpanda Browser"
type: entity
tags: ["Tool", "Browser", "Automation", "Scraping", "Performance", "Zig"]
status: "verified"
created: "2026-05-02"
---

# Lightpanda Browser

## 1. Định nghĩa
**Lightpanda** là một trình duyệt mã nguồn mở được viết hoàn toàn bằng ngôn ngữ **Zig**. Khác với Chromium hay Firefox, Lightpanda được xây dựng từ đầu để tối ưu cho việc tự động hóa và trích xuất dữ liệu (Scraping), loại bỏ các thành phần không cần thiết như GPU rendering hay Media decoding.

## 2. Đặc điểm kỹ thuật
- **Hiệu năng**: Nhanh gấp **9x - 60x** so với Headless Chrome truyền thống.
- **Tài nguyên**: Tiêu thụ RAM/CPU cực thấp do không phải render GUI.
- **Giao thức**: Hỗ trợ đầy đủ **CDP (Chrome DevTools Protocol)**, giúp tương thích tốt với Playwright và Puppeteer.
- **Hệ điều hành**: Chạy tốt nhất trên Linux. Trên Windows cần thông qua **WSL2**.

## 3. Ứng dụng trong Wiki 2.0
- **Fast Ingest**: Tăng tốc độ cào dữ liệu từ các trang tài liệu dài (như docs của framework) mà không phải chờ đợi trình duyệt render CSS/Images.
- **AI Agent Engine**: Phù hợp làm "đôi mắt" cho các Agent cần truy cập web hàng loạt để lấp lỗ hổng tri thức (Gap fulfillment).

## 4. Hướng dẫn cài đặt (Windows/WSL2)
```bash
# Tải binary Linux bên trong WSL
curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-x86_64-linux
chmod a+x ./lightpanda

# Chạy server CDP
./lightpanda serve --host 127.0.0.1 --port 9222
```

---
**Liên kết**:
- Công nghệ liên quan: [[ENTITY_TECH_LLM]]
- Workflow: [/ingest](file:///d:/NoteBookLLM_Br/.agent/workflows/ingest.md)

---
WRITE REPORT:
  file: "3-resources/wiki/entities/ENTITY_TOOL_Lightpanda.md"
  operation: "create"
  added: "TRI THỨC CÔNG CỤ: Nạp thông tin Lightpanda theo đề xuất của User."
  compliance: "Rule 3 & Rule 14 OK."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
