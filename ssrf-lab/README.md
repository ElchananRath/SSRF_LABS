# SSRF Lab (intentionally vulnerable)

This is a small SSRF training lab with multiple levels. **Security issues are intentional** so you can practice exploitation in a safe local environment.

## Quick start

### Windows (PowerShell / CMD)

From the `ssrf-lab` folder:

```bat
setup.bat
.venv\Scripts\python app.py
```

Then open `http://127.0.0.1:5000/`.

### Linux / macOS

From the `ssrf-lab` folder:

```sh
chmod +x setup.sh
./setup.sh
python app.py
```

Then open `http://127.0.0.1:5000/`.

## Project layout

- `app.py`: Flask routes only (no solver logic)
- `config.py`: all constants (paths, secrets, markers)
- `levels/`: per-level solver modules
- `templates/` and `static/`: UI and assets

## Notes

- Flag files live in `static/flags/`.
- Level 3 wordlist uses `file://` URIs built via `pathlib.Path.as_uri()` to work on both Windows and Linux.

