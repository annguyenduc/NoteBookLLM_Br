# HD SOURCE: ARCH_BMAD_Method_FRONT_107_P130-130
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_107
Part Title: NONE
Chapter Title: NONE
Section Title: 11.5 section: Persona - thay thếtoàn bộtính cách
Chunk Range: Pages 130 to 130
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

- `critical\_actions` **Thêm vào** startup actions hiện có `prompts` **Định nghĩa mới**  -  tham chiếu từmenu

## 11.4 section: Agent.metadata đổi tên agent

Trường hợp sử dụng đơn giản nhất: Đặt tên thân thiện hơn cho agent.

```
agent: metadata: name: 'Quang Minh'    # PM của team mình
```

Sau khiáp dụng, agent sẽ tự giới thiệu và được gọi là "Quang Minh" thay vì "Amelia".

Trường hợp dùng thực tế : Một sốteam đặt tên agent theo tên thật của team members  tạo cảm giác làm việc với đồng nghiệp quen thuộc hơn.

## 11.5 section: Persona  -  thay thếtoàn bộtính cách

Section persona thay thếtoàn bộnhân vật của agent. Khi set persona, phải cung cấp đầy đủ tất cả bốn trường:

```
persona: role: 'Product Manager và Startup Advisor' identity: | Một PM đã có kinh nghiệm xây dựng và thất bại với ba startups trước khi thành công với sản phẩm SaaS thứtư. Hiểu sâu về bootstrapping, lean thinking, và tầm quan trọng của revenue positive từ sớm. communication_style: | Thẳng thắn, thực dụng. Luôn hỏi về business impact trước khi tiếp cận bất kỳ quyết định nào. Không kiên nhẫn với nợ kỹ thuật không có kế hoạch trả . Celebrate wins dùnhỏ . principles: -'Revenue trước elegance  ship cái gì đó hoạt động trước khi làm nó đẹp' - 'Luôn hỏi "Tại sao người dùng lại quan tâm đến điều này?"' - 'Kiểm tra assumptions với người dùng thực, không phải với team' - 'Scope creep là kẻ thù của momentum  -  phòng vệtích cực'
```

## Khi Nào Dùng:

Team của bạn cótriết lý hoặc văn hóa riêng biệt

Bạn muốn agent phảnánh một phong cách quản lýcụthể Dự án trong một lĩnh vực đặc thù cần mindset phù hợp

LưuÝ Quan Trọng: Khi không cung cấp đủ bốn trường, agent cóthể không hoạt động đúng cách. Luôn check lại cả bốn: role , identity , communication\_style , principles .