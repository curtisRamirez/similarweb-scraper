thonimport argparse
import json
import logging
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import requests

from extractors.traffic_parser import build_traffic_section
from extractors.keyword_parser import build_keyword_section
from extractors.demographics_parser import build_demographics_section
from extractors.utils_format import (
    clean_domain,
    get_logger,
    load_json_file,
)

from outputs.exporters import export_records

logger = get_logger(__name__)

@dataclass
class ScraperSettings:
    base_url: str = "https://data.similarweb.com"
    api_key: Optional[str] = None
    output_format: str = "json"
    output_dir: str = "data"
    timeout_seconds: int = 15

    @classmethod
    def from_file(cls, path: Path) -> "ScraperSettings":
        if not path.exists():
            logger.warning("Settings file %s not found. Using defaults.", path)
            return cls()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            logger.error("Failed to parse settings JSON at %s: %s", path, exc)
            return cls()

        similarweb_cfg = data.get("similarweb", {})
        general_cfg = data.get("runner", {})

        return cls(
            base_url=similarweb_cfg.get("base_url", cls.base_url),
            api_key=similarweb_cfg.get("api_key") or None,
            output_format=general_cfg.get("output_format", cls.output_format),
            output_dir=general_cfg.get("output_dir", cls.output_dir),
            timeout_seconds=int(general_cfg.get("timeout_seconds", cls.timeout_seconds)),
        )

class SimilarwebClient:
    """
    Very small HTTP client wrapper for Similarweb-like API responses.

    The endpoint/shape here is intentionally generic. In offline mode, this
    client is bypassed.
    """

    def __init__(self, settings: ScraperSettings):
        self.settings = settings
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "SimilarwebScraper/1.0 (+https://bitbash.dev)",
                "Accept": "application/json",
            }
        )

    def fetch_raw_profile(self, domain: str) -> Optional[Dict[str, Any]]:
        """
        Fetch a JSON profile for the given domain.

        This implementation assumes a URL like:
        {base_url}/api/v1/website/{domain}/overview?api_key=...

        Adjust base_url/api_key in settings to match a real endpoint.
        """
        base = self.settings.base_url.rstrip("/")
        url = f"{base}/api/v1/website/{domain}/overview"

        params: Dict[str, Any] = {}
        if self.settings.api_key:
            params["api_key"] = self.settings.api_key

        try:
            logger.info("Fetching Similarweb data for %s", domain)
            resp = self.session.get(url, params=params, timeout=self.settings.timeout_seconds)
            if resp.status_code != 200:
                logger.warning(
                    "Non-200 response for %s: %s %s",
                    domain,
                    resp.status_code,
                    resp.text[:200],
                )
                return None
            return resp.json()
        except requests.RequestException as exc:
            logger.error("Network error while fetching %s: %s", domain, exc)
            return None
        except json.JSONDecodeError as exc:
            logger.error("Failed to decode JSON for %s: %s", domain, exc)
            return None

