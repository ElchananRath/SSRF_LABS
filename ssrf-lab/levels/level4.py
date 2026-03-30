import urllib.request

from config import (
    LEVEL4_BLOCKED_SUBSTRINGS,
    LEVEL4_CHALLENGE_SECRET,
    LEVEL4_REQUEST_TIMEOUT_SECONDS,
    LEVEL4_USER_AGENT_PREFIX,
)


def solve(target_url: str, user_ans: str):
    if any(b in target_url.lower() for b in LEVEL4_BLOCKED_SUBSTRINGS):
        return "fail", "local host wont help you here"

    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": f"{LEVEL4_USER_AGENT_PREFIX}{LEVEL4_CHALLENGE_SECRET}"},
        )

        urllib.request.urlopen(req, timeout=LEVEL4_REQUEST_TIMEOUT_SECONDS)

        if user_ans != LEVEL4_CHALLENGE_SECRET:
            return "fail", "what is the User-Agent?"
        return "success", "good work!"
    except Exception as e:
        return "fail", f"error sending request: {str(e)}"

