from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """
      Декоратор логирования  начала и конца выполнения функции, ее результаты и возникшие ошибки.
     Принимать необязательный аргумент 'filename', определяющий,
    куда будут записываться логи (в файл или в консоль)
    """

    def wrapper(function: Any) -> Any:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)
                log_message = f"{function.__name__} ok\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                raise

        return inner

    return wrapper
