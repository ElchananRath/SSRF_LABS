from __future__ import annotations

import random
import string
import time
import urllib.request
import urllib.parse
from pathlib import Path

from config import (
    LEVEL3_SECRET_URI,
    LEVEL3_SLEEP_SECONDS,
    LEVEL3_WORDLIST_CORRECT_TOKEN,
    LEVEL3_WORDLIST_COUNT,
    flag_uri_for,
)
from levels.common import verify_input


def _normalize_fileish(value: str) -> str:
    """
    Normalize common Windows/Linux file inputs to a canonical file URI.
    This keeps the lab behavior but avoids brittle string-equality issues.
    """
    v = (value or "").strip()
    if not v:
        return v

    try:
        if v.lower().startswith("file:"):
            parsed = urllib.parse.urlparse(v)
            path_str = urllib.request.url2pathname(urllib.parse.unquote(parsed.path))
            return Path(path_str).resolve().as_posix()

        p = Path(v)
        if p.is_absolute():
            return p.resolve().as_posix()
    except Exception:
        return v

    return v


def solve(target_url: str, chosen_path: str):
    if not verify_input(target_url):
        return "fail", "Http or Https request not allowed in input"

    start_time = time.perf_counter()
    try:
        result_status = "fail"

        urllib.request.urlopen(target_url)

        if _normalize_fileish(target_url) == _normalize_fileish(LEVEL3_SECRET_URI):
            time.sleep(LEVEL3_SLEEP_SECONDS)

        end_time = time.perf_counter()
        duration = end_time - start_time

        result = f"Request processed. Response time: {duration:.4f}s"
       

        if _normalize_fileish(chosen_path) == _normalize_fileish(LEVEL3_SECRET_URI):
            result += "good work!"
            result_status = "success"

        return result_status, result
    except Exception:
        duration = time.perf_counter() - start_time
        return "fail", f"Request failed. Response time: {duration:.4f}s"


def _random_token(length: int = 5) -> str:
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for _ in range(length))


def get_wordlist() -> list[str]:
    paths: list[str] = []

    for _ in range(LEVEL3_WORDLIST_COUNT):
        random_val = _random_token()
        paths.append(flag_uri_for(random_val))

    paths.append(flag_uri_for(LEVEL3_WORDLIST_CORRECT_TOKEN))
    random.shuffle(paths)
    return paths

