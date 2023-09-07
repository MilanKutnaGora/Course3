import json

import datetime


def json_load(file_name):
    """
        Загрузка данных по операциям из JSON-файла.
    """

    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data



def format_date(operation):
    """
        Форматирование даты операции в строку".
    """
    date = datetime.datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f")
    description = operation['description']

    return f"{date.strftime('%d.%m.%Y')} {description}"


def format_amount(operation):
    """
        Форматирование суммы операции и валюту в строку.
    """
    return operation["amount"] + " " + operation["currency"]["name"]


def card_info(card_string):
    """
        Формирование информации о карте
    """
    if card_string is None:
        return "Данные отсутствуют"
    card_parts = card_string.split()
    account_number = card_parts[-1]
    name = " ".join(card_parts[:-1])

    if len(account_number) == 16:
        return f"{name} {account_number[:4]} {account_number[4:6]}** **** {account_number[-4:]}"
    elif len(account_number) == 20:
        return f"{name} **{account_number[-4:]}"
    else:
        return "Неизвестный номер"


def get_operations(operations):
    """
        Формирование списка из пяти последних операций.
    """
    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations[:5]


def get_executed(operations):
    """
        Формирование списка выполненых операций

    """
    return [operation for operation in operations if operation and operation["state"] == "EXECUTED"]