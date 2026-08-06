# HD SOURCE: ARCH_BMAD_Method_FRONT_110_P134-134
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_110
Part Title: NONE
Chapter Title: NONE
Section Title: Lỗi: Persona không hoạt động đúng
Chunk Range: Pages 134 to 134
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
1. **GDPR compliance:** Dữ liệu cánhân có được xử lý đúng không? 2. **Authorization:** Mọi endpoint có kiểm tra permission không? 3. **Input validation:** Tất cảinput từ client có được validate không? 4. **SQL injection:** Có raw queries nào không qua Prisma không? 5. **Sensitive data logging:** Log cóchứa PII không? 6. **Rate limiting:** Endpoints nhạy cảm có được protect không? Liệt kêfindings theo priority: CRITICAL → HIGH → MEDIUM → LOW
```

## 11.10 áp dụng thay đổi: Quick update

Sau khi chỉnh sửa file .customize.yaml , phải chạy installer để áp dụng:

```
npx bmad-method install # Chọn: "quick update" (cập nhậ
```

## Quick Update:

```
Áp dụng thay đổi từ các file .customize.yaml KHÔNG ghi đèagent files trong _bmad/agents/ Thực hiện trong một vài giây
```

## 11.11 troubleshooting

## Lỗi: Thay đổi không đượcáp dụng

Chưa chạy Quick Update. Giải pháp: npx bmad-method install → Quick Update.

## Lỗi: Agent không nhận memory tùy chỉnh

Kiểm tra YAML indentation  -  memories phải là list items:

```
# Đúng memories: - 'Memory 1' - 'Memory 2' # Sai  -  thiếu dấu gạch đầu dòng memories: 'Memory 1' 'Memory 2'
```

## Lỗi: Persona không hoạt động đúng

Persona phải có đầy đủ bốn trường. Thiếu bất kỳ trường nào sẽ gây lỗi:

```
t nhanh)
```