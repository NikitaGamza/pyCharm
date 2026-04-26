import json
import os
from typing import Any

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "operations.json")


def info_bank_operations(path: Any) -> list[Any] | None | Any:
    """Функция, возвращающая список финансовых операций"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                result = json.load(f)
                return result
            except json.JSONDecodeError:
                result = []
                return result
    except FileNotFoundError:
        result = []
    return result
