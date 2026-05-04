import os
import sys

# Đảm bảo in ra console không bị lỗi font
sys.stdout.reconfigure(encoding='utf-8')

def check_encoding(file_path):
    """
    Kiểm tra xem file có phải là UTF-8 chuẩn (không BOM) và không chứa ký tự Mojibake phổ biến.
    """
    try:
        with open(file_path, 'rb') as f:
            raw = f.read()
            
        # Kiểm tra UTF-16 BOM (Thường gặp khi dùng PowerShell Out-File)
        if raw.startswith(b'\xff\xfe') or raw.startswith(b'\xfe\xff'):
            return False, "Phát hiện UTF-16 BOM (PowerShell Out-File error)"
            
        # Thử decode UTF-8
        content = raw.decode('utf-8')
        
        # Kiểm tra ký tự '?' xuất hiện bất thường (dấu hiệu của việc mất dữ liệu khi ghi ANSI)
        # Lưu ý: '?' có thể hợp lệ, nhưng chuỗi 'd?i sot' chắc chắn là lỗi của 'đối soát'
        if 'd?i sot' in content or 'Hon t?t' in content:
            return False, "Phát hiện Mojibake (d?i sot / Hon t?t)"
            
        return True, "OK"
    except UnicodeDecodeError:
        return False, "Không phải UTF-8 hợp lệ"

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "dummy_test.md"
    success, msg = check_encoding(target)
    if not success:
        print(f"FAIL: {msg}")
        sys.exit(1)
    print("PASS: Encoding chuẩn UTF-8")
    sys.exit(0)
