import os
import re

current_exam_path = r"d:\NoteBookLLM_Br\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1.md"
inbox_dir = r"D:\NoteBookLLM_Br\workspaces\source-lab\inbox\AI THCS"

def extract_question_texts(file_path):
    if not os.path.exists(file_path):
        return {}
    questions = {}
    current_q = None
    q_lines = []
    
    with open(file_path, "r", encoding="utf-8") as f:
        # Chỉ đọc 3000 dòng
        for _ in range(3000):
            line = f.readline()
            if not line:
                break
            cleaned = line.strip()
            # Khớp các tiêu đề câu hỏi
            match = re.search(r"(?:câu|Câu)\s+(\d+)", cleaned)
            if match:
                if current_q and q_lines:
                    questions[current_q] = " ".join(q_lines)
                current_q = int(match.group(1))
                q_lines = []
            elif current_q is not None and cleaned:
                # Bỏ qua các dòng base64, dòng markdown, dòng đáp án A, B, C, D
                if "data:image" in cleaned or len(cleaned) > 200 or cleaned.startswith("- ") or cleaned.startswith("* "):
                    continue
                display_line = re.sub(r"<[^>]+>", "", cleaned)
                display_line = display_line.replace("__", "").replace("\\", "").strip()
                if display_line:
                    q_lines.append(display_line)
                    
        if current_q and q_lines:
            questions[current_q] = " ".join(q_lines)
            
    return questions

def analyze():
    curr_qs = extract_question_texts(current_exam_path)
    print(f"CURRENT EXAM has {len(curr_qs)} questions extracted.")
    print("  First 3 questions of CURRENT EXAM:")
    for i in range(1, min(4, len(curr_qs)+1)):
        print(f"    Q{i}: {curr_qs.get(i, '')[:120]}")
        
    for i in range(1, 5):
        inbox_file = os.path.join(inbox_dir, f"de_{i}.md")
        inbox_qs = extract_question_texts(inbox_file)
        print(f"\nDE {i} has {len(inbox_qs)} questions.")
        print(f"  First 3 questions of DE {i}:")
        for j in range(1, min(4, len(inbox_qs)+1)):
            print(f"    Q{j}: {inbox_qs.get(j, '')[:120]}")

if __name__ == "__main__":
    analyze()
