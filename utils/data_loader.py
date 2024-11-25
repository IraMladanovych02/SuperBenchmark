import json
from pathlib import Path


def load_json_data(file_path: str):
    """Upload data from JSON file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"JSON file {file_path} is not found.")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
