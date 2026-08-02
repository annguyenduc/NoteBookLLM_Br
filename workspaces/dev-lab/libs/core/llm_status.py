import os
import time
import json
import urllib.request
from typing import Tuple, Dict, Any, Optional
from libs.core.logger import get_logger

logger = get_logger("llm_status")

def check_openrouter_health() -> Tuple[bool, str]:
    """
    Kiểm tra xem IP có bị khóa (403) hoặc hết Quota (429) không.
    
    Returns:
        Tuple (is_healthy, message)
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return False, "❌ Thiếu OPENROUTER_API_KEY trong .env"

    logger.info("🔍 Đang kiểm tra trạng thái IP và Quota...")
    
    # Endpoint test đơn giản: Lấy danh sách model
    url = "https://openrouter.ai/api/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/burn-token",
        "X-Title": "Burn Token Health Check",
    }

    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            # 200 OK -> IP không bị chặn
            headers_info = response.info()
            remaining = headers_info.get("X-RateLimit-Remaining")
            limit = headers_info.get("X-RateLimit-Limit")
            reset = headers_info.get("X-RateLimit-Reset")
            
            status_msg = "✅ IP sạch, kết nối OpenRouter bình thường."
            if remaining and limit:
                status_msg += f" (Quota: {remaining}/{limit})"
            
            if reset:
                reset_time = time.strftime('%H:%M:%S', time.localtime(float(reset)))
                logger.debug(f"Rate limit reset lúc: {reset_time}")
                
            return True, status_msg

    except urllib.error.HTTPError as e:
        if e.code == 429:
            reset = e.headers.get("X-RateLimit-Reset")
            wait_str = ""
            if reset:
                wait_sec = int(float(reset) - time.time())
                wait_str = f" | Reset sau {wait_sec}s"
            return False, f"⚠️  Hết Quota tài khoản (429){wait_str}. Hãy đổi Key hoặc đợi reset."
        
        if e.code == 403:
            return False, "🚫 IP của bạn đã bị OpenRouter chặn (403 Forbidden). Hãy dùng VPN/4G hoặc đợi 1-4h."
            
        if e.code == 401:
            return False, "❌ API Key không hợp lệ (401 Unauthorized). Kiểm tra lại file .env"
            
        return False, f"❌ Lỗi kết nối OpenRouter (HTTP {e.code}): {e.reason}"
    
    except Exception as e:
        return False, f"❌ Lỗi không xác định khi check health: {e}"

if __name__ == "__main__":
    # Test nhanh
    ok, msg = check_openrouter_health()
    print(msg)
