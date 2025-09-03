import os

from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.reader import read_transactions_csv, read_transactions_xlsx
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Главная функция программы. Отвечает за взаимодействие с пользователем:
    - загрузка данных из CSV/XLSX/JSON;
    - фильтрация транзакций;
    - вывод отфильтрованных результатов;
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ").strip()

    base_dir = os.path.join(os.path.dirname(__file__), "data")

    if choice == "1":
        file_path = os.path.join(base_dir, "operations.json")
        print("Для обработки выбран JSON-файл.")
        transactions = load_transactions(file_path)
    elif choice == "2":
        file_path = os.path.join(base_dir, "transactions.csv")
        print("Для обработки выбран CSV-файл.")
        transactions = read_transactions_csv(file_path)
    elif choice == "3":
        file_path = os.path.join(base_dir, "transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
        transactions = read_transactions_xlsx(file_path)
    else:
        print("Некорректный выбор. Завершаю работу.")
        return

    if not transactions:
        print("Файл пуст или данные не удалось загрузить.")
        return

    # фильтрация по статусу
    valid_status = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                f"Доступные для фильтровки статусы ({", ".join(valid_status).upper()}):\n"
            )
            .upper()
            .strip()
        )

        if status in valid_status:
            transactions = filter_by_state(transactions, state=status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    if not transactions:
        print("Не найдено ни одной транзакции по выбранному статусу.")
        return

    # Сортировка по дате
    sort_answer = input("Отсортировать операции по дате? Да/Нет:\n").lower().strip()
    if sort_answer == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\n").lower().strip()
        reverse = True if "убыв" in order else False
        transactions = sort_by_date(transactions, sorting=reverse)

    # Фильтрация только рублёвых транзакций
    rub_only = input("Выводить только рублевые транзакции? Да/Нет:\n").lower().strip()
    if rub_only == "да":
        transactions = [
            t for t in transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    # Поиск по слову
    search_answer = input("Отфильтровать список транзакций по слову в описании? Да/Нет:\n").lower().strip()
    if search_answer == "да":
        word = input("Введите слово для поиска в описании: ").strip()
        transactions = process_bank_search(transactions, word)

    # Вывод результата
    print("\nРаспечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for t in transactions:
        # дата в формате 'ДД.ММ.ГГГГ'
        date = get_date(t.get("date", ""))
        # описание
        desc = t.get("description", "")
        # маскированные счета/карты
        from_acc = mask_account_card(t.get("from", "")) if t.get("from") else ""
        to_acc = mask_account_card(t.get("to", "")) if t.get("to") else ""
        # сумма и валюта
        amount = t.get("operationAmount", {}).get("amount", "")
        currency = t.get("operationAmount", {}).get("currency", {}).get("name", "")

        print(f"{date} {desc}")
        if from_acc and to_acc:
            print(f"{from_acc} -> {to_acc}")
        elif from_acc:
            print(from_acc)
        elif to_acc:
            print(to_acc)
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
