# SKILL_IMPROVEMENT_PROPOSAL

```yaml
proposal_id: SIP_[YYYYMMDD]_[seq]
skill_id: [id]
current_version: [version]
proposed_version: [bump minor, e.g. 0.3.1 → 0.3.2]
source_run_id: [run_id hoặc "manual"]
trigger: [user_correction | missing_step | repeated_failure | output_drift | test_gap]
severity: low | medium | high
approval_required: true
```

## Evidence
_Trích dẫn cụ thể: user nói gì, output sai chỗ nào, bước nào thiếu._

## Problem
_Mô tả gap trong skill hiện tại._

## Proposed Change (diff format)
_Mô tả thay đổi cụ thể. Không sửa SKILL.md trực tiếp — đây chỉ là đề xuất._

## Regression Case
- Input: [mô tả input]
- Expected: [expected behavior sau khi patch]

## Risk
[low / medium / high] — [lý do]

## AN Decision
- [ ] Approve + GO → agent apply patch theo surgical diff
- [ ] Reject → lý do: ___
- [ ] Defer → review lại sau: ___
