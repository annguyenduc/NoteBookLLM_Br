# -*- coding: utf-8 -*-
import os
import sys
import site
import argparse
import re
from pathlib import Path

# Bootstrap project venv
CURRENT_WORKTREE = Path(__file__).resolve().parents[2]
sys.path.append(str(CURRENT_WORKTREE))

REPO_ROOT = Path("D:/NoteBookLLM_Br")
sys.path.append(str(REPO_ROOT))

site_packages = REPO_ROOT / ".venv" / "Lib" / "site-packages"
if site_packages.exists():
    site.addsitedir(str(site_packages))

FREELLM_URL = "http://localhost:3001/v1"

# Fallback Rubric tĩnh chất lượng cao chắt lọc từ prompt-master/SKILL.md
FALLBACK_RUBRIC = """
Bạn là một Chuyên gia Kỹ nghệ Prompt (Prompt Engineer) và Kiến trúc sư Tri thức cấp cao. 
Nhiệm vụ của bạn là lấy ý định thô (vague intent) của người dùng, phân tích và sinh ra một Production-ready prompt duy nhất được tối ưu hóa cho công cụ NotebookLM.

### NGUYÊN TẮC THIẾT KẾ PROMPT:
1. Sử dụng cấu trúc CO-STAR:
   - Context: Bối cảnh nghiệp vụ rõ ràng dựa trên tài liệu đã nạp.
   - Objective: Mục tiêu hành động cụ thể, rõ ràng.
   - Style: Phong cách trình bày (kỹ thuật, trực quan, cô đọng).
   - Tone: Tông giọng (sắc bén, chuyên nghiệp, hoặc sư phạm).
   - Audience: Đối tượng người đọc hướng tới.
   - Response: Định dạng đầu ra (Markdown, cấu trúc rõ ràng).
2. Không sử dụng Chain of Thought (CoT), "hãy nghĩ từng bước" đối với các mô hình suy luận bản xứ (reasoning-native) như Gemini 2.0/3 Pro, o3, R1.
3. Đầu ra chỉ chứa duy nhất prompt hoàn chỉnh được đặt trong một khối mã Markdown (code block) để dễ dàng COPY. Không giải thích dông dài hay thảo luận lý thuyết prompting.

### RANH GIỚI AN TOÀN & QUY ƯỚC VAULT:
1. Mọi prompt sinh ra để phục vụ việc trích xuất tri thức phải hướng tới kết quả trung thực, chống ảo giác (hallucination).
2. Không cố tình tự tổng hợp thông tin nằm ngoài phạm vi tài liệu đã nạp.
3. Toàn bộ ngôn ngữ trong prompt phải viết bằng tiếng Việt.
"""

def load_freeapi_key() -> str:
    """Tự động đọc unified API key từ database SQLite của FreeLLMAPI trong workspaces."""
    import sqlite3
    db_path = CURRENT_WORKTREE / "workspaces" / "freellmapi" / "server" / "data" / "freeapi.db"
    if not db_path.exists():
        db_path = REPO_ROOT / "workspaces" / "freellmapi" / "server" / "data" / "freeapi.db"
        
    if not db_path.exists():
        raise FileNotFoundError(f"Không tìm thấy db FreeLLMAPI tại {db_path}")
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT value FROM settings WHERE key='unified_api_key';")
        row = cursor.fetchone()
        if row:
            return row[0]
        raise ValueError("Không tìm thấy unified_api_key trong bảng settings.")
    finally:
        conn.close()

def extract_prompt_master_core_rubric() -> str:
    """Đọc tệp SKILL.md của prompt-master và chắt lọc Core Rubric để làm System Prompt tối ưu."""
    skill_path = CURRENT_WORKTREE / ".agent" / "skills" / "prompt-master" / "SKILL.md"
    if not skill_path.exists():
        skill_path = REPO_ROOT / ".agent" / "skills" / "prompt-master" / "SKILL.md"
    
    if not skill_path.exists():
        print("[!] Không tìm thấy file SKILL.md. Chuyển sang Fallback Rubric tĩnh.")
        return FALLBACK_RUBRIC
    
    try:
        skill_content = skill_path.read_text(encoding="utf-8")
        core_sections = []
        
        # 1. Trích xuất vai trò chính (Identity)
        identity_match = re.search(r"## PRIMACY ZONE.*?\n(.*?)\n---", skill_content, re.DOTALL)
        if identity_match:
            core_sections.append(f"### VAI TRÒ & NGUYÊN TẮC CỐT LÕI:\n{identity_match.group(1).strip()}")
            
        # 2. Trích xuất Output Format
        format_match = re.search(r"\*\*Output format — Follow this format\*\*.*?\n(.*?)\n---", skill_content, re.DOTALL)
        if format_match:
            core_sections.append(f"### ĐỊNH DẠNG PROMPT YÊU CẦU:\n{format_match.group(1).strip()}")
            
        # 3. Trích xuất Workspace Overlay
        overlay_match = re.search(r"\*\*NoteBookLLM_Br Workspace Overlay\*\*.*?\n(.*?)\n---", skill_content, re.DOTALL)
        if overlay_match:
            core_sections.append(f"### RANH GIỚI AN TOÀN & QUY ƯỚC VAULT:\n{overlay_match.group(1).strip()}")

        if not core_sections:
            raise ValueError("Không thể phân tích các phần cấu trúc của SKILL.md")
            
        return "\n\n".join(core_sections)
    except Exception as e:
        print(f"[!] Lỗi parse SKILL.md: {e}. Tự động fallback sang Rubric tĩnh.")
        return FALLBACK_RUBRIC

