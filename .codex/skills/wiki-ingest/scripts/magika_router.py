import sys
import subprocess
import json
import os

def get_file_info(file_path):
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    try:
        # Run magika with json output
        result = subprocess.run(
            ['magika', '--json', file_path],
            capture_output=True,
            text=True,
            check=True
        )
        data = json.loads(result.stdout)
        
        # Magika output is a list of results
        file_data = data[0]
        mime_type = file_data.get('output', {}).get('mime_type', 'unknown')
        group = file_data.get('output', {}).get('group', 'unknown')
        
        # Determine parser
        parser = "unknown"
        if mime_type == "application/pdf":
            parser = "docling"
        elif mime_type in ["text/markdown", "text/plain"]:
            parser = "native"
        elif group == "office":
            parser = "markitdown"
        elif group == "code":
            parser = "native"
            
        return {
            "path": file_path,
            "mime_type": mime_type,
            "group": group,
            "parser": parser
        }
        
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python magika_router.py <file_path>")
        sys.exit(1)
        
    info = get_file_info(sys.argv[1])
    print(json.dumps(info, indent=2))
