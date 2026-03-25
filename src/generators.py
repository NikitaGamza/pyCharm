from typing import Any, Dict, List

def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> List[Dict[str, Any]]:
    '''Генератор фильтрации по заданной валюте'''
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction