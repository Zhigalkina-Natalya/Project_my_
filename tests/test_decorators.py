import pytest

from src.decorators import log


# Тестирование для успешного выполнения функции
def test_log_successful_func():
    """Тест успешного выполнения функции"""

    @log()
    def log_successful_func(a: int, b: int) -> int:
        """Сложение двух чисел"""
        return a + b

    result = log_successful_func(1, 2)
    assert result == 3


def test_log_failing_func():
    """Тестовая функция, которая вызывает ошибку"""

    @log()
    def log_failing_func(a, b):
        raise ValueError("Test error")


# Тестируемая функция с декоратором
@log()
def divide(a: float, b: float) -> float:
    """Делит a на b"""
    return a / b


def test_divide_by_zero() -> None:
    """Проверяем, что деление на 0 вызывает ошибку"""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_log_successful_execution_console(capsys):
    """Тест успешного выполнения с выводом в консоль"""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)
    assert result == 5
    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    output = captured.out
    assert "add ok" in output
    assert "Result: 5" in output
    assert "Execution time:" in output


def test_log_error_handling_console(capsys):
    """Тест обработки ошибки с выводом в консоль"""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    # Проверяем вывод ошибки в консоль
    captured = capsys.readouterr()
    output = captured.out
    assert "divide error:" in output
    assert "ZeroDivisionError" in output
    assert "Inputs: (1, 0)" in output
    assert "- error time" in output
