from functools import wraps
from typing import Callable, Any

def log(filename: str = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор логирования начала и конца выполнения функции, ее результаты или возникшие ошибки.
    Принимает необязательный аргумент 'filename', который определяет,
    куда будут записываться логи (в файл или в консоль)
    """

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"Function: {func.__name__} ok. Result: {result}\n")
                else:
                    print(f"Function: {func.__name__} ok. Result: {result}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return my_decorator