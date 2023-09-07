from src.func import json_load, get_operations, get_executed,\
    format_date, format_amount, card_info

if __name__ == '__main__':
    filename = '../operatons.json'
    # Загружаем операции из JSON-файла
    operations = json_load(filename)

    # Формирование только выполненных операций
    operations = get_executed(operations)

    # Получение последних 5 выполненных операций
    operations = get_operations(operations)

    # Выводим информацию о каждой из 5 операций
    for operation in operations:

        # Вывод даты и описания операции
        print(format_date(operation))

        # Вывод информации о карте отправителя и получателе
        print(card_info(operation.get("from", None)), "->", operation["to"])

        # Вывод суммы операции и валюты
        print(format_amount(operation["operationAmount"]))

        # Пустая строка для разделения операций
        print()
