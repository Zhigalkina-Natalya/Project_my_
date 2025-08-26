from typing import Any
from unittest.mock import Mock, patch

import pytest

from src.reader import read_transactions_csv, read_transactions_xlsx


@patch("pandas.read_csv")
def test_read_transactions_csv(mock_read_csv: Any) -> None:
    """Тест для чтения CSV - файла"""
    # создаем мок DataFrame
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1, "state": "EXECUTED", "amount": 100}]
    mock_read_csv.return_value = mock_df

    result = read_transactions_csv("data/transactions.csv")

    mock_read_csv.assert_called_once_with("data/transactions.csv", delimiter=";")
    assert result == [{"id": 1, "state": "EXECUTED", "amount": 100}]


@patch("pandas.read_csv", side_effect=FileNotFoundError("File not found"))
def test_read_transactions_csv_file_not_found(mock_read_csv: Any) -> None:
    """Тест, когда файла нет или путь указан неверно"""
    with pytest.raises(FileNotFoundError):
        read_transactions_csv("wrong_path.csv")


@patch("pandas.read_excel")
def test_read_transactions_xlsx(mock_read_excel: Any) -> None:
    """Тест для чтения Excel - файла"""
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 2, "state": "CANCELED", "amount": 200}]
    mock_read_excel.return_value = mock_df

    result = read_transactions_xlsx("data/transactions_excel.xlsx")

    mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx")
    assert result == [{"id": 2, "state": "CANCELED", "amount": 200}]


@patch("pandas.read_excel", side_effect=FileNotFoundError("File not found"))
def test_read_transactions_xlsx_file_not_found(mock_read_excel: Any) -> None:
    """Тест, когда файла нет или путь указан неверно"""
    with pytest.raises(FileNotFoundError):
        read_transactions_xlsx("wrong_path.xlsx")
