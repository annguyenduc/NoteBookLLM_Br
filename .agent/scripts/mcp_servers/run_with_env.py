import os
import sys
import subprocess
from pathlib import Path

def load_env(env_path: Path):
    if not env_path.exists():
        print(f"WARNING: env file not found at {env_path}", file=sys.stderr)
        return
    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, val = line.split("=", 1)
                    # Strip any surrounding quotes/spaces
                    val = val.strip().strip("'\"")
                    os.environ[key.strip()] = val
    except Exception as e:
        print(f"WARNING: failed to load env: {e}", file=sys.stderr)

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_with_env.py <command> [args...]", file=sys.stderr)
        sys.exit(1)
        
    env_path = Path("D:/NoteBookLLM_Br/.env")
    load_env(env_path)
    
    cmd = sys.argv[1:]
    
    try:
        # Use shell=True to support running cmd/npm globally on Windows
        res = subprocess.run(cmd, env=os.environ, shell=True)
        sys.exit(res.returncode)
    except Exception as e:
        print(f"ERROR: failed to execute command {cmd}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
