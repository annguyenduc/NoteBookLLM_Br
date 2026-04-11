"""
LLM client wrapper for calling 9Router with infrastructure audit logging.

Changelog (patch v2):
- [FIX 1] call_worker default model: "power-engine" → "ag/gemini-3-flash" (tránh bị resolve về gemini âm thầm)
- [FIX 2] call_pedagogical_agent + toàn bộ wrapper thêm tham số `model` để override preset
- [NEW] MODEL_FALLBACK_CHAINS: lộ trình dự phòng per-model
- [NEW] _classify_error: phân loại 404/429/502 để xử lý đúng cách
- [NEW] _call_with_fallback: thay thế _call_with_retry, tự động switch model khi 404, wait khi 429
- [REFACTOR] _resolve_router_model: ưu tiên model được truyền trực tiếp, legacy aliases chỉ là fallback
"""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import litellm
import requests
from dotenv import load_dotenv
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from libs.core.logger import get_logger


litellm.suppress_debug_info = True
logger = get_logger("llm_client")


def _sync_env_keys() -> None:
    proxy_env = Path("D:/01_Workspaces/SmartProxyHub/.env")
    if proxy_env.exists():
        load_dotenv(dotenv_path=proxy_env, override=True)
        logger.info(f"Keys synced from {proxy_env}")


_sync_env_keys()

SMART_ROUTER_URL = os.getenv("SMART_ROUTER_URL", "http://localhost:20128/v1/chat/completions")
SMART_ROUTER_KEY = os.getenv("NINEROUTER_API_KEY")
SMART_ROUTER_MODEL = os.getenv(
    "SMART_ROUTER_MODEL",
    "ag/gemini-3-flash",
)
PEDAGOGICAL_MODEL_PRESET = os.getenv("PEDAGOGICAL_MODEL_PRESET", "free")
USE_ROUTER = True

PEDAGOGICAL_MODEL_PRESETS: Dict[str, Dict[str, str]] = {
    "free": {
        "profiler": "groq/llama-3.3-70b-versatile",
        "designer": "groq/qwen/qwen3-32b",
        "engineer": "groq/llama-3.3-70b-versatile",
        "evaluator": "groq/qwen/qwen3-32b",
        "creative": "nvidia/moonshotai/kimi-k2.5",
        "auditor": "groq/qwen/qwen3-32b",
    },
    "balanced": {
        "profiler": "ag/gemini-3-flash",
        "designer": "ag/claude-sonnet-4-6",
        "engineer": "ag/gemini-3-flash",
        "evaluator": "ag/gemini-3.1-pro-low",
        "creative": "ag/claude-sonnet-4-6",
        "auditor": "ag/claude-opus-4-6-thinking",
    },
}

# [NEW] Lộ trình dự phòng khi model chính gặp lỗi 404/429
# Thứ tự: [primary, fallback_1, fallback_2]
MODEL_FALLBACK_CHAINS: Dict[str, List[str]] = {
    "ag/gemini-3-flash":            ["ag/gemini-3-flash", "groq/llama-3.3-70b-versatile", "ag/gemini-3.1-pro-low"],
    "ag/gemini-3.1-pro-low":        ["ag/gemini-3.1-pro-low", "ag/gemini-3-flash", "groq/llama-3.3-70b-versatile"],
    "ag/claude-sonnet-4-6":         ["ag/claude-sonnet-4-6", "ag/gemini-3.1-pro-low", "ag/gemini-3-flash"],
    "ag/claude-opus-4-6-thinking":  ["ag/claude-opus-4-6-thinking", "ag/claude-sonnet-4-6", "ag/gemini-3.1-pro-low"],
    "groq/llama-3.3-70b-versatile": ["groq/llama-3.3-70b-versatile", "ag/gemini-3-flash"],
    "groq/qwen/qwen3-32b":          ["groq/qwen/qwen3-32b", "groq/llama-3.3-70b-versatile", "ag/gemini-3-flash"],
    "nvidia/moonshotai/kimi-k2.5":  ["nvidia/moonshotai/kimi-k2.5", "ag/claude-sonnet-4-6", "ag/gemini-3-flash"],
}

ROLE_ALIASES: Dict[str, str] = {
    "profile": "profiler",
    "profiler": "profiler",
    "design": "designer",
    "designer": "designer",
    "engineer": "engineer",
    "create": "creative",
    "creative": "creative",
    "evaluate": "evaluator",
    "evaluator": "evaluator",
    "audit": "auditor",
    "auditor": "auditor",
}

