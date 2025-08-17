import json
from unittest.mock import mock_open, patch

from src.utils import load_transactions


def test_no_file() -> None:
    """Тест на отсутствие файла"""
    with patch("os.path.exists", return_value=False):
        assert load_transactions("no_file.json") == []


def test_empty_file() -> None:
    """Тест является ли файл пустым."""
    with patch("os.path.exists", return_value=True), patch("os.path.getsize", return_value=0):
        result = load_transactions("file.json")
        assert result == []


def test_valid_file() -> None:
    """Тест с существующим файлом с корректным JSON"""
    # Наш "корректный" список транзакций
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    # Мокаем open, чтобы он возвращал наш JSON
    m = mock_open(read_data=json.dumps(data))

    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.getsize", return_value=10),
        patch("builtins.open", m),
    ):
        result = load_transactions("any_file.json")

    assert result == data


def test_json_not_list() -> None:
    """Тест на отсутствие в фале .json списка"""
    data = {"key": "value"}
    m = mock_open(read_data=json.dumps(data))
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.getsize", return_value=10),
        patch("builtins.open", m),
    ):
        result = load_transactions("any_file.json")
        assert result == []


def test_invalid_json() -> None:
    """Тест на битый JSON (json.JSONDecodeError)"""
    m = mock_open(read_data="{")  # некорректный JSON
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.getsize", return_value=10),
        patch("builtins.open", m),
    ):
        result = load_transactions("any_file.json")

    assert result == []
