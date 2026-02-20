def filter_by_state(proc: list[dict], state: str = 'EXECUTED') -> list[dict]:
    return [item for item in proc if item.get('state') == state]


def sort_by_date(proc: list[dict], sequence: bool = False) -> list[dict]:
    return sorted(proc, key=lambda x: x['date'], reverse=sequence)
