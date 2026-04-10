"""
LLM client wrapper for calling 9Router with infrastructure audit logging.
"""
from __future__ import annotations

import json
import os
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
USE_ROUTER = True


def _resolve_router_model(requested_model: Optional[str] = None) -> str:
    """Preserve legacy aliases while allowing explicit upstream model IDs."""
    legacy_aliases = {
        None,
        "",
        "free",
        "fast-engine",
        "power-engine",
        "main-engine",
        "test-9router",
        "flow-test",
    }
    if requested_model in legacy_aliases:
        return SMART_ROUTER_MODEL
    return requested_model


def _call_9router_audit(
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    requested_model: Optional[str] = None,
) -> Any:
    """Call 9Router and emit request metadata for dashboard correlation."""
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


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=4, max=30),
    retry=retry_if_exception_type((Exception,)),
    reraise=True,
)
def _call_with_retry(
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    model: Optional[str] = None,
) -> Any:
    return _call_9router_audit(messages, temperature, max_tokens, requested_model=model)


def call_worker(
    messages: List[Dict[str, str]],
    model: str = "power-engine",
    temperature: float = 0.3,
    max_tokens: int = 1500,
) -> str:
    start = time.time()
    try:
        content, actual_model = _call_with_retry(messages, temperature, max_tokens, model=model)
        elapsed = time.time() - start
        logger.info(f"  Elapsed: {elapsed:.2f}s | Model Used: {actual_model}")
        return content.strip()
    except Exception as exc:
        logger.error(f"  Swarm Hub Failed: {exc}")
        raise


def call_validator(
    messages: List[Dict[str, str]],
    model: str = "main-engine",
    temperature: float = 0.1,
    max_tokens: int = 500,
) -> tuple[str, str]:
    try:
        content, actual_model = _call_with_retry(messages, temperature, max_tokens, model=model)
        return content.strip(), actual_model
    except Exception as exc:
        logger.warning(f"  Validator failed: {exc}")
        raise
