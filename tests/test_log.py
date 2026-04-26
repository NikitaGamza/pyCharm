from src.decorators import log
import pytest
import os


def divide_function(x, y):
    return x / y

log_divide_function = log(filename="test_log.txt")(divide_function)

@pytest.mark.parametrize("x, y, expected_output", [
    (3, 2, "divide_function ok"),
    (1, 0,"divide_function error: ZeroDivisionError. Inputs: (1, 0), {}")
])


def test_log_to_file(x, y, expected_output):
    log_file = "test_log.txt"
    if os.path.exists(log_file):
        os.remove(log_file)
    if y == 0:
        with pytest.raises(ZeroDivisionError):
            log_divide_function(x, y)
    else:
        log_divide_function(x, y)
    with open(log_file, "r", encoding="utf-8") as file:
        logs = file.read()
        assert expected_output in logs

    if os.path.exists(log_file):
        os.remove(log_file)


@pytest.mark.parametrize("x, y, expected_output", [
    # (3, 2, "divide_function ok"),
    # (1, 0,"divide_function error: ZeroDivisionError. Inputs: (1, 0), {}")
    ])

def test_log_to_console(capsys, x, y, expected_output):
    if y == 0:
        with pytest.raises(ZeroDivisionError):
            divide_function(x, y)
    else:
        divide_function(x, y)
    # Захватываем вывод
    captured = capsys.readouterr()
    assert expected_output in captured.out