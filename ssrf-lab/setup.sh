#!/usr/bin/env sh
set -eu

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

. ".venv/bin/activate"
python -m pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Setup complete."
echo "Run the lab:"
echo "  FLASK_APP=app.py flask run --debug"
echo "or:"
echo "  python app.py"
echo ""

