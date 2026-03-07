from src.processing import filter_by_state


def test_filter_by_state():
    assert filter_by_state([
            {"id": 414288290, "state": "CANCELLED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ], state="SOMESTATE"
        ) == []