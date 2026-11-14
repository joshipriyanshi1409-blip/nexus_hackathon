# Vercel entrypoint. Vercel's Python runtime serves the ASGI `app` object found here;
# vercel.json rewrites every path to this function, so FastAPI still sees the original URL
# (/, /health, /api/...). The UI file is served by the "/" route in backend/app/main.py.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.app.main import app  # noqa: E402,F401
