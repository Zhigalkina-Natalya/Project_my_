import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("type_number, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                   ("Счет 64686473678894779589", "Счет **9589"),
                                                   ("Visa Classic 6831982476737658",
                                                    "Visa Classic 6831 98** **** 7658"),
                                                   ("MasterCard 7158300734726758",
                                                    "MasterCard 7158 30** **** 6758"),
                                                   ("", ""),
                                                   ])
def test_mask_account_card(type_number, expected):
    assert mask_account_card(type_number) == expected


def test_mask_account(type_number_account):
    assert mask_account_card(type_number_account) == "Счет **9589"


def test_mask_card(type_number_card):
    assert mask_account_card(type_number_card) == "Visa Classic 6831 98** **** 7658"


@pytest.mark.parametrize("type_number", [("Счет 1596837868705199123"),
                                         ("Счет 646864736788947795891"),
                                         ("Visa Classic 6831982476737"),
                                         ("MasterCard 715830073472675811")
                                         ])
def test_mask_account_card_invalid(type_number):
    with pytest.raises(ValueError):
        mask_account_card(type_number)


@pytest.mark.parametrize("date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                            ("2024-03-11T02:26:18", "11.03.2024"),
                                            ("2024-03-11T00:00:00", "11.03.2024"),
                                            ("2024-12-31T23:59:59.999999", "31.12.2024"),
                                            ("", "")
                                            ])
def test_get_date_and_empty(date, expected):
    assert get_date(date) == expected


def test_get_date(date):
    assert get_date(date) == "11.03.2024"


@pytest.mark.parametrize("date", [("T23:59:59.999999"),
                                  ("12,31,2024"),
                                  ("1111бю.11.11T")
                                  ])
def test_get_date_invalid(date):
    with pytest.raises(IndexError):
        get_date(date)
