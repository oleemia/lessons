from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(card_info: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты
    возвращает строку с замаскированным номером."""
    card_type, card_number = card_info.rsplit(sep=" ", maxsplit=1)

    if card_type in ["Visa Platinum", "Maestro"]:
        if len(card_number) == 16:
            return f"{card_type} {get_mask_card_number(card_number)}"
        return "Некорректный ввод"
    elif card_type == "Счет":
        return f"{card_type} {get_mask_account(card_number)}"
    else:
        return "Некорректный ввод"


def get_date(date_str: str) -> str:
    try:
        date_obj = datetime.fromisoformat(date_str)
        formatted_date = date_obj.strftime("%d.%m.%Y")
        return formatted_date
    except ValueError:
        return "Некорректный формат даты"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 690224245640522800"))
