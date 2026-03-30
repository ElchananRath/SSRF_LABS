from __future__ import annotations

import sys
from pathlib import Path

from flask import Flask, render_template, request

# Allow running from repo root (python ssrf-lab/app.py) as well as from the ssrf-lab folder.
_APP_DIR = Path(__file__).resolve().parent
if str(_APP_DIR) not in sys.path:
    sys.path.insert(0, str(_APP_DIR))

from config import FLAG1_PATH, FLAG2_PATH
from levels import (
    get_wordlist,
    level1_solve,
    level2_solve,
    level3_solve,
    level4_solve,
    level5_solve,
)

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/level1", methods=["GET", "POST"])
def level1():
    result = None
    result_status = None
    flag_path = str(FLAG1_PATH.resolve())

    if request.method == "POST":
        user_input = request.form.get("url", "")
        result_status, result = level1_solve(user_input)

    return render_template("level1.html", result=result, result_status=result_status, flag_path=flag_path)

@app.route("/level2", methods=["GET", "POST"])
def level2():
    result = None
    result_status = None
    flag_path = str(FLAG2_PATH.resolve())
    
    if request.method == "POST":
        user_input = request.form.get("url", "")
        result_status, result = level2_solve(user_input)
    

    return render_template("level2.html", result=result, result_status=result_status, flag_path=flag_path)

@app.route("/level3", methods=["GET", "POST"])
def level3():
    result = None
    result_status = None
    flag_paths = get_wordlist()

    if request.method == "POST":
        user_input = request.form.get("url", "").strip()
        user_ans = request.form.get("ans", "").strip()
        result_status, result = level3_solve(user_input, user_ans)

    return render_template("level3.html", result=result, result_status=result_status, flag_paths=flag_paths)

@app.route("/level4", methods=["GET", "POST"])
def level4():
    result = None
    result_status = None

    if request.method == "POST":
        user_input = request.form.get("url", "")
        user_ans = request.form.get("ans", "")
        result_status, result = level4_solve(user_input, user_ans)

    return render_template("level4.html", result=result, result_status=result_status)

@app.route("/level5", methods=["GET", "POST"])
def level5():
    result = None
    result_status = None

    if request.method == "POST":
        target_url = request.form.get("url", "")
        result_status, result = level5_solve(target_url)

    return render_template("level5.html", result=result, result_status=result_status)

if __name__ == "__main__":
    app.run(debug=True)