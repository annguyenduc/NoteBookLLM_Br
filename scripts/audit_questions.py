import os
import re
from collections import defaultdict

WIKI_DIR = os.path.join("brain", "wiki")

def main():
    # Cấu trúc: groups[module_submodule][de_str] = set(q_nums)
    groups = defaultdict(lambda: defaultdict(set))
    
    for filename in os.listdir(WIKI_DIR):
        if ("MCQ_" in filename) or ("NON_MCQ_" in filename):
            if filename == "WIKI_INDEX.md" or filename.startswith("WIKI_"):
                continue
                
            match = re.search(r'_(De[X\d]+)_(Q\d+)(?:_v\d+)?\.md$', filename)
            if match:
                de_str = match.group(1)
                q_str = match.group(2)
                
                # Bóc tách tên Module (bỏ phần tiền tố MCQ/NON_MCQ/NEEDS_REVIEW)
                core_name = filename
                for p in ["NEEDS_REVIEW_NON_MCQ_", "NEEDS_REVIEW_MCQ_", "NON_MCQ_", "MCQ_"]:
                    if core_name.startswith(p):
                        core_name = core_name[len(p):]
                        break
                        
                mod_submod = core_name[:core_name.find(f"_{de_str}_")]
                
                q_num = int(q_str[1:])
                groups[mod_submod][de_str].add(q_num)

    report_lines = ["# 📊 Báo cáo Rà soát Thiếu sót Câu hỏi trong Ngân hàng Đề\n"]
    total_missing = 0
    missing_groups = 0
    
    for mod_submod in sorted(groups.keys()):
        has_missing_in_module = False
        module_lines = [f"## 🧩 Mảng: {mod_submod}"]
        
        for de_str in sorted(groups[mod_submod].keys()):
            q_set = groups[mod_submod][de_str]
            max_q = max(q_set) if q_set else 0
            
            missing = []
            for i in range(1, max_q + 1):
                if i not in q_set:
                    missing.append(f"Q{i:02d}")
            
            if missing:
                has_missing_in_module = True
                total_missing += len(missing)
                module_lines.append(f"- **{de_str}**: (Có tổng {len(q_set)}/{max_q} câu) ❌ Thiếu: **{', '.join(missing)}**")
            else:
                module_lines.append(f"- **{de_str}**: ✅ Đầy đủ (1 ➔ Q{max_q:02d})")
                
        module_lines.append("")
        report_lines.extend(module_lines)
        if has_missing_in_module:
            missing_groups += 1

    report_lines.insert(1, f"**Tổng số câu phát hiện bị đứt gãy/thiếu:** {total_missing}")
    
    out_path = os.path.join("brain", "process", "Audit_Missing_Questions.md")
    if not os.path.exists(os.path.dirname(out_path)):
        os.makedirs(os.path.dirname(out_path))
        
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
        
    print(f"Audit completed. Found {total_missing} missing questions. Report saved to {out_path}.")

if __name__ == "__main__":
    main()
