import subprocess
import sys
import os
from pathlib import Path

def run_graphify():
    project_root = Path(os.getcwd())
    input_path = project_root / "brain" / "distilled"
    output_path = project_root / "brain" / "process" / "graphify"
    
    # Äáº£m báº£o thÆ° má»¥c Ä‘áº§u ra tá»“n táº¡i
    os.makedirs(output_path, exist_ok=True)
    
    print(f"--- Starting Graphify Analysis for: {input_path} ---")
    
    # Lá»‡nh chuáº©n: python -m graphify.analyze <input>
    cmd = [
        sys.executable, "-m", "graphify.analyze", 
        str(input_path), 
        "--output", str(output_path),
        "--update"  # Thá»±c hiá»‡n cáº­p nháº­t nhanh náº¿u Ä‘Ã£ cÃ³ dá»¯ liá»‡u
    ]
    
    try:
        # Cháº¡y lá»‡nh vÃ  hiá»ƒn thá»‹ output trá»±c tiáº¿p
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8"
        )
        
        for line in process.stdout:
            print(f"  [graphify] {line.strip()}")
            
        process.wait()
        
        if process.returncode == 0:
            print("\nSuccess! Knowledge Graph v3.6 is now live.")
            print(f"Report: {output_path / 'GRAPH_REPORT.md'}")
        else:
            print(f"\nGraphify failed with exit code {process.returncode}")
            sys.exit(process.returncode)
            
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_graphify()

