import urllib.request

from flask import render_template_string

from config import LEVEL5_TARGET_NUMBER
from levels.common import verify_input


def solve(target_url: str):
    if not verify_input(target_url):
        return "fail", "Http or Https request not allowed in input"

    try:
        response = urllib.request.urlopen(target_url)
        content = response.read().decode("utf-8")
        result = render_template_string(f"{content}")
        result = f"You entered: {result}"
        if LEVEL5_TARGET_NUMBER in result and LEVEL5_TARGET_NUMBER not in content:
            return "success", result
        if LEVEL5_TARGET_NUMBER in content:
            return "fail", " wrong! "
        return "fail", result
    except Exception:
        return "fail", "The syntax of the input you enterd is wrong"