def load_domains_from_file(path: Path) -> List[str]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    domains: List[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        domains.append(clean_domain(stripped))
    return domains

def load_offline_samples(root_dir: Path) -> Dict[str, Dict[str, Any]]:
    sample_path = root_dir / "data" / "sample.json"
    data = load_json_file(sample_path) or []
    mapping: Dict[str, Dict[str, Any]] = {}
    if isinstance(data, dict):
        # Single sample object
        domain = data.get("overview", {}).get("domain") or data.get("domain")
        if domain:
            mapping[clean_domain(domain)] = data
        return mapping

    for item in data:
        if not isinstance(item, dict):
            continue
        domain = (
            item.get("overview", {}).get("domain")
            or item.get("domain")
            or item.get("meta", {}).get("domain")
        )
        if domain:
            mapping[clean_domain(domain)] = item
    return mapping

def assemble_record(
    domain: str,
    raw_payload: Dict[str, Any],
    search_url: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Combine parsed sections into a single flattened record.
    """
    captured_at = datetime.now(timezone.utc).isoformat()

    traffic = build_traffic_section(raw_payload)
    keywords = build_keyword_section(raw_payload)
    demographics = build_demographics_section(raw_payload)

    record: Dict[str, Any] = {
        "data_captured_at": captured_at,
        "searchUrl": search_url or f"https://www.similarweb.com/website/{domain}/",
        "url": traffic.get("url"),
        "domain": traffic.get("domain", domain),
        "title": traffic.get("title"),
        "description": traffic.get("description"),
        "rankGlobal": traffic.get("rankGlobal"),
        "country": traffic.get("country"),
        "countryRank": traffic.get("countryRank"),
        "category": traffic.get("category"),
        "categoryRank": traffic.get("categoryRank"),
        "totalVisits": traffic.get("totalVisits"),
        "monthlyVisits": traffic.get("monthlyVisits"),
        "website_traffic_by_country": traffic.get("website_traffic_by_country"),
        "engagement": traffic.get("engagement"),
        "directTraffic": traffic.get("directTraffic"),
        "referralTraffic": traffic.get("referralTraffic"),
        "searchTraffic": traffic.get("searchTraffic"),
        "socialTraffic": traffic.get("socialTraffic"),
        "mailTraffic": traffic.get("mailTraffic"),
        "countryShare": traffic.get("countryShare"),
        "previewDesktop": traffic.get("previewDesktop"),
        "previewMobile": traffic.get("previewMobile"),
        "snapshotDate": traffic.get("snapshotDate"),
    }

    record.update(
        {
            "topKeywords": keywords.get("topKeywords"),
            "total_keywords": keywords.get("total_keywords"),
        }
    )

    record.update(
        {
            "company": demographics.get("company"),
            "company_employees": demographics.get("company_employees"),
            "company_revenue_range": demographics.get("company_revenue_range"),
            "company_headquarters": demographics.get("company_headquarters"),
            "age_destribution": demographics.get("age_distribution"),
            "gender_destribution": demographics.get("gender_distribution"),
            "competitors": demographics.get("competitors"),
            "top_interested_websites": demographics.get("top_interested_websites"),
            "top_interested_topics": demographics.get("top_interested_topics"),
            "top_categories": demographics.get("top_categories"),
            "top_competitors": demographics.get("top_competitors"),
            "incoming_referring_domains": demographics.get("incoming_referring_domains"),
            "outgoing_referring_domains": demographics.get("outgoing_referring_domains"),
            "ads_networks": demographics.get("ads_networks"),
            "ads_sites": demographics.get("ads_sites"),
            "social_networks_share": demographics.get("social_networks_share"),
        }
    )

    # Drop None values for a cleaner export
    cleaned = {k: v for k, v in record.items() if v is not None}
    return cleaned

def process_domains(
    domains: Iterable[str],
    settings: ScraperSettings,
    offline_samples: Optional[Dict[str, Dict[str, Any]]] = None,
    offline_only: bool = False,
) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []

    client: Optional[SimilarwebClient] = None
    if not offline_only:
        client = SimilarwebClient(settings)

    for domain in domains:
        domain_clean = clean_domain(domain)
        raw_payload: Optional[Dict[str, Any]] = None
        search_url = None

        if offline_samples and domain_clean in offline_samples:
            logger.info("Using offline sample for %s", domain_clean)
            raw_payload = offline_samples[domain_clean]
            search_url = raw_payload.get("meta", {}).get("searchUrl")

        if raw_payload is None and not offline_only and client is not None:
            raw_payload = client.fetch_raw_profile(domain_clean)

        if raw_payload is None:
            logger.error("No data available for %s; skipping.", domain_clean)
            continue

        record = assemble_record(domain_clean, raw_payload, search_url)
        records.append(record)

    return records

def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Similarweb scraper — collect traffic and intelligence for domains."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        default="data/inputs.sample.txt",
        help="Path to input file with one domain or URL per line.",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Output filename. If not specified, a timestamped file is created in the configured output_dir.",
    )
    parser.add_argument(
        "--format",
        "-f",
        type=str,
        choices=["json", "csv"],
        default=None,
        help="Export format. Overrides value in settings file.",
    )
    parser.add_argument(
        "--settings",
        "-s",
        type=str,
        default="src/config/settings.example.json",
        help="Path to settings JSON file.",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        default=True,
        help="Use built-in offline sample data instead of hitting the network (default: enabled).",
    )
    parser.add_argument(
        "--online",
        action="store_true",
        help="Force online mode and ignore offline sample data.",
    )

    return parser.parse_args(argv)

def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)

    project_root = Path(__file__).resolve().parents[1]