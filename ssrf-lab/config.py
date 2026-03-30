from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

STATIC_DIR = PROJECT_ROOT / "static"
FLAGS_DIR = STATIC_DIR / "flags"

# Flag files
FLAG1_PATH = FLAGS_DIR / "flag1.txt"
FLAG2_PATH = FLAGS_DIR / "flag2.txt"
FLAG3_PATH = FLAGS_DIR / "flagxywin.txt"

# Used to build wordlist entries for Level 3 (file:// URIs)
FLAG_TEMPLATE_NAME = "flag{token}.txt"


def flag_uri_for(token: str) -> str:
    # file:///... URI (works across Windows/Linux via Path)
    return (FLAGS_DIR / FLAG_TEMPLATE_NAME.format(token=token)).resolve().as_posix()


# Level 1
LEVEL1_SUCCESS_MARKER = "ssrfBasikWork!"
LEVEL1_TARGET_HINT_FILENAME = "flag1.txt"

# Level 2
LEVEL2_SUCCESS_MARKER = "ssrfValidationmistakes!"
LEVEL2_TARGET_HINT_FILENAME = "flag2.txt"
LEVEL2_STRIP_SUBSTRING = "file"

# Level 3
LEVEL3_SECRET_URI = FLAG3_PATH.resolve().as_posix()
LEVEL3_WORDLIST_COUNT = 100
LEVEL3_WORDLIST_CORRECT_TOKEN = "xywin"
LEVEL3_SLEEP_SECONDS = 2

# Level 4
LEVEL4_CHALLENGE_SECRET = "LEVE4_PWNED"
LEVEL4_BLOCKED_SUBSTRINGS = ["localhost", "127.0.0.1", "0.0.0.0", "192.168", "10.0"]
LEVEL4_USER_AGENT_PREFIX = "SSRF-Lab-Bot-"
LEVEL4_REQUEST_TIMEOUT_SECONDS = 5

# Level 5
LEVEL5_TARGET_NUMBER = "67"

