# HD SOURCE: ARCH_BMAD_Method_FRONT_119_P145-146
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_119
Part Title: NONE
Chapter Title: NONE
Section Title: Tóm tắt chương 12
Chunk Range: Pages 145 to 146
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
# 1. chia nhỏarchitecture document bmad-shard-doc _bmad-output/planning-artifacts/architecture.md # → tạo architecture/ folder với index.md vàmười một sections # 2. archive completed stories mkdir _bmad-output/archive/sprint-1-4/ mv _bmad-output/stories/sprint-1-4/* _bmad-output/archive/sprint-1-4/ # 3. nén toàn bộ research cho future sessions bmad-distillator \ source_documents="./_bmad-output/research/" \ downstream_consumer="Reference chung cho planning meetings" \ --validate # → research -distillate.md (giảm từ 3000 dòng xuống 400 dòng) # 4. tạo index cho toàn bộplanning artifacts bmad-index-docs _bmad-output/planning-artifacts/ # → planning -artifacts/index.md với navigation map đầy đủ # 5. verify: Kiểm tra dangling references grep -r "architecture.md" _bmad-output/ | grep -v "architecture/"
```

## Kết quả :

Architecture được chia thành mười một files cóthểnavigate riêng lẻ Research được nén từ ba nghìn xuống bốn trăm dòng mà không mất thông tin Completed stories được archive, giảm noise

Index cho phép cảngười vàAI dễ dàng tìm đúng tài liệu

## Thực hành ngay

## Bài tập 1  Đánh GiáTài Liệu Hiện Tại:

```
# Kiểm tra kích thước tất cả tài liệu
```

```
wc -l _bmad-output/**/*.md | sort -rn | head -10
```

File nào vượt quá bốn trăm dòng? Đó là ứng viên cho sharding hoặc distillation.

## Bài tập 2  -  Thực Hành Distillation:

```
# Nếu bạn cótài liệu lớn: bmad-distillator # Đầu vào: # Source_documents: [đường dẫn đến file hoặc thưmục] # Downstream_consumer: "tôi sẽ dùng để [mục đích cụthể ]" # --validate # Kiểm tra: Tỷ lệnén là bao nhiêu? thông tin quan trọng còn đủ không?
```

## Tóm tắt chương 12

Tài liệu lớn gây hai vấn đề: Vượt context window của LLM + Khónavigate cho người Ba công cụ quản lý: bmad-shard-doc : Chia tài liệu lớn tại tiêu đề ## → thưmục với sections + index.md. Ngưỡng: hơn năm trăm dòng bmad-distillator : Nén lossless tốiưu cho LLM. --validate để xác nhận tính toàn vẹn bmad-index-docs : Tạo chỉmục navigation cho thưmục nhiều files Lossless ≠ Summary: Distillate bảo toàn TOÀN BỘthông tin, chỉnén format `downstream\_consumer` giúp AIưu tiên loại thông tin đúng khi nén Thứtự xử lý: Đánh giá → Chia nhỏ → Nén → Index → Verify dangling references project-context.md: Không bao giờ shard → Giữnhỏ gọn dưới ba trăm dòng → Cập nhật sau mỗi retrospective Phòng ngừa tốt hơn xử lý: Archive completed artifacts thường xuyên, check kích thước cuối mỗi sprint