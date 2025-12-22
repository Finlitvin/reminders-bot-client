from enum import Enum


class CallbackData(str, Enum):
    SPLIT_SYMBOL = "$"

    BACK = "back"
    REMINDER_LIST_SELECT = "reminder_list${id}"
    SECTION_LIST_SELECT = "section_list${id}"

    @classmethod
    def split_symbol(cls, data: str) -> str:
        return data.split(cls.SPLIT_SYMBOL.value)[0]

    @classmethod
    def reminder_list_select(cls, reminder_id: int) -> str:
        return cls.REMINDER_LIST_SELECT.value.format(id=reminder_id)

    @classmethod
    def section_list_select(cls, section_id: int) -> str:
        return cls.SECTION_LIST_SELECT.value.format(id=section_id)
