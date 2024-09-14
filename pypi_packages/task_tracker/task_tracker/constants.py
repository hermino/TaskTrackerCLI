from pathlib import Path

__script_local__ = Path(__file__).parent

RESOURCES = __script_local__ / "resources"
STORAGE = RESOURCES / "data.json"