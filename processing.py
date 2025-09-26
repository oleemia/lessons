from datetime import datetime


def filter_by_state(data: list, state_value: str = "EXECUTED") -> list:
    """Фильтрует список словарей, возвращая новый список, содержащий только те
    словари, у которых ключ 'state' соответствует указанному значению."""

    filtered_data = [item for item in data if item.get("state") == state_value]
    return filtered_data


def sort_by_date(data: list, reverse: bool = True) -> list:
    """Сортирует список словарей по дате (ключ 'date')."""

    def get_date(item):
        return datetime.fromisoformat(item["date"])

    sorted_data = sorted(data, key=get_date, reverse=reverse)
    return sorted_data
