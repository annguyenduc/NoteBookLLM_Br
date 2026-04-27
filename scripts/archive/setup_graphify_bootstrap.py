import subprocess
import sys
import os
from pathlib import Path

def run_graphify():
    project_root = Path(os.getcwd())
    # Cập nhật: Bao gồm cả wiki và distilled
    input_paths = [
        project_root / "brain" / "wiki",
        project_root / "brain" / "distilled"
    ]
    output_path = project_root / "brain" / "process" / "graphify"
    
    # Đảm bảo thư mục đầu ra tồn tại
    os.makedirs(output_path, exist_ok=True)
    
    print(f"--- Starting Graphify Analysis for Wiki & Distilled ---")
    
    success = True
    for input_path in input_paths:
        if not input_path.exists():
            print(f"  [skip] Path not found: {input_path}")
            continue
            
        print(f"  [process] Analyzing: {input_path}")
        # Lệnh chuẩn: python -m graphify.analyze <input>
        cmd = [
            sys.executable, "-m", "graphify.analyze", 
            str(input_path), 
            "--output", str(output_path),
            "--update"
        ]
        
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8"
            )
            
            for line in process.stdout:
                print(f"    [graphify] {line.strip()}")
                
            process.wait()
            
            if process.returncode != 0:
                print(f"  [error] Graphify failed for {input_path.name} with code {process.returncode}")
                success = False
                
        except Exception as e:
            print(f"  [fatal] Error processing {input_path.name}: {e}")
            success = False

    if success:
        print("\nSuccess! Knowledge Graph v4.0 is now live.")
        print(f"Report: {output_path / 'GRAPH_REPORT.md'}")
    else:
        print("\nGraphify finished with some errors.")

if __name__ == "__main__":
    run_graphify()
