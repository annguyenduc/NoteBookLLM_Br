"""
LLM Discovery Engine — Tự động tìm kiếm và lọc các model miễn phí chất lượng cao.
Tính năng:
  - Gọi API OpenRouter để lấy danh sách model mới nhất.
  - Lọc các model ':free' và có tham số > 10B.
  - Loại bỏ các model nhỏ (1b, 3b, 8b) hoặc lỗi thời.
"""
import urllib.request
import json
import re
from typing import List, Dict, Any
from libs.core.logger import get_logger

logger = get_logger("llm_discovery")

OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"

# Các từ khóa nhận diện model "nhỏ" (< 10B) để loại bỏ
SMALL_MODEL_KEYWORDS = [
    r"1b", r"3b", r"7b", r"8b", r"tiny", r"small", r"nano", r"micro", 
    r"phi-3-mini", r"gemma-2b", r"llama-3-8b", r"llama-3.1-8b", r"llama-3.2-1b", r"llama-3.2-3b"
]

_cached_workers = None

def get_dynamic_free_workers(force_refresh: bool = False) -> List[str]:
    """
    Lấy danh sách các model miễn phí chất lượng cao (>10B) từ OpenRouter.
    Có cơ chế cache để tránh gọi API nhiều lần.
    """
    global _cached_workers
    if _cached_workers and not force_refresh:
        return _cached_workers

    logger.info("🔍 Đang rà soát danh sách model miễn phí trên OpenRouter...")
    try:
        req = urllib.request.Request(OPENROUTER_MODELS_URL)
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read())
            all_models = data.get("data", [])
            
            free_workers = []
            for m in all_models:
                mid = m.get("id", "")
                
                # Chỉ lấy model FREE
                if not mid.endswith(":free"):
                    continue
                
                # Lọc bỏ model nhỏ (<10B)
                is_small = False
                for kw in SMALL_MODEL_KEYWORDS:
                    if re.search(kw, mid.lower()):
                        is_small = True
                        break
                
                if is_small:
                    logger.debug(f"  Bỏ qua model nhỏ: {mid}")
                    continue
                
                # Loại bỏ model Vision/VL (thường chậm hoặc không tối ưu dịch văn bản)
                if "vision" in mid.lower() or "-vl" in mid.lower():
                    continue

                free_workers.append(f"openrouter/{mid}" if not mid.startswith("openrouter/") else mid)
                
            logger.info(f"✅ Tìm thấy {len(free_workers)} model chất lượng cao (>10B) đang miễn phí.")
            # Ưu tiên các model khủng lên đầu (405B, 70B, 72B)
            free_workers.sort(key=lambda x: ("405b" in x.lower() or "70b" in x.lower() or "72b" in x.lower() or "120b" in x.lower()), reverse=True)
            
            _cached_workers = free_workers # Lưu vào cache
            return free_workers

    except Exception as e:
        logger.error(f"❌ Lỗi khi quét danh sách model: {e}")
        # Trả về danh sách fallback cứng nếu API discovery lỗi
        return [
            "openrouter/meta-llama/llama-3.3-70b-instruct:free",
            "openrouter/nousresearch/hermes-3-llama-3.1-405b:free",
            "openrouter/qwen/qwen-2.5-72b-instruct:free",
            "openrouter/nvidia/nemotron-3-super-120b-a12b:free"
        ]

if __name__ == "__main__":
    # Test nhanh
    models = get_dynamic_free_workers()
    for m in models:
        print(f"  - {m}")
