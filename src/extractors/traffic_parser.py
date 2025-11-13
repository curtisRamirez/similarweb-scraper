thonfrom datetime import datetime
from typing import Any, Dict, List, Optional

from .utils_format import safe_get, normalize_percentage

def _parse_overview(raw: Dict[str, Any]) -> Dict[str, Any]:
    overview = raw.get("overview", {}) or {}
    meta = raw.get("meta", {}) or {}

    url = overview.get("url") or meta.get("url")
    domain = overview.get("domain") or meta.get("domain")
    return {
        "url": url or (f"https://{domain}" if domain else None),
        "domain": domain,
        "title": overview.get("title") or meta.get("title"),
        "description": overview.get("description") or meta.get("description"),
        "rankGlobal": overview.get("rankGlobal"),
        "country": overview.get("country") or