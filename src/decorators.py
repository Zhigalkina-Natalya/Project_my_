"""
Напишите декоратор log, который будет автоматически логировать начало и конец выполнения функции,а также ее результаты
или возникшие ошибки. Декоратор должен принимать необязательный аргумент filename, который определяет, куда будут
записываться логи (в файл или в консоль): Если filename задан, логи записываются в указанный файл.
Если filename не задан, логи выводятся в консоль.
Логирование должно включать:
Имя функции и результат выполнения при успешной операции.
Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
"""

import datetime
from functools import wraps
from typing import Any, Callable, Optional, TypeVar

# Создаем переменную типа для возвращаемого значения декорируемой функции
T = TypeVar("T")  # T - это общий тип (может быть int, str, list и т.д.)


def log(filename: Optional[str] = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            try:
                # Логируем успешную работу функции.
                start_time = datetime.datetime.now()
                result: T = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                success_msg = f"{func.__name__} ok\n" f"Result: {result}. Execution time: {end_time - start_time}\n"

                if filename:
                    with open(filename, mode="a", encoding="utf-8") as file:
                        file.write(success_msg)
                else:
                    print(success_msg)
                return result
            # Логируем ошибку
            except Exception as e:
                error_time = datetime.datetime.now()
                error_msg = (
                    f"{func.__name__} error:\n"
                    f"{type(e).__name__}: {str(e)}. Inputs: {args}, {kwargs}\n"
                    f"{error_time} - error time"
                )
                if filename:
                    with open(filename, mode="a", encoding="utf-8") as file:
                        file.write(error_msg)
                else:
                    print(error_msg)
                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator


# @log(filename="mylog.txt")
# def divide(a, b):
#     """Делит a на b"""
#     return a / b
# divide(1, 0)
#
# @log(filename="mylog.txt")
# def my_function(x, y):
#     """Сложение двух чисел"""
#     return x + y
# my_function(1, 2)
