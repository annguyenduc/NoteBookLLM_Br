import sys
import os
from pathlib import Path

# Redirect to the new location in .agent/mcp/
new_path = Path(__file__).parent.parent / ".agent" / "mcp" / "notebooklm_bridge.py"

if not new_path.exists():
    sys.stderr.write(f"Error: Target MCP script not found at {new_path}\n")
    sys.exit(1)

# Execute the new script
os.execv(sys.executable, [sys.executable, str(new_path)] + sys.argv[1:])
