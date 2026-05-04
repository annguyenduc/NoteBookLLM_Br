import os
import re

concept_dir = r"d:\NoteBookLLM_Br\3-resources\wiki\concepts"
non_compliant = []

for filename in os.listdir(concept_dir):
    if not filename.endswith(".md"):
        continue
    
    path = os.path.join(concept_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
        # Check 1: Has source metadata pointing to a SOURCE_ file
        has_source = re.search(r"source:\s*\"?\[\[SOURCE_", content)
        
        # Check 2: Has Rule 17 (Double Examples)
        has_rule17 = "Ví dụ đối chiếu" in content or "Rule 17" in content
        
        # Check 3: Status
        is_stub = "status: \"stub\"" in content or "status: 'stub'" in content

        if not has_source or not has_rule17 or is_stub:
            reason = []
            if not has_source: reason.append("Missing SOURCE_ link")
            if not has_rule17: reason.append("Missing Rule 17 (Double Examples)")
            if is_stub: reason.append("Status is STUB")
            
            non_compliant.append({
                "file": filename,
                "reasons": ", ".join(reason)
            })

print(f"{'FILENAME':<50} | {'ISSUES'}")
print("-" * 100)
for item in non_compliant:
    print(f"{item['file']:<50} | {item['reasons']}")
