from typing import Dict, List


def filter_by_state(operations: List[Dict[str, str | int]], state: str = "EXECUTED") -> List[Dict[str, str | int]]:
    """Функция фильтрации по состоянию"""
    return [item for item in operations if item.get("state") == state]


def sort_by_date(operations: List[Dict[str, str]], reverse : bool = True) -> List[Dict[str, str]]:
    """Функция сортировки по дате"""
    return sorted(operations, key=lambda item : item ["date"][0:11], reverse=reverse )
