import pytest


@pytest.fixture
def list_of_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]


@pytest.fixture
def card_number():
    return "1111222233334444"


@pytest.fixture
def card_number_symbol():
    return "*1111.2222_3333*4444"


@pytest.fixture
def number_account():
    return "11112222333344445555"


@pytest.fixture
def type_number_account():
    return "Счет 64686473678894779589"


@pytest.fixture
def type_number_card():
    return "Visa Classic 6831982476737658"


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"
