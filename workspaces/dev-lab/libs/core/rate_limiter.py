"""
Rate Limiter — Quản lý delay giữa các request để tránh bị OpenRouter chặn.

Giới hạn free tier OpenRouter: ~20 req/phút, ~200 req/ngày.
Module này tự động thêm delay thông minh dựa trên lịch sử request.
"""
from __future__ import annotations

import time
from collections import deque
from threading import Lock


class RateLimiter:
    """
    Token bucket rate limiter đơn giản.

    Đảm bảo không gửi quá N request trong mỗi cửa sổ thời gian T giây.
    Mặc định: 15 req/60s (thấp hơn giới hạn 20 req/60s để có buffer).
    """

    def __init__(
        self,
        max_requests: int = 10,   # Giảm từ 15 -> 10 để an toàn hơn cho Free Tier
        window_seconds: float = 60.0,
        base_delay: float = 5.0,  # Tăng từ 3.0 -> 5.0 để dàn trải requests
    ):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.base_delay = base_delay
        self._timestamps: deque[float] = deque()
        self._lock = Lock()

    def wait(self) -> None:
        """
        Gọi trước mỗi request AI.
        Tự động sleep nếu cần để tránh vượt rate limit.
        """
        with self._lock:
            now = time.time()

            # Loại bỏ timestamp cũ hơn cửa sổ
            while self._timestamps and now - self._timestamps[0] > self.window_seconds:
                self._timestamps.popleft()

            # Nếu đã đủ request trong cửa sổ → cần đợi
            if len(self._timestamps) >= self.max_requests:
                oldest = self._timestamps[0]
                wait_time = self.window_seconds - (now - oldest) + 0.5  # +0.5s buffer
                if wait_time > 0:
                    time.sleep(wait_time)

            # Delay tối thiểu giữa các request + Jitter ngẫu nhiên
            import random
            if self._timestamps:
                elapsed = time.time() - self._timestamps[-1]
                jitter = random.uniform(0.5, 1.5)  # Thêm 0.5s - 1.5s ngẫu nhiên
                required = self.base_delay + jitter
                if elapsed < required:
                    time.sleep(required - elapsed)

            self._timestamps.append(time.time())

    def reset(self) -> None:
        """Reset bộ đếm (dùng khi chuyển sang model mới)."""
        with self._lock:
            self._timestamps.clear()


class ExponentialBackoff:
    """
    Tính thời gian chờ khi gặp lỗi 429 Rate Limit.

    Công thức: delay = base * (2 ^ attempt) + jitter
    Ví dụ: lần 1 = 4s, lần 2 = 8s, lần 3 = 16s (cộng thêm jitter ngẫu nhiên)
    """

    def __init__(
        self,
        base: float = 2.0,
        max_delay: float = 120.0,
    ):
        self.base = base
        self.max_delay = max_delay

    def get_delay(self, attempt: int) -> float:
        """
        Trả về số giây cần đợi.

        Args:
            attempt: Số lần retry đã thực hiện (bắt đầu từ 0)
        """
        import random
        delay = self.base * (2 ** attempt)
        jitter = random.uniform(0, min(delay * 0.1, 5))  # Tối đa 5s jitter
        return min(delay + jitter, self.max_delay)


# Singleton dùng chung toàn pipeline
# worker và validator dùng chung limiter vì cùng 1 API key
_default_limiter = RateLimiter(max_requests=15, window_seconds=60, base_delay=3.0)


def get_limiter() -> RateLimiter:
    """Trả về RateLimiter singleton."""
    return _default_limiter
