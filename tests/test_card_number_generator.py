import pytest
from src.generators import card_number_generator


@pytest.mark.parametrize("start, end, expected", [
    (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    (5, 5, ["0000 0000 0000 0005"]),
])
def test_card_number_generator(start, end, expected):
    result1 = list(card_number_generator(start, end))
    assert result1 == expected