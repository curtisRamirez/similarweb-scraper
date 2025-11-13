thonimport json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional
from urllib.parse import urlparse

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

def clean_domain(raw: str) -> str:
    """
    Normalize a domain or URL into a bare domain string.

    Examples: