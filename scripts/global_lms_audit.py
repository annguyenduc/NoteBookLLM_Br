import os
from pathlib import Path

RAW_ROOT = Path(r"D:\NoteBookLLM_Br\brain\raw\Tổng hợp đề kiểm tra LMS")
WIKI_DIR = Path(r"d:\NoteBookLLM_Br\brain\wiki")

def audit():
    # 1. Thu thập tất cả file RAW (.docx)
    raw_files = {} # filename -> full_path
    for f in RAW_ROOT.rglob("*.docx"):
        raw_files[f.name] = str(f)
    
    # 2. Thu thập tất cả các nguồn đã được trích dẫn trong Wiki
    cited_sources = set()
    wiki_files = list(WIKI_DIR.glob("*.md"))
    
    for wf in wiki_files:
        try:
            with open(wf, "r", encoding="utf-8") as f:
                content = f.read()
                # Tìm source: "[[Filename.docx]]"
                import re
                match = re.search(r'source:\s*"\[\[(.*?)\]\]"', content)
                if match:
                    cited_sources.add(match.group(1))
        except:
            continue
            
    # 3. So sánh
    missing_conversion = []
    for raw_name in raw_files:
        if raw_name not in cited_sources:
            missing_conversion.append(raw_name)
            
    # 4. Ghi báo cáo
    with open(r"d:\NoteBookLLM_Br\brain\process\Global_LMS_Audit_Report.md", "w", encoding="utf-8") as f:
        f.write("# 🛡️ BÁO CÁO KIỂM ĐỊNH TỔNG THỂ LMS\n\n")
        f.write(f"## 📊 Thống kê\n")
        f.write(f"- Tổng số tệp RAW tìm thấy: {len(raw_files)}\n")
        f.write(f"- Tổng số nguồn đã chuyển đổi: {len(cited_sources)}\n")
        f.write(f"- Số tệp RAW chưa được chuyển đổi: {len(missing_conversion)}\n\n")
        
        f.write("## ⚠️ Danh sách tệp RAW chưa được chuyển đổi (Black Holes)\n")
        if not missing_conversion:
            f.write("- [X] Tất cả tệp RAW đã được chuyển đổi thành công.\n")
        else:
            for m in sorted(missing_conversion):
                f.write(f"- [ ] {m}\n")
                
        f.write("\n## ✅ Danh sách các nguồn đã được xác nhận (Verified)\n")
        for s in sorted(cited_sources):
            status = "EXIST" if s in raw_files else "MISSING_RAW"
            f.write(f"- {s} [{status}]\n")

    print(f"Audit complete. Report saved to 3-resources/process/Global_LMS_Audit_Report.md")

if __name__ == "__main__":
    audit()
