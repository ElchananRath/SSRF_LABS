import urllib.request

from config import LEVEL2_STRIP_SUBSTRING, LEVEL2_SUCCESS_MARKER, LEVEL2_TARGET_HINT_FILENAME
from levels.common import verify_input


def solve(target_url: str):
    if not verify_input(target_url):
        return "fail", "Http or Https request not allowed in input"

    if LEVEL2_STRIP_SUBSTRING in target_url.lower():
        target_url = target_url.lower().replace(LEVEL2_STRIP_SUBSTRING, "")

    try:
        response = urllib.request.urlopen(target_url)
        content = response.read().decode("utf-8")

        if LEVEL2_SUCCESS_MARKER in content:
            return "success", content
        return "fail", f"You entered: {target_url} - you need to try to get the {LEVEL2_TARGET_HINT_FILENAME} file"
    except Exception:
        return "fail", f"You entered: {target_url} - wrong syntax!"

