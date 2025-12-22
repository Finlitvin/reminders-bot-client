from enum import Enum


class CallbackData(str, Enum):
    MAIN_MENU = "main_menu"

    REMINDER_LIST_SELECT = "reminder_list_{id}"

    @classmethod
    def reminder_list_select(cls, reminder_id: int) -> str:
        return cls.REMINDER_LIST_SELECT.value.format(id=reminder_id)
