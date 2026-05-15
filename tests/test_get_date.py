from src.widget import get_date

def test_get_date(date):
    assert get_date("2024-03-11T02:26:18.671407") == date