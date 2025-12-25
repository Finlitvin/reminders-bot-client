import re
from enum import Enum


class Callbacks(str, Enum):
    SPLIT_SYMBOL = "$"

    BACK = "back"
    LIST_SELECT = "list_select${id}"
    CATEGORY_SELECT = "category_select${id}"
    REMINDER_SELECT = "reminder_select${id}"

    @classmethod
    def list_select(cls, list_id: int) -> str:
        return cls.LIST_SELECT.value.format(id=list_id)

    @classmethod
    def category_select(cls, category_id: int) -> str:
        return cls.CATEGORY_SELECT.value.format(id=category_id)

    @classmethod
    def reminder_select(cls, reminder_id: int) -> str:
        return cls.REMINDER_SELECT.value.format(id=reminder_id)


PATTERNS = {
    "list_select": re.compile(r"^list_select\$(\d+)$"),
    "category_select": re.compile(r"^category_select\$(\d+)$"),
    "reminder_select": re.compile(r"^reminder_select\$(\d+)$"),
}
