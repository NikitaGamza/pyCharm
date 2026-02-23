from typing import Dict, List


def filter_by_state(proc: List[Dict[str, str | int]], state: str = "EXECUTED") -> List[Dict[str, str | int]]:
    """Функция фильтрации по состоянию"""
    return [item for item in proc if item.get("state") == state]


def sort_by_date(proc: List[Dict[str, str | int]], sequence: bool = False) -> List[Dict[str, str | int]]:
    """Функция сортировки по дате"""
    return sorted(proc, key=lambda x: x["date"][:11], reverse=sequence)
