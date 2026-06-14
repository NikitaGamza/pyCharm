import re
from collections import Counter
from typing import Dict, List


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Фильтрует список банковских операций по строке поиска в описании операции.
    - data: список словарей с данными операций
    - search: строка поиска
    """
    # автоматически экранируем все спец-символы (метасимволы) в строке через re.escape()
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    result = [
        operation for operation in data if "description" in operation and pattern.search(operation["description"])
    ]

    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> dict:
    """
    Функция вывода количества операций в каждой категории.
    """
    descriptions = [transaction["description"] for transaction in data]
    filtered_descriptions = [desc for desc in descriptions if desc in categories]
    return dict(Counter(filtered_descriptions))
