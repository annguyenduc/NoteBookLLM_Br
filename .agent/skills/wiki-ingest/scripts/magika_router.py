import os
import sys
import subprocess
import json

ROOT_DIR = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)

def infer_from_extension(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return {"mime_type": "application/pdf", "group": "document", "parser": "docling"}
    if ext in (".md", ".markdown"):
        return {"mime_type": "text/markdown", "group": "text", "parser": "native"}
    if ext in (".txt", ".log", ".rst"):
        return {"mime_type": "text/plain", "group": "text", "parser": "native"}
    if ext in (".docx", ".pptx", ".xlsx"):
        return {"mime_type": "application/octet-stream", "group": "office", "parser": "markitdown"}
    return {"mime_type": "unknown", "group": "unknown", "parser": "unknown"}

def get_file_info(file_path):
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    try:
        # Determine magika executable path
        venv_magika = os.path.join(ROOT_DIR, ".venv", "Scripts", "magika.exe")
        magika_cmd = venv_magika if os.path.exists(venv_magika) else 'magika'

        # Run magika with json output
        result = subprocess.run(
            [magika_cmd, '--json', file_path],
            capture_output=True,
            text=True,
            check=True
        )
        data = json.loads(result.stdout)
        
        # Magika output is a list of results
        file_data = data[0]
        # Handle the nested structure of Magika JSON output
        result_value = file_data.get('result', {}).get('value', {})
        if not result_value: # Try older structure just in case
             result_value = file_data
             
        mime_type = result_value.get('output', {}).get('mime_type', 'unknown')
        group = result_value.get('output', {}).get('group', 'unknown')
        
        # Determine parser from Magika output
        parser = "unknown"
        if mime_type == "application/pdf":
            parser = "docling"
        elif mime_type in ["text/markdown", "text/plain"]:
            parser = "native"
        elif group == "office":
            parser = "markitdown"
        elif group == "code":
            parser = "native"
            
        info = {
            "path": file_path,
            "mime_type": mime_type,
            "group": group,
            "parser": parser
        }

        # Fallback when Magika cannot classify correctly.
        if info["mime_type"] == "unknown" or info["parser"] == "unknown":
            fallback = infer_from_extension(file_path)
            info.update(fallback)
            info["detection_mode"] = "extension_fallback"
        else:
            info["detection_mode"] = "magika"

        return info
        
    except FileNotFoundError:
        fallback = infer_from_extension(file_path)
        return {
            "path": file_path,
            "mime_type": fallback["mime_type"],
            "group": fallback["group"],
            "parser": fallback["parser"],
            "detection_mode": "extension_fallback",
            "note": "magika command not found"
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python magika_router.py <file_path>")
        sys.exit(1)
        
    info = get_file_info(sys.argv[1])
    print(json.dumps(info, indent=2))
