#!/usr/bin/env python3
"""Search GitHub repositories as a metadata fallback for ReuseAtlas.

This script reports GitHub Search API results only. It does not clone, install,
or execute candidate repositories. Network access is used only when invoked.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

API_URL = "https://api.github.com/search/repositories"
USER_AGENT = "ReuseAtlas-GitHub-Search/1.0"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="GitHub repository search query")
    parser.add_argument("--limit", type=int, default=10, help="results to return (1-100; default: 10)")
    parser.add_argument("--timeout", type=float, default=10.0, help="request timeout in seconds")
    args = parser.parse_args()
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be between 1 and 100")
    if not 0 < args.timeout <= 120:
        parser.error("--timeout must be greater than 0 and at most 120 seconds")
    if not args.query.strip():
        parser.error("query must not be empty")
    return args


def request_results(query: str, limit: int, timeout: float) -> dict:
    params = urlencode({"q": query, "per_page": limit, "sort": "best match"})
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT,
               "X-GitHub-Api-Version": "2022-11-28"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"{API_URL}?{params}", headers=headers)
    try:
        with urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
            remaining = response.headers.get("X-RateLimit-Remaining")
    except HTTPError as exc:
        message = {403: "GitHub rate limit or access denied", 401: "GitHub authentication failed"}.get(
            exc.code, f"GitHub returned HTTP {exc.code}")
        if exc.code == 403 and exc.headers.get("X-RateLimit-Remaining") == "0":
            reset = exc.headers.get("X-RateLimit-Reset")
            message += f"; rate limit resets at Unix time {reset}" if reset else "; rate limit exceeded"
        raise RuntimeError(message) from exc
    except (URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"GitHub request failed: {exc}") from exc
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("GitHub returned an invalid JSON response") from exc

    repositories = []
    for item in payload.get("items", []):
        license_info = item.get("license") or {}
        repositories.append({
            "name": item.get("full_name"),
            "url": item.get("html_url"),
            "description": item.get("description"),
            "language": item.get("language"),
            "stars": item.get("stargazers_count"),
            "forks": item.get("forks_count"),
            "license": license_info.get("spdx_id"),
            "created_at": item.get("created_at"),
            "updated_at": item.get("updated_at"),
            "pushed_at": item.get("pushed_at"),
        })
    return {"query": query, "total_count": payload.get("total_count", 0),
            "incomplete_results": payload.get("incomplete_results", False),
            "rate_limit_remaining": remaining, "repositories": repositories}


def main() -> int:
    args = parse_args()
    try:
        result = request_results(args.query, args.limit, args.timeout)
    except RuntimeError as exc:
        print(json.dumps({"error": str(exc), "query": args.query, "success": False}), file=sys.stderr)
        return 1
    result["success"] = True
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
