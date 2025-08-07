from typing import Iterable

from black import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterable:
    """
    Функция, возвращающая итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


# usd_transactions = filter_by_currency(transactions, "USD")
# for transactions in range(2):
#     print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]) -> Iterable:
    """Генератор, принимающий список словаре с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description")


# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Iterator:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    for num in range(start, end):
        if num <= 16:
            gen_num = "0" * (16 - len(str(num))) + str(num)
            card_number = gen_num[:4] + " " + gen_num[4:8] + " " + gen_num[9:13] + " " + gen_num[-4:]
            yield card_number


# for card_number in card_number_generator(1, 5):
#     print(card_number)
