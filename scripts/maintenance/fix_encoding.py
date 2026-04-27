import os

def fix_mojibake(file_path):
    try:
        # Read the file as bytes to avoid any decoding issues
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Check for UTF-8 BOM (EF BB BF)
        if content.startswith(b'\xef\xbb\xbf'):
            content = content[3:]
            print("Removed BOM.")

        # The mojibake happens when UTF-8 bytes are read as a single-byte encoding (like Windows-1252)
        # and then saved as UTF-8.
        # Let's try to reverse it.
        
        # Step 1: Decode the current messed up file as UTF-8
        text = content.decode('utf-8')
        
        # Step 2: Encode back to 'latin-1' (which is identical to the first 256 chars of Unicode and captures the raw bytes)
        # We use 'cp1252' just in case Windows-specific chars were used.
        raw_bytes = text.encode('cp1252')
        
        # Step 3: Decode those raw bytes as UTF-8 (the intended encoding)
        correct_text = raw_bytes.decode('utf-8')
        
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            f.write(correct_text)
        return True
    except Exception as e:
        print(f"Error: {e}")
        # Alternative attempt: just re-encode from the messed up state
        try:
            # Maybe it's just a simple case of wrong reading
            text = content.decode('utf-8')
            # If that doesn't work, we'll need to manually map
            return False
        except:
            return False

if __name__ == "__main__":
    file_path = r"d:\NoteBookLLM_Br\brain\WIKI_INDEX.md"
    if fix_mojibake(file_path):
        print("Successfully fixed encoding for WIKI_INDEX.md")
    else:
        # Emergency backup: If fix failed, I'll try to regenerate it or use a different approach
        print("Failed to fix encoding with cp1252.")
