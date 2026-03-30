import urllib.request

from config import LEVEL1_SUCCESS_MARKER, LEVEL1_TARGET_HINT_FILENAME
from levels.common import verify_input


def solve(target_url: str):
    if not verify_input(target_url):
        return "fail", "Http or Https request not allowed in input"

    try:
        response = urllib.request.urlopen(target_url)
        content = response.read().decode("utf-8")

        if LEVEL1_SUCCESS_MARKER in content:
            return "success", content
        return "fail", f"You entered: {target_url} - you need to try to get the {LEVEL1_TARGET_HINT_FILENAME} file"
    except Exception:
        return "fail", f"You entered: {target_url} - wrong syntax!"