PEDAGOGICAL_SYSTEM_PROMPTS: Dict[str, str] = {
    "profiler": (
        "Ban la @profiler trong Swarm pedagogical pipeline. "
        "Nhiem vu cua ban la xac dinh muc do trainer (entry/intermediate/advanced), "
        "tom tat boi canh, diem manh, khoang trong nang luc, va nhu cau ho tro. "
        "Tra ve ngan gon, co cau truc, uu tien phan loai ro rang va khuyen nghi hanh dong tiep theo."
    ),
    "designer": (
        "Ban la @designer trong Swarm pedagogical pipeline. "
        "Hay thiet ke learning sequence dua tren Trainer Profile va muc tieu hoc tap. "
        "Bat buoc uu tien logic su pham theo 5E, UDL, Backward Design, co scaffold ro rang, "
        "ket qua hoc tap cu the, va hoat dong phu hop voi trinh do trainer. "
        "Khong hien thi chain-of-thought, khong xuat the <think>, chi tra ve cau tra loi cuoi cung co cau truc."
    ),
    "engineer": (
        "Ban la @engineer trong Swarm pedagogical pipeline. "
        "Ban khong tu y dat lai thiet ke su pham. "
        "Hay tao noi dung dao tao, lesson draft, worksheet, quiz, hoac scenario "
        "dua chat che vao Trainer Profile va Learning Design da co."
    ),
    "evaluator": (
        "Ban la @evaluator trong Swarm pedagogical pipeline. "
        "Hay danh gia ket qua dao tao bang cach xac dinh knowledge gap, diem nghen, "
        "va remediation path theo tu duy Kirkpatrick Level 1-4. "
        "Tra ve nhan dinh ngan gon, co uu tien va co buoc tiep theo. "
        "Khong hien thi chain-of-thought, khong xuat the <think>, chi dua ra ket luan va de xuat."
    ),
    "creative": (
        "Ban la @creative trong Swarm pedagogical pipeline. "
        "Hay tao case study, roleplay, tinh huong lop hoc, va vi du co tinh thuc te cao, "
        "hap dan, dung boi canh giao duc, va van phuc vu muc tieu hoc tap."
    ),
    "auditor": (
        "Ban la @auditor trong Swarm pedagogical pipeline. "
        "Khong dung general knowledge de bo sung claim. "
        "Neu thong tin khong du, phai neu ro khong du nguon. "
        "Uu tien doi soat tinh nhat quan, tinh xac thuc, va phat hien hallucination hoac vuot scope. "
        "Khong hien thi chain-of-thought, khong xuat the <think>, chi tra ve nhan dinh cuoi cung."
    ),
}


def get_pedagogical_model(role: str, preset: Optional[str] = None) -> str:
    """Resolve a pedagogical role to a concrete 9Router model."""
    normalized_role = ROLE_ALIASES.get(role.strip().lower(), role.strip().lower())
    active_preset = (preset or PEDAGOGICAL_MODEL_PRESET).strip().lower()
    registry = PEDAGOGICAL_MODEL_PRESETS.get(active_preset, PEDAGOGICAL_MODEL_PRESETS["free"])
    return registry.get(normalized_role, SMART_ROUTER_MODEL)


def _normalize_role(role: str) -> str:
    return ROLE_ALIASES.get(role.strip().lower(), role.strip().lower())


