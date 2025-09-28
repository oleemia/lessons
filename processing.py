from typing import List, Dict

""" Обработка ключей """


def filter_by_state(
    banking_operations: List[Dict[str, str]], state: str = "EXECUTED"
) -> List[Dict[str, str]]:
    """Функция принимает на вход список словарей с данными о банковских операциях и параметр state,
    возвращает новый список, содержащий только те словари,
     у которых ключ state содержит переданное в функцию значение"""
    return [
        operation for operation in banking_operations if operation.get("state") == state
    ]


""" Сортировка данных """


def sort_by_date(banking_operation: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате"""
    return sorted(banking_operation, key=lambda x: x.get("date"), reverse=reverse)

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Выход функции при стандартных аргументах:
filtered_executed = filter_by_state(operations)
# Выход при передаче 'CANCELED':
filtered_canceled = filter_by_state(operations, 'CANCELED')

# Сортировка всех операций по дате:
sorted_operations = sort_by_date(operations)
