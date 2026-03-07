from typing import Dict, List, Any


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрации по состоянию"""
    return [item for item in operations if item.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse : bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки по дате"""
    return sorted(operations, key=lambda item : item ["date"][0:11], reverse=reverse )