def generate_prompt_via_freellm(user_intent: str, target_tool: str = "NotebookLM", dry_run: bool = False) -> str:
    """Gọi FreeLLMAPI thông qua local proxy để sinh prompt chất lượng cao."""
    system_instructions = extract_prompt_master_core_rubric()
    
    if dry_run:
        print("\n[Dry-Run] Cấu hình System Prompt (Core Rubric) được nạp:")
        print("--------------------------------------------------")
        print(system_instructions[:600] + "\n...")
        print("--------------------------------------------------")
        return "```text\n[MOCK PROMPT] Đây là prompt giả lập từ dry-run. Ý định: " + user_intent + "\n```"
        
    print("--- 🧠 ĐANG GỌI FREELLMAPI (PORT 3001) ĐỂ TẠO PROMPT TEMPLATE ---")
    
    # Lazy import litellm khi không chạy Dry-run để tránh lỗi nạp môi trường khi test
    import litellm
    
    api_key = load_freeapi_key()
    prompt_query = f"Hãy tạo một prompt chất lượng cao tối ưu hóa cho công cụ '{target_tool}' dựa trên ý định sau: '{user_intent}'"
    
    # Sử dụng model auto từ FreeLLMAPI
    model_name = "auto"
    
    response = litellm.completion(
        model=model_name,
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": prompt_query}
        ],
        api_base=FREELLM_URL,
        api_key=api_key,
        custom_llm_provider="openai",
        temperature=0.3
    )
    
    generated_content = response.choices[0].message.content
    return generated_content

def save_prompt_atom(title_slug: str, prompt_content: str) -> Path:
    """Lưu prompt template vào Obsidian Preview Atom (Non-Canonical)."""
    output_dir = CURRENT_WORKTREE / "workspaces" / "learning" / "preview"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    safe_title = title_slug.replace(" ", "_")
    file_path = output_dir / f"PREVIEW_Prompt_{safe_title}.md"
    
    # Script sở hữu logic sinh YAML để đảm bảo tính an toàn cấu trúc của Obsidian
    atom_data = f"""---
title: "Preview Prompt: {title_slug}"
learning_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
source_id: "NONE"
trust: "UNVERIFIED"
tags:
  - "Prompt_Candidate"
  - "Learning_Preview"
target_tool: "NotebookLM"
framework: "CO-STAR"
model_lineage: "prompt-master -> FreeLLMAPI-Auto"
---

# Preview Prompt: {title_slug}

## 🛠️ Generated Prompt Block
{prompt_content}
"""
    file_path.write_text(atom_data, encoding="utf-8")
    print(f"[+] Đã lưu Prompt Preview tại: {file_path}")
    return file_path

