
fn = filename.decode('utf-8', errors='ignore').lower()
if fn.endswith('.docx') or fn.endswith('.sb3') or 'test-lms' in fn or 'output_ban_giao' in fn or 'node_modules' in fn or 'trí tuệ nhân tạo' in fn:
    return None
return filename
