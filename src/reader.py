from typing import Dict, List

import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict]:
    """Функция считывает финансовые операции из CSV-файлов"""
    df = pd.read_csv(file_path, delimiter=";")
    return df.to_dict(orient="records")


def read_transactions_xlsx(file_path: str) -> List[Dict]:
    """Функция считывает финансовые операции из XLSX-файлов"""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    transactions = read_transactions_csv("data/transactions.csv")
    print(transactions[:3])

    transactions_1 = read_transactions_xlsx("data/transactions_excel.xlsx")
    print(transactions_1[:3])
