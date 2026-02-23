from typing import Dict, List


def filter_by_state(operations: List[Dict[str, str | int]], state: str = "EXECUTED") -> List[Dict[str, str | int]]:
    """Функция фильтрации по состоянию"""
    return [item for item in operations if item.get("state") == state]


def sort_by_date(operations: List[Dict[str, str | int]], sequence: bool = False) -> List[Dict[str, str | int]]:
    """Функция сортировки по дате"""
    return sorted(operations, key=lambda date: date["date"][:11], reverse=sequence)
