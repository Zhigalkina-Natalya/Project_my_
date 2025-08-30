import os

import requests
from dotenv import load_dotenv

# загрузка переменных окружения из .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


def get_transaction_amount_in_rub(transaction: dict) -> float:
    """
    Принимает транзакции и возвращает (amount) в рублях. Если транзакция в USD, EUR,
    то происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли
    """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    if amount is None:
        raise ValueError("В транзакции отсутствует 'amount'")
    if not currency:
        raise ValueError("В транзакции отсутствует 'currency'")

    currency = str(currency).strip().upper()
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
