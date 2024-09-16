import json
from pathlib import Path

__script_local__ = Path(__file__).parent

RESOURCES = __script_local__ / "resources"
STORAGE = RESOURCES / "data.json"
STORAGE.write_text(json.dumps([], indent=4)) if not STORAGE.exists() else None
