# HD SOURCE: ARCH_BMAD_Method_FRONT_11_P028-028
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_11
Part Title: NONE
Chapter Title: NONE
Section Title: 1.8 vì sao hàng chục nghìn developer chọn BMad?
Chunk Range: Pages 28 to 28
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Ví dụcụthể : Khi Developer Agent triển khai Story 5.3, nó không chỉ đọc story đó. Nó đọc story (nhiệm vụngay trước mắt), đọc kiến trúc (các quyết định kỹ thuật đã được thống nhất), và đọc projectcontext.md (quyước vàmẫu thiết kếcủa dự án). Kết quả là code nhất quán với phần còn lại của dự án, tuân theo đúng các mẫu đã được thiết kếtừ trước.

## 1.7 hệ sinh thái BMad

BMad được tổ chức theo kiến trúc module: BMad Core -  Bộcông cụcốt lõi luôn có sẵn, bất kể bạn cài module nào. Bao gồm mười công cụtừ brainstorming đến review, từ compression đến document management (chi tiếtở Chương 4). BMM  -  BMad Method -  Module agile development cốt lõi. Bao gồm PM Agent, Architect Agent, Developer Agent, UX Designer Agent, Tech Writer Agent, và hơn ba mươi bốn workflows. Đây làmodule bắt buộc, được cài cùng với Core. BMB  -  BMad Builder -  Module cho phép bạn tạo custom agents, workflows, và các module của riêng mình để chia sẻ với cộng đồng. CIS  -  Creative Intelligence Suite -  Bộcông cụcho sáng tạo và đổi mới. Bảy agents chuyên biệt từInnovation Strategist đến Storyteller. GDS  -  Game Dev Studio -  Module phát triển game hỗ trợ hơn hai mươi mốt thể loại game và các engine phổ biến nhưUnity, Unreal, Godot. TEA  -  Test Architect -  Module kiểm thử cấp doanh nghiệp với agent chuyên gia Murat và chín workflows kiểm thử cócấu trúc.

## 1.8 vì sao hàng chục nghìn developer chọn BMad?

Con số hơn bốn mươi ba nghìn stars trên GitHub phảnánh việc BMad giải quyết đồng thời nhiều vấn đề thực tế : Tính hoàn chỉnh toàn vòng đời: Không chỉ sinh code, mà bao phủ toàn bộtừ ýtưởng đếtriển khai. Tính nhất quán: Tất cảagents đọc cùng một tài liệu kiến trúc và project-context, nên code được tạo ra bởi các agents khác nhau vẫn nhất quán với nhau. Cổng chất lượng được tích hợp sẵn: Implementation Readiness Check, Code Review, Adversarial Review không phải là bước tùy chọn  -  chúng làmột phần của workflow.

n