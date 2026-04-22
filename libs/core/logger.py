"""
Logger toàn cục cho pipeline — dùng Rich để hiển thị màu sắc đẹp.
Đồng thời ghi log vào file để debug sau.
"""
from __future__ import annotations

import logging
import os
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme


# -----------------------------------------------------------
# Theme màu sắc tùy chỉnh
# -----------------------------------------------------------

CUSTOM_THEME = Theme(
    {
        "info": "cyan",
        "success": "bold green",
        "warning": "bold yellow",
        "error": "bold red",
        "step": "bold magenta",
        "dim": "dim white",
    }
)

# Console dùng chung toàn project
console = Console(theme=CUSTOM_THEME)


def get_logger(name: str = "burn_token", log_dir: str = "./brain/process/storage/logs") -> logging.Logger:
    """
    Tạo và trả về logger chuẩn cho pipeline.

    Args:
        name: Tên logger (thường là __name__ của module gọi)
        log_dir: Thư mục lưu file log

    Returns:
        logging.Logger đã cấu hình sẵn Rich + file handler
    """
    # Tạo thư mục logs nếu chưa có
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)

    # Tên file log theo timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_path / f"pipeline_{timestamp}.log"

    # Cấu hình logger gốc
    logger = logging.getLogger(name)
    if logger.handlers:
        # Tránh thêm handler trùng lặp khi gọi nhiều lần
        return logger

    logger.setLevel(logging.DEBUG)

    # Handler 1: Hiển thị ra terminal với Rich (màu sắc, icon)
    rich_handler = RichHandler(
        console=console,
        show_time=True,
        show_level=True,
        show_path=False,
        markup=True,
        rich_tracebacks=True,
    )
    rich_handler.setLevel(logging.INFO)

    # Handler 2: Ghi toàn bộ log vào file (kể cả DEBUG)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(file_formatter)

    logger.addHandler(rich_handler)
    logger.addHandler(file_handler)

    logger.info(f"[dim]Log file: {log_file}[/dim]")
    return logger
