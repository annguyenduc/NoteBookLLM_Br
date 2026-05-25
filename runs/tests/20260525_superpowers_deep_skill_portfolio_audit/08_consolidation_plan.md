# Consolidation Plan: Kế Hoạch Tinh Gọn Kỹ Năng

Bản kế hoạch này đề xuất lộ trình gom, cấu trúc lại và archive các kỹ năng chồng chéo, dư thừa của vault `NoteBookLLM_Br` theo 3 giai đoạn (Phase) cụ thể, đảm bảo an toàn tuyệt đối cho hệ thống.

---

## Phase 1 — No-risk documentation/routing cleanup
Giai đoạn dọn dẹp tài liệu và định tuyến an toàn không gây ảnh hưởng tới logic vận hành mã nguồn.

```yaml
actions:
  - id: "P1A01"
    action: "Di chuyển thư mục references ra khỏi .agent/skills/ sang .agent/docs/"
    files_affected:
      - ".agent/skills/references"
      - ".agent/SKILLS_INDEX.md"
    requires_user_GO: true
    risk: "low"
    rollback: "Khôi phục lại thư mục về vị trí cũ và cập nhật lại SKILLS_INDEX.md."

  - id: "P1A02"
    action: "Chuyển đổi wiki-rebuild và wiki-cleanup từ skill tư duy thành kịch bản workflow hoặc lệnh shell tĩnh"
    files_affected:
      - ".agent/skills/wiki-rebuild"
      - ".agent/skills/wiki-cleanup"
      - ".agent/workflows/wiki-maintenance.md"
    requires_user_GO: true
    risk: "low"
    rollback: "Tạo lại các tệp SKILL.md nguyên bản cho rebuild và cleanup."

  - id: "P1A03"
    action: "Chuyển đổi cm-continuity và cm-quality-gate thành các chốt chặn luật chơi tĩnh (Rule) chạy ở Session End"
    files_affected:
      - ".agent/skills/cm-continuity"
      - ".agent/skills/cm-quality-gate"
      - "AGENTS.md"
    requires_user_GO: true
    risk: "low"
    rollback: "Kích hoạt lại skill cm-continuity và cm-quality-gate và đưa vào global runtime skill path."
```

---

## Phase 2 — Merge or rewrite overlapping skills
Giai đoạn gộp hoặc viết lại các kỹ năng có sự chồng chéo cao về chức năng và trigger.

```yaml
actions:
  - id: "P2A01"
    action: "Hợp nhất hoàn toàn brainstorming vào cm-planning"
    files_affected:
      - ".agent/skills/brainstorming"
      - ".agent/skills/cm-planning/SKILL.md"
    requires_user_GO: true
    risk: "medium"
    rollback: "Tách logic brainstorming cũ ra khỏi SKILL.md của cm-planning."

  - id: "P2A02"
    action: "Hợp nhất cm-tdd vào verification-before-completion"
    files_affected:
      - ".agent/skills/cm-tdd"
      - ".agent/skills/verification-before-completion/SKILL.md"
    requires_user_GO: true
    risk: "medium"
    rollback: "Khôi phục cm-tdd thành một skill hoạt động độc lập."

  - id: "P2A03"
    action: "Hợp nhất systematic-debugging vào cm-debugging"
    files_affected:
      - ".agent/skills/systematic-debugging"
      - ".agent/skills/cm-debugging/SKILL.md"
    requires_user_GO: true
    risk: "medium"
    rollback: "Tách systematic-debugging hoạt động độc lập."
```

---

## Phase 3 — Archive legacy or redundant skills
Giai đoạn đóng lưu trữ (archive) các kỹ năng đã được gộp hoàn tất hoặc không còn use case.

```yaml
actions:
  - id: "P3A01"
    action: "Di chuyển thư mục brainstorming sang thư mục lưu trữ 4-archive/skills/"
    files_affected:
      - ".agent/skills/brainstorming"
    requires_user_GO: true
    risk: "low"
    rollback: "Di chuyển ngược lại .agent/skills/ và khai báo lại trong SKILLS_INDEX.md."

  - id: "P3A02"
    action: "Di chuyển thư mục cm-tdd sang thư mục lưu trữ 4-archive/skills/"
    files_affected:
      - ".agent/skills/cm-tdd"
    requires_user_GO: true
    risk: "low"
    rollback: "Di chuyển ngược lại .agent/skills/."

  - id: "P3A03"
    action: "Di chuyển thư mục systematic-debugging sang 4-archive/skills/"
    files_affected:
      - ".agent/skills/systematic-debugging"
    requires_user_GO: true
    risk: "low"
    rollback: "Di chuyển ngược lại .agent/skills/."
```
