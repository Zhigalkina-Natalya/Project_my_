import os

import requests
from dotenv import load_dotenv

"""Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
тип данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения
текущего курса валют и конвертации суммы операции в рубли. Для конвертации валюты воспользуйтесь
Exchange Rates Data API:
 https://apilayer.com/exchangerates_data-api. Функцию конвертации поместите в модуль external_api
"""
# загрузка переменных окружения из .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


def get_transaction_amount_in_rub(transaction: dict) -> float:
    """
    Принимает транзакции и возвращает (amount) в рублях. Если транзакция в USD, EUR,
    то происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли
    """
    amount = transaction.get("amount")
    # вариант, если валюта есть, но значение None
    currency = str(transaction.get("currency") or "RUB").strip().upper()
    if amount is None:
        raise ValueError("В транзакции отсутствует 'amount'")
    if currency == "RUB":
        return float(amount)
    if currency not in ["USD", "EUR"]:
        raise ValueError(f"Конвертация валюты {currency} не поддерживается")

    params = {"to": "RUB", "from": currency, "amount": amount}

    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise ConnectionError(f"Ошибка API: {response.text}")

    data = response.json()
    if "result" not in data:
        raise ValueError("Некорректный ответ API: отсутствует поле 'result'")
    return float(data.get("result"))


# if __name__ == "__main__":
#    # Получаем статус-код из ответа и выводим его на экран
#    status_code = response.status_code
#    print(f"Статус код: {status_code}")
#    # Пример использования
#    transactions = [
#        {"amount": 50, "currency": "USD"},
#        {"amount": 100, "currency": "EUR"},
#        {"amount": 5000, "currency": "RUB"}
#    ]

#    for t in transactions:
#        print(f"{t['amount']} {t['currency']} = {get_transaction_amount_in_rub(t)} RUB")
