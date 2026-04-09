from src.decorators import log
import pytest
import os


@log()
def multiplication_function(x, y):
    return x * y


def test_log_to_console(capsys):
    multiplication_function(3, 0)
    captured = capsys.readouterr()
    assert "multiplication_function: ZeroDivisionError. Inputs: (3, 0), {}" in captured.out