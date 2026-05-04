import os
import subprocess
import sys

# Force UTF-8 for everything
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

def run_ingest():
    base_path = r"d:\NoteBookLLM_Br\brain\archive\raw_docx"
    if not os.path.exists(base_path):
        print(f"Error: {base_path} does not exist")
        return

    folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
    lms_folder = next((f for f in folders if "LMS" in f), None)

    if lms_folder:
        full_path = os.path.join(base_path, lms_folder)
        print(f"Found: {lms_folder}")
        
        # Call the Engine v15
        engine_script = r"d:\NoteBookLLM_Br\scripts\docx_to_md_raw.py"
        cmd = [sys.executable, engine_script, "--source", full_path, "--prefix", "LMS_MASTER_"]
        
        # Use subprocess with proper environment
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        
        result = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding='utf-8')
        
        print(result.stdout)
        if result.stderr:
            print("Errors detected:")
            print(result.stderr)
    else:
        print("Could not detect any folder containing 'LMS' in raw_docx")

if __name__ == "__main__":
    run_ingest()
