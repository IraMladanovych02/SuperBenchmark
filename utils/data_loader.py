import json
from pathlib import Path


def load_json_data(file_path: str):
    """Завантаження даних із JSON-файлу."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"JSON файл {file_path} не знайдено.")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
