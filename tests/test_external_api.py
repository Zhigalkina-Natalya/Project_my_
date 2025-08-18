from unittest.mock import Mock, patch

import pytest

from src.external_api import get_transaction_amount_in_rub


def test_get_transaction_amount_in_rub() -> None:
    """Тест если валюта USD, то вызываем API и конвертируем"""
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"result": 5000.0}

    with patch("requests.get", return_value=fake_response) as mock_get:
        result = get_transaction_amount_in_rub(transaction)
        assert result == 5000.0
        # Проверяем, что запрос к API был сделан
        mock_get.assert_called_once()


def test_transaction_in_rub() -> None:
    """Тест если валюта RUB, то возврат суммы без обращения к API"""
    transaction = {"operationAmount": {"amount": 1000, "currency": {"code": "RUB"}}}
    result = get_transaction_amount_in_rub(transaction)
    assert result == 1000.0


def test_transaction_without_amount() -> None:
    """Тест если отсутствует поле amount"""
    transaction = {"operationAmount": {"currency": {"code": "USD"}}}
    with pytest.raises(ValueError, match="В транзакции отсутствует 'amount'"):
        get_transaction_amount_in_rub(transaction)


def test_api_invalid_json() -> None:
    """API вернул JSON без поля result"""
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {}

    with patch("requests.get", return_value=fake_response):
        with pytest.raises(ValueError, match="Некорректный ответ API"):
            get_transaction_amount_in_rub(transaction)


def test_transaction_with_unsupported_currency() -> None:
    """Если валюта не RUB/USD/EUR"""
    transaction = {"operationAmount": {"amount": 10, "currency": {"code": "GBP"}}}
    with pytest.raises(ValueError, match="Конвертация валюты GBP не поддерживается"):
        get_transaction_amount_in_rub(transaction)


def test_api_error_response() -> None:
    """Если API вернул ошибку (например 401)"""
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}

    fake_response = Mock()
    fake_response.status_code = 401
    fake_response.text = "Unauthorized"

    with patch("requests.get", return_value=fake_response):
        with pytest.raises(ConnectionError, match="Ошибка API"):
            get_transaction_amount_in_rub(transaction)
