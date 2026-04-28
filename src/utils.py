import json
import os
from typing import Any
import logging

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "operations.json")

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", 'w', encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def info_bank_operations(path: Any) -> list[Any] | None | Any:
    """Функция, возвращающая список финансовых операций"""
    logger.debug(f'Попытка загрузки файла: {path}')
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                result = json.load(f)
                logger.info(f'Данные загружены: {path}')
                return result
            except json.JSONDecodeError:
                result = []
                logger.error("Ошибка чтения файла")
                return result
    except FileNotFoundError as ex:
        logger.error(f'Ошибка: {ex}')
        result = []
    return result
