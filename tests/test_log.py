from src.decorators import log
import pytest


def test_log():
    @log()
    def div(a, b):
        return a / b
    with pytest.raises(Exception, match='div error: division by zero. Inputs: (2, 0), {}'):
        div(2, 0)