def _with_system_prompt(role: str, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
    normalized_role = _normalize_role(role)
    system_prompt = PEDAGOGICAL_SYSTEM_PROMPTS.get(normalized_role)
    if not system_prompt:
        return messages
    if messages and messages[0].get("role") == "system":
        return messages
    return [{"role": "system", "content": system_prompt}, *messages]


def _sanitize_pedagogical_output(content: str) -> str:
    cleaned = re.sub(r"<think>.*?</think>\s*", "", content, flags=re.DOTALL | re.IGNORECASE)
    return cleaned.strip()


# [REFACTOR] _resolve_router_model: ưu tiên model hợp lệ được truyền trực tiếp
# Legacy aliases chỉ được resolve khi không có model cụ thể nào được chỉ định
_LEGACY_ALIASES = {None, "", "free", "fast-engine", "power-engine", "main-engine", "test-9router", "flow-test"}


def _resolve_router_model(requested_model: Optional[str] = None) -> str:
    """
    Giải quyết model theo thứ tự ưu tiên:
    1. model được truyền trực tiếp với prefix ag/ hoặc groq/ hoặc nvidia/ → dùng nguyên
    2. role prefix "role:xxx" → tra bảng pedagogical
    3. legacy alias hoặc None → fallback về SMART_ROUTER_MODEL
    """
    if requested_model in _LEGACY_ALIASES:
        return SMART_ROUTER_MODEL
    if requested_model and requested_model.startswith("role:"):
        return get_pedagogical_model(requested_model.split(":", 1)[1])
    # Model ID hợp lệ được truyền trực tiếp — dùng nguyên, không override
    return requested_model


def _build_fallback_chain(model: str) -> List[str]:
    """Trả về danh sách model theo thứ tự ưu tiên. Luôn có ít nhất 1 phần tử."""
    return MODEL_FALLBACK_CHAINS.get(model, [model, SMART_ROUTER_MODEL])


def _call_9router_audit(
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    requested_model: Optional[str] = None,
) -> Any:
    """Call 9Router và emit request metadata cho dashboard correlation."""
    effective_model = _resolve_router_model(requested_model)
    headers = {
        "Authorization": f"Bearer {SMART_ROUTER_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": effective_model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }

    response = requests.post(SMART_ROUTER_URL, headers=headers, json=payload, timeout=180)
    header_request_id = response.headers.get("x-request-id") or response.headers.get("request-id")
    logger.info(
        f"[9Router Audit] Status: {response.status_code} | Request ID: {header_request_id or 'N/A'} | Model Sent: {effective_model}"
    )

    if response.status_code != 200:
        raise Exception(f"9Router Error ({response.status_code}): {response.text}")

    raw_text = response.text.strip()
    if "data: [DONE]" in raw_text:
        raw_text = raw_text.split("data: [DONE]")[0].strip()

    try:
        json_data = json.loads(raw_text)
        content = json_data["choices"][0]["message"]["content"]
        req_id = json_data.get("id") or header_request_id or "N/A"
        actual_model = json_data.get("model", effective_model)
        logger.info(f"  OK Request ID: {req_id} | Model Returned: {actual_model} | Status: OK")
        return content, actual_model
    except Exception as exc:
        logger.error(f"Logic Parse JSON error: {exc}")
        raise


# [NEW] Phân loại lỗi để quyết định hành động
def _classify_error(exc: Exception) -> str:
    """
    Phân loại lỗi:
    - 'switch' : 404 model not found → đổi sang model tiếp theo trong chain
    - 'wait'   : 429 rate limit → chờ rồi retry cùng model
    - 'retry'  : 502/503 upstream tạm lỗi → retry cùng model
    - 'fatal'  : lỗi khác → raise ngay
    """
    msg = str(exc)
    if "404" in msg or "model_not_found" in msg or "No active credentials" in msg:
        return "switch"
    if "429" in msg or "rate_limit" in msg or "quota" in msg:
        return "wait"
    if "502" in msg or "503" in msg or "fetch failed" in msg:
        return "retry"
    return "fatal"


# [NEW] Thay thế _call_with_retry bằng logic fallback thông minh
def _call_with_fallback(
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    model: Optional[str] = None,
) -> Any:
    """
    Gọi 9Router với cơ chế fallback thông minh:
    - 404 → switch sang model tiếp theo trong fallback chain
    - 429 → wait 10-30s rồi retry cùng model (tối đa 2 lần)
    - 502/503 → retry tối đa 3 lần với exponential backoff
    - fatal → raise ngay
    """
    effective_model = _resolve_router_model(model)
    chain = _build_fallback_chain(effective_model)

    last_exc: Optional[Exception] = None

    for candidate in chain:
        retry_count = 0
        max_retries = 3
        while retry_count < max_retries:
            try:
                logger.info(f"[Fallback] Trying model: {candidate} (attempt {retry_count + 1}/{max_retries})")
                result = _call_9router_audit(messages, temperature, max_tokens, requested_model=candidate)
                return result
            except Exception as exc:
                action = _classify_error(exc)
                last_exc = exc

                if action == "switch":
                    logger.warning(f"[Fallback] 404 on '{candidate}', switching to next model in chain.")
                    break  # Thoát while, thử model tiếp theo trong chain

                elif action == "wait":
                    wait_time = 10 * (retry_count + 1)  # 10s, 20s, 30s
                    logger.warning(f"[Fallback] 429 on '{candidate}', waiting {wait_time}s before retry...")
                    time.sleep(wait_time)
                    retry_count += 1

                elif action == "retry":
                    wait_time = 4 * (2 ** retry_count)  # 4s, 8s, 16s
                    logger.warning(f"[Fallback] 502 on '{candidate}', retrying in {wait_time}s ({retry_count + 1}/{max_retries})...")
                    time.sleep(wait_time)
                    retry_count += 1

                else:
                    # Fatal: không retry, raise ngay
                    logger.error(f"[Fallback] Fatal error on '{candidate}': {exc}")
                    raise

    logger.error(f"[Fallback] All models in chain exhausted. Last error: {last_exc}")
    raise last_exc


def call_worker(
    messages: List[Dict[str, str]],
    model: str = "ag/gemini-3-flash",  # [FIX 1] Đổi từ "power-engine" → model ID thực để tránh bị resolve âm thầm
    temperature: float = 0.3,
    max_tokens: int = 1500,
) -> str:
    start = time.time()
    try:
        content, actual_model = _call_with_fallback(messages, temperature, max_tokens, model=model)
        elapsed = time.time() - start
        logger.info(f"  Elapsed: {elapsed:.2f}s | Model Used: {actual_model}")
        return content.strip()
    except Exception as exc:
        logger.error(f"  Swarm Hub Failed: {exc}")
        raise


def call_validator(
    messages: List[Dict[str, str]],
    model: str = "ag/gemini-3-flash",  # [FIX 1] Đổi từ "main-engine"
    temperature: float = 0.1,
    max_tokens: int = 500,
) -> tuple[str, str]:
    try:
        content, actual_model = _call_with_fallback(messages, temperature, max_tokens, model=model)
        return content.strip(), actual_model
    except Exception as exc:
        logger.warning(f"  Validator failed: {exc}")
        raise


def call_pedagogical_agent(
    role: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.2,
    max_tokens: int = 1500,
    preset: Optional[str] = None,
    model: Optional[str] = None,  # [FIX 2] Cho phép override model, bỏ qua preset
) -> tuple[str, str]:
    """
    Gọi 9Router với model được map theo pedagogical agent role.

    Thứ tự ưu tiên model:
    1. `model` nếu được truyền trực tiếp (override tất cả)
    2. preset → role → PEDAGOGICAL_MODEL_PRESETS
    3. SMART_ROUTER_MODEL (fallback cuối)
    """
    normalized_role = _normalize_role(role)
    resolved_model = model if model else get_pedagogical_model(normalized_role, preset=preset)
    routed_messages = _with_system_prompt(normalized_role, messages)
    content, actual_model = _call_with_fallback(routed_messages, temperature, max_tokens, model=resolved_model)
    return _sanitize_pedagogical_output(content), actual_model


# [FIX 2] Toàn bộ wrapper thêm tham số model để pass xuống call_pedagogical_agent

def call_profiler(
    messages: List[Dict[str, str]],
    max_tokens: int = 1200,
    preset: Optional[str] = None,
    model: Optional[str] = None,
) -> tuple[str, str]:
    return call_pedagogical_agent("profiler", messages, temperature=0.2, max_tokens=max_tokens, preset=preset, model=model)


def call_designer(
    messages: List[Dict[str, str]],
    max_tokens: int = 1800,
    preset: Optional[str] = None,
    model: Optional[str] = None,
) -> tuple[str, str]:
    return call_pedagogical_agent("designer", messages, temperature=0.3, max_tokens=max_tokens, preset=preset, model=model)


def call_pedagogical_engineer(
    messages: List[Dict[str, str]],
    max_tokens: int = 1800,
    preset: Optional[str] = None,
    model: Optional[str] = None,
) -> tuple[str, str]:
    return call_pedagogical_agent("engineer", messages, temperature=0.3, max_tokens=max_tokens, preset=preset, model=model)


def call_evaluator(
    messages: List[Dict[str, str]],
    max_tokens: int = 1400,
    preset: Optional[str] = None,
    model: Optional[str] = None,
) -> tuple[str, str]:
    return call_pedagogical_agent("evaluator", messages, temperature=0.2, max_tokens=max_tokens, preset=preset, model=model)


def call_creative(
    messages: List[Dict[str, str]],
    max_tokens: int = 1800,
    preset: Optional[str] = None,
    model: Optional[str] = None,
) -> tuple[str, str]:
    return call_pedagogical_agent("creative", messages, temperature=0.5, max_tokens=max_tokens, preset=preset, model=model)


def call_auditor(
    messages: List[Dict[str, str]],
    max_tokens: int = 1400,
    preset: Optional[str] = None,
    model: Optional[str] = None,
) -> tuple[str, str]:
    return call_pedagogical_agent("auditor", messages, temperature=0.1, max_tokens=max_tokens, preset=preset, model=model)