def execute_query_on_notebooklm(prompt_text: str, notebook_id: str = None, use_first: bool = False, dry_run: bool = False) -> str:
    """Đẩy prompt vừa sinh lên NotebookLM qua API client và lấy kết quả."""
    if dry_run:
        print("\n[Dry-Run] Gửi prompt lên NotebookLM...")
        print(f"Target Notebook ID: {notebook_id or 'First Available (mocked)'}")
        return "[MOCK ANSWER] Đây là kết quả trích xuất giả lập từ dry-run."
        
    print("--- 🧠 ĐANG GỬI PROMPT LÊN NOTEBOOKLM QUA MCP CLIENT ---")
    
    # Lazy import NotebookLM components chỉ khi không chạy dry-run
    try:
        from notebooklm_mcp.auth import load_cached_tokens
        from notebooklm_mcp.api_client import NotebookLMClient
    except ImportError as e:
        raise ImportError(f"Không thể import NotebookLM Client từ venv: {e}")
        
    tokens = load_cached_tokens()
    if not tokens:
        raise ValueError("Không tìm thấy cached tokens. Vui lòng auth NotebookLM trước.")
        
    client = NotebookLMClient(
        cookies=tokens.cookies,
        csrf_token=tokens.csrf_token,
        session_id=tokens.session_id
    )
    
    try:
        if not notebook_id:
            if not use_first:
                raise ValueError("Cần cung cấp --notebook-id hoặc bật cờ --use-first-notebook để xác nhận sử dụng notebook đầu tiên.")
            notebooks = client.list_notebooks()
            if not notebooks:
                raise ValueError("Không tìm thấy notebook nào trong tài khoản.")
            target_notebook = notebooks[0]
            notebook_id = target_notebook.id
            print(f"Sử dụng notebook mặc định: '{target_notebook.title}' (ID: {notebook_id})")
        
        # Trích xuất phần text prompt chính bên trong cặp thẻ code block để gửi
        prompt_main = prompt_text
        code_block_match = re.search(r"```(?:text)?\n(.*?)\n```", prompt_text, re.DOTALL)
        if code_block_match:
            prompt_main = code_block_match.group(1).strip()
            
        response = client.query(notebook_id, prompt_main)
        client.close()
        
        if isinstance(response, dict):
            return response.get("answer", "")
        return str(response)
    except Exception as e:
        client.close()
        raise e

def save_extracted_knowledge(prompt_title: str, answer_text: str):
    """Lưu kết quả phân tích từ NotebookLM thành một Recon Preview không-canonical."""
    output_dir = CURRENT_WORKTREE / "workspaces" / "learning" / "preview"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    safe_title = prompt_title.replace(" ", "_")
    file_path = output_dir / f"NOTEBOOKLM_RECON_{safe_title}.md"
    
    atom_content = f"""---
title: "NotebookLM Recon: {prompt_title}"
learning_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
source_id: "NONE"
trust: "UNVERIFIED"
tags:
  - "NotebookLM_Recon"
  - "Learning_Preview"
---

# NotebookLM Recon: {prompt_title}

## 📝 Kết quả Trích xuất từ NotebookLM
{answer_text}

## 🔄 Liên kết Tri thức
- **Prompt nguồn:** [[PREVIEW_Prompt_{safe_title}]]
"""
    file_path.write_text(atom_content, encoding="utf-8")
    print(f"[+] Đã lưu Recon Preview tại: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Pipeline tự động sinh Prompt qua FreeLLM và truy vấn NotebookLM.")
    parser.add_argument("intent", help="Ý định sơ bộ của bạn (vague intent)")
    parser.add_argument("--title", required=True, help="Tên ngắn gọn cho Prompt Atom (ví dụ: 'Data Analyst Coach')")
    parser.add_argument("--notebook-id", help="ID của notebook trong NotebookLM")
    parser.add_argument("--use-first-notebook", action="store_true", help="Xác nhận sử dụng notebook đầu tiên nếu không chỉ định ID")
    parser.add_argument("--dry-run", action="store_true", help="Chế độ chạy thử nghiệm an toàn, không gọi API thực tế và không ghi file")
    args = parser.parse_args()
    
    try:
        # Bước 1: Sinh Prompt chất lượng cao qua FreeLLMAPI (chắt lọc Core Rubric từ prompt-master)
        generated_prompt = generate_prompt_via_freellm(args.intent, dry_run=args.dry_run)
        print("\n=== PROMPT ĐÃ ĐƯỢC TỐI ƯU HÓA ===")
        print(generated_prompt)
        print("=================================\n")
        
        # Nếu chạy Dry-run thì DỪNG LẠI TẠI ĐÂY, KHÔNG ghi bất kỳ file nào ra đĩa
        if args.dry_run:
            print("\n[Dry-Run] Đã kiểm tra logic sinh prompt. Dừng chạy an toàn, không ghi file.")
            print("🚀 DRY-RUN HOÀN THÀNH XUẤT SẮC!")
            sys.exit(0)
            
        # Bước 2: Lưu Prompt Atom vào Obsidian Preview
        save_prompt_atom(args.title, generated_prompt)
        
        # Bước 3: Đẩy prompt lên NotebookLM để thực thi truy vấn
        extracted_answer = execute_query_on_notebooklm(
            generated_prompt, 
            notebook_id=args.notebook_id, 
            use_first=args.use_first_notebook,
            dry_run=args.dry_run
        )
        
        # Bước 4: Lưu kết quả thành Recon Preview
        save_extracted_knowledge(args.title, extracted_answer)
        
        print("\n🚀 PIPELINE HOÀN THÀNH XUẤT SẮC!")
        
    except Exception as e:
        print(f"[!] Lỗi trong quá trình chạy Pipeline: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
