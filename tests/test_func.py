import pytest
import json
from src.func import format_amount, card_info, format_date, get_operations, \
    get_executed, json_load
DATA_FILE = "test_json.json"


@pytest.fixture
def test_data():
    """
    Формирование данных для тестирования.
    """
    with open(DATA_FILE, 'r') as json_file:
        return json.load(json_file)


@pytest.fixture
def test_operation(test_data):
    """
    Формирование операции для тестирования.
    """
    return test_data[0]


def test_format_date(test_operation):
    """
    Тестирование функции format_date.

    """
    assert format_date(test_operation) == "08.02.2010 Перевод организации"


def test_format_amount(test_operation):
    """
    Тестирование функции format_amount.

    """
    assert format_amount(test_operation["operationAmount"]) == "62654.30 USD"


def test_card_info():
    """
    Тестирование функции card_info.

    """
    assert card_info("Visa Classic 1203921041964079") == "Visa Classic 1203 92** **** 4079"
    assert card_info("Счет 34616199494072692721") == "Счет **2721"
    assert card_info("Visa Classic 120392001041964079") == "Неизвестный номер"
    assert card_info(None) == "Данные отсутствуют"


def test_get_operations(test_data):
    """
    Тестирование функции get_operations.

    """
    result_list = get_operations(test_data)
    assert len(result_list) == 5
    assert result_list[0]["id"] == 692008409
    assert result_list[-1]["id"] == 636137913


def test_get_executed(test_data):
    """
    Тестирование функции get_executed.

    """
    result_list = get_executed(test_data)
    assert len(result_list) == 5


def test_json_load():
    """
    Тестирование функции json_load

    """
    result_list = json_load(DATA_FILE)
    assert len(result_list) == 6
