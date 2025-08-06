from typing import Iterator

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
        ),
        (
            "RUB",
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
        ),
    ],
)
def test_filter_by_currency(transactions: list[dict], currency: str, expected: dict) -> Iterator[dict]:
    """ "Тест по возвращению итератора, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD или RUB)"""
    assert next(filter_by_currency(transactions, currency)) == expected
    assert next(filter_by_currency(transactions, currency)) == expected


@pytest.mark.parametrize("expected", ["Перевод организации"])
def test_transaction_description(transactions: list[dict], expected: str) -> Iterator[str]:
    """Тест возвращает описание первой операции"""
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == expected


def test_transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Тест возвращает описание каждой операции по очереди"""
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_card_number_generator() -> str:
    generator = card_number_generator()
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
