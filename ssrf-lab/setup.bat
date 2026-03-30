@echo off
setlocal

REM Create venv if missing
if not exist ".venv\" (
  python -m venv .venv
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Setup complete.
echo Run the lab:
echo   .venv\Scripts\python app.py
echo.
