import re
from collections import Counter
from typing import Any

from src.widget import get_date


def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция возвращает новый список словарей, содержащий словари, у которых ключ state
    соответствует указанному значению
    """
    new_list = []
    for i in list_of_dict:
        if i.get("state") == state:
            new_list.append(i)
        else:
            continue
    return new_list


def sort_by_date(list_of_dict: list[dict], sorting: bool = True) -> list[dict[str, Any]]:
    """
    Функция возвращает новый список словарей, отсортированный по дате
    """
    if not isinstance(list_of_dict, list):
        raise TypeError("Ожидается список словарей")

    # Проверяем наличие ключа date
    processed = []
    for idx, transaction in enumerate(list_of_dict):
        if "date" not in transaction:
            raise KeyError(f"Словарь №{idx} не содержит ключа 'date'")

        try:
            dt = get_date(transaction["date"])
            processed.append((dt, transaction))
        except ValueError as e:
            raise ValueError(f"Ошибка в словаре №{idx}: {str(e)}")

    # Сортируем по dt объектам
    processed.sort(key=lambda x: x[0], reverse=sorting)
    # Возвращаем только исходные словари (без dt объектов)
    list_interval = [i[1] for i in processed]
    # Сортируем по датам исходные словари
    list_sorted = sorted(list_interval, key=lambda x: x["date"], reverse=sorting)
    return list_sorted


def process_bank_search(list_of_dict: list[dict], search: str) -> list[dict]:
    """
    Функция, принимающая список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, которые содержат строку поиска.
    """
    if not isinstance(list_of_dict, list):
        raise TypeError("Ожидается список словарей")
    if not isinstance(search, str):
        raise TypeError("Ожидается строка для поиска")

    result = []
    pattern = re.compile(search, re.IGNORECASE)

    for idx, transaction in enumerate(list_of_dict):
        if not isinstance(transaction, dict):
            raise TypeError(f"Элемент под индексом {idx} не является словарем")

        description = transaction.get("description", "")
        if not isinstance(description, str):
            continue
        if pattern.search(description):
            result.append(transaction)
    return result


def process_bank_operations(list_of_dict: list[dict], categories: list) -> dict[str, int]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращаeт словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории. Категории операций хранятся в поле description
    """
    if not isinstance(list_of_dict, list):
        raise TypeError("Ожидается список словарей")
    if not isinstance(categories, list):
        raise TypeError("Ожидается список категорий")

    descriptions = [
        transaction.get("description", "") for transaction in list_of_dict if isinstance(transaction, dict)
    ]
    counter = Counter(descriptions)

    result = {}
    for category in categories:
        if not isinstance(category, str):
            raise TypeError("Категории должны быть строками")
        result[category] = counter.get(category, 0)

    return result
